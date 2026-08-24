import os, sys, time, termios, fcntl, struct, select, threading

DEV = "/dev/ttyACM0"
USBMON_NODE = "/dev/usbmon1"

configs = [
    ("A", "115200 8N1 DTR+RTS", termios.B115200, True, True),
    ("B", "115200 8N1 DTR only", termios.B115200, True, False),
    ("C", "115200 8N1 RTS only", termios.B115200, False, True),
    ("D", "115200 8N1 DTR/RTS disabled", termios.B115200, False, False),
    ("E", "9600 8N1 DTR+RTS", termios.B9600, True, True),
    ("F", "57600 8N1 DTR+RTS", termios.B57600, True, True),
    ("G", "230400 8N1 DTR+RTS", termios.B230400, True, True),
]

class UsbmonCapture:
    def __init__(self):
        self.lines = []
        self.running = False
        self.t = None

    def start(self):
        self.lines = []
        self.running = True
        self.t = threading.Thread(target=self._read)
        self.t.daemon = True
        self.t.start()

    def _read(self):
        try:
            with open(USBMON_NODE, 'rb') as f:
                while self.running:
                    l = f.readline()
                    if not l: break
                    str_l = l.decode('latin1', errors='ignore').strip()
                    if " 1:002:" in str_l or "1:002:" in str_l:
                        self.lines.append(str_l)
        except Exception:
            pass

    def stop(self):
        self.running = False
        time.sleep(0.15)
        return list(self.lines)

matrix_results = []

for cid, desc, baud, dtr, rts in configs:
    print(f"\n--- Testing Config {cid}: {desc} ---")
    mon = UsbmonCapture()
    mon.start()

    rx_spontaneous = bytearray()
    
    try:
        fd = os.open(DEV, os.O_RDWR | os.O_NOCTTY | os.O_NONBLOCK)
        attrs = termios.tcgetattr(fd)
        attrs[0], attrs[1] = 0, 0
        attrs[2] = baud | termios.CS8 | termios.CREAD | termios.CLOCAL
        attrs[3] = 0
        termios.tcsetattr(fd, termios.TCSANOW, attrs)

        TIOCMSET = 0x5418
        status = 0
        if dtr: status |= 0x002
        if rts: status |= 0x004
        fcntl.ioctl(fd, TIOCMSET, struct.pack('I', status))
        termios.tcflush(fd, termios.TCIOFLUSH)

        # Wait 100ms
        time.sleep(0.1)
        
        # Listen for 1.0s with NO vendor commands transmitted
        deadline = time.monotonic() + 1.0
        while time.monotonic() < deadline:
            r, _, _ = select.select([fd], [], [], max(0.01, deadline - time.monotonic()))
            if r:
                try:
                    b = os.read(fd, 512)
                    if b: rx_spontaneous.extend(b)
                except BlockingIOError:
                    pass
                if rx_spontaneous: break

        os.close(fd)
    except Exception as e:
        print(f"Config {cid} Error: {e}")

    mon_log = mon.stop()
    
    ctrl_reqs = [l for l in mon_log if " C " in l or " s " in l or " S " in l or " 0x21 " in l]
    bulk_in = [l for l in mon_log if "Bi:" in l or "bi:" in l]
    int_in = [l for l in mon_log if "Ii:" in l or "ii:" in l]

    print(f"Config {cid} Complete: Spontaneous RX={len(rx_spontaneous)}B, Control Transfers={len(ctrl_reqs)}, Bulk IN={len(bulk_in)}, Int IN={len(int_in)}")
    
    matrix_results.append({
        "cid": cid,
        "desc": desc,
        "spontaneous_rx": len(rx_spontaneous),
        "ctrl_transfers": len(ctrl_reqs),
        "bulk_in_count": len(bulk_in),
        "int_in_count": len(int_in),
        "ctrl_log": ctrl_reqs
    })

# Write cdc_init_matrix.md
with open("/home/tor/pc-case-lcd/cdc_init_matrix.md", "w") as f:
    f.write("# Serial & Line Control Initialization Matrix (`cdc_init_matrix.md`)\n\n")
    f.write("## Overview\n")
    f.write("Tested line configurations (baud rates and DTR/RTS line control states) without transmitting any vendor commands to observe spontaneous transmission or endpoint activity.\n\n")
    f.write("## Test Results Matrix\n\n")
    f.write("| Config | Description | Control Transfers | Spontaneous RX Bytes | Bulk IN URBs | Interrupt IN URBs | Status |\n")
    f.write("| :--- | :--- | :--- | :--- | :--- | :--- | :--- |\n")
    for r in matrix_results:
        f.write(f"| {r['cid']} | {r['desc']} | {r['ctrl_transfers']} | {r['spontaneous_rx']} | {r['bulk_in_count']} | {r['int_in_count']} | {'**SPONTANEOUS DATA RX**' if r['spontaneous_rx'] > 0 else '0 Bytes Transmitted'} |\n")

    f.write("\n## CDC Control Transfer Logs\n\n")
    for r in matrix_results:
        f.write(f"### Config {r['cid']}: {r['desc']}\n")
        f.write("```\n")
        if r['ctrl_log']:
            for l in r['ctrl_log']: f.write(l + "\n")
        else:
            f.write("No control events recorded.\n")
        f.write("```\n\n")

print("Generated /home/tor/pc-case-lcd/cdc_init_matrix.md")
