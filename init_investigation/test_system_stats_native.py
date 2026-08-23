import os
import sys
import time
import struct
import fcntl
import ctypes
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

def create_system_stats_image(cpu=25, ram=42, temp=48):
    # 640x1920 portrait
    img = Image.new('RGB', (640, 1920), (10, 15, 25))
    draw = ImageDraw.Draw(img)
    
    # Outer border
    draw.rectangle([10, 10, 630, 1910], outline=(0, 200, 255), width=4)
    
    try:
        font_lg = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 48)
        font_md = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 36)
        font_sm = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 28)
    except Exception:
        font_lg = font_md = font_sm = ImageFont.load_default()
        
    # Title Box
    draw.rectangle([30, 30, 610, 130], fill=(0, 100, 160))
    draw.text((60, 55), "SYSTEM MONITOR", fill=(255, 255, 255), font=font_lg)
    
    # Panel 1: CPU
    draw.rectangle([30, 160, 610, 560], fill=(20, 35, 55), outline=(0, 180, 255), width=3)
    draw.text((60, 190), "CPU UTILIZATION", fill=(0, 200, 255), font=font_md)
    draw.text((60, 260), f"{cpu:.1f} %", fill=(255, 255, 255), font=font_lg)
    # Progress Bar
    draw.rectangle([60, 370, 580, 430], fill=(10, 50, 80))
    w_cpu = int((580 - 60) * (cpu / 100.0))
    draw.rectangle([60, 370, 60 + w_cpu, 430], fill=(0, 200, 255))
    
    # Panel 2: RAM
    draw.rectangle([30, 600, 610, 1000], fill=(20, 55, 35), outline=(0, 255, 120), width=3)
    draw.text((60, 630), "RAM MEMORY", fill=(0, 255, 120), font=font_md)
    used_gb = 32.0 * (ram / 100.0)
    draw.text((60, 700), f"{used_gb:.1f} GB / 32.0 GB", fill=(255, 255, 255), font=font_lg)
    # Progress Bar
    draw.rectangle([60, 810, 580, 870], fill=(10, 80, 40))
    w_ram = int((580 - 60) * (ram / 100.0))
    draw.rectangle([60, 810, 60 + w_ram, 870], fill=(0, 255, 120))
    
    # Panel 3: GPU Temp
    draw.rectangle([30, 1040, 610, 1440], fill=(55, 35, 20), outline=(255, 160, 0), width=3)
    draw.text((60, 1070), "GPU TEMPERATURE", fill=(255, 160, 0), font=font_md)
    draw.text((60, 1140), f"{temp} °C", fill=(255, 255, 255), font=font_lg)
    # Progress Bar
    draw.rectangle([60, 1250, 580, 1310], fill=(80, 40, 10))
    w_temp = int((580 - 60) * (temp / 100.0))
    draw.rectangle([60, 1250, 60 + w_temp, 1310], fill=(255, 160, 0))
    
    # Panel 4: System Info
    draw.rectangle([30, 1480, 610, 1880], fill=(45, 20, 55), outline=(220, 100, 255), width=3)
    draw.text((60, 1510), "VMAX STATUS", fill=(220, 100, 255), font=font_md)
    draw.text((60, 1590), "DRIVER: LINUX NATIVE", fill=(255, 255, 255), font=font_sm)
    draw.text((60, 1660), "TRANSPORT: USB FS EP02", fill=(255, 255, 255), font=font_sm)
    draw.text((60, 1730), "STATUS: 100% PERFECT", fill=(0, 255, 120), font=font_sm)
    
    return img

def main():
    dev_path = find_device()
    if not dev_path:
        print("Device not found")
        sys.exit(1)
        
    unbind_cdc_acm()
    
    img = create_system_stats_image(28.4, 41.2, 49)
    out_jpg = "/tmp/system_stats_native.jpg"
    # Save with low entropy compression matching baseline pattern
    img.save(out_jpg, format="JPEG", quality=75, subsampling=0, optimize=True)
    
    with open(out_jpg, 'rb') as f:
        jpeg_bytes = f.read()
        
    print(f"Streaming native 640x1920 system stats frame ({len(jpeg_bytes)} B)...")
    
    fd = os.open(dev_path, os.O_RDWR)
    try:
        fcntl.ioctl(fd, USBDEVFS_CLAIMINTERFACE, struct.pack('I', 1))
        
        for i in range(10):
            res = send_frame(fd, jpeg_bytes)
            print(f"  Frame {i+1:02d} sent: OK")
            time.sleep(1.0)
            
        fcntl.ioctl(fd, USBDEVFS_RELEASEINTERFACE, struct.pack('I', 1))
    finally:
        os.close(fd)

if __name__ == "__main__":
    main()
