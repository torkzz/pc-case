#!/usr/bin/env python3
"""
VMAX PC-Case LCD Test Image Generator (Task 11)
Creates a deterministic 2560x666 JPEG test image with high-contrast boundaries,
"VMAX TEST", timestamp, and target VID:PID 33c3:f101 string.
"""

import sys
import os
import time

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    import subprocess
    subprocess.run([sys.executable, "-m", "pip", "install", "pillow"], check=True)
    from PIL import Image, ImageDraw, ImageFont

def generate_vmax_test_image(width=2560, height=666, output_path="/home/tor/pc-case-lcd/vmax_test_2560x666.jpg"):
    # Create black RGB image
    img = Image.new('RGB', (width, height), color=(10, 10, 10))
    draw = ImageDraw.Draw(img)

    # Outer border (white 4px)
    draw.rectangle([4, 4, width - 5, height - 5], outline=(255, 255, 255), width=4)
    # Inner border (cyan 2px)
    draw.rectangle([12, 12, width - 13, height - 13], outline=(0, 255, 255), width=2)

    # Large Center Text
    text_main = "HL VMAX LINUX TEST"
    text_sub = f"VID:PID 33c3:f101 | Node: /dev/ttyACM0 | Time: {time.strftime('%Y-%m-%d %H:%M:%S')}"
    text_res = f"Target Resolution: {width} x {height}"

    try:
        font_large = ImageFont.truetype("/usr/share/fonts/TTF/DejaVuSans-Bold.ttf", 90)
        font_sub = ImageFont.truetype("/usr/share/fonts/TTF/DejaVuSans.ttf", 40)
    except Exception:
        font_large = ImageFont.load_default()
        font_sub = ImageFont.load_default()

    # Draw centered text
    bbox_main = draw.textbbox((0, 0), text_main, font=font_large)
    w_main, h_main = bbox_main[2] - bbox_main[0], bbox_main[3] - bbox_main[1]
    draw.text(((width - w_main) // 2, (height // 2) - 100), text_main, fill=(255, 255, 0), font=font_large)

    bbox_sub = draw.textbbox((0, 0), text_sub, font=font_sub)
    w_sub, h_sub = bbox_sub[2] - bbox_sub[0], bbox_sub[3] - bbox_sub[1]
    draw.text(((width - w_sub) // 2, (height // 2) + 30), text_sub, fill=(0, 255, 255), font=font_sub)

    bbox_res = draw.textbbox((0, 0), text_res, font=font_sub)
    w_res = bbox_res[2] - bbox_res[0]
    draw.text(((width - w_res) // 2, (height // 2) + 100), text_res, fill=(255, 255, 255), font=font_sub)

    # Save baseline JPEG (quality=85)
    img.save(output_path, format="JPEG", quality=85)
    file_size = os.path.getsize(output_path)
    print(f"Generated test JPEG image: {output_path} ({width}x{height}, {file_size} bytes)")
    return output_path

if __name__ == "__main__":
    generate_vmax_test_image()
