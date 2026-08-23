import os
import sys
import time
import struct
import fcntl
import ctypes
import hashlib
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

def send_frame(fd, header_w, header_h, field3, field4, jpeg_bytes, endpoint=0x02, timeout_ms=2000):
    header = struct.pack("<IHHHH", MSDISPLAY_MAGIC_SIGNATURE, header_w, header_h, field3, field4)
    payload = header + jpeg_bytes
    
    data_buf = ctypes.create_string_buffer(payload)
    bulk_req = struct.pack('IIIIPI', endpoint, len(payload), timeout_ms, 0, ctypes.addressof(data_buf), 0)
    res = fcntl.ioctl(fd, USBDEVFS_BULK, bulk_req)
    return res, header.hex(), len(header), len(jpeg_bytes), len(payload)

def generate_static_marked_jpeg(label_text="STATIC SINGLE FRAME"):
    jpg_path = "/tmp/static_marked_480x1920.jpg"
    img = Image.new('RGB', (WIDTH, HEIGHT), (0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # 5 Color Regions
    draw.rectangle([0, 0, WIDTH - 1, 479], fill=(255, 0, 0))          # RED (0..479)
    draw.rectangle([0, 480, WIDTH - 1, 959], fill=(0, 255, 0))        # GREEN (480..959)
    draw.rectangle([0, 960, WIDTH - 1, 1439], fill=(0, 0, 255))       # BLUE (960..1439)
    draw.rectangle([0, 1440, WIDTH - 1, 1799], fill=(255, 255, 0))    # YELLOW (1440..1799)
    draw.rectangle([0, 1800, WIDTH - 1, 1919], fill=(255, 0, 255))    # MAGENTA (1800..1919)
    
    # Vertical white lines at x=0, x=240, x=479
    draw.rectangle([0, 0, 3, HEIGHT - 1], fill=(255, 255, 255))
    draw.rectangle([238, 0, 241, HEIGHT - 1], fill=(255, 255, 255))
    draw.rectangle([WIDTH - 4, 0, WIDTH - 1, HEIGHT - 1], fill=(255, 255, 255))
    
    # Horizontal white lines every 100px
    for y in range(0, HEIGHT, 100):
        draw.rectangle([0, y, WIDTH - 1, min(y + 2, HEIGHT - 1)], fill=(255, 255, 255))
        
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 28)
    except Exception:
        font = ImageFont.load_default()
        
    draw.text((40, 220), label_text, fill=(255, 255, 255), font=font)
    draw.text((40, 700), "NO RETRANSMISSION TEST", fill=(0, 0, 0), font=font)
    
    img.save(jpg_path, "JPEG", quality=95, subsampling=0)
    with open(jpg_path, 'rb') as f:
        data = f.read()
        sha256 = hashlib.sha256(data).hexdigest()
        return data, sha256

def main():
    parser = argparse.ArgumentParser(description="Experiment 3 & 5: Single Static Frame vs Repeated Submissions")
    parser.add_argument('--mode', type=str, choices=['single', 'repeated'], default='single')
    parser.add_argument('--wait', type=float, default=45.0, help="Wait duration for single frame test (seconds)")
    parser.add_argument('--interval', type=float, default=1.0, help="Interval for repeated mode (seconds)")
    args = parser.parse_args()

    jpeg_bytes, sha256 = generate_static_marked_jpeg()
    print(f"=== EXPERIMENT 3 / 5: STATIC SINGLE FRAME ({args.mode.upper()} MODE) ===")
    print(f"  JPEG Size  : {len(jpeg_bytes)} bytes")
    print(f"  JPEG SHA256: {sha256}")

    dev_path = find_device()
    if not dev_path:
        print("[ERROR] USB device 33c3:f101 not found.")
        sys.exit(1)

    unbind_cdc_acm()

    fd = os.open(dev_path, os.O_RDWR)
    try:
        fcntl.ioctl(fd, USBDEVFS_CLAIMINTERFACE, struct.pack('I', 1))
        
        if args.mode == 'single':
            print("\n------------------------------------------------------------")
            print("  TRANSMITTING SINGLE FRAME ONCE (Field3=0, Field4=1)...")
            res, hdr_hex, hdr_l, jpg_l, tot_l = send_frame(fd, WIDTH, HEIGHT, 0, 1, jpeg_bytes)
            print(f"  12-Byte Header Hex: {hdr_hex}")
            print(f"  Total Payload     : {tot_l} bytes")
            print(f"  USB Status        : OK ({tot_l}B)")
            print(f"  [ACTION] NO MORE USB TRANSMISSIONS. Waiting {args.wait}s...")
            print("  OBSERVE LCD NOW: Does the static content move or roll physically?")
            
            start_wait = time.monotonic()
            while (time.monotonic() - start_wait) < args.wait:
                time.sleep(1.0)
                
            print(f"  [COMPLETED] Single frame wait period of {args.wait}s elapsed.")

        elif args.mode == 'repeated':
            print("\n------------------------------------------------------------")
            print(f"  TRANSMITTING IDENTICAL FRAME REPEATEDLY (Interval: {args.interval}s, Duration: 10s)...")
            start = time.monotonic()
            seq = 1
            while (time.monotonic() - start) < 10.0:
                cur_sha = hashlib.sha256(jpeg_bytes).hexdigest()
                res, hdr_hex, hdr_l, jpg_l, tot_l = send_frame(fd, WIDTH, HEIGHT, 0, 1, jpeg_bytes)
                print(f"  Frame #{seq:02d} | SHA256: {cur_sha[:16]}... | Tx: {tot_l}B OK")
                seq += 1
                time.sleep(args.interval)

        fcntl.ioctl(fd, USBDEVFS_RELEASEINTERFACE, struct.pack('I', 1))
    finally:
        os.close(fd)

if __name__ == "__main__":
    main()
