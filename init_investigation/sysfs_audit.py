import subprocess, os, sys, glob

def run_cmd(cmd):
    try:
        res = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        return res.stdout.strip()
    except Exception as e:
        return f"Error: {e}"

print("=== 1. UDEVADM INFO FOR HIDRAW ===")
for node in ['/dev/hidraw2', '/dev/hidraw3']:
    if os.path.exists(node):
        print(f"\n--- {node} ---")
        print(run_cmd(f"udevadm info --query=property --name={node}"))

print("\n=== 2. SYSFS USB TREE AUDIT ===")
for p in ['/sys/bus/usb/devices/3-4', '/sys/bus/usb/devices/3-4.2']:
    print(f"\n--- {p} ---")
    if os.path.exists(p):
        for root, dirs, files in os.walk(p):
            if root.count(os.sep) - p.count(os.sep) > 2:
                continue
            for f in files:
                if f in ['manufacturer', 'product', 'idVendor', 'idProduct', 'serial', 'modalias', 'interface', 'bInterfaceClass', 'bInterfaceSubClass', 'bInterfaceProtocol', 'driver']:
                    filepath = os.path.join(root, f)
                    try:
                        content = open(filepath).read().strip()
                    except Exception:
                        content = "<cannot read>"
                    print(f"{filepath}: {content}")

print("\n=== 4. UDEV RULES AND SYSTEMD SEARCH ===")
cmd_grep = "grep -RniE '05ac|0256|SONiX|USB_DEVICE' /etc/udev/rules.d /usr/lib/udev/rules.d /etc/systemd/system /usr/lib/systemd/system 2>/dev/null | grep -iE 'hid|keyboard|mouse|lcd|display|monitor|case|sonix|usb'"
print(run_cmd(cmd_grep))

print("\n=== 6. INPUT EVENT MAPPING ===")
for ev in sorted(glob.glob('/sys/class/input/event*')):
    name_file = os.path.join(ev, 'device/name')
    if os.path.exists(name_file):
        name = open(name_file).read().strip()
        target = os.readlink(os.path.join(ev, 'device'))
        print(f"{os.path.basename(ev)}: '{name}' -> {target}")

print("\n=== 7. USB POWER STATE ===")
for p in ['/sys/bus/usb/devices/3-4', '/sys/bus/usb/devices/3-4.2']:
    print(f"\n--- Power for {os.path.basename(p)} ---")
    power_dir = os.path.join(p, 'power')
    if os.path.exists(power_dir):
        for pf in sorted(os.listdir(power_dir)):
            filepath = os.path.join(power_dir, pf)
            if os.path.isfile(filepath):
                try:
                    val = open(filepath).read().strip()
                    print(f"  {pf}: {val}")
                except Exception:
                    pass

