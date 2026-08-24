#!/usr/bin/env python3
"""
HL VMAX PC-Case LCD Clean Protocol Driver & Probe Library (Task 10)
Evidence-backed protocol builder, parser, and CLI test tool.
NO DAEMON REQUIRED. USERSPACE PROBE & DISPLAY TEST TOOL.
"""

import sys
import os
import time
import json
import fcntl
import termios
import select
import struct
import argparse

# Evidence Classification Tags
TAG_STATIC = "[CONFIRMED STATIC: DeviceCommunicationLibrary.dll BaseFrame.BuildCTRL]"
TAG_LIVE   = "[CONFIRMED LIVE: Physical /dev/ttyACM0]"

# Protocol Constants
HEADER = b"AH" # 0x41 0x48 [CONFIRMED STATIC]
FOOTER = b"MI" # 0x4D 0x49 [CONFIRMED STATIC]

CMD_HANDSHAKE_REQ         = 0x0080 # [CONFIRMED STATIC]
CMD_HANDSHAKE_RESP        = 0x00C0 # [CONFIRMED STATIC]
CMD_GET_HW_INFO_REQ       = 0x0072 # [CONFIRMED STATIC]
CMD_GET_HW_INFO_RESP       = 0x00B2 # [CONFIRMED STATIC]
CMD_REQUEST_DOWNLOAD_REQ  = 0x0081 # [CONFIRMED STATIC]
CMD_REQUEST_DOWNLOAD_RESP = 0x00C1 # [CONFIRMED STATIC]
CMD_DOWNLOAD_DATA_REQ     = 0x0082 # [CONFIRMED STATIC]
CMD_DOWNLOAD_DATA_RESP     = 0x00C2 # [CONFIRMED STATIC]
CMD_DOWNLOAD_COMPLETE_REQ = 0x008F # [CONFIRMED STATIC]
CMD_DOWNLOAD_COMPLETE_RESP = 0x00CF # [CONFIRMED STATIC]

def crc16_modbus(data: bytes) -> int:
    """Calculates Modbus CRC-16 (Init=0xFFFF, Poly=0xA001) [CONFIRMED STATIC]"""
    crc = 0xFFFF
    for b in data:
        crc ^= b
        for _ in range(8):
            if crc & 1:
                crc = (crc >> 1) ^ 0xA001
            else:
                crc >>= 1
    return crc & 0xFFFF

def build_frame(cmd: int, content: bytes = b"", is_crc_enabled: bool = False) -> bytes:
    """
    Builds AH..MI frame [CONFIRMED STATIC: BaseFrame.BuildCTRL]
    CTRL = CalculateContentLength() = 2 + len(content)
    """
    payload_len = len(content)
    calc_len = payload_len + 2
    ctrl_val = calc_len & 0x0FFF
    if is_crc_enabled:
        ctrl_val |= (1 << 12)

    ctrl_bytes = ctrl_val.to_bytes(2, 'big')
    cmd_bytes = cmd.to_bytes(2, 'big')
    body = ctrl_bytes + cmd_bytes + content

    if is_crc_enabled:
        crc_val = crc16_modbus(body)
        crc_bytes = crc_val.to_bytes(2, 'big')
    else:
        crc_bytes = b"\x00\x00"

    return HEADER + body + crc_bytes + FOOTER

def parse_frame(frame: bytes) -> dict:
    """Parses AH..MI frame [CONFIRMED STATIC: BaseFrame.Parse()]"""
    if len(frame) < 10:
        raise ValueError("Frame size < 10 bytes")
    if frame[:2] != HEADER or frame[-2:] != FOOTER:
        raise ValueError("Invalid AH/MI Header/Footer")

    ctrl = int.from_bytes(frame[2:4], 'big')
    cmd = int.from_bytes(frame[4:6], 'big')
    crc = int.from_bytes(frame[-4:-2], 'big')
    content = frame[6:-4]

    calc_crc = crc16_modbus(frame[2:-4])
    return {
        "ctrl": ctrl,
        "cmd": hex(cmd),
        "content": content,
        "crc_wire": hex(crc),
        "crc_calc": hex(calc_crc),
        "crc_valid": (crc == calc_crc)
    }

def log(msg):
    ts = time.strftime("%H:%M:%S")
    print(f"[{ts}] {msg}")

def main():
    parser = argparse.ArgumentParser(description="HL VMAX LCD Linux Protocol CLI Driver")
    parser.add_argument("--device", default="/dev/ttyACM0", help="Serial device node (default: /dev/ttyACM0)")
    parser.add_argument("--baud", type=int, default=115200, help="Serial baud rate (default: 115200)")
    parser.add_argument("--handshake", action="store_true", help="Send CMD_HANDSHAKE_REQ (0x0080)")
    parser.add_argument("--hardware-info", action="store_true", help="Send CMD_GET_HW_INFO_REQ (0x0072)")
    parser.add_argument("--image", help="Path to JPEG image to send")
    parser.add_argument("--dump-frame", action="store_true", help="Dump generated frame bytes in hex")
    parser.add_argument("--dry-run", action="store_true", help="Build frames without serial dispatch")
    parser.add_argument("--send", action="store_true", help="Confirm physical serial transmission")

    args = parser.parse_args()

    if args.dump_frame or args.dry_run or not args.send:
        frame = build_frame(CMD_HANDSHAKE_REQ)
        log(f"Generated Handshake Frame (TX): {frame.hex(' ')}")
        if args.dry_run or not args.send:
            log("NO TRANSMISSION MODE: Add --send to transmit frame over serial.")
            return

    if not os.path.exists(args.device):
        log(f"ERROR: Serial device {args.device} does not exist!")
        sys.exit(1)

    log(f"Opening {args.device} at {args.baud} baud (115200 8N1 + DTR/RTS)...")
    fd = os.open(args.device, os.O_RDWR | os.O_NOCTTY | os.O_NONBLOCK)
    try:
        attrs = termios.tcgetattr(fd)
        attrs[0], attrs[1], attrs[2], attrs[3] = 0, 0, termios.B115200 | termios.CS8 | termios.CREAD | termios.CLOCAL, 0
        termios.tcsetattr(fd, termios.TCSANOW, attrs)

        # Assert DTR & RTS
        TIOCMGET, TIOCMSET = 0x5415, 0x5418
        TIOCM_DTR, TIOCM_RTS = 0x002, 0x004
        buf = struct.pack('I', 0)
        status = struct.unpack('I', fcntl.ioctl(fd, TIOCMGET, buf))[0] | TIOCM_DTR | TIOCM_RTS
        fcntl.ioctl(fd, TIOCMSET, struct.pack('I', status))

        termios.tcflush(fd, termios.TCIOFLUSH)

        cmd_opcode = CMD_GET_HW_INFO_REQ if args.hardware_info else CMD_HANDSHAKE_REQ
        tx_bytes = build_frame(cmd_opcode)
        log(f"TX Opcode 0x{cmd_opcode:04X} ({len(tx_bytes)} bytes): {tx_bytes.hex(' ')}")
        os.write(fd, tx_bytes)

        log("Waiting for RX response (3.0s bounded timeout)...")
        deadline = time.monotonic() + 3.0
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

        log(f"RX Total Length: {len(rx)} bytes")
        if rx:
            log(f"Raw RX Hex: {bytes(rx).hex(' ')}")
            try:
                parsed = parse_frame(bytes(rx))
                log(f"Parsed Frame: CMD={parsed['cmd']}, CTRL={parsed['ctrl']}, CRC_Valid={parsed['crc_valid']}")
            except Exception as e:
                log(f"Frame parse error: {e}")
        else:
            log("<NO RESPONSE RECEIVED FROM LCD HARDWARE>")

    finally:
        os.close(fd)

if __name__ == "__main__":
    main()
