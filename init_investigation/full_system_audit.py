import os, sys, glob, subprocess

def run_cmd(cmd):
    try:
        res = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=10)
        return res.stdout.strip()
    except Exception as e:
        return f"Error/Timeout: {e}"

print("=========================================")
print("STEP 1: COMPLETE USB INVENTORY")
print("=========================================")
usb_devices = []
for devpath in sorted(glob.glob('/sys/bus/usb/devices/*')):
    if not os.path.exists(os.path.join(devpath, 'idVendor')):
        continue
    devname = os.path.basename(devpath)
    vid = run_cmd(f"cat {devpath}/idVendor 2>/dev/null")
    pid = run_cmd(f"cat {devpath}/idProduct 2>/dev/null")
    mfg = run_cmd(f"cat {devpath}/manufacturer 2>/dev/null")
    prod = run_cmd(f"cat {devpath}/product 2>/dev/null")
    speed = run_cmd(f"cat {devpath}/speed 2>/dev/null")
    bclass = run_cmd(f"cat {devpath}/bDeviceClass 2>/dev/null")
    
    ifaces = []
    for ifdir in sorted(glob.glob(f"{devpath}/{devname}:*")):
        ifname = os.path.basename(ifdir)
        iclass = run_cmd(f"cat {ifdir}/bInterfaceClass 2>/dev/null")
        isub = run_cmd(f"cat {ifdir}/bInterfaceSubClass 2>/dev/null")
        ipro = run_cmd(f"cat {ifdir}/bInterfaceProtocol 2>/dev/null")
        drvlink = os.path.join(ifdir, 'driver')
        drv = os.path.basename(os.readlink(drvlink)) if os.path.exists(drvlink) else "none"
        ifaces.append(f"{ifname}(C:{iclass}/S:{isub}/P:{ipro}/Drv:{drv})")
    
    print(f"Path: {devname:<10} | VID:PID: {vid}:{pid} | Speed: {speed:<5} Mbps | Class: {bclass} | Mfg: '{mfg}' | Prod: '{prod}'")
    print(f"  Interfaces: {', '.join(ifaces) if ifaces else 'None'}")

print("\n=========================================")
print("STEP 2: DRM / DISPLAY INVENTORY")
print("=========================================")
print("--- /proc/fb ---")
print(run_cmd("cat /proc/fb 2>/dev/null"))

print("\n--- /sys/class/drm Status & Modes ---")
for drm in sorted(glob.glob('/sys/class/drm/*')):
    dname = os.path.basename(drm)
    status = run_cmd(f"cat {drm}/status 2>/dev/null")
    enabled = run_cmd(f"cat {drm}/enabled 2>/dev/null")
    modes = run_cmd(f"cat {drm}/modes 2>/dev/null").split('\n')
    top_mode = modes[0] if modes and modes[0] else "none"
    if status or enabled or top_mode != "none":
        print(f"DRM Node: {dname:<18} Status: {status:<15} Enabled: {enabled:<10} Top Mode: {top_mode}")

print("\n--- Display Dev Nodes ---")
print(run_cmd("find /dev -maxdepth 2 \( -name 'fb*' -o -name 'dri' -o -name 'card*' \) 2>/dev/null"))

print("\n=========================================")
print("STEP 3: SEARCH SYSFS DISPLAY NODES")
print("=========================================")
print(run_cmd("grep -RilE 'display|lcd|tft|screen|panel|monitor|hdmi|dvi|dp|mipi|spi|st7789|ili9341|ili9488' /sys/class /sys/devices 2>/dev/null | head -50"))

print("\n--- Display/Video/DRM Links in /sys/class ---")
print(run_cmd("find /sys/class -maxdepth 2 -type l \( -iname '*display*' -o -iname '*lcd*' -o -iname '*panel*' -o -iname '*video*' -o -iname '*drm*' \) 2>/dev/null"))

print("\n=========================================")
print("STEP 4: SEARCH SOFTWARE / SERVICES")
print("=========================================")
print("--- Running Processes ---")
print(run_cmd("ps auxww | grep -Ei 'lcd|display|screen|monitor|hardware.?monitor|hwmon|aida|sensor|rgb|rgb.?control|case|panel|tft|screen' | grep -v grep"))

print("\n--- Systemd Services ---")
print(run_cmd("systemctl list-units --type=service --all 2>/dev/null | grep -Ei 'lcd|display|screen|monitor|hardware|rgb|case|panel'"))
print(run_cmd("systemctl list-unit-files 2>/dev/null | grep -Ei 'lcd|display|screen|monitor|hardware|rgb|case|panel'"))

print("\n=========================================")
print("STEP 5: INSTALLED PACKAGES & BINARIES")
print("=========================================")
print("--- Pacman Packages ---")
print(run_cmd("pacman -Q 2>/dev/null | grep -Ei 'lcd|display|screen|monitor|hwinfo|hardware|sensor|rgb|openrgb|liquid|aida|panel'"))

print("\n--- Binary Search ---")
print(run_cmd("find /usr/bin /usr/local/bin /opt /home/tor -maxdepth 4 -type f \( -iname '*lcd*' -o -iname '*display*' -o -iname '*panel*' -o -iname '*screen*' -o -iname '*monitor*' \) 2>/dev/null | head -50"))

print("\n=========================================")
print("STEP 6: HWMON / SENSORS")
print("=========================================")
for h in sorted(glob.glob('/sys/class/hwmon/hwmon*')):
    name = run_cmd(f"cat {h}/name 2>/dev/null")
    print(f"HWMON Node: {os.path.basename(h):<10} Name: '{name}'")

print("\n=========================================")
print("STEP 7: ALL HIDRAW NODES & UDEV INFO")
print("=========================================")
for h in sorted(glob.glob('/sys/class/hidraw/hidraw*')):
    hname = os.path.basename(h)
    devnode = f"/dev/{hname}"
    info = run_cmd(f"udevadm info --query=property --name={devnode} 2>/dev/null | grep -E '^(ID_VENDOR|ID_MODEL|ID_BUS|PRODUCT)'")
    target = os.readlink(h) if os.path.islink(h) else ""
    print(f"{hname:<10} -> {target}")
    if info:
        print(f"  {info.replace('\n', ' | ')}")

print("\n=========================================")
print("STEP 9: PCI DEVICE INVENTORY")
print("=========================================")
for pci in sorted(glob.glob('/sys/bus/pci/devices/*')):
    pname = os.path.basename(pci)
    vfile = os.path.join(pci, 'vendor')
    dfile = os.path.join(pci, 'device')
    cfile = os.path.join(pci, 'class')
    if os.path.exists(vfile):
        vid = open(vfile).read().strip()
        did = open(dfile).read().strip()
        cls = open(cfile).read().strip()
        drvlink = os.path.join(pci, 'driver')
        drv = os.path.basename(os.readlink(drvlink)) if os.path.exists(drvlink) else "none"
        print(f"PCI {pname} | Class: {cls} | VID:PID = {vid}:{did} | Driver: {drv}")

print("\n=========================================")
print("STEP 10: KERNEL LOGS / VAR LOGS")
print("=========================================")
print(run_cmd("grep -Ei 'usb|hid|drm|display|panel|lcd|mipi|spi|i2c|video' /var/log/messages /var/log/syslog /var/log/dmesg 2>/dev/null | tail -30"))

