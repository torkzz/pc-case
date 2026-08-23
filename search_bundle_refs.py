import os, re

bundle_path = "/home/tor/vmax_bundle"
targets = ["33c3", "f101", "345f", "9132", "MSDISPLAY", "MacroSilicon", "libusb", "DeviceCommunicator", "VMAX", "HL"]

matches = []

for root, dirs, files in os.walk(bundle_path):
    for fname in files:
        fpath = os.path.join(root, fname)
        if fname.endswith(('.dll', '.exe', '.config', '.json', '.xml', '.ini', '.inf', '.db', '.txt')):
            try:
                with open(fpath, 'rb') as f:
                    content = f.read()
                    for t in targets:
                        if re.search(t.encode('utf-8'), content, re.IGNORECASE):
                            matches.append((fpath, t))
            except Exception as e:
                pass

print(f"Found {len(matches)} matching references:")
for path, kw in matches:
    print(f"  [{kw}] {path}")

