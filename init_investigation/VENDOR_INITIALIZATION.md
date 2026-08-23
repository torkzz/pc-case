# Vendor Initialization Path — Complete IL Analysis

## Summary

The vendor software (`DeviceCommunicationLibrary.dll`) uses **pure CDC ACM serial** via `System.IO.Ports.SerialPort`. Zero USB control transfers are issued by the application layer. The OS CDC driver handles all enumeration-level control transfers automatically.

## Frame Format (CONFIRMED from `BaseFrame.ToBytes()`)

```
Byte 0:   0x41 ('A')         — SOF[0]
Byte 1:   0x48 ('H')         — SOF[1]
Byte 2:   CTRL >> 8          — length high
Byte 3:   CTRL & 0xFF        — length low
Byte 4:   CMD >> 8           — command high
Byte 5:   CMD & 0xFF         — command low
Bytes 6…N: Content[]         — payload (may be empty)
Byte N+1: CRC >> 8           — always 0x00 (CRC disabled)
Byte N+2: CRC & 0xFF         — always 0x00 (CRC disabled)
Byte N+3: 0x4D ('M')         — EOF[0]
Byte N+4: 0x49 ('I')         — EOF[1]
```

**CTRL = 2 + Content.Length** (from `CalculateContentLength`: returns `2 + (content?.Length ?? 0)`)

Minimum frame length for parser: **10 bytes** (checked at `Parse()` line 522: `bge 0x0a`)

## Serial Port Configuration (CONFIRMED)

```
Constructor: SerialPort(portName, baudRate, Parity.None=0, 8, StopBits.One=1)
Default baudRate: 0x0001c200 = 115200 bps
Data bits: 8
Parity: None (0)
Stop bits: 1
DTR: NOT SET by Connect() — SerialPort default is false
RTS: NOT SET by Connect() — SerialPort default is false
ReadTimeout: NOT SET — SerialPort default is -1 (infinite)
WriteTimeout: NOT SET — SerialPort default is -1 (infinite)
ReceivedBytesThreshold: NOT SET — SerialPort default is 1
Handshake: NOT SET — SerialPort default is None
Flush before first command: NONE
Delay after Open(): NONE
Delay before first command: NONE
DiscardInBuffer: NONE
DiscardOutBuffer: NONE
```

## Vendor Initialization Sequence (CONFIRMED)

```
Step 1: DeviceCommunicator.Connect(portName, 115200)
    - new SerialPort(portName, 115200, Parity.None, 8, StopBits.One)
    - port.add_DataReceived(SerialPort_DataReceived)
    - port.add_ErrorReceived(SerialPort_ErrorReceived)
    - port.Open()
    ← returns bool (true=success)
    ← NO DTR/RTS, NO delay, NO flush, NO control transfer

Step 2: DeviceCommunicator.HandshakeAsync(timeoutMs)
    - Constructs: HandshakeRequest  [CMD=0x0080, Content=[]]
    - Sends via SendFrame → SerialPort.Write()
    - Frame bytes: 41 48 00 02 00 80 00 00 4D 49
    - Awaits response CMD 0x00C0
    ← returns Task<HandshakeResponse> (contains MaxPackageSize field)

Step 3: DeviceCommunicator.GetHardwareInfoAsync(timeoutMs)
    - Constructs: GetHardwareInfoRequest  [CMD=0x0072, Content=[]]
    - Sends via SendFrame → SerialPort.Write()
    - Frame bytes: 41 48 00 02 00 72 00 00 4D 49
    - Awaits response CMD 0x00B2
    ← returns Task<GetHardwareInfoResponse> (IcId, MaxAcfSize, DisplayHeight, DisplayWidth, ProductId)
```

## Complete Opcode Table (CONFIRMED from IL constructors)

| Request Class              | CMD (hex) | CMD (dec) | Response CMD | Content        |
|---------------------------|-----------|-----------|--------------|----------------|
| HandshakeRequest          | 0x0080    | 128       | 0x00C0 (192) | empty []       |
| GetHardwareInfoRequest    | 0x0072    | 114       | 0x00B2 (178) | empty []       |
| ConnectDeviceRequest      | 0x0062    | 98        | 0x00A2 (162) | empty []       |
| GetFlashInfoRequest       | 0x0062    | 98        | 0x00A2 (162) | empty []       |
| GetGifInfoRequest         | 0x0061    | 97        | 0x00A1 (161) | empty []       |
| ExitRunningRequest        | 0x0063    | 99        | 0x00A2 (162) | empty []       |
| RestartRequest            | 0x0070    | 112       | 0x00B0 (176) | empty []       |
| DownloadCompleteRequest   | 0x008F    | 143       | 0x00CF (207) | empty []       |
| GetDownloadStatusRequest  | 0x0085    | 133       | 0x00C5 (197) | empty []       |
| ChangeStatusRequest       | 0x0071    | 113       | 0x00B1 (177) | [1 byte: status] |
| RegisterOperationRequest  | 0x0090    | 144       | 0x00D0 (208) | register data  |

**Note:** ConnectDeviceRequest and GetFlashInfoRequest share CMD 0x0062 — they are the same wire command. ConnectDeviceAsync awaits GetFlashInfoResponse.

RequestDownloadRequest uses CMD 0x0081. Content = Addr(uint32, BE) + FileSize(uint32, BE) + FileId(byte[16]).

ChangeStatusRequest uses CMD 0x0071. Content = 1 byte. Known STATUS values from ProtocolConstants:
- `STATUS_DOWNLOAD_READY = 0x10`
- `STATUS_DOWNLOADING    = 0x11`
- `STATUS_AHMI           = 0x20`

## ExitRunningAsync Special Case

`ExitRunningAsync` uses `SendFrameWithRetryAsync(frame, maxRetries=3, intervalMs=1000)` NOT `SendRequestAsync`.

- `SendFrameWithRetryAsync` returns `Task<bool>` — the caller DOES await it.
- But it only retries delivery (SerialPort.Write success), NOT waiting for a response frame.
- Retry loop: for i in 0..maxRetries: if SendFrame() returns true → return true; else await Task.Delay(1000ms)
- The bool result is whether the frame was successfully written to the serial port, NOT whether the device acknowledged it.
- ExitRunning is fire-and-forget at the protocol level: no response CMD is expected, no TCS is created.
- The GetExpectedResponseCmd table shows 0x63 → 0xA2 but that mapping is never exercised by ExitRunningAsync.

**STATUS_AHMI implication:** `ChangeStatus(STATUS_AHMI=0x20)` may be required to put the display into UI-rendering mode before download commands. This is called from Vmax.exe but the call site ordering is obfuscated.

## USB Control Transfers

**NONE.** The vendor IL contains zero references to any USB control transfer API. Transport is exclusively `System.IO.Ports.SerialPort`. All CDC ACM control transfers (SET_LINE_CODING, SET_CONTROL_LINE_STATE) are issued by the Windows `usbser.sys` driver automatically when `SerialPort.Open()` is called. The application has no visibility into or control over these transfers.

## No-DTR/RTS Confirmation

The `Connect()` method does not set `DtrEnable` or `RtsEnable` on the `SerialPort` instance. On Windows, `System.IO.Ports.SerialPort` defaults both to `false`. On Linux, `cdc_acm` / `termios` default depends on O_NOCTTY, but typically DTR is asserted on open by the TTY layer unless suppressed with `TIOCM_DTR`.

**This is the key discrepancy.** When Python/C code opens `/dev/ttyACM0` without `TIOCM_DTR` control, Linux `cdc_acm` asserts DTR by default, which causes the firmware to see SET_CONTROL_LINE_STATE with DTR=1 — which is the same as Windows. However, if the firmware firmware responds to the *absence* of DTR during a specific window, or if the timing of DTR relative to the first command matters, there could be a difference.

On Windows, `SerialPort.Open()` sends:
1. SET_CONFIGURATION (OS, automatic)
2. SET_LINE_CODING (115200, 8N1)
3. SET_CONTROL_LINE_STATE (DTR=0, RTS=0) ← default off
4. Then application sends HandshakeRequest

On Linux with `pyserial` or direct open, the equivalent sends:
1. SET_CONFIGURATION (already done at enumeration)
2. SET_LINE_CODING (via termios/ioctl)
3. SET_CONTROL_LINE_STATE (DTR=1 by default unless disabled) ← DIFFERS

**This is POSSIBLE difference.** The firmware may require DTR=0 to respond.
