# Device State Machine — HL VMAX 33c3:f101

Based on IL reverse engineering of DeviceCommunicationLibrary.dll and Vmax.exe.

```
USB ENUMERATION (host-driven, automatic)
    ↓
    OS: SET_CONFIGURATION(1)
    OS: SET_LINE_CODING(115200, 8N1)
    OS: SET_CONTROL_LINE_STATE(DTR=0, RTS=0)  ← Windows default via SerialPort
    [Linux may assert DTR=1 by default — POSSIBLE DISCREPANCY]
    ↓
TRANSPORT READY
    /dev/ttyACM0 appears (Linux) / COMx appears (Windows)
    ↓
APPLICATION LAYER OPEN
    DeviceCommunicator.Connect(portName, 115200)
    → SerialPort.Open()
    → No delay, no flush, no DTR/RTS change
    ↓
HANDSHAKE [CONFIRMED FIRST COMMAND]
    DeviceCommunicator.HandshakeAsync()
    → CMD: 0x0080 (HandshakeRequest)
    → Wire: 41 48 00 02 00 80 00 00 4D 49
    → Awaits response CMD: 0x00C0
    → Response carries: MaxPackageSize (uint32)
    ↓
HARDWARE INFO [CONFIRMED SECOND COMMAND]
    DeviceCommunicator.GetHardwareInfoAsync()
    → CMD: 0x0072 (GetHardwareInfoRequest)
    → Wire: 41 48 00 02 00 72 00 00 4D 49
    → Awaits response CMD: 0x00B2
    → Response carries: IcId, MaxAcfSize, DisplayHeight, DisplayWidth, ProductId
    ↓
DEVICE CONNECTED STATE
    Application knows: MaxPackageSize, display dimensions, IC identifier
    ↓
APPLICATION PROTOCOL
    ┌─────────────────────────────────────────────────────────────┐
    │ GetFlashInfoAsync / ConnectDeviceAsync   CMD 0x0062         │
    │ GetGifInfoAsync                          CMD 0x0061         │
    │ GetDownloadStatusAsync                   CMD 0x0085         │
    │ RequestDownloadAsync(addr, size, fileId) CMD UNKNOWN        │
    │ DownloadDataAsync(offset, data)          CMD UNKNOWN        │
    │ DownloadCompleteAsync()                  CMD 0x008F         │
    │ ChangeStatusAsync(status)               CMD UNKNOWN         │
    │ SetValueRegisterAsync(id, val)          CMD 0x0090          │
    │ SetStringRegisterAsync(id, str)         CMD 0x0090          │
    │ RestartAsync()                          CMD 0x0070          │
    │ ExitRunningAsync()                      CMD 0x0063 (no ACK) │
    └─────────────────────────────────────────────────────────────┘
    ↓
DISCONNECT
    DeviceCommunicator.Disconnect()
    → SerialPort.Close() + Dispose()
    → CancelAllPendingRequests()
```

## State Transitions with Evidence Quality

| State Transition        | Operation                              | Evidence         |
|------------------------|----------------------------------------|-----------------|
| Enumeration → Ready     | OS CDC ACM setup                       | CONFIRMED        |
| Ready → HandshakeSent   | CMD 0x0080 via SerialPort.Write        | CONFIRMED        |
| HandshakeSent → HwInfo  | Await 0x00C0, then CMD 0x0072          | CONFIRMED        |
| HwInfo → AppProtocol    | Await 0x00B2                           | CONFIRMED        |
| AppProtocol ordering    | Caller-dependent                        | UNKNOWN          |
| ExitRunning behavior    | Fire-and-forget (3 retries, 1s apart)  | CONFIRMED        |

## Unknown Transitions

1. Whether `ConnectDeviceAsync` (CMD 0x0062) must be called before any image operation — UNKNOWN from IL (caller sequence not in DeviceCommunicationLibrary itself)
2. Whether `ExitRunning` (CMD 0x0063) is needed to take device out of a running state before Handshake — POSSIBLE
3. What the device state is at power-on — UNKNOWN
4. Whether the device sends unsolicited data on EP 0x81 at any point — UNKNOWN (never observed)
