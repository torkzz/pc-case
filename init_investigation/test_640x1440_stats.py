#!/usr/bin/env python3
"""
640x1440 Native Physical Resolution System Stats Driver (`test_640x1440_stats.py`)

Physical Height Calculation:
- 3 bands of 480px (Red 0-480, Green 480-960, Blue 960-1440) filled 100% of physical screen height.
- True native panel height = 1440 pixels (640 x 1440).
- 4 dashboard sections (CPU, RAM, DISK, UPTIME/CLOCK) sized to 320px each fit 100% inside 1440px canvas.
"""

import sys
import os
import time
import struct
import fcntl
import ctypes
import subprocess
import io
import argparse
from PIL import Image, ImageDraw, ImageFont

WIDTH = 640
HEIGHT = 1440
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

def generate_1440_dashboard_image(cpu_pct, mem_pct, disk_pct, mem_used, mem_total, uptime_str):
    img = Image.new('RGB', (WIDTH, HEIGHT), color=(10, 18, 32))
    draw = ImageDraw.Draw(img)

    try:
        font_title = ImageFont.truetype("/usr/share/fonts/TTF/DejaVuSans-Bold.ttf", 34)
        font_val   = ImageFont.truetype("/usr/share/fonts/TTF/DejaVuSans-Bold.ttf", 40)
        font_label = ImageFont.truetype("/usr/share/fonts/TTF/DejaVuSans-Bold.ttf", 24)
        font_sub   = ImageFont.truetype("/usr/share/fonts/TTF/DejaVuSans-Bold.ttf", 20)
    except Exception:
        font_title = font_val = font_label = font_sub = ImageFont.load_default()

    # Top Header Banner (Y: 0..90)
    draw.rectangle([(0, 0), (WIDTH, 90)], fill=(0, 150, 214))
    draw.text((30, 25), "VMAX SYSTEM MONITOR", fill=(255, 255, 255), font=font_title)

    # Card 1: CPU LOAD (Y: 100 - 410) -> Cyan Border
    draw.rectangle([(20, 100), (620, 410)], fill=(18, 28, 48), outline=(0, 180, 216), width=3)
    draw.text((45, 120), "CPU USAGE", fill=(200, 220, 240), font=font_label)
    cpu_color = (0, 230, 118) if cpu_pct < 70 else (255, 171, 0) if cpu_pct < 85 else (255, 23, 68)
    draw.text((45, 170), f"{cpu_pct}%", fill=cpu_color, font=font_val)
    draw.rectangle([(45, 270), (595, 330)], fill=(30, 45, 70))
    bar_w = int(45 + (cpu_pct / 100.0) * 550)
    draw.rectangle([(45, 270), (max(45, bar_w), 330)], fill=cpu_color)
    draw.text((45, 360), "PROCESSOR TELEMETRY", fill=(180, 200, 220), font=font_sub)

    # Card 2: MEMORY RAM (Y: 430 - 740) -> Green Border
    draw.rectangle([(20, 430), (620, 740)], fill=(18, 28, 48), outline=(0, 230, 118), width=3)
    draw.text((45, 450), "MEMORY (RAM)", fill=(200, 220, 240), font=font_label)
    draw.text((45, 500), f"{mem_pct}%", fill=(0, 212, 255), font=font_val)
    draw.text((45, 580), f"{mem_used} MB / {mem_total} MB", fill=(180, 200, 220), font=font_sub)
    draw.rectangle([(45, 620), (595, 680)], fill=(30, 45, 70))
    ram_w = int(45 + (mem_pct / 100.0) * 550)
    draw.rectangle([(45, 620), (max(45, ram_w), 680)], fill=(0, 212, 255))

    # Card 3: DISK STORAGE (Y: 760 - 1070) -> Yellow Border
    draw.rectangle([(20, 760), (620, 1070)], fill=(18, 28, 48), outline=(255, 214, 10), width=3)
    draw.text((45, 780), "DISK STORAGE", fill=(200, 220, 240), font=font_label)
    draw.text((45, 830), f"{disk_pct}%", fill=(179, 136, 255), font=font_val)
    draw.rectangle([(45, 950), (595, 1010)], fill=(30, 45, 70))
    disk_w = int(45 + (disk_pct / 100.0) * 550)
    draw.rectangle([(45, 950), (max(45, disk_w), 1010)], fill=(179, 136, 255))

    # Card 4: UPTIME & CLOCK (Y: 1090 - 1400) -> Magenta Border
    draw.rectangle([(20, 1090), (620, 1400)], fill=(18, 28, 48), outline=(247, 37, 133), width=3)
    draw.text((45, 1110), "SYSTEM UPTIME", fill=(200, 220, 240), font=font_label)
    draw.text((45, 1160), uptime_str, fill=(255, 215, 0), font=font_val)

    clk_str = time.strftime("%H:%M:%S")
    draw.text((45, 1260), "LIVE CLOCK", fill=(200, 220, 240), font=font_sub)
    draw.text((45, 1310), clk_str, fill=(255, 255, 255), font=font_val)

    out_dir = "dashboard_tmp"
    os.makedirs(out_dir, exist_ok=True)
    ppm_path = os.path.join(out_dir, "dash1440.ppm")
    jpg_path = os.path.join(out_dir, "dash1440.jpg")

    header = f"P6\n{WIDTH} {HEIGHT}\n255\n".encode('ascii')
    with open(ppm_path, 'wb') as f:
        f.write(header)
        f.write(img.tobytes())

    cmd = ['ffmpeg', '-y', '-i', ppm_path, '-vf', 'scale=640:1440', '-q:v', '2', jpg_path]
    subprocess.check_call(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    with open(jpg_path, 'rb') as f:
        return f.read()

def render_dashboard_frame(cpu_pct, mem_pct, disk_pct, mem_used, mem_total, uptime, seq_cnt):
    jpeg_bytes = generate_1440_dashboard_image(cpu_pct, mem_pct, disk_pct, mem_used, mem_total, uptime)
    # Header 640x1440 (W=640 0x0280, H=1440 0x05A0)
    hdr = struct.pack("<IHHHH", MSDISPLAY_MAGIC_SIGNATURE, WIDTH, HEIGHT, STRIDE_LOCK, FLAG_FIXED)
    return hdr + jpeg_bytes

def start_stats_daemon(duration_sec=15.0, interval_sec=1.0):
    dev_path = find_target_usb_device(0x33c3, 0xf101)
    if not dev_path:
        print("[ERROR] USB device 33c3:f101 not found dynamically.")
        return

    unbind_cdc_acm()
    print("=== MSDisplay 640x1440 Native Height System Stats Monitor ===")
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

            payload = render_dashboard_frame(cpu_pct, mem_pct, disk_pct, mem_used, mem_total, uptime_str, seq_cnt)

            data_buf = ctypes.create_string_buffer(payload)
            bulk_req = usbdevfs_bulktransfer()
            bulk_req.ep = 0x02
            bulk_req.len = len(payload)
            bulk_req.timeout = 2000
            bulk_req.data = ctypes.cast(data_buf, ctypes.c_void_p)

            res = fcntl.ioctl(fd, USBDEVFS_BULK, bulk_req)
            ts = time.strftime("%H:%M:%S")
            elapsed = time.monotonic() - start_time
            print(f"[{ts}] Frame #{seq_cnt:02d} ({len(payload)}B, 640x1440) -> CPU: {cpu_pct:02d}% | RAM: {mem_pct:02d}% | USB Tx: {res}B OK | Elapsed: {elapsed:.1f}s / {duration_sec}s")

            seq_cnt += 1
            time.sleep(interval_sec)

        print(f"\n[SUCCESS] Streamed {seq_cnt-1} 640x1440 native dashboard frames over {duration_sec}s.")

    except KeyboardInterrupt:
        print("\n[STATUS] System stats monitor stopped by user.")
    except Exception as e:
        print(f"[ERROR] Stats stream error: {e}")
    finally:
        try: fcntl.ioctl(fd, USBDEVFS_RELEASEINTERFACE, iface_buf)
        except Exception: pass
        os.close(fd)

def main():
    parser = argparse.ArgumentParser(description="MSDisplay 640x1440 Native Linux System Stats Monitor")
    parser.add_argument('--interval', type=float, default=1.0, help="Refresh interval in seconds (default: 1.0)")
    parser.add_argument('--duration', type=float, default=15.0, help="Run duration in seconds (default: 15)")
    args = parser.parse_args()
    start_stats_daemon(duration_sec=args.duration, interval_sec=args.interval)

if __name__ == "__main__":
    main()
