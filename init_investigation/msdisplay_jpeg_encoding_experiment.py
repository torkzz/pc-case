#!/usr/bin/env python3
"""
MSDisplay Controlled JPEG Subsampling & Quality Experiment (`msdisplay_jpeg_encoding_experiment.py`)

Tests whether image corruption is caused by JPEG chroma subsampling / color format:
- TEST 1: Baseline JPEG (YUV 4:2:0) -> ffmpeg -pix_fmt yuv420p
- TEST 2: YUV 4:4:4 Subsampling     -> ffmpeg -pix_fmt yuv444p
- TEST 3: YUV 4:2:2 Subsampling     -> ffmpeg -pix_fmt yuv422p
- TEST 4: YUV 4:0:0 (Grayscale)     -> ffmpeg -pix_fmt gray

Keeps EXACT SAME dimensions (2560x666), 12-byte header (0x0008100A), Interface 1, EP 0x02 Bulk OUT.
Halts after EACH test to await physical LCD observation.
"""

import sys
import os
import time
import struct
import fcntl
import ctypes
import subprocess
import argparse

WIDTH = 2560
HEIGHT = 666
OUT_DIR = "jpeg_encoding_patterns"
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

def generate_jpeg_variant(pix_fmt="yuv420p", quality=2):
    ppm_file = os.path.join(OUT_DIR, "base_4quarter.ppm")
    jpg_file = os.path.join(OUT_DIR, f"4quarter_{pix_fmt}_q{quality}.jpg")

    if not os.path.exists(ppm_file):
        header = f"P6\n{WIDTH} {HEIGHT}\n255\n".encode('ascii')
        pixels = bytearray(WIDTH * HEIGHT * 3)

        q1_end = 166
        q2_end = 333
        q3_end = 499

        for y in range(HEIGHT):
            if y < q1_end: r, g, b = 255, 0, 0        # Red
            elif y < q2_end: r, g, b = 0, 255, 0      # Green
            elif y < q3_end: r, g, b = 0, 0, 255      # Blue
            else: r, g, b = 255, 255, 255         # White

            for x in range(WIDTH):
                idx = (y * WIDTH + x) * 3
                pixels[idx] = r
                pixels[idx+1] = g
                pixels[idx+2] = b

        with open(ppm_file, 'wb') as f:
            f.write(header)
            f.write(pixels)

    cmd = ['ffmpeg', '-y', '-i', ppm_file, '-vf', f'format={pix_fmt}', '-q:v', str(quality), jpg_file]
    subprocess.check_call(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return jpg_file

def parse_jpeg_sof(jpeg_path):
    with open(jpeg_path, 'rb') as f: data = f.read()
    idx = 2
    size = len(data)
    while idx < size - 8:
        if data[idx] != 0xFF:
            idx += 1
            continue
        marker = data[idx+1]
        if marker in (0xC0, 0xC1, 0xC2, 0xC3):
            height = struct.unpack(">H", data[idx+5:idx+7])[0]
            width = struct.unpack(">H", data[idx+7:idx+9])[0]
            comp = data[idx+9]
            return f"0xFF{marker:02X}", width, height, comp
        else:
            length = struct.unpack(">H", data[idx+2:idx+4])[0]
            idx += 2 + length
    return "UNKNOWN", 0, 0, 0

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

def build_msdisplay_frame(jpeg_bytes: bytes, width: int = 2560, height: int = 666) -> bytes:
    header = struct.pack("<IHHHH", MSDISPLAY_MAGIC_SIGNATURE, width, height, 0, 0)
    return header + jpeg_bytes

def unbind_cdc_acm():
    unbind_path = "/sys/bus/usb/drivers/cdc_acm/unbind"
    if os.path.exists(unbind_path):
        try:
            with open(unbind_path, 'w') as f:
                f.write("1-9:1.1\n")
        except Exception: pass

def run_jpeg_experiment(test_num=1):
    unbind_cdc_acm()

    dev_path = find_target_usb_device(0x33c3, 0xf101)
    if not dev_path:
        print("[ERROR] USB device node 33c3:f101 not dynamically accessible.")
        return

    test_configs = {
        1: ("yuv420p", 2, "TEST 1 — Baseline YUV 4:2:0 Subsampling"),
        2: ("yuv444p", 2, "TEST 2 — YUV 4:4:4 Subsampling (No Chroma Subsampling)"),
        3: ("yuv422p", 2, "TEST 3 — YUV 4:2:2 Subsampling (Horizontal 2:1 Chroma)"),
        4: ("gray",    2, "TEST 4 — YUV 4:0:0 Subsampling (Monochrome Grayscale)")
    }

    if test_num not in test_configs:
        print(f"[ERROR] Invalid Test Number {test_num}. Choices: 1, 2, 3, 4")
        return

    pix_fmt, quality, test_desc = test_configs[test_num]
    jpg_path = generate_jpeg_variant(pix_fmt, quality)

    with open(jpg_path, 'rb') as f:
        jpeg_bytes = f.read()

    sof_marker, w_jpg, h_jpg, comp = parse_jpeg_sof(jpg_path)
    hdr = struct.pack("<IHHHH", MSDISPLAY_MAGIC_SIGNATURE, WIDTH, HEIGHT, 0, 0)
    payload = hdr + jpeg_bytes

    print(f"\n==================================================")
    print(f"JPEG ENCODING EXPERIMENT — {test_desc}")
    print(f"  TEST               : TEST {test_num}")
    print(f"  JPEG FILE          : {jpg_path}")
    print(f"  JPEG SIZE          : {len(jpeg_bytes)} bytes")
    print(f"  JPEG DIMENSIONS    : {w_jpg} x {h_jpg}")
    print(f"  JPEG SOF           : {sof_marker} (Components: {comp})")
    print(f"  CHROMA SUBSAMPLING : {pix_fmt}")
    print(f"  QUALITY            : Q={quality}")
    print(f"  MSDISPLAY HEADER   : {hdr.hex(' ')}")
    print(f"  TOTAL PAYLOAD      : {len(payload)} bytes")
    print(f"  USB DEVICE         : 33c3:f101 ({dev_path})")
    print(f"  INTERFACE          : Interface 1")
    print(f"  ENDPOINT           : 0x02 Bulk OUT")
    print(f"==================================================")

    fd = os.open(dev_path, os.O_RDWR)
    iface_buf = struct.pack("I", 1)

    try:
        fcntl.ioctl(fd, USBDEVFS_CLAIMINTERFACE, iface_buf)
        data_buf = ctypes.create_string_buffer(payload)
        bulk_req = usbdevfs_bulktransfer()
        bulk_req.ep = 0x02
        bulk_req.len = len(payload)
        bulk_req.timeout = 3000
        bulk_req.data = ctypes.cast(data_buf, ctypes.c_void_p)

        res = fcntl.ioctl(fd, USBDEVFS_BULK, bulk_req)
        print(f"  TRANSFER RESULT    : {res} bytes submitted successfully to EP 0x02 Bulk OUT.")
        print(f"\n  [ACTION] STOPPED. AWAITING PHYSICAL LCD OBSERVATION FOR TEST {test_num}.")
    except Exception as e:
        print(f"  [ERROR] USB transfer error: {e}")
    finally:
        try: fcntl.ioctl(fd, USBDEVFS_RELEASEINTERFACE, iface_buf)
        except Exception: pass
        os.close(fd)

def main():
    parser = argparse.ArgumentParser(description="MSDisplay Controlled JPEG Subsampling Experiment")
    parser.add_argument('--test', type=int, choices=[1, 2, 3, 4], default=1, help="Test Number (1=4:2:0, 2=4:4:4, 3=4:2:2, 4=4:0:0)")

    args = parser.parse_args()
    run_jpeg_experiment(args.test)

if __name__ == "__main__":
    main()
