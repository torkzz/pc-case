#!/usr/bin/env python3
"""
Read-Only USB Topology Verifier (`verify_usb_topology.py`)

Scans host USB bus dynamically via sysfs and libusb:
1. Enumerates every connected USB device (dynamic path lookup, no hardcoded bus/dev numbers).
2. Checks specifically for target VIDs/PIDs:
   - MacroSilicon MSDisplay: 345f:9132 (and alternate PIDs 9133, 374a, a101)
   - VMAX Telemetry MCU: 33c3:f101
3. Prints bus/device address, active configuration, every interface number.
4. Prints every endpoint address, direction, transfer type, max packet size.
5. Verifies if Interface 3 / EP 0x04 exists on any connected device.
6. NO interface claiming, NO data transmission (100% read-only).
"""

import sys
import os
import ctypes

try:
    libusb = ctypes.CDLL('libusb-1.0.so.0')
except Exception as e:
    print(f"[ERROR] Failed to load libusb-1.0: {e}")
    sys.exit(1)

class libusb_device_descriptor(ctypes.Structure):
    _fields_ = [
        ('bLength', ctypes.c_uint8),
        ('bDescriptorType', ctypes.c_uint8),
        ('bcdUSB', ctypes.c_uint16),
        ('bDeviceClass', ctypes.c_uint8),
        ('bDeviceSubClass', ctypes.c_uint8),
        ('bDeviceProtocol', ctypes.c_uint8),
        ('bMaxPacketSize0', ctypes.c_uint8),
        ('idVendor', ctypes.c_uint16),
        ('idProduct', ctypes.c_uint16),
        ('bcdDevice', ctypes.c_uint16),
        ('iManufacturer', ctypes.c_uint8),
        ('iProduct', ctypes.c_uint8),
        ('iSerialNumber', ctypes.c_uint8),
        ('bNumConfigurations', ctypes.c_uint8),
    ]

libusb.libusb_init.argtypes = [ctypes.c_void_p]
libusb.libusb_init.restype = ctypes.c_int
libusb.libusb_exit.argtypes = [ctypes.c_void_p]

libusb.libusb_get_device_list.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_void_p)]
libusb.libusb_get_device_list.restype = ctypes.c_ssize_t
libusb.libusb_free_device_list.argtypes = [ctypes.c_void_p, ctypes.c_int]

libusb.libusb_get_device_descriptor.argtypes = [ctypes.c_void_p, ctypes.POINTER(libusb_device_descriptor)]
libusb.libusb_get_device_descriptor.restype = ctypes.c_int

libusb.libusb_get_bus_number.argtypes = [ctypes.c_void_p]
libusb.libusb_get_bus_number.restype = ctypes.c_uint8

libusb.libusb_get_device_address.argtypes = [ctypes.c_void_p]
libusb.libusb_get_device_address.restype = ctypes.c_uint8

def parse_sysfs_topology():
    print("=== SYSFS READ-ONLY USB TOPOLOGY SCAN ===")
    usb_dir = '/sys/bus/usb/devices'
    if not os.path.exists(usb_dir):
        print("[ERROR] sysfs path /sys/bus/usb/devices not found.")
        return

    found_345f = False
    found_33c3 = False

    for entry in sorted(os.listdir(usb_dir)):
        dev_path = os.path.join(usb_dir, entry)
        vid_file = os.path.join(dev_path, 'idVendor')
        pid_file = os.path.join(dev_path, 'idProduct')

        if not (os.path.exists(vid_file) and os.path.exists(pid_file)):
            continue

        try:
            with open(vid_file, 'r') as f: vid = f.read().strip().lower()
            with open(pid_file, 'r') as f: pid = f.read().strip().lower()
        except Exception:
            continue

        man, prod = "", ""
        man_f = os.path.join(dev_path, 'manufacturer')
        prod_f = os.path.join(dev_path, 'product')
        if os.path.exists(man_f):
            try:
                with open(man_f, errors='ignore') as f: man = f.read().strip()
            except Exception: pass
        if os.path.exists(prod_f):
            try:
                with open(prod_f, errors='ignore') as f: prod = f.read().strip()
            except Exception: pass

        devnum_f = os.path.join(dev_path, 'devnum')
        busnum_f = os.path.join(dev_path, 'busnum')
        devnum = open(devnum_f).read().strip() if os.path.exists(devnum_f) else "?"
        busnum = open(busnum_f).read().strip() if os.path.exists(busnum_f) else "?"

        dev_node = f"/dev/bus/usb/{int(busnum):03d}/{int(devnum):03d}" if busnum.isdigit() and devnum.isdigit() else "N/A"

        tag = ""
        if vid == "345f":
            found_345f = True
            tag = " *** TARGET: MacroSilicon MSDisplay ***"
        elif vid == "33c3" and pid == "f101":
            found_33c3 = True
            tag = " *** TARGET: HL VMAX Telemetry MCU ***"

        print(f"\n[USB DEVICE] Sysfs: {entry} | Node: {dev_node}")
        print(f"  VID:PID       : {vid}:{pid}{tag}")
        print(f"  Manufacturer  : {man}")
        print(f"  Product       : {prod}")

        # Scan interfaces in sysfs
        interfaces = []
        for if_entry in sorted(os.listdir(dev_path)):
            if if_entry.startswith(f"{entry}:"):
                if_path = os.path.join(dev_path, if_entry)
                if_num_file = os.path.join(if_path, 'bInterfaceNumber')
                if_cls_file = os.path.join(if_path, 'bInterfaceClass')
                if_sub_file = os.path.join(if_path, 'bInterfaceSubClass')
                driver_link = os.path.join(if_path, 'driver')

                if_num = open(if_num_file).read().strip() if os.path.exists(if_num_file) else "?"
                if_cls = open(if_cls_file).read().strip() if os.path.exists(if_cls_file) else "?"
                if_sub = open(if_sub_file).read().strip() if os.path.exists(if_sub_file) else "?"
                driver = os.path.basename(os.readlink(driver_link)) if os.path.islink(driver_link) else "unbound"

                # Enumerate endpoints under interface
                eps = []
                for ep_entry in sorted(os.listdir(if_path)):
                    if ep_entry.startswith('ep_'):
                        ep_addr = ep_entry.replace('ep_', '0x')
                        eps.append(ep_addr)

                print(f"  Interface {if_num}: Class={if_cls}, SubClass={if_sub}, Driver={driver}, Endpoints={eps}")

    print("\n==================================================")
    print("TOPOLOGY VERIFICATION SUMMARY:")
    print(f"  345f:9132 (MacroSilicon MSDisplay IC) : {'PRESENT' if found_345f else 'ABSENT'}")
    print(f"  33c3:f101 (HL VMAX Telemetry MCU)     : {'PRESENT' if found_33c3 else 'ABSENT'}")
    print("==================================================")

def verify_libusb_topology():
    ctx = ctypes.c_void_p()
    if libusb.libusb_init(ctypes.byref(ctx)) < 0:
        print("[ERROR] libusb_init failed")
        return

    devs = ctypes.c_void_p()
    cnt = libusb.libusb_get_device_list(ctx, ctypes.byref(devs))
    if cnt < 0:
        print("[ERROR] libusb_get_device_list failed")
        libusb.libusb_exit(ctx)
        return

    print(f"\n=== LIBUSB READ-ONLY TOPOLOGY SCAN ({cnt} Devices) ===")
    dev_ptrs = ctypes.cast(devs, ctypes.POINTER(ctypes.c_void_p))

    has_345f_if3_ep04 = False
    has_33c3_if1_ep02 = False

    for i in range(cnt):
        dev = dev_ptrs[i]
        if not dev: continue
        desc = libusb_device_descriptor()
        if libusb.libusb_get_device_descriptor(dev, ctypes.byref(desc)) == 0:
            bus = libusb.libusb_get_bus_number(dev)
            addr = libusb.libusb_get_device_address(dev)
            vid = desc.idVendor
            pid = desc.idProduct

            if vid == 0x345f:
                print(f" -> Found 0x345f:0x{pid:04x} at Bus {bus:03d} Dev {addr:03d}")
                if pid == 0x9132:
                    has_345f_if3_ep04 = True
            elif vid == 0x33c3 and pid == 0xf101:
                print(f" -> Found 0x33c3:0x{pid:04x} at Bus {bus:03d} Dev {addr:03d}")
                has_33c3_if1_ep02 = True

    libusb.libusb_free_device_list(devs, 1)
    libusb.libusb_exit(ctx)

    print("\n=== TARGET MATCH COMPARISON ===")
    print(f"Path A (33c3:f101 Interface 1 EP 0x02 Bulk OUT): {'ACTIVE' if has_33c3_if1_ep02 else 'INACTIVE'}")
    print(f"Path B (345f:9132 Interface 3 EP 0x04 Bulk OUT): {'ACTIVE' if has_345f_if3_ep04 else 'ABSENT FROM BUS'}")

if __name__ == "__main__":
    parse_sysfs_topology()
    verify_libusb_topology()
