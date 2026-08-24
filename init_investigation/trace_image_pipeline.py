import os, sys, re, subprocess

bundle_path = "/home/tor/vmax_bundle/bin/Release"

print("=== IMAGE PIPELINE & TURBOJPEG CALLERS ===")
for root, dirs, files in os.walk(bundle_path):
    for f in files:
        if f.endswith(('.dll', '.exe')):
            fp = os.path.join(root, f)
            try:
                data = open(fp, 'rb').read()
                matches = []
                for kw in [b'tj3Init', b'tj3Compress', b'MSDisplaySendPicture', b'SendPicture', b'DownloadData', b'SendFrame', b'MSDISPLAYSDKWRRAPER']:
                    if kw in data:
                        matches.append(kw.decode('ascii', errors='ignore'))
                if matches:
                    print(f"File {f}: {matches}")
            except Exception:
                pass

print("\n=== MSDISPLAYSDKWRRAPER.DLL EXPORT & CALL ANALYSIS ===")
sdk_dll = os.path.join(bundle_path, "MSDISPLAYSDKWRRAPER.dll")
if os.path.exists(sdk_dll):
    data = open(sdk_dll, 'rb').read()
    # Find all ASCII strings containing vid, pid, USB, 33c3, 345f, 9132, f101
    str_matches = [m.group(0).decode('ascii', errors='ignore') for m in re.finditer(b'[\x20-\x7e]{4,}', data) if any(k in m.group(0).lower() for k in [b'vid', b'pid', b'33c3', b'345f', b'9132', b'f101', b'usb', b'display'])]
    print("MSDISPLAYSDKWRRAPER string matches:")
    for s in str_matches[:40]:
        print("  ", s)

