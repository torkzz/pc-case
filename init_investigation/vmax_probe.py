#!/usr/bin/env python3
"""
HL VMAX PC-Case LCD Safe Diagnostic Probe Tool (Task 10)
Provides read-only probing, single-frame handshake validation, and hex logging.
DEFAULT MODE IS READ-ONLY. DO NOT SEND UNVERIFIED FRAMEBUFFER DATA.
"""

import sys
import os
import time
import argparse
from vmax_protocol import handshake_request, parse_handshake_response, hardware_info_request, parse_hardware_info_response

DEV_ACM = "/dev/ttyACM0"

def log(msg):
    ts = time.strftime("%H:%M:%S")
    print(f"[{ts}] {msg}")

def cmd_probe(args):
    log("=== RUNNING SAFE READ-ONLY PROBE ===")
    if not os.path.exists(DEV_ACM):
        log(f"Device node {DEV_ACM} not found.")
        return
    log(f"Device node {DEV_ACM} exists. Access mode: {oct(os.stat(DEV_ACM).st_mode)}")
    log("Read-only probe complete. No bytes were transmitted.")

def cmd_handshake(args):
    log("=== EXECUTING CONTROLLED SINGLE HANDSHAKE ===")
    if not os.path.exists(DEV_ACM):
        log(f"ERROR: {DEV_ACM} not found.")
        return

    import termios
    import select

    tx_bytes = handshake_request()
    log(f"TX ({len(tx_bytes)} bytes): {tx_bytes.hex(' ')}")

    if not args.execute:
        log("DRY RUN MODE: Add --execute flag to transmit handshake frame over serial.")
        return

    fd = os.open(DEV_ACM, os.O_RDWR | os.O_NOCTTY | os.O_NONBLOCK)
    try:
        attrs = termios.tcgetattr(fd)
        attrs[0], attrs[1], attrs[2], attrs[3] = 0, 0, termios.CS8 | termios.CREAD | termios.CLOCAL, 0
        termios.tcsetattr(fd, termios.TCSANOW, attrs)

        os.write(fd, tx_bytes)
        log("TX Frame Written. Waiting 2.0s for response...")

        deadline = time.monotonic() + 2.0
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

        log(f"RX ({len(rx)} bytes): {bytes(rx).hex(' ') if rx else '<NO RESPONSE / TIMEOUT>'}")
        if rx:
            try:
                res = parse_handshake_response(bytes(rx))
                log(f"Handshake Parsed: MaxPackageSize={res['max_package_size']} (CRC Valid: {res['crc_valid']})")
            except Exception as e:
                log(f"Handshake Parse Error: {e}")
    finally:
        os.close(fd)

def main():
    parser = argparse.ArgumentParser(description="HL VMAX LCD Safe Probe Tool")
    subparsers = parser.add_subparsers(dest="command")

    p_probe = subparsers.add_parser("probe", help="Read-only device status check")
    p_hs = subparsers.add_parser("handshake", help="Single handshake request test")
    p_hs.add_argument("--execute", action="store_true", help="Confirm transmission of single handshake frame")

    args = parser.parse_args()
    if args.command == "handshake":
        cmd_handshake(args)
    else:
        cmd_probe(args)

if __name__ == "__main__":
    main()
