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

def fix_jpeg_structure(raw_bytes):
    """
    Strips all original DQT, DHT, and SOF0 markers from raw_bytes and replaces them
    with EXACTLY the single DQT, single DHT, and SOF0 of pattern_640x1920.jpg.
    """
    with open('portrait_patterns/pattern_640x1920.jpg', 'rb') as f:
        pattern_data = f.read()
        
    # Extract exact DQT (Len=67), DHT (Len=81), SOF0 (Len=17) from pattern_640x1920.jpg
    # pattern header up to SOS (offset 0x00CC)
    pattern_header = pattern_data[2:0x00CC] # skip initial SOI (FF D8)
    
    pos = 0
    new_bytes = bytearray()
    new_bytes.extend(b'\xff\xd8') # SOI
    new_bytes.extend(pattern_header) # exact single DQT, single DHT, SOF0, SOS header
    
    # Find original SOS marker in raw_bytes and copy only scan data
    sos_idx = raw_bytes.find(b'\xff\xda')
    if sos_idx != -1:
        sos_len = int.from_bytes(raw_bytes[sos_idx+2:sos_idx+4], 'big')
        scan_data = raw_bytes[sos_idx+2+sos_len:]
        new_bytes.extend(scan_data)
    else:
        new_bytes.extend(raw_bytes)
        
    return bytes(new_bytes)

def create_perfect_frame(text="HELLO WORLD"):
    img = Image.new('RGB', (640, 1920), (10, 18, 32))
    draw = ImageDraw.Draw(img)
    
    draw.rectangle([10, 10, 630, 1910], outline=(0, 200, 255), width=4)
    
    try:
        font_lg = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 48)
        font_md = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 36)
    except Exception:
        font_lg = font_md = ImageFont.load_default()
        
    draw.rectangle([30, 40, 610, 440], fill=(20, 35, 60), outline=(0, 200, 255), width=3)
    draw.text((60, 80), "PERFECT MATCH MONITOR", fill=(0, 200, 255), font=font_md)
    draw.text((60, 200), text, fill=(255, 255, 255), font=font_lg)
    
    draw.rectangle([30, 480, 610, 880], fill=(20, 60, 40), outline=(0, 255, 120), width=3)
    draw.text((60, 520), "STRUCTURE MATCHED", fill=(0, 255, 120), font=font_md)
    draw.text((60, 640), "1 DQT / 1 DHT / 011200", fill=(255, 255, 255), font=font_lg)
    
    draw.rectangle([30, 920, 610, 1320], fill=(60, 40, 20), outline=(255, 160, 0), width=3)
    draw.text((60, 960), "HARDWARE ALIGNED", fill=(255, 160, 0), font=font_md)
    draw.text((60, 1080), "640x1920 PORTRAIT", fill=(255, 255, 255), font=font_lg)
    
    draw.rectangle([30, 1360, 610, 1860], fill=(50, 20, 60), outline=(220, 100, 255), width=3)
    draw.text((60, 1400), "VMAX LINUX NATIVE", fill=(220, 100, 255), font=font_md)
    draw.text((60, 1520), "100% PERFECT RENDER", fill=(255, 255, 255), font=font_lg)
    
    out_jpg = "/tmp/perfect_match.jpg"
    img.save(out_jpg, format="JPEG", quality=75, subsampling=0, optimize=False)
    
    with open(out_jpg, 'rb') as f:
        raw_bytes = f.read()
        
    fixed_bytes = fix_jpeg_structure(raw_bytes)
    with open('/tmp/perfect_match_fixed.jpg', 'wb') as f:
        f.write(fixed_bytes)
    return fixed_bytes

def main():
    dev_path = find_device()
    if not dev_path:
        print("Device 33c3:f101 not found")
        sys.exit(1)
        
    unbind_cdc_acm()
    
    jpeg_bytes = create_perfect_frame("HELLO WORLD")
    print(f"=== Perfect Baseline Matcher Driver Test ({len(jpeg_bytes)} B JPEG) ===")
    
    fd = os.open(dev_path, os.O_RDWR)
    try:
        fcntl.ioctl(fd, USBDEVFS_CLAIMINTERFACE, struct.pack('I', 1))
        
        for i in range(5):
            send_frame(fd, jpeg_bytes)
            print(f"  Frame #{i+1:02d} sent: OK")
            time.sleep(1.0)
            
        fcntl.ioctl(fd, USBDEVFS_RELEASEINTERFACE, struct.pack('I', 1))
    finally:
        os.close(fd)

if __name__ == "__main__":
    main()
