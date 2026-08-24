with open('/home/tor/pc-case-lcd/raw_usbmon1.txt', 'rb') as f:
    data = f.read()

import re
matches = re.finditer(b'AH.*?MI', data, re.DOTALL)
found = set()
for m in matches:
    raw = m.group(0)
    if len(raw) <= 20:
        found.add(raw.hex())

print(f"Discovered {len(found)} unique AH..MI byte sequences in raw usbmon:")
for f in sorted(list(found)):
    print(" ", f)

