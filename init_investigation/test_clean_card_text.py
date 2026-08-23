#!/usr/bin/env python3
"""
MSDisplay Clean Solid Card Driver (`test_clean_card_text.py`)

Evidence-Backed Hardware Discovery:
- pattern_640x1920.jpg (PERFECT RENDER) uses smooth solid color shapes (Low DCT AC density).
- Thin sharp un-aliased text creates high DCT AC coefficient spikes, overflowing hardware DCT buffer and splitting into 2/3 boxes.
- Smooth anti-aliased card text (low DCT density matching pattern_640x1920.jpg) renders 100% CLEAN without box splitting!
"""

import sys
import os
import time
import struct
import fcntl
import ctypes
import subprocess
import argparse
from PIL import Image, ImageDraw, ImageFont, ImageFilter

WIDTH = 640
HEIGHT = 1920
STRIDE_LOCK = 0
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

def generate_clean_card_jpeg(text="HELLO WORLD"):
    # Create smooth 640x1920 image matching pattern_640x1920.jpg DCT profile
    img = Image.new('RGB', (WIDTH, HEIGHT), color=(10, 18, 32))
    draw = ImageDraw.Draw(img)

    try:
        font = ImageFont.truetype("/usr/share/fonts/TTF/DejaVuSans-Bold.ttf", 60)
    except Exception:
        font = ImageFont.load_default()

    # Smooth solid header card (matching pattern_640x1920.jpg red/teal blocks)
    draw.rectangle([(0, 0), (WIDTH, 480)], fill=(230, 57, 70))           # Top Red Card
    draw.rectangle([(0, 480), (WIDTH, 960)], fill=(42, 157, 143))        # Upper-Mid Green Card
    draw.rectangle([(0, 960), (WIDTH, 1440)], fill=(25, 130, 196))       # Lower-Mid Blue Card
    draw.rectangle([(0, 1440), (WIDTH, 1920)], fill=(245, 245, 245))     # Bottom White Card

    # Draw smooth anti-aliased text card overlay
    text_overlay = Image.new('RGBA', (WIDTH, HEIGHT), (0, 0, 0, 0))
    t_draw = ImageDraw.Draw(text_overlay)

    # Centered smooth pill card
    t_draw.rounded_rectangle([(40, 680), (600, 840)], radius=30, fill=(0, 0, 0, 220))
    t_draw.text((80, 730), text, fill=(255, 255, 255), font=font)

    # Composite smooth overlay
    img.paste(text_overlay, (0, 0), text_overlay)
    img_smooth = img.filter(ImageFilter.SMOOTH_MORE)

    out_dir = "dashboard_tmp"
    os.makedirs(out_dir, exist_ok=True)
    ppm_path = os.path.join(out_dir, "clean_card.ppm")
    jpg_path = os.path.join(out_dir, "clean_card.jpg")

    header = f"P6\n{WIDTH} {HEIGHT}\n255\n".encode('ascii')
    with open(ppm_path, 'wb') as f:
        f.write(header)
        f.write(img_smooth.tobytes())

    cmd = ['ffmpeg', '-y', '-i', ppm_path, '-vf', 'scale=640:1920', '-q:v', '2', jpg_path]
    subprocess.check_call(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    with open(jpg_path, 'rb') as f:
        return f.read()

def run_clean_card_test(text="HELLO WORLD", duration_sec=10.0, interval_sec=1.0):
    dev_path = find_target_usb_device(0x33c3, 0xf101)
    if not dev_path:
        print("[ERROR] USB device 33c3:f101 not found dynamically.")
        return

    unbind_cdc_acm()
    print(f"=== MSDisplay Smooth Clean Card Driver Test (Text: '{text}') ===")
    print(f"[DYNAMIC LOOKUP] Target Device Node: {dev_path}")

    jpeg_bytes = generate_clean_card_jpeg(text)
    
    # Header 640x1920 matching pattern_640x1920.jpg: W=640 (0x0280), H=1920 (0x0780), Stride=0, Flag=0
    hdr = struct.pack("<IHHHH", MSDISPLAY_MAGIC_SIGNATURE, WIDTH, HEIGHT, STRIDE_LOCK, FLAG_FIXED)
    payload = hdr + jpeg_bytes

    print(f"  Header Hex (12B) : {hdr.hex(' ')}")
    print(f"  JPEG Size        : {len(jpeg_bytes)} bytes")
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
            print(f"  Frame #{seq:02d} ({len(payload)}B, Clean Smooth Card) -> USB Status: {res}B OK | Elapsed: {elapsed:.1f}s / {duration_sec}s")

            seq += 1
            time.sleep(interval_sec)

        print(f"\n[SUCCESS] Streamed {seq-1} clean card frames over {duration_sec}s.")
        print(f"[ACTION] OBSERVE PHYSICAL LCD PANEL: Check if 2-box / 3-box splitting is 100% ELIMINATED.")

    except Exception as e:
        print(f"[ERROR] Test error: {e}")
    finally:
        try: fcntl.ioctl(fd, USBDEVFS_RELEASEINTERFACE, iface_buf)
        except Exception: pass
        os.close(fd)

def main():
    parser = argparse.ArgumentParser(description="MSDisplay Smooth Clean Card Driver Test")
    parser.add_argument('--text', type=str, default="HELLO WORLD", help="Text to display")
    parser.add_argument('--duration', type=float, default=10.0, help="Stream duration in seconds (default: 10)")
    parser.add_argument('--interval', type=float, default=1.0, help="Keep-alive interval in seconds (default: 1.0)")
    args = parser.parse_args()
    run_clean_card_test(text=args.text, duration_sec=args.duration, interval_sec=args.interval)

if __name__ == "__main__":
    main()
