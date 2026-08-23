#!/usr/bin/env python3
"""
disassemble_rva_functions.py
Extracts the exact x64 assembly instructions for every Wrraper_MSDisplay function RVA
from MSDISPLAYSDKWRRAPER_disasm.asm.
"""

import os
import sys
import json
import re

RVA_MAP = {
    "Wrraper_MSDisplayStart": "180014700",
    "Wrraper_MSDisplayStop": "180014710",
    "Wrraper_MSDisplayRegisterCallback": "1800147c0",
    "Wrraper_MSDisplayGetSDKVersion": "1800147d0",
    "Wrraper_MSDisplayGetDeviceList": "1800147f0",
    "Wrraper_MSDisplayGetDeviceInfo": "180014880",
    "Wrraper_MSDisplaySetVideoParam": "1800148a0",
    "Wrraper_MSDisplaySendPicture": "180014a70",
    "Wrraper_MSDisplayReadXdata": "180014ab0",
    "Wrraper_MSDisplayReadFlash": "180014bb0",
    "Wrraper_MSDisplayReadEEPROM": "180014cb0",
    "Wrraper_MSDisplayWriteXdata": "180014db0",
    "Wrraper_MSDisplayWriteFlash": "180014ea0",
    "Wrraper_MSDisplayWriteEEPROM": "180014f90",
    "Wrraper_MSDisplayFlashErase": "180015080",
    "Wrraper_MSDisplayInitFlashGpio": "1800150a0",
    "Wrraper_MSDisplayReadSN": "180015160",
    "Wrraper_MSDisplayPause": "1800152e0",
    "Wrraper_MSDisplayResume": "1800153a0",
    "Wrraper_MSDisplayEnableSDKScreenProcessor": "180015460",
    "Wrraper_MSDisplayCheckDeviceScreenCapability": "180015480",
    "Wrraper_MSDisplayGetDriverVersion": "1800154e0"
}

ASM_PATH = "/home/tor/pc-case-lcd/init_investigation/MSDISPLAYSDKWRRAPER_disasm.asm"
OUT_DIR = "/home/tor/pc-case-lcd/init_investigation"

def main():
    if not os.path.exists(ASM_PATH):
        print(f"Error: {ASM_PATH} not found.")
        return

    print("Reading disassembly...")
    with open(ASM_PATH, "r", encoding="utf-8", errors="ignore") as f:
        lines = f.read().splitlines()

    print(f"Loaded {len(lines)} lines of disassembly.")

    # Index lines by hex address
    addr_line_map = {}
    for idx, l in enumerate(lines):
        m = re.match(r"^\s*([0-9a-fA-F]+):", l)
        if m:
            addr_hex = m.group(1).lower()
            addr_line_map[addr_hex] = idx

    extracted = {}

    for func_name, addr_hex in RVA_MAP.items():
        if addr_hex in addr_line_map:
            line_num = addr_line_map[addr_hex]
            # Read next 100 instructions
            func_asm = lines[line_num:line_num+100]
            extracted[func_name] = {
                "address": f"0x{addr_hex}",
                "line_start": line_num + 1,
                "assembly": func_asm
            }
            print(f"  Extracted {func_name} @ 0x{addr_hex} (line {line_num+1})")
        else:
            print(f"  WARNING: Address 0x{addr_hex} not found for {func_name}")

    out_file = os.path.join(OUT_DIR, "msdisplay_rva_functions_disasm.json")
    with open(out_file, "w") as f:
        json.dump(extracted, f, indent=2)

    out_md = os.path.join(OUT_DIR, "msdisplay_rva_functions_disasm.md")
    with open(out_md, "w") as f:
        f.write("# MSDISPLAYSDKWRRAPER.dll Native Exports Assembly Disassembly\n\n")
        for func_name, data in extracted.items():
            f.write(f"## `{func_name}` (Address: `{data['address']}`)\n")
            f.write("```assembly\n")
            for al in data["assembly"]:
                f.write(f"{al}\n")
            f.write("```\n\n")

    print(f"\nSaved RVA disassembly to {out_file} and {out_md}")

if __name__ == "__main__":
    main()
