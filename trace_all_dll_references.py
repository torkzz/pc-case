import os, subprocess, re

release_dir = "/home/tor/vmax_bundle/bin/Release"

print("=== CHECKING P/INVOKE & ASSEMBLY REFERENCES ACROSS ALL DLLs ===")

dll_files = [f for f in os.listdir(release_dir) if f.endswith(('.dll', '.exe'))]

msdisplay_users = []
devcomm_users = []
hid_users = []

for f in dll_files:
    fpath = os.path.join(release_dir, f)
    # Check strings for MSDISPLAYSDKWRRAPER or DeviceCommunicationLibrary
    try:
        raw = open(fpath, 'rb').read()
        if b"MSDISPLAYSDKWRRAPER" in raw:
            msdisplay_users.append(f)
        if b"DeviceCommunicationLibrary" in raw or b"DeviceCommunicator" in raw:
            devcomm_users.append(f)
        if b"HidSharp" in raw or b"HidLibrary" in raw:
            hid_users.append(f)
    except Exception as e:
        pass

print(f"Files referencing MSDISPLAYSDKWRRAPER: {msdisplay_users}")
print(f"Files referencing DeviceCommunicationLibrary: {devcomm_users}")
print(f"Files referencing HID Libraries: {hid_users}")

