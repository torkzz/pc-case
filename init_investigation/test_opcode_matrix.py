import os, sys, time, fcntl, termios, select, struct
from vmax_protocol import build_frame, parse_frame

DEV = "/dev/ttyACM0"

def test_opcode_sequence(name, cmd_list, crc_enabled=False):
    print(f"\n==================== TEST SEQUENCE: {name} ====================")
    if not os.path.exists(DEV):
        print(f"Device {DEV} not found.")
        return

    fd = os.open(DEV, os.O_RDWR | os.O_NOCTTY | os.O_NONBLOCK)
    try:
        attrs = termios.tcgetattr(fd)
        attrs[0], attrs[1], attrs[2], attrs[3] = 0, 0, termios.B115200 | termios.CS8 | termios.CREAD | termios.CLOCAL, 0
        termios.tcsetattr(fd, termios.TCSANOW, attrs)

        # Assert DTR & RTS
        TIOCMGET, TIOCMSET = 0x5415, 0x5418
        TIOCM_DTR, TIOCM_RTS = 0x002, 0x004
        buf = struct.pack('I', 0)
        status = struct.unpack('I', fcntl.ioctl(fd, TIOCMGET, buf))[0] | TIOCM_DTR | TIOCM_RTS
        fcntl.ioctl(fd, TIOCMSET, struct.pack('I', status))

        termios.tcflush(fd, termios.TCIOFLUSH)

        for cmd, content in cmd_list:
            frame = build_frame(cmd, content, is_crc_enabled=crc_enabled)
            print(f"TX Opcode 0x{cmd:04X} ({len(frame)} bytes): {frame.hex(' ')}")
            os.write(fd, frame)
            
            # Read response
            deadline = time.monotonic() + 1.0
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
            
            if rx:
                print(f"  >>> SUCCESSFUL RX for 0x{cmd:04X} ({len(rx)} bytes): {bytes(rx).hex(' ')} <<<")
                try:
                    p = parse_frame(bytes(rx))
                    print("  Parsed Frame:", p)
                except Exception as e:
                    print("  Parse error:", e)
            else:
                print(f"  RX for 0x{cmd:04X}: <NO RESPONSE>")

    finally:
        os.close(fd)

# Test combinations:
test_opcode_sequence("0x0072 (GetHardwareInfo) Alone", [(0x0072, b"")])
test_opcode_sequence("0x0062 (ConnectDevice/GetFlashInfo) Alone", [(0x0062, b"")])
test_opcode_sequence("0x0085 (GetDownloadStatus) Alone", [(0x0085, b"")])
test_opcode_sequence("0x0071 (ChangeStatus) Alone", [(0x0071, b"\x20")])
test_opcode_sequence("Sequence: 0x0072 -> 0x0080", [(0x0072, b""), (0x0080, b"")])
test_opcode_sequence("Sequence: 0x0062 -> 0x0080", [(0x0062, b""), (0x0080, b"")])

