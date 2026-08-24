# Receive Path & Serial Driver Analysis Report

## Overview
Analysis of the receive path implementation in `DeviceCommunicationLibrary.dll` (`DeviceCommunicator.cs`).

## Detailed Classification Matrix

| Subsystem / Operation | Implementation Detail | Classification | Technical Description |
| :--- | :--- | :--- | :--- |
| **Port Opening** | `_serialPort.Open()` | **CONFIRMED STATIC** | Opens serial device node (`/dev/ttyACM0` on Linux, `COMx` on Windows). |
| **Line Signaling** | `DtrEnable` / `RtsEnable` | **CONFIRMED STATIC** | Neither `DtrEnable` nor `RtsEnable` is set in `Connect()`. Defaults to `false`. |
| **Baud Rate / Line Coding** | `115200 8N1` | **CONFIRMED STATIC** | Configured as `115200`, `Parity.None`, `DataBits=8`, `StopBits.One`, `Handshake.None`. |
| **Read / Write Timeouts** | Default (-1) | **CONFIRMED STATIC** | Handled asynchronously via `TaskCompletionSource` with CancellationTokenSource timeout. |
| **Event Registration** | `SerialPort.DataReceived` | **CONFIRMED STATIC** | Handler `SerialPort_DataReceived` reads available bytes into `_receiveBuffer`. |
| **Frame Delimiting** | `AH...MI` (`41 48 ... 4D 49`) | **CONFIRMED STATIC** | `FindFrameStart` searches for `0x41 0x48`, `FindFrameEnd` searches for `0x4D 0x49`. |
| **Event Dispatch Order** | `OnDataReceived` first | **CONFIRMED STATIC** | `OnDataReceived(frameData)` fires BEFORE pending dictionary checks or CRC validation. |
| **Mono vs .NET Serial** | Linux `termios` vs Windows `COM` | **CONFIRMED LIVE** | Mono maps `SerialPort` to Linux termios. CDC ACM control transfers (`0x21/0x20`, `0x21/0x22`) succeed on Linux. |
| **Application RX Result** | 0 Bytes Returned | **CONFIRMED LIVE** | Serial driver buffer returned 0 bytes within 2.0s–5.0s timeout windows. Zero bytes were delivered by USB endpoint. |

---

## Receive Path Execution Graph

```
Serial Line (USB Bulk IN EP 0x81)
  │
  ├── 1. Linux Kernel cdc_acm Driver
  │     └── Buffer populated in OS tty ring buffer (/dev/ttyACM0)
  │
  ├── 2. Mono System.IO.Ports.SerialPort
  │     └── SerialPort_DataReceived event fired
  │
  ├── 3. DeviceCommunicator._receiveBuffer
  │     └── Bytes copied into byte array _receiveBuffer
  │
  ├── 4. ProcessReceiveBuffer()
  │     ├── FindFrameStart() -> locates 'A' 'H' (0x41 0x48)
  │     ├── FindFrameEnd() -> locates 'M' 'I' (0x4D 0x49)
  │     └── Extract frameData bytes
  │
  ├── 5. OnDataReceived(frameData)  <-- FIRES FIRST (DataReceived Event)
  │
  └── 6. ProcessCompleteFrame(frameData)
        ├── ExtractCmdFromBytes(frameData)
        ├── ConcurrentDictionary.TryRemove(cmd, out tcs)
        └── ProcessResponseFrame(...) -> tcs.TrySetResult(responseFrame)
```
