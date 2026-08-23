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

def generate_solid_blocks_jpeg(num_blocks=4):
    ppm_path = f"/tmp/blocks_{num_blocks}.ppm"
    jpg_path = f"/tmp/blocks_{num_blocks}.jpg"
    
    img = Image.new('RGB', (WIDTH, HEIGHT), (0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    block_h = HEIGHT // num_blocks
    colors = [
        (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 255),
        (255, 255, 0), (0, 255, 255), (255, 0, 255), (128, 128, 128)
    ]
    
    for i in range(num_blocks):
        y0 = i * block_h
        y1 = (i + 1) * block_h if i < num_blocks - 1 else HEIGHT
        c = colors[i % len(colors)]
        draw.rectangle([0, y0, WIDTH, y1], fill=c)
        
    header = f"P6\n{WIDTH} {HEIGHT}\n255\n".encode('ascii')
    with open(ppm_path, 'wb') as f:
        f.write(header)
        f.write(img.tobytes())
        
    cmd = ['ffmpeg', '-y', '-i', ppm_path, '-q:v', '2', jpg_path]
    subprocess.check_call(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    with open(jpg_path, 'rb') as f:
        return f.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: test_size_threshold.py <num_blocks>")
        sys.exit(1)
        
    num_blocks = int(sys.argv[1])
    dev_path = find_device()
    if not dev_path:
        print("[ERROR] Device 33c3:f101 not found.")
        sys.exit(1)
        
    unbind_cdc_acm()
    jpeg_bytes = generate_solid_blocks_jpeg(num_blocks)
    print(f"=== Testing {num_blocks} Solid Color Blocks (JPEG size: {len(jpeg_bytes)} B) ===")
    
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
