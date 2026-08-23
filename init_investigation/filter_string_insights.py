#!/usr/bin/env python3
"""
filter_string_insights.py
Filters extracted strings for critical protocol startup parameters, register IDs,
device IDs, COM port patterns, and initialization commands.
"""

import os
import sys
import json
import re

STRINGS_JSON = "/home/tor/pc-case-lcd/init_investigation/vmax_strings_relevant.json"

def main():
    if not os.path.exists(STRINGS_JSON):
        print(f"Error: {STRINGS_JSON} not found.")
        return

    with open(STRINGS_JSON, "r") as f:
        data = json.load(f)

    print("=" * 60)
    print("INSIGHT FILTER — RELEVANT VMAX STRINGS")
    print("=" * 60)

    categories = {
        "vid_pid_device_ids": [r"33c3", r"f101", r"345f", r"9132", r"vid_", r"pid_"],
        "com_serial_patterns": [r"com\d+", r"ttyacm", r"baud", r"serial", r"parity", r"stopbits"],
        "opcode_cmd_patterns": [r"0x00[0-9a-f]{2}", r"cmd_", r"handshake", r"gethardware", r"getflash", r"getgif", r"exitrunning", r"changestatus"],
        "status_ahmi_patterns": [r"ahmi", r"status_", r"0x10", r"0x11", r"0x20"],
        "shutdown_sleep_timer_patterns": [r"shutdown", r"poweroff", r"standby", r"sleep", r"timer", r"timeout", r"watchdog", r"auto.*off", r"close.*device"],
        "register_operation_patterns": [r"register", r"setvalue", r"setstring", r"func", r"modbus"]
    }

    for cat_name, patterns in categories.items():
        print(f"\n── {cat_name.upper()} ──────────────────────────────────")
        matched_strings = set()
        for fname, file_data in data.items():
            for s in file_data.get("relevant_strings", []):
                if any(re.search(pat, s, re.IGNORECASE) for pat in patterns):
                    # Filter out noise (very long UI text / base64)
                    if len(s) < 150:
                        matched_strings.add(f"[{fname}] {s}")

        print(f"Total matched: {len(matched_strings)}")
        for ms in sorted(list(matched_strings))[:30]:
            print(f"  {ms}")

if __name__ == "__main__":
    main()
