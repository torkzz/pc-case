#!/usr/bin/env python3
"""
MSDisplay Resolution & Hardware Scalar Experiment (`generate_resolution_experiment.py`)

Generates diagnostic pattern frames for standard MacroSilicon hardware resolutions:
- Resolution R1: 1920x1080 (Solid Red upper, Green mid, Blue lower, 1920x1080 JPEG)
- Resolution R2: 1280x720 (Solid Red upper, Green mid, Blue lower, 1280x720 JPEG)
- Resolution R3: 2560x666 (Baseline ultra-wide bar, 2560x666 JPEG)
"""

import os
import sys
import struct
import fcntl
import ctypes
import subprocess
import argparse

OUT_DIR = "resolution_patterns"
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

def generate_rgb_stripes_jpeg(width, height, filename):
    ppm_file = os.path.join(OUT_DIR, f"stripes_{width}x{height}.ppm")
    jpg_file = os.path.join(OUT_DIR, filename)

    header = f"P6\n{width} {height}\n255\n".encode('ascii')
    pixels = bytearray(width * height * 3)

    h1 = height // 3
    h2 = 2 * (height // 3)

    for y in range(height):
        if y < h1:
            r, g, b = 255, 0, 0     # Red
        elif y < h2:
            r, g, b = 0, 255, 0     # Green
        else:
            r, g, b = 0, 0, 255     # Blue

        for x in range(width):
            idx = (y * width + x) * 3
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

def run_res_test(res_type="1920x1080"):
    if res_type == "1920x1080":
        w, h = 1920, 1080
    elif res_type == "1280x720":
        w, h = 1280, 720
    elif res_type == "2560x666":
        w, h = 2560, 666
    else:
        print(f"[ERROR] Invalid resolution type: {res_type}")
        return

    jpg_file = generate_rgb_stripes_jpeg(w, h, f"pattern_{w}x{h}.jpg")
    with open(jpg_file, 'rb') as f:
        jpeg_bytes = f.read()

    hdr = struct.pack("<IHHHH", MSDISPLAY_MAGIC_SIGNATURE, w, h, 0, 0)
    payload = hdr + jpeg_bytes

    print(f"\n==================================================")
    print(f"HARDWARE SCALAR RESOLUTION EXPERIMENT — {w}x{h}")
    print(f"  Header Hex (12B): {hdr.hex(' ')}")
    print(f"  JPEG Dimensions : {w} x {h}")
    print(f"  JPEG Byte Size  : {len(jpeg_bytes)} bytes")
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
        print(f"  [ACTION] OBSERVE PHYSICAL LCD PANEL NOW & RECORD FULL-SCREEN SCALING FOR {w}x{h}.")
    except Exception as e:
        print(f"  [ERROR] USB transfer error: {e}")
    finally:
        try: fcntl.ioctl(fd, USBDEVFS_RELEASEINTERFACE, iface_buf)
        except Exception: pass
        os.close(fd)

def main():
    parser = argparse.ArgumentParser(description="MSDisplay Resolution & Hardware Scalar Experiment")
    parser.add_argument('--res', choices=['1920x1080', '1280x720', '2560x666'], default='1920x1080')
    args = parser.parse_args()
    run_res_test(args.res)

if __name__ == "__main__":
    main()
