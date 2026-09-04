import os, re

release_dir = "/home/tor/vmax_bundle/bin/Release"

for fname in os.listdir(release_dir):
    if fname.endswith(('.dll', '.exe')):
        fpath = os.path.join(release_dir, fname)
        raw = open(fpath, 'rb').read()
        aic_matches = re.findall(b'AICDisp[A-Za-z0-9_]*', raw)
        ms_matches = re.findall(b'MSDisplay[A-Za-z0-9_]*', raw)
        if aic_matches or ms_matches:
            print(f"\n==========================================")
            print(f"File: {fname}")
            print(f"==========================================")
            print("AICDisp matches:", set([m.decode(errors='ignore') for m in aic_matches]))
            print("MSDisplay matches:", set([m.decode(errors='ignore') for m in ms_matches]))

