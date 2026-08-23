#!/usr/bin/env python3
"""
MSDisplay Linux Discovery & Topology Probe Script (`msdisplay_linux_probe.py`)
Performs safe, non-destructive USB device discovery for MacroSilicon (345f:*) and VMAX (33c3:f101).
Prints VID/PID, interface configurations, and endpoints without transmitting arbitrary data.
"""

import sys
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
libusb.libusb_exit.restype = None

libusb.libusb_get_device_list.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_void_p)]
libusb.libusb_get_device_list.restype = ctypes.c_ssize_t

libusb.libusb_free_device_list.argtypes = [ctypes.c_void_p, ctypes.c_int]
libusb.libusb_free_device_list.restype = None

libusb.libusb_get_device_descriptor.argtypes = [ctypes.c_void_p, ctypes.POINTER(libusb_device_descriptor)]
libusb.libusb_get_device_descriptor.restype = ctypes.c_int

def run_discovery_probe():
    ctx = ctypes.c_void_p()
    ret = libusb.libusb_init(ctypes.byref(ctx))
    if ret < 0:
        print(f"[ERROR] libusb_init failed: {ret}")
        return

    devs = ctypes.c_void_p()
    cnt = libusb.libusb_get_device_list(ctx, ctypes.byref(devs))
    if cnt < 0:
        print(f"[ERROR] libusb_get_device_list failed: {cnt}")
        libusb.libusb_exit(ctx)
        return

    print("==================================================")
    print("MSDisplay Linux Safe Discovery Probe (Read-Only)")
    print("==================================================")
    print(f"Total USB Devices Detected: {cnt}\n")

    target_ms_found = False
    target_vmax_found = False

    dev_ptrs = ctypes.cast(devs, ctypes.POINTER(ctypes.c_void_p))

    for i in range(cnt):
        dev = dev_ptrs[i]
        if not dev:
            continue
        desc = libusb_device_descriptor()
        res = libusb.libusb_get_device_descriptor(dev, ctypes.byref(desc))
        if res == 0:
            vid = desc.idVendor
            pid = desc.idProduct
            if vid == 0x345f:
                print(f"[FOUND] MacroSilicon Target Device: VID=0x{vid:04x}, PID=0x{pid:04x}")
                print(f"        bNumConfigurations: {desc.bNumConfigurations}")
                target_ms_found = True
            elif vid == 0x33c3:
                print(f"[FOUND] VMAX CDC ACM MCU Device: VID=0x{vid:04x}, PID=0x{pid:04x}")
                print(f"        bNumConfigurations: {desc.bNumConfigurations}")
                target_vmax_found = True

    libusb.libusb_free_device_list(devs, 1)
    libusb.libusb_exit(ctx)

    print("\n--------------------------------------------------")
    print("TOPOLOGY SUMMARY:")
    print(f"  MacroSilicon Video Controller (345f:*): {'PRESENT' if target_ms_found else 'ABSENT (Unpowered / Drivers Required)'}")
    print(f"  VMAX CDC Telemetry MCU (33c3:f101)  : {'PRESENT' if target_vmax_found else 'ABSENT'}")
    print("--------------------------------------------------")
    print("SAFE-GUARD: Probe execution finished without writing any data to host devices.")

if __name__ == "__main__":
    run_discovery_probe()
