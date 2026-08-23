# MSDISPLAY FUNCTION MAP (`MSDISPLAY_FUNCTION_MAP.md`)

## Evidence Classification
- Native DLL Exports & Addresses: [CONFIRMED STATIC]
- PE Import Addresses & Target Libraries: [CONFIRMED STATIC]

---

## Complete Export Map (`MSDISPLAYSDKWRRAPER.dll`) [CONFIRMED STATIC]

| Function Export | RVA / VA | Purpose | Direct USB / Win32 API Call |
|---|---|---|---|
| `Wrraper_MSDisplayGetSDKVersion` | `0x147d0` / `0x1800147d0` | Returns SDK version DWORDs (`3.2.7.36`) | Standard return |
| `Wrraper_MSDisplayGetDeviceList` | `0x147f0` / `0x1800147f0` | Scans libusb0 & SetupAPI for target VID/PIDs | `libusb_find_devices`, `SetupDiGetClassDevsW` |
| `Wrraper_MSDisplayGetDeviceInfo` | `0x14880` / `0x180014880` | Queries display device topology & caps | `DeviceIoControl(0x304054, 0x1002)` |
| `Wrraper_MSDisplaySetVideoParam` | `0x148a0` / `0x1800148a0` | Configures video resolution & parameters | `DeviceIoControl(0x304054, 0x21006)` |
| `Wrraper_MSDisplayStart` | `0x14700` / `0x180014700` | Opens device, claims interface, issues HID control | `usb_open`, `usb_claim_interface(dev, 3)`, `usb_control_msg` |
| `Wrraper_MSDisplayStop` | `0x14710` / `0x180014710` | Releases interface & closes device handle | `usb_release_interface(dev, 3)`, `usb_close` |
| `Wrraper_MSDisplayEnableSDKScreenProcessor` | `0x15460` / `0x180015460` | Activates screen frame processing loop | Internal state flag assignment |
| `Wrraper_MSDisplaySendPicture` | `0x14a70` / `0x180014a70` | Encodes RGB frame to JPEG & streams over Bulk OUT | TurboJPEG `tjCompressFromYUV`, `usb_bulk_write(EP 0x04, 3000ms)` |
| `Wrraper_MSDisplayCheckDeviceScreenCapability` | `0x15480` / `0x180015480` | Queries screen capability | `DeviceIoControl(0x304054, 0x21003)` |
