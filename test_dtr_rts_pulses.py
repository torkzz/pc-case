import os, sys, time, fcntl, termios, select, struct

DEV = "/dev/ttyACM0"
TX_HANDSHAKE = bytes.fromhex("41 48 10 04 00 80 85 44 4d 49")

def set_lines(fd, dtr, rts):
    TIOCMGET = 0x5415
    TIOCMSET = 0x5418
    TIOCM_DTR = 0x002
    TIOCM_RTS = 0x004
    buf = struct.pack('I', 0)
    res = fcntl.ioctl(fd, TIOCMGET, buf)
    status = struct.unpack('I', res)[0]
    if dtr: status |= TIOCM_DTR
    else: status &= ~TIOCM_DTR
    if rts: status |= TIOCM_RTS
    else: status &= ~TIOCM_RTS
    fcntl.ioctl(fd, TIOCMSET, struct.pack('I', status))

def test_sequence(name, pre_delay, pulse_dtr_rts, post_delay):
    print(f"\n--- TESTING SEQUENCE: {name} ---")
    if not os.path.exists(DEV):
        print(f"Device {DEV} not found.")
        return

    fd = os.open(DEV, os.O_RDWR | os.O_NOCTTY | os.O_NONBLOCK)
    try:
        attrs = termios.tcgetattr(fd)
        attrs[0], attrs[1], attrs[2], attrs[3] = 0, 0, termios.B115200 | termios.CS8 | termios.CREAD | termios.CLOCAL, 0
        termios.tcsetattr(fd, termios.TCSANOW, attrs)

        if pulse_dtr_rts:
            # Set DTR/RTS low (off)
            set_lines(fd, False, False)
            time.sleep(0.1)
            # Set DTR/RTS high (on)
            set_lines(fd, True, True)
        else:
            set_lines(fd, True, True)

        if post_delay > 0:
            time.sleep(post_delay)

        termios.tcflush(fd, termios.TCIOFLUSH)

        print(f"TX ({len(TX_HANDSHAKE)} bytes): {TX_HANDSHAKE.hex(' ')}")
        os.write(fd, TX_HANDSHAKE)

        deadline = time.monotonic() + 2.0
        rx = bytearray()
        while time.monotonic() < deadline:
            r, _, _ = select.select([fd], [], [], max(0, deadline - time.monotonic()))
            if r:
                try:
                    b = os.read(fd, 256)
                    if b: rx.extend(b)
                except BlockingIOError:
                    pass
                if rx: break

        print(f"RX length: {len(rx)}")
        if rx:
            print(">>> SUCCESSFUL RESPONSE RECEIVED: <<<")
            print("RX Hex:", bytes(rx).hex(' '))
        else:
            print("RX: <NO RESPONSE>")

    finally:
        os.close(fd)

test_sequence("Immediate DTR/RTS Assert", 0, False, 0.05)
test_sequence("DTR/RTS Reset Pulse (100ms)", 0, True, 0.2)
test_sequence("Post-Open Settle Delay (500ms)", 0, True, 0.5)
test_sequence("Post-Open Long Delay (1.5s)", 0, True, 1.5)

