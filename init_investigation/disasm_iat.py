import subprocess, re

dll_path = '/home/tor/vmax_bundle/bin/Release/MSDISPLAYSDKWRRAPER.dll'

res = subprocess.run(['objdump', '-d', dll_path], capture_output=True, text=True)
lines = res.stdout.splitlines()

# Search for indirect calls via IAT: 0x74328 (usb_control_msg), 0x74340 (usb_bulk_write), 0x74318 (usb_claim_interface), 0x74338 (usb_open)
iat_targets = {
    '74328': 'usb_control_msg',
    '74340': 'usb_bulk_write',
    '74318': 'usb_claim_interface',
    '74338': 'usb_open',
    '74320': 'usb_close',
}

for i, l in enumerate(lines):
    for addr, name in iat_targets.items():
        if addr in l:
            print(f"\n==================== Found reference to {name} (0x{addr}) at line {i} ====================")
            start = max(0, i - 25)
            end = min(len(lines), i + 25)
            for j in range(start, end):
                print(f"{j:6d}: {lines[j]}")

