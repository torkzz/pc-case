with open('/home/tor/pc-case-lcd/DeviceCommunicationLibrary.il', 'r', encoding='utf-8', errors='ignore') as f:
    il_text = f.read()

import re

def print_method_il(mname):
    print(f"\n==================== METHOD: {mname} ====================")
    pattern = re.compile(rf'\.method.*?\b{mname}\b.*?\n\s*\{{(.*?)\n\s*\}}', re.DOTALL)
    match = pattern.search(il_text)
    if match:
        lines = match.group(0).splitlines()
        for i, l in enumerate(lines[:100]):
            print(f"{i+1:4d}: {l}")
    else:
        print("Method not found.")

print_method_il("ProcessReceiveBuffer")
print_method_il("FindFrameStart")
print_method_il("FindFrameEnd")

