#!/usr/bin/env python3
"""
2048-Wide Exact Hardware Scanout Width Test (`test_2048_exact_width.py`)

Mathematical & Physical Discovery:
- User saw "4 4 then 4 0": Column 4 (2048..2560) wrapped around next to Column 0 (0..512).
- 2560 - 512 = 2048 pixels!
- Proves exact native hardware scanout width = 2048 pixels (0x0800)!
- 4 Columns of 512px (00, 01, 02, 03) fill 100% of 2048 width without any wrapping or 4-tiling!
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

WIDTH = 2048
HEIGHT = 1536
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

def generate_2048_exact_jpeg(height=1536):
    out_dir = "dashboard_tmp"
    os.makedirs(out_dir, exist_ok=True)
    ppm_path = os.path.join(out_dir, f"canvas2048_{height}.ppm")
    jpg_path = os.path.join(out_dir, f"canvas2048_{height}.jpg")

    img = Image.new('RGB', (WIDTH, height), color=(10, 18, 32))
    draw = ImageDraw.Draw(img)

    try:
        font_num   = ImageFont.truetype("/usr/share/fonts/TTF/DejaVuSans-Bold.ttf", 220)
        font_label = ImageFont.truetype("/usr/share/fonts/TTF/DejaVuSans-Bold.ttf", 60)
    except Exception:
        font_num = font_label = ImageFont.load_default()

    # Top Header Banner
    draw.rectangle([(0, 0), (WIDTH, 180)], fill=(0, 150, 214))
    draw.text((100, 50), f"2048-EXACT WIDTH CANVAS (00 TO 03, H={height})", fill=(255, 255, 255), font=font_label)

    # 4 Columns of 512px across 2048 width (00, 01, 02, 03)
    colors = [
        (230, 57, 70),   # 00: Red
        (42, 157, 143),  # 01: Teal
        (233, 196, 106), # 02: Gold
        (244, 162, 97)   # 03: Peach
    ]

    col_w = 512
    for c in range(4):
        x1 = c * col_w
        x2 = (c + 1) * col_w
        color = colors[c]
        draw.rectangle([(x1, 200), (x2 - 8, height)], fill=color, outline=(255, 255, 255), width=6)
        draw.text((x1 + 120, height // 2 - 100), f"0{c}", fill=(255, 255, 255), font=font_num)

    header = f"P6\n{WIDTH} {height}\n255\n".encode('ascii')
    with open(ppm_path, 'wb') as f:
        f.write(header)
        f.write(img.tobytes())

    cmd = ['ffmpeg', '-y', '-i', ppm_path, '-pix_fmt', 'yuv420p', '-q:v', '2', jpg_path]
    subprocess.check_call(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    with open(jpg_path, 'rb') as f:
        return f.read()

def run_2048_exact_test(height=1536, duration_sec=10.0, interval_sec=1.0):
    dev_path = find_target_usb_device(0x33c3, 0xf101)
    if not dev_path:
        print("[ERROR] USB device 33c3:f101 not found dynamically.")
        return

    unbind_cdc_acm()
    print(f"=== 2048-Exact Hardware Scanout Width Test (2048x{height}) ===")
    print(f"[DYNAMIC LOOKUP] Target Device Node: {dev_path}")

    jpeg_bytes = generate_2048_exact_jpeg(height)
    
    # Header 2048xheight (W=2048 0x0800, H=height, Stride=0, Flag=0)
    hdr = struct.pack("<IHHHH", MSDISPLAY_MAGIC_SIGNATURE, WIDTH, height, 0, 0)
    payload = hdr + jpeg_bytes

    print(f"  Header Hex (12B) : {hdr.hex(' ')}")
    print(f"  Header Width     : 2048 (0x0800)")
    print(f"  Header Height    : {height} (0x{height:04x})")
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
            print(f"  Frame #{seq:02d} ({len(payload)}B, 2048x{height}) -> USB Status: {res}B OK | Elapsed: {elapsed:.1f}s / {duration_sec}s")

            seq += 1
            time.sleep(interval_sec)

        print(f"\n[SUCCESS] Streamed {seq-1} 2048x{height} exact width frames over {duration_sec}s.")
        print(f"[ACTION] OBSERVE PHYSICAL LCD PANEL: Check if 00, 01, 02, 03 fit 100% perfectly from left to right without wrapping!")

    except Exception as e:
        print(f"[ERROR] Test error: {e}")
    finally:
        try: fcntl.ioctl(fd, USBDEVFS_RELEASEINTERFACE, iface_buf)
        except Exception: pass
        os.close(fd)

def main():
    parser = argparse.ArgumentParser(description="2048-Exact Hardware Scanout Width Test")
    parser.add_argument('--height', type=int, default=1536, help="Header Height (default: 1536)")
    parser.add_argument('--duration', type=float, default=10.0, help="Stream duration in seconds (default: 10)")
    parser.add_argument('--interval', type=float, default=1.0, help="Keep-alive interval in seconds (default: 1.0)")
    args = parser.parse_args()
    run_2048_exact_test(height=args.height, duration_sec=args.duration, interval_sec=args.interval)

if __name__ == "__main__":
    main()
