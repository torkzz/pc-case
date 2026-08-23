# Vendor Application Startup & Command Sequence Analysis

## Overview
Analysis derived from disassembly of `DeviceCommunicationLibrary.dll`, `Vmax.exe`, and static IL structure.

## Confirmed Protocol Call Graph

```
DeviceCommunicator Constructor
    ├── Initializes locks (_serialLock, _bufferLock, _eventLock)
    ├── Initializes receive buffer (_receiveBuffer = byte[0])
    └── Initializes _pendingRequests (ConcurrentDictionary<uint16, TaskCompletionSource>)

DeviceCommunicator.Connect(portName, baudRate = 115200)
    ├── Disconnects existing connection if _serialPort.IsOpen
    ├── Creates new SerialPort(portName, 115200, Parity.None, 8, StopBits.One)
    ├── Adds SerialPort_DataReceived handler
    ├── Adds SerialPort_ErrorReceived handler
    └── Calls SerialPort.Open()  [No DTR/RTS set; defaults to DTR=0, RTS=0 on Windows]

DeviceCommunicator Initialization Sequence (Standard Application Flow)
    ├── 1. HandshakeAsync(timeoutMs)
    │     ├── Constructs HandshakeRequest [CMD = 0x0080, Content = []]
    │     ├── Frame: 41 48 00 02 00 80 00 00 4D 49  (10 bytes)
    │     ├── Calls SendRequestAsync<HandshakeResponse>(frame, timeoutMs)
    │     └── Awaits HandshakeResponse [CMD = 0x00C0, MaxPackageSize: uint32]
    │
    ├── 2. GetHardwareInfoAsync(timeoutMs)
    │     ├── Constructs GetHardwareInfoRequest [CMD = 0x0072, Content = []]
    │     ├── Frame: 41 48 00 02 00 72 00 00 4D 49  (10 bytes)
    │     ├── Calls SendRequestAsync<GetHardwareInfoResponse>(frame, timeoutMs)
    │     └── Awaits GetHardwareInfoResponse [CMD = 0x00B2: IcId, MaxAcfSize, Height, Width, ProductId]
    │
    └── 3. ChangeStatusAsync(status, timeoutMs) [Optional State Transition]
          ├── Constructs ChangeStatusRequest [CMD = 0x0071, Content = [status]]
          ├── Frame (11 bytes): 41 48 00 03 00 71 [STATUS] 00 00 4D 49
          │     - STATUS_DOWNLOAD_READY = 0x10
          │     - STATUS_DOWNLOADING    = 0x11
          │     - STATUS_AHMI           = 0x20
          ├── Calls SendRequestAsync<ChangeStatusResponse>(frame, timeoutMs)
          └── Awaits ChangeStatusResponse [CMD = 0x00B1]

Fire-and-Forget / Special Cleanup Commands
    └── ExitRunningAsync(maxRetries=3, intervalMs=1000)
          ├── Constructs ExitRunningRequest [CMD = 0x0063, Content = []]
          ├── Frame: 41 48 00 02 00 63 00 00 4D 49  (10 bytes)
          ├── Calls SendFrameWithRetryAsync(frame, 3, 1000)  [Returns Task<bool> delivery success]
          └── Does NOT await a protocol response frame
