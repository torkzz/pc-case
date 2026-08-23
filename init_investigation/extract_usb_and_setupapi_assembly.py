#!/usr/bin/env python3
"""
extract_usb_and_setupapi_assembly.py
Extracts full assembly context for libusb0.dll, SETUPAPI.dll, and DeviceIoControl call sites
from resolved_iat_call_sites.json.
"""

import os
import json

RESOLVED_JSON = "/home/tor/pc-case-lcd/init_investigation/resolved_iat_call_sites.json"
OUT_DIR = "/home/tor/pc-case-lcd/init_investigation"

TARGET_FUNCS = [
    "libusb0.dll!usb_open",
    "libusb0.dll!usb_claim_interface",
    "libusb0.dll!usb_control_msg",
    "libusb0.dll!usb_bulk_write",
    "SETUPAPI.dll!SetupDiGetClassDevsW",
    "SETUPAPI.dll!SetupDiEnumDeviceInterfaces",
    "SETUPAPI.dll!SetupDiGetDeviceInterfaceDetailW",
    "KERNEL32.dll!CreateFileW",
    "KERNEL32.dll!DeviceIoControl"
]

def main():
    if not os.path.exists(RESOLVED_JSON):
        return

    with open(RESOLVED_JSON, "r") as f:
        calls = json.load(f)

    target_calls = [c for c in calls if c["imported_func"] in TARGET_FUNCS]

    print(f"Extracted {len(target_calls)} call site contexts for USB, SetupAPI, and DeviceIoControl.")

    out_file = os.path.join(OUT_DIR, "usb_native_call_contexts.json")
    with open(out_file, "w") as f:
        json.dump(target_calls, f, indent=2)

    out_md = os.path.join(OUT_DIR, "usb_native_call_contexts.md")
    with open(out_md, "w") as f:
        f.write("# Native USB & SetupAPI Call Contexts in MSDISPLAYSDKWRRAPER.dll\n\n")
        
        # Group by imported_func
        by_func = {}
        for tc in target_calls:
            fn = tc["imported_func"]
            if fn not in by_func:
                by_func[fn] = []
            by_func[fn].append(tc)

        for fn, call_list in sorted(by_func.items()):
            f.write(f"## `{fn}` ({len(call_list)} Call Sites)\n\n")
            for idx, cs in enumerate(call_list, 1):
                f.write(f"### Call Site #{idx} (Line {cs['line_num']}, Address `{cs['target_va']}`)\n")
                f.write("```assembly\n")
                for cl in cs["context"]:
                    f.write(f"{cl}\n")
                f.write("```\n\n")

    print(f"Saved context report to {out_file} and {out_md}")

if __name__ == "__main__":
    main()
