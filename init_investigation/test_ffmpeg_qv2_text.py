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

def generate_ffmpeg_qv2_frame(text="HELLO WORLD"):
    ppm_path = "/tmp/qv2_text.ppm"
    jpg_path = "/tmp/qv2_text.jpg"
    
    img = Image.new('RGB', (WIDTH, HEIGHT), (10, 18, 32))
    draw = ImageDraw.Draw(img)
    
    draw.rectangle([10, 10, 630, 1910], outline=(0, 200, 255), width=4)
    
    try:
        font_lg = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 52)
        font_md = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 38)
    except Exception:
        font_lg = font_md = ImageFont.load_default()
        
    # Card 1: Main Text Banner
    draw.rectangle([35, 40, 605, 450], fill=(20, 35, 60), outline=(0, 200, 255), width=3)
    draw.text((60, 80), "TEXT TEST", fill=(0, 200, 255), font=font_md)
    draw.text((60, 200), text, fill=(255, 255, 255), font=font_lg)
    
    # Card 2: Status
    draw.rectangle([35, 490, 605, 900], fill=(20, 60, 40), outline=(0, 255, 120), width=3)
    draw.text((60, 530), "HARDWARE PIPELINE", fill=(0, 255, 120), font=font_md)
    draw.text((60, 650), "FFMPEG QV2 ENCODER", fill=(255, 255, 255), font=font_lg)
    
    # Card 3: Details
    draw.rectangle([35, 940, 605, 1350], fill=(60, 40, 20), outline=(255, 160, 0), width=3)
    draw.text((60, 980), "RESOLUTION", fill=(255, 160, 0), font=font_md)
    draw.text((60, 1100), "640 x 1920 PORTRAIT", fill=(255, 255, 255), font=font_lg)
    
    # Card 4: Footer
    draw.rectangle([35, 1390, 605, 1840], fill=(50, 20, 60), outline=(220, 100, 255), width=3)
    draw.text((60, 1430), "VMAX LINUX NATIVE", fill=(220, 100, 255), font=font_md)
    draw.text((60, 1550), "STATUS: OK", fill=(255, 255, 255), font=font_lg)
    
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
    jpeg_bytes = generate_ffmpeg_qv2_frame("HELLO WORLD")
    print(f"=== FFmpeg -q:v 2 Text Frame Test ({len(jpeg_bytes)} B JPEG) ===")
    
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
