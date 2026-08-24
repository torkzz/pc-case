import os, re

release_dir = "/home/tor/vmax_bundle/bin/Release"

for fname in ["libcompositeScreenModel.dll", "libstack.dll", "common.dll", "CMSMTCInstaller.dll"]:
    fpath = os.path.join(release_dir, fname)
    if os.path.exists(fpath):
        raw = open(fpath, 'rb').read()
        print(f"\n==========================================")
        print(f"FILE: {fname} ({len(raw)} bytes)")
        print(f"==========================================")
        
        # Extract ASCII strings
        strings = re.findall(b'[\x20-\x7e]{4,}', raw)
        clean_strs = [s.decode('ascii', errors='ignore') for s in strings]
        
        # Print relevant strings
        relevant = [s for s in clean_strs if any(k in s for k in ["Screen", "Display", "Device", "Connect", "AIC", "MSDisplay", "33c3", "f101", "345f", "9132", "COM", "tty", "Send", "Frame", "Jpeg", "JPEG"])]
        print(f"Found {len(relevant)} relevant strings:")
        for s in relevant[:30]:
            print("  ", s)

