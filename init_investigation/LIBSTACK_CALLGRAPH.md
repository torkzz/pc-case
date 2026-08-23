# LIBSTACK CALLGRAPH (`LIBSTACK_CALLGRAPH.md`)

## Evidence Classification
- Class Hierarchy & Exports: [CONFIRMED STATIC]
- Internal USB Backends (libusb/WinUSB/UsbDk): [CONFIRMED STATIC]

---

## 1. Class & Method Mapping (`libstack.dll`) [CONFIRMED STATIC]

```
SavManager::instance()
    ↓
SavManager::init()
    ↓
SavApp::register_model()
    ↓
SavApp::async_action(device_id, opcode, payload, callback)
    ↓
CompositeDevice::send_data()
    ↓
libusb_bulk_transfer / libusb_control_transfer
```

---

## 2. Low-Level USB Backends Embedded in `libstack.dll` [CONFIRMED STATIC]

- **`libusb` backend**: `libusb_open`, `libusb_claim_interface`, `libusb_control_transfer`, `libusb_bulk_transfer`.
- **`WinUSB` backend**: `WinUsb_Initialize`, `WinUsb_ControlTransfer`, `WinUsb_WritePipe`, `WinUsb_ReadPipe`.
- **`UsbDk` backend**: `UsbDk_StartRedirect`, `UsbDk_WritePipe`.
