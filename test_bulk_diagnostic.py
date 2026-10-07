#!/usr/bin/env python3
import os
import sys
import time
import fcntl
import termios
import struct
import ctypes
from PIL import Image

from msdisplay.protocol import build_frame_payload
from msdisplay.jpeg import create_test_grid_jpeg, encode_jpeg
from msdisplay.usb import find_target_usb_device, find_sysfs_device_name

TIOCMBIS = 0x5416
TIOCM_DTR = 0x002
TIOCM_RTS = 0x004

USBDEVFS_CLAIMINTERFACE = 0x8004550F
USBDEVFS_RELEASEINTERFACE = 0x80045510
USBDEVFS_BULK = 0xC0185502

# 1. Wake device via /dev/ttyACM0
tty = '/dev/ttyACM0'
print(f"[STEP 1] Checking CDC ACM serial port {tty}...")
if os.path.exists(tty):
    try:
        fd_tty = os.open(tty, os.O_RDWR | os.O_NOCTTY | os.O_NONBLOCK)
        attr = termios.tcgetattr(fd_tty)
        attr[0] &= ~(termios.IGNBRK | termios.BRKINT | termios.PARMRK | termios.ISTRIP | termios.INLCR | termios.IGNCR | termios.ICRNL | termios.IXON)
        attr[1] &= ~termios.OPOST
        attr[2] &= ~(termios.PARENB | termios.CSTOPB | termios.CRTSCTS)
        attr[2] |= (termios.CS8 | termios.CREAD | termios.CLOCAL)
        attr[3] &= ~(termios.ISIG | termios.ICANON | termios.ECHO | termios.ECHOE | termios.ECHOK | termios.ECHONL | termios.IEXTEN)
        attr[4] = termios.B115200
        attr[5] = termios.B115200
        termios.tcsetattr(fd_tty, termios.TCSANOW, attr)

        lines = struct.pack('I', TIOCM_DTR | TIOCM_RTS)
        fcntl.ioctl(fd_tty, TIOCMBIS, lines)
        time.sleep(0.1)

        wake_pkt = bytes.fromhex('41481004008085444d49')
        n_w = os.write(fd_tty, wake_pkt)
        termios.tcdrain(fd_tty)
        print(f"    Wrote {n_w} bytes wake packet to {tty}.")
        os.close(fd_tty)
    except Exception as e:
        print(f"    [WARN] Serial wake failed: {e}")
else:
    print(f"    [WARN] {tty} not present.")

# 2. Unbind 1.1 from cdc_acm
sysfs_name = find_sysfs_device_name() or "1-9"
unbind_path = "/sys/bus/usb/drivers/cdc_acm/unbind"
print(f"[STEP 2] Unbinding {sysfs_name}:1.1 from cdc_acm...")
if os.path.exists(unbind_path):
    try:
        with open(unbind_path, 'w') as f:
            f.write(f"{sysfs_name}:1.1\n")
        print("    Unbound 1.1 successfully.")
    except Exception as e:
        print(f"    Unbind note: {e}")

# 3. Find USB node and open
dev_node = find_target_usb_device()
print(f"[STEP 3] Target USB device node: {dev_node}")
if not dev_node:
    print("[ERROR] USB device node not found!")
    sys.exit(1)

fd_usb = os.open(dev_node, os.O_RDWR)
print(f"    Opened {dev_node} as fd={fd_usb}.")

try:
    # 4. Claim Interface 1
    print("[STEP 4] Claiming Interface 1 via USBDEVFS_CLAIMINTERFACE (0x8004550F)...")
    iface_buf = struct.pack("I", 1)
    res_claim = fcntl.ioctl(fd_usb, USBDEVFS_CLAIMINTERFACE, iface_buf)
    print(f"    Interface 1 claimed. ioctl result = {res_claim}")

    # 5. Generate Test JPEG & Build Payload
    print("[STEP 5] Generating test pattern JPEG (460x1920)...")
    jpg_bytes = create_test_grid_jpeg(460, 1920)
    print(f"    JPEG size: {len(jpg_bytes)} bytes.")
    payload = build_frame_payload(jpg_bytes, 460, 1920)
    print(f"    Frame payload total size: {len(payload)} bytes (12-byte header + {len(jpg_bytes)} JPEG).")

    # 6. Perform Bulk OUT Transfer to EP 0x02
    print("[STEP 6] Executing USBDEVFS_BULK (0xC0185502) to Endpoint 0x02...")
    endpoint = 0x02
    timeout_ms = 2000
    data_buf = ctypes.create_string_buffer(payload)
    
    # 24-byte struct usbdevfs_bulktransfer on 64-bit Linux: endpoint(I), len(I), timeout(I), pad(4B alignment), data(P)
    bulk_req = struct.pack('IIIP', endpoint, len(payload), timeout_ms, ctypes.addressof(data_buf))
    print(f"    usbdevfs_bulktransfer struct size: {len(bulk_req)} bytes.")

    t0 = time.monotonic()
    ret_bulk = fcntl.ioctl(fd_usb, USBDEVFS_BULK, bulk_req)
    dt = time.monotonic() - t0

    print(f"    [BULK TX RESULT] ioctl returned {ret_bulk} (bytes transferred) in {dt:.3f}s.")
    if ret_bulk == len(payload):
        print("    [SUCCESS] Transmitted ALL frame bytes cleanly!")
    else:
        print(f"    [PARTIAL TRANSMISSION] Transmitted {ret_bulk} / {len(payload)} bytes.")

finally:
    print("[STEP 7] Releasing Interface 1 and closing device...")
    try:
        fcntl.ioctl(fd_usb, USBDEVFS_RELEASEINTERFACE, iface_buf)
    except Exception:
        pass
    os.close(fd_usb)
    print("    Diagnostic complete.")
