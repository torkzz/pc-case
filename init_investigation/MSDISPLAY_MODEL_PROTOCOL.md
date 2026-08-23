# MSDISPLAY MODEL PROTOCOL (`MSDISPLAY_MODEL_PROTOCOL.md`)

## 1. Overview [CONFIRMED STATIC]
`libcompositeScreenModel.dll` and `libstack.dll` implement an asynchronous composite model RPC protocol stack (`CompositeScreenModel` / `SavApp` / `SavManager`) used by VMAX for video streaming, local storage management, and heartbeat monitoring.

```
Vmax.exe (UI / Application Layer)
    ↓
libcompositeScreenModel.dll (Model Layer)
  ├── async_send_stream_fragmented_frame
  ├── async_heartbeat
  ├── async_set_work_mode / async_set_play_mode
  └── async_get_device_info / async_get_storage_info
    ↓
libstack.dll (Stack / Transport Layer)
  ├── SavApp::async_action
  ├── SavManager::dispatch
  └── SavNotice::register_listener
    ↓
MSDISPLAYSDKWRRAPER.dll / libusb0.dll (Native USB Transport)
    ↓
USB Interface 3 / Endpoint 0x04 (Bulk OUT)
```

---

## 2. Exported Model Functions & Structs [CONFIRMED STATIC]

### `composite_model_async_send_stream_fragmented_frame`
- **Address**: `0x1800127d0`
- **Purpose**: Fragments large video frames into chunks of max size `0x1FDE` (8158 bytes) or `0x1000` (4096 bytes) and queues them for transmission to the display transport.
- **Parameters**: `(string device_path, StreamFrameInfo info, vector<uint8> frame_data, function<void()> callback)`

### `composite_model_async_heartbeat`
- **Address**: `0x1800114f0`
- **Purpose**: Transmits periodic heartbeat packet to prevent LCD standby auto-shutdown.
- **Opcode Data**: `0x180021b10` / `0x1800223d0` constant headers.

### `composite_model_async_set_work_mode`
- **Address**: `0x180014ac0`
- **Purpose**: Configures device work mode (`WorkMode::StreamMode = 0`, `WorkMode::LocalFileMode = 1`).

### `composite_model_async_set_play_mode`
- **Address**: `0x180013e80`
- **Purpose**: Sets media playback mode (`PlayMode::Loop = 0`, `PlayMode::Single = 1`).

### `composite_model_async_get_device_info`
- **Address**: `0x180010620`
- **Purpose**: Queries display device info (`DeviceInfo` struct containing screen resolution, width, height, firmware version).

---

## 3. Wire Packet Structures [CONFIRMED STATIC]

```
+-----------------------------------------------------------------------------------+
| Offset (Hex) | Field Name              | Type   | Proven Value / Meaning          |
+-----------------------------------------------------------------------------------+
| 0x00 - 0x01  | Packet Command Opcode   | WORD   | Opcode (e.g. Heartbeat/Stream)  |
| 0x02 - 0x03  | Sub-command / Sequence  | WORD   | Fragment / Packet Index         |
| 0x04 - 0x07  | Total Payload Length    | DWORD  | Fragment / Buffer Size          |
| 0x08 - End   | Payload Buffer          | Bytes  | JPEG Fragment / Command Data    |
+-----------------------------------------------------------------------------------+
```
