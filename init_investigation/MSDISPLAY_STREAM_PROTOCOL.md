# MSDISPLAY STREAM PROTOCOL (`MSDISPLAY_STREAM_PROTOCOL.md`)

## Evidence Classification
- Frame Header Signature & Structure: [CONFIRMED STATIC]
- Frame Encoding Engine (TurboJPEG): [CONFIRMED STATIC]
- Transport Endpoint & Interface: [CONFIRMED STATIC]

---

## Frame Packetization & Layout [CONFIRMED STATIC]

When `Wrraper_MSDisplaySendPicture` (address `0x180018927`) is called, desktop RGB frames are processed as follows:

1. **JPEG Compression**: RGB frame compressed to JPEG via TurboJPEG (`tjCompressFromYUV`).
2. **Proprietary Header Prepend**: A 12-byte header is prepended to the JPEG byte stream:

| Offset (Hex) | Size (Bytes) | Field | How Derived | Confidence |
|---|---|---|---|---|
| `0x00` | 4 | Magic Header Signature (`0x0008100A`) | Assembly `movl $0x8100a, (%rbx)` | [CONFIRMED STATIC] |
| `0x04` | 2 | Frame Width (e.g., 2560) | Assembly `movw %r15w, 0x4(%rbx)` | [CONFIRMED STATIC] |
| `0x06` | 2 | Frame Height (e.g., 666) | Assembly `movw %r12w, 0x6(%rbx)` | [CONFIRMED STATIC] |
| `0x08` | 2 | Frame Format Stride | Assembly `movw %si, 0x8(%rbx)` | [CONFIRMED STATIC] |
| `0x0A` | 2 | Quality / Compression Flag | Assembly `movw %ax, 0xa(%rbx)` | [CONFIRMED STATIC] |
| `0x0C` | N | TurboJPEG Image Data | `memcpy` at `0x180018942` (`rbx + 12`) | [CONFIRMED STATIC] |

3. **USB Transport Submission**: The combined 12-byte header + JPEG payload is submitted to `Endpoint 0x04` Bulk OUT via `usb_bulk_write` with a 3000ms timeout.
