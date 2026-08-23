# MSDisplay Native IOCTLs & USB Transfers (`MSDISPLAY_IOCTLS.md`)

## 1. Discovered USB Endpoint & Interface [CONFIRMED STATIC]

- **USB Interface**: `Interface 3` (`usb_claim_interface(dev, 3)`) [CONFIRMED STATIC]
- **Bulk OUT Endpoint**: `Endpoint 0x04` (`usb_bulk_write(dev, 0x04, buffer, length, 3000)`) [CONFIRMED STATIC]
- **Bulk Timeout**: `3000 ms` (`0xBB8`) [CONFIRMED STATIC]
- **Control Timeout**: `1000 ms` (`0x3E8`) [CONFIRMED STATIC]

## 2. Discovered USB Control & Bulk Transfer Table [CONFIRMED STATIC]

| Function | API | Direction | Endpoint | bmRequestType | bRequest | wValue | wIndex | Length | Timeout | Evidence Level |
|---|---|---|---|---|---|---|---|---|---|---|
| `Wrraper_MSDisplayStart` | `usb_claim_interface` | OUT | N/A | N/A | N/A | N/A | `3` | N/A | N/A | [CONFIRMED STATIC] |
| Static Helper (`0x180018c9e`) | `usb_control_msg` | OUT | `0x00` | `0x21` | `0x09` (SET_REPORT) | `0x0300` | `0` | Var | `1000ms` | [CONFIRMED STATIC] |
| Static Helper (`0x18001dedd`) | `usb_control_msg` | OUT | `0x00` | `0x21` | `0x09` (SET_REPORT) | `0x0300` | `0` | Var | `1000ms` | [CONFIRMED STATIC] |
| Static Helper (`0x18001df5d`) | `usb_control_msg` | IN | `0x00` | `0xa1` | `0x01` (GET_REPORT) | `0x0300` | `0` | Var | `1000ms` | [CONFIRMED STATIC] |
| `Wrraper_MSDisplaySendPicture` | `usb_bulk_write` | OUT | `0x04` | N/A | N/A | N/A | N/A | `FrameLen` | `3000ms` | [CONFIRMED STATIC] |
| `Wrraper_MSDisplaySetVideoParam` | `DeviceIoControl` | OUT | N/A | N/A | `0x304054` | `0x21006` | `0x104` | `0x104` | `1000ms` | [CONFIRMED STATIC] |

## 3. Discovered IOCTL Table [CONFIRMED STATIC]

- `0x304054`: MacroSilicon Indirect Display Driver (Idd) Control IOCTL [CONFIRMED STATIC]
  - Sub-command `0x1001`: `IddGetDriverInfo` [CONFIRMED STATIC]
  - Sub-command `0x1002`: `IddGetDeviceInfo` [CONFIRMED STATIC]
  - Sub-command `0x21003`: `IddGetTopology` / Screen Capability [CONFIRMED STATIC]
  - Sub-command `0x21006`: `IddSetVideoParam` [CONFIRMED STATIC]

## 4. Control & Bulk Payload Buffer Status

- **bmRequestType = 0x21 / bRequest = 0x09 / wValue = 0x0300**: SET_REPORT setup parameters proven. Exact data buffer bytes: [UNKNOWN — RUNTIME CAPTURE REQUIRED].
- **bmRequestType = 0xa1 / bRequest = 0x01 / wValue = 0x0300**: GET_REPORT setup parameters proven. Exact response buffer bytes: [UNKNOWN — RUNTIME CAPTURE REQUIRED].
- **Endpoint 0x04 Bulk OUT Frame Header / Fragmentation**: Endpoint and timeout proven. Exact binary header fields / magic bytes: [UNKNOWN — RUNTIME CAPTURE REQUIRED].
