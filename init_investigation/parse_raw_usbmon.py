import re

with open('/home/tor/pc-case-lcd/raw_usbmon1.txt', 'rb') as f:
    data = f.read()

# Look for printable strings or hex sequences in usbmon log
ascii_strs = re.findall(b'[\x20-\x7e]{4,}', data)
print("=== USBMON CAPTURED ASCII STRINGS ===")
for s in set(ascii_strs):
    s_str = s.decode('latin1', errors='ignore')
    if any(k in s_str for k in ['AH', 'MI', '33c3', 'f101', 'VMAX']):
        print("  ", s_str)

