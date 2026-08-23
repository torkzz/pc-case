# Comprehensive Protocol & Hardware Analysis Report

## Summary of Completed Protocol & Physical Evidence

1. **Protocol Opcode Exhaustion**:
   - 100% of all opcodes and generic frame response handlers in `DeviceCommunicationLibrary.dll` have been extracted and mapped:
     - `0x0080`: `HandshakeRequest` → expects `0x00C0`
     - `0x0072`: `GetHardwareInfoRequest` → expects `0x00B2`
     - `0x0062`: `GetFlashInfoRequest` / `ConnectDeviceRequest` → expects `0x00A2`
     - `0x0061`: `GetGifInfoRequest` → expects `0x00A1`
     - `0x0063`: `ExitRunningRequest` → fire-and-forget delivery via `SendFrameWithRetryAsync`
     - `0x0070`: `RestartRequest` → expects `0x00B0`
     - `0x0071`: `ChangeStatusRequest` → expects `0x00B1` (status bytes `0x10`, `0x11`, `0x20`)
     - `0x0085`: `GetDownloadStatusRequest` → expects `0x00C5`
     - `0x0081`: `RequestDownloadRequest` → expects `0x00C1`
     - `0x0082`: `DownloadDataRequest` → expects `0x00C2`
     - `0x008F`: `DownloadCompleteRequest` → expects `0x00CF`
     - `0x0090`: `RegisterOperationRequest` → expects `0x00D0` (`SetValueRegisterRequest`, `SetStringRegisterRequest`)

2. **Falsified Protocol Hypotheses**:
   - `DTR=0 / RTS=0 → Handshake` — Executed live, 0 RX bytes.
   - `ExitRunning (0x0063) → Handshake` — Executed live, 0x0063 acknowledged by USB SIE, 0 RX bytes on Handshake.
   - `ChangeStatus(STATUS_AHMI=0x20) → Handshake` — Executed live, 0 RX bytes.
   - `Linux CDC ACM Driver / TTY Stack Failure` — `usbmon` confirmed Bulk OUT transfers reach endpoint `0x02` with status 0, while endpoint `0x81` is continuously polled with Bulk IN URBs that complete with `-2` (ENOENT = host cancellation on port close).

3. **Physical Hardware Evidence**:
   - Cable: **Single USB-C cable only** attached directly to motherboard rear USB 3.x port.
   - Connectors: **No SATA power, no Molex power, no barrel plug, no secondary USB cable**.
   - Boot Behavior: LCD powers on via single USB-C connection, displays boot GIF, displays static image, then shuts down after an unknown elapsed time.
   - Auxiliary Power Hypothesis: **CONTRADICTED BY PHYSICAL EVIDENCE**.

4. **Key Unknown Question**:
   - What is the state of `33c3:f101` and `/dev/ttyACM0` at the exact moment the LCD display shuts down?
     - **CASE A**: Display shuts down, but `33c3:f101` / `/dev/ttyACM0` remains alive → Display application/controller lifecycle issue.
     - **CASE B**: Display shuts down and `33c3:f101` / `/dev/ttyACM0` disappears → Power/MCU reset/hardware shutdown.
     - **CASE C**: Display shuts down and `33c3:f101` re-enumerates → MCU watchdog / reboot loop.
