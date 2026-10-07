#!/usr/bin/env python3
import os
import sys
import time
import fcntl
import termios
import struct
import ctypes
from PIL import Image

from msdisplay.protocol import pack_msdisplay_header
from msdisplay.jpeg import create_test_grid_jpeg, encode_jpeg
from msdisplay.usb import find_target_usb_device, find_sysfs_device_name

TIOCMBIS = 0x5416
TIOCM_DTR = 0x002
TIOCM_RTS = 0x004

USBDEVFS_CLAIMINTERFACE = 0x8004550F
USBDEVFS_RELEASEINTERFACE = 0x80045510
USBDEVFS_BULK = 0xC0185502

# 1. Wake via CDC ACM serial
tty = '/dev/ttyACM0'
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
        os.write(fd_tty, wake_pkt)
        termios.tcdrain(fd_tty)
        print("Wrote 10-byte wake packet to ttyACM0.")
        os.close(fd_tty)
    except Exception as e:
        print("Serial wake note:", e)

# 2. Unbind 1.1 from cdc_acm
sysfs_name = find_sysfs_device_name() or "1-9"
unbind_path = "/sys/bus/usb/drivers/cdc_acm/unbind"
if os.path.exists(unbind_path):
    try:
        with open(unbind_path, 'w') as f:
            f.write(f"{sysfs_name}:1.1\n")
    except Exception:
        pass

dev_node = find_target_usb_device()
if not dev_node:
    print("USB dev node not found!")
    sys.exit(1)

fd_usb = os.open(dev_node, os.O_RDWR)
iface_buf = struct.pack("I", 1)
fcntl.ioctl(fd_usb, USBDEVFS_CLAIMINTERFACE, iface_buf)

try:
    # Test 1: Header 480x1920 (stride 480, flag 1)
    print("\n--- TEST 1: Sending 480x1920 JPEG with Stride 480 ---")
    hdr1 = pack_msdisplay_header(480, 1920, 480, 1)
    print("Header 1 hex:", hdr1.hex())
    jpg1 = create_test_grid_jpeg(480, 1920)
    payload1 = hdr1 + jpg1
    buf1 = ctypes.create_string_buffer(payload1)
    req1 = bytearray(struct.pack('IIIP', 0x02, len(payload1), 2000, ctypes.addressof(buf1)))
    ret1 = fcntl.ioctl(fd_usb, USBDEVFS_BULK, req1)
    print(f"Transmitted {ret1} / {len(payload1)} bytes for 480x1920 payload.")

    time.sleep(2.0)

    # Test 2: Header 460x1920 (stride 0, flag 1)
    print("\n--- TEST 2: Sending 460x1920 JPEG with Stride 0 ---")
    hdr2 = pack_msdisplay_header(460, 1920, 0, 1)
    print("Header 2 hex:", hdr2.hex())
    jpg2 = create_test_grid_jpeg(460, 1920)
    payload2 = hdr2 + jpg2
    buf2 = ctypes.create_string_buffer(payload2)
    req2 = bytearray(struct.pack('IIIP', 0x02, len(payload2), 2000, ctypes.addressof(buf2)))
    ret2 = fcntl.ioctl(fd_usb, USBDEVFS_BULK, req2)
    print(f"Transmitted {ret2} / {len(payload2)} bytes for 460x1920 payload.")

finally:
    try:
        fcntl.ioctl(fd_usb, USBDEVFS_RELEASEINTERFACE, iface_buf)
    except Exception:
        pass
    os.close(fd_usb)
