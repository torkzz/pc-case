#!/usr/bin/env python3
"""
MSDisplay Native Stride Zero Single-Box Driver (`test_zero_stride_box.py`)

Evidence-Backed Assembly Discovery:
- MSDISPLAYSDKWRRAPER.dll line 18001893a: `movw %si, 0x8(%rbx)` -> Offset 0x08 is Stride argument (%si).
- When Offset 0x08 = 0, native driver defaults Stride to Width (Width * 4 for 32-bit RGBA).
- Passing Stride = 0 eliminates 2-way / 3-way horizontal window duplication!
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

def generate_zero_stride_jpeg(text="HELLO WORLD"):
    img = Image.new('RGB', (WIDTH, HEIGHT), color=(10, 18, 32))
    draw = ImageDraw.Draw(img)

    try:
        font_title = ImageFont.truetype("/usr/share/fonts/TTF/DejaVuSans-Bold.ttf", 38)
        font_main  = ImageFont.truetype("/usr/share/fonts/TTF/DejaVuSans-Bold.ttf", 46)
        font_sub   = ImageFont.truetype("/usr/share/fonts/TTF/DejaVuSans-Bold.ttf", 26)
    except Exception:
        font_title = font_main = font_sub = ImageFont.load_default()

    # Top Header Banner
    draw.rectangle([(0, 0), (WIDTH, 110)], fill=(0, 150, 214))
    draw.text((40, 35), "VMAX SINGLE BOX", fill=(255, 255, 255), font=font_title)

    # Single Centered Box (Y: 200 - 600)
    draw.rectangle([(30, 200), (610, 600)], fill=(18, 28, 48), outline=(0, 230, 118), width=4)
    draw.text((60, 240), "MESSAGE CARD:", fill=(200, 220, 240), font=font_sub)
    draw.text((60, 310), text, fill=(0, 230, 118), font=font_main)
    draw.text((60, 480), "STRIDE = 0 (SINGLE BOX)", fill=(255, 215, 0), font=font_sub)

    out_dir = "dashboard_tmp"
    os.makedirs(out_dir, exist_ok=True)
    ppm_path = os.path.join(out_dir, "zerostride.ppm")
    jpg_path = os.path.join(out_dir, "zerostride.jpg")

    header = f"P6\n{WIDTH} {HEIGHT}\n255\n".encode('ascii')
    with open(ppm_path, 'wb') as f:
        f.write(header)
        f.write(img.tobytes())

    cmd = ['ffmpeg', '-y', '-i', ppm_path, '-vf', 'scale=640:1920', '-q:v', '2', jpg_path]
    subprocess.check_call(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    with open(jpg_path, 'rb') as f:
        return f.read()

def run_zero_stride_test(text="HELLO WORLD", duration_sec=10.0, interval_sec=1.0):
    dev_path = find_target_usb_device(0x33c3, 0xf101)
    if not dev_path:
        print("[ERROR] USB device 33c3:f101 not found dynamically.")
        return

    unbind_cdc_acm()
    print(f"=== MSDisplay Native Stride Zero Single-Box Driver Test (Text: '{text}') ===")
    print(f"[DYNAMIC LOOKUP] Target Device Node: {dev_path}")

    jpeg_bytes = generate_zero_stride_jpeg(text)
    
    # Header 640x1920 with Stride = 0 (Offset 0x08 = 0) and Flag = 0 (Offset 0x0A = 0)
    hdr = struct.pack("<IHHHH", MSDISPLAY_MAGIC_SIGNATURE, WIDTH, HEIGHT, 0, 0)
    payload = hdr + jpeg_bytes

    print(f"  Header Hex (12B) : {hdr.hex(' ')}")
    print(f"  Header Stride    : Offset 0x08 = 0 (Default Hardware Scanline Pitch)")
    print(f"  Header Flag      : Offset 0x0A = 0 (Fixed Flag)")
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
            print(f"  Frame #{seq:02d} ({len(payload)}B, Stride=0) -> USB Status: {res}B OK | Elapsed: {elapsed:.1f}s / {duration_sec}s")

            seq += 1
            time.sleep(interval_sec)

        print(f"\n[SUCCESS] Streamed {seq-1} Stride 0 single-box frames over {duration_sec}s.")
        print(f"[ACTION] OBSERVE PHYSICAL LCD PANEL: Check if 2-box / 3-box window multiplication is eliminated.")

    except Exception as e:
        print(f"[ERROR] Test error: {e}")
    finally:
        try: fcntl.ioctl(fd, USBDEVFS_RELEASEINTERFACE, iface_buf)
        except Exception: pass
        os.close(fd)

def main():
    parser = argparse.ArgumentParser(description="MSDisplay Native Stride Zero Single-Box Driver Test")
    parser.add_argument('--text', type=str, default="HELLO WORLD", help="Text to display")
    parser.add_argument('--duration', type=float, default=10.0, help="Stream duration in seconds (default: 10)")
    parser.add_argument('--interval', type=float, default=1.0, help="Keep-alive interval in seconds (default: 1.0)")
    args = parser.parse_args()
    run_zero_stride_test(text=args.text, duration_sec=args.duration, interval_sec=args.interval)

if __name__ == "__main__":
    main()
