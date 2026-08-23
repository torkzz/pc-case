# Update all ledgers and vmax_init_state_machine.md to reflect Linux-only active status

ledger_text = """# Comprehensive Evidence Ledger & Protocol Specification

## Project Status Statement
**Linux-only investigation active; Windows capture unavailable and NOT required for current investigation.**

## Evidence Level Classifications
- **CONFIRMED STATIC**: Proven by IL disassembly of `DeviceCommunicationLibrary.dll`, `Vmax.exe`, and native disassembly of `MSDISPLAYSDKWRRAPER.dll`, `libstack.dll`, `libcompositeScreenModel.dll`.
- **CONFIRMED LIVE / HOST_USB_CONFIRMED**: Proven by `lsusb -v`, `lsusb -t`, sysfs `/sys/bus/usb/devices/1-9`, and kernel `usbmon1` URB submission and completion status `0`.
- **WIRE_TX_CONFIRMED**: Proven by kernel `usbmon1` capture confirming 10-byte frame payload `41 48 00 02 00 80 00 00 4D 49` passed to physical USB host controller EP 0x02.
- **DEVICE_RX_UNKNOWN**: Host USB controller submitted Bulk OUT transfer successfully; physical MCU application-level reception not established.
- **DEVICE_RESPONSE_NOT_OBSERVED**: Endpoint 0x81 (Bulk IN) and Endpoint 0x83 (Interrupt IN) returned 0 bytes within observation windows across all 12 matrix test sequences (A–L).
- **HYPOTHESIS**: Unproven candidate root cause under systematic investigation.

---

## Dual Architecture Evidence Summary

| Component | VID:PID | Driver | Managed / Native Assembly | Role / Function | Evidence Level |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **HL VMAX Controller** | `33c3:f101` | CDC ACM (`cdc_acm`) | `DeviceCommunicationLibrary.dll` | Telemetry, status, and theme asset storage MCU | **CONFIRMED STATIC** / **CONFIRMED LIVE** |
| **MacroSilicon Display** | `345f:9132` | `MSUSBDisplay.inf` / `libusb0` | `MSDISPLAYSDKWRRAPER.dll` | Real-time high-speed video/framebuffer transport IC | **CONFIRMED STATIC** |

---

## Runtime Status of `33c3:f101`
- **HOST USB TX**: **WIRE_TX_CONFIRMED** (10-byte frame `41 48 00 02 00 80 00 00 4D 49` sent on EP 0x02, status 0).
- **DEVICE RX**: **DEVICE_RX_UNKNOWN** (Host submission confirmed; physical MCU application-level reception not established).
- **DEVICE RESPONSE**: **DEVICE_RESPONSE_NOT_OBSERVED** (0 bytes returned on EP 0x81 / EP 0x83 across 12 matrix sequences).
"""

with open("/home/tor/pc-case-lcd/EVIDENCE.md", "w") as f:
    f.write(ledger_text)

with open("/home/tor/pc-case-lcd/VMAX_RUNTIME_EVIDENCE.md", "w") as f:
    f.write(ledger_text)

sm_text = """# VMAX Device Initialization State Machine

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
"""

with open("/home/tor/pc-case-lcd/vmax_init_state_machine.md", "w") as f:
    f.write(sm_text)

print("Updated EVIDENCE.md, VMAX_RUNTIME_EVIDENCE.md, and vmax_init_state_machine.md")
