import os
import sys
import time
import struct
import fcntl
import ctypes
import subprocess
from PIL import Image, ImageDraw, ImageFont

USBDEVFS_CLAIMINTERFACE = 0x8004550F
USBDEVFS_RELEASEINTERFACE = 0x80045510
USBDEVFS_BULK = 0xC0185502

WIDTH = 640
HEIGHT = 1920
MSDISPLAY_MAGIC_SIGNATURE = 0x0008100A

def find_device():
    import glob
    for dev in sorted(glob.glob('/dev/bus/usb/*/*')):
        try:
            with open(dev, 'rb') as f:
                data = f.read(18)
                if len(data) == 18:
                    vid, pid = struct.unpack('<HH', data[8:12])
                    if vid == 0x33c3 and pid == 0xf101:
                        return dev
        except Exception:
            pass
    return None

def unbind_cdc_acm():
    try:
        if os.path.exists('/sys/bus/usb/drivers/cdc_acm/1-9:1.1'):
            with open('/sys/bus/usb/drivers/cdc_acm/unbind', 'w') as f:
                f.write('1-9:1.1\n')
    except Exception:
        pass

def send_frame(fd, jpeg_bytes):
    header = struct.pack("<IHHHH", MSDISPLAY_MAGIC_SIGNATURE, WIDTH, HEIGHT, 0, 1)
    payload = header + jpeg_bytes
    
    data_buf = ctypes.create_string_buffer(payload)
    bulk_req = struct.pack('IIIIPI', 0x02, len(payload), 2000, 0, ctypes.addressof(data_buf), 0)
    return fcntl.ioctl(fd, USBDEVFS_BULK, bulk_req)

def create_15k_dashboard_jpeg(cpu_val=25, ram_val=40):
    ppm_path = "/tmp/dash_15k.ppm"
    jpg_path = "/tmp/dash_15k.jpg"
    
    # 640x1920 portrait
    img = Image.new('RGB', (WIDTH, HEIGHT), (10, 18, 32))
    draw = ImageDraw.Draw(img)
    
    # Border
    draw.rectangle([10, 10, 630, 1910], outline=(0, 200, 255), width=4)
    
    # 4 High-contrast solid telemetry cards
    # Card 1: CPU
    draw.rectangle([30, 40, 610, 440], fill=(20, 35, 60), outline=(0, 200, 255), width=3)
    draw.rectangle([50, 60, 590, 120], fill=(0, 150, 220))
    # CPU Progress Bar
    draw.rectangle([60, 240, 580, 320], fill=(10, 50, 80))
    w_cpu = int((580 - 60) * (cpu_val / 100.0))
    draw.rectangle([60, 240, 60 + w_cpu, 320], fill=(0, 220, 120))
    
    # Card 2: RAM
    draw.rectangle([30, 480, 610, 880], fill=(20, 60, 40), outline=(0, 255, 120), width=3)
    draw.rectangle([50, 500, 590, 560], fill=(0, 180, 90))
    # RAM Progress Bar
    draw.rectangle([60, 680, 580, 760], fill=(10, 70, 35))
    w_ram = int((580 - 60) * (ram_val / 100.0))
    draw.rectangle([60, 680, 60 + w_ram, 760], fill=(0, 255, 120))
    
    # Card 3: DISK
    draw.rectangle([30, 920, 610, 1320], fill=(60, 40, 20), outline=(255, 160, 0), width=3)
    draw.rectangle([50, 940, 590, 1000], fill=(220, 140, 0))
    draw.rectangle([60, 1120, 580, 1200], fill=(70, 45, 10))
    draw.rectangle([60, 1120, 380, 1200], fill=(255, 180, 0))
    
    # Card 4: UPTIME
    draw.rectangle([30, 1360, 610, 1860], fill=(50, 20, 60), outline=(220, 100, 255), width=3)
    draw.rectangle([50, 1380, 590, 1440], fill=(200, 50, 180))
    draw.rectangle([60, 1560, 580, 1640], fill=(60, 20, 70))
    draw.rectangle([60, 1560, 440, 1640], fill=(220, 100, 255))
    
    header = f"P6\n{WIDTH} {HEIGHT}\n255\n".encode('ascii')
    with open(ppm_path, 'wb') as f:
        f.write(header)
        f.write(img.tobytes())
        
    cmd = ['ffmpeg', '-y', '-i', ppm_path, '-q:v', '2', jpg_path]
    subprocess.check_call(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    with open(jpg_path, 'rb') as f:
        return f.read()

def main():
    dev_path = find_device()
    if not dev_path:
        print("[ERROR] Device 33c3:f101 not found.")
        sys.exit(1)
        
    unbind_cdc_acm()
    jpeg_bytes = create_15k_dashboard_jpeg(45, 68)
    print(f"=== Testing 15KB Baseline Dashboard Frame (JPEG size: {len(jpeg_bytes)} B) ===")
    
    fd = os.open(dev_path, os.O_RDWR)
    try:
        fcntl.ioctl(fd, USBDEVFS_CLAIMINTERFACE, struct.pack('I', 1))
        for i in range(5):
            res = send_frame(fd, jpeg_bytes)
            print(f"  Frame #{i+1:02d} sent OK ({len(jpeg_bytes)} B payload)")
            time.sleep(1.0)
        fcntl.ioctl(fd, USBDEVFS_RELEASEINTERFACE, struct.pack('I', 1))
    finally:
        os.close(fd)

if __name__ == "__main__":
    main()
