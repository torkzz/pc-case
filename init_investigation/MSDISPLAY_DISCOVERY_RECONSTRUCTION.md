# MSDISPLAY DISCOVERY RECONSTRUCTION (`MSDISPLAY_DISCOVERY_RECONSTRUCTION.md`)

## Evidence Classification
- Target VID/PID Enumeration Constants: [CONFIRMED STATIC]
- Device Class GUID & SetupAPI Imports: [CONFIRMED STATIC]
- Host Topology Device Status: [CONFIRMED LIVE]

---

## Device Selection Logic [CONFIRMED STATIC]

When `Wrraper_MSDisplayGetDeviceList` (RVA `0x147f0`) is invoked, the native DLL executes two parallel discovery paths:

1. **Direct `libusb0.dll` Bus Enumeration**:
   - Executes `usb_init()`, `usb_find_busses()`, `usb_find_devices()`, `usb_get_busses()`.
   - Iterates through connected USB devices and checks `idVendor` and `idProduct`:
     - `idVendor == 0x345f` (MacroSilicon)
     - `idProduct` matches any of: `0x9132`, `0x9133`, `0x374a`, `0xa101`.

2. **SetupAPI / WinUSB Device Interface Enumeration**:
   - `SetupDiGetClassDevsW({FB781AAF-9C70-4523-A5DF-642A87ECA567})`
   - `SetupDiEnumDeviceInterfaces`
   - `SetupDiGetDeviceInterfaceDetailW`
   - `CreateFileW("\\\\.\\WinUsbDisplay\\")`

---

## Target Interface & Endpoint Selection [CONFIRMED STATIC]

- **Interface**: `Interface 3` (`USB\VID_345F&PID_9132&MI_03`)
- **Bulk OUT Endpoint**: `Endpoint 0x04`
- **Max Packet Size**: `512 bytes` (USB 2.0 High-Speed Bulk Endpoint)
- **Transfer Timeout**: `3000 ms`
