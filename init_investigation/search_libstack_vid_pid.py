import re

libstack_raw = open("/home/tor/vmax_bundle/bin/Release/libstack.dll", "rb").read()

print("=== SEARCHING VID/PID REFS IN libstack.dll ===")

# Search for VID / PID patterns in libstack.dll
vid_pid_matches = re.findall(b'vid_[0-9a-fA-F]{4}&pid_[0-9a-fA-F]{4}', libstack_raw, re.IGNORECASE)
print("VID/PID string matches in libstack.dll:", set([m.decode() for m in vid_pid_matches]))

# Search for raw 16-bit VID/PID values or strings in libstack.dll
# Look for 0x33c3, 0xf101, 0x345f, 0x9132 in hex
for vid, pid in [(0x33c3, 0xf101), (0x345f, 0x9132), (0x345f, 0x9133), (0x345f, 0x374a), (0x345f, 0xa101)]:
    vid_b = vid.to_bytes(2, 'little')
    pid_b = pid.to_bytes(2, 'little')
    print(f"Searching VID {vid:#06x} ({vid_b.hex()}), PID {pid:#06x} ({pid_b.hex()})...")
    m1 = [m.start() for m in re.finditer(re.escape(vid_b), libstack_raw)]
    m2 = [m.start() for m in re.finditer(re.escape(pid_b), libstack_raw)]
    print(f"  VID matches: {len(m1)}, PID matches: {len(m2)}")

