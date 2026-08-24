evidence_md = """# Evidence Ledger & Protocol Specification

## Evidence Level Classifications
- **STATIC_CONFIRMED**: Proven by disassembly of `DeviceCommunicationLibrary.dll`, `Vmax.exe`, and `MSDISPLAYSDKWRRAPER.dll`.
- **HOST_USB_CONFIRMED**: Proven by `lsusb -v`, `udevadm`, and kernel `usbmon1` URB submission and completion status 0.
- **DEVICE_RX_UNKNOWN**: Host USB controller submitted 10-byte Bulk OUT transfer successfully; endpoint bulk IN / interrupt IN returned 0 bytes within timeout windows.
- **DEVICE_RESPONSE_NOT_OBSERVED**: No application-level response frame received from device.
- **HYPOTHESIS**: Unproven candidate root cause.

## Dual Engine Architecture Evidence

| Component | VID:PID | Driver | Managed / Native Assembly | Purpose | Evidence Level |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **HL VMAX Controller** | `33c3:f101` | CDC ACM (`cdc_acm`) | `DeviceCommunicationLibrary.dll` | Telemetry, assets, status MCU | **STATIC_CONFIRMED** / **HOST_USB_CONFIRMED** |
| **MacroSilicon Display** | `345f:9132` | `MSUSBDisplay.inf` | `MSDISPLAYSDKWRRAPER.dll` | Real-time desktop video display IC | **STATIC_CONFIRMED** |

## Runtime Status of `33c3:f101`
- **HOST USB TX**: **HOST_USB_CONFIRMED** (10-byte frame `41 48 00 02 00 80 00 00 4D 49` sent on EP 0x02, status 0).
- **DEVICE RX**: **DEVICE_RX_UNKNOWN** (Host submission confirmed; physical MCU application-level reception not established).
- **DEVICE RESPONSE**: **DEVICE_RESPONSE_NOT_OBSERVED** (0 bytes returned on EP 0x81 / EP 0x83).
"""

with open("/home/tor/pc-case-lcd/EVIDENCE.md", "w") as f:
    f.write(evidence_md)

print("Updated /home/tor/pc-case-lcd/EVIDENCE.md")
