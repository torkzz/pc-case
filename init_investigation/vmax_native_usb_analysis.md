# Native USB & Display Driver Analysis (`vmax_native_usb_analysis.md`)

## Overview
Analysis derived from binary disassembly and string extraction of `MSDISPLAYSDKWRRAPER.dll`, `libstack.dll`, and `MSUSBDisplay.inf`.

## Native Driver & API Calls in `MSDISPLAYSDKWRRAPER.dll`

- **Device Interface Path**: `\\.\\WinUsbDisplay\\`
- **Device Driver INF**: `MSUSBDisplay.inf` (`USB\VID_345F&PID_9132&MI_03`)
- **Native Windows APIs**:
  - `CreateFileW` (opens handle to `WinUsbDisplay`)
  - `DeviceIoControl` (dispatches control codes to Indirect Display Driver)
  - `SetupDiGetClassDevsW` / `SetupDiEnumDeviceInterfaces` (enumerates display adapters)
- **Indirect Display Driver (Idd) Control Codes**:
  - `IddGetDeviceInfo`
  - `IddGetDeviceStatus`
  - `IddGetDriverInfo`
  - `IddGetTopology`
  - `IddSendPicture`

## Native USB Stack in `libstack.dll`

- **Driver Layer**: WinUSB (`WinUsb_*` functions dynamically loaded via `GetProcAddress`) and HID (`HidD_*`).
- **HID Operations**: `HidD_GetAttributes`, `HidD_GetHidGuid`, `HidD_GetManufacturerString`, `HidD_FlushQueue`.
- **Bulk Transfer Handling**: `msdisplay_bulk_transfer` function with timeout handling.
