# Vmax SerialPort Configuration (`vmax_serial_configuration.md`)

## Confirmed SerialPort Settings

Extracted from static IL analysis of `DeviceCommunicationLibrary.dll`:

- **Constructor**: `new SerialPort(portName, baudRate = 115200, Parity.None = 0, dataBits = 8, StopBits.One = 1)`
- **BaudRate**: 115200 bps (`0x0001C200`)
- **DataBits**: 8
- **Parity**: `Parity.None` (0)
- **StopBits**: `StopBits.One` (1)
- **DTR / RTS**: `DtrEnable` and `RtsEnable` are **NOT explicitly set** in `DeviceCommunicator.Connect()`. On Windows `System.IO.Ports.SerialPort`, both default to `false` (wValue = `0x0000`).
- **Timeouts**: `ReadTimeout` and `WriteTimeout` default to `-1` (infinite).
- **Buffer Threshold**: `ReceivedBytesThreshold` = 1 (default).
- **Event Handling**: `SerialPort.DataReceived` handles incoming bytes; calls `SerialPort.Read(buf, 0, BytesToRead)` and processes frames via `ProcessReceiveBuffer()`.
