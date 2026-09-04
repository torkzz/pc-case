# Full USB Descriptor & Configuration Baseline (`33c3:f101`)

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
  - Direction: IN (Device $ightarrow$ Host)
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
  - Direction: OUT (Host $ightarrow$ Device)
  - wMaxPacketSize: `512 bytes` (High Speed 480Mbps)
  - bInterval: `0`
- **Endpoint 0x81 (Bulk IN)**:
  - Transfer Type: Bulk
  - Direction: IN (Device $ightarrow$ Host)
  - wMaxPacketSize: `512 bytes` (High Speed 480Mbps)
  - bInterval: `0`

---

## Raw `lsusb -v -d 33c3:f101` Output
```text
Couldn't open device, some information will be missing

Bus 001 Device 002: ID 33c3:f101 HL VMAX   HL-VMAX-USB-Device
Negotiated speed: High Speed (480Mbps)
Device Descriptor:
  bLength                18
  bDescriptorType         1
  bcdUSB               2.00
  bDeviceClass          239 Miscellaneous Device
  bDeviceSubClass         2 [unknown]
  bDeviceProtocol         1 Interface Association
  bMaxPacketSize0        64
  idVendor           0x33c3 HL VMAX  
  idProduct          0xf101 HL-VMAX-USB-Device
  bcdDevice            1.41
  iManufacturer           1 HL VMAX  
  iProduct                2 HL-VMAX-USB-Device
  iSerial                 0 
  bNumConfigurations      1
  Configuration Descriptor:
    bLength                 9
    bDescriptorType         2
    wTotalLength       0x004b
    bNumInterfaces          2
    bConfigurationValue     1
    iConfiguration          0 
    bmAttributes         0x80
      (Bus Powered)
    MaxPower              100mA
    Interface Association:
      bLength                 8
      bDescriptorType        11
      bFirstInterface         0
      bInterfaceCount         2
      bFunctionClass          2 Communications
      bFunctionSubClass       2 Abstract (modem)
      bFunctionProtocol       1 AT-commands (v.25ter)
      iFunction               0 
    Interface Descriptor:
      bLength                 9
      bDescriptorType         4
      bInterfaceNumber        0
      bAlternateSetting       0
      bNumEndpoints           1
      bInterfaceClass         2 Communications
      bInterfaceSubClass      2 Abstract (modem)
      bInterfaceProtocol      1 AT-commands (v.25ter)
      iInterface              2 
      CDC Header:
        bcdCDC               1.10
      CDC Call Management:
        bmCapabilities       0x00
        bDataInterface          1
      CDC ACM:
        bmCapabilities       0x02
          line coding and serial state
      CDC Union:
        bMasterInterface        0
        bSlaveInterface         1 
      Endpoint Descriptor:
        bLength                 7
        bDescriptorType         5
        bEndpointAddress     0x83  EP 3 IN
        bmAttributes            3
          Transfer Type            Interrupt
          Synch Type               None
          Usage Type               Data
        wMaxPacketSize     0x0008  1x 8 bytes
        bInterval              10
    Interface Descriptor:
      bLength                 9
      bDescriptorType         4
      bInterfaceNumber        1
      bAlternateSetting       0
      bNumEndpoints           2
      bInterfaceClass        10 CDC Data
      bInterfaceSubClass      0 [unknown]
      bInterfaceProtocol      0 
      iInterface              0 
      Endpoint Descriptor:
        bLength                 7
        bDescriptorType         5
        bEndpointAddress     0x02  EP 2 OUT
        bmAttributes            2
          Transfer Type            Bulk
          Synch Type               None
          Usage Type               Data
        wMaxPacketSize     0x0200  1x 512 bytes
        bInterval               0
      Endpoint Descriptor:
        bLength                 7
        bDescriptorType         5
        bEndpointAddress     0x81  EP 1 IN
        bmAttributes            2
          Transfer Type            Bulk
          Synch Type               None
          Usage Type               Data
        wMaxPacketSize     0x0200  1x 512 bytes
        bInterval               0
```

## Raw `lsusb -t` Output
```text
/:  Bus 001.Port 001: Dev 001, Class=root_hub, Driver=xhci_hcd/10p, 480M
    |__ Port 008: Dev 003, If 0, Class=Audio, Driver=snd-usb-audio, 12M
    |__ Port 008: Dev 003, If 1, Class=Audio, Driver=snd-usb-audio, 12M
    |__ Port 008: Dev 003, If 2, Class=Audio, Driver=snd-usb-audio, 12M
    |__ Port 008: Dev 003, If 3, Class=Human Interface Device, Driver=usbhid, 12M
    |__ Port 009: Dev 002, If 0, Class=Communications, Driver=cdc_acm, 480M
    |__ Port 009: Dev 002, If 1, Class=CDC Data, Driver=cdc_acm, 480M
/:  Bus 002.Port 001: Dev 001, Class=root_hub, Driver=xhci_hcd/4p, 10000M
/:  Bus 003.Port 001: Dev 001, Class=root_hub, Driver=xhci_hcd/4p, 480M
    |__ Port 002: Dev 011, If 0, Class=Human Interface Device, Driver=usbhid, 12M
    |__ Port 002: Dev 011, If 1, Class=Human Interface Device, Driver=usbhid, 12M
    |__ Port 004: Dev 003, If 0, Class=Hub, Driver=hub/4p, 480M
        |__ Port 002: Dev 004, If 0, Class=Human Interface Device, Driver=usbhid, 12M
        |__ Port 002: Dev 004, If 1, Class=Human Interface Device, Driver=usbhid, 12M
/:  Bus 004.Port 001: Dev 001, Class=root_hub, Driver=xhci_hcd/4p, 10000M
```

## Raw `udevadm info -q all -n /dev/ttyACM0` Output
```text
P: /devices/pci0000:00/0000:00:01.2/0000:02:00.0/usb1/1-9/1-9:1.0/tty/ttyACM0
M: ttyACM0
R: 0
J: c166:0
U: tty
D: c 166:0
N: ttyACM0
L: 0
S: serial/by-path/pci-0000:02:00.0-usb-0:9:1.0
S: serial/by-path/pci-0000:02:00.0-usbv2-0:9:1.0
S: serial/by-id/usb-HL_VMAX_HL-VMAX-USB-Device-if00
E: DEVPATH=/devices/pci0000:00/0000:00:01.2/0000:02:00.0/usb1/1-9/1-9:1.0/tty/ttyACM0
E: DEVNAME=/dev/ttyACM0
E: MAJOR=166
E: MINOR=0
E: SUBSYSTEM=tty
E: USEC_INITIALIZED=3059639661
E: ID_BUS=usb
E: ID_MODEL=HL-VMAX-USB-Device
E: ID_MODEL_ENC=HL-VMAX-USB-Device
E: ID_MODEL_ID=f101
E: ID_SERIAL=HL_VMAX_HL-VMAX-USB-Device
E: ID_VENDOR=HL_VMAX
E: ID_VENDOR_ENC=HL\x20VMAX\x20\x20
E: ID_VENDOR_ID=33c3
E: ID_REVISION=0141
E: ID_TYPE=generic
E: ID_USB_MODEL=HL-VMAX-USB-Device
E: ID_USB_MODEL_ENC=HL-VMAX-USB-Device
E: ID_USB_MODEL_ID=f101
E: ID_USB_SERIAL=HL_VMAX_HL-VMAX-USB-Device
E: ID_USB_VENDOR=HL_VMAX
E: ID_USB_VENDOR_ENC=HL\x20VMAX\x20\x20
E: ID_USB_VENDOR_ID=33c3
E: ID_USB_REVISION=0141
E: ID_USB_TYPE=generic
E: ID_USB_INTERFACES=:020201:0a0000:
E: ID_USB_INTERFACE_NUM=00
E: ID_USB_DRIVER=cdc_acm
E: ID_USB_CLASS_FROM_DATABASE=Miscellaneous Device
E: ID_USB_PROTOCOL_FROM_DATABASE=Interface Association
E: ID_PATH_WITH_USB_REVISION=pci-0000:02:00.0-usbv2-0:9:1.0
E: ID_PATH=pci-0000:02:00.0-usb-0:9:1.0
E: ID_PATH_TAG=pci-0000_02_00_0-usb-0_9_1_0
E: ID_INTEGRATION=external
E: ID_MM_CANDIDATE=1
E: DEVLINKS=/dev/serial/by-path/pci-0000:02:00.0-usb-0:9:1.0 /dev/serial/by-path/pci-0000:02:00.0-usbv2-0:9:1.0 /dev/serial/by-id/usb-HL_VMAX_HL-VMAX-USB-Device-if00
E: TAGS=:systemd:
E: CURRENT_TAGS=:systemd:
```
