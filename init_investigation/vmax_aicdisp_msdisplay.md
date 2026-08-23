# Dual-Engine Architecture: AICDisp vs MSDisplay (`vmax_aicdisp_msdisplay.md`)

## Overview
Analysis derived from binary strings, native DLL exports, and disassembly of `Vmax.exe`, `DeviceCommunicationLibrary.dll`, `MSDISPLAYSDKWRRAPER.dll`, `libstack.dll`, and `libcompositeScreenModel.dll`.

## Architecture Mapping

```
Vmax.exe (Master Application)
  │
  ├── 1. AICDisp Engine (DeviceCommunicationLibrary.dll)
  │     ├── Target: 33c3:f101 (HL VMAX CDC ACM MCU)
  │     ├── Transport: SerialPort (/dev/ttyACM0, 115200 8N1)
  │     ├── Purpose: Telemetry, status reporting, SPI Flash asset storage (Texture.acf)
  │     └── Native/P-Invoke exports in Vmax.exe:
  │           - AICDispStart
  │           - AICDispStop
  │           - AICDispPicture
  │           - AICDispResolution
  │           - AICDispSendPicture
  │           - AICDispRegisterCallback
  │
  └── 2. MSDisplay Engine (MSDISPLAYSDKWRRAPER.dll)
        ├── Target: MacroSilicon Display Controller (345f:9132 / MSUSBDisplay)
        ├── Driver: WinUSB / Indirect Display Driver (Idd) / MSUSBDisplay.inf
        ├── Transport: Direct USB / WinUSB / DeviceIoControl (IddSendPicture)
        ├── Native Exports in MSDISPLAYSDKWRRAPER.dll:
        │     - Wrraper_MSDisplayGetDeviceList
        │     - Wrraper_MSDisplayStart
        │     - Wrraper_MSDisplayStop
        │     - Wrraper_MSDisplaySendPicture
        │     - Wrraper_MSDisplayEnableSDKScreenProcessor
        │     - Wrraper_MSDisplayCheckDeviceScreenCapability
        │     - Wrraper_MSDisplaySetVideoParam
        │     - Wrraper_MSDisplayReadSN / ReadFlash / WriteFlash
        └── Purpose: Real-time high-speed desktop video streaming & frame display
```

## Key Architectural Insights

1. **Why `33c3:f101` accepts OUT frames but returns 0 bytes on EP `0x81`**:
   `33c3:f101` is the **AICDisp telemetry & asset storage MCU**. In normal operation, live video display streaming does NOT go through `DeviceCommunicationLibrary.dll` serial protocol — it is handled by the native `MSDisplay` engine via `MSDISPLAYSDKWRRAPER.dll`.

2. **Why the LCD displays a boot GIF, static image, then shuts down**:
   Upon receiving host USB-C power, the onboard MCU autonomously plays a boot GIF from SPI Flash and displays a default static image (`Texture.acf`). If the host application does not initialize the video stream (`MSDisplayStart` / `Wrraper_MSDisplayStart`), the display panel firmware automatically powers off the LCD backlight to enter standby. The `33c3:f101` USB SIE remains connected and active on the host USB bus (`DISPLAY_APPLICATION_SHUTDOWN`).
