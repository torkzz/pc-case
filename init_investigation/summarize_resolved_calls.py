#!/usr/bin/env python3
"""
summarize_resolved_calls.py
Summarizes and formats every call site for libusb0.dll, SETUPAPI.dll, and KERNEL32.dll
import functions in MSDISPLAYSDKWRRAPER.dll.
"""

import os
import json

RESOLVED_JSON = "/home/tor/pc-case-lcd/init_investigation/resolved_iat_call_sites.json"
OUT_DIR = "/home/tor/pc-case-lcd/init_investigation"

def main():
    if not os.path.exists(RESOLVED_JSON):
        print(f"Error: {RESOLVED_JSON} not found.")
        return

    with open(RESOLVED_JSON, "r") as f:
        calls = json.load(f)

    print("=" * 70)
    print("VERIFIED NATIVE CALL SUMMARY — MSDISPLAYSDKWRRAPER.DLL")
    print("=" * 70)

    by_dll = {}
    for c in calls:
        func_full = c["imported_func"]
        dll, fn = func_full.split("!") if "!" in func_full else ("UNKNOWN", func_full)
        if dll not in by_dll:
            by_dll[dll] = {}
        if fn not in by_dll[dll]:
            by_dll[dll][fn] = []
        by_dll[dll][fn].append(c)

    summary_out = {}

    for dll, funcs in sorted(by_dll.items()):
        print(f"\nDLL: {dll}")
        summary_out[dll] = {}
        for fn, call_list in sorted(funcs.items()):
            print(f"  - {fn}: {len(call_list)} call site(s)")
            summary_out[dll][fn] = [
                {
                    "line": cs["line_num"],
                    "target_va": cs["target_va"],
                    "instruction": cs["line_text"]
                } for cs in call_list
            ]

    out_file = os.path.join(OUT_DIR, "msdisplay_native_calls_summary.json")
    with open(out_file, "w") as f:
        json.dump(summary_out, f, indent=2)

    print(f"\nSaved call summary to {out_file}")

if __name__ == "__main__":
    main()
