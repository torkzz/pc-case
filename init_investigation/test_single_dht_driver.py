import os
import sys
import time
import struct
import fcntl
import ctypes
from PIL import Image, ImageDraw, ImageFont

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

def combine_dht_markers(jpeg_bytes):
    """
    Merges all separate 0xFF 0xC4 (DHT) markers into a SINGLE 0xFF 0xC4 marker.
    """
    pos = 0
    new_bytes = bytearray()
    combined_dht_payload = bytearray()
    
    while pos < len(jpeg_bytes):
        if jpeg_bytes[pos] != 0xFF:
            new_bytes.append(jpeg_bytes[pos])
            pos += 1
            continue
            
        marker = jpeg_bytes[pos+1]
        if marker in (0xD8, 0xD9): # SOI, EOI
            new_bytes.extend(jpeg_bytes[pos:pos+2])
            pos += 2
            continue
            
        length = struct.unpack('>H', jpeg_bytes[pos+2:pos+4])[0]
        if marker == 0xC4: # DHT
            # Accumulate DHT table payload (excluding length bytes)
            dht_payload = jpeg_bytes[pos+4:pos+2+length]
            combined_dht_payload.extend(dht_payload)
            pos += 2 + length
            continue
        elif marker == 0xDA: # SOS
            # Insert the single combined DHT marker before SOS!
            dht_len = len(combined_dht_payload) + 2
            new_bytes.extend(b'\xff\xc4')
            new_bytes.extend(struct.pack('>H', dht_len))
            new_bytes.extend(combined_dht_payload)
            
            # Append remaining SOS and scan data
            new_bytes.extend(jpeg_bytes[pos:])
            break
        else:
            new_bytes.extend(jpeg_bytes[pos:pos+2+length])
            pos += 2 + length
            
    return bytes(new_bytes)

def create_single_dht_frame(text="HELLO WORLD"):
    img = Image.new('RGB', (640, 1920), (10, 18, 32))
    draw = ImageDraw.Draw(img)
    
    draw.rectangle([10, 10, 630, 1910], outline=(0, 200, 255), width=4)
    
    try:
        font_lg = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 48)
        font_md = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 36)
    except Exception:
        font_lg = font_md = ImageFont.load_default()
        
    draw.rectangle([30, 40, 610, 440], fill=(20, 35, 60), outline=(0, 200, 255), width=3)
    draw.text((60, 80), "SINGLE DHT MONITOR", fill=(0, 200, 255), font=font_md)
    draw.text((60, 200), text, fill=(255, 255, 255), font=font_lg)
    
    draw.rectangle([30, 480, 610, 880], fill=(20, 60, 40), outline=(0, 255, 120), width=3)
    draw.text((60, 520), "COMBINED DHT TABLE", fill=(0, 255, 120), font=font_md)
    draw.text((60, 640), "STATUS: OK", fill=(255, 255, 255), font=font_lg)
    
    draw.rectangle([30, 920, 610, 1320], fill=(60, 40, 20), outline=(255, 160, 0), width=3)
    draw.text((60, 960), "MCU SAMPLING", fill=(255, 160, 0), font=font_md)
    draw.text((60, 1080), "SINGLE FFC4 MARKER", fill=(255, 255, 255), font=font_lg)
    
    draw.rectangle([30, 1360, 610, 1860], fill=(50, 20, 60), outline=(220, 100, 255), width=3)
    draw.text((60, 1400), "VMAX LINUX NATIVE", fill=(220, 100, 255), font=font_md)
    draw.text((60, 1520), "640x1920", fill=(255, 255, 255), font=font_lg)
    
    out_jpg = "/tmp/single_dht.jpg"
    img.save(out_jpg, format="JPEG", quality=75, subsampling=0, optimize=False)
    
    with open(out_jpg, 'rb') as f:
        raw_bytes = f.read()
        
    single_dht_jpeg = combine_dht_markers(raw_bytes)
    return single_dht_jpeg

def main():
    dev_path = find_device()
    if not dev_path:
        print("Device 33c3:f101 not found")
        sys.exit(1)
        
    unbind_cdc_acm()
    
    jpeg_bytes = create_single_dht_frame("HELLO WORLD")
    print(f"=== Combined Single DHT Marker Test ({len(jpeg_bytes)} B JPEG) ===")
    
    # Inspect DHT count
    dht_count = jpeg_bytes.count(b'\xff\xc4')
    idx_dht = jpeg_bytes.find(b'\xff\xc4')
    dht_len = int.from_bytes(jpeg_bytes[idx_dht+2:idx_dht+4], 'big')
    print(f"DHT Marker count: {dht_count}, Combined DHT Len: {dht_len} bytes")
    
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
