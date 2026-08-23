#!/usr/bin/env python3
"""
disassemble_msdisplay_wrapper.py
Disassembles x64 MSDISPLAYSDKWRRAPER.dll exports using objdump and gdb/llvm-objdump
Target functions:
- Wrraper_MSDisplayGetDeviceList
- Wrraper_MSDisplayStart
- Wrraper_MSDisplayEnableSDKScreenProcessor
- Wrraper_MSDisplaySendPicture
- Wrraper_MSDisplayGetDeviceInfo
- Wrraper_MSDisplayCheckDeviceScreenCapability
- Wrraper_MSDisplaySetVideoParam
"""

import os
import sys
import subprocess
import json
import re

DLL_PATH = "/home/tor/vmax_bundle/dll/x64/MSDISPLAYSDKWRRAPER.dll"
OUT_DIR = "/home/tor/pc-case-lcd/init_investigation"

TARGET_EXPORTS = [
    "Wrraper_MSDisplayGetDeviceList",
    "Wrraper_MSDisplayStart",
    "Wrraper_MSDisplayEnableSDKScreenProcessor",
    "Wrraper_MSDisplaySendPicture",
    "Wrraper_MSDisplayGetDeviceInfo",
    "Wrraper_MSDisplayCheckDeviceScreenCapability",
    "Wrraper_MSDisplaySetVideoParam",
    "Wrraper_MSDisplayReadSN",
    "Wrraper_MSDisplayReadFlash"
]

def disassemble_dll():
    try:
        res = subprocess.run(["objdump", "-d", DLL_PATH], capture_output=True, text=True, check=True)
        return res.stdout
    except Exception as e:
        print(f"objdump error: {e}")
        try:
            res = subprocess.run(["llvm-objdump", "-d", DLL_PATH], capture_output=True, text=True, check=True)
            return res.stdout
        except Exception as e2:
            print(f"llvm-objdump error: {e2}")
            return ""

def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    print("=" * 70)
    print("DISASSEMBLING MSDISPLAYSDKWRRAPER.DLL NATIVE EXPORTS")
    print("=" * 70)

    disasm = disassemble_dll()
    if not disasm:
        print("Failed to disassemble DLL.")
        return

    print(f"Disassembly length: {len(disasm)} characters ({len(disasm.splitlines())} lines)")

    # Save full disassembly
    full_asm_path = os.path.join(OUT_DIR, "MSDISPLAYSDKWRRAPER_disasm.asm")
    with open(full_asm_path, "w") as f:
        f.write(disasm)
    print(f"Saved full disassembly to {full_asm_path}")

    # Extract target function blocks
    extracted_funcs = {}
    lines = disasm.splitlines()

    for func in TARGET_EXPORTS:
        func_lines = []
        recording = False
        for line in lines:
            if func in line and "<" in line and ">:" in line:
                recording = True
                func_lines.append(line)
                continue
            if recording:
                if line.strip().endswith(">:") and "<" in line:
                    break
                func_lines.append(line)

        if func_lines:
            extracted_funcs[func] = "\n".join(func_lines[:150]) # First 150 lines per function
            print(f"  Extracted {func}: {len(func_lines)} assembly lines")

    out_json = os.path.join(OUT_DIR, "msdisplay_exported_functions_disasm.json")
    with open(out_json, "w") as f:
        json.dump(extracted_funcs, f, indent=2)

    print(f"Saved target functions disassembly to {out_json}")

if __name__ == "__main__":
    main()
