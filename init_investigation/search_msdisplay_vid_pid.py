import re

ms_raw = open("/home/tor/vmax_bundle/bin/Release/MSDISPLAYSDKWRRAPER.dll", "rb").read()

print("=== SEARCHING VID/PID IN MSDISPLAYSDKWRRAPER.dll ===")

for vid, pid in [(0x345f, 0x9132), (0x345f, 0x9133), (0x345f, 0x374a), (0x345f, 0xa101), (0x33c3, 0xf101)]:
    vid_b1 = vid.to_bytes(2, 'little')
    pid_b1 = pid.to_bytes(2, 'little')
    vid_b2 = vid.to_bytes(2, 'big')
    pid_b2 = pid.to_bytes(2, 'big')
    
    m_vid1 = len(list(re.finditer(re.escape(vid_b1), ms_raw)))
    m_pid1 = len(list(re.finditer(re.escape(pid_b1), ms_raw)))
    print(f"VID {vid:#06x}: little-endian matches={m_vid1}, PID {pid:#06x}: matches={m_pid1}")

# Search strings in MSDISPLAYSDKWRRAPER.dll
strings = re.findall(b'[\x20-\x7e]{3,}', ms_raw)
for s in strings:
    str_val = s.decode('ascii', errors='ignore')
    if any(k in str_val for k in ["VID", "PID", "345", "913", "374", "A10", "USB", "ep", "EP", "Bulk", "Interface"]):
        print("  String:", str_val)

