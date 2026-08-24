import os, sys, time, struct, termios, fcntl, select, threading

USBMON_PATH = "/dev/usbmon1"
DEVICE_PATH = "/dev/ttyACM0"

class UsbmonCapture:
    def __init__(self):
        self.events = []
        self.running = False
        self.thread = None

    def start(self):
        self.events = []
        self.running = True
        self.thread = threading.Thread(target=self._run)
        self.thread.daemon = True
        self.thread.start()

    def _run(self):
        if not os.path.exists(USBMON_PATH):
            return
        try:
            with open(USBMON_PATH, "rb") as f:
                while self.running:
                    line = f.readline()
                    if not line: break
                    text = line.decode("latin1", errors="ignore").strip()
                    # Filter for USB bus 1 device 9 (33c3:f101) or 1:002
                    if " 1:002:" in text or "1:002:" in text or ":1:002:" in text:
                        self.events.append((time.time(), text))
        except Exception as e:
            self.events.append((time.time(), f"EXC: {e}"))

    def stop(self):
        self.running = False
        time.sleep(0.1)
        return self.events

def raw_reader_test(frame_hex_list):
    print("=== PHASE 6 & 7: RAW PARSER BYPASS & USBMON VERIFICATION ===")
    
    mon = UsbmonCapture()
    mon.start()

    fd = None
    try:
        fd = os.open(DEVICE_PATH, os.O_RDWR | os.O_NOCTTY | os.O_NONBLOCK)
        attrs = termios.tcgetattr(fd)
        attrs[0], attrs[1] = 0, 0
        attrs[2] = termios.B115200 | termios.CS8 | termios.CREAD | termios.CLOCAL
        attrs[3] = 0
        termios.tcsetattr(fd, termios.TCSANOW, attrs)

        TIOCMSET = 0x5418
        fcntl.ioctl(fd, TIOCMSET, struct.pack('I', 0x002 | 0x004)) # DTR+RTS ON
        termios.tcflush(fd, termios.TCIOFLUSH)

        for i, frame in enumerate(frame_hex_list):
            data = bytes.fromhex(frame)
            print(f"\n[{i+1}/{len(frame_hex_list)}] Transmitting raw frame: {data.hex(' ')}")
            written = os.write(fd, data)
            print(f"  Bytes written: {written}")

            # Continuous raw read loop for 3.0 seconds
            rx_bytes = bytearray()
            deadline = time.monotonic() + 3.0
            while time.monotonic() < deadline:
                r_fds, _, _ = select.select([fd], [], [], max(0.01, deadline - time.monotonic()))
                if r_fds:
                    try:
                        chunk = os.read(fd, 1024)
                        if chunk:
                            rx_bytes.extend(chunk)
                            print(f"  *** RAW READ GOT BYTES! ({len(chunk)}B): {chunk.hex(' ')}")
                    except BlockingIOError:
                        pass
            if not rx_bytes:
                print("  No raw application bytes received.")

            time.sleep(0.3)
    except Exception as e:
        print(f"Error during raw test: {e}")
    finally:
        if fd is not None:
            os.close(fd)

    events = mon.stop()
    print(f"\n=== USBMON KERNEL EVENT ANALYSIS ({len(events)} events) ===")
    in_urbs = [ev for t, ev in events if " In " in ev or " Bi " in ev or " Zi " in ev or " Ci " in ev or "Ii" in ev or " ep81 " in ev or " ep83 " in ev or " 81 " in ev or " 83 " in ev]
    out_urbs = [ev for t, ev in events if " Bo " in ev or " Co " in ev or " ep02 " in ev or " 02 " in ev]
    ctrl_urbs = [ev for t, ev in events if " Co " in ev or " Ci " in ev or " ep0 " in ev]

    print(f"Total USB OUT URBs: {len(out_urbs)}")
    for ev in out_urbs[:10]:
        print(f"  OUT: {ev}")

    print(f"Total USB IN URBs (EP 0x81 / EP 0x83): {len(in_urbs)}")
    for ev in in_urbs[:10]:
        print(f"  IN:  {ev}")

    print(f"Total Control URBs (EP0): {len(ctrl_urbs)}")
    for ev in ctrl_urbs[:10]:
        print(f"  CTRL: {ev}")

    if in_urbs:
        print("\n*** STOP CONDITION CHECK: IN URBs WERE DETECTED ON USB BUS! ***")

if __name__ == "__main__":
    test_frames = [
        "41480002008000004d49", # Handshake 0x0080
        "41480002007200004d49", # HardwareInfo 0x0072
        "41480002006200004d49", # FlashInfo 0x0062
        "41480002008500004d49", # DownloadStatus 0x0085
    ]
    raw_reader_test(test_frames)
