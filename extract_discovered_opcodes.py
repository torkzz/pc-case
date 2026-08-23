import re, json

il_comm = open("DeviceCommunicationLibrary.il", "r", encoding="utf-8", errors="ignore").read()

# Extract all numeric constants passed to Frame constructors or used in get_Cmd / switch statements
opcodes = {}

# 1. Classes extending BaseFrame or RegisterOperationRequest
matches = re.findall(r'\.class [^{]+ ([A-Za-z0-9_]+)\s+extends DeviceCommunicationLibrary\.([A-Za-z0-9_]+)', il_comm)

for c_name, base in matches:
    pos = il_comm.find(f".class public auto ansi beforefieldinit {c_name}")
    if pos == -1: pos = il_comm.find(f".class public auto ansi {c_name}")
    if pos != -1:
        block = il_comm[pos:pos+3000]
        # find ldc.i4 in ctor or get_Cmd
        cmd_m = re.search(r'ldc\.i4(?:\.s)?\s+(0x[0-9a-fA-F]+|\d+)', block)
        if cmd_m:
            v_str = cmd_m.group(1)
            v_int = int(v_str, 16) if v_str.startswith("0x") else int(v_str)
            opcodes[f"0x{v_int:04X}"] = {
                "opcode_dec": v_int,
                "class": c_name,
                "base": base,
                "confidence": "HIGH (Static IL Class)"
            }

# 2. Switch statement opcodes in GetExpectedResponseCmd / ProcessResponseFrame
switch_matches = re.findall(r'ldc\.i4(?:\.s)?\s+(0x[0-9a-fA-F]+|\d+)', il_comm)
for sm in switch_matches:
    v_int = int(sm, 16) if sm.startswith("0x") else int(sm)
    if 0x0010 <= v_int <= 0x00FF:
        hex_key = f"0x{v_int:04X}"
        if hex_key not in opcodes:
            opcodes[hex_key] = {
                "opcode_dec": v_int,
                "class": "Switch/Branch Candidate",
                "base": "BaseFrame",
                "confidence": "MEDIUM (IL Constant)"
            }

# Save discovered_opcodes.json
out_list = sorted(opcodes.values(), key=lambda x: x['opcode_dec'])
with open("/home/tor/pc-case-lcd/discovered_opcodes.json", "w") as f:
    json.dump(out_list, f, indent=2)

print(f"Generated discovered_opcodes.json with {len(out_list)} opcodes:")
for item in out_list:
    print(f"  Opcode {item['opcode_dec']:#06x} ({item['opcode_dec']:3d}): Class = {item['class']}")

