#!/usr/bin/env python3
"""
MSDisplay Controlled Transmission Framing / Fragmentation Experiment (`msdisplay_framing_experiment.py`)

Tests whether image corruption is caused by one-shot transmission vs required USB chunk fragmentation:
- TEST A: Entire frame [12B Header + JPEG] in 1 single USB bulk transfer.
- TEST B: Send Frame in 4096-Byte Fragments.
- TEST C: Send Frame in 8192-Byte Fragments.
- TEST D: Send Frame in 16384-Byte Fragments.

Keeps EXACT SAME JPEG (diagnostic_patterns/4quarter_blocks.jpg) and 12-byte header (0x0008100A, W=2560, H=666).
Repeats frame transmission for --duration seconds (default 10s) to keep panel active.
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

def run_framing_test(test_id="A", duration_sec=10.0):
    unbind_cdc_acm()

    dev_path = find_target_usb_device(0x33c3, 0xf101)
    if not dev_path:
        print("[ERROR] USB device node 33c3:f101 not dynamically accessible.")
        return

    pattern_file = "diagnostic_patterns/4quarter_blocks.jpg"
    if not os.path.exists(pattern_file):
        print(f"[ERROR] Diagnostic image '{pattern_file}' not found.")
        return

    with open(pattern_file, 'rb') as f:
        jpeg_bytes = f.read()

    full_payload = build_msdisplay_frame(jpeg_bytes)
    total_len = len(full_payload)

    # Determine Chunk Size per Test ID
    if test_id == "A":
        chunk_size = total_len
        test_desc = "TEST A: Entire Frame in 1 Single USB Bulk Transfer"
    elif test_id == "B":
        chunk_size = 4096
        test_desc = "TEST B: Send Frame in 4096-Byte Fragments"
    elif test_id == "C":
        chunk_size = 8192
        test_desc = "TEST C: Send Frame in 8192-Byte Fragments"
    elif test_id == "D":
        chunk_size = 16384
        test_desc = "TEST D: Send Frame in 16384-Byte Fragments"
    else:
        print(f"[ERROR] Invalid Test ID: {test_id}")
        return

    # Fragment payload
    chunks = [full_payload[i:i+chunk_size] for i in range(0, total_len, chunk_size)]
    num_transfers = len(chunks)

    print(f"\n==================================================")
    print(f"FRAG EXPERIMENT — {test_desc} (Duration: {duration_sec}s)")
    print(f"  Target Device Node: {dev_path}")
    print(f"  Endpoint          : 0x02 Bulk OUT (Interface 1)")
    print(f"  Header Hex (12B)  : {full_payload[:12].hex(' ')}")
    print(f"  JPEG Size         : {len(jpeg_bytes)} bytes")
    print(f"  Total Frame Size  : {total_len} bytes")
    print(f"  Chunk Size        : {chunk_size} bytes")
    print(f"  Chunks per Frame  : {num_transfers}")
    print(f"==================================================")

    fd = os.open(dev_path, os.O_RDWR)
    iface_buf = struct.pack("I", 1)

    try:
        fcntl.ioctl(fd, USBDEVFS_CLAIMINTERFACE, iface_buf)
        start_time = time.monotonic()
        frame_count = 0

        while (time.monotonic() - start_time) < duration_sec:
            for idx, chunk in enumerate(chunks):
                data_buf = ctypes.create_string_buffer(chunk)
                bulk_req = usbdevfs_bulktransfer()
                bulk_req.ep = 0x02
                bulk_req.len = len(chunk)
                bulk_req.timeout = 1000
                bulk_req.data = ctypes.cast(data_buf, ctypes.c_void_p)
                res = fcntl.ioctl(fd, USBDEVFS_BULK, bulk_req)
            
            frame_count += 1
            if frame_count % 30 == 0 or frame_count == 1:
                elapsed = time.monotonic() - start_time
                print(f"  [STREAMING] Sent {frame_count} frames ({frame_count * num_transfers} chunks) | Elapsed: {elapsed:.1f}s / {duration_sec}s")
            time.sleep(0.033) # ~30 FPS

        print(f"\n  [SUCCESS] Streamed {frame_count} frames ({frame_count * num_transfers} USB transfers) over {duration_sec}s for TEST {test_id}.")
        print(f"  [ACTION] OBSERVE PHYSICAL LCD PANEL NOW.")
    except Exception as e:
        print(f"  [ERROR] Transfer error: {e}")
    finally:
        try: fcntl.ioctl(fd, USBDEVFS_RELEASEINTERFACE, iface_buf)
        except Exception: pass
        os.close(fd)

def main():
    parser = argparse.ArgumentParser(description="MSDisplay Transmission Framing & Fragmentation Experiment")
    parser.add_argument('--test', choices=['A', 'B', 'C', 'D'], default='A', help="Test ID (A=One-shot, B=4096, C=8192, D=16384)")
    parser.add_argument('--duration', type=float, default=10.0, help="Stream duration in seconds (default: 10)")

    args = parser.parse_args()
    run_framing_test(args.test, duration_sec=args.duration)

if __name__ == "__main__":
    main()
