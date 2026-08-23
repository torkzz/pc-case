# COMPOSITE PROTOCOL RE (`COMPOSITE_PROTOCOL_RE.md`)

## Evidence Classification
- Function Exports & Signatures: [CONFIRMED STATIC]
- Fragmentation Calculation: [CONFIRMED STATIC]
- Layer Classification: [CONFIRMED STATIC]

---

## 1. Dissected Functions in `libcompositeScreenModel.dll` [CONFIRMED STATIC]

1. `composite_model_async_send_stream_fragmented_frame`:
   - Address: `0x1800127d0`
   - Purpose: Calculates frame chunk size (`leaq 0x1fde(%rax), %rcx` -> max chunk size 8158 / 4096 bytes) and dispatches fragment payload via `SavApp::async_action`.

2. `composite_model_async_heartbeat`:
   - Address: `0x1800114f0`
   - Purpose: Sends periodic heartbeat keep-alive packet to prevent display panel standby auto-shutdown.

3. `composite_model_async_set_work_mode`:
   - Address: `0x180014ac0`
   - Purpose: Sets display mode (`WorkMode::StreamMode = 0`, `WorkMode::LocalFileMode = 1`).

4. `composite_model_async_set_play_mode`:
   - Address: `0x180013e80`
   - Purpose: Sets media loop/single playback mode (`PlayMode::Loop = 0`, `PlayMode::Single = 1`).

---

## 2. Layer Protocol Classification [CONFIRMED STATIC]

The Composite Screen Model protocol (`libcompositeScreenModel.dll` + `libstack.dll`) is an **RPC message protocol overlay** layered over the primary USB display transport, used for async stream control, file transfers, and heartbeat monitoring.
