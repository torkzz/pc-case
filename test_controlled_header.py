#!/usr/bin/env python3
import os
import sys
import time
import fcntl
import termios
import struct
import ctypes

TIOCMBIS = 0x5416
TIOCM_DTR = 0x002
TIOCM_RTS = 0x004

USBDEVFS_CLAIMINTERFACE = 0x8004550F
USBDEVFS_RELEASEINTERFACE = 0x80045510
USBDEVFS_BULK = 0xC0185502

def pack_msdisplay_header(width, height, stride, flag):
    return struct.pack("<IHHHH", 0x0008100A, width, height, stride, flag)

def main():
    print("=== CONTROLLED HARDWARE HEADER TEST ===")

    # 1. CDC ACM Wake Sequence
    tty = '/dev/ttyACM0'
    print(f"\n[1] Checking serial port {tty}...")
    if not os.path.exists(tty):
        print(f"[ERROR] {tty} does not exist!")
        sys.exit(1)

    print(f"[2] Opening {tty} with raw 115200 8N1 + DTR/RTS...")
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
    print(f"    CDC wake packet sent ({n_w}/10 bytes).")
    os.close(fd_tty)

    time.sleep(0.2)

    # 2. Unbind Interface 1.1 only
    sysfs_name = "1-9"
    unbind_path = "/sys/bus/usb/drivers/cdc_acm/unbind"
    if os.path.exists(unbind_path):
        try:
            with open(unbind_path, 'w') as f:
                f.write(f"{sysfs_name}:1.1\n")
            print("    Unbound 1-9:1.1 from cdc_acm.")
        except Exception as e:
            print("    Unbind 1.1 note:", e)

    # 3. Open USB device node
    dev_node = "/dev/bus/usb/001/006"
    fd_usb = os.open(dev_node, os.O_RDWR)
    iface_buf = struct.pack("I", 1)
    fcntl.ioctl(fd_usb, USBDEVFS_CLAIMINTERFACE, iface_buf)
    print(f"    Claimed Interface 1 on {dev_node}.")

    try:
        from msdisplay.jpeg import create_test_grid_jpeg

        # Test A: Current Header (460x1920, stride=0, flag=1)
        print("\n==========================================")
        print("  TEST A: Current Header (460x1920, Stride=0)")
        print("==========================================")
        hdr_a = pack_msdisplay_header(460, 1920, 0, 1)
        jpg_a = create_test_grid_jpeg(460, 1920)
        payload_a = hdr_a + jpg_a
        buf_a = ctypes.create_string_buffer(payload_a)
        req_a = bytearray(struct.pack('IIIP', 0x02, len(payload_a), 2000, ctypes.addressof(buf_a)))

        t0 = time.monotonic()
        ret_a = fcntl.ioctl(fd_usb, USBDEVFS_BULK, req_a)
        dt_a = time.monotonic() - t0

        print(f"  Header Hex      : {hdr_a.hex()}")
        print(f"  JPEG Size       : {len(jpg_a)} bytes")
        print(f"  Total Payload   : {len(payload_a)} bytes")
        print(f"  USB Ioctl Return: {ret_a}")
        print(f"  Transmitted     : {ret_a} / {len(payload_a)} bytes")
        print(f"  Elapsed Time    : {dt_a:.4f} seconds")
        print("  --> PLEASE CHECK PHYSICAL LCD SCREEN NOW FOR TEST A <--")

        print("\nWaiting 5 seconds before Test B...")
        time.sleep(5.0)

        # Test B: Historical Native Header (480x1920, stride=480, flag=1)
        print("\n==========================================")
        print("  TEST B: Historical Native Header (480x1920, Stride=480)")
        print("==========================================")
        hdr_b = pack_msdisplay_header(480, 1920, 480, 1)
        jpg_b = create_test_grid_jpeg(480, 1920)
        payload_b = hdr_b + jpg_b
        buf_b = ctypes.create_string_buffer(payload_b)
        req_b = bytearray(struct.pack('IIIP', 0x02, len(payload_b), 2000, ctypes.addressof(buf_b)))

        t0 = time.monotonic()
        ret_b = fcntl.ioctl(fd_usb, USBDEVFS_BULK, req_b)
        dt_b = time.monotonic() - t0

        print(f"  Header Hex      : {hdr_b.hex()}")
        print(f"  JPEG Size       : {len(jpg_b)} bytes")
        print(f"  Total Payload   : {len(payload_b)} bytes")
        print(f"  USB Ioctl Return: {ret_b}")
        print(f"  Transmitted     : {ret_b} / {len(payload_b)} bytes")
        print(f"  Elapsed Time    : {dt_b:.4f} seconds")
        print("  --> PLEASE CHECK PHYSICAL LCD SCREEN NOW FOR TEST B <--")

    finally:
        try:
            fcntl.ioctl(fd_usb, USBDEVFS_RELEASEINTERFACE, iface_buf)
        except Exception:
            pass
        os.close(fd_usb)

if __name__ == "__main__":
    main()
