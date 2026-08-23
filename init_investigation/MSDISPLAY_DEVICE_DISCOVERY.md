# MSDisplay Device Discovery & Interface (`MSDISPLAY_DEVICE_DISCOVERY.md`)

## 1. Class GUIDs & Interface Names (`CONFIRMED STATIC`)
- **Device Interface Class GUID**: `{FB781AAF-9C70-4523-A5DF-642A87ECA567}` (from `MSUSBDisplay.inf`)
- **Setup Class GUID**: `{e3fc78a8-c15c-4955-accd-a73f3eba1639}` (from `MSUSBDisplay.inf`)
- **Win32 Device Path**: `\\\\.\\WinUsbDisplay\\`

## 2. Driver & Kernel Service (`CONFIRMED STATIC`)
- **Service Binary**: `libusb0.sys` (from `MSUSBDisplay.inf`: `ServiceBinary = %12%\\libusb0.sys`)
- **User-Mode DLL**: `MSDISPLAYSDKWRRAPER.dll` (imports `libusb0.dll`, `KERNEL32.dll`, `SETUPAPI.dll`)

## 3. Why MacroSilicon `345f:9132` is Not Enumerating in Linux `lsusb` (`STRONGLY SUPPORTED`)
On Windows, MacroSilicon operates as an **Indirect Display Driver (Idd) / WinUSBDisplay virtual display device**.
It does NOT enumerate as an ordinary USB class device on standard Linux host controllers without the `libusb0` or `WinUsbDisplay` driver initializing the interface handle via `Wrraper_MSDisplayStart()`.
