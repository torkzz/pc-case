#!/usr/bin/env python3
"""
analyze_msdisplay_disassembly.py
Analyzes the native x64 assembly disassembly of MSDISPLAYSDKWRRAPER.dll
Targeting:
1. Device discovery & enumeration in Wrraper_MSDisplayGetDeviceList
2. Device open & WinUSB / libusb0 initialization in Wrraper_MSDisplayStart
3. Frame construction & TurboJPEG compression in Wrraper_MSDisplaySendPicture
4. Screen capability checks in Wrraper_MSDisplayCheckDeviceScreenCapability
"""

import os
import sys
import json
import re

ASM_PATH = "/home/tor/pc-case-lcd/init_investigation/MSDISPLAYSDKWRRAPER_disasm.asm"
OUT_DIR = "/home/tor/pc-case-lcd/init_investigation"

def parse_function_blocks(asm_text):
    lines = asm_text.splitlines()
    funcs = {}
    cur_func = None
    cur_lines = []

    for line in lines:
        m = re.match(r"^[0-9a-fA-F]+\s+<([^>]+)>:", line)
        if m:
            if cur_func:
                funcs[cur_func] = cur_lines
            cur_func = m.group(1)
            cur_lines = [line]
        elif cur_func:
            cur_lines.append(line)

    if cur_func:
        funcs[cur_func] = cur_lines

    return funcs

def analyze_function(func_name, lines):
    text = "\n".join(lines)
    
    # Calls to other functions / imports
    calls = re.findall(r"callq?\s+([^\n]+)", text)
    # String references (lea rcx, [rip+0x...])
    leas = re.findall(r"lea\s+([^\n]+)", text)
    # Movs/Immediates
    movs = re.findall(r"mov\s+([^\n]+)", text)

    return {
        "line_count": len(lines),
        "calls": sorted(list(set(calls[:30]))),
        "sample_lines": lines[:60]
    }

def main():
    if not os.path.exists(ASM_PATH):
        print(f"Error: {ASM_PATH} not found.")
        return

    print("Reading MSDISPLAYSDKWRRAPER_disasm.asm...")
    with open(ASM_PATH, "r", encoding="utf-8", errors="ignore") as f:
        asm_text = f.read()

    funcs = parse_function_blocks(asm_text)
    print(f"Parsed {len(funcs)} functions from assembly disassembly.")

    target_names = [
        "Wrraper_MSDisplayGetDeviceList",
        "Wrraper_MSDisplayStart",
        "Wrraper_MSDisplayEnableSDKScreenProcessor",
        "Wrraper_MSDisplaySendPicture",
        "Wrraper_MSDisplayGetDeviceInfo",
        "Wrraper_MSDisplayCheckDeviceScreenCapability",
        "Wrraper_MSDisplaySetVideoParam",
        "Wrraper_MSDisplayStop",
        "Wrraper_MSDisplayReadSN",
        "Wrraper_MSDisplayReadFlash"
    ]

    analysis = {}
    for name in target_names:
        # Find exact or matching function names
        matching = [k for k in funcs.keys() if name in k]
        for m in matching:
            analysis[m] = analyze_function(m, funcs[m])

    out_file = os.path.join(OUT_DIR, "msdisplay_assembly_analysis.json")
    with open(out_file, "w") as f:
        json.dump(analysis, f, indent=2)

    print(f"Saved function analysis to {out_file}")

if __name__ == "__main__":
    main()
