#!/usr/bin/env python3
import os
import sys
import time
import struct
import fcntl
import termios
from PIL import Image, ImageDraw
import io

HEADER = b"AH"
FOOTER = b"MI"

def build_frame(cmd: int, content: bytes = b"") -> bytes:
    calc_len = len(content) + 2
    ctrl_val = calc_len & 0x0FFF
    ctrl_bytes = ctrl_val.to_bytes(2, 'big')
    cmd_bytes = cmd.to_bytes(2, 'big')
    crc_bytes = b"\x00\x00"
    return HEADER + ctrl_bytes + cmd_bytes + content + crc_bytes + FOOTER

def main():
    tty = '/dev/ttyACM0'
    print(f"Opening {tty} for VMAX AH..MI frame protocol test...")
    if not os.path.exists(tty):
        print(f"Error: {tty} does not exist.")
        sys.exit(1)

    fd = os.open(tty, os.O_RDWR | os.O_NOCTTY | os.O_NONBLOCK)
    attr = termios.tcgetattr(fd)
    attr[0], attr[1] = 0, 0
    attr[2] = termios.B115200 | termios.CS8 | termios.CREAD | termios.CLOCAL
    attr[3] = 0
    termios.tcsetattr(fd, termios.TCSANOW, attr)

    TIOCMSET = 0x5418
    fcntl.ioctl(fd, TIOCMSET, struct.pack('I', 0x002 | 0x004))
    termios.tcflush(fd, termios.TCIOFLUSH)

    # 1. Send Handshake
    hs_frame = build_frame(0x0080)
    print(f"Sending Handshake 0x0080: {hs_frame.hex(' ')}")
    os.write(fd, hs_frame)
    time.sleep(0.2)

    # 2. Generate small red test JPEG
    img = Image.new('RGB', (480, 1920), (255, 0, 0))
    buf = io.BytesIO()
    img.save(buf, format="JPEG", quality=80)
    jpg_bytes = buf.getvalue()
    print(f"Generated test JPEG: {len(jpg_bytes)} bytes")

    # 3. Send Chunk via CMD_DOWNLOAD_DATA_REQ (0x0082)
    offset = 0
    chunk_size = 4096
    for i in range(0, len(jpg_bytes), chunk_size):
        chunk = jpg_bytes[i:i+chunk_size]
        offset_bytes = struct.pack(">I", i)
        payload = offset_bytes + chunk
        frame = build_frame(0x0082, payload)
        os.write(fd, frame)
        time.sleep(0.01)

    # 4. Send Download Complete (0x008F)
    comp_frame = build_frame(0x008F)
    os.write(fd, comp_frame)
    print("Sent Download Complete 0x008F frame.")

    os.close(fd)
    print("Serial AH..MI frame test completed.")

if __name__ == "__main__":
    main()
