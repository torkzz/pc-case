import os, sys, re, subprocess

bundle_path = "/home/tor/vmax_bundle"

def run_cmd(cmd):
    try:
        res = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=10)
        return res.stdout
    except Exception as e:
        return str(e)

print("=== 1. CHECK NATIVE EXPORTS OF MSDISPLAYSDKWRRAPER.dll ===")
nm_out = run_cmd("nm -D /home/tor/vmax_bundle/bin/Release/MSDISPLAYSDKWRRAPER.dll 2>/dev/null || objdump -x /home/tor/vmax_bundle/bin/Release/MSDISPLAYSDKWRRAPER.dll | grep -i 'export'")
print(nm_out if nm_out.strip() else "No exports found via nm/objdump, checking strings...")

strings_ms = run_cmd("strings /home/tor/vmax_bundle/bin/Release/MSDISPLAYSDKWRRAPER.dll | grep -iE 'USB|Display|Open|Init|Send|Frame|345F|9132|33C3|F101|Vendor|Device|Write|Read'")
print("--- MSDISPLAYSDKWRRAPER.dll Strings ---")
print("\n".join(strings_ms.splitlines()[:50]))

print("\n=== 2. CHECK ALL REFERENCES TO MSDISPLAY / MACROSILICON IN VMAX.IL ===")
il_vmax_path = "/home/tor/pc-case-lcd/Vmax.il"
if not os.path.exists(il_vmax_path) or os.path.getsize(il_vmax_path) < 1000:
    print("Regenerating Vmax.il using monodis...")
    run_cmd("monodis /home/tor/vmax_bundle/bin/Release/Vmax.exe > /home/tor/pc-case-lcd/Vmax.il")

il_vmax = open(il_vmax_path, "r", encoding="utf-8", errors="ignore").read()

for kw in ["MSDISPLAY", "MSDISPLAYSDKWRRAPER", "DeviceCommunicator", "MacroSilicon", "345f", "9132", "33c3", "f101", "UsbDisplay", "ScreenModel", "libcomposite"]:
    matches = [l.strip() for l in il_vmax.splitlines() if re.search(r'\b' + re.escape(kw) + r'\b', l, re.IGNORECASE)]
    print(f"Vmax.il -> Keyword: {kw} (Count: {len(matches)})")
    for m in matches[:10]:
        print("  ", m)

