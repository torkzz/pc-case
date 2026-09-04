# Vendor Architecture & Dual Transport Investigation

## Executive Summary
The forensic audit of `/home/tor/vmax_bundle/` reveals that `Vmax.exe` supports **two distinct hardware display engines**:

1. **HL VMAX Telemetry & Control Engine (`33c3:f101`)**:
   - **Assembly**: `DeviceCommunicationLibrary.dll`
   - **Transport**: CDC ACM Serial Port (`115200 8N1`, Bulk OUT EP 0x02, Bulk IN EP 0x81).
   - **Protocol**: `AH...MI` structured frames (`41 48 ... 4D 49`).
   - **Engine Class in Vmax.exe**: `AICDisp*` (`AICDispPicture`, `AICDispSendPicture`, `AICDispStart`, `AICDispStop`, `AICDispResolution`).
   - **Target Hardware**: Secondary MCU (`33c3:f101`) managing hardware telemetry, asset storage, status control, and status displays.

2. **MacroSilicon High-Speed Video Engine (`345f:9132` / `345f:*`)**:
   - **Assembly**: `MSDISPLAYSDKWRRAPER.dll` (Native C/C++ DLL wrapper over MacroSilicon USB Display SDK).
   - **Transport**: Native USB Display Bulk Driver (`MSUSBDisplay.inf`, `libusb0.sys`, `UsbDk`).
   - **Native API**: `Wrraper_MSDisplayGetDeviceList`, `Wrraper_MSDisplaySendPicture`, `Wrraper_MSDisplayEnableSDKScreenProcessor`, `Wrraper_MSDisplaySetVideoParam`, `Wrraper_MSDisplayStart`, `Wrraper_MSDisplayStop`.
   - **Engine Class in Vmax.exe**: `MSDisplay*` (`MSDisplayPicture`, `MSDisplaySendPicture`, `MSDisplayStart`, `MSDisplayStop`, `MSDisplayEnableSDKScreenProcessor`).
   - **Target Hardware**: MacroSilicon USB Display Controller ICs (`345f:9132`, `345f:9133`, `345f:374a`, `345f:a101`).

---

## Detailed Component & VID/PID Reference Map

| VID:PID | Device Description | Driver / Transport | Managed Assembly / Wrapper | Engine Class |
| :--- | :--- | :--- | :--- | :--- |
| `33c3:f101` | HL VMAX USB Device | CDC ACM (`cdc_acm`) | `DeviceCommunicationLibrary.dll` | `AICDisp*` |
| `345f:9132` | MacroSilicon MS USB Display | `MSUSBDisplay.inf` / `libusb0` | `MSDISPLAYSDKWRRAPER.dll` | `MSDisplay*` |
| `345f:9133` | MacroSilicon MS USB Display (Alt) | `MSUSBDisplay.inf` / `libusb0` | `MSDISPLAYSDKWRRAPER.dll` | `MSDisplay*` |
| `345f:374a` | MacroSilicon Display Controller | `MSUSBDisplay.inf` / `libusb0` | `MSDISPLAYSDKWRRAPER.dll` | `MSDisplay*` |
| `345f:a101` | MacroSilicon Display Controller | `MSUSBDisplay.inf` / `libusb0` | `MSDISPLAYSDKWRRAPER.dll` | `MSDisplay*` |

---

## Call Order & Engine Selection Logic in `Vmax.exe`

```
Process Startup (Vmax.exe)
  │
  ├── 1. Device Discovery Phase
  │     ├── Call Wrraper_MSDisplayGetDeviceList()
  │     │     ├── If MacroSilicon device (345f:*) detected:
  │     │     │     └── Instantiate MSDisplayEngine (MSDisplaySendPicture)
  │     │     └── If 0 devices returned:
  │     │           └── Fallback to Serial CDC enumeration
  │     │
  │     └── Call DeviceHelper.EnumerateComPorts()
  │           └── If 33c3:f101 serial port (/dev/ttyACM0) detected:
  │                 └── Instantiate AICDispEngine (DeviceCommunicator)
  │
  ├── 2. AICDisp Engine Execution Path (33c3:f101)
  │     ├── Connect(portName, 115200)
  │     ├── HandshakeAsync() [CMD 0x0080]
  │     ├── GetHardwareInfoAsync() [CMD 0x0072]
  │     ├── GetFlashInfoAsync() [CMD 0x0062]
  │     └── AICDispSendPicture() -> RequestDownloadAsync [CMD 0x0081] -> DownloadDataAsync [CMD 0x0082]
  │
  └── 3. MSDisplay Engine Execution Path (345f:9132)
        ├── Wrraper_MSDisplayStart()
        ├── Wrraper_MSDisplayEnableSDKScreenProcessor(true)
        └── Wrraper_MSDisplaySendPicture(deviceHandle, jpegBuffer, bufferSize)
```
