import os
import sys
import time
import struct
import fcntl
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

def create_text_image(text="HELLO WORLD"):
    img = Image.new('RGB', (640, 1920), (0, 0, 40))
    draw = ImageDraw.Draw(img)
    
    # Draw simple background shapes
    draw.rectangle([20, 20, 620, 1900], outline=(0, 255, 255), width=4)
    
    # Draw large centered text
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 60)
    except Exception:
        font = ImageFont.load_default()
        
    draw.text((100, 300), text, fill=(255, 255, 255), font=font)
    draw.text((100, 500), "STATUS: ONLINE", fill=(0, 255, 0), font=font)
    draw.text((100, 700), "SYSTEM NORMAL", fill=(255, 255, 0), font=font)
    
    return img

def main():
    dev_path = find_device()
    if not dev_path:
        print("Device not found")
        sys.exit(1)
        
    unbind_cdc_acm()
    
    img = create_text_image("HELLO WORLD")
    
    # Save using baseline PIL settings matching low-entropy JPEG
    img_path = "/tmp/test_text_baseline.jpg"
    img.save(img_path, format="JPEG", quality=75, subsampling=2)
    
    with open(img_path, 'rb') as f:
        jpeg_bytes = f.read()
        
    # MSDisplay Header: Magic=0x0008100A, W=640, H=1920, Stride=0, Flag=1
    header = struct.pack("<IHHHH", 0x0008100A, 640, 1920, 0, 1)
    payload = header + jpeg_bytes
    
    print(f"Sending text frame ({len(jpeg_bytes)} B JPEG, total {len(payload)} B)...")
    
    fd = os.open(dev_path, os.O_RDWR)
    try:
        fcntl.ioctl(fd, USBDEVFS_CLAIMINTERFACE, struct.pack('I', 1))
        
        # Keep alive for 5 seconds
        for i in range(5):
            buf = (ctypes.c_char * len(payload)).from_buffer_copy(payload)
            bulk_req = struct.pack('IIIIPI', 0x02, len(payload), 5000, 0, ctypes.addressof(buf), 0)
            res = fcntl.ioctl(fd, USBDEVFS_BULK, bulk_req)
            print(f"  Frame {i+1} sent: {res} B OK")
            time.sleep(1.0)
            
        fcntl.ioctl(fd, USBDEVFS_RELEASEINTERFACE, struct.pack('I', 1))
    finally:
        os.close(fd)

if __name__ == "__main__":
    import ctypes
    main()
