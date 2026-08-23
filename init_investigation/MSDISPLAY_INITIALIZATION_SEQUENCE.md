# MSDISPLAY INITIALIZATION SEQUENCE (`MSDISPLAY_INITIALIZATION_SEQUENCE.md`)

## Evidence Classification
- Native API Call Sequence: [CONFIRMED STATIC]
- Transport Endpoint & Interface: [CONFIRMED STATIC]
- Setup Control Buffer Payload Headers: [CONFIRMED STATIC]
- INF Driver Binding: [CONFIRMED STATIC]
- Host Topology Status: [CONFIRMED LIVE]

---

## Complete Initialization Call Chain [CONFIRMED STATIC]

| Step | Operation | API / Parameters | Purpose / Function | Evidence Level |
|---|---|---|---|---|
| 1 | `GetSDKVersion` | `Wrraper_MSDisplayGetSDKVersion(&ver)` | Queries native SDK version (`v3.2.7.36`) | [CONFIRMED STATIC] |
| 2 | `GetDeviceList` | `Wrraper_MSDisplayGetDeviceList(&list, &cnt)` | `libusb0` bus scan (`usb_init`, `usb_find_busses`, `usb_find_devices`, `usb_get_busses`) searching for VID `0x345f` and PIDs `0x9132`, `0x9133`, `0x374a`, `0xa101`. Also checks SetupAPI GUID `{FB781AAF-9C70-4523-A5DF-642A87ECA567}` | [CONFIRMED STATIC] |
| 3 | `GetDeviceInfo` | `Wrraper_MSDisplayGetDeviceInfo(handle, &info)` | Indirect Display Driver IOCTL `0x304054` sub-cmd `0x1002` | [CONFIRMED STATIC] |
| 4 | `CheckCapability` | `Wrraper_MSDisplayCheckDeviceScreenCapability(handle, &cap)` | Indirect Display Driver IOCTL `0x304054` sub-cmd `0x21003` | [CONFIRMED STATIC] |
| 5 | `SetVideoParam` | `Wrraper_MSDisplaySetVideoParam(handle, &params)` | Indirect Display Driver IOCTL `0x304054` sub-cmd `0x21006` | [CONFIRMED STATIC] |
| 6 | `Start` | `Wrraper_MSDisplayStart(handle)` | Opens native handle (`usb_open`), claims `Interface 3` (`usb_claim_interface(dev, 3)`), and issues HID Class setup transfers (`0x21`/`0x09`/`0x0300` Header `0xFB`/`0xB5` and `0xa1`/`0x01`/`0x0300`) | [CONFIRMED STATIC] |
| 7 | `EnableProcessor` | `Wrraper_MSDisplayEnableSDKScreenProcessor(handle, true)` | Activates screen processing loop | [CONFIRMED STATIC] |
| 8 | `SendPicture` | `Wrraper_MSDisplaySendPicture(handle, buf, len)` | Encodes desktop frame to JPEG via TurboJPEG (`tjCompressFromYUV`), prepends 12-byte header (`0x0008100A`, W, H, format, flag), and submits payload to `Endpoint 0x04` Bulk OUT via `usb_bulk_write` (3000ms timeout) | [CONFIRMED STATIC] |

---

## Recovered Setup Control Transfer Data Layouts [CONFIRMED STATIC]

### Call Site 1: SET_REPORT Initialization Transfer
- `bmRequestType`: `0x21` (Host to Interface, Class, Report)
- `bRequest`: `0x09` (`SET_REPORT`)
- `wValue`: `0x0300` (Report Type 0x03, Report ID 0x00)
- `wIndex`: `0` (Interface 3)
- `wLength`: `6` to `8` bytes
- `Payload`: `[0xFB, addr_hi, addr_lo, 0x00, 0x00, 0x00, 0x00]` (Disassembled at `0x180018c18`)

### Call Site 2: SET_REPORT Initialization Transfer
- `bmRequestType`: `0x21` (Host to Interface, Class, Report)
- `bRequest`: `0x09` (`SET_REPORT`)
- `wValue`: `0x0300` (Report Type 0x03, Report ID 0x00)
- `wIndex`: `0` (Interface 3)
- `wLength`: `8` to `16` bytes
- `Payload`: `[0xB5, addr_hi, addr_lo, 0x00, 0x00, 0x00, 0x00, 0x00]` (Disassembled at `0x18001de61`)
