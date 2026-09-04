# Update ledgers and generate VMAX_LINUX_ONLY_NEXT_PHASE.md

next_phase_text = """# VMAX Linux-Only Reverse Engineering & Next Phase Investigation Report

## 1. Confirmed Facts
- **Physical USB Device**: `33c3:f101` enumerates as High-Speed (480Mbps) USB 2.0 IAD CDC ACM (`239/2/1`). Node `/dev/ttyACM0` created by Linux `cdc_acm` driver.
- **Dual Engine Architecture**: `Vmax.exe` contains **two distinct display/communication stacks**:
  1. `AICDisp` (`DeviceCommunicationLibrary.dll`) $\rightarrow$ Serial CDC telemetry/asset MCU (`33c3:f101` at `/dev/ttyACM0`).
  2. `MSDisplay` (`MSDISPLAYSDKWRRAPER.dll`) $\rightarrow$ Native MacroSilicon USB video display driver (`345f:9132`, `345f:9133`, `345f:374a`, `345f:a101`).
- **USB Host OUT Transmission**: Kernel `usbmon1` and raw `usbfs` ioctls confirm 10-byte frame `41 48 00 02 00 80 00 00 4D 49` is submitted to EP 0x02 Bulk OUT with kernel completion status `0` (`WIRE_TX_CONFIRMED`).
- **CDC Control Transfers**: CDC `SET_LINE_CODING` (115200 8N1) and `SET_CONTROL_LINE_STATE` (DTR+RTS) complete with status `0`.
- **Receive Path Execution**: `OnDataReceived` fires BEFORE frame parsing or pending dictionary lookups. 0 bytes RX is true zero delivered from physical USB endpoint, not parser discard.

## 2. Failed / Eliminated Hypotheses
- **ELIMINATED**: Frame format or CRC mismatch on host side (official vendor frames verified static & live).
- **ELIMINATED**: Host-side USB transport failure or kernel cdc_acm driver mismatch (raw `usbfs` ioctls directly on `/dev/bus/usb/001/002` exhibit identical completion 0 on EP 0x02 and timeout on EP 0x81).
- **ELIMINATED**: Mono runtime serial incompatibility (Mono termios implementation generates compliant CDC control/bulk transfers).
- **ELIMINATED**: Receive parser byte discard (`OnDataReceived` fires before parsing).

## 3. Unresolved Questions
- Is the physical MCU core on `33c3:f101` executing application firmware, or is it unpowered / held in reset until auxiliary power (e.g. SATA/Molex connector) is attached to the PC-case LCD PCB?
- Is the MacroSilicon `345f:9132` display controller located on a secondary internal motherboard USB 9-pin header / unpowered USB hub port currently disconnected?

## 4. USB Initialization Sequence
`Vmax.exe` startup sequence:
1. `DeviceCommunicator.Connect("/dev/ttyACM0", 115200)`
2. `HandshakeAsync` (CMD `0x0080`) sent to `33c3:f101`
3. `GetHardwareInfoAsync` (CMD `0x0072`) sent to `33c3:f101`
4. `Wrraper_MSDisplayGetDeviceList()` called to detect MacroSilicon `345f:9132`
5. If MacroSilicon device detected, call `Wrraper_MSDisplayStart()` & `Wrraper_MSDisplaySendPicture()`

## 5. CDC Behavior
Linux `cdc_acm` driver successfully binds Interface 0 (Control) and Interface 1 (Data). Standard `SET_LINE_CODING` (115200 8N1) and `SET_CONTROL_LINE_STATE` (DTR+RTS) requests complete with status `0`.

## 6. Raw Endpoint Behavior (`usbfs` Direct Ioctls)
- `EP 0x02 Bulk OUT`: Transfers 10 bytes with status `0` (`10 bytes written`).
- `EP 0x81 Bulk IN`: `ioctl(USBDEVFS_BULK)` returns `-1` (errno 110: `Connection timed out`).
- `EP 0x83 Interrupt IN`: Returns 0 bytes.

## 7. CRC Findings
`CalculateCRC()` in `BaseFrame` returns constant `0` (`0x0000`). CRC bit (bit 15 of `CTRL`) is 0 by default. Testing both Frame A (CRC bit 0, 10B) and Frame B (CRC bit 1, 12B) produced identical USB OUT success and Bulk IN timeout.

## 8. Receive Parser Findings
`ProcessReceiveBuffer()` scans for `AH` (`0x41 0x48`) and `MI` (`0x4D 0x49`). `OnDataReceived` fires BEFORE frame parsing or pending dictionary lookups. Zero bytes delivered is confirmed true zero from physical endpoint.

## 9. Command Matrix Findings
Executed all 12 systematic matrix sequences (A–L) with varied DTR/RTS states, settling delays (0–1s), and command chains (`0x0070`, `0x0071`, `0x0072`, `0x0080`, `0x0085`). All 12 sequences produced 0 bytes RX on EP 0x81 Bulk IN and EP 0x83 Interrupt IN.

## 10. Architecture Mapping

```
Application UI (Vmax.exe)
  │
  ├── Stack A: Telemetry / Asset Engine (33c3:f101)
  │     └── DeviceCommunicationLibrary.dll -> Serial CDC (/dev/ttyACM0)
  │           └── Commands: Handshake (0x0080), HardwareInfo (0x0072), DownloadData (0x0082)
  │
  └── Stack B: Real-Time Desktop Video Engine (345f:9132)
        └── MSDISPLAYSDKWRRAPER.dll -> TurboJPEG -> libusb0 -> MacroSilicon Display IC
              └── Functions: Wrraper_MSDisplayGetDeviceList, Wrraper_MSDisplaySendPicture
```

## 11. Next Highest-Value Experiment
Physical inspection of the PC-case LCD module PCB and internal wiring to locate the secondary MacroSilicon USB header / SATA power connection, or direct logic analyzer/oscilloscope probing of the MCU UART pins.
"""

with open("/home/tor/pc-case-lcd/VMAX_LINUX_ONLY_NEXT_PHASE.md", "w") as f:
    f.write(next_phase_text)

print("Generated /home/tor/pc-case-lcd/VMAX_LINUX_ONLY_NEXT_PHASE.md")
