import os, sys, glob

bundle_path = "/home/tor/vmax_bundle"
exes = []
for root, dirs, files in os.walk(bundle_path):
    for f in files:
        if f.endswith('.exe'):
            fp = os.path.join(root, f)
            sz = os.path.getsize(fp)
            exes.append((f, sz, fp))

print("=== ALL EXECUTABLES IN VMAX BUNDLE ===")
for name, sz, fp in sorted(exes):
    print(f"{name:<35} | {sz:>10} bytes | {fp}")

