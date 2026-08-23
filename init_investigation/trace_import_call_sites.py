#!/usr/bin/env python3
"""
trace_import_call_sites.py
Traces the exact RVA call sites for libusb0.dll, SETUPAPI.dll, and KERNEL32.dll
import functions inside MSDISPLAYSDKWRRAPER.dll.

Extracts argument setup registers (RCX, RDX, R8, R9) before each call.
"""

import os
import sys
import re
import json

ASM_PATH = "/home/tor/pc-case-lcd/init_investigation/MSDISPLAYSDKWRRAPER_disasm.asm"
OUT_DIR = "/home/tor/pc-case-lcd/init_investigation"

# Import addresses in IAT or call targets
TARGET_IMPORTS = [
    "usb_open", "usb_claim_interface", "usb_control_msg", "usb_bulk_write",
    "usb_init", "usb_find_busses", "usb_find_devices", "usb_get_busses", "usb_close", "usb_release_interface",
    "SetupDiGetClassDevsW", "SetupDiEnumDeviceInterfaces", "SetupDiGetDeviceInterfaceDetailW",
    "CreateFileW", "DeviceIoControl"
]

def main():
    if not os.path.exists(ASM_PATH):
        print(f"Error: {ASM_PATH} not found.")
        return

    print("Reading disassembly...")
    with open(ASM_PATH, "r", encoding="utf-8", errors="ignore") as f:
        lines = f.read().splitlines()

    print(f"Loaded {len(lines)} lines of disassembly.")

    findings = {}

    for imp_name in TARGET_IMPORTS:
        matches = []
        for idx, l in enumerate(lines):
            if imp_name in l:
                # Capture 15 lines before and 5 lines after call site
                start_idx = max(0, idx - 15)
                end_idx = min(len(lines), idx + 5)
                matches.append({
                    "line_num": idx + 1,
                    "matched_line": l.strip(),
                    "context": lines[start_idx:end_idx]
                })

        findings[imp_name] = {
            "call_count": len(matches),
            "call_sites": matches
        }
        print(f"  {imp_name}: {len(matches)} call site(s) found.")

    out_file = os.path.join(OUT_DIR, "verified_import_call_sites.json")
    with open(out_file, "w") as f:
        json.dump(findings, f, indent=2)

    out_md = os.path.join(OUT_DIR, "verified_import_call_sites.md")
    with open(out_md, "w") as f:
        f.write("# Verified Import Call Sites in MSDISPLAYSDKWRRAPER.dll\n\n")
        for imp_name, data in findings.items():
            f.write(f"## `{imp_name}` ({data['call_count']} Call Sites)\n\n")
            for cs in data["call_sites"]:
                f.write(f"### Line {cs['line_num']}: `{cs['matched_line']}`\n")
                f.write("```assembly\n")
                for cl in cs["context"]:
                    f.write(f"{cl}\n")
                f.write("```\n\n")

    print(f"\nSaved import call site analysis to {out_file} and {out_md}")

if __name__ == "__main__":
    main()
