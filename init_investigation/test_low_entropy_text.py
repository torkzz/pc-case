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

def generate_low_entropy_dashboard_jpeg(cpu_val=25, ram_val=40):
    ppm_path = "/tmp/low_entropy.ppm"
    jpg_path = "/tmp/low_entropy.jpg"
    
    img = Image.new('RGB', (WIDTH, HEIGHT), (10, 20, 40))
    draw = ImageDraw.Draw(img)
    
    # 4 distinct solid color section cards (matching pattern_640x1920 geometry)
    # Card 1: Top (Red/Dark Blue)
    draw.rectangle([0, 0, WIDTH, 480], fill=(20, 40, 80))
    draw.rectangle([30, 30, 610, 110], fill=(0, 150, 220))
    draw.rectangle([40, 220, 600, 320], fill=(0, 200, 120))
    
    # Card 2: Upper Mid (Green)
    draw.rectangle([0, 480, WIDTH, 960], fill=(15, 60, 30))
    draw.rectangle([30, 510, 610, 590], fill=(0, 180, 90))
    draw.rectangle([40, 700, 600, 800], fill=(0, 220, 255))
    
    # Card 3: Lower Mid (Blue)
    draw.rectangle([0, 960, WIDTH, 1440], fill=(60, 40, 15))
    draw.rectangle([30, 990, 610, 1070], fill=(220, 140, 0))
    draw.rectangle([40, 1180, 600, 1280], fill=(255, 200, 0))
    
    # Card 4: Bottom (White/Purple)
    draw.rectangle([0, 1440, WIDTH, 1920], fill=(50, 15, 60))
    draw.rectangle([30, 1470, 610, 1550], fill=(200, 50, 180))
    draw.rectangle([40, 1660, 600, 1760], fill=(255, 100, 220))
    
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
    jpeg_bytes = generate_low_entropy_dashboard_jpeg(35, 62)
    print(f"=== Testing Low-Entropy Dashboard Cards (JPEG size: {len(jpeg_bytes)} B) ===")
    
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
