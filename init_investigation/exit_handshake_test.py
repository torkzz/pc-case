#!/usr/bin/env python3
"""
exit_handshake_test.py
ExitRunning (CMD 0x0063) → Handshake (CMD 0x0080) → GetHardwareInfo (CMD 0x0072)

EVIDENCE BASIS (from DeviceCommunicationLibrary.il):
  - ExitRunningAsync: SendFrameWithRetryAsync(maxRetries=3, intervalMs=1000ms)
    Returns Task<bool> (write delivery, not response). No response expected.
  - HandshakeAsync:   SendRequestAsync, awaits CMD 0x00C0
    Response: HandshakeResponse { MaxPackageSize: uint32 }
  - GetHardwareInfoAsync: SendRequestAsync, awaits CMD 0x00B2
    Response: GetHardwareInfoResponse { IcId, MaxAcfSize, DisplayHeight, DisplayWidth, ProductId }
  - DTR/RTS: not set by vendor code (Windows SerialPort defaults = false)
  - No delays between commands in vendor IL

FRAME FORMAT (BaseFrame.ToBytes()):
  [0x41][0x48][CTRL_H][CTRL_L][CMD_H][CMD_L][content...][CRC_H][CRC_L][0x4D][0x49]
  CTRL = 2 + len(content); CRC = 0x0000 (IsCRCEnabled=false)
  Minimum frame: 10 bytes

USAGE:
  python3 exit_handshake_test.py [--send] [--port /dev/ttyACM0] [--timeout 3.0]

Without --send: prints planned operations (dry run).
With    --send: executes the experiment.

STOP CONDITIONS (print and exit immediately):
  - Any RX bytes received → STOP, print full state
  - USB error or serial exception → STOP
  - Device disconnect → STOP
"""

import sys
import time
import argparse


# ── Frame definitions ──────────────────────────────────────────────────────────
#
# ExitRunningRequest:    CMD=0x0063, Content=[]  → CTRL=0x0002
EXIT_FRAME    = bytes([0x41, 0x48, 0x00, 0x02, 0x00, 0x63, 0x00, 0x00, 0x4D, 0x49])
#
# HandshakeRequest:      CMD=0x0080, Content=[]  → CTRL=0x0002
HANDSHAKE_FRAME = bytes([0x41, 0x48, 0x00, 0x02, 0x00, 0x80, 0x00, 0x00, 0x4D, 0x49])
#
# GetHardwareInfoRequest: CMD=0x0072, Content=[] → CTRL=0x0002
HWINFO_FRAME  = bytes([0x41, 0x48, 0x00, 0x02, 0x00, 0x72, 0x00, 0x00, 0x4D, 0x49])


def parse_frame(rx: bytes) -> dict:
    """Parse a received AH...MI frame. Returns dict with parsed fields or error."""
    if len(rx) < 10:
        return {"error": f"too short ({len(rx)} bytes)"}
    if rx[0] != 0x41 or rx[1] != 0x48:
        return {"error": f"bad SOF: {rx[0]:02X} {rx[1]:02X}"}
    if rx[-2] != 0x4D or rx[-1] != 0x49:
        return {"error": f"bad EOF: {rx[-2]:02X} {rx[-1]:02X}"}
    ctrl = (rx[2] << 8) | rx[3]
    cmd  = (rx[4] << 8) | rx[5]
    crc  = (rx[-4] << 8) | rx[-3]
    content = bytes(rx[6:len(rx)-4])
    return {"ctrl": ctrl, "cmd": cmd, "crc": crc, "content": content.hex(' ').upper()}


def parse_handshake_response(rx: bytes) -> str:
    f = parse_frame(rx)
    if "error" in f:
        return f"PARSE ERROR: {f['error']}"
    if f["cmd"] != 0x00C0:
        return f"CMD MISMATCH: got 0x{f['cmd']:04X}, expected 0x00C0"
    content_hex = f["content"]
    content_bytes = bytes.fromhex(content_hex.replace(' ', ''))
    if len(content_bytes) >= 4:
        max_pkg = (content_bytes[0]<<24)|(content_bytes[1]<<16)|(content_bytes[2]<<8)|content_bytes[3]
        return f"HandshakeResponse: CMD=0x{f['cmd']:04X}  MaxPackageSize={max_pkg}  (0x{max_pkg:08X})"
    return f"HandshakeResponse: CMD=0x{f['cmd']:04X}  content=[{content_hex}]"


def parse_hwinfo_response(rx: bytes) -> str:
    f = parse_frame(rx)
    if "error" in f:
        return f"PARSE ERROR: {f['error']}"
    if f["cmd"] != 0x00B2:
        return f"CMD MISMATCH: got 0x{f['cmd']:04X}, expected 0x00B2"
    content_bytes = bytes.fromhex(f["content"].replace(' ', '')) if f["content"] else b''
    # GetHardwareInfoResponse fields (from IL): IcId(4), MaxAcfSize(4), Height(4), Width(4), ProductId(32)
    fields = {}
    if len(content_bytes) >= 4:
        fields["IcId"] = f"0x{int.from_bytes(content_bytes[0:4], 'big'):08X}"
    if len(content_bytes) >= 8:
        fields["MaxAcfSize"] = int.from_bytes(content_bytes[4:8], 'big')
    if len(content_bytes) >= 12:
        fields["DisplayHeight"] = int.from_bytes(content_bytes[8:12], 'big')
    if len(content_bytes) >= 16:
        fields["DisplayWidth"] = int.from_bytes(content_bytes[12:16], 'big')
    if len(content_bytes) >= 48:
        try:
            fields["ProductId"] = content_bytes[16:48].decode('utf-8', errors='replace').rstrip('\x00')
        except Exception:
            fields["ProductId"] = content_bytes[16:48].hex()
    return f"GetHardwareInfoResponse: CMD=0x{f['cmd']:04X}  {fields}"


def wait_for_frame(port, timeout_s: float, label: str) -> bytes:
    """Read until complete AH...MI frame or timeout. Returns bytes (empty = timeout)."""
    rx = bytearray()
    deadline = time.time() + timeout_s
    while time.time() < deadline:
        chunk = port.read(port.in_waiting or 1)
        if chunk:
            rx.extend(chunk)
            if len(rx) >= 10 and rx[-2:] == b'\x4D\x49':
                return bytes(rx)
        time.sleep(0.01)
    return bytes(rx)


def print_separator(title=""):
    width = 60
    if title:
        print(f"{'─'*4} {title} {'─'*(width - len(title) - 6)}")
    else:
        print("─" * width)


def main():
    parser = argparse.ArgumentParser(description="ExitRunning → Handshake → GetHardwareInfo test")
    parser.add_argument("--send",    action="store_true", help="Execute (default: dry run)")
    parser.add_argument("--port",    default="/dev/ttyACM0")
    parser.add_argument("--baud",    type=int, default=115200)
    parser.add_argument("--timeout", type=float, default=3.0, help="RX wait per command (seconds)")
    args = parser.parse_args()

    # ── Print test plan ───────────────────────────────────────────────────────
    print("=" * 60)
    print("TEST PLAN — ExitRunning → Handshake → GetHardwareInfo")
    print("=" * 60)
    print(f"PORT:    {args.port}")
    print(f"BAUD:    {args.baud}")
    print(f"MODE:    {'LIVE SEND' if args.send else 'DRY RUN (no transmission)'}")
    print(f"TIMEOUT: {args.timeout}s per command")
    print()

    ops = [
        ("STEP 1", "Open port, DTR=False, RTS=False, settle 100ms",
         None, "SET_CONTROL_LINE_STATE(wValue=0x0000) via cdc_acm"),
        ("STEP 2", "ExitRunning (CMD 0x0063) — fire-and-forget delivery",
         EXIT_FRAME,
         "No response expected. SendFrameWithRetryAsync(maxRetries=3, intervalMs=1000ms) in vendor.\n"
         "         We send once, wait 1000ms (vendor retry interval), check for any RX."),
        ("STEP 3", "HandshakeRequest (CMD 0x0080) — awaits CMD 0x00C0",
         HANDSHAKE_FRAME,
         f"Wait up to {args.timeout}s. Response: HandshakeResponse {{MaxPackageSize:uint32}}"),
        ("STEP 4", "GetHardwareInfoRequest (CMD 0x0072) — awaits CMD 0x00B2",
         HWINFO_FRAME,
         f"Only sent if Handshake received response.\n"
         "         Response: GetHardwareInfoResponse {IcId, MaxAcfSize, Height, Width, ProductId}"),
    ]
    for tag, desc, frame, note in ops:
        print(f"{tag}: {desc}")
        if frame:
            print(f"         TX: {frame.hex(' ').upper()}")
        print(f"         {note}")
        print()

    if not args.send:
        print("→ DRY RUN: add --send to transmit.")
        return 0

    # ── Live execution ────────────────────────────────────────────────────────
    try:
        import serial
    except ImportError:
        print("ERROR: pyserial not installed. Run: pip install pyserial")
        return 1

    import os
    if not os.path.exists(args.port):
        print(f"ERROR: {args.port} not found — run on host (not in sandbox)")
        return 1

    print_separator("OPENING PORT")
    try:
        port = serial.Serial(
            port=None,
            baudrate=args.baud,
            bytesize=8,
            parity='N',
            stopbits=1,
            timeout=args.timeout,
            xonxoff=False,
            rtscts=False,
            dsrdtr=False,    # suppress automatic DTR
        )
        port.port = args.port
        port.open()
    except Exception as e:
        print(f"ERROR opening port: {e}")
        return 1

    results = {}

    try:
        # DTR=False, RTS=False immediately after open
        port.dtr = False
        port.rts = False
        time.sleep(0.1)
        port.reset_input_buffer()
        port.reset_output_buffer()
        print(f"Port open. DTR=False, RTS=False. DSR={port.dsr}  CTS={port.cts}  DCD={port.cd}  RI={port.ri}")
        print()

        # ── STEP 2: ExitRunning ───────────────────────────────────────────────
        print_separator("STEP 2 — ExitRunning CMD=0x0063")
        print(f"TX ({len(EXIT_FRAME)} bytes): {EXIT_FRAME.hex(' ').upper()}")
        t0 = time.time()
        port.write(EXIT_FRAME)
        print(f"Written. Waiting 1000ms (vendor retry interval)...")
        time.sleep(1.0)
        raw = port.read(port.in_waiting or 0)
        elapsed = time.time() - t0
        if raw:
            print()
            print("!" * 60)
            print("STOP CONDITION: RX BYTES RECEIVED AFTER ExitRunning")
            print("!" * 60)
            print(f"RX ({len(raw)} bytes): {raw.hex(' ').upper()}")
            print(f"Elapsed: {elapsed:.3f}s")
            print(f"TX was: {EXIT_FRAME.hex(' ').upper()}")
            results["exit_rx"] = raw.hex(' ').upper()
            results["stop_reason"] = "RX after ExitRunning"
            return _report(results, port)
        else:
            print(f"RX: EMPTY (expected — ExitRunning is fire-and-forget)")
            results["exit_rx"] = "EMPTY"
        port.reset_input_buffer()
        time.sleep(0.25)
        print()

        # ── STEP 3: HandshakeRequest ──────────────────────────────────────────
        print_separator("STEP 3 — HandshakeRequest CMD=0x0080")
        print(f"TX ({len(HANDSHAKE_FRAME)} bytes): {HANDSHAKE_FRAME.hex(' ').upper()}")
        t0 = time.time()
        port.write(HANDSHAKE_FRAME)
        print(f"Written. Waiting up to {args.timeout}s for CMD=0x00C0 response...")
        rx_hs = wait_for_frame(port, args.timeout, "Handshake")
        elapsed = time.time() - t0
        print(f"Elapsed: {elapsed:.3f}s")
        if rx_hs:
            print()
            print("!" * 60)
            print("STOP CONDITION: RX BYTES RECEIVED AFTER HandshakeRequest")
            print("!" * 60)
            print(f"RX ({len(rx_hs)} bytes): {rx_hs.hex(' ').upper()}")
            print(f"Parsed: {parse_handshake_response(rx_hs)}")
            results["handshake_rx"] = rx_hs.hex(' ').upper()
            results["handshake_parsed"] = parse_handshake_response(rx_hs)
            results["stop_reason"] = "RX after HandshakeRequest"
            # Still try GetHardwareInfo if handshake response was valid
            if b'\x41\x48' in rx_hs and rx_hs[-2:] == b'\x4D\x49':
                f = parse_frame(rx_hs)
                if f.get("cmd") == 0x00C0:
                    print()
                    print_separator("STEP 4 — GetHardwareInfoRequest CMD=0x0072")
                    print(f"TX ({len(HWINFO_FRAME)} bytes): {HWINFO_FRAME.hex(' ').upper()}")
                    port.reset_input_buffer()
                    time.sleep(0.25)
                    t0 = time.time()
                    port.write(HWINFO_FRAME)
                    print(f"Written. Waiting up to {args.timeout}s for CMD=0x00B2 response...")
                    rx_hw = wait_for_frame(port, args.timeout, "GetHardwareInfo")
                    elapsed = time.time() - t0
                    print(f"Elapsed: {elapsed:.3f}s")
                    if rx_hw:
                        print(f"RX ({len(rx_hw)} bytes): {rx_hw.hex(' ').upper()}")
                        print(f"Parsed: {parse_hwinfo_response(rx_hw)}")
                        results["hwinfo_rx"] = rx_hw.hex(' ').upper()
                        results["hwinfo_parsed"] = parse_hwinfo_response(rx_hw)
                    else:
                        print("RX: EMPTY (GetHardwareInfo timed out)")
                        results["hwinfo_rx"] = "EMPTY"
            return _report(results, port)
        else:
            print(f"RX: EMPTY")
            results["handshake_rx"] = "EMPTY"
        print()

        # ── STEP 4 skipped (no handshake response) ───────────────────────────
        print_separator("STEP 4 — GetHardwareInfo SKIPPED (no Handshake response)")
        results["hwinfo_rx"] = "SKIPPED"
        print()

    except serial.SerialException as e:
        print(f"\nSERIAL ERROR: {e}")
        results["serial_error"] = str(e)
    except Exception as e:
        print(f"\nERROR: {e}")
        results["error"] = str(e)

    return _report(results, port)


def _report(results: dict, port) -> int:
    print()
    print("=" * 60)
    print("RESULT SUMMARY")
    print("=" * 60)
    print()

    exit_rx = results.get("exit_rx", "NOT RUN")
    hs_rx   = results.get("handshake_rx", "NOT RUN")
    hw_rx   = results.get("hwinfo_rx", "NOT RUN")

    print("TEST                           | TX FRAME              | RX")
    print("─" * 70)
    print(f"ExitRunning (0x0063)           | {EXIT_FRAME.hex(' ').upper():21s} | {exit_rx}")
    print(f"HandshakeRequest (0x0080)      | {HANDSHAKE_FRAME.hex(' ').upper():21s} | {hs_rx}")
    print(f"GetHardwareInfo (0x0072)       | {HWINFO_FRAME.hex(' ').upper():21s} | {hw_rx}")
    print()

    if "handshake_parsed" in results:
        print(f"Handshake parsed: {results['handshake_parsed']}")
    if "hwinfo_parsed" in results:
        print(f"HwInfo parsed:    {results['hwinfo_parsed']}")
    print()

    # Classification
    any_rx = any(v not in ("EMPTY", "NOT RUN", "SKIPPED") and v for v in [exit_rx, hs_rx, hw_rx])
    if any_rx:
        print("RESULT: DATA RECEIVED")
        print("INTERPRETATION: Device responded. Analyze RX frames above.")
        print("EVIDENCE LEVEL: CONFIRMED (device is responsive)")
        print()
        print("NEXT STEP: Analyze the response frame and continue with GetHardwareInfo if not yet sent.")
    else:
        print("RESULT: NO RESPONSE (all commands: 0 RX bytes)")
        print()
        print("INTERPRETATION:")
        print("  ExitRunning → Handshake sequence produced no response.")
        print("  This contradicts the hypothesis:")
        print("    'Device needs ExitRunning before Handshake'")
        print("  Evidence now against: DTR mismatch AND ExitRunning-first both tried.")
        print()
        print("EVIDENCE LEVEL: STRONGLY SUPPORTED (negative, 2 hypotheses falsified)")
        print()
        print("NEXT HIGHEST-VALUE EXPERIMENTS (in order):")
        print()
        print("  A) Capture usbmon while running this test — verify EP 0x81 IN URBs")
        print("     (distinguish: device sends nothing vs Linux drops the bytes)")
        print("     sudo modprobe usbmon")
        print("     sudo cat /sys/kernel/debug/usb/usbmon/1u  # while running test")
        print()
        print("  B) Try DTR=True (opposite of previous tests) — some firmware boots")
        print("     with DTR=1 as 'host ready' signal, not DTR=0.")
        print("     frame: 41 48 00 02 00 80 00 00 4D 49 with port.dtr=True")
        print()
        print("  C) Try ChangeStatus(STATUS_AHMI=0x20) before Handshake:")
        print("     Wire: 41 48 00 03 00 71 20 00 00 4D 49")
        print("     CTRL=3 (2+1), CMD=0x71, Content=[0x20], CRC=0x0000")
        print("     Hypothesis: firmware boots into a mode where it ignores protocol")
        print("     until told to enter AHMI (display application) mode.")
        print()
        print("  D) Capture EP 0x83 (Interrupt IN) content — SERIAL_STATE notifications")
        print("     may encode device state (e.g., bit 0=DCD=device ready signal).")
        print("     The cdc_acm driver reads these internally — check dmesg for errors.")
        print()
        print("  E) Static analysis of Vmax.exe with a deobfuscator (de4dot) to find")
        print("     the exact call sequence including ChangeStatus ordering.")

    try:
        port.close()
        print("\nPort closed.")
    except Exception:
        pass

    return 0


if __name__ == "__main__":
    sys.exit(main())
