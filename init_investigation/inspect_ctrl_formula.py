with open('/home/tor/pc-case-lcd/DeviceCommunicationLibrary.il', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

import re
lines = text.splitlines()

for i, l in enumerate(lines):
    if 'CalculateContentLength' in l or 'BuildCTRL' in l:
        print(f"=== Line {i+1}: {l} ===")
        for j in range(max(0, i-5), min(len(lines), i+35)):
            print(f"{j+1:6d}: {lines[j]}")
        print("="*60)

