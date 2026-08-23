#!/usr/bin/env python3
"""
1920-Wide Landscape System Monitor Driver (`test_1920_landscape_dashboard.py`)

Hardware Discovery:
- The LCD controller hardware scalar expects a LANDSCAPE JPEG (1920x1080 or 1920x640).
- Sending a 640-wide portrait JPEG causes the 1920-line scanout engine to tile the 640px image 3 times (3 boxes).
- Rendering the dashboard onto a 1920x640 landscape canvas (Header W=1920, H=640) eliminates 3-box / 2-box tiling 100%!
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

WIDTH = 1920
HEIGHT = 640
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

def generate_landscape_dashboard_image(cpu_pct, mem_pct, disk_pct, mem_used, mem_total, uptime_str):
    img = Image.new('RGB', (WIDTH, HEIGHT), color=(10, 18, 32))
    draw = ImageDraw.Draw(img)

    try:
        font_title = ImageFont.truetype("/usr/share/fonts/TTF/DejaVuSans-Bold.ttf", 48)
        font_val   = ImageFont.truetype("/usr/share/fonts/TTF/DejaVuSans-Bold.ttf", 52)
        font_label = ImageFont.truetype("/usr/share/fonts/TTF/DejaVuSans-Bold.ttf", 32)
        font_sub   = ImageFont.truetype("/usr/share/fonts/TTF/DejaVuSans-Bold.ttf", 26)
    except Exception:
        font_title = font_val = font_label = font_sub = ImageFont.load_default()

    # Top Banner across full 1920 width
    draw.rectangle([(0, 0), (WIDTH, 110)], fill=(0, 150, 214))
    draw.text((60, 30), "VMAX SYSTEM MONITOR (1920-WIDE SINGLE SCANOUT)", fill=(255, 255, 255), font=font_title)

    # 4 Side-by-Side Cards (Width 440 each)
    card_w = 440
    gap = 30

    # Card 1: CPU (X: 30..470)
    c1_x = 30
    draw.rectangle([(c1_x, 140), (c1_x + card_w, 610)], fill=(18, 28, 48), outline=(0, 180, 216), width=4)
    draw.rectangle([(c1_x, 140), (c1_x + card_w, 210)], fill=(0, 150, 214))
    draw.text((c1_x + 30, 155), "CPU USAGE", fill=(255, 255, 255), font=font_label)
    cpu_color = (0, 230, 118) if cpu_pct < 70 else (255, 171, 0) if cpu_pct < 85 else (255, 23, 68)
    draw.text((c1_x + 30, 240), f"{cpu_pct}%", fill=cpu_color, font=font_val)
    draw.rectangle([(c1_x + 30, 380), (c1_x + card_w - 30, 440)], fill=(30, 45, 70))
    bar_w = int(c1_x + 30 + (cpu_pct / 100.0) * (card_w - 60))
    draw.rectangle([(c1_x + 30, 380), (max(c1_x + 30, bar_w), 440)], fill=cpu_color)
    draw.text((c1_x + 30, 480), "PROCESSOR", fill=(180, 200, 220), font=font_sub)

    # Card 2: RAM (X: 500..940)
    c2_x = 500
    draw.rectangle([(c2_x, 140), (c2_x + card_w, 610)], fill=(18, 28, 48), outline=(0, 230, 118), width=4)
    draw.rectangle([(c2_x, 140), (c2_x + card_w, 210)], fill=(0, 200, 100))
    draw.text((c2_x + 30, 155), "MEMORY (RAM)", fill=(255, 255, 255), font=font_label)
    draw.text((c2_x + 30, 240), f"{mem_pct}%", fill=(0, 212, 255), font=font_val)
    draw.text((c2_x + 30, 320), f"{mem_used} MB", fill=(180, 200, 220), font=font_sub)
    draw.rectangle([(c2_x + 30, 380), (c2_x + card_w - 30, 440)], fill=(30, 45, 70))
    ram_w = int(c2_x + 30 + (mem_pct / 100.0) * (card_w - 60))
    draw.rectangle([(c2_x + 30, 380), (max(c2_x + 30, ram_w), 440)], fill=(0, 212, 255))
    draw.text((c2_x + 30, 480), f"OF {mem_total} MB", fill=(180, 200, 220), font=font_sub)

    # Card 3: DISK (X: 970..1410)
    c3_x = 970
    draw.rectangle([(c3_x, 140), (c3_x + card_w, 610)], fill=(18, 28, 48), outline=(255, 214, 10), width=4)
    draw.rectangle([(c3_x, 140), (c3_x + card_w, 210)], fill=(230, 180, 0))
    draw.text((c3_x + 30, 155), "DISK STORAGE", fill=(255, 255, 255), font=font_label)
    draw.text((c3_x + 30, 240), f"{disk_pct}%", fill=(179, 136, 255), font=font_val)
    draw.rectangle([(c3_x + 30, 380), (c3_x + card_w - 30, 440)], fill=(30, 45, 70))
    disk_w = int(c3_x + 30 + (disk_pct / 100.0) * (card_w - 60))
    draw.rectangle([(c3_x + 30, 380), (max(c3_x + 30, disk_w), 440)], fill=(179, 136, 255))
    draw.text((c3_x + 30, 480), "STORAGE ROOT", fill=(180, 200, 220), font=font_sub)

    # Card 4: UPTIME/CLOCK (X: 1440..1880)
    c4_x = 1440
    draw.rectangle([(c4_x, 140), (c4_x + card_w, 610)], fill=(18, 28, 48), outline=(247, 37, 133), width=4)
    draw.rectangle([(c4_x, 140), (c4_x + card_w, 210)], fill=(220, 30, 110))
    draw.text((c4_x + 30, 155), "UPTIME & CLOCK", fill=(255, 255, 255), font=font_label)
    draw.text((c4_x + 30, 240), uptime_str, fill=(255, 215, 0), font=font_val)
    clk_str = time.strftime("%H:%M:%S")
    draw.text((c4_x + 30, 350), clk_str, fill=(255, 255, 255), font=font_val)
    draw.text((c4_x + 30, 480), "LIVE CLOCK", fill=(180, 200, 220), font=font_sub)

    out_dir = "dashboard_tmp"
    os.makedirs(out_dir, exist_ok=True)
    ppm_path = os.path.join(out_dir, "landscape_dash.ppm")
    jpg_path = os.path.join(out_dir, "landscape_dash.jpg")

    header = f"P6\n{WIDTH} {HEIGHT}\n255\n".encode('ascii')
    with open(ppm_path, 'wb') as f:
        f.write(header)
        f.write(img.tobytes())

    cmd = ['ffmpeg', '-y', '-i', ppm_path, '-pix_fmt', 'yuv420p', '-q:v', '2', jpg_path]
    subprocess.check_call(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    with open(jpg_path, 'rb') as f:
        return f.read()

def render_dashboard_frame(cpu_pct, mem_pct, disk_pct, mem_used, mem_total, uptime, seq_cnt):
    jpeg_bytes = generate_landscape_dashboard_image(cpu_pct, mem_pct, disk_pct, mem_used, mem_total, uptime)
    hdr = struct.pack("<IHHHH", MSDISPLAY_MAGIC_SIGNATURE, WIDTH, HEIGHT, 1920, 0)
    return hdr + jpeg_bytes

def start_stats_daemon(duration_sec=15.0, interval_sec=1.0):
    dev_path = find_target_usb_device(0x33c3, 0xf101)
    if not dev_path:
        print("[ERROR] USB device 33c3:f101 not found dynamically.")
        return

    unbind_cdc_acm()
    print("=== MSDisplay 1920-Wide Landscape Single Scanout System Stats Monitor ===")
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
            print(f"[{ts}] Frame #{seq_cnt:02d} ({len(payload)}B, 1920x640 Landscape) -> CPU: {cpu_pct:02d}% | RAM: {mem_pct:02d}% | USB Tx: {res}B OK | Elapsed: {elapsed:.1f}s / {duration_sec}s")

            seq_cnt += 1
            time.sleep(interval_sec)

        print(f"\n[SUCCESS] Streamed {seq_cnt-1} 1920-wide landscape dashboard frames over {duration_sec}s.")

    except KeyboardInterrupt:
        print("\n[STATUS] System stats monitor stopped by user.")
    except Exception as e:
        print(f"[ERROR] Stats stream error: {e}")
    finally:
        try: fcntl.ioctl(fd, USBDEVFS_RELEASEINTERFACE, iface_buf)
        except Exception: pass
        os.close(fd)

def main():
    parser = argparse.ArgumentParser(description="MSDisplay 1920-Wide Landscape System Stats Monitor")
    parser.add_argument('--interval', type=float, default=1.0, help="Refresh interval in seconds (default: 1.0)")
    parser.add_argument('--duration', type=float, default=15.0, help="Run duration in seconds (default: 15)")
    args = parser.parse_args()
    start_stats_daemon(duration_sec=args.duration, interval_sec=args.interval)

if __name__ == "__main__":
    main()
