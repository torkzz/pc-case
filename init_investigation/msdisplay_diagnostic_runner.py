#!/usr/bin/env python3
"""
MSDisplay Diagnostic Runner (`msdisplay_diagnostic_runner.py`)

Executes systematic tests for horizontal corruption diagnosis:
1. --mode single: Transmits ONE single deterministic test frame (Pattern A), logs exact JPEG size and USB byte count, then halts.
2. --mode repeated: Transmits the SAME frame repeatedly (50 iterations) with 100ms delay.
3. --mode alternate: Transmits Pattern A and Pattern B alternately (A -> B -> A -> B) to observe if glitch moves or is fixed to physical Y rows.
4. --mode color-bars: Transmits Pattern C (Horizontal Color Bands: Red, Green, Blue, White, Black).
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
    """Dynamically locates USB device node path in sysfs."""
    usb_dir = '/sys/bus/usb/devices'
    if not os.path.exists(usb_dir):
        return None

    target_vid_hex = f"{vid:04x}"
    target_pid_hex = f"{pid:04x}"

    for entry in os.listdir(usb_dir):
        dev_path = os.path.join(usb_dir, entry)
        vid_file = os.path.join(dev_path, 'idVendor')
        pid_file = os.path.join(dev_path, 'idProduct')

        if os.path.exists(vid_file) and os.path.exists(pid_file):
            try:
                with open(vid_file, 'r') as f: v = f.read().strip().lower()
                with open(pid_file, 'r') as f: p = f.read().strip().lower()
                if v == target_vid_hex and p == target_pid_hex:
                    devnum_f = os.path.join(dev_path, 'devnum')
                    busnum_f = os.path.join(dev_path, 'busnum')
                    if os.path.exists(devnum_f) and os.path.exists(busnum_f):
                        devnum = int(open(devnum_f).read().strip())
                        busnum = int(open(busnum_f).read().strip())
                        node = f"/dev/bus/usb/{busnum:03d}/{devnum:03d}"
                        if os.path.exists(node):
                            return node
            except Exception:
                continue
    return None

def build_msdisplay_frame(jpeg_bytes: bytes, width: int = 2560, height: int = 666) -> bytes:
    """Prepends 12-byte MSDisplay header to JPEG payload [CONFIRMED STATIC]"""
    header = struct.pack("<IHHHH", MSDISPLAY_MAGIC_SIGNATURE, width, height, 0, 0)
    return header + jpeg_bytes

def unbind_cdc_acm():
    unbind_path = "/sys/bus/usb/drivers/cdc_acm/unbind"
    if os.path.exists(unbind_path):
        try:
            with open(unbind_path, 'w') as f:
                f.write("1-9:1.1\n")
        except Exception:
            pass

def send_frame_usbfs(fd, frame_payload, ep=0x02, timeout_ms=3000):
    data_buf = ctypes.create_string_buffer(frame_payload)
    bulk_req = usbdevfs_bulktransfer()
    bulk_req.ep = ep
    bulk_req.len = len(frame_payload)
    bulk_req.timeout = timeout_ms
    bulk_req.data = ctypes.cast(data_buf, ctypes.c_void_p)

    res = fcntl.ioctl(fd, USBDEVFS_BULK, bulk_req)
    return res

def run_diagnostic(mode="single"):
    unbind_cdc_acm()

    dev_path = find_target_usb_device(0x33c3, 0xf101)
    if not dev_path:
        print("[ERROR] USB device node 33c3:f101 not dynamically accessible.")
        return

    print(f"[DYNAMIC LOOKUP] Target Device Node: {dev_path}")

    pattern_a = "diagnostic_patterns/pattern_a_black_grid.jpg"
    pattern_b = "diagnostic_patterns/pattern_b_white_grid.jpg"
    pattern_c = "diagnostic_patterns/pattern_c_color_bars.jpg"

    with open(pattern_a, 'rb') as f: bytes_a = f.read()
    with open(pattern_b, 'rb') as f: bytes_b = f.read()
    with open(pattern_c, 'rb') as f: bytes_c = f.read()

    fd = os.open(dev_path, os.O_RDWR)
    iface_buf = struct.pack("I", 1)

    try:
        fcntl.ioctl(fd, USBDEVFS_CLAIMINTERFACE, iface_buf)
        print(f"=== MSDisplay Diagnostic Test Execution (Mode: {mode.upper()}) ===")

        if mode == "single":
            payload = build_msdisplay_frame(bytes_a)
            print(f"[TEST 1: SINGLE FRAME]")
            print(f"  Image File      : {pattern_a}")
            print(f"  JPEG Byte Size  : {len(bytes_a)} bytes")
            print(f"  Header Size     : 12 bytes (Magic: 0x0008100A, W: 2560, H: 666)")
            print(f"  Total Payload   : {len(payload)} bytes")
            res = send_frame_usbfs(fd, payload)
            print(f"  USB Transfer Result Code: {res} bytes submitted successfully to EP 0x02 Bulk OUT.")
            print("\n  OBSERVE LCD PANEL NOW: Record whether corruption appears on single static frame.")

        elif mode == "repeated":
            payload = build_msdisplay_frame(bytes_a)
            print(f"[TEST 2: REPEATED SAME FRAME (50 Iterations)]")
            print(f"  Image File      : {pattern_a} ({len(bytes_a)} bytes JPEG)")
            print(f"  Payload Size    : {len(payload)} bytes")
            for i in range(50):
                res = send_frame_usbfs(fd, payload)
                if i % 10 == 0:
                    print(f"  Tx Iteration {i+1}/50 -> Result: {res} bytes OK")
                time.sleep(0.1)
            print("\n  OBSERVE LCD PANEL NOW: Record if corruption stays stable, flickers, or shifts.")

        elif mode == "alternate":
            payload_a = build_msdisplay_frame(bytes_a)
            payload_b = build_msdisplay_frame(bytes_b)
            print(f"[TEST 3: ALTERNATE PATTERNS A <-> B (40 Iterations)]")
            print(f"  Pattern A Size  : {len(payload_a)} bytes (Black Background)")
            print(f"  Pattern B Size  : {len(payload_b)} bytes (White Background)")
            for i in range(40):
                current_payload = payload_a if i % 2 == 0 else payload_b
                pat_name = "Pattern A (Black)" if i % 2 == 0 else "Pattern B (White)"
                res = send_frame_usbfs(fd, current_payload)
                if i % 10 == 0:
                    print(f"  Tx Iteration {i+1}/40 ({pat_name}) -> Result: {res} bytes OK")
                time.sleep(0.2)
            print("\n  OBSERVE LCD PANEL NOW: Does corruption move with pattern or stay fixed to physical Y rows?")

        elif mode == "color-bars":
            payload = build_msdisplay_frame(bytes_c)
            print(f"[TEST 4: 5-COLOR HORIZONTAL BANDS (Red, Green, Blue, White, Black)]")
            print(f"  Image File      : {pattern_c}")
            print(f"  JPEG Byte Size  : {len(bytes_c)} bytes")
            print(f"  Total Payload   : {len(payload)} bytes")
            res = send_frame_usbfs(fd, payload)
            print(f"  USB Transfer Result Code: {res} bytes submitted successfully to EP 0x02 Bulk OUT.")
            print("\n  OBSERVE LCD PANEL NOW: Check which horizontal color band contains the corruption.")

    except Exception as e:
        print(f"[ERROR] Diagnostic transfer error: {e}")
    finally:
        try: fcntl.ioctl(fd, USBDEVFS_RELEASEINTERFACE, iface_buf)
        except Exception: pass
        os.close(fd)
        print("=== Diagnostic Execution Completed ===")

def main():
    parser = argparse.ArgumentParser(description="MSDisplay Diagnostic Test Runner")
    parser.add_argument('--mode', choices=['single', 'repeated', 'alternate', 'color-bars'], default='single', help="Diagnostic test mode")

    args = parser.parse_args()
    run_diagnostic(mode=args.mode)

if __name__ == "__main__":
    main()
