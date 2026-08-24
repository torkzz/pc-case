import re

with open('/home/tor/pc-case-lcd/DeviceCommunicationLibrary.il', 'r', encoding='utf-8', errors='ignore') as f:
    il_lines = f.readlines()

print(f"Total IL lines: {len(il_lines)}")

# Helper to print method blocks
def print_method_block(start_pattern, max_lines=150):
    for i, line in enumerate(il_lines):
        if re.search(start_pattern, line):
            print(f"=== MATCH AT LINE {i+1}: {line.strip()} ===")
            start = i
            end = min(len(il_lines), i + max_lines)
            for j in range(start, end):
                print(f"{j+1:6d}: {il_lines[j]}", end="")
                if il_lines[j].strip().startswith("}") and j > start + 5:
                    print(f"\n--- End of method at line {j+1} ---")
                    break
            print("\n" + "="*80)

print("\n1. Searching for Connect method:")
print_method_block(r'\.method.*?\bConnect\b')

print("\n2. Searching for DeviceCommunicator .ctor:")
print_method_block(r'\.class.*?\bDeviceCommunicator\b')

print("\n3. Searching for HandshakeAsync:")
print_method_block(r'\.method.*?\bHandshakeAsync\b')

print("\n4. Searching for SendFrame / SendRequestAsync:")
print_method_block(r'\.method.*?\bSendRequestAsync\b')

print("\n5. Searching for SerialPort DataReceived / ProcessReceiveBuffer:")
print_method_block(r'\.method.*?\bProcessReceiveBuffer\b')

