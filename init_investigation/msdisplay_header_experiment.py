#!/usr/bin/env python3
"""
4-Quarter Block Image & Header Field Experiment Utility (`msdisplay_header_experiment.py`)

Generates 2560x666 4-Quarter Block Diagnostic Image (No gradients, no background):
- Quarter 1 (Y: 0-166): Solid Red (255, 0, 0)
- Quarter 2 (Y: 166-333): Solid Green (0, 255, 0)
- Quarter 3 (Y: 333-499): Solid Blue (0, 0, 255)
- Quarter 4 (Y: 499-666): Solid White (255, 255, 255)

Executes controlled MSDisplay 12-byte header field variations (one parameter changed at a time):
- Variant 1 (Baseline): Magic=0x0008100A, W=2560, H=666, Stride=0, Flag=0
- Variant 2 (Stride=2560): Stride=2560 (0x0A00)
- Variant 3 (Format=1): Stride=1
- Variant 4 (Flag=1): Flag=1
- Variant 5 (Big-Endian Header): Magic=0x0A100800, W=2560, H=666
"""

import os
import sys
import time
import struct
import fcntl
import ctypes
import subprocess
import argparse

WIDTH = 2560
HEIGHT = 666
OUT_DIR = "diagnostic_patterns"
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

def generate_4quarter_jpeg():
    ppm_file = os.path.join(OUT_DIR, "4quarter_blocks.ppm")
    jpg_file = os.path.join(OUT_DIR, "4quarter_blocks.jpg")

    header = f"P6\n{WIDTH} {HEIGHT}\n255\n".encode('ascii')
    pixels = bytearray(WIDTH * HEIGHT * 3)

    q1_end = 166
    q2_end = 333
    q3_end = 499

    for y in range(HEIGHT):
        if y < q1_end:
            r, g, b = 255, 0, 0      # Red
        elif y < q2_end:
            r, g, b = 0, 255, 0      # Green
        elif y < q3_end:
            r, g, b = 0, 0, 255      # Blue
        else:
            r, g, b = 255, 255, 255  # White

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

def run_header_variant_test(variant=1):
    jpg_file = generate_4quarter_jpeg()
    with open(jpg_file, 'rb') as f:
        jpeg_bytes = f.read()

    # Define Header Variants
    if variant == 1:
        # Baseline Little-Endian Header
        hdr = struct.pack("<IHHHH", MSDISPLAY_MAGIC_SIGNATURE, WIDTH, HEIGHT, 0, 0)
        desc = "Variant 1 (Baseline: Magic=0x0008100A, W=2560, H=666, Stride=0, Flag=0)"
    elif variant == 2:
        # Stride = 2560
        hdr = struct.pack("<IHHHH", MSDISPLAY_MAGIC_SIGNATURE, WIDTH, HEIGHT, 2560, 0)
        desc = "Variant 2 (Stride=2560: Stride=0x0A00)"
    elif variant == 3:
        # Format/Stride = 1
        hdr = struct.pack("<IHHHH", MSDISPLAY_MAGIC_SIGNATURE, WIDTH, HEIGHT, 1, 0)
        desc = "Variant 3 (Format=1: Format Specifier=1)"
    elif variant == 4:
        # Flag = 1
        hdr = struct.pack("<IHHHH", MSDISPLAY_MAGIC_SIGNATURE, WIDTH, HEIGHT, 0, 1)
        desc = "Variant 4 (Flag=1: Quality Flag=1)"
    elif variant == 5:
        # Big-Endian Header Format
        hdr = struct.pack(">IHHHH", MSDISPLAY_MAGIC_SIGNATURE, WIDTH, HEIGHT, 0, 0)
        desc = "Variant 5 (Big-Endian Header Format)"

    payload = hdr + jpeg_bytes

    print(f"\n==================================================")
    print(f"HEADER EXPERIMENT — {desc}")
    print(f"  Header Hex (12B): {hdr.hex(' ')}")
    print(f"  JPEG File       : {jpg_file}")
    print(f"  JPEG Byte Size  : {len(jpeg_bytes)} bytes (JPEG Dimensions: 2560x666)")
    print(f"  Total Payload   : {len(payload)} bytes")
    print(f"==================================================")

    dev_path = find_target_usb_device(0x33c3, 0xf101)
    if not dev_path:
        print("[ERROR] USB device 33c3:f101 not found.")
        return

    unbind_cdc_acm()
    fd = os.open(dev_path, os.O_RDWR)
    iface_buf = struct.pack("I", 1)

    try:
        fcntl.ioctl(fd, USBDEVFS_CLAIMINTERFACE, iface_buf)
        data_buf = ctypes.create_string_buffer(payload)
        bulk_req = usbdevfs_bulktransfer()
        bulk_req.ep = 0x02
        bulk_req.len = len(payload)
        bulk_req.timeout = 3000
        bulk_req.data = ctypes.cast(data_buf, ctypes.c_void_p)

        res = fcntl.ioctl(fd, USBDEVFS_BULK, bulk_req)
        print(f"  [SUCCESS] USB Transfer Status: {res} bytes submitted successfully to EP 0x02 Bulk OUT.")
        print(f"  [ACTION] OBSERVE PHYSICAL LCD PANEL NOW & RECORD RENDER RESULT FOR VARIANT {variant}.")
    except Exception as e:
        print(f"  [ERROR] USB transfer error: {e}")
    finally:
        try: fcntl.ioctl(fd, USBDEVFS_RELEASEINTERFACE, iface_buf)
        except Exception: pass
        os.close(fd)

def main():
    parser = argparse.ArgumentParser(description="MSDisplay Controlled Header Field Experiment")
    parser.add_argument('--variant', type=int, choices=[1, 2, 3, 4, 5], default=1, help="Header variant number (1..5)")

    args = parser.parse_args()
    run_header_variant_test(args.variant)

if __name__ == "__main__":
    main()
