#!/usr/bin/env python3
"""
analyze_shutdown_logic.py
Deep IL & binary search for VMAX screen power-off, sleep, standby, timer, and watchdog logic.
"""

import os
import sys
import re
import json

DCL_IL_PATH = "/home/tor/pc-case-lcd/DeviceCommunicationLibrary.il"
VMAX_IL_PATH = "/home/tor/pc-case-lcd/Vmax.il"

def main():
    print("=" * 60)
    print("SHUTDOWN & TIMEOUT LOGIC ANALYSIS")
    print("=" * 60)

    with open(DCL_IL_PATH, "r", encoding="utf-8", errors="ignore") as f:
        dcl_il = f.read()

    with open(VMAX_IL_PATH, "r", encoding="utf-8", errors="ignore") as f:
        vmax_il = f.read()

    keywords = [
        "sleep", "shutdown", "standby", "idle", "power", "off", "close",
        "timer", "interval", "timeout", "watchdog", "auto", "display",
        "black", "screen", "restart", "exit"
    ]

    print("[1] Searching DeviceCommunicationLibrary.il for power/timer references...")
    dcl_matches = []
    for line_idx, line in enumerate(dcl_il.splitlines(), 1):
        line_lower = line.lower()
        if any(k in line_lower for k in ["sleep", "timer", "timeout", "power", "status", "restart", "exit"]):
            dcl_matches.append(f"L{line_idx}: {line.strip()}")

    print(f"Found {len(dcl_matches)} matching lines in DCL.")

    print("\n[2] Searching Vmax.il for power/timer/shutdown references...")
    vmax_matches = []
    for line_idx, line in enumerate(vmax_il.splitlines(), 1):
        line_lower = line.lower()
        if any(k in line_lower for k in ["sleep", "timer", "timeout", "power", "status", "restart", "exit"]):
            vmax_matches.append(f"L{line_idx}: {line.strip()}")

    print(f"Found {len(vmax_matches)} matching lines in Vmax.il.")

    output = {
        "dcl_power_timer_lines_sample": dcl_matches[:40],
        "vmax_power_timer_lines_sample": vmax_matches[:40]
    }

    out_path = "/home/tor/pc-case-lcd/init_investigation/shutdown_logic_analysis.json"
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2)

    print(f"\nSaved analysis to {out_path}")

if __name__ == "__main__":
    main()
