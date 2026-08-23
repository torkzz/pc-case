import os
import sys
import time
import struct
import fcntl
import ctypes
import subprocess
from PIL import Image, ImageDraw

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

def generate_full_width_stripes_jpeg():
    ppm_path = "/tmp/stripes_full.ppm"
    jpg_path = "/tmp/stripes_full.jpg"
    
    img = Image.new('RGB', (WIDTH, HEIGHT), (0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Card 1: CPU (Red/Yellow horizontal bands, 0 to 480)
    draw.rectangle([0, 0, WIDTH, 120], fill=(200, 30, 30))
    draw.rectangle([0, 120, WIDTH, 240], fill=(20, 20, 40))
    draw.rectangle([0, 240, WIDTH, 360], fill=(0, 220, 120))
    draw.rectangle([0, 360, WIDTH, 480], fill=(20, 20, 40))
    
    # Card 2: RAM (Green/Blue horizontal bands, 480 to 960)
    draw.rectangle([0, 480, WIDTH, 600], fill=(30, 180, 60))
    draw.rectangle([0, 600, WIDTH, 720], fill=(20, 20, 40))
    draw.rectangle([0, 720, WIDTH, 840], fill=(0, 200, 255))
    draw.rectangle([0, 840, WIDTH, 960], fill=(20, 20, 40))
    
    # Card 3: DISK (Orange/Yellow horizontal bands, 960 to 1440)
    draw.rectangle([0, 960, WIDTH, 1080], fill=(220, 140, 0))
    draw.rectangle([0, 1080, WIDTH, 1200], fill=(20, 20, 40))
    draw.rectangle([0, 1200, WIDTH, 1320], fill=(255, 200, 0))
    draw.rectangle([0, 1320, WIDTH, 1440], fill=(20, 20, 40))
    
    # Card 4: UPTIME (Purple/White horizontal bands, 1440 to 1920)
    draw.rectangle([0, 1440, WIDTH, 1560], fill=(180, 40, 200))
    draw.rectangle([0, 1560, WIDTH, 1680], fill=(20, 20, 40))
    draw.rectangle([0, 1680, WIDTH, 1800], fill=(255, 255, 255))
    draw.rectangle([0, 1800, WIDTH, 1920], fill=(20, 20, 40))
    
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
    jpeg_bytes = generate_full_width_stripes_jpeg()
    print(f"=== Testing Full-Width Horizontal Stripes (JPEG size: {len(jpeg_bytes)} B) ===")
    
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
