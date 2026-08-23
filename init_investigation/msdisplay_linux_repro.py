#!/usr/bin/env python3
"""
MSDisplay Linux Minimal Reproduction Prototype (`msdisplay_linux_repro.py`)

Fulfills Phase 12 Requirements:
1. Enumerate target device (345f:* or 33c3:f101).
2. Print descriptors.
3. Claim interface safely (detach kernel driver if required).
4. Execute proven initialization setup transfers.
5. Print every transfer / result in real time.
6. Stop safely.
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

libusb.libusb_claim_interface.argtypes = [ctypes.c_void_p, ctypes.c_int]
libusb.libusb_claim_interface.restype = ctypes.c_int

libusb.libusb_release_interface.argtypes = [ctypes.c_void_p, ctypes.c_int]
libusb.libusb_release_interface.restype = ctypes.c_int

libusb.libusb_kernel_driver_active.argtypes = [ctypes.c_void_p, ctypes.c_int]
libusb.libusb_kernel_driver_active.restype = ctypes.c_int

libusb.libusb_detach_kernel_driver.argtypes = [ctypes.c_void_p, ctypes.c_int]
libusb.libusb_detach_kernel_driver.restype = ctypes.c_int

libusb.libusb_attach_kernel_driver.argtypes = [ctypes.c_void_p, ctypes.c_int]
libusb.libusb_attach_kernel_driver.restype = ctypes.c_int

libusb.libusb_control_transfer.argtypes = [
    ctypes.c_void_p,
    ctypes.c_uint8,  # bmRequestType
    ctypes.c_uint8,  # bRequest
    ctypes.c_uint16, # wValue
    ctypes.c_uint16, # wIndex
    ctypes.c_char_p, # data
    ctypes.c_uint16, # wLength
    ctypes.c_uint    # timeout
]
libusb.libusb_control_transfer.restype = ctypes.c_int

TARGET_VIDS = [0x345f, 0x33c3]

def run_repro():
    print("=== MSDisplay Linux Reproduction Prototype (Phase 12) ===")
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

    print(f"[STEP 1] Enumerating {cnt} host USB devices...")
    target_dev = None
    target_desc = libusb_device_descriptor()

    dev_ptrs = ctypes.cast(devs, ctypes.POINTER(ctypes.c_void_p))
    for i in range(cnt):
        dev = dev_ptrs[i]
        if not dev:
            continue
        desc = libusb_device_descriptor()
        if libusb.libusb_get_device_descriptor(dev, ctypes.byref(desc)) == 0:
            if desc.idVendor in TARGET_VIDS:
                target_dev = dev
                target_desc = desc
                print(f"[SUCCESS] Target Device Located: VID=0x{desc.idVendor:04x}, PID=0x{desc.idProduct:04x}")
                if desc.idVendor == 0x345f:
                    break  # Prefer 345f if present

    if not target_dev:
        print("[ERROR] No candidate MSDisplay or VMAX device found on host USB bus.")
        libusb.libusb_free_device_list(devs, 1)
        libusb.libusb_exit(ctx)
        return

    print("\n[STEP 2] Descriptors:")
    print(f"  VID:PID         : 0x{target_desc.idVendor:04x}:0x{target_desc.idProduct:04x}")
    print(f"  bcdUSB          : 0x{target_desc.bcdUSB:04x}")
    print(f"  bDeviceClass    : {target_desc.bDeviceClass}")
    print(f"  bMaxPacketSize0 : {target_desc.bMaxPacketSize0}")
    print(f"  bNumConfigs     : {target_desc.bNumConfigurations}")

    handle = ctypes.c_void_p()
    res = libusb.libusb_open(target_dev, ctypes.byref(handle))
    if res != 0:
        print(f"[ERROR] libusb_open failed with status code {res}")
        libusb.libusb_free_device_list(devs, 1)
        libusb.libusb_exit(ctx)
        return

    print("\n[STEP 3] Testing Control Setup GET_DESCRIPTOR / Feature Transfer:")
    # Read Device Descriptor via control transfer 0x80 / 0x06 / 0x0100
    buf = ctypes.create_string_buffer(18)
    ctrl_res = libusb.libusb_control_transfer(handle, 0x80, 0x06, 0x0100, 0, buf, 18, 1000)
    print(f"  GET_DESCRIPTOR (0x80 / 0x06 / 0x0100) -> Status: {ctrl_res} bytes read")
    if ctrl_res > 0:
        print(f"  Hex Bytes: {buf.raw[:ctrl_res].hex(' ')}")

    # If device is 345f:9132, claim Interface 3 and test proven setup control transfer
    if target_desc.idVendor == 0x345f:
        print("\n[STEP 4] Claiming Interface 3 on 345f:9132...")
        if libusb.libusb_kernel_driver_active(handle, 3) == 1:
            libusb.libusb_detach_kernel_driver(handle, 3)
        claim_res = libusb.libusb_claim_interface(handle, 3)
        print(f"  libusb_claim_interface(3) -> Status: {claim_res}")

        if claim_res == 0:
            print("[STEP 5] Executing proven SET_REPORT setup transfer (0x21 / 0x09 / 0x0300)...")
            set_buf = ctypes.create_string_buffer(8)
            set_res = libusb.libusb_control_transfer(handle, 0x21, 0x09, 0x0300, 3, set_buf, 8, 1000)
            print(f"  SET_REPORT (0x21 / 0x09 / 0x0300) -> Result Code: {set_res}")
            libusb.libusb_release_interface(handle, 3)

    libusb.libusb_close(handle)
    libusb.libusb_free_device_list(devs, 1)
    libusb.libusb_exit(ctx)
    print("\n=== Minimal Reproduction Prototype Execution Finished ===")

if __name__ == "__main__":
    run_repro()
