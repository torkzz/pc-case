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

def send_frame(fd, width, height, jpeg_bytes, endpoint=0x02, timeout_ms=2000):
    # Header: Magic=0x0008100A, W, H, Stride=0, Flag=1
    header = struct.pack("<IHHHH", MSDISPLAY_MAGIC_SIGNATURE, width, height, 0, 1)
    payload = header + jpeg_bytes
    
    data_buf = ctypes.create_string_buffer(payload)
    bulk_req = struct.pack('IIIIPI', endpoint, len(payload), timeout_ms, 0, ctypes.addressof(data_buf), 0)
    res = fcntl.ioctl(fd, USBDEVFS_BULK, bulk_req)
    return res, len(header), len(jpeg_bytes), len(payload)

def build_test_a_480x1920_3col():
    width, height = 480, 1920
    img = Image.new('RGB', (width, height), (0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    colors_grid = [
        [(255, 0, 0),   (0, 255, 0),   (0, 0, 255)],     # Red, Green, Blue
        [(255, 255, 0), (0, 255, 255), (255, 0, 255)],   # Yellow, Cyan, Magenta
        [(255, 128, 0), (0, 255, 128), (128, 0, 255)],   # Orange, Mint, Purple
        [(128, 0, 0),   (0, 128, 0),   (0, 0, 128)]      # Dark Red, Dark Green, Dark Blue
    ]
    col_w, row_h = 160, 480
    for row_idx in range(4):
        y0, y1 = row_idx * row_h, (row_idx + 1) * row_h
        for col_idx in range(3):
            x0, x1 = col_idx * col_w, (col_idx + 1) * col_w
            c = colors_grid[row_idx][col_idx]
            draw.rectangle([x0, y0, x1 - 1, y1 - 1], fill=c)
            
    jpg_path = "/tmp/test_a_480x1920.jpg"
    img.save(jpg_path, "JPEG", quality=95, subsampling=0)
    with open(jpg_path, 'rb') as f:
        return width, height, f.read()

def build_test_b_640x1920_4col():
    width, height = 640, 1920
    img = Image.new('RGB', (width, height), (0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    colors_grid = [
        [(255, 0, 0),   (0, 255, 0),   (0, 0, 255),   (255, 255, 255)],
        [(255, 255, 0), (0, 255, 255), (255, 0, 255), (128, 128, 128)],
        [(255, 128, 0), (0, 255, 128), (128, 0, 255), (255, 255, 128)],
        [(128, 0, 0),   (0, 128, 0),   (0, 0, 128),   (200, 200, 200)]
    ]
    col_w, row_h = 160, 480
    for row_idx in range(4):
        y0, y1 = row_idx * row_h, (row_idx + 1) * row_h
        for col_idx in range(4):
            x0, x1 = col_idx * col_w, (col_idx + 1) * col_w
            c = colors_grid[row_idx][col_idx]
            draw.rectangle([x0, y0, x1 - 1, y1 - 1], fill=c)
            
    jpg_path = "/tmp/test_b_640x1920.jpg"
    img.save(jpg_path, "JPEG", quality=95, subsampling=0)
    with open(jpg_path, 'rb') as f:
        return width, height, f.read()

def build_test_c_fourth_col_isolation():
    # 640x1920: X=0..479 Black, X=480..639 Bright White
    width, height = 640, 1920
    img = Image.new('RGB', (width, height), (0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw.rectangle([480, 0, 639, 1919], fill=(255, 255, 255))
    jpg_path = "/tmp/test_c_isolation.jpg"
    img.save(jpg_path, "JPEG", quality=95, subsampling=0)
    with open(jpg_path, 'rb') as f:
        return width, height, f.read()

def build_test_d_first_col_isolation():
    # 640x1920: X=0..159 Bright White, X=160..639 Black
    width, height = 640, 1920
    img = Image.new('RGB', (width, height), (0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw.rectangle([0, 0, 159, 1919], fill=(255, 255, 255))
    jpg_path = "/tmp/test_d_isolation.jpg"
    img.save(jpg_path, "JPEG", quality=95, subsampling=0)
    with open(jpg_path, 'rb') as f:
        return width, height, f.read()

def build_test_e_sweep_frame(block_index):
    # block_index 0: X=0..159 RED
    # block_index 1: X=160..319 GREEN
    # block_index 2: X=320..479 BLUE
    # block_index 3: X=480..639 WHITE
    width, height = 640, 1920
    img = Image.new('RGB', (width, height), (0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    col_w = 160
    x0, x1 = block_index * col_w, (block_index + 1) * col_w
    colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 255)]
    draw.rectangle([x0, 0, x1 - 1, 1919], fill=colors[block_index])
    
    jpg_path = f"/tmp/test_e_sweep_{block_index}.jpg"
    img.save(jpg_path, "JPEG", quality=95, subsampling=0)
    with open(jpg_path, 'rb') as f:
        return width, height, f.read()

def run_test_sequence(test_name, build_fn, duration_sec=5.0, interval_sec=1.0):
    dev_path = find_device()
    if not dev_path:
        print(f"[ERROR] USB device 33c3:f101 not found for {test_name}.")
        return
        
    unbind_cdc_acm()
    w, h, jpeg_bytes = build_fn()
    
    fd = os.open(dev_path, os.O_RDWR)
    try:
        fcntl.ioctl(fd, USBDEVFS_CLAIMINTERFACE, struct.pack('I', 1))
        print(f"\n========================================================")
        print(f"  RUNNING {test_name}: Header ({w}x{h}), JPEG ({len(jpeg_bytes)} B)")
        print(f"========================================================")
        
        start_time = time.monotonic()
        seq = 1
        while (time.monotonic() - start_time) < duration_sec:
            tx_res, hdr_len, jpg_len, tot_len = send_frame(fd, w, h, jpeg_bytes)
            print(f"  [{test_name}] Frame #{seq:02d} | W={w} H={h} | Header={hdr_len}B JPG={jpg_len}B Total={tot_len}B | Tx Status: {tx_res}B OK")
            seq += 1
            time.sleep(interval_sec)
            
        fcntl.ioctl(fd, USBDEVFS_RELEASEINTERFACE, struct.pack('I', 1))
    finally:
        os.close(fd)

def main():
    parser = argparse.ArgumentParser(description="LCD Geometry Investigation Suite")
    parser.add_argument('--test', type=str, choices=['A', 'B', 'C', 'D', 'E', 'ALL'], default='ALL')
    parser.add_argument('--duration', type=float, default=4.0)
    args = parser.parse_args()
    
    if args.test in ('A', 'ALL'):
        run_test_sequence("TEST A (480x1920 3-Col)", build_test_a_480x1920_3col, args.duration)
        time.sleep(1.0)
        
    if args.test in ('B', 'ALL'):
        run_test_sequence("TEST B (640x1920 4-Col)", build_test_b_640x1920_4col, args.duration)
        time.sleep(1.0)
        
    if args.test in ('C', 'ALL'):
        run_test_sequence("TEST C (Fourth Col Isolation X=480..639)", build_test_c_fourth_col_isolation, args.duration)
        time.sleep(1.0)
        
    if args.test in ('D', 'ALL'):
        run_test_sequence("TEST D (First Col Isolation X=0..159)", build_test_d_first_col_isolation, args.duration)
        time.sleep(1.0)
        
    if args.test in ('E', 'ALL'):
        for i in range(4):
            block_names = ["X=0..159 (RED)", "X=160..319 (GREEN)", "X=320..479 (BLUE)", "X=480..639 (WHITE)"]
            name = f"TEST E Sweep #{i+1} ({block_names[i]})"
            fn = lambda idx=i: build_test_e_sweep_frame(idx)
            run_test_sequence(name, fn, args.duration)
            time.sleep(1.0)

if __name__ == "__main__":
    main()
