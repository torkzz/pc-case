import re

il_vmax = open("Vmax.il", "r", encoding="utf-8", errors="ignore").read()

def search_vmax(kw):
    lines = il_vmax.splitlines()
    matches = []
    for idx, l in enumerate(lines):
        if re.search(r'\b' + re.escape(kw) + r'\b', l, re.IGNORECASE):
            matches.append((idx+1, l.strip()))
    return matches

print("=== SEARCHING Vmax.il ===")
for kw in ["33c3", "f101", "345f", "9132", "MSDISPLAY", "DeviceCommunicator", "ConnectDevice"]:
    res = search_vmax(kw)
    print(f"\n--- Keyword: {kw} (Matches: {len(res)}) ---")
    for line_num, l in res[:20]:
        print(f"  Line {line_num}: {l}")

