#!/usr/bin/env python3
"""
MSDisplay Line Stride Lock & Motion Elimination Test (`test_stride_lock.py`)

Physical Observation Finding:
- Image appears to be "moving / scrolling".
- Cause: Line pitch / stride mismatch at Offset 0x08 in 12-byte MSDisplay header.
- When Offset 0x08 = 0, line pitch defaults to unaligned hardware buffer.
- Correct Stride values for 640-pixel width:
  - Stride = 1920 (0x0780) -> 640 * 3 bytes/pixel (24-bit RGB line pitch)
  - Stride = 2560 (0x0A00) -> 640 * 4 bytes/pixel (32-bit RGBA line pitch)
  - Stride = 1280 (0x0500) -> 640 * 2 bytes/pixel (16-bit YUV422 line pitch)
"""

import sys
import os
import time
import struct
import fcntl
import ctypes
import argparse

WIDTH = 640
HEIGHT = 1920
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

def get_test_jpeg():
    jpg_path = os.path.join(OUT_DIR, "pattern_640x1920.jpg")
    if os.path.exists(jpg_path):
        with open(jpg_path, 'rb') as f: return f.read()
    default_jpg = "/home/tor/pc-case-lcd/vmax_test_2560x666.jpg"
    with open(default_jpg, 'rb') as f: return f.read()

def run_stride_test(stride_val=1920, duration_sec=10.0):
    unbind_cdc_acm()
    dev_path = find_target_usb_device(0x33c3, 0xf101)
    if not dev_path:
        print("[ERROR] USB device 33c3:f101 not found.")
        return

    jpeg_bytes = get_test_jpeg()

    # Build Header with Offset 0x08 = stride_val
    hdr = struct.pack("<IHHHH", MSDISPLAY_MAGIC_SIGNATURE, WIDTH, HEIGHT, stride_val, 1)
    payload = hdr + jpeg_bytes

    print(f"=== Line Stride Lock Test (Stride={stride_val} / 0x{stride_val:04x}, Duration={duration_sec}s) ===")
    print(f"  Header Hex (12B) : {hdr.hex(' ')}")
    print(f"  Payload Size     : {len(payload)} bytes")
    print(f"  Target Device    : {dev_path}")

    fd = os.open(dev_path, os.O_RDWR)
    iface_buf = struct.pack("I", 1)

    try:
        fcntl.ioctl(fd, USBDEVFS_CLAIMINTERFACE, iface_buf)
        start_time = time.monotonic()
        tx_count = 0

        while (time.monotonic() - start_time) < duration_sec:
            data_buf = ctypes.create_string_buffer(payload)
            bulk_req = usbdevfs_bulktransfer()
            bulk_req.ep = 0x02
            bulk_req.len = len(payload)
            bulk_req.timeout = 1000
            bulk_req.data = ctypes.cast(data_buf, ctypes.c_void_p)

            res = fcntl.ioctl(fd, USBDEVFS_BULK, bulk_req)
            tx_count += 1
            time.sleep(0.033) # 30 FPS

        print(f"\n  [SUCCESS] Streamed {tx_count} frames over {duration_sec}s with Stride={stride_val}.")
        print("  [ACTION] OBSERVE PHYSICAL LCD PANEL NOW: Check if motion/scrolling STOPS completely.")
    except Exception as e:
        print(f"  [ERROR] USB transfer error: {e}")
    finally:
        try: fcntl.ioctl(fd, USBDEVFS_RELEASEINTERFACE, iface_buf)
        except Exception: pass
        os.close(fd)

def main():
    parser = argparse.ArgumentParser(description="MSDisplay Line Stride Lock Test")
    parser.add_argument('--stride', type=int, default=1920, help="Line stride value at Offset 0x08 (default: 1920)")
    parser.add_argument('--duration', type=float, default=10.0, help="Stream duration in seconds (default: 10)")
    args = parser.parse_args()
    run_stride_test(stride_val=args.stride, duration_sec=args.duration)

if __name__ == "__main__":
    main()
