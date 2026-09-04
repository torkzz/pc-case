# Next Breakthrough Report — HL VMAX & MacroSilicon Investigation

## 1. What do we KNOW?
- **Device Identity**: `33c3:f101` is a High-Speed (480Mbps) USB 2.0 IAD CDC ACM device bound to `/dev/ttyACM0`.
- **Vendor Architecture**: `Vmax.exe` contains **two separate display engines**:
  - `AICDisp` (`DeviceCommunicationLibrary.dll`) $\rightarrow$ Serial CDC telemetry/asset MCU (`33c3:f101`).
  - `MSDisplay` (`MSDISPLAYSDKWRRAPER.dll`) $\rightarrow$ Native MacroSilicon USB video display driver (`345f:9132`).
- **Protocol & Opcode Definitions**: Frame structure `41 48 [LEN] [CMD] [PAYLOAD] [CRC] 4D 49` (`AH...MI`). Response opcodes follow `ResponseCmd = RequestCmd | 0x40`.
- **Receive Path Design**: `OnDataReceived` fires BEFORE frame parsing or pending dictionary lookups. 0 bytes RX is true zero delivered from USB endpoint, not parser discard.

## 2. What have we PROVEN on the physical device?
- **Host USB TX Confirmed (`WIRE_TX_CONFIRMED`)**: Host USB controller submits 10-byte frames to EP 0x02 Bulk OUT with kernel completion status `0`.
- **CDC Control Transfers Confirmed**: `SET_LINE_CODING` (115200 8N1) and `SET_CONTROL_LINE_STATE` (DTR+RTS) complete with status `0`.
- **Systematic Command Matrix (A–L)**: Executing all 12 matrix test sequences across varied DTR/RTS states, settling delays (0–1s), and command chains (`0x0070`, `0x0071`, `0x0072`, `0x0080`, `0x0085`) produces 0 bytes RX on EP 0x81 Bulk IN and EP 0x83 Interrupt IN.

## 3. What remains UNKNOWN?
- Whether MCU `33c3:f101` is executing application firmware or stuck in internal standby/bootloader mode.
- Whether the MacroSilicon display controller (`345f:9132`) resides on a secondary motherboard USB 9-pin header or unpowered internal USB hub port.

## 4. What hypotheses have been eliminated?
- **ELIMINATED**: Frame format / CRC mismatch on host side (verified static & live against vendor DLL).
- **ELIMINATED**: Host-side USB transport failure or cdc_acm driver mismatch (usbmon confirms EP 0x02 completion).
- **ELIMINATED**: Mono runtime serial incompatibility (Mono termios implementation generates compliant CDC transfers).
- **ELIMINATED**: Receive parser byte discard (`OnDataReceived` fires before parsing).

## 5. What hypotheses remain?
- **Hypothesis 1 (External Board Power Missing)**: MCU `33c3:f101` requires auxiliary SATA/Molex 5V/12V power rail attached to the PC-case LCD PCB to execute inner application firmware.
- **Hypothesis 2 (Secondary USB Header for Video)**: Real-time video display controller (`345f:9132`) is on a separate internal 9-pin USB header currently unplugged.
- **Hypothesis 3 (MCU in Bootloader/Standby)**: MCU `33c3:f101` is held in bootloader mode awaiting a hardware pulse.

## 6. What is the strongest next experiment?
Physical PCB inspection of the PC-case LCD module to check for a secondary internal USB connector / SATA power connection, or probing board power rails.

## 7. What exact command/script should be run next?
Perform physical PCB/wiring inspection, then run `python3 /home/tor/pc-case-lcd/vmax_command_matrix.py` while verifying SATA power connection.

## 8. What result would constitute a breakthrough?
Receiving $\ge 1$ byte of application RX data on EP 0x81 Bulk IN or EP 0x83 Interrupt IN, OR observing `345f:9132` enumerate on `lsusb`.

## 9. What result would falsify the current hypothesis?
Finding that the PC-case LCD PCB has no MacroSilicon IC and no secondary USB header, proving `33c3:f101` must handle both telemetry AND video transport.
