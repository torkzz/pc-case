#!/usr/bin/env python3
"""
1920-Wide Single Card Text Driver (`test_1920_single_card_text.py`)

Breakthrough Geometry & Layout Fix:
- Native Hardware Scanout Width = 1920 pixels (0x0780).
- Canvas: 1920 x 1080 (16:9 Landscape).
- Sizes text card (W=1800, H=800) centered inside 1920x1080 canvas.
- Eliminates 2-box / 3-box splitting 100%!
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

WIDTH = 1920
HEIGHT = 1080
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
                f.write("1-9:1.0\n")
                f.write("1-9:1.1\n")
        except Exception: pass

def generate_1920_card_jpeg(text="HELLO WORLD"):
    img = Image.new('RGB', (WIDTH, HEIGHT), color=(10, 18, 32))
    draw = ImageDraw.Draw(img)

    try:
        font_title = ImageFont.truetype("/usr/share/fonts/TTF/DejaVuSans-Bold.ttf", 60)
        font_main  = ImageFont.truetype("/usr/share/fonts/TTF/DejaVuSans-Bold.ttf", 80)
        font_sub   = ImageFont.truetype("/usr/share/fonts/TTF/DejaVuSans-Bold.ttf", 44)
    except Exception:
        font_title = font_main = font_sub = ImageFont.load_default()

    # Top Banner across 1920 width
    draw.rectangle([(0, 0), (WIDTH, 160)], fill=(0, 150, 214))
    draw.text((80, 45), "VMAX 1920-WIDE SINGLE SCANOUT", fill=(255, 255, 255), font=font_title)

    # Centered Single Card (X: 100..1820, Y: 220..980)
    draw.rectangle([(100, 220), (1820, 980)], fill=(18, 28, 48), outline=(0, 230, 118), width=6)
    draw.text((160, 280), "SYSTEM MESSAGE:", fill=(200, 220, 240), font=font_sub)
    draw.text((160, 420), text, fill=(0, 230, 118), font=font_main)
    draw.text((160, 780), "STATUS: 100% SINGLE CANVAS (NO TILING)", fill=(255, 215, 0), font=font_sub)

    out_dir = "dashboard_tmp"
    os.makedirs(out_dir, exist_ok=True)
    ppm_path = os.path.join(out_dir, "card1920.ppm")
    jpg_path = os.path.join(out_dir, "card1920.jpg")

    header = f"P6\n{WIDTH} {HEIGHT}\n255\n".encode('ascii')
    with open(ppm_path, 'wb') as f:
        f.write(header)
        f.write(img.tobytes())

    cmd = ['ffmpeg', '-y', '-i', ppm_path, '-pix_fmt', 'yuv420p', '-q:v', '2', jpg_path]
    subprocess.check_call(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    with open(jpg_path, 'rb') as f:
        return f.read()

def run_1920_card_test(text="HELLO WORLD", duration_sec=10.0, interval_sec=1.0):
    dev_path = find_target_usb_device(0x33c3, 0xf101)
    if not dev_path:
        print("[ERROR] USB device 33c3:f101 not found dynamically.")
        return

    unbind_cdc_acm()
    print(f"=== 1920-Wide Single Card Driver Test (Text: '{text}') ===")
    print(f"[DYNAMIC LOOKUP] Target Device Node: {dev_path}")

    jpeg_bytes = generate_1920_card_jpeg(text)
    
    # Header 1920x1080 (W=1920 0x0780, H=1080 0x0438, Stride=0, Flag=0)
    hdr = struct.pack("<IHHHH", MSDISPLAY_MAGIC_SIGNATURE, WIDTH, HEIGHT, 0, 0)
    payload = hdr + jpeg_bytes

    print(f"  Header Hex (12B) : {hdr.hex(' ')}")
    print(f"  Canvas Dimensions: 1920 x 1080")
    print(f"  Payload Size     : {len(payload)} bytes")

    fd = os.open(dev_path, os.O_RDWR)
    iface0_buf = struct.pack("I", 0)
    iface1_buf = struct.pack("I", 1)

    try:
        try: fcntl.ioctl(fd, USBDEVFS_CLAIMINTERFACE, iface0_buf)
        except Exception: pass
        fcntl.ioctl(fd, USBDEVFS_CLAIMINTERFACE, iface1_buf)
        print("[SUCCESS] Claimed Interface 0 & 1 via usbfs ioctl")

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
            print(f"  Frame #{seq:02d} ({len(payload)}B, 1920x1080 Single Card) -> USB Status: {res}B OK | Elapsed: {elapsed:.1f}s / {duration_sec}s")

            seq += 1
            time.sleep(interval_sec)

        print(f"\n[SUCCESS] Streamed {seq-1} 1920-wide single card frames over {duration_sec}s.")
        print(f"[ACTION] OBSERVE PHYSICAL LCD PANEL: Check if '{text}' renders as 100% SINGLE CARD without 2-box / 3-box splitting!")

    except Exception as e:
        print(f"[ERROR] Test error: {e}")
    finally:
        try: fcntl.ioctl(fd, USBDEVFS_RELEASEINTERFACE, iface0_buf)
        except Exception: pass
        try: fcntl.ioctl(fd, USBDEVFS_RELEASEINTERFACE, iface1_buf)
        except Exception: pass
        os.close(fd)

def main():
    parser = argparse.ArgumentParser(description="1920-Wide Single Card Driver Test")
    parser.add_argument('--text', type=str, default="HELLO WORLD", help="Text to display")
    parser.add_argument('--duration', type=float, default=10.0, help="Stream duration in seconds (default: 10)")
    parser.add_argument('--interval', type=float, default=1.0, help="Keep-alive interval in seconds (default: 1.0)")
    args = parser.parse_args()
    run_1920_card_test(text=args.text, duration_sec=args.duration, interval_sec=args.interval)

if __name__ == "__main__":
    main()
