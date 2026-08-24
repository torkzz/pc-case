with open('/home/tor/vmax_bundle/bin/Release/MSDISPLAYSDKWRRAPER.dll', 'rb') as f:
    data = f.read()

import re
matches = [m.start() for m in re.finditer(b'usb_control_msg', data)]
print("usb_control_msg string offsets:", [hex(m) for m in matches])

matches_bulk = [m.start() for m in re.finditer(b'usb_bulk_write', data)]
print("usb_bulk_write string offsets:", [hex(m) for m in matches_bulk])

