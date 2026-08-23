# Reconciliation: Genuine Windows Vmax vs Current Linux Test (`Vmax_vs_Linux.md`)

## Comparison Table

| Stage | Genuine Windows Vmax Application | Current Linux Implementation | Difference |
|---|---|---|---|
| **USB Enumeration** | Enumerates `33c3:f101` (CDC ACM) and initializes `WinUsbDisplay` / `MSUSBDisplay` driver | Enumerates `33c3:f101` as `/dev/ttyACM0`; `345f:9132` not enumerated | Linux lacks `MSDisplay` driver for video stream |
| **SerialPort Open** | Opens `COMx` at 115200 8N1 via `DeviceCommunicationLibrary.dll` | Opens `/dev/ttyACM0` at 115200 8N1 via `pyserial` | **MATCH** (Serial config identical) |
| **CDC Control State** | `usbser.sys` sends `SET_LINE_CODING` (115200) & `SET_CONTROL_LINE_STATE(0x0000)` | `cdc_acm` sends `SET_LINE_CODING` (115200) & `SET_CONTROL_LINE_STATE(0x0000)` | **MATCH** (Confirmed via usbmon) |
| **Primary Display Engine** | Invokes `MSDisplay` (`MSDISPLAYSDKWRRAPER.dll`) → `Wrraper_MSDisplayStart()` → TurboJPEG capture → `IddSendPicture` | Sends `DeviceCommunicationLibrary.dll` serial protocol frames (`0x0080`, `0x0072`, `0x0071`) | **FIRST DIVERGENCE**: Genuine Vmax drives video via `MSDisplay`, NOT serial commands |
| **Telemetry / Asset MCU** | `DeviceCommunicator.HandshakeAsync` (0x0080) used during asset/theme flashing or status sync | Sends standalone `0x0080` to `33c3:f101` | `33c3:f101` requires active `MSDisplay` session or asset transfer mode |
| **Display Panel Power** | Kept active by continuous video stream from `MSDisplay` | Display turns off (standby timeout) because no video stream is received | Display enters autonomous standby after boot GIF |

## First Behavioral Divergence
**Genuine Vmax drives live video display output through `MSDisplay` (`MSDISPLAYSDKWRRAPER.dll` / WinUSB / Indirect Display Driver), whereas our Linux tests attempted to initialize the display solely via `DeviceCommunicationLibrary.dll` serial commands on `33c3:f101`.**

Because `33c3:f101` is the CDC ACM telemetry/storage MCU (AICDisp), sending standalone serial commands to it without the primary `MSDisplay` video engine active leaves the LCD display panel un-driven, causing the display firmware to enter autonomous standby.
