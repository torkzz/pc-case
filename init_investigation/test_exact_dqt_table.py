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

EXACT_MSDISPLAY_DQT_TABLE = bytes([
    8, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 8, 8, 8, 7, 7, 7, 6, 6, 7, 7, 8, 8, 8, 8, 9, 9, 9, 8, 8, 8, 8, 9, 9, 10, 10, 10, 12, 12, 11, 11, 14, 14, 14, 17, 17, 20
])

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

def create_exact_dqt_jpeg(text="HELLO WORLD"):
    img = Image.new('RGB', (640, 1920), (10, 18, 32))
    draw = ImageDraw.Draw(img)
    
    draw.rectangle([10, 10, 630, 1910], outline=(0, 200, 255), width=4)
    
    try:
        font_lg = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 48)
        font_md = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 36)
    except Exception:
        font_lg = font_md = ImageFont.load_default()
        
    draw.rectangle([30, 40, 610, 440], fill=(20, 35, 60), outline=(0, 200, 255), width=3)
    draw.text((60, 80), "EXACT DQT MONITOR", fill=(0, 200, 255), font=font_md)
    draw.text((60, 200), text, fill=(255, 255, 255), font=font_lg)
    
    draw.rectangle([30, 480, 610, 880], fill=(20, 60, 40), outline=(0, 255, 120), width=3)
    draw.text((60, 520), "HARDWARE MATRIX", fill=(0, 255, 120), font=font_md)
    draw.text((60, 640), "MATCHED DQT TABLE", fill=(255, 255, 255), font=font_lg)
    
    draw.rectangle([30, 920, 610, 1320], fill=(60, 40, 20), outline=(255, 160, 0), width=3)
    draw.text((60, 960), "STATUS", fill=(255, 160, 0), font=font_md)
    draw.text((60, 1080), "SINGLE DQT MATCH", fill=(255, 255, 255), font=font_lg)
    
    draw.rectangle([30, 1360, 610, 1860], fill=(50, 20, 60), outline=(220, 100, 255), width=3)
    draw.text((60, 1400), "VMAX LINUX NATIVE", fill=(220, 100, 255), font=font_md)
    draw.text((60, 1520), "640x1920", fill=(255, 255, 255), font=font_lg)
    
    # Write custom DQT file for cjpeg
    dqt_txt_path = "/tmp/msdisplay_dqt.txt"
    with open(dqt_txt_path, 'w') as f:
        # Write 64 integers separated by spaces
        f.write(" ".join(str(x) for x in EXACT_MSDISPLAY_DQT_TABLE) + "\n")
        
    ppm_path = "/tmp/exact_dqt.ppm"
    jpg_path = "/tmp/exact_dqt.jpg"
    
    header = f"P6\n640 1920\n255\n".encode('ascii')
    with open(ppm_path, 'wb') as f:
        f.write(header)
        f.write(img.tobytes())
        
    cmd = [
        'cjpeg',
        '-qtable', dqt_txt_path,
        '-sample', '1x2,1x2,1x2',
        '-outfile', jpg_path,
        ppm_path
    ]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    with open(jpg_path, 'rb') as f:
        return f.read()

def main():
    dev_path = find_device()
    if not dev_path:
        print("Device 33c3:f101 not found")
        sys.exit(1)
        
    unbind_cdc_acm()
    
    jpeg_bytes = create_exact_dqt_jpeg("HELLO WORLD")
    print(f"=== Exact DQT Table Driver Test ({len(jpeg_bytes)} B JPEG) ===")
    
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
