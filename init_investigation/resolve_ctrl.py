with open('/home/tor/pc-case-lcd/DeviceCommunicationLibrary.il', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

import re

def show_block(name, length=100):
    print(f"\n==================== {name} ====================")
    matches = re.finditer(rf'\.method.*?\b{name}\b.*?\n\s*\{{(.*?)\n\s*\}}', text, re.DOTALL)
    for i, m in enumerate(matches):
        print(f"--- Match #{i+1} ---")
        lines = m.group(0).splitlines()
        print("\n".join(lines[:length]))

show_block("CalculateContentLength")
show_block("BuildCTRL")
show_block("ToBytes")
show_block("SendRequestAsync")

