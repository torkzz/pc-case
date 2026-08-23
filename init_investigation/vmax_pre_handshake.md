# Pre-Handshake Operations (`vmax_pre_handshake.md`)

## Operations Between SerialPort.Open() and Handshake (0x0080)

Static IL disassembly confirms:
1. **SerialPort.Open()** is called inside `DeviceCommunicator.Connect(portName, 115200)`.
2. Windows `usbser.sys` automatically issues:
   - `SET_LINE_CODING(115200 8N1)`
   - `SET_CONTROL_LINE_STATE(wValue=0x0000)`  (DTR=0, RTS=0)
3. **No serial writes or reads occur before `HandshakeRequest` (0x0080)**.
4. `HandshakeRequest` (CMD `0x0080`) is the **very first application-layer frame** sent to `33c3:f101` via `DeviceCommunicationLibrary.dll`.
5. However, before or alongside telemetry serial port open, `Vmax.exe` initializes native display drivers via `MSDISPLAYSDKWRRAPER.dll` (`Wrraper_MSDisplayGetDeviceList`, `Wrraper_MSDisplayStart`).
