#!/usr/bin/env python3
"""
Solid Color & Line Alignment Frame Generator (`generate_solid_patterns.py`)

Creates 2560x666 diagnostic pattern JPEGs:
- solid_black.jpg (PPM -> JPEG)
- solid_white.jpg
- solid_red.jpg
- solid_green.jpg
- solid_blue.jpg
- alignment_markers.jpg (1px / 8px / 16px horizontal and vertical calibration lines)
"""

import os
import subprocess

WIDTH = 2560
HEIGHT = 666
OUT_DIR = "solid_patterns"
os.makedirs(OUT_DIR, exist_ok=True)

def create_solid_ppm(filename, r, g, b):
    header = f"P6\n{WIDTH} {HEIGHT}\n255\n".encode('ascii')
    pixels = bytes([r, g, b]) * (WIDTH * HEIGHT)
    with open(filename, 'wb') as f:
        f.write(header)
        f.write(pixels)

def create_alignment_ppm(filename):
    header = f"P6\n{WIDTH} {HEIGHT}\n255\n".encode('ascii')
    pixels = bytearray(WIDTH * HEIGHT * 3)

    for y in range(HEIGHT):
        # Draw 1px line at Y=100, 8px band at Y=300, 16px band at Y=500
        is_1px = (y == 100)
        is_8px = (300 <= y < 308)
        is_16px = (500 <= y < 516)

        for x in range(WIDTH):
            idx = (y * WIDTH + x) * 3
            if is_1px:
                pixels[idx] = 255; pixels[idx+1] = 0; pixels[idx+2] = 0 # Red
            elif is_8px:
                pixels[idx] = 0; pixels[idx+1] = 255; pixels[idx+2] = 0 # Green
            elif is_16px:
                pixels[idx] = 0; pixels[idx+1] = 0; pixels[idx+2] = 255 # Blue
            else:
                pixels[idx] = 50; pixels[idx+1] = 50; pixels[idx+2] = 50 # Dark Gray

    with open(filename, 'wb') as f:
        f.write(header)
        f.write(pixels)

def convert_ppm_to_jpeg(ppm_file, jpg_file):
    cmd = ['ffmpeg', '-y', '-i', ppm_file, '-q:v', '2', jpg_file]
    subprocess.check_call(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def main():
    print("=== Generating Solid Color & Alignment Pattern Frames (2560x666) ===")
    colors = {
        'solid_black': (0, 0, 0),
        'solid_white': (255, 255, 255),
        'solid_red': (255, 0, 0),
        'solid_green': (0, 255, 0),
        'solid_blue': (0, 0, 255)
    }

    for name, (r, g, b) in colors.items():
        ppm = os.path.join(OUT_DIR, f"{name}.ppm")
        jpg = os.path.join(OUT_DIR, f"{name}.jpg")
        create_solid_ppm(ppm, r, g, b)
        convert_ppm_to_jpeg(ppm, jpg)
        print(f"[SUCCESS] Generated {name}.jpg ({os.path.getsize(jpg)} bytes)")

    align_ppm = os.path.join(OUT_DIR, "alignment_markers.ppm")
    align_jpg = os.path.join(OUT_DIR, "alignment_markers.jpg")
    create_alignment_ppm(align_ppm)
    convert_ppm_to_jpeg(align_ppm, align_jpg)
    print(f"[SUCCESS] Generated alignment_markers.jpg ({os.path.getsize(align_jpg)} bytes)")

if __name__ == "__main__":
    main()
