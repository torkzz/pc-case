# Device Initialization Call Graph & Chronological Trace

## Overview
Reconstructed chronological sequence from IL disassembly of `DeviceCommunicationLibrary.dll` and `Vmax.exe`.

## Chronological Call Graph

```
Application Startup (Vmax.exe)
  │
  ├── 1. DeviceCommunicator Constructor (.ctor)
  │     ├── Instantiates _serialPort = new SerialPort()
  │     ├── Instantiates _receiveBuffer = new byte[0]
  │     ├── Instantiates _pendingRequests ConcurrentDictionary<ushort, TaskCompletionSource<BaseFrame>>
  │     └── Registers SerialPort.DataReceived += OnSerialDataReceived
  │
  ├── 2. Connect(portName, baudRate = 115200)
  │     ├── Checks _serialPort.IsOpen -> disconnects if open
  │     ├── Sets _serialPort.PortName = portName
  │     ├── Sets _serialPort.BaudRate = 115200
  │     ├── Sets Parity.None, DataBits=8, StopBits.One
  │     └── Calls _serialPort.Open()
  │
  └── 3. Command Transmission
        ├── HandshakeAsync(timeoutMs = 5000)
        │     └── SendRequestAsync<HandshakeResponse>(HandshakeRequest [CMD 0x0080])
        │           ├── CalculateContentLength() -> CTRL = 0x0002
        │           ├── BuildFrame() -> 41 48 00 02 00 80 00 00 4D 49
        │           ├── _serialPort.Write(frameBytes)
        │           └── Awaits TaskCompletionSource registered under response opcode 0x00C0
        │
        └── ConnectDeviceAsync(timeoutMs = 5000)
              └── SendRequestAsync<GetFlashInfoResponse>(GetFlashInfoRequest [CMD 0x0062])
                    ├── BuildFrame() -> 41 48 00 02 00 62 00 00 4D 49
                    └── Awaits TaskCompletionSource registered under response opcode 0x00A2
```

## Critical Verification
- **What happens before CMD 0x0080?**
  Only `SerialPort.Open()` setting 115200 8N1! There are NO hidden vendor commands, NO secret control transfers, and NO prior handshake packets executed inside `Connect()`.
- **Is `ConnectDeviceAsync` a separate command?**
  Yes. `ConnectDeviceAsync` sends `GetFlashInfoRequest` (CMD `0x0062`), whereas `HandshakeAsync` sends `HandshakeRequest` (CMD `0x0080`).
