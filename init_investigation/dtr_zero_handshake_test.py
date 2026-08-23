#!/usr/bin/env python3
"""
dtr_zero_handshake_test.py
Phase 10 experiment: Test HandshakeRequest with DTR=0 (matching Windows SerialPort default).

EVIDENCE BASIS:
- Vendor IL: Connect() never sets DtrEnable — Windows SerialPort default = false
- Windows usbser.sys: sends SET_CONTROL_LINE_STATE(wValue=0x0000) on Open()
- Linux cdc_acm: asserts DTR=1 by default on port open
- This is the strongest identified discrepancy between Windows and Linux behavior.

USAGE:
  python3 dtr_zero_handshake_test.py [--send] [--port /dev/ttyACM0]

Without --send: prints planned operations, does not transmit.
With --send: executes the experiment.
"""

import sys
import time
import argparse

def main():
    parser = argparse.ArgumentParser(description="DTR=0 HandshakeRequest test")
    parser.add_argument("--send", action="store_true", help="Actually send (default: dry-run)")
    parser.add_argument("--port", default="/dev/ttyACM0", help="Serial port")
    parser.add_argument("--baud", type=int, default=115200)
    parser.add_argument("--timeout", type=float, default=2.0, help="RX wait seconds")
    parser.add_argument("--exit-first", action="store_true",
                        help="Send ExitRunning (CMD 0x0063) before Handshake")
    args = parser.parse_args()

    # ── Frame definitions ──────────────────────────────────────────────────────
    #
    # Frame format (from BaseFrame.ToBytes() IL):
    #   [0x41][0x48][CTRL_H][CTRL_L][CMD_H][CMD_L][content...][CRC_H][CRC_L][0x4D][0x49]
    #   CTRL = 2 + len(content)
    #   CRC  = 0x0000 (always, IsCRCEnabled=false)
    #
    # HandshakeRequest: CMD=0x0080, content=[]  → CTRL=0x0002
    handshake_frame = bytes([0x41, 0x48, 0x00, 0x02, 0x00, 0x80, 0x00, 0x00, 0x4D, 0x49])

    # ExitRunningRequest: CMD=0x0063, content=[] → CTRL=0x0002
    # ExitRunning is fire-and-forget (SendFrameWithRetry, no response awaited)
    exit_frame = bytes([0x41, 0x48, 0x00, 0x02, 0x00, 0x63, 0x00, 0x00, 0x4D, 0x49])

    # ── Print planned operations ───────────────────────────────────────────────
    print("=" * 60)
    print("TEST PLAN")
    print("=" * 60)
    print(f"PORT:     {args.port}")
    print(f"BAUD:     {args.baud}")
    print(f"MODE:     {'LIVE SEND' if args.send else 'DRY RUN (no transmission)'}")
    print()

    if args.exit_first:
        print("OPERATION 1: ExitRunning (CMD=0x0063, fire-and-forget)")
        print(f"  bmRequestType: N/A (application-layer, not control transfer)")
        print(f"  DATA:          {exit_frame.hex(' ').upper()}")
        print(f"  DELAY AFTER:   1000ms")
        print()

    print("OPERATION: HandshakeRequest")
    print(f"  CLASS:         HandshakeRequest")
    print(f"  CMD:           0x0080")
    print(f"  CTRL:          0x0002")
    print(f"  CONTENT:       [] (empty)")
    print(f"  CRC:           0x0000 (disabled)")
    print(f"  DATA:          {handshake_frame.hex(' ').upper()}")
    print()
    print("SETUP:")
    print("  DTR:           FALSE (explicitly cleared — matches Windows SerialPort default)")
    print("  RTS:           FALSE (explicitly cleared — matches Windows SerialPort default)")
    print("  DELAY AFTER OPEN: 100ms (settle)")
    print()
    print("EXPECTED RESPONSE:")
    print("  CMD:           0x00C0 (192 decimal)")
    print("  FORMAT:        41 48 [CTRL_H] [CTRL_L] 00 C0 [MaxPackageSize:4 bytes big-endian] 00 00 4D 49")
    print("  MIN LENGTH:    10 bytes")
    print()

    if not args.send:
        print("  → DRY RUN: not sending. Add --send to transmit.")
        return 0

    # ── Live execution ─────────────────────────────────────────────────────────
    try:
        import serial
    except ImportError:
        print("ERROR: pyserial not installed. Run: pip install pyserial")
        return 1

    import os
    if not os.path.exists(args.port):
        print(f"ERROR: {args.port} does not exist")
        print("  Ensure device is connected and /dev/ttyACM0 is present.")
        print("  (This sandbox lacks the device node — run on host system.)")
        return 1

    print("Opening port...")
    try:
        port = serial.Serial(
            port=None,       # don't open yet
            baudrate=args.baud,
            bytesize=8,
            parity='N',
            stopbits=1,
            timeout=args.timeout,
            xonxoff=False,
            rtscts=False,
            dsrdtr=False,    # do NOT automatically assert DTR
        )
        port.port = args.port
        port.open()
    except Exception as e:
        print(f"ERROR opening port: {e}")
        return 1

    try:
        # Explicitly clear DTR and RTS immediately after open
        # This sends SET_CONTROL_LINE_STATE(wValue=0x0000) via cdc_acm
        print("Setting DTR=False, RTS=False (SET_CONTROL_LINE_STATE wValue=0x0000)...")
        port.dtr = False
        port.rts = False
        time.sleep(0.1)

        # Flush any pending input
        port.reset_input_buffer()
        port.reset_output_buffer()

        if args.exit_first:
            print(f"\nSENDING ExitRunning: {exit_frame.hex(' ').upper()}")
            port.write(exit_frame)
            print("Waiting 1000ms (vendor retry interval)...")
            time.sleep(1.0)
            rx = port.read(port.in_waiting or 1)
            if rx:
                print(f"  RX after ExitRunning: {rx.hex(' ').upper()}")
            else:
                print("  RX after ExitRunning: EMPTY (expected for fire-and-forget)")
            port.reset_input_buffer()
            time.sleep(0.25)

        print(f"\nSENDING HandshakeRequest: {handshake_frame.hex(' ').upper()}")
        port.write(handshake_frame)
        start = time.time()
        print(f"Waiting up to {args.timeout}s for response...")

        # Read with extended timeout
        rx = bytearray()
        deadline = time.time() + args.timeout
        while time.time() < deadline:
            chunk = port.read(port.in_waiting or 1)
            if chunk:
                rx.extend(chunk)
                # Check for complete frame (ends with 4D 49)
                if len(rx) >= 10 and rx[-2:] == b'\x4D\x49':
                    break
            time.sleep(0.01)

        elapsed = time.time() - start

        print()
        print("=" * 60)
        print("RESULT")
        print("=" * 60)
        print(f"RX bytes ({len(rx)}): {bytes(rx).hex(' ').upper() if rx else 'EMPTY'}")
        print(f"Elapsed: {elapsed:.3f}s")

        if not rx:
            print("RESULT: NO RESPONSE")
            print()
            print("Possible causes:")
            print("  1. Firmware still not responding — try --exit-first")
            print("  2. DTR state is correct but ExitRunning needed first")
            print("  3. Firmware requires a different first command")
            print("  4. Firmware has additional undiscovered state requirement")
        else:
            print("RESULT: DATA RECEIVED")
            if len(rx) >= 10 and rx[0] == 0x41 and rx[1] == 0x48:
                cmd = (rx[4] << 8) | rx[5]
                print(f"  SOF: 41 48 ✓")
                print(f"  CMD: 0x{cmd:04X} (expected 0x00C0 = {0x00C0})")
                if cmd == 0x00C0:
                    print("  ✓ HANDSHAKE RESPONSE RECEIVED!")
                    if len(rx) >= 14:
                        content = rx[6:len(rx)-4]
                        if len(content) >= 4:
                            max_pkg = (content[0]<<24)|(content[1]<<16)|(content[2]<<8)|content[3]
                            print(f"  MaxPackageSize: {max_pkg}")
                else:
                    print(f"  ! Unexpected CMD. Full frame: {bytes(rx).hex(' ').upper()}")
            else:
                print(f"  ! Not a valid AH frame. Raw: {bytes(rx).hex(' ').upper()}")

        # Check DTR/RTS/modem signals
        print()
        print("MODEM SIGNALS:")
        print(f"  DSR: {port.dsr}")
        print(f"  CTS: {port.cts}")
        print(f"  DCD: {port.cd}")
        print(f"  RI:  {port.ri}")

    finally:
        port.close()
        print("\nPort closed.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
