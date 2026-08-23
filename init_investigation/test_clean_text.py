import os
import sys
import time
import struct
import fcntl
import ctypes
import argparse
from PIL import Image, ImageDraw, ImageFont

USBDEVFS_CLAIMINTERFACE = 0x8004550F
USBDEVFS_RELEASEINTERFACE = 0x80045510
USBDEVFS_BULK = 0xC0185502

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
    header = struct.pack("<IHHHH", 0x0008100A, 640, 1920, 0, 1)
    payload = header + jpeg_bytes
    
    buf = (ctypes.c_char * len(payload)).from_buffer_copy(payload)
    bulk_req = struct.pack('IIIIPI', 0x02, len(payload), 5000, 0, ctypes.addressof(buf), 0)
    return fcntl.ioctl(fd, USBDEVFS_BULK, bulk_req)

def create_text_card(text="HELLO WORLD"):
    img = Image.new('RGB', (640, 1920), (12, 20, 35))
    draw = ImageDraw.Draw(img)
    
    # Outer frame
    draw.rectangle([15, 15, 625, 1905], outline=(0, 220, 255), width=4)
    
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
    draw.text((60, 530), "HARDWARE DECODER", fill=(0, 255, 120), font=font_md)
    draw.text((60, 650), "STATUS: OK", fill=(255, 255, 255), font=font_lg)
    
    # Card 3: Details
    draw.rectangle([35, 940, 605, 1350], fill=(60, 40, 20), outline=(255, 160, 0), width=3)
    draw.text((60, 980), "MCU TILING", fill=(255, 160, 0), font=font_md)
    draw.text((60, 1100), "8x8 MCU YUV444", fill=(255, 255, 255), font=font_lg)
    
    # Card 4: Footer
    draw.rectangle([35, 1390, 605, 1840], fill=(50, 20, 60), outline=(220, 100, 255), width=3)
    draw.text((60, 1430), "VMAX LINUX NATIVE", fill=(220, 100, 255), font=font_md)
    draw.text((60, 1550), "640 x 1920", fill=(255, 255, 255), font=font_lg)
    
    return img

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--text', type=str, default="HELLO WORLD")
    parser.add_argument('--duration', type=float, default=5.0)
    parser.add_argument('--subsampling', type=int, default=0)
    parser.add_argument('--quality', type=int, default=75)
    args = parser.parse_args()
    
    dev_path = find_device()
    if not dev_path:
        print("Device not found")
        sys.exit(1)
        
    unbind_cdc_acm()
    
    img = create_text_card(args.text)
    out_jpg = "/tmp/clean_text.jpg"
    img.save(out_jpg, format="JPEG", quality=args.quality, subsampling=args.subsampling, optimize=True)
    
    with open(out_jpg, 'rb') as f:
        jpeg_bytes = f.read()
        
    print(f"=== Clean Text Test: '{args.text}' ({len(jpeg_bytes)} B JPEG) ===")
    
    fd = os.open(dev_path, os.O_RDWR)
    try:
        fcntl.ioctl(fd, USBDEVFS_CLAIMINTERFACE, struct.pack('I', 1))
        
        start = time.monotonic()
        frame_idx = 1
        while (time.monotonic() - start) < args.duration:
            send_frame(fd, jpeg_bytes)
            print(f"  Frame #{frame_idx:02d} sent: OK")
            frame_idx += 1
            time.sleep(1.0)
            
        fcntl.ioctl(fd, USBDEVFS_RELEASEINTERFACE, struct.pack('I', 1))
    finally:
        os.close(fd)

if __name__ == "__main__":
    main()
