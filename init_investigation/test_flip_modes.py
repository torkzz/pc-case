#!/usr/bin/env python3
"""
Scanout Orientation & Text Glyph Un-Mirroring Test (`test_flip_modes.py`)

Physical Observation Finding:
- User saw "00 then 01 but inverted": Order 0, 1... is correct, but text characters are mirrored/inverted!
- Tests precise FFmpeg video filter modes:
  - --mode hflip      : Horizontal flip only (-vf hflip)
  - --mode vflip      : Vertical flip only (-vf vflip)
  - --mode transpose1 : 90 deg CW (-vf transpose=1)
  - --mode transpose2 : 90 deg CCW (-vf transpose=2)
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

WIDTH = 2560
HEIGHT = 666
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

def generate_mode_jpeg(mode="hflip"):
    out_dir = "dashboard_tmp"
    os.makedirs(out_dir, exist_ok=True)
    ppm_path = os.path.join(out_dir, "flip_mode.ppm")
    jpg_path = os.path.join(out_dir, f"flip_{mode}.jpg")

    img = Image.new('RGB', (WIDTH, HEIGHT), color=(10, 18, 32))
    draw = ImageDraw.Draw(img)

    try:
        font_num   = ImageFont.truetype("/usr/share/fonts/TTF/DejaVuSans-Bold.ttf", 130)
        font_label = ImageFont.truetype("/usr/share/fonts/TTF/DejaVuSans-Bold.ttf", 36)
    except Exception:
        font_num = font_label = ImageFont.load_default()

    # Top Header Banner
    draw.rectangle([(0, 0), (WIDTH, 90)], fill=(0, 150, 214))
    draw.text((60, 25), f"UN-MIRRORING TEST (MODE: {mode.upper()})", fill=(255, 255, 255), font=font_label)

    # 10 Column Colors (256px wide each)
    colors = [
        (230, 57, 70),   # 0: Red
        (42, 157, 143),  # 1: Teal
        (233, 196, 106), # 2: Gold
        (244, 162, 97),  # 3: Peach
        (231, 111, 81),  # 4: Coral
        (106, 76, 147),  # 5: Purple
        (25, 130, 196),  # 6: Blue
        (138, 201, 38),  # 7: Green
        (255, 89, 94),   # 8: Pink
        (108, 117, 125)  # 9: Gray
    ]

    col_w = 256
    for c in range(10):
        x1 = c * col_w
        x2 = (c + 1) * col_w
        color = colors[c]
        draw.rectangle([(x1, 100), (x2 - 4, HEIGHT)], fill=color, outline=(255, 255, 255), width=3)
        draw.text((x1 + 80, 260), f"0{c}", fill=(255, 255, 255), font=font_num)

    header = f"P6\n{WIDTH} {HEIGHT}\n255\n".encode('ascii')
    with open(ppm_path, 'wb') as f:
        f.write(header)
        f.write(img.tobytes())

    vf_map = {
        'hflip': 'hflip',
        'vflip': 'vflip',
        'transpose1': 'transpose=1',
        'transpose2': 'transpose=2'
    }
    vf = vf_map.get(mode, 'hflip')

    cmd = ['ffmpeg', '-y', '-i', ppm_path, '-vf', vf, '-pix_fmt', 'yuv420p', '-q:v', '2', jpg_path]
    subprocess.check_call(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    with open(jpg_path, 'rb') as f:
        return f.read()

def run_flip_mode_test(mode="hflip", duration_sec=10.0, interval_sec=1.0):
    dev_path = find_target_usb_device(0x33c3, 0xf101)
    if not dev_path:
        print("[ERROR] USB device 33c3:f101 not found dynamically.")
        return

    unbind_cdc_acm()
    print(f"=== Scanout Orientation & Text Un-Mirroring Test (Mode: {mode.upper()}) ===")
    print(f"[DYNAMIC LOOKUP] Target Device Node: {dev_path}")

    jpeg_bytes = generate_mode_jpeg(mode)
    
    # Header 2560x666 (W=2560 0x0A00, H=666 0x029A, Stride=0, Flag=0)
    hdr = struct.pack("<IHHHH", MSDISPLAY_MAGIC_SIGNATURE, WIDTH, HEIGHT, 0, 0)
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
            print(f"  Frame #{seq:02d} ({len(payload)}B, Mode: {mode.upper()}) -> USB Status: {res}B OK | Elapsed: {elapsed:.1f}s / {duration_sec}s")

            seq += 1
            time.sleep(interval_sec)

        print(f"\n[SUCCESS] Streamed {seq-1} {mode.upper()} frames over {duration_sec}s.")
        print(f"[ACTION] OBSERVE PHYSICAL LCD PANEL: Check if 00, 01, 02... are readable and NOT mirrored!")

    except Exception as e:
        print(f"[ERROR] Test error: {e}")
    finally:
        try: fcntl.ioctl(fd, USBDEVFS_RELEASEINTERFACE, iface_buf)
        except Exception: pass
        os.close(fd)

def main():
    parser = argparse.ArgumentParser(description="Scanout Orientation & Text Glyph Un-Mirroring Test")
    parser.add_argument('--mode', choices=['hflip', 'vflip', 'transpose1', 'transpose2'], default='hflip', help="Filter mode")
    parser.add_argument('--duration', type=float, default=10.0, help="Stream duration in seconds (default: 10)")
    parser.add_argument('--interval', type=float, default=1.0, help="Keep-alive interval in seconds (default: 1.0)")
    args = parser.parse_args()
    run_flip_mode_test(mode=args.mode, duration_sec=args.duration, interval_sec=args.interval)

if __name__ == "__main__":
    main()
