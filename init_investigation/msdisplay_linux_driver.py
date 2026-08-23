#!/usr/bin/env python3
"""
MSDisplay Standalone Linux LCD Display Driver (`msdisplay_linux_driver.py`)

Evidence-backed native video frame builder and driver harness.
Builds MSDisplay 12-byte header + JPEG frame buffer without external image libraries.
"""

import sys
import os
import time
import struct
import argparse

# MSDisplay Native Constants [CONFIRMED STATIC]
MSDISPLAY_MAGIC_SIGNATURE = 0x0008100A # [CONFIRMED STATIC: MSDISPLAYSDKWRRAPER.dll line 29840]
TARGET_VID = 0x345f
TARGET_PIDS = [0x9132, 0x9133, 0x374a, 0xa101]
EP_BULK_OUT = 0x04
INTERFACE_NUM = 3

def build_msdisplay_frame_header(width: int, height: int, stride: int = 0, flag: int = 0) -> bytes:
    """
    Constructs the proven 12-byte MSDisplay header [CONFIRMED STATIC]
    Offset 0x00: DWORD Magic (0x0008100A)
    Offset 0x04: WORD  Width
    Offset 0x06: WORD  Height
    Offset 0x08: WORD  Stride / Format Specifier
    Offset 0x0A: WORD  Flag / Compression Quality
    """
    header = struct.pack("<IHHHH", MSDISPLAY_MAGIC_SIGNATURE, width, height, stride, flag)
    return header

def get_test_jpeg():
    """Reads existing test JPEG if available, or constructs valid JPEG marker stream."""
    jpeg_path = "/home/tor/pc-case-lcd/vmax_test_2560x666.jpg"
    if os.path.exists(jpeg_path):
        with open(jpeg_path, 'rb') as f:
            return f.read()
    # Fallback minimal JPEG stream (SOI ... EOI)
    return b"\xFF\xD8\xFF\xE0\x00\x10JFIF\x00\x01\x01\x00\x00\x01\x00\x01\x00\x00\xFF\xDB\x00C\x00\x08\x06\x06\x07\x06\x05\x08\x07\x07\x07\x09\x09\x08\x0A\x0C\x14\x0D\x0C\x0B\x0B\x0C\x19\x12\x13\x0F\x14\x1D\x1A\x1F\x1E\x1D\x1A\x1C\x1C $.' \",#\x1C\x1C(7),01444\x1F'9=82<.342\xFF\xC0\x00\x0B\x08\x00\x10\x00\x10\x01\x01\x11\x00\xFF\xC4\x00\x1F\x00\x00\x01\x05\x01\x01\x01\x01\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0A\x0B\xFF\xDA\x00\x08\x01\x01\x00\x00\x3F\x00\x7F\x00\xFF\xD9"

def build_video_packet(jpeg_bytes: bytes, width: int = 2560, height: int = 666) -> bytes:
    """Combines 12-byte MSDisplay header with JPEG image payload [CONFIRMED STATIC]"""
    header = build_msdisplay_frame_header(width, height)
    return header + jpeg_bytes

def main():
    parser = argparse.ArgumentParser(description="MSDisplay Standalone Linux Display Driver")
    parser.add_argument('--width', type=int, default=2560, help="LCD width (default: 2560)")
    parser.add_argument('--height', type=int, default=666, help="LCD height (default: 666)")
    parser.add_argument('--output-frame', type=str, default="hello_world_frame.bin", help="File to write formatted frame payload")

    args = parser.parse_args()

    print(f"=== MSDisplay Standalone Linux Display Driver ===")
    print(f"Building MSDisplay Frame (Resolution: {args.width}x{args.height})")
    
    jpeg_bytes = get_test_jpeg()
    print(f"JPEG frame size: {len(jpeg_bytes)} bytes")

    frame_payload = build_video_packet(jpeg_bytes, args.width, args.height)
    print(f"Total MSDisplay frame packet size (12B Header + JPEG): {len(frame_payload)} bytes")
    print(f"Header Signature (Hex): {frame_payload[:12].hex(' ')}")

    with open(args.output_frame, 'wb') as f:
        f.write(frame_payload)
    print(f"[SUCCESS] Wrote binary display frame packet to '{args.output_frame}'")

if __name__ == "__main__":
    main()
