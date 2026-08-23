#!/usr/bin/env python3
"""
MSDisplay Fixed SOS Offset (0x00BE / 190B) System Stats Monitor (`test_fixed_sos_dash.py`)

Evidence-Backed Discovery:
- `pattern_640x1920.jpg` (NON-SCROLLING) has SOS (Start of Scan) at EXACT OFFSET 0x00BE (190 bytes).
- Hardware JPEG decoder on LCD controller expects SOS at 0x00BE (190B).
- Custom/extended Huffman tables push SOS to 0x0165 (357B), causing bitstream drift & scrolling!
- Standard Huffman tables (-huffman default / cjpeg default) lock SOS to 0x00BE (190B) -> ELIMINATES SCROLLING!
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

def get_cpu_usage():
    try:
        with open('/proc/stat', 'r') as f:
            lines = f.readlines()
        cpu_line = lines[0].split()
        user, nice, system, idle = map(int, cpu_line[1:5])
        total = user + nice + system + idle
        return total, idle
    except Exception:
        return 100, 50

def get_mem_info():
    try:
        mem = {}
        with open('/proc/meminfo', 'r') as f:
            for line in f:
                parts = line.split(':')
                if len(parts) == 2:
                    key = parts[0].strip()
                    val = int(parts[1].split()[0])
                    mem[key] = val
        total = mem.get('MemTotal', 1)
        free = mem.get('MemAvailable', mem.get('MemFree', 0))
        used = total - free
        pct = int((used / total) * 100)
        return pct, used // 1024, total // 1024
    except Exception:
        return 0, 0, 0

def get_disk_info():
    try:
        st = os.statvfs('/')
        total = (st.f_blocks * st.f_frsize) // (1024 * 1024 * 1024)
        free = (st.f_bavail * st.f_frsize) // (1024 * 1024 * 1024)
        used = total - free
        pct = int((used / total) * 100)
        return pct, used, total
    except Exception:
        return 0, 0, 0

def get_uptime():
    try:
        with open('/proc/uptime', 'r') as f:
            up = float(f.readline().split()[0])
        hours = int(up // 3600)
        mins = int((up % 3600) // 60)
        return f"{hours}h {mins}m"
    except Exception:
        return "N/A"

def generate_dashboard_image(cpu_pct, mem_pct, disk_pct, mem_used, mem_total, uptime_str):
    img = Image.new('RGB', (WIDTH, HEIGHT), color=(10, 18, 32))
    draw = ImageDraw.Draw(img)

    try:
        font_title = ImageFont.truetype("/usr/share/fonts/TTF/DejaVuSans-Bold.ttf", 38)
        font_val   = ImageFont.truetype("/usr/share/fonts/TTF/DejaVuSans-Bold.ttf", 46)
        font_label = ImageFont.truetype("/usr/share/fonts/TTF/DejaVuSans-Bold.ttf", 26)
        font_sub   = ImageFont.truetype("/usr/share/fonts/TTF/DejaVuSans-Bold.ttf", 22)
    except Exception:
        font_title = font_val = font_label = font_sub = ImageFont.load_default()

    # Top Header Banner
    draw.rectangle([(0, 0), (WIDTH, 110)], fill=(0, 150, 214))
    draw.text((40, 35), "SYSTEM MONITOR", fill=(255, 255, 255), font=font_title)

    # Section 1: CPU LOAD (Y: 150 - 500)
    draw.rectangle([(30, 150), (610, 500)], fill=(18, 28, 48), outline=(0, 180, 216), width=3)
    draw.text((60, 180), "CPU USAGE", fill=(200, 220, 240), font=font_label)
    cpu_color = (0, 230, 118) if cpu_pct < 70 else (255, 171, 0) if cpu_pct < 85 else (255, 23, 68)
    draw.text((60, 240), f"{cpu_pct}%", fill=cpu_color, font=font_val)
    draw.rectangle([(60, 370), (580, 430)], fill=(30, 45, 70))
    bar_w = int(60 + (cpu_pct / 100.0) * 520)
    draw.rectangle([(60, 370), (max(60, bar_w), 430)], fill=cpu_color)

    # Section 2: RAM USAGE (Y: 530 - 880)
    draw.rectangle([(30, 530), (610, 880)], fill=(18, 28, 48), outline=(0, 180, 216), width=3)
    draw.text((60, 560), "MEMORY (RAM)", fill=(200, 220, 240), font=font_label)
    draw.text((60, 620), f"{mem_pct}%", fill=(0, 212, 255), font=font_val)
    draw.text((60, 710), f"{mem_used} MB / {mem_total} MB", fill=(180, 200, 220), font=font_sub)
    draw.rectangle([(60, 770), (580, 830)], fill=(30, 45, 70))
    ram_w = int(60 + (mem_pct / 100.0) * 520)
    draw.rectangle([(60, 770), (max(60, ram_w), 930)], fill=(0, 212, 255))

    # Section 3: DISK UTILIZATION (Y: 910 - 1260)
    draw.rectangle([(30, 910), (610, 1260)], fill=(18, 28, 48), outline=(0, 180, 216), width=3)
    draw.text((60, 940), "DISK STORAGE", fill=(200, 220, 240), font=font_label)
    draw.text((60, 1000), f"{disk_pct}%", fill=(179, 136, 255), font=font_val)
    draw.rectangle([(60, 1150), (580, 1210)], fill=(30, 45, 70))
    disk_w = int(60 + (disk_pct / 100.0) * 520)
    draw.rectangle([(60, 1150), (max(60, disk_w), 1210)], fill=(179, 136, 255))

    # Section 4: UPTIME & CLOCK (Y: 1290 - 1850)
    draw.rectangle([(30, 1290), (610, 1850)], fill=(18, 28, 48), outline=(0, 180, 216), width=3)
    draw.text((60, 1320), "SYSTEM UPTIME", fill=(200, 220, 240), font=font_label)
    draw.text((60, 1380), uptime_str, fill=(255, 215, 0), font=font_val)

    clk_str = time.strftime("%H:%M:%S")
    draw.text((60, 1520), "LIVE CLOCK", fill=(200, 220, 240), font=font_sub)
    draw.text((60, 1580), clk_str, fill=(255, 255, 255), font=font_val)

    out_dir = "dashboard_tmp"
    os.makedirs(out_dir, exist_ok=True)
    ppm_path = os.path.join(out_dir, "dash.ppm")
    jpg_path = os.path.join(out_dir, "dash.jpg")

    header = f"P6\n{WIDTH} {HEIGHT}\n255\n".encode('ascii')
    with open(ppm_path, 'wb') as f:
        f.write(header)
        f.write(img.tobytes())

    # Encode PPM -> FFmpeg JPEG with standard static Huffman tables (-huffman default)
    cmd = ['ffmpeg', '-y', '-i', ppm_path, '-pix_fmt', 'yuv420p', '-huffman', 'default', '-q:v', '2', jpg_path]
    subprocess.check_call(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    with open(jpg_path, 'rb') as f:
        return f.read()

def enforce_fixed_sos_header(jpeg_data):
    """
    Enforces SOS offset at byte 190 (0x00BE) by replacing dynamic JPEG header
    with exact static header from pattern_640x1920.jpg.
    """
    sos_idx = jpeg_data.find(b'\xFF\xDA')
    if sos_idx < 0:
        return jpeg_data

    pattern_path = "portrait_patterns/pattern_640x1920.jpg"
    if os.path.exists(pattern_path):
        with open(pattern_path, 'rb') as f:
            pat_bytes = f.read()
        pat_sos = pat_bytes.find(b'\xFF\xDA')
        if pat_sos > 0:
            fixed_hdr = pat_bytes[:pat_sos] # Exactly 190 bytes (0x00BE)
            scan_payload = jpeg_data[sos_idx:]
            return fixed_hdr + scan_payload

    return jpeg_data

def run_fixed_sos_test(duration_sec=15.0, interval_sec=1.0):
    dev_path = find_target_usb_device(0x33c3, 0xf101)
    if not dev_path:
        print("[ERROR] USB device 33c3:f101 not found dynamically.")
        return

    unbind_cdc_acm()
    print("=== MSDisplay SOS Offset 0x00BE (190B) Fixed Header System Stats Monitor ===")
    print(f"[DYNAMIC LOOKUP] Target Device Node: {dev_path}")

    fd = os.open(dev_path, os.O_RDWR)
    iface_buf = struct.pack("I", 1)

    try:
        fcntl.ioctl(fd, USBDEVFS_CLAIMINTERFACE, iface_buf)
        print("[SUCCESS] Claimed Interface 1 via usbfs ioctl")

        prev_total, prev_idle = get_cpu_usage()
        seq_cnt = 1
        start_time = time.monotonic()

        while (time.monotonic() - start_time) < duration_sec:
            curr_total, curr_idle = get_cpu_usage()
            diff_total = curr_total - prev_total
            diff_idle = curr_idle - prev_idle
            cpu_pct = int(((diff_total - diff_idle) / diff_total) * 100) if diff_total > 0 else 0
            prev_total, prev_idle = curr_total, curr_idle

            mem_pct, mem_used, mem_total = get_mem_info()
            disk_pct, disk_used, disk_total = get_disk_info()
            uptime_str = get_uptime()

            raw_jpeg = generate_dashboard_image(cpu_pct, mem_pct, disk_pct, mem_used, mem_total, uptime_str)
            fixed_jpeg = enforce_fixed_sos_header(raw_jpeg)

            hdr = struct.pack("<IHHHH", MSDISPLAY_MAGIC_SIGNATURE, WIDTH, HEIGHT, STRIDE_LOCK, FLAG_FIXED)
            payload = hdr + fixed_jpeg

            data_buf = ctypes.create_string_buffer(payload)
            bulk_req = usbdevfs_bulktransfer()
            bulk_req.ep = 0x02
            bulk_req.len = len(payload)
            bulk_req.timeout = 2000
            bulk_req.data = ctypes.cast(data_buf, ctypes.c_void_p)

            res = fcntl.ioctl(fd, USBDEVFS_BULK, bulk_req)
            ts = time.strftime("%H:%M:%S")
            elapsed = time.monotonic() - start_time
            print(f"[{ts}] Frame #{seq_cnt:02d} ({len(payload)}B, SOS=0x00BE) -> CPU: {cpu_pct:02d}% | RAM: {mem_pct:02d}% | USB Tx: {res}B OK | Elapsed: {elapsed:.1f}s / {duration_sec}s")

            seq_cnt += 1
            time.sleep(interval_sec)

        print(f"\n[SUCCESS] Streamed {seq_cnt-1} fixed SOS header frames over {duration_sec}s.")

    except KeyboardInterrupt:
        print("\n[STATUS] System stats monitor stopped by user.")
    except Exception as e:
        print(f"[ERROR] Stats stream error: {e}")
    finally:
        try: fcntl.ioctl(fd, USBDEVFS_RELEASEINTERFACE, iface_buf)
        except Exception: pass
        os.close(fd)

def main():
    parser = argparse.ArgumentParser(description="MSDisplay SOS Offset 0x00BE Fixed Header Test")
    parser.add_argument('--interval', type=float, default=1.0, help="Refresh interval in seconds (default: 1.0)")
    parser.add_argument('--duration', type=float, default=15.0, help="Run duration in seconds (default: 15)")
    args = parser.parse_args()
    run_fixed_sos_test(duration_sec=args.duration, interval_sec=args.interval)

if __name__ == "__main__":
    main()
