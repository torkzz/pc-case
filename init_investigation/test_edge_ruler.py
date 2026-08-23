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

MSDISPLAY_MAGIC_SIGNATURE = 0x0008100A
WIDTH = 480
HEIGHT = 1920

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

def send_frame(fd, width, height, field3, field4, jpeg_bytes, endpoint=0x02, timeout_ms=2000):
    header = struct.pack("<IHHHH", MSDISPLAY_MAGIC_SIGNATURE, width, height, field3, field4)
    payload = header + jpeg_bytes
    
    data_buf = ctypes.create_string_buffer(payload)
    bulk_req = struct.pack('IIIIPI', endpoint, len(payload), timeout_ms, 0, ctypes.addressof(data_buf), 0)
    res = fcntl.ioctl(fd, USBDEVFS_BULK, bulk_req)
    return res, header.hex(), len(payload)

def generate_edge_ruler_jpeg():
    jpg_path = "/tmp/edge_ruler_480x1920.jpg"
    img = Image.new('RGB', (WIDTH, HEIGHT), (15, 20, 35))
    draw = ImageDraw.Draw(img)
    
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 20)
        font_lg = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 36)
    except Exception:
        font = font_lg = ImageFont.load_default()

    # Title
    draw.text((60, 60), "EDGE RULER DIAGNOSTIC", fill=(0, 220, 255), font=font_lg)
    draw.text((60, 120), "Check Left & Right Labels", fill=(255, 255, 255), font=font)

    # Horizontal bars across middle for height reference
    draw.rectangle([0, 480, WIDTH-1, 484], fill=(255, 255, 255))
    draw.rectangle([0, 960, WIDTH-1, 964], fill=(255, 255, 255))
    draw.rectangle([0, 1440, WIDTH-1, 1444], fill=(255, 255, 255))

    # LEFT EDGE RULER (X = 0 to 60)
    left_markers = [0, 10, 20, 30, 40, 50, 60]
    colors_left = [(255, 0, 0), (255, 128, 0), (255, 255, 0), (0, 255, 0), (0, 255, 255), (0, 128, 255), (128, 0, 255)]
    for idx, x in enumerate(left_markers):
        c = colors_left[idx % len(colors_left)]
        draw.line([(x, 0), (x, HEIGHT)], fill=c, width=2)
        # Label near Y=300
        draw.text((x + 2, 200 + (idx * 35)), f"L{x}", fill=c, font=font)

    # RIGHT EDGE RULER (X = 400 to 479)
    right_markers = [400, 410, 420, 430, 440, 450, 460, 470, 479]
    colors_right = [(255, 0, 0), (255, 128, 0), (255, 255, 0), (0, 255, 0), (0, 255, 255), (0, 128, 255), (128, 0, 255), (255, 0, 255), (255, 255, 255)]
    for idx, x in enumerate(right_markers):
        c = colors_right[idx % len(colors_right)]
        draw.line([(x, 0), (x, HEIGHT)], fill=c, width=2)
        # Label near Y=700
        draw.text((x - 45, 650 + (idx * 35)), f"R{x}", fill=c, font=font)

    # Center Marker
    draw.line([(240, 0), (240, HEIGHT)], fill=(255, 255, 255), width=2)
    draw.text((210, 500), "C240", fill=(255, 255, 255), font=font)

    img.save(jpg_path, "JPEG", quality=95, subsampling=0)
    with open(jpg_path, 'rb') as f:
        return f.read()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--duration', type=float, default=10.0)
    args = parser.parse_args()

    dev_path = find_device()
    if not dev_path:
        print("[ERROR] USB device 33c3:f101 not found.")
        sys.exit(1)

    unbind_cdc_acm()
    jpeg_bytes = generate_edge_ruler_jpeg()
    print(f"=== EDGE RULER DIAGNOSTIC (480x1920) ===")
    print(f"  JPEG Size: {len(jpeg_bytes)} bytes")

    fd = os.open(dev_path, os.O_RDWR)
    try:
        fcntl.ioctl(fd, USBDEVFS_CLAIMINTERFACE, struct.pack('I', 1))
        
        start = time.monotonic()
        while (time.monotonic() - start) < args.duration:
            send_frame(fd, WIDTH, HEIGHT, 0, 1, jpeg_bytes)
            time.sleep(1.0)
            
        fcntl.ioctl(fd, USBDEVFS_RELEASEINTERFACE, struct.pack('I', 1))
    finally:
        os.close(fd)

if __name__ == "__main__":
    main()
