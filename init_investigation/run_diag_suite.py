import os, sys, time, fcntl, termios, select, struct, subprocess

DEV = "/dev/ttyACM0"
TX_HANDSHAKE = bytes.fromhex("41 48 00 02 00 80 00 00 4d 49")
LOG_FILE = "/home/tor/pc-case-lcd/diag_suite.log"

def log(msg):
    ts = time.strftime("%H:%M:%S.%MS")
    line = f"[{ts}] {msg}"
    print(line)
    with open(LOG_FILE, "a") as f:
        f.write(line + "\n")

open(LOG_FILE, "w").close()

log("=== DIAGNOSTIC SUITE START ===")

if not os.path.exists(DEV):
    log(f"ERROR: {DEV} not found.")
    sys.exit(1)

# Task 7 & 8: Test timing variations (0ms, 10ms, 100ms, 500ms, 1000ms, 2000ms, 5000ms)
delays = [0.0, 0.01, 0.1, 0.5, 1.0, 2.0, 5.0]

for delay in delays:
    log(f"\n--- TESTING TIMING DELAY AFTER OPEN/INIT: {delay*1000:.0f} ms ---")
    fd = os.open(DEV, os.O_RDWR | os.O_NOCTTY | os.O_NONBLOCK)
    try:
        # Termios 115200 8N1
        attrs = termios.tcgetattr(fd)
        attrs[0] = 0
        attrs[1] = 0
        attrs[2] = termios.B115200 | termios.CS8 | termios.CREAD | termios.CLOCAL
        attrs[3] = 0
        termios.tcsetattr(fd, termios.TCSANOW, attrs)

        # Assert DTR/RTS
        TIOCMGET, TIOCMSET = 0x5415, 0x5418
        TIOCM_DTR, TIOCM_RTS = 0x002, 0x004
        buf = struct.pack('I', 0)
        status = struct.unpack('I', fcntl.ioctl(fd, TIOCMGET, buf))[0] | TIOCM_DTR | TIOCM_RTS
        fcntl.ioctl(fd, TIOCMSET, struct.pack('I', status))

        termios.tcflush(fd, termios.TCIOFLUSH)

        if delay > 0:
            time.sleep(delay)

        log(f"TX Handshake: {TX_HANDSHAKE.hex(' ')}")
        w = os.write(fd, TX_HANDSHAKE)
        log(f"TX Result: {w} bytes written.")

        # Continuous read loop for 3.0s
        deadline = time.monotonic() + 3.0
        rx = bytearray()
        while time.monotonic() < deadline:
            r, _, _ = select.select([fd], [], [], max(0, deadline - time.monotonic()))
            if r:
                try:
                    b = os.read(fd, 256)
                    if b:
                        rx.extend(b)
                        log(f"RX CHUNK: {b.hex(' ')}")
                except BlockingIOError:
                    pass
                if rx: break

        log(f"Total RX Length: {len(rx)} bytes. Payload: {bytes(rx).hex(' ') if rx else '<NO DATA>'}")
    except Exception as e:
        log(f"Exception during test: {e}")
    finally:
        os.close(fd)

