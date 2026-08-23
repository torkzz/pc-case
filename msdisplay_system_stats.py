#!/usr/bin/env python3
"""
MSDisplay 640x1920 System Stats Monitor (`msdisplay_system_stats.py`)
"""

import sys
import os
import time
import struct
import fcntl
import ctypes
import argparse
from PIL import Image, ImageDraw, ImageFont

WIDTH = 640
HEIGHT = 1920
STRIDE_LOCK = 0
FLAG_ONE = 1
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

def generate_dashboard_image(cpu_pct, mem_pct, disk_pct, mem_used, mem_total, uptime_str):
    import io
    img = Image.new('RGB', (WIDTH, HEIGHT), color=(10, 18, 32))
    draw = ImageDraw.Draw(img)

    try:
        font_title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 36)
        font_val   = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 46)
        font_sub   = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 24)
    except Exception:
        font_title = font_val = font_sub = ImageFont.load_default()

    draw.rectangle([(10, 10), (630, 1910)], outline=(0, 200, 255), width=4)

    draw.rectangle([(25, 40), (615, 450)], fill=(18, 28, 48), outline=(0, 180, 216), width=3)
    draw.rectangle([(25, 40), (615, 110)], fill=(0, 150, 214))
    draw.text((45, 55), "CPU UTILIZATION", fill=(255, 255, 255), font=font_title)
    cpu_color = (0, 230, 118) if cpu_pct < 70 else (255, 171, 0) if cpu_pct < 85 else (255, 23, 68)
    draw.text((55, 140), f"{cpu_pct}%", fill=cpu_color, font=font_val)

    buf = io.BytesIO()
    img.save(buf, format="JPEG", quality=75)
    return buf.getvalue()

def render_dashboard_frame(cpu_pct, mem_pct, disk_pct, mem_used, mem_total, uptime):
    jpeg_bytes = generate_dashboard_image(cpu_pct, mem_pct, disk_pct, mem_used, mem_total, uptime)
    hdr = struct.pack("<IHHHH", MSDISPLAY_MAGIC_SIGNATURE, WIDTH, HEIGHT, STRIDE_LOCK, FLAG_ONE)
    return hdr + jpeg_bytes

def start_stats_daemon(duration_sec=15.0, interval_sec=1.0):
    dev_path = find_target_usb_device(0x33c3, 0xf101)
    if not dev_path:
        print("[ERROR] USB device 33c3:f101 not found.")
        return

    unbind_cdc_acm()
    fd = os.open(dev_path, os.O_RDWR)
    iface_buf = struct.pack("I", 1)

    try:
        fcntl.ioctl(fd, USBDEVFS_CLAIMINTERFACE, iface_buf)
        seq_cnt = 1
        start_time = time.monotonic()

        while (time.monotonic() - start_time) < duration_sec:
            payload = render_dashboard_frame(25, 40, 50, 8000, 16000, "1h")

            data_buf = ctypes.create_string_buffer(payload)
            bulk_req = usbdevfs_bulktransfer()
            bulk_req.ep = 0x02
            bulk_req.len = len(payload)
            bulk_req.timeout = 2000
            bulk_req.data = ctypes.cast(data_buf, ctypes.c_void_p)

            res = fcntl.ioctl(fd, USBDEVFS_BULK, bulk_req)
            print(f"Frame #{seq_cnt:02d} sent OK ({len(payload)}B)")
            seq_cnt += 1
            time.sleep(interval_sec)

    finally:
        try: fcntl.ioctl(fd, USBDEVFS_RELEASEINTERFACE, iface_buf)
        except Exception: pass
        os.close(fd)

def main():
    start_stats_daemon(duration_sec=5.0, interval_sec=1.0)

if __name__ == "__main__":
    main()
