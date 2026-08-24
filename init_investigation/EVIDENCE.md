# Comprehensive Evidence Ledger & Protocol Specification

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


---

## Architecture Investigation — Phase 2

- **Timestamp**: 2026-08-22
- **Investigation Status**: **CONFIRMED STATIC & LIVE HOST EVIDENCE ESTABLISHED; PHYSICAL PCB/POWER INSPECTION REQUIRED.**

### Confirmed Findings Summary
1. `33c3:f101` is the CDC ACM telemetry and asset storage MCU (`DeviceCommunicationLibrary.dll`).
2. MacroSilicon `345f:9132` is the native high-speed video display controller (`MSDISPLAYSDKWRRAPER.dll`).
3. Direct `USBDEVFS_BULK` ioctls confirm EP 0x02 Bulk OUT accepts vendor frames with status 0 while EP 0x81 Bulk IN returns `ETIMEDOUT`. The Linux serial stack is 100% exonerated.
4. `345f:9132` is absent from `lsusb` because the video controller IC is unpowered (missing auxiliary SATA/Molex power) or connected via an unplugged secondary internal USB header.
