import subprocess, re

# Inspect disassembly of MSDISPLAYSDKWRRAPER.dll around usb_control_msg
res = subprocess.run(['objdump', '-d', '/home/tor/vmax_bundle/bin/Release/MSDISPLAYSDKWRRAPER.dll'], capture_output=True, text=True)
lines = res.stdout.splitlines()

ctrl_calls = []
for i, l in enumerate(lines):
    if 'usb_control_msg' in l:
        print(f"usb_control_msg call at line {i}: {l}")
        start = max(0, i - 25)
        end = min(len(lines), i + 10)
        for j in range(start, end):
            print(f"  {lines[j]}")
        print("="*60)

