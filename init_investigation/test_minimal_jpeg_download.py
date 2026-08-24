import os, sys, time, struct, termios, fcntl, select
from vmax_bruteforce import build_frame, UsbmonMonitor

DEVICE_PATH = "/dev/ttyACM0"

def test_minimal_jpeg():
    print("=== PHASE 11: SINGLE CONTROLLED 0x0082 (DOWNLOAD DATA) TEST ===")
    
    # 1 tiny dummy JPEG header or chunk (64 bytes)
    offset_bytes = struct.pack(">I", 0) # Offset = 0
    dummy_jpeg_chunk = b"\xFF\xD8\xFF\xE0\x00\x10JFIF\x00\x01\x01\x01\x00`\x00`\x00\x00" + b"\x00" * 46
    payload = offset_bytes + dummy_jpeg_chunk

    cmd = 0x0082 # DownloadDataRequest
    ctrl = 2 + len(payload)
    frame = build_frame(cmd, payload=payload, ctrl=ctrl, use_crc=False)

    print(f"Command: 0x{cmd:04X} | Offset: 0 | Data Len: {len(dummy_jpeg_chunk)}B | Payload Len: {len(payload)}B | CTRL: 0x{ctrl:04X}")
    print(f"Frame Hex: {frame[:20].hex(' ')} ... {frame[-10:].hex(' ')} (Total {len(frame)}B)")

    fd = os.open(DEVICE_PATH, os.O_RDWR | os.O_NOCTTY | os.O_NONBLOCK)
    attrs = termios.tcgetattr(fd)
    attrs[0], attrs[1] = 0, 0
    attrs[2] = termios.B115200 | termios.CS8 | termios.CREAD | termios.CLOCAL
    attrs[3] = 0
    termios.tcsetattr(fd, termios.TCSANOW, attrs)

    fcntl.ioctl(fd, 0x5418, struct.pack('I', 0x002 | 0x004))
    termios.tcflush(fd, termios.TCIOFLUSH)

    print(f"Transmitting single 0x0082 frame...")
    written = os.write(fd, frame)
    print(f"Bytes written: {written}")

    rx_data = bytearray()
    deadline = time.monotonic() + 3.0
    while time.monotonic() < deadline:
        r, _, _ = select.select([fd], [], [], max(0.01, deadline - time.monotonic()))
        if r:
            try:
                b = os.read(fd, 512)
                if b:
                    rx_data.extend(b)
                    print(f"*** RECEIVED RESPONSE ({len(b)}B): {b.hex(' ')}")
            except BlockingIOError:
                pass
        if rx_data: break

    os.close(fd)
    if not rx_data:
        print("No RX response received to 0x0082.")

if __name__ == "__main__":
    test_minimal_jpeg()
