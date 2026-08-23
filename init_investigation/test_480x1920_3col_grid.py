import os
import sys
import time
import struct
import fcntl
import ctypes
from PIL import Image, ImageDraw

USBDEVFS_CLAIMINTERFACE = 0x8004550F
USBDEVFS_RELEASEINTERFACE = 0x80045510
USBDEVFS_BULK = 0xC0185502

WIDTH = 480
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
    # MSDisplay Header: W=480 (0x01E0), H=1920 (0x0780), Stride=0, Flag=1
    header = struct.pack("<IHHHH", MSDISPLAY_MAGIC_SIGNATURE, WIDTH, HEIGHT, 0, 1)
    payload = header + jpeg_bytes
    
    data_buf = ctypes.create_string_buffer(payload)
    bulk_req = struct.pack('IIIIPI', 0x02, len(payload), 2000, 0, ctypes.addressof(data_buf), 0)
    return fcntl.ioctl(fd, USBDEVFS_BULK, bulk_req)

def generate_3col_grid_jpeg():
    jpg_path = "/tmp/480x1920_3col_grid.jpg"
    
    img = Image.new('RGB', (WIDTH, HEIGHT), (0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # 3 Vertical Columns across 480px width (each 160px wide)
    # 4 Horizontal Rows across 1920px height (each 480px tall)
    colors_grid = [
        # Row 0 (Y: 0 - 480)
        [(255, 0, 0),   (0, 255, 0),   (0, 0, 255)],     # Red, Green, Blue
        # Row 1 (Y: 480 - 960)
        [(255, 255, 0), (0, 255, 255), (255, 0, 255)],   # Yellow, Cyan, Magenta
        # Row 2 (Y: 960 - 1440)
        [(255, 128, 0), (0, 255, 128), (128, 0, 255)],   # Orange, Mint, Purple
        # Row 3 (Y: 1440 - 1920)
        [(128, 0, 0),   (0, 128, 0),   (0, 0, 128)]      # Dark Red, Dark Green, Dark Blue
    ]
    
    col_w = 160
    row_h = 480
    
    for row_idx in range(4):
        y0 = row_idx * row_h
        y1 = (row_idx + 1) * row_h
        for col_idx in range(3):
            x0 = col_idx * col_w
            x1 = (col_idx + 1) * col_w
            c = colors_grid[row_idx][col_idx]
            # Non-overlapping rectangle boundary
            draw.rectangle([x0, y0, x1 - 1, y1 - 1], fill=c)
            
    img.save(jpg_path, "JPEG", quality=95, subsampling=0)
    
    with open(jpg_path, 'rb') as f:
        return f.read()

def main():
    dev_path = find_device()
    if not dev_path:
        print("[ERROR] Device 33c3:f101 not found.")
        sys.exit(1)
        
    unbind_cdc_acm()
    jpeg_bytes = generate_3col_grid_jpeg()
    print(f"=== 480x1920 3-Column x 4-Row Test (JPEG size: {len(jpeg_bytes)} B) ===")
    print("  Header Hex: 0a 10 08 00 e0 01 80 07 00 00 01 00")
    print("  Column 1 (Left 0-160px)  : RED, Yellow, Orange, Dark Red")
    print("  Column 2 (Mid  160-320px): GREEN, Cyan, Mint, Dark Green")
    print("  Column 3 (Right 320-480px): BLUE, Magenta, Purple, Dark Blue")
    
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
