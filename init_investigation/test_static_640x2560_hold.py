#!/usr/bin/env python3
"""
Static Single-Frame Hold Test for 640x2560 Portrait Panel (`test_static_640x2560_hold.py`)

Fixes rapid blinking/moving:
- Sends ONE SINGLE frame (Seq=1).
- Keeps usbfs interface claimed and device handle open.
- Does NOT loop or spam transfers.
- Holds for --hold seconds (default: 15s).
"""

import os
import sys
import time
import struct
import fcntl
import ctypes
import subprocess
import argparse

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

    if not os.path.exists(jpg_file):
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

def run_single_hold_test(hold_sec=15.0):
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
        print(f"=== Static Single-Frame Hold Test ({hold_sec}s Hold) ===")

        # Header 640x2560 (W=640 0x0280, H=2560 0x0A00, Seq=1)
        hdr = struct.pack("<IHHHH", MSDISPLAY_MAGIC_SIGNATURE, WIDTH, HEIGHT, 0, 1)
        payload = hdr + jpeg_bytes

        data_buf = ctypes.create_string_buffer(payload)
        bulk_req = usbdevfs_bulktransfer()
        bulk_req.ep = 0x02
        bulk_req.len = len(payload)
        bulk_req.timeout = 3000
        bulk_req.data = ctypes.cast(data_buf, ctypes.c_void_p)

        res = fcntl.ioctl(fd, USBDEVFS_BULK, bulk_req)
        print(f"  Single Frame Submitted -> USB Status: {res} bytes OK")
        print(f"  [STATUS] Holding handle open for {hold_sec} seconds WITHOUT sending new frames...")

        start_time = time.monotonic()
        while (time.monotonic() - start_time) < hold_sec:
            time.sleep(0.5)

        print(f"\n  [SUCCESS] Single static frame held for {hold_sec}s.")
        print("  [ACTION] OBSERVE PHYSICAL LCD PANEL NOW: Check if image is static, non-blinking, and stable.")

    except Exception as e:
        print(f"  [ERROR] USB transfer error: {e}")
    finally:
        try: fcntl.ioctl(fd, USBDEVFS_RELEASEINTERFACE, iface_buf)
        except Exception: pass
        os.close(fd)

def main():
    parser = argparse.ArgumentParser(description="Static Single-Frame Hold Test")
    parser.add_argument('--hold', type=float, default=15.0, help="Hold duration in seconds (default: 15)")
    args = parser.parse_args()
    run_single_hold_test(args.hold)

if __name__ == "__main__":
    main()
