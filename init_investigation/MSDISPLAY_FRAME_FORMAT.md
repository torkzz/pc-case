# MSDISPLAY FRAME FORMAT (`MSDISPLAY_FRAME_FORMAT.md`)

## Evidence Classification
- Frame Header Signature & Offset Layout: [CONFIRMED STATIC]
- Frame Encoder (TurboJPEG): [CONFIRMED STATIC]
- Bulk Endpoint Address: [CONFIRMED STATIC]

---

## 12-Byte Frame Header Structure [CONFIRMED STATIC]

The payload submitted to Endpoint 0x04 Bulk OUT during `Wrraper_MSDisplaySendPicture` (address `0x180018927`) consists of a 12-byte header followed by TurboJPEG compressed frame data:

| Offset (Hex) | Size (Bytes) | Field Name | How Derived | Confidence |
|---|---|---|---|---|
| `0x00` | 4 | Magic Signature (`0x0008100A`) | Assembly `movl $0x8100a, (%rbx)` at `0x180018927` | [CONFIRMED STATIC] |
| `0x04` | 2 | Frame Width (e.g. 2560) | Assembly `movw %r15w, 0x4(%rbx)` at `0x180018930` | [CONFIRMED STATIC] |
| `0x06` | 2 | Frame Height (e.g. 666) | Assembly `movw %r12w, 0x6(%rbx)` at `0x180018935` | [CONFIRMED STATIC] |
| `0x08` | 2 | Format Stride / Color Mode | Assembly `movw %si, 0x8(%rbx)` at `0x18001893a` | [CONFIRMED STATIC] |
| `0x0A` | 2 | Compression Flag / Quality | Assembly `movw %ax, 0xa(%rbx)` at `0x18001893e` | [CONFIRMED STATIC] |
| `0x0C` | N | TurboJPEG Frame Buffer | `memcpy` at `0x180018942` (`rbx + 12`) | [CONFIRMED STATIC] |

---

## Stream Fragmentation Layout [CONFIRMED STATIC]

When streaming via `libcompositeScreenModel.dll` (`composite_model_async_send_stream_fragmented_frame` at `0x1800127d0`), frame buffers exceeding 4KB / 8KB are divided into chunk sizes of `0x1FDE` (8158 bytes) or `0x1000` (4096 bytes) and submitted sequentially to the transport queue.
