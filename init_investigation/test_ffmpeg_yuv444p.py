import os
import sys
import time
import struct
import fcntl
import ctypes
import subprocess

USBDEVFS_CLAIMINTERFACE = 0x8004550F
USBDEVFS_RELEASEINTERFACE = 0x80045510
USBDEVFS_BULK = 0xC0185502

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

def generate_ffmpeg_yuv444p_jpeg(text="HELLO WORLD"):
    out_path = "/tmp/ffmpeg_yuv444p.jpg"
    vf_filter = (
        f"drawbox=y=0:color=black:t=fill,"
        f"drawbox=x=20:y=20:w=600:h=1880:color=cyan:t=4,"
        f"drawbox=x=30:y=40:w=580:h=400:color=blue@0.6:t=fill,"
        f"drawtext=text='{text}':fontcolor=white:fontsize=50:x=60:y=180,"
        f"drawbox=x=30:y=480:w=580:h=400:color=green@0.6:t=fill,"
        f"drawtext=text='STATUS OK':fontcolor=white:fontsize=50:x=60:y=620,"
        f"drawbox=x=30:y=920:w=580:h=400:color=orange@0.6:t=fill,"
        f"drawtext=text='NO SPLITTING':fontcolor=white:fontsize=50:x=60:y=1060,"
        f"drawbox=x=30:y=1360:w=580:h=480:color=purple@0.6:t=fill,"
        f"drawtext=text='640x1920':fontcolor=white:fontsize=50:x=60:y=1500"
    )
    cmd = [
        'ffmpeg', '-y', '-f', 'lavfi', '-i', 'color=c=black:s=640x1920',
        '-vf', vf_filter,
        '-vframes', '1',
        '-pix_fmt', 'yuv444p',
        out_path
    ]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    with open(out_path, 'rb') as f:
        return f.read()

def main():
    dev_path = find_device()
    if not dev_path:
        print("Device 33c3:f101 not found")
        sys.exit(1)
        
    unbind_cdc_acm()
    
    jpeg_bytes = generate_ffmpeg_yuv444p_jpeg("HELLO WORLD")
    print(f"=== FFmpeg YUV444p Test ({len(jpeg_bytes)} B JPEG) ===")
    
    # Analyze header
    idx_sof = jpeg_bytes.find(b'\xff\xc0')
    if idx_sof != -1:
        sof_len = int.from_bytes(jpeg_bytes[idx_sof+2:idx_sof+4], 'big')
        print(f"SOF0 hex: {jpeg_bytes[idx_sof:idx_sof+2+sof_len].hex()}")
        
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
