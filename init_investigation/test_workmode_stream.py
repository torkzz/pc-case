#!/usr/bin/env python3
"""
MSDisplay WorkMode Stream Mode Initialization & Driver (`test_workmode_stream.py`)

Evidence-Backed Discovery:
- `libcompositeScreenModel.dll` export `async_set_work_mode` (RVA 0x14ac0):
  - `WorkMode::StreamMode = 0` -> Disables local SPI Flash asset multiplexing (tiling).
  - Locks hardware compositor exclusively to incoming live USB video stream.
"""

import sys
import os
import time
import struct
import fcntl
import ctypes
import subprocess
import argparse
import serial
from PIL import Image, ImageDraw, ImageFont

WIDTH = 640
HEIGHT = 1920
STRIDE_LOCK = 1920
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

def crc16_modbus(data: bytes) -> int:
    crc = 0xFFFF
    for b in data:
        crc ^= b
        for _ in range(8):
            if crc & 1:
                crc = (crc >> 1) ^ 0xA001
            else:
                crc >>= 1
    return crc & 0xFFFF

def build_cdc_frame(cmd: int, content: bytes = b"") -> bytes:
    payload_len = len(content)
    calc_len = payload_len + 2
    ctrl_val = calc_len & 0x0FFF
    ctrl_bytes = ctrl_val.to_bytes(2, 'big')
    cmd_bytes = cmd.to_bytes(2, 'big')
    body = ctrl_bytes + cmd_bytes + content
    crc_bytes = b"\x00\x00"
    return b"AH" + body + crc_bytes + b"MI"

def send_cdc_workmode_stream():
    port_path = "/dev/ttyACM0"
    if not os.path.exists(port_path):
        return False

    try:
        ser = serial.Serial(port_path, 115200, timeout=1.0)
        # CMD 0x0071 ChangeStatus: content = [0x00] (WorkMode::StreamMode = 0)
        frame_stream_mode = build_cdc_frame(0x0071, b"\x00")
        ser.write(frame_stream_mode)
        ser.flush()
        ser.close()
        print("[SUCCESS] Sent WorkMode::StreamMode (0x00) over /dev/ttyACM0")
        return True
    except Exception as e:
        print(f"[INFO] CDC ACM WorkMode status: {e}")
        return False

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

def generate_stream_jpeg(text="HELLO WORLD"):
    img = Image.new('RGB', (WIDTH, HEIGHT), color=(10, 18, 32))
    draw = ImageDraw.Draw(img)

    try:
        font_title = ImageFont.truetype("/usr/share/fonts/TTF/DejaVuSans-Bold.ttf", 38)
        font_main  = ImageFont.truetype("/usr/share/fonts/TTF/DejaVuSans-Bold.ttf", 46)
        font_sub   = ImageFont.truetype("/usr/share/fonts/TTF/DejaVuSans-Bold.ttf", 26)
    except Exception:
        font_title = font_main = font_sub = ImageFont.load_default()

    draw.rectangle([(0, 0), (WIDTH, 110)], fill=(0, 150, 214))
    draw.text((40, 35), "VMAX LCD STREAM MODE", fill=(255, 255, 255), font=font_title)

    draw.rectangle([(30, 200), (610, 600)], fill=(18, 28, 48), outline=(0, 230, 118), width=4)
    draw.text((60, 240), "STREAM MESSAGE:", fill=(200, 220, 240), font=font_sub)
    draw.text((60, 310), text, fill=(0, 230, 118), font=font_main)
    draw.text((60, 480), "WORK MODE: STREAM (0x00)", fill=(255, 215, 0), font=font_sub)

    out_dir = "dashboard_tmp"
    os.makedirs(out_dir, exist_ok=True)
    ppm_path = os.path.join(out_dir, "workmode_text.ppm")
    jpg_path = os.path.join(out_dir, "workmode_text.jpg")

    header = f"P6\n{WIDTH} {HEIGHT}\n255\n".encode('ascii')
    with open(ppm_path, 'wb') as f:
        f.write(header)
        f.write(img.tobytes())

    cmd = ['ffmpeg', '-y', '-i', ppm_path, '-vf', 'scale=640:1920', '-q:v', '2', jpg_path]
    subprocess.check_call(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    with open(jpg_path, 'rb') as f:
        return f.read()

def run_workmode_test(text="HELLO WORLD", duration_sec=10.0, interval_sec=1.0):
    # Step 1: Send WorkMode::StreamMode = 0 via CDC ACM
    send_cdc_workmode_stream()

    # Step 2: Unbind CDC ACM and claim usbfs Interface 1
    dev_path = find_target_usb_device(0x33c3, 0xf101)
    if not dev_path:
        print("[ERROR] USB device 33c3:f101 not found dynamically.")
        return

    unbind_cdc_acm()
    print(f"=== WorkMode::StreamMode Video Stream Test (Text: '{text}') ===")
    print(f"[DYNAMIC LOOKUP] Target Device Node: {dev_path}")

    jpeg_bytes = generate_stream_jpeg(text)
    hdr = struct.pack("<IHHHH", MSDISPLAY_MAGIC_SIGNATURE, WIDTH, HEIGHT, STRIDE_LOCK, FLAG_FIXED)
    payload = hdr + jpeg_bytes

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
            print(f"  Frame #{seq:02d} ({len(payload)}B, StreamMode=0) -> USB Status: {res}B OK | Elapsed: {elapsed:.1f}s / {duration_sec}s")

            seq += 1
            time.sleep(interval_sec)

        print(f"\n[SUCCESS] Streamed {seq-1} WorkMode::StreamMode frames over {duration_sec}s.")
        print(f"[ACTION] OBSERVE PHYSICAL LCD PANEL: Check if 2-box / 3-box tiling is 100% ELIMINATED.")

    except Exception as e:
        print(f"[ERROR] Test error: {e}")
    finally:
        try: fcntl.ioctl(fd, USBDEVFS_RELEASEINTERFACE, iface_buf)
        except Exception: pass
        os.close(fd)

def main():
    parser = argparse.ArgumentParser(description="WorkMode Stream Mode Initialization & Driver Test")
    parser.add_argument('--text', type=str, default="HELLO WORLD", help="Text to display")
    parser.add_argument('--duration', type=float, default=10.0, help="Stream duration in seconds (default: 10)")
    parser.add_argument('--interval', type=float, default=1.0, help="Keep-alive interval in seconds (default: 1.0)")
    args = parser.parse_args()
    run_workmode_test(text=args.text, duration_sec=args.duration, interval_sec=args.interval)

if __name__ == "__main__":
    main()
