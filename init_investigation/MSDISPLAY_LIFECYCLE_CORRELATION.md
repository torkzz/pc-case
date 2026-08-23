# MSDISPLAY LIFECYCLE CORRELATION (`MSDISPLAY_LIFECYCLE_CORRELATION.md`)

## Evidence Classification
- Visual Evidence (Photo / Panel Rendering): [CONFIRMED LIVE]
- USB Endpoint Monitoring & usbfs Submissions: [CONFIRMED LIVE]
- Diagnostic Pattern Generation: [CONFIRMED LIVE]

---

## 1. User Visual Observation Analysis [CONFIRMED LIVE]

- **Panel Power & Backlight**: ON.
- **Display Content**: Highly recognizable image rendering (blue/cloud static asset content).
- **Artifact Observed**: Distinct horizontal corrupted/glitched band across the upper/middle portion of the panel.
- **Image Integrity**: Image content above and below the band is substantially recognizable and intact.
- **Conclusion**: The LCD panel and display controller pipeline are physically functional and receiving frame data over Linux usbfs Endpoint 0x02 Bulk OUT.

---

## 2. Diagnostic Execution Matrix [CONFIRMED LIVE]

| Test Mode | Pattern Sent | JPEG Byte Size | Total USB Payload | Purpose | Execution Status |
|---|---|---|---|---|---|
| `single` | Pattern A (Black Grid) | 118,976 bytes | 118,988 bytes | Test single static frame rendering | Executed OK (`118988 bytes`) |
| `color-bars` | Pattern C (Red/Green/Blue/White/Black) | 52,772 bytes | 52,784 bytes | Isolate horizontal color Y band | Executed OK (`52784 bytes`) |
| `alternate` | Pattern A <-> Pattern B | 118,988 B <-> 119,402 B | 118,988 B / 119,402 B | Check if corruption moves with image or stays fixed | Executed OK (40 Iterations) |

---

## 3. Potential Artifact Causes & Upgrade Path [STRONGLY SUPPORTED]

1. **JPEG Subsampling / Stride Mismatch**:
   - `MSDisplay` 12-byte header `WORD` at Offset `0x08` (Format/Stride) or Offset `0x0A` (Quality Flag) specifies YUV subsampling mode (4:2:0 vs 4:2:2 vs 4:4:4).
2. **Transfer Packetization / Endpoint Boundary Alignment**:
   - High-speed USB 2.0 Bulk packets use 512-byte packet boundaries (`0x200`). If a JPEG frame length is not padded to expected alignment, the MCU display buffer may skew at the final boundary.
