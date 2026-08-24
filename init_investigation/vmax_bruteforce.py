import os, sys, time, argparse, struct, fcntl, termios, select, json, threading

RESULTS_DIR = "/home/tor/pc-case-lcd/bruteforce_results"
os.makedirs(RESULTS_DIR, exist_ok=True)

USBMON_NODE = "/dev/usbmon1"

def calculate_crc(data: bytes) -> int:
    # DLL BaseFrame::CalculateCRC IL disassembly returns 0x0000 by default.
    return 0x0000

def build_frame(cmd: int, payload: bytes = b"", ctrl: int = None, use_crc: bool = False) -> bytes:
    # Header: 'A' 'H' (0x41 0x48)
    header = b"\x41\x48"
    
    # CTRL calculation per DLL: 2 + len(payload)
    if ctrl is None:
        ctrl_val = 2 + len(payload)
        if use_crc:
            ctrl_val |= 0x8000
    else:
        ctrl_val = ctrl

    ctrl_bytes = struct.pack(">H", ctrl_val)
    cmd_bytes = struct.pack(">H", cmd)
    
    body = ctrl_bytes + cmd_bytes + payload
    
    if use_crc:
        crc_val = calculate_crc(body)
        crc_bytes = struct.pack(">H", crc_val)
    else:
        crc_bytes = b"\x00\x00"

    footer = b"\x4D\x49" # 'M' 'I'
    return header + ctrl_bytes + cmd_bytes + payload + crc_bytes + footer

class UsbmonMonitor:
    def __init__(self):
        self.lines = []
        self.running = False
        self.thread = None

    def start(self):
        self.lines = []
        self.running = True
        self.thread = threading.Thread(target=self._read)
        self.thread.daemon = True
        self.thread.start()

    def _read(self):
        try:
            with open(USBMON_NODE, 'rb') as f:
                while self.running:
                    l = f.readline()
                    if not l: break
                    str_l = l.decode('latin1', errors='ignore').strip()
                    if " 1:002:" in str_l or "1:002:" in str_l or "1:009:" in str_l:
                        self.lines.append(str_l)
        except Exception:
            pass

    def stop(self):
        self.running = False
        time.sleep(0.05)
        return list(self.lines)

def run_fuzzing_session(device, items, send=False, timeout_sec=3.0, delay_ms=300, use_crc=False, log_usbmon=True, repeat=1):
    print(f"\n=======================================================")
    print(f"=== VMAX SAFE BRUTE-FORCE HARNESS ===")
    print(f"Device: {device} | Total Frames: {len(items)} x {repeat} | Send Mode: {send} | Delay: {delay_ms}ms | CRC: {use_crc}")
    print(f"=======================================================")

    results = []
    stop_triggered = False
    stop_reason = ""

    log_filename = os.path.join(RESULTS_DIR, f"run_{time.strftime('%Y%m%d_%H%M%S')}.json")

    seq_num = 0
    for r in range(repeat):
        if stop_triggered: break

        for item in items:
            seq_num += 1
            cmd = item['cmd']
            payload = item.get('payload', b"")
            ctrl_override = item.get('ctrl', None)
            
            frame = build_frame(cmd, payload, ctrl=ctrl_override, use_crc=use_crc)
            ctrl_val = struct.unpack(">H", frame[2:4])[0]
            crc_val = struct.unpack(">H", frame[-4:-2])[0]

            print(f"\n[{seq_num}/{len(items) * repeat}] CMD: 0x{cmd:04X} ({cmd}) | Payload Len: {len(payload)}B | CTRL: 0x{ctrl_val:04X} | CRC: 0x{crc_val:04X}")
            print(f"Frame Hex: {frame.hex(' ')}")

            if not send:
                print("  DRY-RUN MODE: Frame not transmitted. Pass --send to enable TX.")
                continue

            if not os.path.exists(device):
                stop_triggered = True
                stop_reason = f"Device node {device} disappeared!"
                print(f"*** CRITICAL STOP: {stop_reason} ***")
                break

            mon = None
            if log_usbmon and os.path.exists(USBMON_NODE):
                mon = UsbmonMonitor()
                mon.start()

            tx_time = time.time()
            bytes_written = 0
            rx_data = bytearray()
            exception_str = ""

            try:
                fd = os.open(device, os.O_RDWR | os.O_NOCTTY | os.O_NONBLOCK)
                attrs = termios.tcgetattr(fd)
                attrs[0], attrs[1] = 0, 0
                attrs[2] = termios.B115200 | termios.CS8 | termios.CREAD | termios.CLOCAL
                attrs[3] = 0
                termios.tcsetattr(fd, termios.TCSANOW, attrs)

                TIOCMSET = 0x5418
                fcntl.ioctl(fd, TIOCMSET, struct.pack('I', 0x002 | 0x004)) # DTR+RTS ON
                termios.tcflush(fd, termios.TCIOFLUSH)

                bytes_written = os.write(fd, frame)
                
                deadline = time.monotonic() + timeout_sec
                while time.monotonic() < deadline:
                    r_fds, _, _ = select.select([fd], [], [], max(0.01, deadline - time.monotonic()))
                    if r_fds:
                        try:
                            b = os.read(fd, 512)
                            if b: rx_data.extend(b)
                        except BlockingIOError:
                            pass
                        if rx_data: break
                os.close(fd)
            except Exception as e:
                exception_str = str(e)
                print(f"  Exception: {e}")

            mon_log = mon.stop() if mon else []

            record = {
                "seq": seq_num,
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(tx_time)),
                "cmd_hex": f"0x{cmd:04X}",
                "cmd_dec": cmd,
                "payload_hex": payload.hex(' '),
                "payload_len": len(payload),
                "ctrl_hex": f"0x{ctrl_val:04X}",
                "crc_hex": f"0x{crc_val:04X}",
                "frame_hex": frame.hex(' '),
                "bytes_written": bytes_written,
                "rx_len": len(rx_data),
                "rx_hex": rx_data.hex(' '),
                "exception": exception_str,
                "usbmon_events": len(mon_log)
            }
            results.append(record)

            if rx_data:
                stop_triggered = True
                stop_reason = f"*** UNEXPECTED RESPONSE RECEIVED! ({len(rx_data)}B): {rx_data.hex(' ')} ***"
                print(stop_reason)
                break

            if exception_str:
                stop_triggered = True
                stop_reason = f"USB/Device Exception occurred: {exception_str}"
                print(f"*** STOP TRIGGERED: {stop_reason} ***")
                break

            time.sleep(max(0.25, delay_ms / 1000.0))

    if send:
        with open(log_filename, 'w') as f:
            json.dump(results, f, indent=2)
        print(f"\nExecution log written to {log_filename}")

    if stop_triggered:
        print(f"\n*** STOP CONDITION MET: {stop_reason} ***")

    return results

def main():
    parser = argparse.ArgumentParser(description="HL VMAX Safe Brute-Force & Protocol Tester")
    parser.add_argument("--send", action="store_true", help="Enable live transmission over serial port (default: dry-run)")
    parser.add_argument("--device", default="/dev/ttyACM0", help="Device path (default /dev/ttyACM0)")
    parser.add_argument("--cmd", type=lambda x: int(x, 0), help="Single command opcode (e.g. 0x0080)")
    parser.add_argument("--payload", type=str, default="", help="Payload in hex string (e.g. '01 00')")
    parser.add_argument("--ctrl", type=lambda x: int(x, 0), help="Override CTRL word")
    parser.add_argument("--crc", action="store_true", help="Enable CRC bit and calculation")
    parser.add_argument("--timeout", type=float, default=3.0, help="RX timeout in seconds (default: 3.0)")
    parser.add_argument("--repeat", type=int, default=1, help="Number of repetitions")
    parser.add_argument("--delay", type=int, default=300, help="Inter-frame delay in ms (min: 250ms)")
    parser.add_argument("--usbmon-log", action="store_true", help="Log usbmon kernel events")

    args = parser.parse_args()

    if args.cmd is not None:
        payload_bytes = bytes.fromhex(args.payload) if args.payload else b""
        items = [{"cmd": args.cmd, "payload": payload_bytes, "ctrl": args.ctrl}]
        run_fuzzing_session(args.device, items, send=args.send, timeout_sec=args.timeout, delay_ms=args.delay, use_crc=args.crc, log_usbmon=args.usbmon_log, repeat=args.repeat)
    else:
        print("VMAX Safe Brute-Force Harness Ready. Pass --cmd or run phase test scripts.")

if __name__ == "__main__":
    main()
