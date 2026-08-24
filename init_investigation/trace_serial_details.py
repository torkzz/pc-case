with open('/home/tor/pc-case-lcd/DeviceCommunicationLibrary.il', 'r', encoding='utf-8', errors='ignore') as f:
    il_text = f.read()

import re

def search_section(title, pattern_str):
    print(f"\n==================== {title} ====================")
    matches = re.finditer(pattern_str, il_text, re.DOTALL)
    count = 0
    for m in matches:
        count += 1
        print(m.group(0)[:1500])
        print("-" * 40)
        if count >= 5:
            break
    if count == 0:
        print("No matches found.")

search_section("Connect Method", r'\.method\s+public.*?Connect\s*\(.*?\)\s*cil\s+managed.*?\n\s*\}')
search_section("DtrEnable / RtsEnable / Timeout", r'\.method.*?(?:set_DtrEnable|set_RtsEnable|set_ReadTimeout|set_WriteTimeout|set_BaudRate).*?\n\s*\}')
search_section("HandshakeAsync Method", r'\.method.*?HandshakeAsync.*?\n\s*\}')
search_section("SendRequestAsync Method", r'\.method.*?SendRequestAsync.*?\n\s*\}')
search_section("ProcessReceiveBuffer Method", r'\.method.*?ProcessReceiveBuffer.*?\n\s*\}')

