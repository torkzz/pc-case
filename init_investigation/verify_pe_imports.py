#!/usr/bin/env python3
"""
verify_pe_imports.py
Directly parses the PE Import Directory & Import Name Table / Import Address Table
of MSDISPLAYSDKWRRAPER.dll to verify every imported function name from every DLL.
"""

import os
import struct
import json

DLL_PATH = "/home/tor/vmax_bundle/dll/x64/MSDISPLAYSDKWRRAPER.dll"

def parse_pe_imports(filepath):
    with open(filepath, "rb") as f:
        data = f.read()

    if data[:2] != b'MZ':
        return {"error": "Not a valid PE file"}

    e_lfanew = struct.unpack_from("<I", data, 0x3C)[0]
    pe_sig = data[e_lfanew:e_lfanew+4]
    if pe_sig != b'PE\x00\x00':
        return {"error": "Invalid PE signature"}

    coff_offset = e_lfanew + 4
    num_sections = struct.unpack_from("<H", data, coff_offset + 2)[0]
    opt_header_size = struct.unpack_from("<H", data, coff_offset + 16)[0]
    opt_header_offset = coff_offset + 20
    magic = struct.unpack_from("<H", data, opt_header_offset)[0]
    is_64 = (magic == 0x20B)

    # Import Directory is DataDirectory[1]
    import_dir_rva = struct.unpack_from("<I", data, opt_header_offset + (120 if is_64 else 104))[0]
    import_dir_size = struct.unpack_from("<I", data, opt_header_offset + (124 if is_64 else 108))[0]

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

    imports = {}
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

                # INT (Import Name Table) or IAT
                thunk_rva = original_first_thunk if original_first_thunk != 0 else first_thunk
                thunk_ptr = rva_to_ptr(thunk_rva)

                func_names = []
                if thunk_ptr:
                    t_cur = thunk_ptr
                    while True:
                        if is_64:
                            val = struct.unpack_from("<Q", data, t_cur)[0]
                            t_cur += 8
                        else:
                            val = struct.unpack_from("<I", data, t_cur)[0]
                            t_cur += 4

                        if val == 0:
                            break

                        # Check ordinal vs name (bit 63 for 64-bit)
                        is_ordinal = (val & (0x8000000000000000 if is_64 else 0x80000000)) != 0
                        if is_ordinal:
                            ordinal = val & 0xFFFF
                            func_names.append(f"Ordinal_{ordinal}")
                        else:
                            hint_name_rva = val & 0x7FFFFFFF
                            hint_name_ptr = rva_to_ptr(hint_name_rva)
                            if hint_name_ptr:
                                hint = struct.unpack_from("<H", data, hint_name_ptr)[0]
                                fn_end = data.find(b'\x00', hint_name_ptr + 2)
                                if fn_end != -1:
                                    fn_name = data[hint_name_ptr+2:fn_end].decode('ascii', errors='ignore')
                                    func_names.append(fn_name)

                imports[dll_name] = func_names
                cur += 20

    return imports

def main():
    imports = parse_pe_imports(DLL_PATH)
    out_file = "/home/tor/pc-case-lcd/init_investigation/verified_pe_imports.json"
    with open(out_file, "w") as f:
        json.dump(imports, f, indent=2)

    print("=" * 70)
    print("VERIFIED PE IMPORT TABLE OF MSDISPLAYSDKWRRAPER.DLL")
    print("=" * 70)
    for dll, funcs in imports.items():
        print(f"\nDLL: {dll} ({len(funcs)} functions imported)")
        for fn in funcs:
            print(f"  - {fn}")

if __name__ == "__main__":
    main()
