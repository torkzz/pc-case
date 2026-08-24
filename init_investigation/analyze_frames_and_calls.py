import re

il_comm = open("DeviceCommunicationLibrary.il", "r", encoding="utf-8", errors="ignore").read()
il_vmax = open("Vmax.il", "r", encoding="utf-8", errors="ignore").read()

print("=== 1. FIND ALL FRAME CLASSES AND OPCODES IN DeviceCommunicationLibrary.il ===")

# Find class definitions inheriting from BaseFrame or RequestFrame or ResponseFrame
classes = re.findall(r'\.class public auto ansi beforefieldinit ([A-Za-z0-9_]+)\s+extends DeviceCommunicationLibrary\.([A-Za-z0-9_]+)', il_comm)

print(f"Found {len(classes)} frame classes:")
for c, base in classes:
    print(f"  Class: {c} (extends {base})")

# Extract Cmd property getters / constructors to find numerical Opcode values
frames_info = {}
for c, base in classes:
    pos = il_comm.find(f".class public auto ansi beforefieldinit {c}")
    if pos != -1:
        end_pos = il_comm.find("} // end of class", pos)
        block = il_comm[pos:end_pos]
        # Look for ldc.i4 or cmd opcode
        cmd_match = re.search(r'ldc\.i4(?:\.s)?\s+(0x[0-9a-fA-F]+|\d+)', block)
        opcode = cmd_match.group(1) if cmd_match else "Unknown"
        frames_info[c] = {"base": base, "opcode": opcode, "block": block}
        print(f"  Frame {c}: base={base}, opcode={opcode}")

print("\n=== 2. FIND ALL CALLS TO DeviceCommunicator IN Vmax.il ===")
vmax_calls = re.findall(r'call(?:virt)?\s+instance\s+[^\n]+DeviceCommunicator::([A-Za-z0-9_]+)', il_vmax)
print("Vmax.il DeviceCommunicator calls:", set(vmax_calls))

print("\n=== 3. DETAILED METHOD CALL SITES IN DeviceCommunicationLibrary.il ===")
# Search DeviceCommunicator methods
dc_pos = il_comm.find(".class public auto ansi beforefieldinit DeviceCommunicator")
dc_end = il_comm.find("} // end of class DeviceCommunicationLibrary.DeviceCommunicator", dc_pos)
dc_block = il_comm[dc_pos:dc_end]

methods = re.findall(r'\.method public[^\n]+', dc_block)
for m in methods:
    print("  ", m.strip())

