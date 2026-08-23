#!/usr/bin/env python3
"""
MSDisplay Frame Ownership & Control Verification Test (`test_frame_ownership.py`)

Proportional Font Typography (Fixed Oversized Text):
- Stride Lock (Offset 0x08 = 1920), Flag Fixed (Offset 0x0A = 0)
- Native resolution: 640 x 1920 (Portrait)
- Proportional clean typography
"""

import sys
import os
import time
import struct
import fcntl
import ctypes
import io
import argparse
from PIL import Image, ImageDraw, ImageFont

WIDTH = 640
HEIGHT = 1920
STRIDE_LOCK = 1920
FLAG_FIXED = 0
MSDISPLAY_MAGIC_SIGNATURE = 0x0008100A

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

def generate_ownership_frame(frame_id, timestamp_str):
    img = Image.new('RGB', (WIDTH, HEIGHT), color=(10, 18, 32))
    draw = ImageDraw.Draw(img)

    try:
        font_title = ImageFont.truetype("/usr/share/fonts/TTF/DejaVuSans-Bold.ttf", 38)
        font_val   = ImageFont.truetype("/usr/share/fonts/TTF/DejaVuSans-Bold.ttf", 46)
        font_label = ImageFont.truetype("/usr/share/fonts/TTF/DejaVuSans-Bold.ttf", 26)
        font_sub   = ImageFont.truetype("/usr/share/fonts/TTF/DejaVuSans-Bold.ttf", 22)
    except Exception:
        font_title = font_val = font_label = font_sub = ImageFont.load_default()

    # Top Header Banner
    draw.rectangle([(0, 0), (WIDTH, 110)], fill=(0, 150, 214))
    draw.text((40, 35), "FRAME OWNERSHIP TEST", fill=(255, 255, 255), font=font_title)

    # Box 1: CONTROL ID (Y: 150 - 500)
    draw.rectangle([(30, 150), (610, 500)], fill=(18, 28, 48), outline=(0, 180, 216), width=3)
    draw.text((60, 180), "CONTROL FRAME ID", fill=(200, 220, 240), font=font_label)
    draw.text((60, 240), f"#{frame_id:04d}", fill=(255, 214, 10), font=font_val)
    draw.text((60, 340), "STATUS: LIVE & STRIDE LOCKED", fill=(0, 230, 118), font=font_sub)

    # Box 2: TIME STAMP (Y: 530 - 880)
    draw.rectangle([(30, 530), (610, 880)], fill=(18, 28, 48), outline=(0, 180, 216), width=3)
    draw.text((60, 560), "CURRENT TIMESTAMP", fill=(200, 220, 240), font=font_label)
    draw.text((60, 620), timestamp_str, fill=(0, 212, 255), font=font_val)
    draw.text((60, 720), "REFRESH: 1.0 SECONDS", fill=(180, 200, 220), font=font_sub)

    # Box 3: HARDWARE TRANSPORT (Y: 910 - 1260)
    draw.rectangle([(30, 910), (610, 1260)], fill=(18, 28, 48), outline=(0, 180, 216), width=3)
    draw.text((60, 940), "USB HARDWARE TRANSPORT", fill=(200, 220, 240), font=font_label)
    draw.text((60, 1000), "33c3:f101 (Interface 1)", fill=(255, 255, 255), font=font_val)
    draw.text((60, 1100), "ENDPOINT: 0x02 BULK OUT", fill=(179, 136, 255), font=font_sub)

    # Box 4: NATIVE GEOMETRY (Y: 1290 - 1850)
    draw.rectangle([(30, 1290), (610, 1850)], fill=(18, 28, 48), outline=(0, 180, 216), width=3)
    draw.text((60, 1320), "PANEL SCANOUT GEOMETRY", fill=(200, 220, 240), font=font_label)
    draw.text((60, 1380), "640 x 1920 (Portrait)", fill=(255, 215, 0), font=font_val)
    draw.text((60, 1480), "HEADER MAGIC: 0x0008100A", fill=(180, 200, 220), font=font_sub)
    draw.text((60, 1540), f"STRIDE: {STRIDE_LOCK} | FLAG: {FLAG_FIXED}", fill=(180, 200, 220), font=font_sub)

    buf = io.BytesIO()
    img.save(buf, format='JPEG', quality=95)
    return buf.getvalue()

def run_ownership_test(duration_sec=15.0, interval_sec=1.0):
    dev_path = find_target_usb_device(0x33c3, 0xf101)
    if not dev_path:
        print("[ERROR] Target USB device 33c3:f101 not found dynamically.")
        return

    unbind_cdc_acm()
    print("=== MSDisplay Proportional Font Ownership Test ===")
    print(f"[DYNAMIC LOOKUP] Target Device Node: {dev_path}")

    fd = os.open(dev_path, os.O_RDWR)
    iface_buf = struct.pack("I", 1)

    try:
        fcntl.ioctl(fd, USBDEVFS_CLAIMINTERFACE, iface_buf)
        print("[SUCCESS] Claimed Interface 1 via usbfs ioctl")

        start_time = time.monotonic()
        frame_id = 1

        while (time.monotonic() - start_time) < duration_sec:
            ts = time.strftime("%H:%M:%S")
            jpeg_bytes = generate_ownership_frame(frame_id, ts)
            
            # Header 640x1920 (W=640, H=1920, Stride=1920, Flag=0)
            hdr = struct.pack("<IHHHH", MSDISPLAY_MAGIC_SIGNATURE, WIDTH, HEIGHT, STRIDE_LOCK, FLAG_FIXED)
            payload = hdr + jpeg_bytes

            data_buf = ctypes.create_string_buffer(payload)
            bulk_req = usbdevfs_bulktransfer()
            bulk_req.ep = 0x02
            bulk_req.len = len(payload)
            bulk_req.timeout = 1000
            bulk_req.data = ctypes.cast(data_buf, ctypes.c_void_p)

            res = fcntl.ioctl(fd, USBDEVFS_BULK, bulk_req)
            elapsed = time.monotonic() - start_time
            print(f"[{ts}] Frame #{frame_id:04d} (Size: {len(payload)}B) -> USB Status: {res}B OK | Elapsed: {elapsed:.1f}s / {duration_sec}s")

            frame_id += 1
            time.sleep(interval_sec)

        print(f"\n[SUCCESS] Streamed {frame_id-1} proportional font frames over {duration_sec}s.")
        print("[ACTION] OBSERVE PHYSICAL LCD PANEL: Confirm clean, well-proportioned layout.")

    except Exception as e:
        print(f"[ERROR] Ownership test error: {e}")
    finally:
        try: fcntl.ioctl(fd, USBDEVFS_RELEASEINTERFACE, iface_buf)
        except Exception: pass
        os.close(fd)

def main():
    parser = argparse.ArgumentParser(description="MSDisplay Frame Ownership Verification Test")
    parser.add_argument('--duration', type=float, default=15.0, help="Stream duration in seconds (default: 15)")
    parser.add_argument('--interval', type=float, default=1.0, help="Frame interval in seconds (default: 1.0)")
    args = parser.parse_args()
    run_ownership_test(duration_sec=args.duration, interval_sec=args.interval)

if __name__ == "__main__":
    main()
