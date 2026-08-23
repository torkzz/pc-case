#!/usr/bin/env python3
"""
Full-Vertical Height Coverage Test (`test_fullscreen_coverage.py`)

Distributes 4 bright colored cards across the full 640x1920 vertical screen height:
- Top Region     (Y:    0 -  480): Cyan Card (0, 180, 216) + Text "1. TOP REGION"
- Upper Mid      (Y:  480 -  960): Green Card (0, 230, 118) + Text "2. UPPER MID"
- Lower Mid      (Y:  960 - 1440): Yellow Card (255, 214, 10) + Text "3. LOWER MID"
- Bottom Region  (Y: 1440 - 1920): Magenta Card (247, 37, 133) + Text "4. BOTTOM REGION"
"""

import sys
import os
import time
import struct
import fcntl
import ctypes
import subprocess
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

def generate_fullscreen_coverage_jpeg(text="HELLO WORLD"):
    img = Image.new('RGB', (WIDTH, HEIGHT), color=(10, 18, 32))
    draw = ImageDraw.Draw(img)

    try:
        font_large = ImageFont.truetype("/usr/share/fonts/TTF/DejaVuSans-Bold.ttf", 44)
        font_sub   = ImageFont.truetype("/usr/share/fonts/TTF/DejaVuSans-Bold.ttf", 32)
    except Exception:
        font_large = font_sub = ImageFont.load_default()

    # Region 1: Cyan Top Card (Y: 20 - 440)
    draw.rectangle([(20, 20), (620, 440)], fill=(0, 180, 216), outline=(255, 255, 255), width=4)
    draw.text((50, 60), "1. TOP REGION", fill=(0, 0, 0), font=font_large)
    draw.text((50, 150), f"TEXT: {text}", fill=(255, 255, 255), font=font_sub)
    draw.text((50, 250), "Y: 0 - 480 px", fill=(0, 0, 0), font=font_sub)

    # Region 2: Green Upper-Mid Card (Y: 500 - 920)
    draw.rectangle([(20, 500), (620, 920)], fill=(0, 230, 118), outline=(255, 255, 255), width=4)
    draw.text((50, 540), "2. UPPER MID", fill=(0, 0, 0), font=font_large)
    draw.text((50, 630), "GREEN DISPLAY CARD", fill=(0, 0, 0), font=font_sub)
    draw.text((50, 730), "Y: 480 - 960 px", fill=(0, 0, 0), font=font_sub)

    # Region 3: Yellow Lower-Mid Card (Y: 980 - 1400)
    draw.rectangle([(20, 980), (620, 1400)], fill=(255, 214, 10), outline=(255, 255, 255), width=4)
    draw.text((50, 1020), "3. LOWER MID", fill=(0, 0, 0), font=font_large)
    draw.text((50, 1110), "YELLOW DISPLAY CARD", fill=(0, 0, 0), font=font_sub)
    draw.text((50, 1210), "Y: 960 - 1440 px", fill=(0, 0, 0), font=font_sub)

    # Region 4: Magenta Bottom Card (Y: 1460 - 1880)
    draw.rectangle([(20, 1460), (620, 1880)], fill=(247, 37, 133), outline=(255, 255, 255), width=4)
    draw.text((50, 1500), "4. BOTTOM REGION", fill=(255, 255, 255), font=font_large)
    draw.text((50, 1590), "MAGENTA DISPLAY CARD", fill=(255, 255, 255), font=font_sub)
    draw.text((50, 1690), "Y: 1440 - 1920 px", fill=(255, 255, 255), font=font_sub)

    out_dir = "dashboard_tmp"
    os.makedirs(out_dir, exist_ok=True)
    ppm_path = os.path.join(out_dir, "fullscreen_coverage.ppm")
    jpg_path = os.path.join(out_dir, "fullscreen_coverage.jpg")

    header = f"P6\n{WIDTH} {HEIGHT}\n255\n".encode('ascii')
    with open(ppm_path, 'wb') as f:
        f.write(header)
        f.write(img.tobytes())

    cmd = ['ffmpeg', '-y', '-i', ppm_path, '-vf', 'scale=640:1920', '-q:v', '2', jpg_path]
    subprocess.check_call(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    with open(jpg_path, 'rb') as f:
        return f.read()

def run_fullscreen_test(text="HELLO WORLD", duration_sec=10.0, interval_sec=1.0):
    dev_path = find_target_usb_device(0x33c3, 0xf101)
    if not dev_path:
        print("[ERROR] USB device 33c3:f101 not found dynamically.")
        return

    unbind_cdc_acm()
    print(f"=== Full-Vertical Height Coverage Test (Text: '{text}') ===")
    print(f"[DYNAMIC LOOKUP] Target Device Node: {dev_path}")

    jpeg_bytes = generate_fullscreen_coverage_jpeg(text)
    hdr = struct.pack("<IHHHH", MSDISPLAY_MAGIC_SIGNATURE, WIDTH, HEIGHT, STRIDE_LOCK, FLAG_FIXED)
    payload = hdr + jpeg_bytes

    print(f"  Header Hex (12B) : {hdr.hex(' ')}")
    print(f"  Canvas Dimensions: 640 x 1920 (Full Vertical Coverage)")
    print(f"  Payload Size     : {len(payload)} bytes")

    fd = os.open(dev_path, os.O_RDWR)
    iface_buf = struct.pack("I", 1)

    try:
        fcntl.ioctl(fd, USBDEVFS_CLAIMINTERFACE, iface_buf)
        print("[SUCCESS] Claimed Interface 1 via usbfs ioctl")

        start_time = time.monotonic()
        seq = 1

        while (time.monotonic() - start_time) < duration_sec:
            data_buf = ctypes.create_string_buffer(payload)
            bulk_req = usbdevfs_bulktransfer()
            bulk_req.ep = 0x02
            bulk_req.len = len(payload)
            bulk_req.timeout = 2000
            bulk_req.data = ctypes.cast(data_buf, ctypes.c_void_p)

            res = fcntl.ioctl(fd, USBDEVFS_BULK, bulk_req)
            elapsed = time.monotonic() - start_time
            print(f"  Frame #{seq:02d} ({len(payload)}B, Full Vertical Height) -> USB Status: {res}B OK | Elapsed: {elapsed:.1f}s / {duration_sec}s")

            seq += 1
            time.sleep(interval_sec)

        print(f"\n[SUCCESS] Streamed {seq-1} full vertical height frames over {duration_sec}s.")
        print(f"[ACTION] OBSERVE PHYSICAL LCD PANEL: Check if all 4 cards (Cyan top, Green upper-mid, Yellow lower-mid, Magenta bottom) fill entire screen.")

    except Exception as e:
        print(f"[ERROR] Test error: {e}")
    finally:
        try: fcntl.ioctl(fd, USBDEVFS_RELEASEINTERFACE, iface_buf)
        except Exception: pass
        os.close(fd)

def main():
    parser = argparse.ArgumentParser(description="Full-Vertical Height Coverage Test")
    parser.add_argument('--text', type=str, default="HELLO WORLD", help="Text to display")
    parser.add_argument('--duration', type=float, default=10.0, help="Stream duration in seconds (default: 10)")
    parser.add_argument('--interval', type=float, default=1.0, help="Keep-alive interval in seconds (default: 1.0)")
    args = parser.parse_args()
    run_fullscreen_test(text=args.text, duration_sec=args.duration, interval_sec=args.interval)

if __name__ == "__main__":
    main()
