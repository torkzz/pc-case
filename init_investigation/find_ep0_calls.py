import subprocess
import re
import struct

dll_path = '/home/tor/vmax_bundle/bin/Release/MSDISPLAYSDKWRRAPER.dll'

# Run objdump -d -r to get disassembly with relocations
res = subprocess.run(['objdump', '-d', '-r', dll_path], capture_output=True, text=True)
lines = res.stdout.splitlines()
print(f"Total disassembly lines: {len(lines)}")

# Search for occurrences of usb_control_msg, usb_bulk_write, libusb0.dll
matches = []
for idx, line in enumerate(lines):
    if any(k in line for k in ['usb_control_msg', 'usb_bulk_write', 'usb_open', 'usb_claim_interface', 'usb_set_configuration', 'usb_control_msg']):
        matches.append((idx, line))

print(f"Found {len(matches)} symbol references in disassembly:")
for idx, line in matches:
    print(f"Line {idx}: {line}")
    # Print context
    start = max(0, idx - 20)
    end = min(len(lines), idx + 25)
    print("--- Context ---")
    for j in range(start, end):
        print(f"{j:6d}: {lines[j]}")
    print("=" * 60)

