#!/usr/bin/env python3
"""
Rotated Pattern Frame Generator (`generate_rotated_patterns.py`)

Creates 4 rotation variants of the 4-quarter block diagnostic pattern:
1. rot0   : Original 2560x666
2. rot90  : 90 deg CW (666x2560)
3. rot180 : 180 deg (2560x666)
4. rot270 : 270 deg CW (666x2560)
"""

import os
import subprocess

OUT_DIR = "diagnostic_patterns"
os.makedirs(OUT_DIR, exist_ok=True)

base_ppm = os.path.join(OUT_DIR, "pattern_a_black_grid.ppm")

def create_rotated_jpegs():
    if not os.path.exists(base_ppm):
        # Generate base PPM 2560x666
        header = f"P6\n2560 666\n255\n".encode('ascii')
        pixels = bytearray(2560 * 666 * 3)
        q1_end = 166
        q2_end = 333
        q3_end = 499

        for y in range(666):
            if y < q1_end: r, g, b = 255, 0, 0        # Red
            elif y < q2_end: r, g, b = 0, 255, 0      # Green
            elif y < q3_end: r, g, b = 0, 0, 255      # Blue
            else: r, g, b = 255, 255, 255         # White

            for x in range(2560):
                idx = (y * 2560 + x) * 3
                pixels[idx] = r
                pixels[idx+1] = g
                pixels[idx+2] = b

        with open(base_ppm, 'wb') as f:
            f.write(header)
            f.write(pixels)

    rotations = {
        'rot0': (2560, 666, None),
        'rot90': (666, 2560, 'transpose=1'),
        'rot180': (2560, 666, 'hflip,vflip'),
        'rot270': (666, 2560, 'transpose=2')
    }

    generated = {}

    for rot_name, (w, h, vf) in rotations.items():
        jpg_out = os.path.join(OUT_DIR, f"4quarter_{rot_name}.jpg")
        cmd = ['ffmpeg', '-y', '-i', base_ppm]
        if vf:
            cmd.extend(['-vf', vf])
        cmd.extend(['-q:v', '2', jpg_out])
        
        subprocess.check_call(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        generated[rot_name] = (jpg_out, w, h, os.path.getsize(jpg_out))
        print(f"[SUCCESS] Generated {rot_name}: {jpg_out} ({w}x{h}, {os.path.getsize(jpg_out)} bytes)")

    return generated

if __name__ == "__main__":
    create_rotated_jpegs()
