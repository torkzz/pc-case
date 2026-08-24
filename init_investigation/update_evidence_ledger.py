# Update VMAX_RUNTIME_EVIDENCE.md with exact evidence language and matrix results

content_vmax = """# VMAX Runtime Evidence Ledger

| Test / Claim | Input / Parameters | Expected | Actual Result | USB TX | USB RX | Application RX | Status | Evidence Level | Technical Interpretation |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **USB Enumeration** | Physical cable plug | Device `33c3:f101` active | Listed in `lsusb` | N/A | N/A | N/A | **PASS** | **STATIC_CONFIRMED** / **HOST_USB_CONFIRMED** | High-Speed USB 2.0 (480Mbps) device connected, CDC ACM profile. |
| **CDC Driver Binding** | Kernel `cdc_acm` | `/dev/ttyACM0` created | Node `/dev/ttyACM0` active | N/A | N/A | N/A | **PASS** | **HOST_USB_CONFIRMED** | Linux `cdc_acm` driver bound to Interface 0 (Control) & Interface 1 (Data). |
| **CDC Line Setup** | `0x21/0x20` 115200 8N1 | Control setup success | `ioctl` return 7B | Yes | Yes | N/A | **PASS** | **HOST_USB_CONFIRMED** | Line coding (115200 8N1) accepted by USB CDC stack. |
| **CDC Line Control** | `0x21/0x22` DTR+RTS | Control setup success | `ioctl` return 0B | Yes | Yes | N/A | **PASS** | **HOST_USB_CONFIRMED** | DTR and RTS control line state transfers asserted. |
| **Bulk OUT EP 0x02** | `41 48 00 02 00 80 00 00 4d 49` | 10B written | `usbmon` confirmed 10B URB submit/completion | Yes | No RX | N/A | **PASS** | **HOST_USB_CONFIRMED** | USB host-side transmission confirmed; MCU application-level reception/response not established. |
| **Handshake RX (CMD 0x0080)** | Handshake frame | 0x00C0 Response Frame | 0 bytes / Timeout | Yes | No | None | **UNKNOWN** | **DEVICE_RX_UNKNOWN** | MCU application-level reception/response not established. |
| **Hardware Info RX (CMD 0x0072)** | Hardware Info frame | 0x00B2 Response Frame | 0 bytes / Timeout | Yes | No | None | **UNKNOWN** | **DEVICE_RX_UNKNOWN** | MCU application-level reception/response not established. |
| **Flash Info RX (CMD 0x0062)** | Flash Info frame | 0x00A2 Response Frame | 0 bytes / Timeout | Yes | No | None | **UNKNOWN** | **DEVICE_RX_UNKNOWN** | MCU application-level reception/response not established. |
| **Exit Running RX (CMD 0x0063)** | Exit Running frame | 0x00A3 Response Frame | 0 bytes / Timeout | Yes | No | None | **UNKNOWN** | **DEVICE_RX_UNKNOWN** | MCU application-level reception/response not established. |
| **Restart RX (CMD 0x0070)** | Restart frame | 0x00B0 Response Frame | 0 bytes / Timeout | Yes | No | None | **UNKNOWN** | **DEVICE_RX_UNKNOWN** | MCU application-level reception/response not established. |
| **Change Status RX (CMD 0x0071)** | Change Status frame | 0x00B1 Response Frame | 0 bytes / Timeout | Yes | No | None | **UNKNOWN** | **DEVICE_RX_UNKNOWN** | MCU application-level reception/response not established. |

---

## Evidence Level Classifications
- **STATIC_CONFIRMED**: Proven by Mono/.NET IL disassembly of `DeviceCommunicationLibrary.dll` and `Vmax.exe`.
- **HOST_USB_CONFIRMED**: Proven by `lsusb -v`, `udevadm`, and kernel `usbmon1` URB submission and completion status `0`.
- **DEVICE_RX_CONFIRMED**: Proven when physical device returns application bytes (not yet achieved).
- **DEVICE_RX_UNKNOWN**: Host USB controller submitted 10-byte Bulk OUT transfer successfully; endpoint bulk IN / interrupt IN returned 0 bytes within timeout windows.
- **DEVICE_RESPONSE_CONFIRMED**: Proven when device returns valid `AH...MI` response frame matching expected response opcode.
- **HYPOTHESIS**: Unproven candidate root causes under investigation.

---

## Competing Hypotheses & Current Status

- **H1 (Undocumented init sequence required):** Investigated. IL disassembly of `DeviceCommunicator.cs` proves `Connect()` only executes standard `SerialPort.Open()` (115200 8N1). No vendor init packets exist prior to CMD 0x0080 or CMD 0x0062.
- **H2 (MCU not in application state / stuck in bootloader):** Viable. The MCU accepts USB High-Speed transfers at the USB hardware layer (SIE), but fails to service EP 0x81 IN requests at the application/firmware layer.
- **H3 (Linux CDC configuration discrepancy):** Disproven. Descriptors confirm standard CDC ACM IAD (`239/2/1`). USB control transfers (`SET_LINE_CODING`, `SET_CONTROL_LINE_STATE`) complete with status `0`.
- **H4 (Vendor DLL extra init logic):** Disproven. Chronological call graph of `DeviceCommunicator` shows `Connect()` executes `SerialPort.Open()`, followed immediately by `HandshakeAsync` (CMD `0x0080`) or `ConnectDeviceAsync` (CMD `0x0062`).
- **H5 (Different Endpoint / Interface):** Disproven by descriptor audit. Descriptor proves Interface 0 has EP 0x83 (Interrupt IN 8B) and Interface 1 has EP 0x02 (Bulk OUT 512B) and EP 0x81 (Bulk IN 512B). `usbmon1` monitoring on both EP 0x81 and EP 0x83 showed 0 URBs returned.
- **H6 (DTR/RTS line signaling state machine requirements):** Evaluated. Tested full matrix of DTR/RTS states, pulses (10ms, 100ms, 500ms, 1s, 3s), and settle delays. All combinations produced USB host-side TX confirmation but 0 RX bytes.
- **H7 (Frame parser discarding bytes):** Disproven. IL inspection of `ProcessReceiveBuffer` and `ProcessCompleteFrame` proves `OnDataReceived` fires BEFORE frame parsing or pending request dictionary checks. Zero bytes were delivered to the OS serial driver buffer.
- **H8 (Hardware / Firmware failure or freeze):** Viable hypothesis. Physical MCU USB peripheral controller remains active (negotiating High-Speed 480Mbps), but inner core / UART interface to LCD screen controller is unresponsive.
- **H9 (Secondary control MCU / MacroSilicon USB Display):** Artifact discovery. Bundle contains `MSUSBDisplay.inf` for `345f:9132` (MacroSilicon USB display adapter) and `33c3:f101` (HL VMAX CDC ACM serial controller). The physical case screen uses `33c3:f101` for telemetry data injection.
"""

with open("/home/tor/pc-case-lcd/VMAX_RUNTIME_EVIDENCE.md", "w") as f:
    f.write(content_vmax)

print("Updated /home/tor/pc-case-lcd/VMAX_RUNTIME_EVIDENCE.md")
