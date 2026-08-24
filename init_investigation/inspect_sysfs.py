import os, sys, glob

def check_usb():
    print("=== USB DEVICES IN SYSFS ===")
    for dev in sorted(glob.glob('/sys/bus/usb/devices/*')):
        idv = os.path.join(dev, 'idVendor')
        idp = os.path.join(dev, 'idProduct')
        if os.path.exists(idv) and os.path.exists(idp):
            vid = open(idv).read().strip()
            pid = open(idp).read().strip()
            mfg = open(os.path.join(dev, 'manufacturer')).read().strip() if os.path.exists(os.path.join(dev, 'manufacturer')) else ""
            prod = open(os.path.join(dev, 'product')).read().strip() if os.path.exists(os.path.join(dev, 'product')) else ""
            speed = open(os.path.join(dev, 'speed')).read().strip() if os.path.exists(os.path.join(dev, 'speed')) else ""
            print(f"Path: {os.path.basename(dev):<10} VID:PID={vid}:{pid} Speed={speed:<6} Mfg='{mfg}' Prod='{prod}'")

def check_drm():
    print("\n=== DRM CONNECTORS IN SYSFS ===")
    for status_file in sorted(glob.glob('/sys/class/drm/*/status')):
        conn = status_file.split('/')[-2]
        st = open(status_file).read().strip()
        modes_file = os.path.join(os.path.dirname(status_file), 'modes')
        modes = open(modes_file).read().strip().split('\n') if os.path.exists(modes_file) else []
        top_mode = modes[0] if modes and modes[0] else "No modes"
        print(f"Connector: {conn:<15} Status: {st:<15} Top Mode: {top_mode}")

def check_hidraw():
    print("\n=== HIDRAW NODES IN SYSFS ===")
    for h in sorted(glob.glob('/sys/class/hidraw/*')):
        name = os.path.basename(h)
        target = os.readlink(h)
        print(f"{name} -> {target}")

def check_v4l2():
    print("\n=== VIDEO4LINUX NODES ===")
    nodes = glob.glob('/sys/class/video4linux/*')
    print(f"Count: {len(nodes)}")
    for n in nodes:
        print(os.path.basename(n))

def check_tty():
    print("\n=== USB / ACM TTY NODES ===")
    for tty in sorted(glob.glob('/sys/class/tty/*')):
        target = os.readlink(tty)
        if 'usb' in target or 'ACM' in target:
            print(f"{os.path.basename(tty)} -> {target}")

check_usb()
check_drm()
check_hidraw()
check_v4l2()
check_tty()
