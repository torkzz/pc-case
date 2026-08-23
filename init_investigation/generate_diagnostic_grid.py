#!/usr/bin/env python3
"""
MSDisplay Diagnostic Grid Frame Generator (`generate_diagnostic_grid.py`)

Creates deterministic 2560x666 test pattern frames:
- Pattern A: Black background + white horizontal & vertical grid lines + numbered Y regions (Top 0-222, Mid 222-444, Bot 444-666).
- Pattern B: White background + black grid lines (Inverted).
- Pattern C: 5-Band Horizontal Color Stripes (Red, Green, Blue, White, Black).
"""

import os
import sys
import subprocess

WIDTH = 2560
HEIGHT = 666

OUT_DIR = "diagnostic_patterns"
os.makedirs(OUT_DIR, exist_ok=True)

def generate_ppm_grid(filename_ppm, is_inverted=False):
    bg_r, bg_g, bg_b = (255, 255, 255) if is_inverted else (0, 0, 0)
    fg_r, fg_g, fg_b = (0, 0, 0) if is_inverted else (255, 255, 255)

    ppm_header = f"P6\n{WIDTH} {HEIGHT}\n255\n".encode('ascii')
    pixels = bytearray(WIDTH * HEIGHT * 3)

    # Fill background
    for i in range(0, len(pixels), 3):
        pixels[i] = bg_r
        pixels[i+1] = bg_g
        pixels[i+2] = bg_b

    # Draw horizontal grid lines every 50 pixels and region boundaries at Y=222 and Y=444
    for y in range(HEIGHT):
        is_grid_y = (y % 50 == 0) or (y in (222, 444))
        for x in range(WIDTH):
            is_grid_x = (x % 100 == 0) or (x in (640, 1280, 1920))
            if is_grid_y or is_grid_x:
                idx = (y * WIDTH + x) * 3
                pixels[idx] = fg_r
                pixels[idx+1] = fg_g
                pixels[idx+2] = fg_b

    with open(filename_ppm, 'wb') as f:
        f.write(ppm_header)
        f.write(pixels)

def generate_color_bars_ppm(filename_ppm):
    ppm_header = f"P6\n{WIDTH} {HEIGHT}\n255\n".encode('ascii')
    pixels = bytearray(WIDTH * HEIGHT * 3)

    # 5 horizontal bands (height ~133 pixels each)
    band_height = HEIGHT // 5
    colors = [
        (255, 0, 0),    # Red (0 - 133)
        (0, 255, 0),    # Green (133 - 266)
        (0, 0, 255),    # Blue (266 - 399)
        (255, 255, 255),# White (399 - 532)
        (0, 0, 0)       # Black (532 - 666)
    ]

    for y in range(HEIGHT):
        color_idx = min(y // band_height, len(colors) - 1)
        r, g, b = colors[color_idx]
        for x in range(WIDTH):
            idx = (y * WIDTH + x) * 3
            pixels[idx] = r
            pixels[idx+1] = g
            pixels[idx+2] = b

    with open(filename_ppm, 'wb') as f:
        f.write(ppm_header)
        f.write(pixels)

def convert_ppm_to_jpeg(ppm_file, jpg_file):
    cmd = ['ffmpeg', '-y', '-i', ppm_file, '-q:v', '2', jpg_file]
    subprocess.check_call(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def main():
    print("=== Generating Diagnostic Test Pattern Frames (2560x666) ===")
    
    ppm_a = os.path.join(OUT_DIR, "pattern_a_black_grid.ppm")
    jpg_a = os.path.join(OUT_DIR, "pattern_a_black_grid.jpg")
    generate_ppm_grid(ppm_a, is_inverted=False)
    convert_ppm_to_jpeg(ppm_a, jpg_a)
    print(f"[SUCCESS] Pattern A (Black Grid) generated: {jpg_a} ({os.path.getsize(jpg_a)} bytes)")

    ppm_b = os.path.join(OUT_DIR, "pattern_b_white_grid.ppm")
    jpg_b = os.path.join(OUT_DIR, "pattern_b_white_grid.jpg")
    generate_ppm_grid(ppm_b, is_inverted=True)
    convert_ppm_to_jpeg(ppm_b, jpg_b)
    print(f"[SUCCESS] Pattern B (White Grid) generated: {jpg_b} ({os.path.getsize(jpg_b)} bytes)")

    ppm_c = os.path.join(OUT_DIR, "pattern_c_color_bars.ppm")
    jpg_c = os.path.join(OUT_DIR, "pattern_c_color_bars.jpg")
    generate_color_bars_ppm(ppm_c)
    convert_ppm_to_jpeg(ppm_c, jpg_c)
    print(f"[SUCCESS] Pattern C (Color Bars) generated: {jpg_c} ({os.path.getsize(jpg_c)} bytes)")

if __name__ == "__main__":
    main()
