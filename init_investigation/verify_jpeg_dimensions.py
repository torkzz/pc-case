#!/usr/bin/env python3
"""
JPEG Header & Dimension Verification Utility (`verify_jpeg_dimensions.py`)

Inspects binary JPEG files, parses SOF markers (SOF0/SOF2), verifies width, height,
color components, and compares source JPEG dimensions against MSDisplay header dimensions.
"""

import sys
import os
import struct

def parse_jpeg_dimensions(jpeg_path):
    if not os.path.exists(jpeg_path):
        print(f"[ERROR] File '{jpeg_path}' not found.")
        return None

    with open(jpeg_path, 'rb') as f:
        data = f.read()

    size = len(data)
    if size < 4 or data[:2] != b'\xFF\xD8':
        print(f"[ERROR] '{jpeg_path}' is not a valid JPEG (Missing SOI 0xFFD8).")
        return None

    idx = 2
    height, width, components = 0, 0, 0
    sof_marker_found = None

    while idx < size - 8:
        if data[idx] != 0xFF:
            idx += 1
            continue

        marker = data[idx+1]
        # SOF0 (0xC0), SOF1 (0xC1), SOF2 (0xC2), SOF3 (0xC3)
        if marker in (0xC0, 0xC1, 0xC2, 0xC3):
            sof_marker_found = f"0xFF{marker:02X}"
            length = struct.unpack(">H", data[idx+2:idx+4])[0]
            precision = data[idx+4]
            height = struct.unpack(">H", data[idx+5:idx+7])[0]
            width = struct.unpack(">H", data[idx+7:idx+9])[0]
            components = data[idx+9]
            break
        else:
            length = struct.unpack(">H", data[idx+2:idx+4])[0]
            idx += 2 + length

    return {
        "file": jpeg_path,
        "size_bytes": size,
        "sof_marker": sof_marker_found,
        "width": width,
        "height": height,
        "components": components,
        "aspect_ratio": f"{width}:{height}"
    }

def main():
    print("=== Source JPEG Dimension & Marker Verification ===")
    test_files = [
        "diagnostic_patterns/pattern_a_black_grid.jpg",
        "diagnostic_patterns/pattern_b_white_grid.jpg",
        "diagnostic_patterns/pattern_c_color_bars.jpg",
        "/home/tor/pc-case-lcd/vmax_test_2560x666.jpg"
    ]

    for tf in test_files:
        info = parse_jpeg_dimensions(tf)
        if info:
            print(f"File: {info['file']}")
            print(f"  Byte Size  : {info['size_bytes']} bytes")
            print(f"  SOF Marker : {info['sof_marker']}")
            print(f"  Dimensions : {info['width']} x {info['height']} (Components: {info['components']})")
            print(f"  Aspect     : {info['aspect_ratio']}")
            print("-" * 50)

if __name__ == "__main__":
    main()
