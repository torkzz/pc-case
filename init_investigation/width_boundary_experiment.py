import os
import sys
import time
import struct
import fcntl
import ctypes
import argparse
from PIL import Image, ImageDraw

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

def inspect_jpeg_sof0(jpeg_bytes):
    idx = jpeg_bytes.find(b'\xff\xc0')
    if idx == -1:
        return None, None, None
    length = struct.unpack('>H', jpeg_bytes[idx+2:idx+4])[0]
    sof_payload = jpeg_bytes[idx:idx+2+length]
    prec = sof_payload[4]
    h = (sof_payload[5] << 8) | sof_payload[6]
    w = (sof_payload[7] << 8) | sof_payload[8]
    comps = sof_payload[9]
    return w, h, sof_payload.hex()

def send_frame(fd, header_w, header_h, jpeg_bytes, endpoint=0x02, timeout_ms=2000):
    header = struct.pack("<IHHHH", MSDISPLAY_MAGIC_SIGNATURE, header_w, header_h, 0, 1)
    payload = header + jpeg_bytes
    
    data_buf = ctypes.create_string_buffer(payload)
    bulk_req = struct.pack('IIIIPI', endpoint, len(payload), timeout_ms, 0, ctypes.addressof(data_buf), 0)
    res = fcntl.ioctl(fd, USBDEVFS_BULK, bulk_req)
    return res, header.hex(), len(header), len(jpeg_bytes), len(payload)

def generate_3col_jpeg(width, height=1920):
    jpg_path = f"/tmp/test_w{width}_h{height}.jpg"
    img = Image.new('RGB', (width, height), (0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    col_w = width / 3.0
    row_h = height / 4.0
    colors_grid = [
        [(255, 0, 0),   (0, 255, 0),   (0, 0, 255)],     # Red, Green, Blue
        [(255, 255, 0), (0, 255, 255), (255, 0, 255)],   # Yellow, Cyan, Magenta
        [(255, 128, 0), (0, 255, 128), (128, 0, 255)],   # Orange, Mint, Purple
        [(128, 0, 0),   (0, 128, 0),   (0, 0, 128)]      # Dark Red, Dark Green, Dark Blue
    ]
    
    for row_idx in range(4):
        y0 = int(row_idx * row_h)
        y1 = int((row_idx + 1) * row_h)
        for col_idx in range(3):
            x0 = int(col_idx * col_w)
            x1 = int((col_idx + 1) * col_w)
            c = colors_grid[row_idx][col_idx]
            draw.rectangle([x0, y0, max(x0, x1 - 1), max(y0, y1 - 1)], fill=c)
            
    img.save(jpg_path, "JPEG", quality=95, subsampling=0)
    with open(jpg_path, 'rb') as f:
        return f.read()

def run_part1_width_sweep(duration_sec=3.0, interval_sec=1.0):
    widths = [320, 400, 479, 480, 481, 512, 640, 800]
    dev_path = find_device()
    if not dev_path:
        print("[ERROR] USB device 33c3:f101 not found.")
        return
        
    unbind_cdc_acm()
    
    fd = os.open(dev_path, os.O_RDWR)
    try:
        fcntl.ioctl(fd, USBDEVFS_CLAIMINTERFACE, struct.pack('I', 1))
        print("\n==========================================================================================")
        print("  PART 1: CONTROLLED WIDTH-BOUNDARY EXPERIMENT (H=1920)")
        print("==========================================================================================")
        print(f"{'Width':<6} | {'Header Hex':<26} | {'SOF WxH':<10} | {'JPEG Size':<10} | {'Total Tx':<10} | {'USB Status':<12}")
        print("-" * 90)
        
        for w in widths:
            jpeg_bytes = generate_3col_jpeg(w, 1920)
            sof_w, sof_h, sof_hex = inspect_jpeg_sof0(jpeg_bytes)
            
            start = time.monotonic()
            while (time.monotonic() - start) < duration_sec:
                res, hdr_hex, hdr_l, jpg_l, tot_l = send_frame(fd, w, 1920, jpeg_bytes)
                time.sleep(interval_sec)
                
            print(f"{w:<6} | {hdr_hex:<26} | {sof_w}x{sof_h:<5} | {jpg_l:<10} | {tot_l:<10} | OK ({tot_l}B)")
            time.sleep(1.0)
            
        fcntl.ioctl(fd, USBDEVFS_RELEASEINTERFACE, struct.pack('I', 1))
    finally:
        os.close(fd)

def run_part2_matrix(duration_sec=3.0, interval_sec=1.0):
    matrix_cases = [
        ("M1 (Hdr 480 + JPG 480)", 480, 480),
        ("M2 (Hdr 480 + JPG 640)", 480, 640),
        ("M3 (Hdr 640 + JPG 480)", 640, 480),
        ("M4 (Hdr 640 + JPG 640)", 640, 640),
    ]
    dev_path = find_device()
    if not dev_path:
        print("[ERROR] USB device 33c3:f101 not found.")
        return
        
    unbind_cdc_acm()
    
    fd = os.open(dev_path, os.O_RDWR)
    try:
        fcntl.ioctl(fd, USBDEVFS_CLAIMINTERFACE, struct.pack('I', 1))
        print("\n==========================================================================================")
        print("  PART 2: 2x2 PROTOCOL MATRIX EXPERIMENT (HEADER vs JPEG DIMENSIONS)")
        print("==========================================================================================")
        print(f"{'Matrix Case':<24} | {'Hdr WxH':<10} | {'JPG SOF WxH':<12} | {'JPEG Size':<10} | {'Total Tx':<10} | {'USB Status':<12}")
        print("-" * 90)
        
        for name, hdr_w, jpg_w in matrix_cases:
            jpeg_bytes = generate_3col_jpeg(jpg_w, 1920)
            sof_w, sof_h, sof_hex = inspect_jpeg_sof0(jpeg_bytes)
            
            start = time.monotonic()
            while (time.monotonic() - start) < duration_sec:
                res, hdr_hex, hdr_l, jpg_l, tot_l = send_frame(fd, hdr_w, 1920, jpeg_bytes)
                time.sleep(interval_sec)
                
            print(f"{name:<24} | {hdr_w}x1920    | {sof_w}x{sof_h:<7} | {jpg_l:<10} | {tot_l:<10} | OK ({tot_l}B)")
            time.sleep(1.0)
            
        fcntl.ioctl(fd, USBDEVFS_RELEASEINTERFACE, struct.pack('I', 1))
    finally:
        os.close(fd)

def main():
    parser = argparse.ArgumentParser(description="Width Boundary & Protocol Layer Experiment")
    parser.add_argument('--mode', type=str, choices=['part1', 'part2', 'all'], default='all')
    parser.add_argument('--duration', type=float, default=3.0)
    args = parser.parse_args()
    
    if args.mode in ('part1', 'all'):
        run_part1_width_sweep(duration_sec=args.duration)
        
    if args.mode in ('part2', 'all'):
        run_part2_matrix(duration_sec=args.duration)

if __name__ == "__main__":
    main()
