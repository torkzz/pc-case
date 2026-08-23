# VIDEO ARCHITECTURE RECONCILIATION (`VIDEO_ARCHITECTURE_RECONCILIATION.md`)

## Evidence Classification
- Dual Protocol Architecture Mapping: [CONFIRMED STATIC]
- CDC Telemetry Channel: [CONFIRMED STATIC & CONFIRMED LIVE]
- MSDisplay Video Transport Channel: [CONFIRMED STATIC]

---

## Reconciliation of Video Transport Paths [CONFIRMED STATIC]

The VMAX software suite contains two complementary display/control engines:

1. **Path A: Direct MSDisplay Engine (`MSDISPLAYSDKWRRAPER.dll`)**
   - **Target**: MacroSilicon Display Controller (`345f:9132` / `MSUSBDisplay.inf`).
   - **Transport**: `Interface 3`, `Endpoint 0x04` Bulk OUT via `libusb0.dll` / WinUSB.
   - **Function**: Real-time high-speed desktop video streaming (TurboJPEG 60 FPS).

2. **Path B: Composite Model Telemetry & Asset RPC (`libcompositeScreenModel.dll` + `libstack.dll` / `DeviceCommunicationLibrary.dll`)**
   - **Target**: CDC ACM Telemetry MCU (`33c3:f101` at `/dev/ttyACM0`).
   - **Transport**: CDC ACM serial interface, Bulk OUT Endpoint 0x02, Interrupt EP 0x83.
   - **Function**: Device status queries, hardware telemetry, theme asset/GIF flashing, heartbeat ping.

---

## Relationship Between Paths

- Path A (`MSDisplay`) is the **primary live video transport**.
- Path B (`CompositeScreenModel` / `AICDisp`) is the **telemetry, asset, and control channel**.
- Streaming frames over Path A (or sending periodic heartbeat packets over Path B) keeps the display panel active and prevents autonomous backlight standby auto-off.
