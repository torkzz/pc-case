import os, sys, time, termios, fcntl, select

DEV = "/dev/ttyACM0"
print(f"=== PASSTHROUGH RAW READER (30s TIMEOUT) ON {DEV} ===")

if not os.path.exists(DEV):
    print("Device node not found.")
    sys.exit(1)

fd = os.open(DEV, os.O_RDWR | os.O_NOCTTY | os.O_NONBLOCK)
try:
    attrs = termios.tcgetattr(fd)
    attrs[0] = 0; attrs[1] = 0
    attrs[2] = termios.B115200 | termios.CS8 | termios.CREAD | termios.CLOCAL
    attrs[3] = 0
    termios.tcsetattr(fd, termios.TCSANOW, attrs)

    # Flush input
    termios.tcflush(fd, termios.TCIFLUSH)

    print("Monitoring raw bytes from MCU for 5 seconds (READ ONLY)...")
    start = time.monotonic()
    rx_total = bytearray()
    
    while time.monotonic() - start < 5.0:
        r, _, _ = select.select([fd], [], [], 0.5)
        if r:
            try:
                b = os.read(fd, 256)
                if b:
                    rx_total.extend(b)
                    print(f"[{time.monotonic()-start:.3f}s] RX {len(b)} bytes: {b.hex(' ')}")
            except BlockingIOError:
                pass

    print(f"Finished. Total bytes received: {len(rx_total)}")
finally:
    os.close(fd)
