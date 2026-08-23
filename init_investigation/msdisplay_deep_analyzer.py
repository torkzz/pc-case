#!/usr/bin/env python3
"""
msdisplay_deep_analyzer.py
Exhaustive dissection of MSDisplay native libraries and INF files.

Targets:
- MSDISPLAYSDKWRRAPER.dll
- libstack.dll
- libcompositeScreenModel.dll
- MSUSBDisplay.inf
"""

import os
import sys
import re
import struct
import json

BUNDLE_DIR = "/home/tor/vmax_bundle"
RELEASE_DIR = os.path.join(BUNDLE_DIR, "bin/Release")
INF_FILE = os.path.join(BUNDLE_DIR, "libusb/MSUSBDisplay.inf")
OUT_DIR = "/home/tor/pc-case-lcd/init_investigation"

TARGET_DLLS = [
    os.path.join(RELEASE_DIR, "MSDISPLAYSDKWRRAPER.dll"),
    os.path.join(RELEASE_DIR, "libstack.dll"),
    os.path.join(RELEASE_DIR, "libcompositeScreenModel.dll"),
    os.path.join(BUNDLE_DIR, "dll/x64/MSDISPLAYSDKWRRAPER.dll")
]

def extract_strings_with_offsets(filepath):
    if not os.path.exists(filepath):
        return []
    with open(filepath, "rb") as f:
        data = f.read()

    results = []
    # ASCII
    for m in re.finditer(rb"[\x20-\x7e]{4,}", data):
        try:
            results.append({"offset": hex(m.start()), "type": "ascii", "str": m.group(0).decode('ascii')})
        except:
            pass
    # UTF-16LE
    for m in re.finditer(rb"(?:[\x20-\x7e]\x00){4,}", data):
        try:
            results.append({"offset": hex(m.start()), "type": "utf16", "str": m.group(0).decode('utf-16le')})
        except:
            pass
    return results

def parse_inf(filepath):
    if not os.path.exists(filepath):
        return {}
    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    hw_ids = re.findall(r"USB\\VID_[0-9A-Fa-f]{4}&PID_[0-9A-Fa-f]{4}[^\s\n]*", content)
    guids = re.findall(r"\{[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{12}\}", content)
    services = re.findall(r"ServiceBinary\s*=\s*[^\n]+", content, re.IGNORECASE)

    return {
        "hardware_ids": sorted(list(set(hw_ids))),
        "guids": sorted(list(set(guids))),
        "services": services
    }

def scan_pe_exports_imports(filepath):
    if not os.path.exists(filepath):
        return {}
    with open(filepath, "rb") as f:
        data = f.read()

    if data[:2] != b'MZ':
        return {}

    e_lfanew = struct.unpack_from("<I", data, 0x3C)[0]
    coff_offset = e_lfanew + 4
    num_sections = struct.unpack_from("<H", data, coff_offset + 2)[0]
    opt_header_size = struct.unpack_from("<H", data, coff_offset + 16)[0]
    opt_header_offset = coff_offset + 20
    magic = struct.unpack_from("<H", data, opt_header_offset)[0]
    is_64 = (magic == 0x20B)

    export_dir_rva = struct.unpack_from("<I", data, opt_header_offset + (112 if is_64 else 96))[0]
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

    exports = []
    if export_dir_rva:
        exp_ptr = rva_to_ptr(export_dir_rva)
        if exp_ptr:
            num_names = struct.unpack_from("<I", data, exp_ptr + 24)[0]
            names_rva = struct.unpack_from("<I", data, exp_ptr + 32)[0]
            names_ptr = rva_to_ptr(names_rva)
            if names_ptr:
                for i in range(num_names):
                    n_rva = struct.unpack_from("<I", data, names_ptr + (i * 4))[0]
                    n_ptr = rva_to_ptr(n_rva)
                    if n_ptr:
                        n_end = data.find(b'\x00', n_ptr)
                        if n_end != -1:
                            exports.append(data[n_ptr:n_end].decode('ascii', errors='ignore'))

    imports = []
    if import_dir_rva:
        imp_ptr = rva_to_ptr(import_dir_rva)
        if imp_ptr:
            cur = imp_ptr
            while True:
                name_rva = struct.unpack_from("<I", data, cur + 12)[0]
                if name_rva == 0:
                    break
                name_ptr = rva_to_ptr(name_rva)
                if name_ptr:
                    n_end = data.find(b'\x00', name_ptr)
                    if n_end != -1:
                        imports.append(data[name_ptr:n_end].decode('ascii', errors='ignore'))
                cur += 20

    return {"exports": sorted(exports), "imported_dlls": sorted(imports)}

def main():
    os.makedirs(OUT_DIR, exist_ok=True)

    print("=== PARSING MSUSBDisplay.inf ===")
    inf_data = parse_inf(INF_FILE)
    print("  Hardware IDs:", inf_data.get("hardware_ids"))
    print("  GUIDs:", inf_data.get("guids"))
    print("  Services:", inf_data.get("services"))

    dll_analysis = {}
    for dll_path in TARGET_DLLS:
        fname = os.path.basename(dll_path)
        if not os.path.exists(dll_path):
            continue
        print(f"\n=== ANALYZING {fname} ({dll_path}) ===")
        pe_info = scan_pe_exports_imports(dll_path)
        strings = extract_strings_with_offsets(dll_path)

        relevant_strings = [
            s for s in strings
            if any(k in s["str"].lower() for k in [
                "display", "winusb", "idd", "deviceio", "createfile", "setupdi",
                "wrraper", "picture", "screen", "capab", "video", "param", "sn",
                "flash", "eeprom", "xdata", "ms", "bulk", "timeout", "chip_id",
                "jpeg", "yuv", "scale", "345f", "9132"
            ])
        ]

        dll_analysis[fname] = {
            "path": dll_path,
            "exports": pe_info.get("exports", []),
            "imported_dlls": pe_info.get("imported_dlls", []),
            "relevant_strings_count": len(relevant_strings),
            "relevant_strings": relevant_strings
        }
        print(f"  Exports ({len(pe_info.get('exports', []))}):", pe_info.get("exports", []))
        print(f"  Imported DLLs:", pe_info.get("imported_dlls", []))
        print(f"  Relevant Strings: {len(relevant_strings)}")

    out_file = os.path.join(OUT_DIR, "msdisplay_native_dissection.json")
    with open(out_file, "w") as f:
        json.dump({"inf_data": inf_data, "dll_analysis": dll_analysis}, f, indent=2)

    print(f"\nSaved analysis to {out_file}")

if __name__ == "__main__":
    main()
