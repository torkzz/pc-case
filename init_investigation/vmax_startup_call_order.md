# Vmax Application Startup & Execution Call Order

## Overview
Sequence traced from disassembly of `Vmax.exe`, `DeviceCommunicationLibrary.dll`, and `MSDISPLAYSDKWRRAPER.dll`.

## Chronological Call Order

```
Vmax.exe Startup
  │
  ├── 1. Framework Initialization
  │     ├── WPF / Prism.DryIoc container setup
  │     └── Registrations of AICDispEngine and MSDisplayEngine
  │
  ├── 2. Control MCU Discovery & Connection (33c3:f101)
  │     ├── DeviceHelper.EnumerateComPorts()
  │     ├── DeviceCommunicator.Connect("/dev/ttyACM0", 115200)
  │     ├── DeviceCommunicator.HandshakeAsync() [CMD 0x0080]
  │     └── DeviceCommunicator.GetHardwareInfoAsync() [CMD 0x0072]
  │
  ├── 3. MacroSilicon Display Controller Discovery (345f:9132)
  │     ├── Wrraper_MSDisplayGetDeviceList(&deviceList, &deviceCount)
  │     │
  │     ├── IF MacroSilicon device (345f:*) is DETECTED:
  │     │     ├── Wrraper_MSDisplayStart(handle)
  │     │     ├── Wrraper_MSDisplayEnableSDKScreenProcessor(handle, true)
  │     │     └── Real-time rendering loop:
  │     │           └── Wrraper_MSDisplaySendPicture(handle, jpegBuffer, bufferLen)
  │     │
  │     └── IF MacroSilicon device (345f:*) is NOT DETECTED:
  │           └── Fallback to AICDisp telemetry/asset mode over Serial CDC
```

## Key Architectural Answer
- **Does Vmax start AICDisp (33c3:f101) before MSDisplay (345f:9132)?**
  Yes. Serial CDC connection to `33c3:f101` and `HandshakeAsync` (CMD `0x0080`) are executed first during device initialization, prior to calling `Wrraper_MSDisplayGetDeviceList`.
