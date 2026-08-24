import os
import sys
import time
import fcntl
import termios
import select
import struct

DEV_ACM = "/dev/ttyACM0"
TX_HANDSHAKE = bytes.fromhex("41 48 10 04 00 80 85 44 4d 49") # 0x0080 Handshake Request

def log(msg):
    ts = time.strftime("%H:%M:%S.%MS")
    print(f"[{ts}] {msg}")

def main():
    device_path = sys.argv[1] if len(sys.argv) > 1 else DEV_ACM

    log("=== HL VMAX LCD LINUX INITIALIZATION PROBE ===")
    log(f"Target node: {device_path}")

    if not os.path.exists(device_path):
        log(f"ERROR: Node {device_path} does not exist!")
        sys.exit(1)

    log(f"Opening {device_path} (O_RDWR | O_NOCTTY | O_NONBLOCK)...")
    try:
        fd = os.open(device_path, os.O_RDWR | os.O_NOCTTY | os.O_NONBLOCK)
    except Exception as e:
        log(f"ERROR: Failed to open {device_path}: {e}")
        sys.exit(1)

    try:
        # Step 1: Configure termios (IL default baud: 115200, 8 data, 1 stop, Parity.None)
        log("Configuring termios: 115200 baud, 8 data bits, 1 stop bit, no parity (CS8 | CREAD | CLOCAL)...")
        attrs = termios.tcgetattr(fd)
        attrs[0] = 0 # iflag
        attrs[1] = 0 # oflag
        attrs[2] = termios.B115200 | termios.CS8 | termios.CREAD | termios.CLOCAL # cflag
        attrs[3] = 0 # lflag
        termios.tcsetattr(fd, termios.TCSANOW, attrs)

        # Step 2: Assert CDC DTR & RTS via TIOCMSET ioctl
        log("Asserting CDC DTR & RTS signals via TIOCMSET ioctl...")
        try:
            TIOCMGET = 0x5415
            TIOCMSET = 0x5418
            TIOCM_DTR = 0x002
            TIOCM_RTS = 0x004
            
            buf = struct.pack('I', 0)
            res = fcntl.ioctl(fd, TIOCMGET, buf)
            status = struct.unpack('I', res)[0]
            status |= (TIOCM_DTR | TIOCM_RTS)
            fcntl.ioctl(fd, TIOCMSET, struct.pack('I', status))
            log("DTR and RTS line signals ASSERTED successfully.")
        except Exception as e:
            log(f"Warning: Line signaling ioctl: {e}")

        # Step 3: Flush stale input/output buffers
        log("Flushing input and output buffers...")
        termios.tcflush(fd, termios.TCIOFLUSH)

        # Step 4: Transmit Handshake Request Frame
        log(f"TX Frame (10 bytes): {TX_HANDSHAKE.hex(' ')}")
        written = os.write(fd, TX_HANDSHAKE)
        log(f"TX Result: {written} bytes written to serial driver.")

        # Step 5: Bounded Non-Blocking Read Loop (Wait up to 3.0s)
        log("Waiting for Handshake Response (3.0s bounded timeout)...")
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
                        log(f"Received chunk ({len(data)} bytes): {data.hex(' ')}")
                except BlockingIOError:
                    pass

        log(f"Total RX Length: {len(rx)} bytes")
        if rx:
            log(f"Raw RX Hex: {bytes(rx).hex(' ')}")
            if len(rx) >= 10 and rx[:2] == b"AH" and rx[-2:] == b"MI":
                log(">>> HANDSHAKE RESPONSE VALIDATED (AH..MI)! <<<")
                cmd = int.from_bytes(rx[4:6], 'big')
                log(f"Response CMD: 0x{cmd:04X}")
                if len(rx) >= 10:
                    max_pkg = int.from_bytes(rx[6:10], 'big')
                    log(f"MaxPackageSize: {max_pkg} bytes (0x{max_pkg:08X})")
            else:
                log("Frame structure does not match AH..MI pattern.")
        else:
            log("<NO RESPONSE RECEIVED FROM LCD FIRMWARE>")

    finally:
        os.close(fd)

if __name__ == "__main__":
    main()
