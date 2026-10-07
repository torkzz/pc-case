#!/usr/bin/env python3
import os
import sys
import time
import fcntl
import termios
import struct

TIOCMGET = 0x5415
TIOCMBIS = 0x5416
TIOCM_DTR = 0x002
TIOCM_RTS = 0x004

tty = '/dev/ttyACM0'
print(f"[1] Checking for {tty}...")
if not os.path.exists(tty):
    print(f"[ERROR] {tty} does not exist.")
    sys.exit(1)

print(f"[2] Opening {tty} with O_RDWR | O_NOCTTY | O_NONBLOCK...")
fd = os.open(tty, os.O_RDWR | os.O_NOCTTY | os.O_NONBLOCK)

try:
    print("[3] Configuring raw 115200 8N1 termios mode...")
    attr = termios.tcgetattr(fd)
    # Input flags: clear IGNBRK, BRKINT, PARMRK, ISTRIP, INLCR, IGNCR, ICRNL, IXON
    attr[0] &= ~(termios.IGNBRK | termios.BRKINT | termios.PARMRK | termios.ISTRIP | termios.INLCR | termios.IGNCR | termios.ICRNL | termios.IXON)
    # Output flags: clear OPOST
    attr[1] &= ~termios.OPOST
    # Control flags: set CS8, CREAD, CLOCAL, clear PARENB, CSTOPB, CRTSCTS
    attr[2] &= ~(termios.PARENB | termios.CSTOPB | termios.CRTSCTS)
    attr[2] |= (termios.CS8 | termios.CREAD | termios.CLOCAL)
    # Local flags: clear ISIG, ICANON, ECHO, ECHOE, ECHOK, ECHONL, IEXTEN
    attr[3] &= ~(termios.ISIG | termios.ICANON | termios.ECHO | termios.ECHOE | termios.ECHOK | termios.ECHONL | termios.IEXTEN)
    # Speed: 115200 baud
    attr[4] = termios.B115200
    attr[5] = termios.B115200
    termios.tcsetattr(fd, termios.TCSANOW, attr)
    print("    Termios raw mode applied.")

    print("[4] Asserting DTR and RTS via TIOCMBIS ioctl...")
    lines = struct.pack('I', TIOCM_DTR | TIOCM_RTS)
    fcntl.ioctl(fd, TIOCMBIS, lines)
    
    # Read back line flags via TIOCMGET
    buf = struct.pack('I', 0)
    res = fcntl.ioctl(fd, TIOCMGET, buf)
    flags = struct.unpack('I', res)[0]
    dtr_state = bool(flags & TIOCM_DTR)
    rts_state = bool(flags & TIOCM_RTS)
    print(f"    Line Control State: DTR={dtr_state}, RTS={rts_state} (Raw flags: 0x{flags:04x})")

    print("[5] Waiting 200ms for hardware line stabilization...")
    time.sleep(0.2)

    wake_pkt = bytes.fromhex('41481004008085444d49')
    print(f"[6] Transmitting 10-byte wake packet: {wake_pkt.hex()}...")
    n_written = os.write(fd, wake_pkt)
    print(f"    Wrote {n_written} / {len(wake_pkt)} bytes.")

    print("[7] Draining TTY output buffer (tcdrain)...")
    termios.tcdrain(fd)
    print("    Drain complete.")

    print("[8] Keeping device open for 1.5 seconds and listening for response...")
    start_t = time.monotonic()
    resp = b""
    while (time.monotonic() - start_t) < 1.5:
        try:
            chunk = os.read(fd, 64)
            if chunk:
                resp += chunk
        except BlockingIOError:
            pass
        time.sleep(0.05)

    if resp:
        print(f"    [RESPONSE RECEIVED] {len(resp)} bytes: {resp.hex()}")
    else:
        print("    [NO RESPONSE RECEIVED] (Device accepted wake silent or response on bulk endpoint)")

finally:
    print("[9] Closing file descriptor...")
    os.close(fd)
    print("[10] Diagnostic test finished.")
