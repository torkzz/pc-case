import os, sys, time, fcntl, termios, select, struct

DEV = "/dev/ttyACM0"
# Exact frame logged by official DeviceCommunicationLibrary.dll:
# 0x41 0x48 0x00 0x02 0x00 0x80 0x00 0x00 0x4D 0x49
TX_OFFICIAL_HANDSHAKE = bytes.fromhex("41 48 00 02 00 80 00 00 4d 49")

print(f"=== TESTING OFFICIAL NO-CRC HANDSHAKE FRAME ===")
print(f"Target node: {DEV}")
print(f"TX Frame (10 bytes): {TX_OFFICIAL_HANDSHAKE.hex(' ')}")

fd = os.open(DEV, os.O_RDWR | os.O_NOCTTY | os.O_NONBLOCK)
try:
    attrs = termios.tcgetattr(fd)
    attrs[0], attrs[1], attrs[2], attrs[3] = 0, 0, termios.B115200 | termios.CS8 | termios.CREAD | termios.CLOCAL, 0
    termios.tcsetattr(fd, termios.TCSANOW, attrs)

    # Assert DTR & RTS
    TIOCMGET, TIOCMSET = 0x5415, 0x5418
    TIOCM_DTR, TIOCM_RTS = 0x002, 0x004
    buf = struct.pack('I', 0)
    res = fcntl.ioctl(fd, TIOCMGET, buf)
    status = struct.unpack('I', res)[0] | TIOCM_DTR | TIOCM_RTS
    fcntl.ioctl(fd, TIOCMSET, struct.pack('I', status))

    termios.tcflush(fd, termios.TCIOFLUSH)

    written = os.write(fd, TX_OFFICIAL_HANDSHAKE)
    print(f"TX Result: {written} bytes written to serial driver.")

    print("Waiting for Handshake Response (3.0s bounded timeout)...")
    deadline = time.monotonic() + 3.0
    rx = bytearray()

    while time.monotonic() < deadline:
        remaining = max(0, deadline - time.monotonic())
        r, _, _ = select.select([fd], [], [], remaining)
        if r:
            try:
                data = os.read(fd, 4096)
                if data:
                    rx.extend(data)
                    print(f"Received chunk ({len(data)} bytes): {data.hex(' ')}")
            except BlockingIOError:
                pass
            if rx: break

    print(f"Total RX Length: {len(rx)} bytes")
    if rx:
        print(">>> SUCCESSFUL RESPONSE RECEIVED FROM HARDWARE: <<<")
        print("Raw RX Hex:", bytes(rx).hex(' '))
    else:
        print("<NO RESPONSE RECEIVED FROM HARDWARE>")

finally:
    os.close(fd)
