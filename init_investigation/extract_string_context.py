import re

vmax_raw = open("/home/tor/vmax_bundle/bin/Release/Vmax.exe", "rb").read()

def print_context(pattern, name):
    print(f"\n==========================================")
    print(f"=== CONTEXT FOR {name} ===")
    print(f"==========================================")
    for m in re.finditer(pattern, vmax_raw, re.IGNORECASE):
        start = max(0, m.start() - 100)
        end = min(len(vmax_raw), m.end() + 100)
        chunk = vmax_raw[start:end]
        # Clean non-printable bytes
        printable = "".join([chr(b) if 32 <= b <= 126 else "." for b in chunk])
        print(f"Offset {m.start():#08x}: {printable}")

print_context(b"345f", "VID 345F")
print_context(b"9132", "PID 9132")
print_context(b"33c3", "VID 33C3")
print_context(b"f101", "PID F101")
print_context(b"Wrraper_MSDisplaySendPicture", "Wrraper_MSDisplaySendPicture")

