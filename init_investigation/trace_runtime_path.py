import os, sys, re, subprocess

vmax_dir = "/home/tor/vmax_bundle/bin/Release"
libusb_dir = "/home/tor/vmax_bundle/libusb"

print("=== TASK 3: SEARCHING ALL BINARIES & INFS FOR VID / PID STRINGS ===")

target_vids = [b"33c3", b"33C3", b"345f", b"345F", b"f101", b"F101", b"9132"]

def search_file(filepath):
    try:
        data = open(filepath, 'rb').read()
        found = []
        for vid in target_vids:
            if vid in data:
                found.append(vid.decode('ascii'))
        return found
    except Exception as e:
        return []

for root, dirs, files in os.walk("/home/tor/vmax_bundle"):
    for f in files:
        fp = os.path.join(root, f)
        res = search_file(fp)
        if res:
            print(f"File {fp} contains target VID/PID strings: {set(res)}")

print("\n=== TASK 1 & 2: DISCOVERING CALL SITES IN DeviceCommunicationLibrary.il ===")
il_file = "/home/tor/pc-case-lcd/DeviceCommunicationLibrary.il"
if os.path.exists(il_file):
    il_text = open(il_file, 'r').read()
    
    serial_references = []
    for line_no, line in enumerate(il_text.splitlines(), 1):
        if any(k in line for k in ['SerialPort', 'Open', 'Write', 'Read', 'GetPortNames', 'baudRate']):
            serial_references.append((line_no, line.strip()))
            
    print(f"Found {len(serial_references)} SerialPort references in DeviceCommunicationLibrary.il:")
    for lno, lstr in serial_references[:30]:
        print(f"  Line {lno}: {lstr}")

