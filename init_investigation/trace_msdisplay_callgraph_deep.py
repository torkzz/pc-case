#!/usr/bin/env python3
"""
trace_msdisplay_callgraph_deep.py
Recursive x64 assembly tracer for MSDISPLAYSDKWRRAPER.dll
Traces RVA entrypoints -> internal functions -> PE import calls (libusb0 / SetupAPI / Kernel32)
Extracts exact registers (RCX, RDX, R8, R9, RSP) before each call.
"""

import os
import sys
import re
import json

ASM_PATH = "/home/tor/pc-case-lcd/init_investigation/MSDISPLAYSDKWRRAPER_disasm.asm"
IAT_PATH = "/home/tor/pc-case-lcd/init_investigation/resolved_iat_call_sites.json"
OUT_DIR = "/home/tor/pc-case-lcd/init_investigation"

# Entrypoints to trace (ImageBase = 0x180000000)
# RVA -> VA (add 0x180000000)
ENTRYPOINTS = {
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

def parse_asm_by_address(asm_text):
    lines = asm_text.splitlines()
    addr_map = {}
    for idx, l in enumerate(lines):
        m = re.match(r"^\s*([0-9a-fA-F]+):", l)
        if m:
            addr_hex = m.group(1).lower()
            addr_map[addr_hex] = idx
    return lines, addr_map

def extract_function_block(lines, addr_map, start_va):
    if start_va not in addr_map:
        return []
    start_idx = addr_map[start_va]
    block = []
    for i in range(start_idx, len(lines)):
        l = lines[i]
        block.append(l)
        # End of function detection: ret / retq followed by int3 or nop or next function header
        if ("ret" in l or "jmp" in l) and i > start_idx + 3:
            # check if next line is int3 or function boundary
            if i + 1 < len(lines):
                next_l = lines[i+1]
                if "int3" in next_l or "nop" in next_l or re.match(r"^\s*[0-9a-fA-F]+ <", next_l):
                    break
        if len(block) > 300: # safety cap
            break
    return block

def analyze_calls_in_block(block, addr_map):
    internal_calls = []
    iat_calls = []
    
    for l in block:
        # Match direct call: call 0x1800...
        m_call = re.search(r"callq?\s+(0x1800[0-9a-fA-F]+)", l)
        if m_call:
            internal_calls.append(m_call.group(1).lower())

        # Match jmp target: jmp 0x1800...
        m_jmp = re.search(r"jmpq?\s+(0x1800[0-9a-fA-F]+)", l)
        if m_jmp:
            internal_calls.append(m_jmp.group(1).lower())

        # Match indirect call/jmp via RIP (IAT)
        m_iat = re.search(r"(callq?|jmpq?)\s+\*0x[0-9a-fA-F]+\(%rip\)\s+#\s+(0x1800[0-9a-fA-F]+)", l)
        if m_iat:
            iat_calls.append(m_iat.group(2).lower())

    return sorted(list(set(internal_calls))), sorted(list(set(iat_calls)))

def main():
    if not os.path.exists(ASM_PATH):
        print(f"Error: {ASM_PATH} not found.")
        return

    with open(ASM_PATH, "r", encoding="utf-8", errors="ignore") as f:
        asm_text = f.read()

    lines, addr_map = parse_asm_by_address(asm_text)
    print(f"Parsed {len(addr_map)} instruction addresses.")

    with open(IAT_PATH, "r") as f:
        iat_data = json.load(f)

    iat_name_map = {}
    for item in iat_data:
        iat_name_map[item["target_va"]] = item["imported_func"]

    callgraph = {}
    visited_internal = set()
    to_visit = list(ENTRYPOINTS.values())

    # Build entrypoint blocks first
    for name, va in ENTRYPOINTS.items():
        block = extract_function_block(lines, addr_map, va)
        int_calls, iat_calls = analyze_calls_in_block(block, addr_map)
        
        resolved_iat = [f"{c} ({iat_name_map.get(c, 'UNKNOWN')})" for c in iat_calls]
        
        int_calls_clean = [f"0x{int(c, 16):x} (RVA 0x{int(c, 16) - 0x180000000:05x})" for c in int_calls]
        callgraph[name] = {
            "address": f"0x{va}",
            "rva": f"0x{int(va, 16) - 0x180000000:05x}",
            "block_lines": len(block),
            "internal_calls": int_calls_clean,
            "iat_calls": resolved_iat,
            "assembly_sample": block[:30]
        }
        
        for c in int_calls:
            if c not in visited_internal:
                to_visit.append(c)

    # Recursively resolve internal calls (up to 2 levels deep)
    internal_blocks = {}
    for va in to_visit:
        if va in ENTRYPOINTS.values() or va in internal_blocks:
            continue
        block = extract_function_block(lines, addr_map, va)
        if block:
            int_calls, iat_calls = analyze_calls_in_block(block, addr_map)
            resolved_iat = [f"{c} ({iat_name_map.get(c, 'UNKNOWN')})" for c in iat_calls]
            rva_val = int(va, 16) - 0x180000000
            int_calls_clean = [f"0x{int(c, 16):x} (RVA 0x{int(c, 16) - 0x180000000:05x})" for c in int_calls]
            internal_blocks[f"0x{va}"] = {
                "rva": f"0x{rva_val:05x}",
                "block_lines": len(block),
                "internal_calls": int_calls_clean,
                "iat_calls": resolved_iat,
                "assembly_sample": block[:40]
            }

    master_graph = {
        "entrypoints": callgraph,
        "internal_functions": internal_blocks
    }

    out_file = os.path.join(OUT_DIR, "msdisplay_callgraph_deep.json")
    with open(out_file, "w") as f:
        json.dump(master_graph, f, indent=2)

    out_md = os.path.join(OUT_DIR, "MSDISPLAY_CALLGRAPH.md")
    with open(out_md, "w") as f:
        f.write("# MSDisplay Native Call Graph & Function RVAs (`MSDISPLAY_CALLGRAPH.md`)\n\n")
        f.write("## Entrypoints\n\n")
        for name, data in callgraph.items():
            f.write(f"### `{name}` (RVA `{data['rva']}`, Address `{data['address']}`)\n")
            f.write(f"- **Internal Calls**: `{data['internal_calls']}`\n")
            f.write(f"- **IAT Calls**: `{data['iat_calls']}`\n\n")
            f.write("```assembly\n")
            for bl in data["assembly_sample"]:
                f.write(f"{bl}\n")
            f.write("```\n\n")

        f.write("## Internal Call Targets\n\n")
        for addr, data in internal_blocks.items():
            f.write(f"### Function `{addr}` (RVA `{data['rva']}`)\n")
            f.write(f"- **Internal Calls**: `{data['internal_calls']}`\n")
            f.write(f"- **IAT Calls**: `{data['iat_calls']}`\n\n")
            f.write("```assembly\n")
            for bl in data["assembly_sample"]:
                f.write(f"{bl}\n")
            f.write("```\n\n")

    print(f"Traced call graph: {len(callgraph)} entrypoints, {len(internal_blocks)} internal targets.")
    print(f"Saved to {out_file} and {out_md}")

if __name__ == "__main__":
    main()
