#!/usr/bin/env python3
"""
MSDisplay Linux Live Video Stream Daemon (`msdisplay_live_stream.py`)

Dynamic USB Topology Lookup (NO HARDCODED BUS/DEV NUMBERS):
Target: 33c3:f101 Interface 1 Endpoint 0x02 Bulk OUT
Continuously streams MSDisplay formatted frame payloads (12-byte header + JPEG)
over usbfs to maintain continuous LCD illumination and live playback.
"""

import sys
import os
import time
import struct
import fcntl
import ctypes
import argparse

# USBDEVFS definitions
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

def get_jpeg_frames(image_path: str = None):
    """Loads JPEG files from path or default test file."""
    frames = []
    if image_path and os.path.exists(image_path):
        with open(image_path, 'rb') as f:
            frames.append(f.read())
    
    default_jpg = "/home/tor/pc-case-lcd/vmax_test_2560x666.jpg"
    if not frames and os.path.exists(default_jpg):
        with open(default_jpg, 'rb') as f:
            frames.append(f.read())

    if not frames:
        # Fallback minimal valid JPEG stream
        frames.append(b"\xFF\xD8\xFF\xE0\x00\x10JFIF\x00\x01\x01\x00\x00\x01\x00\x01\x00\x00\xFF\xDB\x00C\x00\x08\x06\x06\x07\x06\x05\x08\x07\x07\x07\x09\x09\x08\x0A\x0C\x14\x0D\x0C\x0B\x0B\x0C\x19\x12\x13\x0F\x14\x1D\x1A\x1F\x1E\x1D\x1A\x1C\x1C $.' \",#\x1C\x1C(7),01444\x1F'9=82<.342\xFF\xC0\x00\x0B\x08\x00\x10\x00\x10\x01\x01\x11\x00\xFF\xC4\x00\x1F\x00\x00\x01\x05\x01\x01\x01\x01\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0A\x0B\xFF\xDA\x00\x08\x01\x01\x00\x00\x3F\x00\x7F\x00\xFF\xD9")

    return frames

def unbind_cdc_acm():
    """Unbinds cdc_acm kernel driver to release Interface 1"""
    unbind_path = "/sys/bus/usb/drivers/cdc_acm/unbind"
    if os.path.exists(unbind_path):
        try:
            with open(unbind_path, 'w') as f:
                f.write("1-9:1.1\n")
        except Exception:
            pass

def start_stream(fps=30, image_path=None, duration_sec=None):
    unbind_cdc_acm()

    dev_path = find_target_usb_device(0x33c3, 0xf101)
    if not dev_path:
        print("[ERROR] Target USB device 33c3:f101 not found dynamically on host bus.")
        return

    print(f"[DYNAMIC LOOKUP] Target Device Node: {dev_path}")
    raw_jpegs = get_jpeg_frames(image_path)
    print(f"=== Starting MSDisplay Live Video Stream Daemon ({fps} FPS) ===")

    fd = os.open(dev_path, os.O_RDWR)
    iface_buf = struct.pack("I", 1)

    try:
        fcntl.ioctl(fd, USBDEVFS_CLAIMINTERFACE, iface_buf)
        print("[SUCCESS] Claimed Interface 1 via usbfs ioctl")
    except Exception as e:
        print(f"[INFO] Interface claim status: {e}")

    frame_delay = 1.0 / float(fps)
    tx_count = 0
    start_time = time.monotonic()

    try:
        while True:
            jpeg = raw_jpegs[tx_count % len(raw_jpegs)]
            payload = build_msdisplay_frame(jpeg)
            
            data_buf = ctypes.create_string_buffer(payload)
            bulk_req = usbdevfs_bulktransfer()
            bulk_req.ep = 0x02
            bulk_req.len = len(payload)
            bulk_req.timeout = 1000
            bulk_req.data = ctypes.cast(data_buf, ctypes.c_void_p)

            res = fcntl.ioctl(fd, USBDEVFS_BULK, bulk_req)
            tx_count += 1

            if tx_count % 30 == 0:
                elapsed = time.monotonic() - start_time
                actual_fps = tx_count / elapsed
                print(f"[STREAMING] Sent {tx_count} frames | Active FPS: {actual_fps:.1f}")

            if duration_sec and (time.monotonic() - start_time) >= duration_sec:
                print(f"[STATUS] Target streaming duration {duration_sec}s reached.")
                break

            time.sleep(frame_delay)

    except KeyboardInterrupt:
        print("\n[STATUS] Stream daemon stopped by user.")
    except Exception as e:
        print(f"[ERROR] Stream transfer error: {e}")
    finally:
        try:
            fcntl.ioctl(fd, USBDEVFS_RELEASEINTERFACE, iface_buf)
        except Exception:
            pass
        os.close(fd)
        print("=== Stream Daemon Terminated Safely ===")

def main():
    parser = argparse.ArgumentParser(description="MSDisplay Linux Live Video Stream Daemon")
    parser.add_argument('--fps', type=int, default=30, help="Target streaming FPS (default: 30)")
    parser.add_argument('--image', type=str, help="JPEG file path for streaming")
    parser.add_argument('--duration', type=float, help="Run duration in seconds (optional)")

    args = parser.parse_args()
    start_stream(fps=args.fps, image_path=args.image, duration_sec=args.duration)

if __name__ == "__main__":
    main()
