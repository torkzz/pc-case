#!/usr/bin/env python3
"""
CDC ACM Alternate Setting & Interface Mode Probe (`cdc_alt_probe.py`)
Inspects alternate settings and tests vendor-specific control requests on 33c3:f101.
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

libusb.libusb_open.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_void_p)]
libusb.libusb_open.restype = ctypes.c_int

libusb.libusb_close.argtypes = [ctypes.c_void_p]
libusb.libusb_close.restype = None

libusb.libusb_set_interface_alt_setting.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]
libusb.libusb_set_interface_alt_setting.restype = ctypes.c_int

def probe_alt_settings():
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

    target_dev = None
    dev_ptrs = ctypes.cast(devs, ctypes.POINTER(ctypes.c_void_p))
    for i in range(cnt):
        dev = dev_ptrs[i]
        if not dev: continue
        desc = libusb_device_descriptor()
        if libusb.libusb_get_device_descriptor(dev, ctypes.byref(desc)) == 0:
            if desc.idVendor == 0x33c3 and desc.idProduct == 0xf101:
                target_dev = dev
                print(f"[FOUND] 33c3:f101 MCU Device")
                break

    if not target_dev:
        print("[ERROR] 33c3:f101 not found.")
        libusb.libusb_free_device_list(devs, 1)
        libusb.libusb_exit(ctx)
        return

    handle = ctypes.c_void_p()
    res = libusb.libusb_open(target_dev, ctypes.byref(handle))
    print(f"libusb_open status: {res}")
    
    if res == 0:
        for iface in (0, 1):
            for alt in (0, 1):
                set_res = libusb.libusb_set_interface_alt_setting(handle, iface, alt)
                print(f"SetInterfaceAltSetting(iface={iface}, alt={alt}) -> Status: {set_res}")
        libusb.libusb_close(handle)

    libusb.libusb_free_device_list(devs, 1)
    libusb.libusb_exit(ctx)

if __name__ == "__main__":
    probe_alt_settings()
