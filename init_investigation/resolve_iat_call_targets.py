#!/usr/bin/env python3
"""
resolve_iat_call_targets.py
Maps IAT RVAs to imported function names and finds all indirect call/jmp sites
in MSDISPLAYSDKWRRAPER_disasm.asm targeting libusb0.dll, SETUPAPI.dll, and KERNEL32.dll.
"""

import os
import sys
import struct
import json
import re

DLL_PATH = "/home/tor/vmax_bundle/dll/x64/MSDISPLAYSDKWRRAPER.dll"
ASM_PATH = "/home/tor/pc-case-lcd/init_investigation/MSDISPLAYSDKWRRAPER_disasm.asm"
OUT_DIR = "/home/tor/pc-case-lcd/init_investigation"

def parse_iat_mapping(filepath):
    with open(filepath, "rb") as f:
        data = f.read()

    e_lfanew = struct.unpack_from("<I", data, 0x3C)[0]
    coff_offset = e_lfanew + 4
    num_sections = struct.unpack_from("<H", data, coff_offset + 2)[0]
    opt_header_size = struct.unpack_from("<H", data, coff_offset + 16)[0]
    opt_header_offset = coff_offset + 20
    magic = struct.unpack_from("<H", data, opt_header_offset)[0]
    is_64 = (magic == 0x20B)
    image_base = struct.unpack_from("<Q" if is_64 else "<I", data, opt_header_offset + 24)[0]

    # Import Directory is DataDirectory[1]
    import_dir_rva = struct.unpack_from("<I", data, opt_header_offset + (120 if is_64 else 104))[0]
    
    # Section Headers
    section_headers_offset = opt_header_offset + opt_header_size
    sections = []
    for i in range(num_sections):
        s_off = section_headers_offset + (i * 40)
        s_name = data[s_off:s_off+8].rstrip(b'\x00').decode('ascii', errors='ignore')
        s_vsize, s_rva, s_raw_size, s_raw_ptr = struct.unpack_from("<IIII", data, s_off + 8)
        sections.append({"name": s_name, "rva": s_rva, "vsize": s_vsize, "raw_ptr": s_raw_ptr})

    def rva_to_ptr(rva):
        for s in sections:
            if s["rva"] <= rva < s["rva"] + s["vsize"]:
                return s["raw_ptr"] + (rva - s["rva"])
        return None

    iat_map = {} # VA -> (dll_name, func_name)

    if import_dir_rva:
        imp_ptr = rva_to_ptr(import_dir_rva)
        if imp_ptr:
            cur = imp_ptr
            while True:
                original_first_thunk, time_stamp, forwarder_chain, name_rva, first_thunk = struct.unpack_from("<IIIII", data, cur)
                if name_rva == 0:
                    break

                dll_name_ptr = rva_to_ptr(name_rva)
                dll_name = "UNKNOWN"
                if dll_name_ptr:
                    n_end = data.find(b'\x00', dll_name_ptr)
                    if n_end != -1:
                        dll_name = data[dll_name_ptr:n_end].decode('ascii', errors='ignore')

                # IAT is at first_thunk RVA
                iat_rva = first_thunk
                thunk_rva = original_first_thunk if original_first_thunk != 0 else first_thunk

                thunk_ptr = rva_to_ptr(thunk_rva)
                iat_entry_ptr = rva_to_ptr(iat_rva)

                if thunk_ptr and iat_entry_ptr:
                    t_cur = thunk_ptr
                    i_rva_cur = iat_rva
                    while True:
                        val = struct.unpack_from("<Q" if is_64 else "<I", data, t_cur)[0]
                        t_cur += 8 if is_64 else 4

                        if val == 0:
                            break

                        entry_va = image_base + i_rva_cur
                        i_rva_cur += 8 if is_64 else 4

                        is_ordinal = (val & (0x8000000000000000 if is_64 else 0x80000000)) != 0
                        if is_ordinal:
                            fn_name = f"Ordinal_{val & 0xFFFF}"
                        else:
                            hint_name_rva = val & 0x7FFFFFFF
                            hint_name_ptr = rva_to_ptr(hint_name_rva)
                            fn_name = "UNKNOWN"
                            if hint_name_ptr:
                                fn_end = data.find(b'\x00', hint_name_ptr + 2)
                                if fn_end != -1:
                                    fn_name = data[hint_name_ptr+2:fn_end].decode('ascii', errors='ignore')

                        iat_map[f"0x{entry_va:x}"] = f"{dll_name}!{fn_name}"

                cur += 20

    return iat_map

def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    iat_map = parse_iat_mapping(DLL_PATH)

    print(f"Mapped {len(iat_map)} IAT addresses.")

    with open(ASM_PATH, "r", encoding="utf-8", errors="ignore") as f:
        asm_lines = f.read().splitlines()

    resolved_calls = []

    for idx, line in enumerate(asm_lines):
        # Match indirect call/jmp: callq *offset(%rip) # 0x1800...
        m = re.search(r"(callq?|jmpq?)\s+\*0x[0-9a-fA-F]+\(%rip\)\s+#\s+(0x[0-9a-fA-F]+)", line)
        if m:
            inst = m.group(1)
            target_va = m.group(2).lower()
            if target_va in iat_map:
                target_name = iat_map[target_va]
                # Capture 15 lines context before call site
                context = asm_lines[max(0, idx-15):min(len(asm_lines), idx+5)]
                resolved_calls.append({
                    "line_num": idx + 1,
                    "instruction": inst,
                    "target_va": target_va,
                    "imported_func": target_name,
                    "line_text": line.strip(),
                    "context": context
                })

    out_file = os.path.join(OUT_DIR, "resolved_iat_call_sites.json")
    with open(out_file, "w") as f:
        json.dump(resolved_calls, f, indent=2)

    out_md = os.path.join(OUT_DIR, "resolved_iat_call_sites.md")
    with open(out_md, "w") as f:
        f.write("# Resolved Indirect IAT Call Sites in MSDISPLAYSDKWRRAPER.dll\n\n")
        f.write(f"Total indirect IAT call sites resolved: `{len(resolved_calls)}`\n\n")

        # Group by imported_func
        by_func = {}
        for rc in resolved_calls:
            fn = rc["imported_func"]
            if fn not in by_func:
                by_func[fn] = []
            by_func[fn].append(rc)

        for fn, call_list in sorted(by_func.items()):
            f.write(f"## `{fn}` ({len(call_list)} Call Sites)\n\n")
            for cs in call_list:
                f.write(f"### Line {cs['line_num']} (Address `{cs['target_va']}`)\n")
                f.write("```assembly\n")
                for cl in cs["context"]:
                    f.write(f"{cl}\n")
                f.write("```\n\n")

    print(f"Resolved {len(resolved_calls)} indirect IAT calls!")
    print(f"Saved results to {out_file} and {out_md}")

if __name__ == "__main__":
    main()
