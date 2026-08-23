import subprocess, re

# Disassemble MSDISPLAYSDKWRRAPER.dll
res = subprocess.run(['objdump', '-d', '/home/tor/vmax_bundle/bin/Release/MSDISPLAYSDKWRRAPER.dll'], capture_output=True, text=True)
asm = res.stdout.splitlines()

# Search for VID/PID constants: 0x345F (13407), 0x9132 (37170), 0x33C3 (13251), 0xF101 (61697)
vid_pid_matches = []
for i, line in enumerate(asm):
    if any(k in line.lower() for k in ['345f', '9132', '33c3', 'f101', '13407', '37170']):
        vid_pid_matches.append((i, line))

print(f"Found {len(vid_pid_matches)} VID/PID references in MSDISPLAYSDKWRRAPER.dll disassembly:")
for idx, line in vid_pid_matches:
    print(f"Line {idx}: {line}")
    start = max(0, idx - 15)
    end = min(len(asm), idx + 20)
    for j in range(start, end):
        print(f"  {asm[j]}")
    print("="*60)

