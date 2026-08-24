import re

il_path = "/home/tor/pc-case-lcd/DeviceCommunicationLibrary.il"
with open(il_path, "r", encoding="utf-8", errors="ignore") as f:
    text = f.read()

md_out = "/home/tor/pc-case-lcd/device_communicator_callgraph.md"

doc = """# DeviceCommunicator Call Graph & Method Audit

| Method | Opcode | Expected Response | Timeout | Payload Structure |
| :--- | :--- | :--- | :--- | :--- |
| `Connect(port, baud)` | N/A | N/A | N/A | `SerialPort.ctor(port, baud, Parity.None, 8, StopBits.One)`, registers `DataReceived` & `ErrorReceived`, calls `Open()` |
| `HandshakeAsync()` | `0x0080` | `0x00C0` | 3000ms | Empty content -> `AH 00 02 00 80 00 00 MI` (CTRL = 0x0002) |
| `GetHardwareInfoAsync()` | `0x0072` | `0x00B2` | 3000ms | Empty content -> `AH 00 02 00 72 00 00 MI` |
| `GetFlashInfoAsync()` | `0x0062` | `0x00A2` | 3000ms | Empty content -> `AH 00 02 00 62 00 00 MI` |
| `GetGifInfoAsync()` | `0x0061` | `0x00A1` | 3000ms | Empty content -> `AH 00 02 00 61 00 00 MI` |
| `GetDownloadStatusAsync()`| `0x0085` | `0x00C5` | 3000ms | Empty content -> `AH 00 02 00 85 00 00 MI` |
| `RequestDownloadAsync()` | `0x0081` | `0x00C1` | 3000ms | `Address` (4B BE uint32) + `FileSize` (4B BE uint32) + `FileId` (N bytes) |
| `DownloadDataAsync()` | `0x0082` | `0x00C2` | 3000ms | `Offset` (4B BE uint32) + `Data` (N bytes JPEG chunk) |
| `DownloadCompleteAsync()` | `0x008F` | `0x00CF` | 3000ms | Empty content |
| `ChangeStatusAsync()` | `0x0071` | `0x00B1` | 3000ms | `Status` (1B byte) |
| `RestartAsync()` | `0x0070` | `0x00B0` | 3000ms | Empty content |
| `ExitRunningAsync()` | `0x0063` | None | N/A | Empty content |

## Receive & Parsing Architecture

```text
SerialPort.DataReceived Event
       ↓
SerialPort_DataReceived(sender, e)
       ├── Checks: SerialPort.BytesToRead > 0
       ├── Allocates: byte[BytesToRead]
       ├── Reads: SerialPort.Read(buffer, 0, count)
       └── Calls: ProcessReceivedData(newData, bytesRead)
               ↓
ProcessReceivedData(newData, bytesRead)
       ├── Appends newData to _receiveBuffer
       └── Calls: ProcessReceiveBuffer()
               ↓
ProcessReceiveBuffer()
       ├── Finds: FindFrameStart(_receiveBuffer) -> Look for 'A' 'H' (0x41 0x48)
       ├── Finds: FindFrameEnd(_receiveBuffer, startIdx) -> Look for 'M' 'I' (0x4D 0x49)
       └── Extracts: frameData -> Calls Task.Run(() => ProcessCompleteFrame(frameData))
               ↓
ProcessCompleteFrame(frameData)
       ├── Extracts: CMD = ExtractCmdFromBytes(frameData) (bytes 4..5)
       ├── Resolves: TaskCompletionSource from _pendingRequests[CMD]
       └── Sets: TaskCompletionSource.SetResult(parsedFrame)
```
"""

with open(md_out, "w") as f:
    f.write(doc)

print("Generated " + md_out)
