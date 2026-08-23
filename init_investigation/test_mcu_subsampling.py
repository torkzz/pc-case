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
    # MSDisplay Header: Magic=0x0008100A, W=640, H=1920, Stride=0, Flag=1
    header = struct.pack("<IHHHH", 0x0008100A, 640, 1920, 0, 1)
    payload = header + jpeg_bytes
    
    buf = (ctypes.c_char * len(payload)).from_buffer_copy(payload)
    bulk_req = struct.pack('IIIIPI', 0x02, len(payload), 5000, 0, ctypes.addressof(buf), 0)
    return fcntl.ioctl(fd, USBDEVFS_BULK, bulk_req)

def create_dashboard_image(title_text="MCU TEST"):
    img = Image.new('RGB', (640, 1920), (15, 15, 25))
    draw = ImageDraw.Draw(img)
    
    # Border
    draw.rectangle([10, 10, 630, 1910], outline=(0, 220, 255), width=4)
    
    # 4 distinct vertical sections
    draw.rectangle([30, 40, 610, 440], fill=(20, 40, 70), outline=(0, 180, 255), width=3)
    draw.rectangle([30, 480, 610, 880], fill=(20, 70, 40), outline=(0, 255, 120), width=3)
    draw.rectangle([30, 920, 610, 1320], fill=(70, 40, 20), outline=(255, 160, 0), width=3)
    draw.rectangle([30, 1360, 610, 1860], fill=(50, 20, 70), outline=(220, 100, 255), width=3)
    
    try:
        font_title = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 40)
        font_body = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 32)
    except Exception:
        font_title = font_body = ImageFont.load_default()
        
    draw.text((60, 80), title_text, fill=(255, 255, 255), font=font_title)
    draw.text((60, 180), "PANEL: 640x1920", fill=(0, 220, 255), font=font_body)
    
    draw.text((60, 520), "SECTION 2: CPU", fill=(255, 255, 255), font=font_title)
    draw.text((60, 620), "LOAD: 15.2%", fill=(0, 255, 120), font=font_body)
    
    draw.text((60, 960), "SECTION 3: RAM", fill=(255, 255, 255), font=font_title)
    draw.text((60, 1060), "USED: 8.4 GB", fill=(255, 160, 0), font=font_body)
    
    draw.text((60, 1400), "SECTION 4: GPU", fill=(255, 255, 255), font=font_title)
    draw.text((60, 1500), "TEMP: 42 C", fill=(220, 100, 255), font=font_body)
    
    return img

def main():
    if len(sys.argv) < 2:
        print("Usage: python test_mcu_subsampling.py <subsampling: 0=YUV444, 1=YUV422, 2=YUV420>")
        sys.exit(1)
        
    subsampling = int(sys.argv[1])
    sub_names = {0: "YUV444 (8x8 MCU)", 1: "YUV422 (16x8 MCU)", 2: "YUV420 (16x16 MCU)"}
    sub_name = sub_names.get(subsampling, f"Unknown ({subsampling})")
    
    dev_path = find_device()
    if not dev_path:
        print("Device 33c3:f101 not found")
        sys.exit(1)
        
    unbind_cdc_acm()
    
    img = create_dashboard_image(f"SUB: {sub_name}")
    out_path = f"/tmp/mcu_test_sub{subsampling}.jpg"
    img.save(out_path, format="JPEG", quality=75, subsampling=subsampling, optimize=True)
    
    with open(out_path, 'rb') as f:
        jpeg_bytes = f.read()
        
    print(f"=== Testing {sub_name} ===")
    print(f"JPEG size: {len(jpeg_bytes)} bytes")
    
    # Inspect SOF0
    idx = jpeg_bytes.find(b'\xff\xc0')
    if idx != -1:
        length = int.from_bytes(jpeg_bytes[idx+2:idx+4], 'big')
        print(f"SOF0 hex: {jpeg_bytes[idx:idx+2+length].hex()}")
        
    fd = os.open(dev_path, os.O_RDWR)
    try:
        fcntl.ioctl(fd, USBDEVFS_CLAIMINTERFACE, struct.pack('I', 1))
        
        for i in range(5):
            res = send_frame(fd, jpeg_bytes)
            print(f"  Frame {i+1} sent: OK")
            time.sleep(1.0)
            
        fcntl.ioctl(fd, USBDEVFS_RELEASEINTERFACE, struct.pack('I', 1))
    finally:
        os.close(fd)

if __name__ == "__main__":
    main()
