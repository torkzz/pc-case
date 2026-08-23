#!/usr/bin/env python3
"""
deep_string_analyzer.py
Exhaustive string search across Vmax.exe, DeviceCommunicationLibrary.dll, and common.dll
Searches for protocol strings, register IDs, command opcodes, timeouts, and startup sequences.
"""

import os
import sys
import re
import json

BIN_DIR = "/home/tor/vmax_bundle/bin/Release"

FILES_TO_SCAN = [
    os.path.join(BIN_DIR, "Vmax.exe"),
    os.path.join(BIN_DIR, "DeviceCommunicationLibrary.dll"),
    os.path.join(BIN_DIR, "common.dll")
]

KEYWORDS = [
    "connect", "handshake", "status", "exit", "running", "power", "shutdown",
    "sleep", "delay", "timer", "close", "restart", "dtr", "rts", "baud",
    "screen", "display", "33c3", "345f", "f101", "9132", "ahmi", "gif", "flash",
    "hardware", "device", "serial", "acm", "com", "tty", "read", "write",
    "register", "value", "string", "download", "complete", "0x00", "0x",
    "cmd_", "status_"
]

def extract_all_strings(filepath):
    with open(filepath, "rb") as f:
        data = f.read()

    # ASCII strings
    ascii_matches = re.findall(rb"[\x20-\x7e]{3,}", data)
    # Unicode / UTF-16LE strings
    utf16_matches = re.findall(rb"(?:[\x20-\x7e]\x00){3,}", data)

    results = set()
    for m in ascii_matches:
        try:
            results.add(m.decode('ascii'))
        except:
            pass

    for m in utf16_matches:
        try:
            results.add(m.decode('utf-16le'))
        except:
            pass

    return sorted(list(results))

def main():
    print("=" * 60)
    print("DEEP STRING SEARCH — VMAX BINARIES")
    print("=" * 60)

    all_findings = {}

    for fpath in FILES_TO_SCAN:
        fname = os.path.basename(fpath)
        if not os.path.exists(fpath):
            print(f"File not found: {fpath}")
            continue

        print(f"Scanning {fname}...")
        strings = extract_all_strings(fpath)
        print(f"  Total unique strings extracted: {len(strings)}")

        filtered = [s for s in strings if any(k in s.lower() for k in KEYWORDS)]
        print(f"  Protocol/hardware-relevant strings: {len(filtered)}")

        all_findings[fname] = {
            "total_strings": len(strings),
            "relevant_strings_count": len(filtered),
            "relevant_strings": filtered
        }

    # Save to text and JSON
    out_json = "/home/tor/pc-case-lcd/init_investigation/vmax_strings_relevant.json"
    with open(out_json, "w") as f:
        json.dump(all_findings, f, indent=2)

    out_txt = "/home/tor/pc-case-lcd/init_investigation/vmax_strings_relevant.txt"
    with open(out_txt, "w") as f:
        for fname, data in all_findings.items():
            f.write(f"=== {fname} ({data['relevant_strings_count']} relevant strings) ===\n")
            for s in data["relevant_strings"]:
                f.write(f"  {s}\n")
            f.write("\n")

    print(f"\nSaved findings to:\n  - {out_json}\n  - {out_txt}")

if __name__ == "__main__":
    main()
