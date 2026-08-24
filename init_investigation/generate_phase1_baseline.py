import subprocess

def run(cmd):
    try:
        res = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=10)
        return res.stdout
    except Exception as e:
        return str(e)

lsusb_v = run("lsusb -v -d 33c3:f101 2>&1")
lsusb_t = run("lsusb -t 2>&1")
udev_info = run("udevadm info -q all -n /dev/ttyACM0 2>&1")

content = f"""# Full USB Descriptor & Configuration Baseline (`33c3:f101`)

## Overview
Complete descriptor tree, interface associations, CDC ACM capabilities, and udev parameters for device `33c3:f101` on Linux.

## Device Identification & Speed
- **Vendor ID (VID)**: `0x33c3` (`HL VMAX`)
- **Product ID (PID)**: `0xf101` (`HL-VMAX-USB-Device`)
- **USB Device Version**: `2.00`
- **Negotiated Speed**: High-Speed (`480 Mbps`)
- **Device Class**: `239` (Miscellaneous Device)
- **Device SubClass**: `2` (Interface Association Descriptor)
- **Device Protocol**: `1` (IAD - Interface Association)
- **Max Packet Size 0 (Control)**: `64 bytes`
- **Manufacturer String**: `HL VMAX  ` (Index 1)
- **Product String**: `HL-VMAX-USB-Device` (Index 2)
- **Serial Number**: `0` (None)

---

## Interface Association Descriptor (IAD)
- **bFirstInterface**: `0`
- **bInterfaceCount**: `2`
- **bFunctionClass**: `2` (Communications)
- **bFunctionSubClass**: `2` (Abstract / Modem)
- **bFunctionProtocol**: `1` (AT-commands v.25ter)

---

## Interface 0 — CDC Control (`cdc_acm`)
- **bInterfaceNumber**: `0`
- **bAlternateSetting**: `0`
- **bNumEndpoints**: `1`
- **bInterfaceClass**: `2` (Communications)
- **bInterfaceSubClass**: `2` (Abstract Modem)
- **bInterfaceProtocol**: `1` (AT-commands)
- **CDC Functional Descriptors**:
  - `CDC Header`: `bcdCDC 1.10`
  - `CDC Call Management`: `bmCapabilities 0x00` (Data interface handles call management)
  - `CDC ACM`: `bmCapabilities 0x02` (Supports `SET_LINE_CODING`, `GET_LINE_CODING`, `SET_CONTROL_LINE_STATE`, `SERIAL_STATE` notification)
  - `CDC Union`: Master = Interface 0, Slave = Interface 1
- **Endpoint 0x83 (Interrupt IN)**:
  - Transfer Type: Interrupt
  - Direction: IN (Device $\rightarrow$ Host)
  - wMaxPacketSize: `8 bytes`
  - bInterval: `10` (Polling every 10 ms)

---

## Interface 1 — CDC Data (`cdc_acm`)
- **bInterfaceNumber**: `1`
- **bAlternateSetting**: `0`
- **bNumEndpoints**: `2`
- **bInterfaceClass**: `10` (CDC Data)
- **Endpoint 0x02 (Bulk OUT)**:
  - Transfer Type: Bulk
  - Direction: OUT (Host $\rightarrow$ Device)
  - wMaxPacketSize: `512 bytes` (High Speed 480Mbps)
  - bInterval: `0`
- **Endpoint 0x81 (Bulk IN)**:
  - Transfer Type: Bulk
  - Direction: IN (Device $\rightarrow$ Host)
  - wMaxPacketSize: `512 bytes` (High Speed 480Mbps)
  - bInterval: `0`

---

## Raw `lsusb -v -d 33c3:f101` Output
```text
{lsusb_v.strip()}
```

## Raw `lsusb -t` Output
```text
{lsusb_t.strip()}
```

## Raw `udevadm info -q all -n /dev/ttyACM0` Output
```text
{udev_info.strip()}
```
"""

with open("/home/tor/pc-case-lcd/USB_DESCRIPTOR_BASELINE.md", "w") as f:
    f.write(content)

print("Generated /home/tor/pc-case-lcd/USB_DESCRIPTOR_BASELINE.md")
