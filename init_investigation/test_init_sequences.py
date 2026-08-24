import os, sys, time, struct, termios, fcntl, select, json
from vmax_bruteforce import build_frame, UsbmonMonitor

DEVICE_PATH = "/dev/ttyACM0"

SEQUENCES = [
    ("Seq 1: ConnectDevice (0x0062)", [0x0062]),
    ("Seq 2: Handshake (0x0080) -> HardwareInfo (0x0072)", [0x0080, 0x0072]),
    ("Seq 3: Flash (0x0062) -> Handshake (0x0080) -> HwInfo (0x0072) -> DlStatus (0x0085)", [0x0062, 0x0080, 0x0072, 0x0085]),
    ("Seq 4: Flash (0x0062) -> GifInfo (0x0061) -> HwInfo (0x0072)", [0x0062, 0x0061, 0x0072]),
    ("Seq 5: Handshake (0x0080) -> Flash (0x0062) -> DlReq (0x0081)", [0x0080, 0x0062, 0x0081]),
    ("Seq 6: Restart (0x0070) -> Handshake (0x0080)", [0x0070, 0x0080]),
    ("Seq 7: ChangeStatus (0x0071) -> Handshake (0x0080)", [0x0071, 0x0080]),
]

def run_sequence(name, opcodes, timeout_sec=2.0, delay_ms=100):
    print(f"\n=======================================================")
    print(f"=== {name} ===")
    print(f"Opcodes: {[hex(o) for o in opcodes]}")
    print(f"=======================================================")

    fd = None
    try:
        fd = os.open(DEVICE_PATH, os.O_RDWR | os.O_NOCTTY | os.O_NONBLOCK)
        attrs = termios.tcgetattr(fd)
        attrs[0], attrs[1] = 0, 0
        attrs[2] = termios.B115200 | termios.CS8 | termios.CREAD | termios.CLOCAL
        attrs[3] = 0
        termios.tcsetattr(fd, termios.TCSANOW, attrs)

        fcntl.ioctl(fd, 0x5418, struct.pack('I', 0x002 | 0x004))
        termios.tcflush(fd, termios.TCIOFLUSH)

        for step, cmd in enumerate(opcodes):
            frame = build_frame(cmd, payload=b"", ctrl=2)
            print(f" Step {step+1}: Transmitting CMD 0x{cmd:04X} ({frame.hex(' ')})")
            os.write(fd, frame)

            rx_data = bytearray()
            deadline = time.monotonic() + timeout_sec
            while time.monotonic() < deadline:
                r, _, _ = select.select([fd], [], [], max(0.01, deadline - time.monotonic()))
                if r:
                    try:
                        chunk = os.read(fd, 512)
                        if chunk:
                            rx_data.extend(chunk)
                            print(f"   *** RECEIVED {len(chunk)}B: {chunk.hex(' ')}")
                    except BlockingIOError:
                        pass
                if rx_data:
                    break

            if rx_data:
                print(f"*** STOP CONDITION MET IN SEQUENCE: Unexpected RX: {rx_data.hex(' ')}")
                break

            time.sleep(delay_ms / 1000.0)

    except Exception as e:
        print(f"Sequence exception: {e}")
    finally:
        if fd is not None:
            os.close(fd)

def main():
    for name, opcodes in SEQUENCES:
        run_sequence(name, opcodes)

if __name__ == "__main__":
    main()
