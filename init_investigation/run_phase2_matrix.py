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
    h = (sof_payload[5] << 8) | sof_payload[6]
    w = (sof_payload[7] << 8) | sof_payload[8]
    return w, h, sof_payload.hex()

def send_frame(fd, header_w, header_h, jpeg_bytes, endpoint=0x02, timeout_ms=2000):
    header = struct.pack("<IHHHH", MSDISPLAY_MAGIC_SIGNATURE, header_w, header_h, 0, 1)
    payload = header + jpeg_bytes
    
    data_buf = ctypes.create_string_buffer(payload)
    bulk_req = struct.pack('IIIIPI', endpoint, len(payload), timeout_ms, 0, ctypes.addressof(data_buf), 0)
    res = fcntl.ioctl(fd, USBDEVFS_BULK, bulk_req)
    return res, header.hex(), len(header), len(jpeg_bytes), len(payload)

def generate_stripe_jpeg(width, height=1920):
    jpg_path = f"/tmp/matrix_w{width}_h{height}.jpg"
    img = Image.new('RGB', (width, height), (0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255), (255, 0, 255), (255, 255, 255), (128, 128, 128)]
    stripe_w = 16
    num_stripes = (width + stripe_w - 1) // stripe_w
    for i in range(num_stripes):
        x0 = i * stripe_w
        x1 = min(width, (i + 1) * stripe_w)
        c = colors[i % len(colors)]
        draw.rectangle([x0, 0, max(x0, x1 - 1), height - 1], fill=c)
        
    img.save(jpg_path, "JPEG", quality=95, subsampling=0)
    with open(jpg_path, 'rb') as f:
        return f.read()

def main():
    parser = argparse.ArgumentParser(description="Phase 2: 2x2 Header vs JPEG Matrix")
    parser.add_argument('--duration', type=float, default=3.0)
    args = parser.parse_args()
    
    matrix_cases = [
        ("Test A (Hdr 480 + JPG 480)", 480, 480),
        ("Test B (Hdr 480 + JPG 640)", 480, 640),
        ("Test C (Hdr 640 + JPG 480)", 640, 480),
        ("Test D (Hdr 640 + JPG 640)", 640, 640),
    ]
    
    dev_path = find_device()
    if not dev_path:
        print("[ERROR] USB device 33c3:f101 not found.")
        sys.exit(1)
        
    unbind_cdc_acm()
    
    fd = os.open(dev_path, os.O_RDWR)
    try:
        fcntl.ioctl(fd, USBDEVFS_CLAIMINTERFACE, struct.pack('I', 1))
        print("\n==========================================================================================")
        print("  PHASE 2: 2x2 PROTOCOL MATRIX EXPERIMENT (HEADER vs JPEG DIMENSIONS)")
        print("==========================================================================================")
        print(f"{'Matrix Test':<27} | {'Header WxH':<10} | {'SOF WxH':<10} | {'JPEG Size':<10} | {'Total Tx':<10} | {'USB Status':<12}")
        print("-" * 90)
        
        for name, hdr_w, jpg_w in matrix_cases:
            jpeg_bytes = generate_stripe_jpeg(jpg_w, 1920)
            sof_w, sof_h, sof_hex = inspect_jpeg_sof0(jpeg_bytes)
            
            start = time.monotonic()
            while (time.monotonic() - start) < args.duration:
                res, hdr_hex, hdr_l, jpg_l, tot_l = send_frame(fd, hdr_w, 1920, jpeg_bytes)
                time.sleep(0.8)
                
            print(f"{name:<27} | {hdr_w}x1920    | {sof_w}x{sof_h:<5} | {jpg_l:<10} | {tot_l:<10} | OK ({tot_l}B)")
            time.sleep(0.5)
            
        fcntl.ioctl(fd, USBDEVFS_RELEASEINTERFACE, struct.pack('I', 1))
    finally:
        os.close(fd)

if __name__ == "__main__":
    main()
