import re, os

bundle_dir = "/home/tor/vmax_bundle/bin/Release"
il_comm_path = "/home/tor/pc-case-lcd/DeviceCommunicationLibrary.il"
il_vmax_path = "/home/tor/pc-case-lcd/Vmax.il"

il_comm = open(il_comm_path, "r", encoding="utf-8", errors="ignore").read()
il_vmax = open(il_vmax_path, "r", encoding="utf-8", errors="ignore").read()

keywords = [
    "GPIO", "Gpio", "Reset", "RESET", "Enable", "Disable", "Power", 
    "PowerOn", "PowerOff", "Start", "Stop", "Restart", "ChangeStatus", 
    "Display", "MSDisplay", "USB", "345f", "9132", "9133", "374a", "a101"
]

print("=== TASK 1: SEARCHING DeviceCommunicationLibrary.il FOR CONTROL/GPIO/RESET STRINGS & METHODS ===")

for kw in ["GPIO", "Gpio", "Reset", "Power", "Enable", "ChangeStatus", "Restart", "Init", "Gpio", "Switch"]:
    matches = [l.strip() for l in il_comm.splitlines() if re.search(r'\b' + re.escape(kw) + r'\b', l, re.IGNORECASE)]
    print(f"DeviceCommunicationLibrary.il -> Keyword: '{kw}' (Count: {len(matches)})")
    for m in matches[:5]:
        print("  ", m)

print("\n=== SEARCHING NATIVE / MANAGED STRINGS FOR GPIO / POWER / RESET CONTROLS ===")

for fname in ["MSDISPLAYSDKWRRAPER.dll", "libstack.dll", "libcompositeScreenModel.dll"]:
    fpath = os.path.join(bundle_dir, fname)
    if os.path.exists(fpath):
        raw = open(fpath, "rb").read()
        print(f"\n--- File: {fname} ---")
        for kw in [b"Gpio", b"GPIO", b"Reset", b"RESET", b"Power", b"Enable", b"InitFlash", b"FlashGpio"]:
            m_cnt = len(list(re.finditer(re.escape(kw), raw, re.IGNORECASE)))
            print(f"  Keyword '{kw.decode()}': {m_cnt} matches")
            for match in re.finditer(re.escape(kw), raw, re.IGNORECASE):
                start = max(0, match.start() - 30)
                end = min(len(raw), match.end() + 30)
                chunk = "".join([chr(b) if 32 <= b <= 126 else "." for b in raw[start:end]])
                print(f"    Offset {match.start():#08x}: {chunk}")
                break

