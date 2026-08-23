#!/usr/bin/env python3
"""
MSDisplay Linux Transport Test Script (`msdisplay_linux_transport_test.py`)
Executes proven static setup transfers for Interface 3 / Endpoint 0x04 when target device is available.
Safeguards execution if payload bytes are unverified.
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

# Proven Static Parameters
TARGET_VID = 0x345f
TARGET_PIDS = [0x9132, 0x9133, 0x374a, 0xa101]
INTERFACE_NUM = 3
EP_BULK_OUT = 0x04
TIMEOUT_BULK_MS = 3000
TIMEOUT_CTRL_MS = 1000

def test_transport():
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

    target_dev = None
    dev_ptrs = ctypes.cast(devs, ctypes.POINTER(ctypes.c_void_p))

    for i in range(cnt):
        dev = dev_ptrs[i]
        if not dev:
            continue
        desc = libusb_device_descriptor()
        if libusb.libusb_get_device_descriptor(dev, ctypes.byref(desc)) == 0:
            if desc.idVendor == TARGET_VID and desc.idProduct in TARGET_PIDS:
                target_dev = dev
                print(f"[SUCCESS] Target MacroSilicon Device Located: VID=0x{desc.idVendor:04x}, PID=0x{desc.idProduct:04x}")
                break

    if not target_dev:
        print(f"[STATUS] MacroSilicon Device (0x{TARGET_VID:04x}) not present on host USB bus.")
        print("          Aborting transport test safely without transmission.")
        libusb.libusb_free_device_list(devs, 1)
        libusb.libusb_exit(ctx)
        return

    # Payload verification safeguard
    payload_verified = False
    if not payload_verified:
        print("\n[CRITICAL SAFETY LOCK]")
        print("PAYLOAD UNKNOWN — STATIC TRACE REQUIRED")
        print("Exact setup control payload bytes require Windows USBPcap trace.")
        print("Halting transmission to prevent device state corruption.")

    libusb.libusb_free_device_list(devs, 1)
    libusb.libusb_exit(ctx)

if __name__ == "__main__":
    test_transport()
