#!/usr/bin/env python3
import array
import fcntl
import os
import struct
import sys
import time

# ioctl constants for hidraw
# HIDIOCGRAWNAME(len): _IOC(_IOC_READ, 'H', 0x04, len) -> 0x80004804 | (len << 16) ... 
# calculate IOC values:
# _IOC(dir, type, nr, size)
# dir: READ=2, WRITE=1, READ|WRITE=3
# type: 'H' (0x48)
def _IOC(dir_, type_, nr, size):
    return (dir_ << 30) | (ord(type_) << 8) | nr | (size << 16)

HIDIOCGRAWINFO = _IOC(2, 'H', 0x03, 8)  # 2 bytes bustype, 2 bytes vendor, 2 bytes product, 2 bytes pad
HIDIOCGRDESCSIZE = _IOC(2, 'H', 0x01, 4)
# HIDIOCGRDESC: struct hidraw_report_descriptor { __u32 size; __u8 value[4096]; } -> size = 4 + 4096 = 4100
HIDIOCGRDESC = _IOC(2, 'H', 0x02, 4100)
# HIDIOCGFEATURE(len): _IOC(_IOC_READ|_IOC_WRITE, 'H', 0x07, len) -> dir=3
def HIDIOCGFEATURE(length):
    return _IOC(3, 'H', 0x07, length)

HIDRAW_PATH = "/dev/hidraw2"

def get_raw_name(fd):
    buf = bytearray(256)
    # HIDIOCGRAWNAME(len)
    cmd = _IOC(2, 'H', 0x04, len(buf))
    try:
        res = fcntl.ioctl(fd, cmd, buf)
        return buf[:res].decode('utf-8', errors='replace').rstrip('\x00')
    except Exception as e:
        return f"Error: {e}"

def get_raw_info(fd):
    buf = bytearray(8)
    try:
        fcntl.ioctl(fd, HIDIOCGRAWINFO, buf)
        bustype, vendor, product = struct.unpack("<IHH", buf[:8])
        return bustype, vendor, product
    except Exception as e:
        return None, None, None

def get_report_descriptor(fd):
    try:
        buf = bytearray(4)
        fcntl.ioctl(fd, HIDIOCGRDESCSIZE, buf)
        desc_size = struct.unpack("<I", buf)[0]
        desc_buf = bytearray(4 + desc_size)
        struct.pack_into("<I", desc_buf, 0, desc_size)
        fcntl.ioctl(fd, HIDIOCGRDESC, desc_buf)
        return bytes(desc_buf[4:4+desc_size])
    except Exception as e:
        try:
            with open("/sys/class/hidraw/hidraw2/device/report_descriptor", "rb") as f:
                return f.read()
        except Exception as e2:
            print(f"Failed to read report descriptor: ioctl({e}), sysfs({e2})")
            return b""

def parse_hid_descriptor(desc):
    print("--- HID DESCRIPTOR PARSER ---")
    i = 0
    indent = ""
    report_ids = set()
    usage_pages = []
    usages = []

    while i < len(desc):
        b = desc[i]
        bSize = b & 0x03
        if bSize == 3:
            bSize = 4
        bType = (b >> 2) & 0x03
        bTag = (b >> 4) & 0x0F

        data_bytes = desc[i+1 : i+1+bSize]
        val = int.from_bytes(data_bytes, byteorder='little', signed=False) if data_bytes else 0

        # Tags
        tag_names = {
            (0, 0): "Usage Page", (0, 1): "Logical Min", (0, 2): "Logical Max",
            (0, 3): "Physical Min", (0, 4): "Physical Max", (0, 7): "Report Size",
            (0, 8): "Report ID", (0, 9): "Report Count",
            (1, 0): "Usage", (1, 1): "Usage Min", (1, 2): "Usage Max",
            (2, 0): "Collection", (2, 1): "End Collection",
            (2, 8): "Input", (2, 9): "Output", (2, 11): "Feature"
        }

        tag_name = tag_names.get((bType, bTag), f"Type={bType} Tag={bTag}")
        if (bType, bTag) == (0, 8): # Report ID
            report_ids.add(val)
        if (bType, bTag) == (0, 0): # Usage Page
            usage_pages.append(val)
        if (bType, bTag) == (1, 0): # Usage
            usages.append(val)

        hex_data = ' '.join(f"{x:02x}" for x in desc[i:i+1+bSize])
        print(f"[{i:03d}] {hex_data:<15} | {tag_name}: {val} (0x{val:x})")
        i += 1 + bSize

    print(f"\nDiscovered Report IDs: {sorted(list(report_ids)) if report_ids else 'None (implicit 0)'}")
    print(f"Discovered Usage Pages: {[hex(x) for x in usage_pages]}")
    print(f"Discovered Usages: {[hex(x) for x in usages]}")

def perform_get_feature(fd, report_id=0, payload_len=64):
    # Buffer structure: report_id byte + payload_len bytes
    buf = bytearray(1 + payload_len)
    buf[0] = report_id & 0xFF
    cmd = HIDIOCGFEATURE(len(buf))
    try:
        res = fcntl.ioctl(fd, cmd, buf)
        return bytes(buf[:res])
    except Exception as e:
        print(f"GET_FEATURE (Report ID {report_id}) failed: {e}")
        return None

def print_payload(data):
    if not data:
        return
    report_id = data[0]
    payload = data[1:]
    print(f"Report ID: {report_id:02x} | Length: {len(payload)} bytes")
    print("Offset  Hex                                               ASCII")
    print("-" * 68)
    for off in range(0, len(payload), 16):
        chunk = payload[off:off+16]
        hex_str = ' '.join(f"{b:02x}" for b in chunk)
        ascii_str = ''.join(chr(b) if 32 <= b <= 126 else '.' for b in chunk)
        print(f"{off:04x}:   {hex_str:<47}  {ascii_str}")

def main():
    print(f"Opening {HIDRAW_PATH} read-only...")
    try:
        fd = os.open(HIDRAW_PATH, os.O_RDONLY)
    except Exception as e:
        print(f"CRITICAL: Failed to open {HIDRAW_PATH}: {e}")
        sys.exit(1)

    try:
        dev_name = get_raw_name(fd)
        bustype, vid, pid = get_raw_info(fd)
        print(f"Device Name : {dev_name}")
        print(f"VID:PID     : {vid:04x}:{pid:04x} (BusType: {bustype})")
        print()

        desc = get_report_descriptor(fd)
        if desc:
            parse_hid_descriptor(desc)
        else:
            print("No report descriptor available.")

        print("\n=== STABILITY TEST: 10x GET_FEATURE (Implicit Report ID 0) ===")
        samples = []
        for s in range(10):
            ts = time.strftime("%H:%M:%S.%MS")
            res = perform_get_feature(fd, report_id=0, payload_len=64)
            samples.append(res)
            print(f"\nSample #{s+1} at {ts}:")
            if res:
                print_payload(res)
            else:
                print("Failed read.")
            time.sleep(0.1)

        print("\n--- BYTE-BY-BYTE COMPARISON ---")
        if all(s == samples[0] for s in samples):
            print("RESULT: Response is 100% STABLE across all 10 samples.")
        else:
            print("RESULT: Response INSTABILITY detected!")
            for i in range(1, len(samples)):
                if samples[i] != samples[0]:
                    print(f"Sample {i+1} differs from Sample 1!")

    finally:
        os.close(fd)

if __name__ == "__main__":
    main()
