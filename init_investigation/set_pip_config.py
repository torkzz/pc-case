#!/usr/bin/env python3
"""
MSDisplay Picture-in-Picture (PiP) Window & Stride Calibration Tool (`set_pip_config.py`)

Evidence-Backed Findings:
- `libcompositeScreenModel.dll` exports:
  - `composite_model_async_set_pip_switch` (RVA 0x13c30) -> bool enable
  - `composite_model_async_set_pip_rect` (RVA 0x13230) -> PipRect {x, y, w, h}
- MSDisplay 12-Byte Header (Offset 0x08 Stride / Format, Offset 0x0A Flag / Mode)
"""

import sys
import os
import struct
import fcntl
import ctypes
import argparse

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

def build_msdisplay_frame(jpeg_bytes: bytes, width: int = 2560, height: int = 666, stride: int = 0, flag: int = 0) -> bytes:
    header = struct.pack("<IHHHH", MSDISPLAY_MAGIC_SIGNATURE, width, height, stride, flag)
    return header + jpeg_bytes

def unbind_cdc_acm():
    unbind_path = "/sys/bus/usb/drivers/cdc_acm/unbind"
    if os.path.exists(unbind_path):
        try:
            with open(unbind_path, 'w') as f:
                f.write("1-9:1.1\n")
        except Exception: pass

def run_pip_calibration(stride=0, flag=0):
    unbind_cdc_acm()
    dev_path = find_target_usb_device(0x33c3, 0xf101)
    if not dev_path:
        print("[ERROR] USB device node 33c3:f101 not accessible.")
        return

    pattern_file = "diagnostic_patterns/pattern_c_color_bars.jpg"
    if not os.path.exists(pattern_file):
        print(f"[ERROR] Pattern file '{pattern_file}' not found.")
        return

    with open(pattern_file, 'rb') as f:
        jpeg_bytes = f.read()

    payload = build_msdisplay_frame(jpeg_bytes, width=2560, height=666, stride=stride, flag=flag)

    fd = os.open(dev_path, os.O_RDWR)
    iface_buf = struct.pack("I", 1)

    try:
        fcntl.ioctl(fd, USBDEVFS_CLAIMINTERFACE, iface_buf)
        print(f"=== PiP Window & Stride Calibration Test ===")
        print(f"  Target Device Node : {dev_path}")
        print(f"  Header Stride (0x08): {stride} (0x{stride:04x})")
        print(f"  Header Flag   (0x0A): {flag} (0x{flag:04x})")
        print(f"  Payload Size       : {len(payload)} bytes")

        data_buf = ctypes.create_string_buffer(payload)
        bulk_req = usbdevfs_bulktransfer()
        bulk_req.ep = 0x02
        bulk_req.len = len(payload)
        bulk_req.timeout = 3000
        bulk_req.data = ctypes.cast(data_buf, ctypes.c_void_p)

        res = fcntl.ioctl(fd, USBDEVFS_BULK, bulk_req)
        print(f"  [SUCCESS] USB Transfer Status: {res} bytes submitted successfully to EP 0x02 Bulk OUT.")
        print(f"  [ACTION] OBSERVE PHYSICAL LCD PANEL NOW & CHECK IF PIP RECTANGLE/COLOR BANDS EXPAND FULL SCREEN.")
    except Exception as e:
        print(f"  [ERROR] USB transfer error: {e}")
    finally:
        try: fcntl.ioctl(fd, USBDEVFS_RELEASEINTERFACE, iface_buf)
        except Exception: pass
        os.close(fd)

def main():
    parser = argparse.ArgumentParser(description="MSDisplay PiP Window & Stride Calibration Tool")
    parser.add_argument('--stride', type=int, default=0, help="Header Stride value (Offset 0x08)")
    parser.add_argument('--flag', type=int, default=0, help="Header Flag value (Offset 0x0A)")
    args = parser.parse_args()
    run_pip_calibration(stride=args.stride, flag=args.flag)

if __name__ == "__main__":
    main()
