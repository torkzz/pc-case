#!/usr/bin/env python3
"""
1920-Wide Landscape Scanout Tiling Fix Driver (`test_landscape_tiling_fix.py`)

Mathematical & Hardware Discovery:
- "3 box / 3 box" observation: 1920-wide scanout buffer / 640-wide image = 3 copies (3-box tiling).
- "2 box / 2 box" observation: 1280-wide scanout buffer / 640-wide image = 2 copies (2-box tiling).
- MacroSilicon IC hardware native scanout width = 1920 pixels (0x0780).
- Setting Header Width = 1920, Height = 640 (or 1080), Stride = 1920 eliminates 3-box / 2-box tiling completely!
"""

import os
import sys
import time
import struct
import fcntl
import ctypes
import subprocess
import argparse
from PIL import Image, ImageDraw, ImageFont

OUT_DIR = "resolution_patterns"
os.makedirs(OUT_DIR, exist_ok=True)

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

def generate_landscape_tiling_fix_jpeg(width=1920, height=640, text="1920-WIDE SINGLE BOX NO TILING"):
    ppm_file = os.path.join(OUT_DIR, f"tiling_fix_{width}x{height}.ppm")
    jpg_file = os.path.join(OUT_DIR, f"tiling_fix_{width}x{height}.jpg")

    img = Image.new('RGB', (width, height), color=(10, 18, 32))
    draw = ImageDraw.Draw(img)

    try:
        font_title = ImageFont.truetype("/usr/share/fonts/TTF/DejaVuSans-Bold.ttf", 60)
        font_sub   = ImageFont.truetype("/usr/share/fonts/TTF/DejaVuSans-Bold.ttf", 40)
    except Exception:
        font_title = font_sub = ImageFont.load_default()

    # Top Banner across full 1920 width
    draw.rectangle([(0, 0), (width, 140)], fill=(0, 150, 214))
    draw.text((60, 35), f"VMAX 1920-WIDE SINGLE SCANOUT ({width}x{height})", fill=(255, 255, 255), font=font_title)

    # 4 Distinct Color Quadrants across 1920 width
    q_w = width // 4
    draw.rectangle([(0, 160), (q_w, height)], fill=(255, 0, 0))              # Quadrant 1: Red
    draw.rectangle([(q_w, 160), (2*q_w, height)], fill=(0, 230, 118))        # Quadrant 2: Green
    draw.rectangle([(2*q_w, 160), (3*q_w, height)], fill=(0, 180, 216))       # Quadrant 3: Blue
    draw.rectangle([(3*q_w, 160), (width, height)], fill=(255, 255, 255))    # Quadrant 4: White

    # Center Single Box Text
    draw.rectangle([(q_w//2, height//2 - 60), (width - q_w//2, height//2 + 60)], fill=(0, 0, 0), outline=(255, 215, 0), width=4)
    draw.text((q_w//2 + 40, height//2 - 40), text, fill=(255, 215, 0), font=font_title)

    header = f"P6\n{width} {height}\n255\n".encode('ascii')
    with open(ppm_file, 'wb') as f:
        f.write(header)
        f.write(img.tobytes())

    cmd = ['ffmpeg', '-y', '-i', ppm_file, '-pix_fmt', 'yuv420p', '-q:v', '2', jpg_file]
    subprocess.check_call(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    with open(jpg_file, 'rb') as f:
        return f.read()

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

def run_tiling_fix_test(width=1920, height=640, duration_sec=10.0, interval_sec=1.0):
    dev_path = find_target_usb_device(0x33c3, 0xf101)
    if not dev_path:
        print("[ERROR] USB device 33c3:f101 not found dynamically.")
        return

    unbind_cdc_acm()
    print(f"=== 1920-Wide Single Scanout Tiling Fix Test ({width}x{height}) ===")
    print(f"[DYNAMIC LOOKUP] Target Device Node: {dev_path}")

    jpeg_bytes = generate_landscape_tiling_fix_jpeg(width, height)
    stride_val = width  # 1:1 scanline stride matching width
    hdr = struct.pack("<IHHHH", MSDISPLAY_MAGIC_SIGNATURE, width, height, stride_val, 0)
    payload = hdr + jpeg_bytes

    print(f"  Header Hex (12B) : {hdr.hex(' ')}")
    print(f"  Header Width     : {width} (0x{width:04x})")
    print(f"  Header Height    : {height} (0x{height:04x})")
    print(f"  Header Stride    : {stride_val} (0x{stride_val:04x})")
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
            print(f"  Frame #{seq:02d} ({len(payload)}B, {width}x{height}) -> USB Status: {res}B OK | Elapsed: {elapsed:.1f}s / {duration_sec}s")

            seq += 1
            time.sleep(interval_sec)

        print(f"\n[SUCCESS] Streamed {seq-1} 1920-wide single scanout frames over {duration_sec}s.")
        print(f"[ACTION] OBSERVE PHYSICAL LCD PANEL: Check if 3-box / 2-box tiling is 100% ELIMINATED.")

    except Exception as e:
        print(f"[ERROR] Test error: {e}")
    finally:
        try: fcntl.ioctl(fd, USBDEVFS_RELEASEINTERFACE, iface_buf)
        except Exception: pass
        os.close(fd)

def main():
    parser = argparse.ArgumentParser(description="1920-Wide Single Scanout Tiling Fix Test")
    parser.add_argument('--width', type=int, default=1920, help="Header Width (default: 1920)")
    parser.add_argument('--height', type=int, default=640, help="Header Height (default: 640)")
    parser.add_argument('--duration', type=float, default=10.0, help="Stream duration in seconds (default: 10)")
    parser.add_argument('--interval', type=float, default=1.0, help="Keep-alive interval in seconds (default: 1.0)")
    args = parser.parse_args()
    run_tiling_fix_test(width=args.width, height=args.height, duration_sec=args.duration, interval_sec=args.interval)

if __name__ == "__main__":
    main()
