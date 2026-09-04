import os, sys, time, fcntl, termios, select, struct, subprocess, threading

DEV = "/dev/ttyACM0"
USBMON_NODE = "/dev/usbmon1"
TX_HANDSHAKE = bytes.fromhex("41 48 00 02 00 80 00 00 4D 49") # Official handshake frame (CMD 0x0080)

def set_lines(fd, dtr, rts):
    TIOCMSET = 0x5418
    TIOCM_DTR = 0x002
    TIOCM_RTS = 0x004
    status = 0
    if dtr: status |= TIOCM_DTR
    if rts: status |= TIOCM_RTS
    fcntl.ioctl(fd, TIOCMSET, struct.pack('I', status))

class UsbmonCapturer:
    def __init__(self):
        self.lines = []
        self.running = False
        self.proc = None

    def start(self):
        self.lines = []
        self.running = True
        self.thread = threading.Thread(target=self._run)
        self.thread.daemon = True
        self.thread.start()

    def _run(self):
        try:
            with open(USBMON_NODE, 'r', errors='ignore') as f:
                while self.running:
                    line = f.readline()
                    if not line: break
                    if " 1:002:" in line or "1:002:" in line:
                        self.lines.append(line.strip())
        except Exception as e:
            self.lines.append(f"Error reading usbmon: {e}")

    def stop(self):
        self.running = False
        time.sleep(0.2)
        return list(self.lines)

def run_test(name, setup_fn):
    print(f"\n--- RUNNING TEST: {name} ---")
    mon = UsbmonCapturer()
    mon.start()
    time.sleep(0.1)

    rx_data = bytearray()
    start_time = time.monotonic()
    
    try:
        fd = os.open(DEV, os.O_RDWR | os.O_NOCTTY | os.O_NONBLOCK)
        # Apply termios settings: 115200 8N1 raw
        attrs = termios.tcgetattr(fd)
        # c_iflag, c_oflag, c_cflag, c_lflag, c_cc
        attrs[0] = 0
        attrs[1] = 0
        attrs[2] = termios.B115200 | termios.CS8 | termios.CREAD | termios.CLOCAL
        attrs[3] = 0
        termios.tcsetattr(fd, termios.TCSANOW, attrs)

        # Run custom line-control sequence
        setup_fn(fd)

        # Flush buffers
        termios.tcflush(fd, termios.TCIOFLUSH)

        # Send handshake
        tx_time = time.monotonic()
        os.write(fd, TX_HANDSHAKE)

        # Wait up to 2 seconds for response
        deadline = time.monotonic() + 2.0
        while time.monotonic() < deadline:
            r, _, _ = select.select([fd], [], [], max(0.01, deadline - time.monotonic()))
            if r:
                try:
                    b = os.read(fd, 512)
                    if b:
                        rx_data.extend(b)
                except BlockingIOError:
                    pass
                if rx_data: break
        os.close(fd)
    except Exception as e:
        print(f"Exception during test {name}: {e}")

    duration = time.monotonic() - start_time
    mon_log = mon.stop()

    # Summarize usbmon activity
    ctrl_events = [l for l in mon_log if " C " in l or " s " in l or " S " in l or "Ci:" in l or "Co:" in l or " 0x21 " in l]
    bulk_out = [l for l in mon_log if "Bo:" in l or "bo:" in l]
    bulk_in = [l for l in mon_log if "Bi:" in l or "bi:" in l]
    int_in = [l for l in mon_log if "Ii:" in l or "ii:" in l]

    print(f"Duration: {duration:.3f}s, RX Bytes: {len(rx_data)}")
    print(f"USB Controls: {len(ctrl_events)}, Bulk OUT: {len(bulk_out)}, Bulk IN: {len(bulk_in)}, Int IN: {len(int_in)}")
    if rx_data:
        print(f"RX Data: {rx_data.hex(' ')}")
    
    return {
        "name": name,
        "rx_bytes": len(rx_data),
        "rx_hex": rx_data.hex(' ') if rx_data else "",
        "ctrl_events": ctrl_events,
        "bulk_out": bulk_out,
        "bulk_in": bulk_in,
        "int_in": int_in,
        "raw_mon": mon_log
    }

results = []

# Test A: open -> no DTR / no RTS -> handshake
results.append(run_test("A. open -> no DTR/RTS -> handshake", lambda fd: set_lines(fd, False, False)))
time.sleep(0.5)

# Test B: open -> DTR only -> handshake
results.append(run_test("B. open -> DTR only -> handshake", lambda fd: set_lines(fd, True, False)))
time.sleep(0.5)

# Test C: open -> RTS only -> handshake
results.append(run_test("C. open -> RTS only -> handshake", lambda fd: set_lines(fd, False, True)))
time.sleep(0.5)

# Test D: open -> DTR+RTS -> handshake
results.append(run_test("D. open -> DTR+RTS -> handshake", lambda fd: set_lines(fd, True, True)))
time.sleep(0.5)

# Test E: DTR+RTS -> drop both -> wait 100ms -> restore DTR+RTS -> handshake
def setup_E(fd):
    set_lines(fd, True, True)
    time.sleep(0.05)
    set_lines(fd, False, False)
    time.sleep(0.1)
    set_lines(fd, True, True)
    time.sleep(0.05)

results.append(run_test("E. DTR+RTS -> drop both -> wait 100ms -> restore -> handshake", setup_E))
time.sleep(0.5)

# Test F: toggle DTR with delays (0ms, 10ms, 100ms, 500ms, 1000ms, 3000ms)
for delay_ms in [0, 10, 100, 500, 1000, 3000]:
    def make_setup_F(d_ms):
        def setup_F(fd):
            set_lines(fd, False, True) # DTR off, RTS on
            time.sleep(0.02)
            set_lines(fd, True, True) # DTR high
            if d_ms > 0:
                time.sleep(d_ms / 1000.0)
        return setup_F
    results.append(run_test(f"F. Toggle DTR with delay {delay_ms}ms -> handshake", make_setup_F(delay_ms)))
    time.sleep(0.5)

# Write Markdown report cdc_control_state_tests.md
with open("/home/tor/pc-case-lcd/cdc_control_state_tests.md", "w") as f:
    f.write("# CDC Control & DTR/RTS State Machine Test Report\n\n")
    f.write("## Overview\n")
    f.write("Tested line signal control state transitions (DTR, RTS, timing delays) and monitored `usbmon1` for control requests and endpoint responses.\n\n")
    
    f.write("## Detailed Results Matrix\n\n")
    f.write("| Case | Description | Control Transfers | Bulk OUT | Bulk IN URBs | Interrupt IN URBs | RX Byte Count | Result |\n")
    f.write("| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |\n")
    
    for r in results:
        ctrl_cnt = len(r['ctrl_events'])
        bout_cnt = len(r['bulk_out'])
        bin_cnt = len(r['bulk_in'])
        iint_cnt = len(r['int_in'])
        rx_cnt = r['rx_bytes']
        status = "**DATA RX!**" if rx_cnt > 0 else "0 Bytes RX"
        f.write(f"| {r['name']} | {r['name']} | {ctrl_cnt} | {bout_cnt} | {bin_cnt} | {iint_cnt} | {rx_cnt} | {status} |\n")

    f.write("\n## Raw Control Transfer Details\n\n")
    for r in results:
        f.write(f"### {r['name']}\n")
        f.write("```\n")
        if r['ctrl_events']:
            for line in r['ctrl_events']:
                f.write(line + "\n")
        else:
            f.write("No control events recorded.\n")
        f.write("```\n\n")

print("\nMatrix test complete. Written to /home/tor/pc-case-lcd/cdc_control_state_tests.md")
