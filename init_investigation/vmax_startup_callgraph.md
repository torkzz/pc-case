# Vmax Startup Callgraph (`vmax_startup_callgraph.md`)

```
Vmax.exe Startup
  │
  ├── 1. UI & Plugin Initialization (Prism.Wpf / DryIoc)
  │     ├── Registers AICDispEngine and MSDisplayEngine
  │     └── Loads theme schemes (ThemeScheme.db)
  │
  ├── 2. Control & Asset MCU Discovery (33c3:f101)
  │     ├── Enumerates COM ports (/dev/ttyACM0)
  │     ├── DeviceCommunicator.Connect("/dev/ttyACM0", 115200)
  │     └── HandshakeAsync() [CMD 0x0080] → GetHardwareInfoAsync() [CMD 0x0072]
  │
  └── 3. Primary Display Driver Initialization (MSDisplay)
        ├── Wrraper_MSDisplayGetDeviceList(&deviceList, &deviceCount)
        ├── Wrraper_MSDisplayStart(handle)
        ├── Wrraper_MSDisplayEnableSDKScreenProcessor(handle, true)
        └── Live Desktop Frame Rendering Loop:
              └── Wrraper_MSDisplaySendPicture(handle, turboJpegBuffer, bufferLen)
```
