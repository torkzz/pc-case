import re

vmax_raw = open("/home/tor/vmax_bundle/bin/Release/Vmax.exe", "rb").read()

# Extract method names, string literals, and class definitions related to AICDisp and MSDisplay
def search_ascii_patterns():
    print("=== SEARCHING ALL METHODS AND STRINGS AROUND AICDisp AND MSDisplay ===")
    
    pattern = re.compile(b'(AICDisp[A-Za-z0-9_]*|MSDisplay[A-Za-z0-9_]*|DeviceCommunicat[A-Za-z0-9_]*)')
    for m in pattern.finditer(vmax_raw):
        pos = m.start()
        chunk = vmax_raw[max(0, pos-40):min(len(vmax_raw), pos+60)]
        clean = "".join([chr(b) if 32 <= b <= 126 else "." for b in chunk])
        print(f"Offset {pos:#08x}: {clean}")

search_ascii_patterns()
