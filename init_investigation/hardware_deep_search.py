import os, re, json

pc_dir = "/home/tor/pc-case-lcd"
bundle_dir = "/home/tor/vmax_bundle/bin/Release"

# 1. Search for firmware update, bootloader, reset, power, OTA, and USB mode strings
print("=== 1. SEARCHING FOR FIRMWARE / BOOTLOADER / OTA LOGIC ===")

for root, dirs, files in os.walk(bundle_dir):
    for f in files:
        if f.endswith(('.dll', '.exe')):
            fpath = os.path.join(root, f)
            try:
                raw = open(fpath, 'rb').read()
                matches = re.findall(b'(OTA|bootloader|Bootloader|Firmware|firmware|Reset|RESET|Power|POWER|ModeSwitch|DFU|hid|HID|usbdk|UsbDk)', raw, re.IGNORECASE)
                if matches:
                    print(f"File {f}: {set([m.decode(errors='ignore') for m in matches])}")
            except Exception as e:
                pass

print("\n=== 2. INSPECTING DESCRIPTOR BASELINE DETAILS ===")
desc_path = os.path.join(pc_dir, "USB_DESCRIPTOR_BASELINE.md")
if os.path.exists(desc_path):
    desc_txt = open(desc_path).read()
    print("Descriptor file size:", len(desc_txt))

print("\n=== 3. SEARCHING VMAX.EXE FOR ALL DISPLAY & DEVICE INITIALIZATION CLASSES ===")
il_vmax = open(os.path.join(pc_dir, "Vmax.il"), "r", encoding="utf-8", errors="ignore").read()

classes_in_vmax = re.findall(r'\.class[^\n]+', il_vmax)
print(f"Vmax.il classes found: {len(classes_in_vmax)}")

