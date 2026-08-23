#!/usr/bin/env python3
"""
trace_vmax_handshake_caller.py
Searches vmax_raw_disasm.il for <HandShake>d__44, Connect, DeviceCommunicator calls,
and all initialization and startup state machines in Vmax.exe.
"""

import os
import sys
import re
import json

VMAX_IL_PATH = "/home/tor/pc-case-lcd/init_investigation/vmax_raw_disasm.il"

def main():
    print("=" * 60)
    print("TRACING VMAX HANDSHAKE & CONNECT CALLERS IN VMAX.EXE")
    print("=" * 60)

    if not os.path.exists(VMAX_IL_PATH):
        print(f"Error: {VMAX_IL_PATH} not found.")
        return

    with open(VMAX_IL_PATH, "r", encoding="utf-8", errors="ignore") as f:
        il_content = f.read()

    # Search for HandShake or Handshake in Vmax.exe IL
    hs_matches = [m.start() for m in re.finditer(r"HandShake|Handshake", il_content, re.IGNORECASE)]
    print(f"Found {len(hs_matches)} occurrences of 'Handshake' in Vmax.exe disassembly.")

    snippets = []
    for idx in hs_matches:
        start = max(0, idx - 500)
        end = min(len(il_content), idx + 500)
        snippets.append(il_content[start:end])

    # Search for classes/methods containing HandShake
    hs_classes = re.findall(r"\.class[\s\S]*?HandShake[\s\S]*?\{([\s\S]*?)\n  \} // end of class", il_content)
    
    # Search for DeviceCommunicator references in Vmax.exe IL
    dc_refs = [m.start() for m in re.finditer(r"DeviceCommunicator", il_content)]
    print(f"Found {len(dc_refs)} occurrences of 'DeviceCommunicator' in Vmax.exe disassembly.")

    dc_snippets = []
    for idx in dc_refs[:20]:
        start = max(0, idx - 300)
        end = min(len(il_content), idx + 300)
        dc_snippets.append(il_content[start:end])

    output = {
        "handshake_occurrences": len(hs_matches),
        "handshake_snippets_sample": snippets[:10],
        "device_communicator_occurrences": len(dc_refs),
        "device_communicator_snippets_sample": dc_snippets
    }

    out_file = "/home/tor/pc-case-lcd/init_investigation/vmax_handshake_callgraph.json"
    with open(out_file, "w") as f:
        json.dump(output, f, indent=2)

    print(f"Callgraph findings saved to {out_file}")

if __name__ == "__main__":
    main()
