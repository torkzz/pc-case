#!/usr/bin/env python3
"""
2560x1332 Full-Screen High-DPI Panel Test (`test_1332_full_screen.py`)

Physical Observation Finding:
- 2560x666 renders on top half of LCD screen (~333/666 pixels rendered).
- Physical panel resolution is 2560x1332 (Dual 666-pixel scanout / 2x high-DPI scaling).

Constructs 2560x1332 4-Quarter Block Diagnostic Frame:
- Quarter 1 (Y: 0-333): Solid Red
- Quarter 2 (Y: 333-666): Solid Green
- Quarter 3 (Y: 666-999): Solid Blue
- Quarter 4 (Y: 999-1332): Solid White
"""

import os
import sys
import struct
import fcntl
import ctypes
import subprocess

WIDTH = 2560
HEIGHT = 1332
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

def generate_1332_jpeg():
    ppm_file = os.path.join(OUT_DIR, "pattern_2560x1332.ppm")
    jpg_file = os.path.join(OUT_DIR, "pattern_2560x1332.jpg")

    header = f"P6\n{WIDTH} {HEIGHT}\n255\n".encode('ascii')
    pixels = bytearray(WIDTH * HEIGHT * 3)

    q1 = 333
    q2 = 666
    q3 = 999

    for y in range(HEIGHT):
        if y < q1: r, g, b = 255, 0, 0        # Red
        elif y < q2: r, g, b = 0, 255, 0      # Green
        elif y < q3: r, g, b = 0, 0, 255      # Blue
        else: r, g, b = 255, 255, 255         # White

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

def run_1332_test():
    jpg_file = generate_1332_jpeg()
    with open(jpg_file, 'rb') as f:
        jpeg_bytes = f.read()

    # Header 2560x1332 (0x0A00 x 0x0534)
    hdr = struct.pack("<IHHHH", MSDISPLAY_MAGIC_SIGNATURE, WIDTH, HEIGHT, 0, 0)
    payload = hdr + jpeg_bytes

    print(f"=== 2560x1332 Full-Screen Resolution Test ===")
    print(f"  Header Hex (12B): {hdr.hex(' ')}")
    print(f"  JPEG Dimensions : 2560 x 1332")
    print(f"  JPEG Byte Size  : {len(jpeg_bytes)} bytes")
    print(f"  Total Payload   : {len(payload)} bytes")

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
        print(f"  [ACTION] OBSERVE PHYSICAL LCD PANEL NOW: Check if 2560x1332 image covers FULL LCD SCREEN.")
    except Exception as e:
        print(f"  [ERROR] USB transfer error: {e}")
    finally:
        try: fcntl.ioctl(fd, USBDEVFS_RELEASEINTERFACE, iface_buf)
        except Exception: pass
        os.close(fd)

if __name__ == "__main__":
    run_1332_test()
