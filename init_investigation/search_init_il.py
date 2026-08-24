import re

il_comm = open("DeviceCommunicationLibrary.il", "r", encoding="utf-8", errors="ignore").read()
il_vmax = open("Vmax.il", "r", encoding="utf-8", errors="ignore").read()

keywords = [
    "Connect", "Open", "SerialPort", "DtrEnable", "RtsEnable", "BaudRate", 
    "DataBits", "StopBits", "Parity", "Handshake", "ReadTimeout", "WriteTimeout", 
    "DiscardInBuffer", "DiscardOutBuffer", "BaseStream", "BytesToRead", "DataReceived", 
    "HandshakeRequest", "ChangeStatus", "Restart", "ExitRunning", "Reset", 
    "Initialize", "Init", "OpenDevice", "ConnectDevice", "ConnectDeviceAsync"
]

print("=== SEARCHING DeviceCommunicationLibrary.il ===")
for kw in keywords:
    matches = [line.strip() for line in il_comm.splitlines() if re.search(r'\b' + re.escape(kw) + r'\b', line, re.IGNORECASE)]
    if matches:
        print(f"\n--- Keyword: {kw} (Count: {len(matches)}) ---")
        for m in matches[:10]:
            print("  ", m)

print("\n=== SEARCHING Vmax.il ===")
for kw in keywords:
    matches = [line.strip() for line in il_vmax.splitlines() if re.search(r'\b' + re.escape(kw) + r'\b', line, re.IGNORECASE)]
    if matches:
        print(f"\n--- Keyword: {kw} (Count: {len(matches)}) ---")
        for m in matches[:10]:
            print("  ", m)

