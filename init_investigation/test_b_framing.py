#!/usr/bin/env python3
"""
MSDisplay Controlled USB Framing Test — TEST B (4096-Byte Fragments, Single Frame)

Requirements:
- Target: Dynamically discovered 33c3:f101 (Interface 1, EP 0x02 Bulk OUT)
- JPEG: diagnostic_patterns/4quarter_blocks.jpg (50,049 bytes)
- Header: 0a 10 08 00 00 0a 9a 02 00 00 00 00 (Magic=0x0008100A, W=2560, H=666, 0x08=0, 0x0A=0)
- Total Payload: 50,061 bytes
- Framing: 4096-byte chunks (13 fragments total)
- Execution: EXACTLY ONE frame (no loop, no repeat).
"""

import sys
import os
import time
import struct
import fcntl
import ctypes

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
CHUNK_SIZE = 4096

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

def run_test_b():
    pattern_file = "diagnostic_patterns/4quarter_blocks.jpg"
    if not os.path.exists(pattern_file):
        print(f"[ERROR] Pattern image file '{pattern_file}' not found.")
        return

    with open(pattern_file, 'rb') as f:
        jpeg_bytes = f.read()

    # Exact 12-byte header: Magic=0x0008100A, Width=2560 (0x0A00), Height=666 (0x029A), Stride=0, Flag=0
    hdr = struct.pack("<IHHHH", MSDISPLAY_MAGIC_SIGNATURE, 2560, 666, 0, 0)
    payload = hdr + jpeg_bytes
    total_len = len(payload)

    # Calculate chunks
    chunks = [payload[i:i+CHUNK_SIZE] for i in range(0, total_len, CHUNK_SIZE)]
    num_fragments = len(chunks)

    print("==================================================")
    print("DRY-RUN CALCULATION — TEST B (4096-BYTE FRAGMENTATION)")
    print(f"  JPEG File        : {pattern_file}")
    print(f"  JPEG Size        : {len(jpeg_bytes)} bytes")
    print(f"  Header Hex (12B) : {hdr.hex(' ')}")
    print(f"  Total Payload    : {total_len} bytes")
    print(f"  Fragment Size    : {CHUNK_SIZE} bytes")
    print(f"  Total Fragments  : {num_fragments}")
    print("  Fragment Breakdown:")
    for idx, c in enumerate(chunks):
        offset = idx * CHUNK_SIZE
        print(f"    Fragment #{idx+1:02d}: Offset 0x{offset:04X} ({offset:5d}B) -> Length: {len(c):4d} bytes")
    print("==================================================\n")

    dev_path = find_target_usb_device(0x33c3, 0xf101)
    if not dev_path:
        print("[ERROR] Target USB device 33c3:f101 not found dynamically.")
        return

    unbind_cdc_acm()
    fd = os.open(dev_path, os.O_RDWR)
    iface_buf = struct.pack("I", 1)

    total_sent = 0
    errors = []

    try:
        fcntl.ioctl(fd, USBDEVFS_CLAIMINTERFACE, iface_buf)
        print(f"[STATUS] Claimed Interface 1 on {dev_path}")
        print(f"[STATUS] Transmitting TEST B (13 chunks of 4096 bytes)...")

        for idx, chunk in enumerate(chunks):
            offset = idx * CHUNK_SIZE
            data_buf = ctypes.create_string_buffer(chunk)
            bulk_req = usbdevfs_bulktransfer()
            bulk_req.ep = 0x02
            bulk_req.len = len(chunk)
            bulk_req.timeout = 1000
            bulk_req.data = ctypes.cast(data_buf, ctypes.c_void_p)

            try:
                res = fcntl.ioctl(fd, USBDEVFS_BULK, bulk_req)
                total_sent += res
                print(f"  Tx #{idx+1:02d}/{num_fragments}: Offset {offset:5d}B, Requested {len(chunk):4d}B -> Returned {res:4d}B [OK]")
            except Exception as e:
                err_msg = f"Fragment #{idx+1} (Offset {offset}): {e}"
                errors.append(err_msg)
                print(f"  Tx #{idx+1:02d}/{num_fragments}: Offset {offset:5d}B -> ERROR: {e}")
                break

    finally:
        try: fcntl.ioctl(fd, USBDEVFS_RELEASEINTERFACE, iface_buf)
        except Exception: pass
        os.close(fd)

    print("\n--------------------------------------------------")
    print("FRAMING TEST:")
    print("TEST B")
    print(f"FRAGMENT SIZE: {CHUNK_SIZE} bytes")
    print(f"TOTAL PAYLOAD: {total_len} bytes")
    print(f"NUMBER OF TRANSFERS: {num_fragments}")
    print(f"TOTAL BYTES SENT: {total_sent} bytes")
    print(f"USB RESULT: {'SUCCESS' if total_sent == total_len else 'PARTIAL/FAILED'}")
    print(f"ERRORS: {errors if errors else 'None'}")
    print("\nPHYSICAL OBSERVATION:")
    print("PENDING")
    print("--------------------------------------------------")

if __name__ == "__main__":
    run_test_b()
