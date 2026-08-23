#!/usr/bin/env python3
"""
CDC ACM Asset Download Test (`test_cdc_asset_download.py`)
Tests SPI Flash asset download handshake (CMD 0x0081 / 0x0082) over /dev/ttyACM0.
"""

import sys
import os
import time
import struct
import serial

def crc16_modbus(data: bytes) -> int:
    crc = 0xFFFF
    for b in data:
        crc ^= b
        for _ in range(8):
            if crc & 1:
                crc = (crc >> 1) ^ 0xA001
            else:
                crc >>= 1
    return crc & 0xFFFF

def build_frame(cmd: int, content: bytes = b"", is_crc: bool = False) -> bytes:
    payload_len = len(content)
    calc_len = payload_len + 2
    ctrl_val = calc_len & 0x0FFF
    if is_crc:
        ctrl_val |= (1 << 12)

    ctrl_bytes = ctrl_val.to_bytes(2, 'big')
    cmd_bytes = cmd.to_bytes(2, 'big')
    body = ctrl_bytes + cmd_bytes + content

    if is_crc:
        crc_val = crc16_modbus(body)
        crc_bytes = crc_val.to_bytes(2, 'big')
    else:
        crc_bytes = b"\x00\x00"

    return b"AH" + body + crc_bytes + b"MI"

def test_download_handshake(port_path="/dev/ttyACM0"):
    print(f"=== CDC ACM Asset Download Handshake Test ({port_path}) ===")
    if not os.path.exists(port_path):
        print(f"[ERROR] Port {port_path} not found.")
        return

    try:
        ser = serial.Serial(port_path, 115200, timeout=2.0)
        print(f"[SUCCESS] Opened {port_path} at 115200 8N1")

        # CMD 0x0081 RequestDownload: address(4B) + fileSize(4B) + fileId(16B)
        addr = 0x08100000
        size = 27883
        file_id = b"VMAX_TEST_IMG_01" # 16 bytes
        content = struct.pack(">II", addr, size) + file_id

        frame = build_frame(0x0081, content, is_crc=False)
        print(f"Tx RequestDownload (CMD 0x0081): {frame.hex(' ')}")

        ser.reset_input_buffer()
        ser.write(frame)
        ser.flush()

        time.sleep(0.5)
        rx = ser.read(512)
        if rx:
            print(f"Rx Response ({len(rx)} bytes): {rx.hex(' ')}")
        else:
            print("Rx Response: 0 bytes (No response received)")

        ser.close()
    except Exception as e:
        print(f"[ERROR] Serial test error: {e}")

if __name__ == "__main__":
    test_download_handshake()
