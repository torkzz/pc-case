#!/usr/bin/env python3
"""
MSDisplay Image Rotation Test Runner (`msdisplay_rotation_test.py`)

Streams 4 rotation variants of the 4-quarter block diagnostic pattern:
1. --rot rot0   : 2560x666 (0 deg)
2. --rot rot90  : 666x2560 (90 deg CW)
3. --rot rot180 : 2560x666 (180 deg)
4. --rot rot270 : 666x2560 (270 deg CW)

Updates MSDisplay 12-byte header dynamically to match rotated JPEG dimensions.
"""

import sys
import os
import time
import struct
import fcntl
import ctypes
import argparse

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

def build_msdisplay_frame(jpeg_bytes: bytes, width: int, height: int) -> bytes:
    header = struct.pack("<IHHHH", MSDISPLAY_MAGIC_SIGNATURE, width, height, 0, 0)
    return header + jpeg_bytes

def unbind_cdc_acm():
    unbind_path = "/sys/bus/usb/drivers/cdc_acm/unbind"
    if os.path.exists(unbind_path):
        try:
            with open(unbind_path, 'w') as f:
                f.write("1-9:1.1\n")
        except Exception: pass

def run_rotation_test(rot="rot90", duration_sec=10.0):
    unbind_cdc_acm()

    dev_path = find_target_usb_device(0x33c3, 0xf101)
    if not dev_path:
        print("[ERROR] USB device 33c3:f101 not found.")
        return

    rot_info = {
        'rot0': (2560, 666, "diagnostic_patterns/4quarter_rot0.jpg"),
        'rot90': (666, 2560, "diagnostic_patterns/4quarter_rot90.jpg"),
        'rot180': (2560, 666, "diagnostic_patterns/4quarter_rot180.jpg"),
        'rot270': (666, 2560, "diagnostic_patterns/4quarter_rot270.jpg")
    }

    if rot not in rot_info:
        print(f"[ERROR] Invalid rotation '{rot}'. Choices: {list(rot_info.keys())}")
        return

    width, height, jpg_path = rot_info[rot]

    if not os.path.exists(jpg_path):
        print(f"[ERROR] Image file '{jpg_path}' not found. Run generate_rotated_patterns.py first.")
        return

    with open(jpg_path, 'rb') as f:
        jpeg_bytes = f.read()

    hdr = struct.pack("<IHHHH", MSDISPLAY_MAGIC_SIGNATURE, width, height, 0, 0)
    payload = hdr + jpeg_bytes

    print(f"\n==================================================")
    print(f"MSDISPLAY ROTATION EXPERIMENT — {rot.upper()}")
    print(f"  Target Device Node : {dev_path}")
    print(f"  Image File         : {jpg_path}")
    print(f"  Header Dimensions  : {width} x {height}")
    print(f"  Header Hex (12B)   : {hdr.hex(' ')}")
    print(f"  JPEG Size          : {len(jpeg_bytes)} bytes")
    print(f"  Total Payload      : {len(payload)} bytes")
    print(f"==================================================")

    fd = os.open(dev_path, os.O_RDWR)
    iface_buf = struct.pack("I", 1)

    try:
        fcntl.ioctl(fd, USBDEVFS_CLAIMINTERFACE, iface_buf)
        start_time = time.monotonic()
        frame_count = 0

        while (time.monotonic() - start_time) < duration_sec:
            data_buf = ctypes.create_string_buffer(payload)
            bulk_req = usbdevfs_bulktransfer()
            bulk_req.ep = 0x02
            bulk_req.len = len(payload)
            bulk_req.timeout = 1000
            bulk_req.data = ctypes.cast(data_buf, ctypes.c_void_p)

            res = fcntl.ioctl(fd, USBDEVFS_BULK, bulk_req)
            frame_count += 1

            if frame_count % 30 == 0 or frame_count == 1:
                elapsed = time.monotonic() - start_time
                print(f"  [STREAMING] Sent {frame_count} frames ({frame_count * len(payload)} bytes) | Elapsed: {elapsed:.1f}s / {duration_sec}s")

            time.sleep(0.033)

        print(f"\n  [SUCCESS] Streamed {frame_count} frames ({frame_count * len(payload)} bytes) over {duration_sec}s for {rot.upper()}.")
        print(f"  [ACTION] OBSERVE PHYSICAL LCD PANEL NOW.")
    except Exception as e:
        print(f"  [ERROR] USB transfer error: {e}")
    finally:
        try: fcntl.ioctl(fd, USBDEVFS_RELEASEINTERFACE, iface_buf)
        except Exception: pass
        os.close(fd)

def main():
    parser = argparse.ArgumentParser(description="MSDisplay Image Rotation Test Runner")
    parser.add_argument('--rot', choices=['rot0', 'rot90', 'rot180', 'rot270'], default='rot90', help="Rotation angle (rot0, rot90, rot180, rot270)")
    parser.add_argument('--duration', type=float, default=10.0, help="Stream duration in seconds (default: 10)")

    args = parser.parse_args()
    run_rotation_test(args.rot, duration_sec=args.duration)

if __name__ == "__main__":
    main()
