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
    return res, header.hex(), len(header), len(jpeg_bytes), len(payload)

def generate_460_diagnostic_jpeg(width, height=1920):
    jpg_path = f"/tmp/test_w{width}_h{height}_diag.jpg"
    img = Image.new('RGB', (width, height), (10, 18, 32))
    draw = ImageDraw.Draw(img)
    
    # 4 Horizontal color sections
    draw.rectangle([0, 0, width - 1, 479], fill=(200, 30, 30))          # Section 1: Red
    draw.rectangle([0, 480, width - 1, 959], fill=(20, 160, 40))        # Section 2: Green
    draw.rectangle([0, 960, width - 1, 1439], fill=(30, 60, 200))       # Section 3: Blue
    draw.rectangle([0, 1440, width - 1, 1919], fill=(220, 140, 0))      # Section 4: Orange
    
    # X=0: Left edge white vertical line (2px wide)
    draw.rectangle([0, 0, 1, height - 1], fill=(255, 255, 255))
    
    # X=100: Green marker vertical line
    if width > 100:
        draw.rectangle([99, 0, 101, height - 1], fill=(0, 255, 0))
        
    # X=center: White center marker vertical line
    center_x = width // 2
    draw.rectangle([center_x - 1, 0, center_x + 1, height - 1], fill=(255, 255, 255))
    
    # X=width-1: Right edge blue vertical line (2px wide)
    draw.rectangle([width - 2, 0, width - 1, height - 1], fill=(0, 200, 255))
    
    # Horizontal white grid lines every 100px
    for y in range(0, height, 100):
        draw.rectangle([0, y, width - 1, min(y + 1, height - 1)], fill=(255, 255, 255))
        
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 32)
    except Exception:
        font = ImageFont.load_default()
        
    draw.text((20, 200), f"WIDTH {width}", fill=(255, 255, 255), font=font)
    draw.text((20, 260), f"HEIGHT {height}", fill=(255, 255, 255), font=font)
    draw.text((20, 700), f"X-CENTER: {center_x}", fill=(255, 255, 255), font=font)
    draw.text((20, 1200), f"RIGHT-EDGE: {width-1}", fill=(255, 255, 255), font=font)
    
    img.save(jpg_path, "JPEG", quality=95, subsampling=0)
    with open(jpg_path, 'rb') as f:
        data = f.read()
        sha256 = hashlib.sha256(data).hexdigest()
        return data, sha256

def run_width_sweep(duration_sec=3.0, interval_sec=0.8):
    widths = [440, 450, 459, 460, 461, 470, 479, 480]
    dev_path = find_device()
    if not dev_path:
        print("[ERROR] USB device 33c3:f101 not found.")
        return
        
    unbind_cdc_acm()
    fd = os.open(dev_path, os.O_RDWR)
    try:
        fcntl.ioctl(fd, USBDEVFS_CLAIMINTERFACE, struct.pack('I', 1))
        print("\n==========================================================================================")
        print("  WIDTH SWEEP TEST AROUND 460 vs 480 BOUNDARY (H=1920)")
        print("==========================================================================================")
        print(f"{'Width':<6} | {'Header Hex':<26} | {'JPEG Size':<10} | {'Total Tx':<10} | {'USB Status':<12}")
        print("-" * 90)
        
        for w in widths:
            jpeg_bytes, sha256 = generate_460_diagnostic_jpeg(w, 1920)
            start = time.monotonic()
            while (time.monotonic() - start) < duration_sec:
                res, hdr_hex, hdr_l, jpg_l, tot_l = send_frame(fd, w, 1920, 0, 1, jpeg_bytes)
                time.sleep(interval_sec)
            print(f"{w:<6} | {hdr_hex:<26} | {jpg_l:<10} | {tot_l:<10} | OK ({tot_l}B)")
            time.sleep(0.5)
            
        fcntl.ioctl(fd, USBDEVFS_RELEASEINTERFACE, struct.pack('I', 1))
    finally:
        os.close(fd)

def run_field3_test_for_460(duration_sec=3.0, interval_sec=0.8):
    f3_values = [0, 460, 480, 1920]
    dev_path = find_device()
    if not dev_path:
        print("[ERROR] USB device 33c3:f101 not found.")
        return
        
    unbind_cdc_acm()
    jpeg_bytes, sha256 = generate_460_diagnostic_jpeg(460, 1920)
    
    fd = os.open(dev_path, os.O_RDWR)
    try:
        fcntl.ioctl(fd, USBDEVFS_CLAIMINTERFACE, struct.pack('I', 1))
        print("\n==========================================================================================")
        print("  WIDTH=460 FIELD3 INTERACTION TEST (H=1920, Field4=1)")
        print("==========================================================================================")
        print(f"{'Field 3':<8} | {'Header Hex':<26} | {'JPEG Size':<10} | {'Total Tx':<10} | {'USB Status':<12}")
        print("-" * 90)
        
        for f3 in f3_values:
            start = time.monotonic()
            while (time.monotonic() - start) < duration_sec:
                res, hdr_hex, hdr_l, jpg_l, tot_l = send_frame(fd, 460, 1920, f3, 1, jpeg_bytes)
                time.sleep(interval_sec)
            print(f"{f3:<8} | {hdr_hex:<26} | {jpg_l:<10} | {tot_l:<10} | OK ({tot_l}B)")
            time.sleep(0.5)
            
        fcntl.ioctl(fd, USBDEVFS_RELEASEINTERFACE, struct.pack('I', 1))
    finally:
        os.close(fd)

def main():
    parser = argparse.ArgumentParser(description="Test Width 460 Investigation")
    parser.add_argument('--mode', type=str, choices=['sweep', 'field3', 'compare460vs480', 'all'], default='all')
    parser.add_argument('--duration', type=float, default=3.0)
    args = parser.parse_args()

    if args.mode in ('sweep', 'all'):
        run_width_sweep(duration_sec=args.duration)

    if args.mode in ('field3', 'all'):
        run_field3_test_for_460(duration_sec=args.duration)

    if args.mode in ('compare460vs480', 'all'):
        dev_path = find_device()
        if not dev_path:
            print("[ERROR] USB device 33c3:f101 not found.")
            sys.exit(1)
        unbind_cdc_acm()
        fd = os.open(dev_path, os.O_RDWR)
        try:
            fcntl.ioctl(fd, USBDEVFS_CLAIMINTERFACE, struct.pack('I', 1))
            print("\n==========================================================================================")
            print("  DIRECT COMPARISON: 460x1920 VS 480x1920")
            print("==========================================================================================")
            
            # Test 460
            jpg460, sha460 = generate_460_diagnostic_jpeg(460, 1920)
            res460, hex460, _, _, tot460 = send_frame(fd, 460, 1920, 0, 1, jpg460)
            print(f"  [1/2] Transmitted 460x1920 | Header: {hex460} | SHA256: {sha460[:16]}... | Tx: {tot460}B OK")
            print("  OBSERVE LCD: Check left edge (white line), center line, right edge (blue line).")
            time.sleep(args.duration)
            
            # Test 480
            jpg480, sha480 = generate_460_diagnostic_jpeg(480, 1920)
            res480, hex480, _, _, tot480 = send_frame(fd, 480, 1920, 0, 1, jpg480)
            print(f"  [2/2] Transmitted 480x1920 | Header: {hex480} | SHA256: {sha480[:16]}... | Tx: {tot480}B OK")
            print("  OBSERVE LCD: Check left edge (white line), center line, right edge (blue line).")
            time.sleep(args.duration)

            fcntl.ioctl(fd, USBDEVFS_RELEASEINTERFACE, struct.pack('I', 1))
        finally:
            os.close(fd)

if __name__ == "__main__":
    main()
