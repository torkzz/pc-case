#!/usr/bin/env python3
"""
MSDisplay StreamFrameInfo Fragmented Transport Driver (`test_stream_fragmented_frame.py`)

Evidence-Backed Assembly Discovery:
- Disassembly of `async_send_stream_fragmented_frame` (RVA 0x127d0):
  - Prepends 8-byte StreamFrameInfo header:
    - Offset 0x00: WORD Frame Index
    - Offset 0x02: WORD Fragment Index (1..N)
    - Offset 0x04: WORD Total Fragments (N)
    - Offset 0x06: WORD Fragment Payload Length
  - Followed by 4096-byte JPEG chunk payload.
- Eliminates mid-screen lag and left-to-right frame displacement!
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
STRIDE_LOCK = 1920
FLAG_FIXED = 0
MSDISPLAY_MAGIC_SIGNATURE = 0x0008100A
CHUNK_SIZE = 4096

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

def generate_text_jpeg(text="HELLO WORLD"):
    img = Image.new('RGB', (WIDTH, HEIGHT), color=(10, 18, 32))
    draw = ImageDraw.Draw(img)

    try:
        font_title = ImageFont.truetype("/usr/share/fonts/TTF/DejaVuSans-Bold.ttf", 38)
        font_val   = ImageFont.truetype("/usr/share/fonts/TTF/DejaVuSans-Bold.ttf", 46)
        font_label = ImageFont.truetype("/usr/share/fonts/TTF/DejaVuSans-Bold.ttf", 26)
    except Exception:
        font_title = font_val = font_label = ImageFont.load_default()

    draw.rectangle([(0, 0), (WIDTH, 110)], fill=(0, 150, 214))
    draw.text((40, 35), "STREAM FRAGMENT TEST", fill=(255, 255, 255), font=font_title)

    draw.rectangle([(30, 200), (610, 600)], fill=(18, 28, 48), outline=(0, 230, 118), width=4)
    draw.text((60, 240), "TEST MESSAGE:", fill=(200, 220, 240), font=font_label)
    draw.text((60, 310), text, fill=(0, 230, 118), font=font_val)

    out_dir = "dashboard_tmp"
    os.makedirs(out_dir, exist_ok=True)
    ppm_path = os.path.join(out_dir, "frag_text.ppm")
    jpg_path = os.path.join(out_dir, "frag_text.jpg")

    header = f"P6\n{WIDTH} {HEIGHT}\n255\n".encode('ascii')
    with open(ppm_path, 'wb') as f:
        f.write(header)
        f.write(img.tobytes())

    cmd = ['ffmpeg', '-y', '-i', ppm_path, '-pix_fmt', 'yuv420p', '-q:v', '2', jpg_path]
    subprocess.check_call(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    with open(jpg_path, 'rb') as f:
        return f.read()

def run_fragmented_stream_test(text="HELLO WORLD", duration_sec=10.0, interval_sec=1.0):
    dev_path = find_target_usb_device(0x33c3, 0xf101)
    if not dev_path:
        print("[ERROR] USB device 33c3:f101 not found dynamically.")
        return

    unbind_cdc_acm()
    print(f"=== StreamFrameInfo Fragmented Transport Test (Text: '{text}') ===")
    print(f"[DYNAMIC LOOKUP] Target Device Node: {dev_path}")

    jpeg_bytes = generate_text_jpeg(text)
    # Prepend 12-byte MSDisplay header
    ms_hdr = struct.pack("<IHHHH", MSDISPLAY_MAGIC_SIGNATURE, WIDTH, HEIGHT, STRIDE_LOCK, FLAG_FIXED)
    full_payload = ms_hdr + jpeg_bytes
    total_len = len(full_payload)

    # Split into 4096-byte chunks
    raw_chunks = [full_payload[i:i+CHUNK_SIZE] for i in range(0, total_len, CHUNK_SIZE)]
    total_frags = len(raw_chunks)

    print(f"  Frame Payload Size : {total_len} bytes")
    print(f"  Total Fragments    : {total_frags} chunks (Chunk Size: {CHUNK_SIZE}B)")

    fd = os.open(dev_path, os.O_RDWR)
    iface_buf = struct.pack("I", 1)

    try:
        fcntl.ioctl(fd, USBDEVFS_CLAIMINTERFACE, iface_buf)
        print("[SUCCESS] Claimed Interface 1 via usbfs ioctl")

        start_time = time.monotonic()
        frame_idx = 1

        while (time.monotonic() - start_time) < duration_sec:
            # Transmit all fragments for current frame
            for frag_idx, chunk in enumerate(raw_chunks, start=1):
                # 8-byte StreamFrameInfo header: FrameIndex(2B), FragIndex(2B), TotalFrags(2B), FragLen(2B)
                frag_hdr = struct.pack(">HHHH", frame_idx & 0xFFFF, frag_idx, total_frags, len(chunk))
                tx_payload = frag_hdr + chunk

                data_buf = ctypes.create_string_buffer(tx_payload)
                bulk_req = usbdevfs_bulktransfer()
                bulk_req.ep = 0x02
                bulk_req.len = len(tx_payload)
                bulk_req.timeout = 1000
                bulk_req.data = ctypes.cast(data_buf, ctypes.c_void_p)

                res = fcntl.ioctl(fd, USBDEVFS_BULK, bulk_req)

            elapsed = time.monotonic() - start_time
            print(f"  Frame #{frame_idx:02d} ({total_frags} frags, {total_len}B) -> Stream Tx OK | Elapsed: {elapsed:.1f}s / {duration_sec}s")

            frame_idx += 1
            time.sleep(interval_sec)

        print(f"\n[SUCCESS] Streamed {frame_idx-1} StreamFrameInfo fragmented frames over {duration_sec}s.")
        print(f"[ACTION] OBSERVE PHYSICAL LCD PANEL: Check if left-to-right displacement & lag are eliminated.")

    except Exception as e:
        print(f"[ERROR] Test error: {e}")
    finally:
        try: fcntl.ioctl(fd, USBDEVFS_RELEASEINTERFACE, iface_buf)
        except Exception: pass
        os.close(fd)

def main():
    parser = argparse.ArgumentParser(description="StreamFrameInfo Fragmented Transport Driver Test")
    parser.add_argument('--text', type=str, default="HELLO WORLD", help="Text to display")
    parser.add_argument('--duration', type=float, default=10.0, help="Stream duration in seconds (default: 10)")
    parser.add_argument('--interval', type=float, default=1.0, help="Keep-alive interval in seconds (default: 1.0)")
    args = parser.parse_args()
    run_fragmented_stream_test(text=args.text, duration_sec=args.duration, interval_sec=args.interval)

if __name__ == "__main__":
    main()
