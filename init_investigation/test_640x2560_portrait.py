#!/usr/bin/env python3
"""
640x2560 Native Portrait Panel Resolution Test (`test_640x2560_portrait.py`)

Physical Observation Finding:
- Red, Green, Blue render cleanly in upper/middle sections.
- 2560 pixels height = 4 x 640px bands (640 * 4 = 2560).
- True physical width = 640 (640x2560 = 1:4 exact aspect ratio).

Constructs 640x2560 4-Band Frame:
- Band 1 (Y: 0 - 640)    : Solid Red (255, 0, 0)
- Band 2 (Y: 640 - 1280) : Solid Green (0, 255, 0)
- Band 3 (Y: 1280 - 1920): Solid Blue (0, 0, 255)
- Band 4 (Y: 1920 - 2560): Solid White (255, 255, 255)
"""

import os
import sys
import time
import struct
import fcntl
import ctypes
import subprocess

WIDTH = 640
HEIGHT = 2560
OUT_DIR = "portrait_patterns"
os.makedirs(OUT_DIR, exist_ok=True)

USBDEVFS_BULK = 0xc0185502
USBDEVFS_CLAIMINTERFACE = 0x8004550f
USBDEVFS_RELEASEINTERFACE = 0x80045510

class usbdevfs_bulktransfer(ctypes.Structure):
    _fields_ = [
        ('ep', ctypes.c_uint),
        ('len', ctypes.c_uint),
        ('timeout', ctypes.c_uint),
        ('data', ctypes.c_void_p),
    ]

MSDISPLAY_MAGIC_SIGNATURE = 0x0008100A

def generate_640x2560_jpeg():
    ppm_file = os.path.join(OUT_DIR, "pattern_640x2560.ppm")
    jpg_file = os.path.join(OUT_DIR, "pattern_640x2560.jpg")

    header = f"P6\n{WIDTH} {HEIGHT}\n255\n".encode('ascii')
    pixels = bytearray(WIDTH * HEIGHT * 3)

    b1 = 640
    b2 = 1280
    b3 = 1920

    for y in range(HEIGHT):
        if y < b1: r, g, b = 255, 0, 0         # Red (Band 1: Top)
        elif y < b2: r, g, b = 0, 255, 0       # Green (Band 2: Upper Mid)
        elif y < b3: r, g, b = 0, 0, 255       # Blue (Band 3: Lower Mid)
        else: r, g, b = 255, 255, 255          # White (Band 4: Bottom)

        for x in range(WIDTH):
            idx = (y * WIDTH + x) * 3
            pixels[idx] = r
            pixels[idx+1] = g
            pixels[idx+2] = b

    with open(ppm_file, 'wb') as f:
        f.write(header)
        f.write(pixels)

    cmd = ['ffmpeg', '-y', '-i', ppm_file, '-q:v', '2', jpg_file]
    subprocess.check_call(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return jpg_file

def find_target_usb_device(vid=0x33c3, pid=0xf101):
    usb_dir = '/sys/bus/usb/devices'
    if not os.path.exists(usb_dir): return None
    for entry in os.listdir(usb_dir):
        dev_path = os.path.join(usb_dir, entry)
        v_f, p_f = os.path.join(dev_path, 'idVendor'), os.path.join(dev_path, 'idProduct')
        if os.path.exists(v_f) and os.path.exists(p_f):
            try:
                v = open(v_f).read().strip().lower()
                p = open(p_f).read().strip().lower()
                if v == f"{vid:04x}" and p == f"{pid:04x}":
                    d_f, b_f = os.path.join(dev_path, 'devnum'), os.path.join(dev_path, 'busnum')
                    if os.path.exists(d_f) and os.path.exists(b_f):
                        d = int(open(d_f).read().strip())
                        b = int(open(b_f).read().strip())
                        node = f"/dev/bus/usb/{b:03d}/{d:03d}"
                        if os.path.exists(node): return node
            except Exception: pass
    return None

def unbind_cdc_acm():
    unbind_path = "/sys/bus/usb/drivers/cdc_acm/unbind"
    if os.path.exists(unbind_path):
        try:
            with open(unbind_path, 'w') as f:
                f.write("1-9:1.1\n")
        except Exception: pass

def run_640x2560_test(iterations=10):
    jpg_file = generate_640x2560_jpeg()
    with open(jpg_file, 'rb') as f:
        jpeg_bytes = f.read()

    dev_path = find_target_usb_device(0x33c3, 0xf101)
    if not dev_path:
        print("[ERROR] USB device 33c3:f101 not found.")
        return

    unbind_cdc_acm()
    fd = os.open(dev_path, os.O_RDWR)
    iface_buf = struct.pack("I", 1)

    try:
        fcntl.ioctl(fd, USBDEVFS_CLAIMINTERFACE, iface_buf)
        print(f"=== 640x2560 Native Portrait Test ({iterations} Frames) ===")

        for seq in range(1, iterations + 1):
            # Header 640x2560 (W=640 0x0280, H=2560 0x0A00, Offset 0x0A = seq)
            hdr = struct.pack("<IHHHH", MSDISPLAY_MAGIC_SIGNATURE, WIDTH, HEIGHT, 0, seq)
            payload = hdr + jpeg_bytes

            data_buf = ctypes.create_string_buffer(payload)
            bulk_req = usbdevfs_bulktransfer()
            bulk_req.ep = 0x02
            bulk_req.len = len(payload)
            bulk_req.timeout = 1000
            bulk_req.data = ctypes.cast(data_buf, ctypes.c_void_p)

            res = fcntl.ioctl(fd, USBDEVFS_BULK, bulk_req)
            print(f"  Frame {seq:02d}/{iterations} (Header W=640, H=2560, Seq={seq}) -> USB Status: {res} bytes OK")
            time.sleep(0.05)

        print("\n  [SUCCESS] All 640x2560 frames submitted successfully!")
        print("  [ACTION] OBSERVE PHYSICAL LCD PANEL NOW: Check if Red, Green, Blue, White fit 100% full portrait screen.")

    except Exception as e:
        print(f"  [ERROR] USB transfer error: {e}")
    finally:
        try: fcntl.ioctl(fd, USBDEVFS_RELEASEINTERFACE, iface_buf)
        except Exception: pass
        os.close(fd)

if __name__ == "__main__":
    run_640x2560_test()
