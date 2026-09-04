import os, sys, glob, re

bundle_path = "/home/tor/vmax_bundle"

print("=== 1. SEARCHING CONFIG & XML FILES ===")
for root, dirs, files in os.walk(bundle_path):
    for f in files:
        if f.endswith(('.config', '.xml', '.json', '.ini', '.inf', '.txt')):
            fp = os.path.join(root, f)
            try:
                txt = open(fp, 'r', errors='ignore').read()
                if any(k in txt.lower() for k in ['33c3', 'f101', 'vmax', 'msdisplay', 'usb', 'baud', 'com']):
                    print(f"File: {fp}")
                    for line in txt.splitlines():
                        if any(k in line.lower() for k in ['33c3', 'f101', 'vmax', 'msdisplay', 'baud', 'com', 'port', 'driver']):
                            print(f"  {line.strip()[:120]}")
            except Exception:
                pass

print("\n=== 2. SEARCHING DLL / EXE BINARY CONSTANTS ===")
for root, dirs, files in os.walk(bundle_path):
    for f in files:
        if f.endswith(('.dll', '.exe')):
            fp = os.path.join(root, f)
            try:
                data = open(fp, 'rb').read()
                matches = re.findall(rb'33[cC]3|f101|F101|HL-VMAX|MacroSilicon|MSDisplay|UsbDisplay', data)
                if matches:
                    unique = set(m.decode('ascii', errors='ignore') for m in matches)
                    print(f"Binary: {f} -> Matches: {unique}")
            except Exception:
                pass

