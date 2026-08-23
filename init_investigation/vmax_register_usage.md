# Register Operation Protocol & Usage (`vmax_register_usage.md`)

## Protocol Definition (CMD 0x0090)

`RegisterOperationRequest` uses **CMD 0x0090 (144)** and expects response **CMD 0x00D0 (208)** (`BaseRegisterResponse`).

### Control Byte Format
- Bit 7: `NeedReply` (0x80)
- Bits 4–6: `FunctionCode`
  - `FUNC_SET_VALUE_REG = 0x00`
  - `FUNC_READ_VALUE_REG = 0x04`
  - `FUNC_SET_STRING_REG = 0x05`
  - `FUNC_READ_STRING_REG = 0x06`
  - `FUNC_SET_ARRAY_REG = 0x07`
- Bits 0–3: `RegisterCount`

### Usage in Vmax.exe
Register operations (`SetValueRegisterAsync`, `SetStringRegisterAsync`) are used for dynamic sensor value updates (CPU temp, GPU load, RAM usage) when the telemetry engine operates in CDC ACM asset mode. They are **not part of the initial connection handshake**.
