import re

vmax_raw = open("/home/tor/vmax_bundle/bin/Release/Vmax.exe", "rb").read()

print(f"Vmax.exe total size: {len(vmax_raw)} bytes ({len(vmax_raw)/1024/1024:.2f} MB)")

# Search for strings inside Vmax.exe
targets = [
    b"Wrraper_MSDisplay", b"MSDISPLAY", b"DeviceCommunicator", b"DeviceCommunicationLibrary",
    b"33c3", b"f101", b"345f", b"9132", b"9133", b"374a", b"a101",
    b"costura", b"Costura", b"Resource", b"libcompositeScreenModel", b"libstack"
]

for t in targets:
    matches = [m.start() for m in re.finditer(re.escape(t), vmax_raw, re.IGNORECASE)]
    print(f"String '{t.decode()}' matches: {len(matches)}")

# Extract ASCII strings near matches
print("\n=== SAMPLE MATCHES FOR WRRAPER_MSDISPLAY ===")
for m in re.finditer(b"Wrraper_MSDisplay[A-Za-z0-9_]*", vmax_raw):
    print(" ", m.group(0).decode(errors='ignore'))

print("\n=== SAMPLE MATCHES FOR DEVICECOMMUNICATOR ===")
for m in re.finditer(b"DeviceCommunicat[A-Za-z0-9_]*", vmax_raw):
    print(" ", m.group(0).decode(errors='ignore'))

