import os
import sys
import time
import struct
import fcntl
import ctypes
import hashlib
import argparse
from PIL import Image, ImageDraw

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

def send_single_frame(fd, header_w, header_h, field3, field4, jpeg_bytes, endpoint=0x02, timeout_ms=2000):
    header = struct.pack("<IHHHH", MSDISPLAY_MAGIC_SIGNATURE, header_w, header_h, field3, field4)
    payload = header + jpeg_bytes
    
    data_buf = ctypes.create_string_buffer(payload)
    bulk_req = struct.pack('IIIIPI', endpoint, len(payload), timeout_ms, 0, ctypes.addressof(data_buf), 0)
    res = fcntl.ioctl(fd, USBDEVFS_BULK, bulk_req)
    return res, header.hex(), len(header), len(jpeg_bytes), len(payload)

def generate_static_480x1920_jpeg():
    jpg_path = "/tmp/static_480x1920_exp2.jpg"
    img = Image.new('RGB', (WIDTH, HEIGHT), (10, 18, 32))
    draw = ImageDraw.Draw(img)
    
    draw.rectangle([0, 0, WIDTH - 1, 479], fill=(255, 0, 0))
    draw.rectangle([0, 480, WIDTH - 1, 959], fill=(0, 255, 0))
    draw.rectangle([0, 960, WIDTH - 1, 1439], fill=(0, 0, 255))
    draw.rectangle([0, 1440, WIDTH - 1, 1919], fill=(255, 255, 0))
    
    draw.rectangle([0, 0, 15, HEIGHT - 1], fill=(255, 255, 255))
    draw.rectangle([235, 0, 245, HEIGHT - 1], fill=(255, 255, 255))
    draw.rectangle([WIDTH - 16, 0, WIDTH - 1, HEIGHT - 1], fill=(255, 255, 255))
    
    img.save(jpg_path, "JPEG", quality=95, subsampling=0)
    with open(jpg_path, 'rb') as f:
        data = f.read()
        sha256 = hashlib.sha256(data).hexdigest()
        return data, sha256

def main():
    parser = argparse.ArgumentParser(description="Experiment 2: Header Field 4 Variations")
    parser.add_argument('--variant', type=str, choices=['A', 'B', 'C', 'D', 'ALL'], default='ALL')
    args = parser.parse_args()

    jpeg_bytes, sha256 = generate_static_480x1920_jpeg()
    print(f"=== EXPERIMENT 2: HEADER FIELD 4 VARIATIONS ===")
    print(f"  JPEG Size  : {len(jpeg_bytes)} bytes")
    print(f"  JPEG SHA256: {sha256}")

    test_cases = [
        ("A", 0, 0),
        ("B", 0, 1),
        ("C", 0, 2),
        ("D", 0, 3),
    ]

    dev_path = find_device()
    if not dev_path:
        print("[ERROR] USB device 33c3:f101 not found.")
        sys.exit(1)

    unbind_cdc_acm()

    fd = os.open(dev_path, os.O_RDWR)
    try:
        fcntl.ioctl(fd, USBDEVFS_CLAIMINTERFACE, struct.pack('I', 1))
        
        for name, f3, f4 in test_cases:
            if args.variant not in ('ALL', name):
                continue
                
            print(f"\n------------------------------------------------------------")
            print(f"  VARIANT {name}: Field3={f3}, Field4={f4}")
            res, hdr_hex, hdr_l, jpg_l, tot_l = send_single_frame(fd, WIDTH, HEIGHT, f3, f4, jpeg_bytes)
            print(f"  12-Byte Header Hex: {hdr_hex}")
            print(f"  Total Payload     : {tot_l} bytes")
            print(f"  USB Status        : OK (Submitted 1 frame)")
            print("  [ACTION] Wait 15-20s. Observe physical LCD for behavior.")
            
            if args.variant == 'ALL':
                time.sleep(15.0)

        fcntl.ioctl(fd, USBDEVFS_RELEASEINTERFACE, struct.pack('I', 1))
    finally:
        os.close(fd)

if __name__ == "__main__":
    main()
