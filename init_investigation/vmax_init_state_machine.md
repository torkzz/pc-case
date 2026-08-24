# VMAX Device Initialization State Machine

## Overview
State machine diagram of `DeviceCommunicator` and `Vmax.exe` initialization phases.

```mermaid
graph TD
    A[Linux System Power On] --> B[USB High-Speed Enumeration VID:PID 33c3:f101]
    B --> C[Kernel cdc_acm Driver Binds /dev/ttyACM0]
    C --> D[DeviceCommunicator.Connect 115200 8N1]
    D --> E[CDC Control Transfer SET_LINE_CODING & SET_CONTROL_LINE_STATE]
    E --> F[HandshakeAsync CMD 0x0080 Frame Sent to EP 0x02]
    F --> G{Device Application Response Received?}
    G -- Yes --> H[State Active: Telemetry & Asset Upload Ready]
    G -- No / Timeout --> I[Device Response Not Observed: MCU Core Unresponsive or Standby]
```

## Status
- **Current State**: `Device Response Not Observed` at Step G.
- **Investigation Focus**: Identifying missing hardware trigger / secondary MacroSilicon USB header or power rail enable.
