#!/usr/bin/env python3
"""
Alignment & Solid Pattern Test Execution Script (`run_alignment_experiment.py`)

Submits solid color and line alignment frames directly to EP 0x02 Bulk OUT via usbfs:
1. --pattern align: 1px (Red) / 8px (Green) / 16px (Blue) line alignment markers
2. --duration: Stream duration in seconds (default: 10 seconds)
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

def build_msdisplay_frame(jpeg_bytes: bytes, width: int = 2560, height: int = 666) -> bytes:
    header = struct.pack("<IHHHH", MSDISPLAY_MAGIC_SIGNATURE, width, height, 0, 0)
    return header + jpeg_bytes

def unbind_cdc_acm():
    unbind_path = "/sys/bus/usb/drivers/cdc_acm/unbind"
    if os.path.exists(unbind_path):
        try:
            with open(unbind_path, 'w') as f:
                f.write("1-9:1.1\n")
        except Exception: pass

def run_pattern_test(pattern_name="align", duration_sec=10.0):
    unbind_cdc_acm()

    dev_path = find_target_usb_device(0x33c3, 0xf101)
    if not dev_path:
        print("[ERROR] USB device node 33c3:f101 not dynamically accessible.")
        return

    pattern_file = os.path.join("solid_patterns", f"{pattern_name}.jpg") if pattern_name != "align" else "solid_patterns/alignment_markers.jpg"
    if not os.path.exists(pattern_file):
        print(f"[ERROR] Pattern file '{pattern_file}' not found.")
        return

    with open(pattern_file, 'rb') as f:
        jpeg_bytes = f.read()

    payload = build_msdisplay_frame(jpeg_bytes)

    fd = os.open(dev_path, os.O_RDWR)
    iface_buf = struct.pack("I", 1)

    try:
        fcntl.ioctl(fd, USBDEVFS_CLAIMINTERFACE, iface_buf)
        print(f"=== Alignment & Solid Pattern Execution (Pattern: {pattern_name.upper()}, Duration: {duration_sec}s) ===")
        print(f"  Pattern File   : {pattern_file}")
        print(f"  JPEG Size      : {len(jpeg_bytes)} bytes")
        print(f"  Payload Size   : {len(payload)} bytes (12B Header + JPEG)")

        data_buf = ctypes.create_string_buffer(payload)
        bulk_req = usbdevfs_bulktransfer()
        bulk_req.ep = 0x02
        bulk_req.len = len(payload)
        bulk_req.timeout = 1000
        bulk_req.data = ctypes.cast(data_buf, ctypes.c_void_p)

        start_time = time.monotonic()
        count = 0
        while (time.monotonic() - start_time) < duration_sec:
            res = fcntl.ioctl(fd, USBDEVFS_BULK, bulk_req)
            count += 1
            if count % 30 == 0 or count == 1:
                elapsed = time.monotonic() - start_time
                print(f"  [STREAMING] Sent {count} frames | Elapsed: {elapsed:.1f}s / {duration_sec}s")
            time.sleep(0.033) # ~30 FPS

        print(f"[SUCCESS] Streamed {count} frames over {duration_sec} seconds to EP 0x02 Bulk OUT.")
        print("\n  OBSERVE LCD PANEL NOW: Record line alignment and display stability.")

    except Exception as e:
        print(f"[ERROR] Transfer error: {e}")
    finally:
        try: fcntl.ioctl(fd, USBDEVFS_RELEASEINTERFACE, iface_buf)
        except Exception: pass
        os.close(fd)

def main():
    parser = argparse.ArgumentParser(description="Solid Pattern & Alignment Test Runner")
    parser.add_argument('--pattern', choices=['align', 'solid_black', 'solid_white', 'solid_red', 'solid_green', 'solid_blue'], default='align')
    parser.add_argument('--duration', type=float, default=10.0, help="Stream duration in seconds (default: 10)")
    args = parser.parse_args()
    run_pattern_test(args.pattern, duration_sec=args.duration)

if __name__ == "__main__":
    main()
