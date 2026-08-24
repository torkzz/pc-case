import os, sys, time, fcntl, termios, select, struct, json, threading

DEV = "/dev/ttyACM0"
USBMON_NODE = "/dev/usbmon1"

FRAMES = {
    "HANDSHAKE": bytes.fromhex("41 48 00 02 00 80 00 00 4D 49"),        # 0x0080
    "HARDWARE_INFO": bytes.fromhex("41 48 00 02 00 72 00 00 4D 49"),    # 0x0072
    "CHANGE_STATUS": bytes.fromhex("41 48 00 03 00 71 01 00 4D 49"),    # 0x0071 (status 1)
    "RESTART": bytes.fromhex("41 48 00 02 00 70 00 00 4D 49"),          # 0x0070
    "DOWNLOAD_STATUS": bytes.fromhex("41 48 00 02 00 85 00 00 4D 49"),  # 0x0085
}

def set_dtr_rts(fd, dtr, rts):
    TIOCMSET = 0x5418
    status = 0
    if dtr: status |= 0x002 # TIOCM_DTR
    if rts: status |= 0x004 # TIOCM_RTS
    fcntl.ioctl(fd, TIOCMSET, struct.pack('I', status))

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
            with open(USBMON_NODE, 'r', errors='ignore') as f:
                while self.running:
                    line = f.readline()
                    if not line: break
                    if " 1:002:" in line or "1:002:" in line:
                        self.lines.append(line.strip())
        except Exception as e:
            self.lines.append(f"usbmon error: {e}")

    def stop(self):
        self.running = False
        time.sleep(0.15)
        return list(self.lines)

def run_sequence(seq_id, description, steps):
    print(f"\n=======================================================")
    print(f"=== SEQUENCE {seq_id}: {description} ===")
    print(f"=======================================================")

    # Step 1 & 2: Close / Settle 500ms
    time.sleep(0.5)

    mon = UsbmonCapture()
    mon.start()

    tx_events = []
    rx_events = []
    rx_bytes_total = bytearray()
    
    t_start = time.monotonic()
    
    try:
        # Step 3: Open port at 115200 8N1
        fd = os.open(DEV, os.O_RDWR | os.O_NOCTTY | os.O_NONBLOCK)
        attrs = termios.tcgetattr(fd)
        attrs[0], attrs[1] = 0, 0
        attrs[2] = termios.B115200 | termios.CS8 | termios.CREAD | termios.CLOCAL
        attrs[3] = 0
        termios.tcsetattr(fd, termios.TCSANOW, attrs)

        # Step 4: Line signaling & step execution
        dtr_state, rts_state = True, True # Default DTR+RTS ON

        for action in steps:
            op = action.get("op")
            
            if op == "DTR_RTS":
                dtr_state = action.get("dtr", True)
                rts_state = action.get("rts", True)
                set_dtr_rts(fd, dtr_state, rts_state)
                time.sleep(0.02)
                
            elif op == "WAIT":
                delay_s = action.get("delay_ms", 100) / 1000.0
                time.sleep(delay_s)
                
            elif op == "SEND":
                cmd_key = action.get("cmd")
                frame = FRAMES[cmd_key]
                
                # Step 5: Flush buffers
                termios.tcflush(fd, termios.TCIOFLUSH)
                
                # Step 6 & 7: Transmit & Timestamp
                ts_tx = time.monotonic() - t_start
                w_bytes = os.write(fd, frame)
                tx_events.append({
                    "time_offset_s": round(ts_tx, 4),
                    "cmd": cmd_key,
                    "frame_hex": frame.hex(' '),
                    "bytes_written": w_bytes
                })
                print(f"[{ts_tx:.3f}s] TX {cmd_key}: {frame.hex(' ')} ({w_bytes}B)")

                # Step 8: Read loop for 1.5s
                deadline = time.monotonic() + 1.5
                while time.monotonic() < deadline:
                    r, _, _ = select.select([fd], [], [], max(0.005, deadline - time.monotonic()))
                    if r:
                        try:
                            b = os.read(fd, 512)
                            if b:
                                ts_rx = time.monotonic() - t_start
                                rx_bytes_total.extend(b)
                                rx_events.append({
                                    "time_offset_s": round(ts_rx, 4),
                                    "hex": b.hex(' '),
                                    "length": len(b)
                                })
                                print(f"[{ts_rx:.3f}s] *** RX CHUNK ({len(b)}B): {b.hex(' ')} ***")
                        except BlockingIOError:
                            pass
                        if rx_bytes_total: break

        os.close(fd)
    except Exception as e:
        print(f"Sequence Exception: {e}")

    mon_log = mon.stop()

    # URB Analysis
    bulk_out = [l for l in mon_log if "Bo:" in l or "bo:" in l]
    bulk_in = [l for l in mon_log if "Bi:" in l or "bi:" in l]
    int_in = [l for l in mon_log if "Ii:" in l or "ii:" in l]
    ctrl_trans = [l for l in mon_log if " C " in l or " s " in l or " S " in l or " 0x21 " in l]

    result = {
        "seq_id": seq_id,
        "description": description,
        "tx_count": len(tx_events),
        "rx_bytes_total": len(rx_bytes_total),
        "rx_hex": rx_bytes_total.hex(' '),
        "tx_events": tx_events,
        "rx_events": rx_events,
        "urb_counts": {
            "control": len(ctrl_trans),
            "bulk_out": len(bulk_out),
            "bulk_in": len(bulk_in),
            "interrupt_in": len(int_in)
        },
        "raw_mon_lines": mon_log
    }

    print(f"Sequence {seq_id} Complete. RX Total: {len(rx_bytes_total)}B. URBs: Bulk OUT={len(bulk_out)}, Bulk IN={len(bulk_in)}, Int IN={len(int_in)}")
    return result

# Sequences A through L
sequence_definitions = [
    ("A", "OPEN -> WAIT 100ms -> HANDSHAKE 0x0080", [
        {"op": "WAIT", "delay_ms": 100},
        {"op": "SEND", "cmd": "HANDSHAKE"}
    ]),
    ("B", "OPEN -> WAIT 10ms -> HANDSHAKE", [
        {"op": "WAIT", "delay_ms": 10},
        {"op": "SEND", "cmd": "HANDSHAKE"}
    ]),
    ("C", "OPEN -> WAIT 100ms -> HANDSHAKE", [
        {"op": "WAIT", "delay_ms": 100},
        {"op": "SEND", "cmd": "HANDSHAKE"}
    ]),
    ("D", "OPEN -> WAIT 500ms -> HANDSHAKE", [
        {"op": "WAIT", "delay_ms": 500},
        {"op": "SEND", "cmd": "HANDSHAKE"}
    ]),
    ("E", "OPEN -> DTR ON -> RTS ON -> WAIT 50ms -> HANDSHAKE", [
        {"op": "DTR_RTS", "dtr": True, "rts": True},
        {"op": "WAIT", "delay_ms": 50},
        {"op": "SEND", "cmd": "HANDSHAKE"}
    ]),
    ("F", "OPEN -> DTR OFF -> RTS OFF -> WAIT 50ms -> HANDSHAKE", [
        {"op": "DTR_RTS", "dtr": False, "rts": False},
        {"op": "WAIT", "delay_ms": 50},
        {"op": "SEND", "cmd": "HANDSHAKE"}
    ]),
    ("G", "HANDSHAKE -> HARDWARE_INFO", [
        {"op": "SEND", "cmd": "HANDSHAKE"},
        {"op": "WAIT", "delay_ms": 100},
        {"op": "SEND", "cmd": "HARDWARE_INFO"}
    ]),
    ("H", "HANDSHAKE -> CHANGE_STATUS 0x0071 -> HANDSHAKE", [
        {"op": "SEND", "cmd": "HANDSHAKE"},
        {"op": "WAIT", "delay_ms": 100},
        {"op": "SEND", "cmd": "CHANGE_STATUS"},
        {"op": "WAIT", "delay_ms": 100},
        {"op": "SEND", "cmd": "HANDSHAKE"}
    ]),
    ("I", "HANDSHAKE -> RESTART 0x0070 -> WAIT 1s -> HANDSHAKE", [
        {"op": "SEND", "cmd": "HANDSHAKE"},
        {"op": "WAIT", "delay_ms": 100},
        {"op": "SEND", "cmd": "RESTART"},
        {"op": "WAIT", "delay_ms": 1000},
        {"op": "SEND", "cmd": "HANDSHAKE"}
    ]),
    ("J", "CHANGE_STATUS -> HANDSHAKE -> HARDWARE_INFO", [
        {"op": "SEND", "cmd": "CHANGE_STATUS"},
        {"op": "WAIT", "delay_ms": 100},
        {"op": "SEND", "cmd": "HANDSHAKE"},
        {"op": "WAIT", "delay_ms": 100},
        {"op": "SEND", "cmd": "HARDWARE_INFO"}
    ]),
    ("K", "RESTART -> WAIT 100ms -> HANDSHAKE -> HARDWARE_INFO", [
        {"op": "SEND", "cmd": "RESTART"},
        {"op": "WAIT", "delay_ms": 100},
        {"op": "SEND", "cmd": "HANDSHAKE"},
        {"op": "WAIT", "delay_ms": 100},
        {"op": "SEND", "cmd": "HARDWARE_INFO"}
    ]),
    ("L", "HARDWARE_INFO -> HANDSHAKE", [
        {"op": "SEND", "cmd": "HARDWARE_INFO"},
        {"op": "WAIT", "delay_ms": 100},
        {"op": "SEND", "cmd": "HANDSHAKE"}
    ])
]

all_results = []
for seq_id, desc, steps in sequence_definitions:
    res = run_sequence(seq_id, desc, steps)
    all_results.append(res)

# Save JSON results
with open("/home/tor/pc-case-lcd/vmax_command_matrix_results.json", "w") as f:
    json.dump(all_results, f, indent=2)

# Save Markdown report
with open("/home/tor/pc-case-lcd/vmax_command_matrix_report.md", "w") as f:
    f.write("# Systematic Command Matrix Execution Report\n\n")
    f.write("## Matrix Execution Summary\n\n")
    f.write("| Seq | Description | TX Count | Ctrl URBs | Bulk OUT URBs | Bulk IN URBs | Int IN URBs | Total RX Bytes | Status |\n")
    f.write("| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |\n")
    
    for r in all_results:
        u = r['urb_counts']
        status = "**RESPONSE RECEIVED!**" if r['rx_bytes_total'] > 0 else "0 Bytes / Timeout"
        f.write(f"| {r['seq_id']} | {r['description']} | {r['tx_count']} | {u['control']} | {u['bulk_out']} | {u['bulk_in']} | {u['interrupt_in']} | {r['rx_bytes_total']} | {status} |\n")

    f.write("\n## Detailed Per-Sequence Logs\n\n")
    for r in all_results:
        f.write(f"### Sequence {r['seq_id']}: {r['description']}\n")
        f.write("#### Transmission Log:\n```json\n")
        f.write(json.dumps(r['tx_events'], indent=2) + "\n")
        f.write("```\n")
        f.write("#### Reception Log:\n```\n")
        if r['rx_events']:
            for rx in r['rx_events']:
                f.write(f"[{rx['time_offset_s']:.4f}s] {rx['length']}B: {rx['hex']}\n")
        else:
            f.write("No application RX bytes received.\n")
        f.write("```\n\n")

print("\nMatrix execution complete. Saved vmax_command_matrix_results.json and vmax_command_matrix_report.md.")
