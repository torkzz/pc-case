with open('/home/tor/pc-case-lcd/DeviceCommunicationLibrary.il', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

import re
lines = text.splitlines()

for i, l in enumerate(lines):
    if '.class' in l and 'DownloadDataRequest' in l:
        print(f"=== Line {i+1}: {l} ===")
        for j in range(i, min(len(lines), i+80)):
            print(f"{j+1:6d}: {lines[j]}")
        print("="*60)

