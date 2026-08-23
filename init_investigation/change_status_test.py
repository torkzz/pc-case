#!/usr/bin/env python3
"""
change_status_test.py
ChangeStatus(STATUS_AHMI=0x20) → Handshake (CMD 0x0080) → GetHardwareInfo (CMD 0x0072)

EVIDENCE BASIS:
  ChangeStatusRequest (from DeviceCommunicationLibrary.il):
    CMD = 0x0071 (113 decimal)
    Content = 1 byte: status value
    ProtocolConstants.STATUS_AHMI = 0x20

  Hypothesis: firmware boots into a state where it ignores protocol requests
  until told to enter AHMI (display application) mode via ChangeStatus(0x20).
  The vendor Vmax.exe calls ChangeStatusAsync but the call site ordering is
  obfuscated (Confuser.Core 1.6.0). This test probes whether ChangeStatus(AHMI)
  before Handshake unblocks the device.

FRAME FORMAT:
  ChangeStatus(STATUS_AHMI=0x20):
    CMD=0x0071, Content=[0x20] (1 byte), CTRL=3 (2+1), CRC=0x0000
    Wire: 41 48 00 03 00 71 20 00 00 4D 49  (11 bytes)

  Expected response CMD: 0x00B1 (ChangeStatusResponse)

USAGE:
  python3 change_status_test.py [--send] [--port /dev/ttyACM0]

STOP: any RX bytes at any step → stop and print full state.
"""

import sys
import time
import argparse

# Frames
# ChangeStatus(STATUS_AHMI=0x20): CMD=0x71, Content=[0x20], CTRL=3
CHANGE_STATUS_AHMI = bytes([0x41, 0x48, 0x00, 0x03, 0x00, 0x71, 0x20, 0x00, 0x00, 0x4D, 0x49])
# ChangeStatus(STATUS_DOWNLOAD_READY=0x10): CMD=0x71, Content=[0x10], CTRL=3
CHANGE_STATUS_DL_READY = bytes([0x41, 0x48, 0x00, 0x03, 0x00, 0x71, 0x10, 0x00, 0x00, 0x4D, 0x49])
# HandshakeRequest: CMD=0x80, Content=[], CTRL=2
HANDSHAKE_FRAME = bytes([0x41, 0x48, 0x00, 0x02, 0x00, 0x80, 0x00, 0x00, 0x4D, 0x49])
# GetHardwareInfo: CMD=0x72, Content=[], CTRL=2
HWINFO_FRAME    = bytes([0x41, 0x48, 0x00, 0x02, 0x00, 0x72, 0x00, 0x00, 0x4D, 0x49])


def wait_for_frame(port, timeout_s: float) -> bytes:
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


def main():
    parser = argparse.ArgumentParser(description="ChangeStatus(AHMI) → Handshake test")
    parser.add_argument("--send",    action="store_true")
    parser.add_argument("--port",    default="/dev/ttyACM0")
    parser.add_argument("--baud",    type=int, default=115200)
    parser.add_argument("--timeout", type=float, default=3.0)
    args = parser.parse_args()

    print("=" * 60)
    print("TEST PLAN — ChangeStatus(AHMI) → Handshake → GetHardwareInfo")
    print("=" * 60)
    print(f"PORT:    {args.port}")
    print(f"BAUD:    {args.baud}")
    print(f"MODE:    {'LIVE SEND' if args.send else 'DRY RUN'}")
    print()
    print("STEP 1: Open port, DTR=False, RTS=False, settle 100ms")
    print()
    print(f"STEP 2: ChangeStatus(STATUS_AHMI=0x20) — CMD=0x0071, Content=[0x20]")
    print(f"        TX: {CHANGE_STATUS_AHMI.hex(' ').upper()}")
    print(f"        Expected response: CMD=0x00B1 (ChangeStatusResponse)")
    print(f"        Wait {args.timeout}s")
    print()
    print(f"STEP 3: HandshakeRequest — CMD=0x0080")
    print(f"        TX: {HANDSHAKE_FRAME.hex(' ').upper()}")
    print(f"        Expected response: CMD=0x00C0 (HandshakeResponse)")
    print(f"        Wait {args.timeout}s")
    print()
    print(f"STEP 4: GetHardwareInfo — CMD=0x0072 (only if step 3 responded)")
    print(f"        TX: {HWINFO_FRAME.hex(' ').upper()}")
    print(f"        Expected response: CMD=0x00B2 (GetHardwareInfoResponse)")
    print()
    print("HYPOTHESIS: Firmware ignores Handshake until told to enter AHMI mode.")
    print()

    if not args.send:
        print("→ DRY RUN: add --send to transmit.")
        return 0

    try:
        import serial
    except ImportError:
        print("ERROR: pyserial not installed")
        return 1

    import os
    if not os.path.exists(args.port):
        print(f"ERROR: {args.port} not found")
        return 1

    try:
        port = serial.Serial(
            port=None, baudrate=args.baud, bytesize=8, parity='N', stopbits=1,
            timeout=args.timeout, xonxoff=False, rtscts=False, dsrdtr=False)
        port.port = args.port
        port.open()
    except Exception as e:
        print(f"ERROR opening port: {e}")
        return 1

    try:
        port.dtr = False
        port.rts = False
        time.sleep(0.1)
        port.reset_input_buffer()
        port.reset_output_buffer()
        print(f"Port open. DTR=False RTS=False  DSR={port.dsr} CTS={port.cts} DCD={port.cd}\n")

        for step, label, frame, expect_cmd in [
            (2, "ChangeStatus(STATUS_AHMI=0x20)", CHANGE_STATUS_AHMI, 0x00B1),
            (3, "HandshakeRequest",                HANDSHAKE_FRAME,     0x00C0),
        ]:
            print(f"── STEP {step}: {label} ─────────────────────────────────────")
            print(f"TX ({len(frame)} bytes): {frame.hex(' ').upper()}")
            t0 = time.time()
            port.write(frame)
            rx = wait_for_frame(port, args.timeout)
            elapsed = time.time() - t0
            print(f"Elapsed: {elapsed:.3f}s")
            if rx:
                print()
                print("!" * 60)
                print(f"STOP: RX BYTES after {label}")
                print("!" * 60)
                print(f"RX ({len(rx)} bytes): {rx.hex(' ').upper()}")
                if len(rx) >= 6:
                    cmd = (rx[4] << 8) | rx[5]
                    print(f"CMD: 0x{cmd:04X}  (expected 0x{expect_cmd:04X})  {'MATCH' if cmd == expect_cmd else 'MISMATCH'}")
                print()
                # If handshake succeeded, try GetHardwareInfo
                if step == 3 and len(rx) >= 6 and (rx[4] << 8 | rx[5]) == 0x00C0:
                    print(f"── STEP 4: GetHardwareInfo ──────────────────────────────────")
                    print(f"TX ({len(HWINFO_FRAME)} bytes): {HWINFO_FRAME.hex(' ').upper()}")
                    port.reset_input_buffer()
                    time.sleep(0.25)
                    t0 = time.time()
                    port.write(HWINFO_FRAME)
                    rx_hw = wait_for_frame(port, args.timeout)
                    elapsed = time.time() - t0
                    print(f"Elapsed: {elapsed:.3f}s")
                    if rx_hw:
                        print(f"RX ({len(rx_hw)} bytes): {rx_hw.hex(' ').upper()}")
                    else:
                        print("RX: EMPTY")
                return 0
            else:
                print(f"RX: EMPTY")
            port.reset_input_buffer()
            time.sleep(0.25)
            print()

        print("=" * 60)
        print("RESULT: NO RESPONSE to either command")
        print("INTERPRETATION: ChangeStatus(AHMI) → Handshake hypothesis falsified")
        print()
        print("NEXT HIGHEST-VALUE EXPERIMENTS:")
        print()
        print("  A) Capture usbmon — confirm EP 0x81 IN URBs produce 0 bytes from device")
        print("     (critical: distinguish device-silent vs data-loss in Linux path)")
        print()
        print("  B) Try DTR=True before Handshake (some firmware: DTR=1 = host connected)")
        print("     import serial; p=serial.Serial('/dev/ttyACM0',115200,timeout=3)")
        print("     p.dtr=True; p.rts=False; p.write(b'\\x41\\x48\\x00\\x02\\x00\\x80\\x00\\x00\\x4D\\x49')")
        print("     print(p.read(32).hex())")
        print()
        print("  C) Try de4dot on Vmax.exe to deobfuscate call sequence:")
        print("     mono de4dot.exe Vmax.exe  # or wine de4dot.exe Vmax.exe")
        print("     Then recheck the exact ChangeStatus call position.")
        print()
        print("  D) Check EP 0x83 SERIAL_STATE bytes (modem status notification)")
        print("     from cdc_acm — DCD bit may indicate device readiness state.")

    except Exception as e:
        print(f"\nERROR: {e}")
    finally:
        try:
            port.close()
            print("\nPort closed.")
        except Exception:
            pass

    return 0


if __name__ == "__main__":
    sys.exit(main())
