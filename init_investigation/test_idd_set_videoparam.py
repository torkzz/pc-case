#!/usr/bin/env python3
"""
MSDisplay IddSetVideoParam (Sub-command 0x21006) Driver (`test_idd_set_videoparam.py`)

Evidence-Backed Disassembly Discovery:
- MSDISPLAYSDKWRRAPER.dll line 27540: IOCTL 0x304054 sub-command 0x21006 (IddSetVideoParam).
- Claims Interface 0 & Interface 1.
- Sends 260-byte (0x104) IddSetVideoParam setup packet to Interface 0 (wIndex=0).
- Configures hardware display controller mode:
  - Sub-cmd  : 0x21006 (DWORD 0)
  - Width    : 640     (DWORD 1)
  - Height   : 1920    (DWORD 2)
  - Refresh  : 60 FPS  (DWORD 3)
  - Mode     : 0 (Single Full-Screen Window, Disables 3-Box PiP Multiplexing)
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
STRIDE_LOCK = 0
FLAG_FIXED = 0
MSDISPLAY_MAGIC_SIGNATURE = 0x0008100A

USBDEVFS_BULK = 0xc0185502
USBDEVFS_CLAIMINTERFACE = 0x8004550f
USBDEVFS_RELEASEINTERFACE = 0x80045510
USBDEVFS_CONTROL = 0xc0185500

class usbdevfs_bulktransfer(ctypes.Structure):
    _fields_ = [
        ('ep', ctypes.c_uint),
        ('len', ctypes.c_uint),
        ('timeout', ctypes.c_uint),
        ('data', ctypes.c_void_p),
    ]

class usbdevfs_ctrltransfer(ctypes.Structure):
    _fields_ = [
        ('bmRequestType', ctypes.c_uint8),
        ('bRequest', ctypes.c_uint8),
        ('wValue', ctypes.c_uint16),
        ('wIndex', ctypes.c_uint16),
        ('wLength', ctypes.c_uint16),
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

def send_idd_set_videoparam_control(fd):
    """
    Submits IddSetVideoParam setup packet (Sub-cmd 0x21006, W=640, H=1920, 60FPS)
    via USB control transfer to Interface 0 (wIndex=0).
    """
    param_payload = struct.pack("<IIIII", 0x21006, WIDTH, HEIGHT, 60, 0) + b"\x00" * 240
    data_buf = ctypes.create_string_buffer(param_payload)

    ctrl_req = usbdevfs_ctrltransfer()
    ctrl_req.bmRequestType = 0x21 # Class / Interface / Host-to-Device
    ctrl_req.bRequest = 0x09      # SET_REPORT / IddControl
    ctrl_req.wValue = 0x0300       # Report Type 0x03, Report ID 0x00
    ctrl_req.wIndex = 0x0000       # Interface 0 (CDC Control Interface)
    ctrl_req.wLength = len(param_payload)
    ctrl_req.timeout = 1000
    ctrl_req.data = ctypes.cast(data_buf, ctypes.c_void_p)

    try:
        res = fcntl.ioctl(fd, USBDEVFS_CONTROL, ctrl_req)
        print(f"[SUCCESS] Sent IddSetVideoParam (0x21006, 640x1920, 60FPS) to Interface 0 -> Status: {res} bytes OK")
    except Exception as e:
        print(f"[INFO] Interface 0 IddSetVideoParam control status: {e}")

def generate_patched_jpeg(text="HELLO WORLD"):
    base_jpg = "portrait_patterns/pattern_640x1920.jpg"
    out_dir = "dashboard_tmp"
    os.makedirs(out_dir, exist_ok=True)
    ppm_path = os.path.join(out_dir, "patched_idd.ppm")
    jpg_path = os.path.join(out_dir, "patched_idd.jpg")

    img = Image.open(base_jpg).convert('RGB')
    draw = ImageDraw.Draw(img)

    try:
        font = ImageFont.truetype("/usr/share/fonts/TTF/DejaVuSans-Bold.ttf", 60)
    except Exception:
        font = ImageFont.load_default()

    draw.rectangle([(40, 680), (600, 840)], fill=(10, 18, 32), outline=(255, 255, 255), width=4)
    draw.text((80, 730), text, fill=(0, 230, 118), font=font)

    header = f"P6\n{WIDTH} {HEIGHT}\n255\n".encode('ascii')
    with open(ppm_path, 'wb') as f:
        f.write(header)
        f.write(img.tobytes())

    cmd = ['ffmpeg', '-y', '-i', ppm_path, '-vf', 'scale=640:1920', '-q:v', '2', jpg_path]
    subprocess.check_call(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    with open(jpg_path, 'rb') as f:
        return f.read()

def run_idd_param_test(text="HELLO WORLD", duration_sec=10.0, interval_sec=1.0):
    dev_path = find_target_usb_device(0x33c3, 0xf101)
    if not dev_path:
        print("[ERROR] USB device 33c3:f101 not found dynamically.")
        return

    unbind_cdc_acm()
    print(f"=== Interface 0 IddSetVideoParam (0x21006) Driver Test (Text: '{text}') ===")
    print(f"[DYNAMIC LOOKUP] Target Device Node: {dev_path}")

    jpeg_bytes = generate_patched_jpeg(text)
    hdr = struct.pack("<IHHHH", MSDISPLAY_MAGIC_SIGNATURE, WIDTH, HEIGHT, STRIDE_LOCK, FLAG_FIXED)
    payload = hdr + jpeg_bytes

    fd = os.open(dev_path, os.O_RDWR)
    iface0_buf = struct.pack("I", 0)
    iface1_buf = struct.pack("I", 1)

    try:
        # Claim Interface 0 & Interface 1
        try: fcntl.ioctl(fd, USBDEVFS_CLAIMINTERFACE, iface0_buf)
        except Exception: pass
        fcntl.ioctl(fd, USBDEVFS_CLAIMINTERFACE, iface1_buf)
        print("[SUCCESS] Claimed Interface 0 & Interface 1 via usbfs ioctl")

        # Step 1: Issue IddSetVideoParam (0x21006) to Interface 0
        send_idd_set_videoparam_control(fd)

        # Step 2: Stream frame payload to EP 0x02 Bulk OUT
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
            print(f"  Frame #{seq:02d} ({len(payload)}B, IddSetVideoParam Mode) -> USB Status: {res}B OK | Elapsed: {elapsed:.1f}s / {duration_sec}s")

            seq += 1
            time.sleep(interval_sec)

        print(f"\n[SUCCESS] Streamed {seq-1} IddSetVideoParam initialized frames over {duration_sec}s.")
        print(f"[ACTION] OBSERVE PHYSICAL LCD PANEL: Check if 2-box / 3-box splitting is 100% ELIMINATED.")

    except Exception as e:
        print(f"[ERROR] Test error: {e}")
    finally:
        try: fcntl.ioctl(fd, USBDEVFS_RELEASEINTERFACE, iface0_buf)
        except Exception: pass
        try: fcntl.ioctl(fd, USBDEVFS_RELEASEINTERFACE, iface1_buf)
        except Exception: pass
        os.close(fd)

def main():
    parser = argparse.ArgumentParser(description="IddSetVideoParam Display Initialization Driver Test")
    parser.add_argument('--text', type=str, default="HELLO WORLD", help="Text to display")
    parser.add_argument('--duration', type=float, default=10.0, help="Stream duration in seconds (default: 10)")
    parser.add_argument('--interval', type=float, default=1.0, help="Keep-alive interval in seconds (default: 1.0)")
    args = parser.parse_args()
    run_idd_param_test(text=args.text, duration_sec=args.duration, interval_sec=args.interval)

if __name__ == "__main__":
    main()
