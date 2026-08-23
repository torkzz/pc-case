#!/usr/bin/env python3
"""
Direct usbfs Bulk OUT Frame Submission Test (`usbfs_direct_test.py`)
Claims interface 1 and submits MSDisplay binary frame payload to EP 0x02 Bulk OUT.
"""

import sys
import os
import fcntl
import struct
import ctypes

FRAME_PATH = "hello_world_frame.bin"

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

def send_bulk_usbfs():
    if not os.path.exists(FRAME_PATH):
        print(f"[ERROR] Frame payload '{FRAME_PATH}' not found. Run msdisplay_linux_driver.py first.")
        return

    with open(FRAME_PATH, 'rb') as f:
        frame_payload = f.read()

    print(f"Loaded MSDisplay frame payload: {len(frame_payload)} bytes")
    print(f"Header Signature: {frame_payload[:12].hex(' ')}")

    dev_path = "/dev/bus/usb/001/003"
    if not os.path.exists(dev_path):
        print(f"[ERROR] Node '{dev_path}' not found.")
        return

    try:
        fd = os.open(dev_path, os.O_RDWR)
        print(f"[SUCCESS] Opened {dev_path} (fd={fd})")

        # Claim Interface 1
        iface_buf = struct.pack("I", 1)
        try:
            fcntl.ioctl(fd, USBDEVFS_CLAIMINTERFACE, iface_buf)
            print("[SUCCESS] Claimed Interface 1 via usbfs ioctl")
        except Exception as ie:
            print(f"[INFO] Claim interface 1 status: {ie}")

        # Send Bulk OUT payload on EP 0x02
        data_buf = ctypes.create_string_buffer(frame_payload)
        bulk_req = usbdevfs_bulktransfer()
        bulk_req.ep = 0x02
        bulk_req.len = len(frame_payload)
        bulk_req.timeout = 3000
        bulk_req.data = ctypes.cast(data_buf, ctypes.c_void_p)

        print("[STATUS] Submitting MSDisplay frame to EP 0x02 Bulk OUT (3000ms timeout)...")
        res = fcntl.ioctl(fd, USBDEVFS_BULK, bulk_req)
        print(f"[SUCCESS] USBDEVFS_BULK result: {res} bytes submitted successfully to EP 0x02 Bulk OUT!")

        # Release Interface 1
        fcntl.ioctl(fd, USBDEVFS_RELEASEINTERFACE, iface_buf)
        os.close(fd)

    except Exception as e:
        print(f"[ERROR] usbfs ioctl execution status: {e}")

if __name__ == "__main__":
    send_bulk_usbfs()
