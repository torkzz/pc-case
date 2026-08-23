#!/usr/bin/env python3
"""
640x1920 Native Physical Panel Driver & Keep-Alive Daemon (`test_640x1920_native.py`)

Physical Discoveries:
1. Native Panel Geometry: 640 x 1920 pixels (exact 1:3 aspect ratio).
2. Standby Timeout: Firmware backlight auto-off occurs at T=4.0 seconds if no stream frame is submitted.
3. Refresh Loop: Periodic frame submission every 1.0 second maintains continuous backlight illumination without blinking.

Constructs 640x1920 4-Quarter Block Frame:
- Quarter 1 (Y: 0 - 480)   : Solid Red (255, 0, 0)
- Quarter 2 (Y: 480 - 960)  : Solid Green (0, 255, 0)
- Quarter 3 (Y: 960 - 1440) : Solid Blue (0, 0, 255)
- Quarter 4 (Y: 1440 - 1920): Solid White (255, 255, 255)
"""

import os
import sys
import time
import struct
import fcntl
import ctypes
import subprocess
import argparse

WIDTH = 640
HEIGHT = 1920
OUT_DIR = "portrait_patterns"
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

def generate_640x1920_jpeg():
    ppm_file = os.path.join(OUT_DIR, "pattern_640x1920.ppm")
    jpg_file = os.path.join(OUT_DIR, "pattern_640x1920.jpg")

    header = f"P6\n{WIDTH} {HEIGHT}\n255\n".encode('ascii')
    pixels = bytearray(WIDTH * HEIGHT * 3)

    q1 = 480
    q2 = 960
    q3 = 1440

    for y in range(HEIGHT):
        if y < q1: r, g, b = 255, 0, 0         # Red (Quarter 1: Top)
        elif y < q2: r, g, b = 0, 255, 0       # Green (Quarter 2: Upper Mid)
        elif y < q3: r, g, b = 0, 0, 255       # Blue (Quarter 3: Lower Mid)
        else: r, g, b = 255, 255, 255          # White (Quarter 4: Bottom)

        for x in range(WIDTH):
            idx = (y * WIDTH + x) * 3
            pixels[idx] = r
            pixels[idx+1] = g
            pixels[idx+2] = b

    with open(ppm_file, 'wb') as f:
        f.write(header)
        f.write(pixels)

    cmd = ['ffmpeg', '-y', '-i', ppm_file, '-q:v', '2', jpg_file]
    subprocess.check_call(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return jpg_file

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

def run_1920_native_driver(duration_sec=15.0, interval_sec=1.0):
    jpg_file = generate_640x1920_jpeg()
    with open(jpg_file, 'rb') as f:
        jpeg_bytes = f.read()

    dev_path = find_target_usb_device(0x33c3, 0xf101)
    if not dev_path:
        print("[ERROR] USB device 33c3:f101 not found.")
        return

    unbind_cdc_acm()
    fd = os.open(dev_path, os.O_RDWR)
    iface_buf = struct.pack("I", 1)

    try:
        fcntl.ioctl(fd, USBDEVFS_CLAIMINTERFACE, iface_buf)
        print(f"=== 640x1920 Native Physical Panel Driver ({duration_sec}s Stream) ===")

        # Header 640x1920 (W=640 0x0280, H=1920 0x0780)
        hdr = struct.pack("<IHHHH", MSDISPLAY_MAGIC_SIGNATURE, WIDTH, HEIGHT, 0, 1)
        payload = hdr + jpeg_bytes

        start_time = time.monotonic()
        tx_count = 0

        while (time.monotonic() - start_time) < duration_sec:
            data_buf = ctypes.create_string_buffer(payload)
            bulk_req = usbdevfs_bulktransfer()
            bulk_req.ep = 0x02
            bulk_req.len = len(payload)
            bulk_req.timeout = 1000
            bulk_req.data = ctypes.cast(data_buf, ctypes.c_void_p)

            res = fcntl.ioctl(fd, USBDEVFS_BULK, bulk_req)
            tx_count += 1
            elapsed = time.monotonic() - start_time
            print(f"  Frame {tx_count:02d} (640x1920, {len(payload)}B) -> USB Status: {res} bytes OK | Elapsed: {elapsed:.1f}s / {duration_sec}s")
            time.sleep(interval_sec)

        print(f"\n  [SUCCESS] 640x1920 native stream active for {duration_sec}s ({tx_count} keep-alive frames sent).")
        print("  [ACTION] OBSERVE PHYSICAL LCD PANEL NOW: Check if Red (top), Green (upper-mid), Blue (lower-mid), White (bottom) fit 100% full screen.")

    except Exception as e:
        print(f"  [ERROR] USB transfer error: {e}")
    finally:
        try: fcntl.ioctl(fd, USBDEVFS_RELEASEINTERFACE, iface_buf)
        except Exception: pass
        os.close(fd)

def main():
    parser = argparse.ArgumentParser(description="640x1920 Native Physical Panel Driver")
    parser.add_argument('--duration', type=float, default=15.0, help="Stream duration in seconds (default: 15)")
    parser.add_argument('--interval', type=float, default=1.0, help="Keep-alive interval in seconds (default: 1.0)")
    args = parser.parse_args()
    run_1920_native_driver(duration_sec=args.duration, interval_sec=args.interval)

if __name__ == "__main__":
    main()
