#!/usr/bin/env python3
import fcntl
import os
import struct
import sys
import time

def _IOC(dir_, type_, nr, size):
    return (dir_ << 30) | (ord(type_) << 8) | nr | (size << 16)

HIDIOCGRAWINFO = _IOC(2, 'H', 0x03, 8)
HIDIOCGRDESCSIZE = _IOC(2, 'H', 0x01, 4)
HIDIOCGRDESC = _IOC(2, 'H', 0x02, 4100)

def HIDIOCGFEATURE(length):
    return _IOC(3, 'H', 0x07, length)

def main():
    dev_path = "/dev/hidraw2"
    if len(sys.argv) > 1:
        dev_path = sys.argv[1]

    print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Starting Safe Read-Only Probe on {dev_path}")
    
    try:
        fd = os.open(dev_path, os.O_RDONLY)
    except Exception as e:
        print(f"ERROR: Cannot open {dev_path}: {e}")
        sys.exit(1)

    try:
        # Get VID / PID
        buf = bytearray(8)
        fcntl.ioctl(fd, HIDIOCGRAWINFO, buf)
        bustype, vendor, product = struct.unpack("<IHH", buf[:8])
        print(f"Device VID:PID = {vendor:04x}:{product:04x}")
        if vendor != 0x05ac or product != 0x0256:
            print("WARNING: Device VID:PID does not match expected SONiX 05ac:0256!")

        # Perform 30 second GET_FEATURE sampling loop
        print("\nSampling GET_FEATURE (64-byte payload) for 30 seconds... (READ-ONLY)")
        start_time = time.time()
        sample_count = 0
        all_zeros = True
        previous_payload = None
        changed = False

        while time.time() - start_time < 30:
            sample_count += 1
            ts = time.strftime("%H:%M:%S")
            
            # Buffer: 1 byte report ID + 64 bytes payload
            feat_buf = bytearray(65)
            feat_buf[0] = 0x00 # Report ID 0
            cmd = HIDIOCGFEATURE(len(feat_buf))
            
            try:
                res = fcntl.ioctl(fd, cmd, feat_buf)
                payload = bytes(feat_buf[1:res])
                hex_str = ' '.join(f"{b:02x}" for b in payload[:16])
                
                if any(b != 0 for b in payload):
                    all_zeros = False
                    
                if previous_payload is not None and payload != previous_payload:
                    changed = True
                    print(f"[{ts}] Sample #{sample_count}: CHANGED! Payload: {hex_str}...")
                else:
                    print(f"[{ts}] Sample #{sample_count}: {hex_str}... (64 bytes total)")
                
                previous_payload = payload
            except Exception as e:
                print(f"[{ts}] Sample #{sample_count}: GET_FEATURE failed: {e}")

            time.sleep(3.0)

        print("\n--- PROBE SUMMARY ---")
        print(f"Total samples taken: {sample_count}")
        print(f"Payload all zeros  : {all_zeros}")
        print(f"Payload changed    : {changed}")

    finally:
        os.close(fd)

if __name__ == "__main__":
    main()
