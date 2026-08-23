# MSDisplay VMAX PC-Case LCD — Reverse Engineering & Driver Status

## 1. Executive Summary
- **Physical Device:** HL-VMAX PC-Case LCD Display (`33c3:f101`).
- **Physical Connection:** Single USB-C cable (5V Power + Data). No SATA/Molex/secondary cables.
- **Physical Panel Resolution:** `640 x 1920` (Portrait `|` orientation, 1:3 aspect ratio).
- **USB Transport Target:** `33c3:f101` Interface 1 Endpoint `0x02` Bulk OUT via `USBDEVFS_BULK` ioctl.
- **Driver State:** **100% Native Linux Driver Working.** Real-time system stats dashboard streaming via fast PIL in-memory pipeline.

---

## 2. Wire Protocol & Frame Format
Each frame submitted to Endpoint 0x02 Bulk OUT consists of a **12-byte MSDisplay Header** prepended to a **TurboJPEG payload**:

```
[12-Byte Header] + [JPEG Stream Payload]
```

### 12-Byte Header Field Layout
```
Offset 0x00 (4 Bytes) : Magic Signature 0x0008100A (Hex: 0a 10 08 00)
Offset 0x04 (2 Bytes) : Width = 640 (Little Endian uint16: 80 02)
Offset 0x06 (2 Bytes) : Height = 1920 (Little Endian uint16: 80 07)
Offset 0x08 (2 Bytes) : Stride = 0 (Little Endian uint16: 00 00)
Offset 0x0A (2 Bytes) : Display Flag = 1 (Little Endian uint16: 01 00)
```

---

## 3. Root Cause of Image Splitting & Resolution
- **Issue:** FFmpeg subprocess execution + default high-q FFmpeg JPEG encoding generated frame payloads exceeding 100KB with 16x16 MCU block sizes, causing the hardware JPEG decoder on the LCD board to lag and split MCU rows.
- **Solution:** Switched pipeline to native PIL drawing directly in RAM (`subsampling=0` YUV444 8x8 MCU blocks or `subsampling=2` optimized). Render latency dropped from ~200ms (ffmpeg) to <5ms (PIL), eliminating all splitting, scrolling, and lag.

---

## 4. Key Executables & Usage
- **Real-Time System Stats Monitor:**
  ```bash
  .venv/bin/python msdisplay_system_stats.py --interval 1.0 --duration 60
  ```
- **Native 640x1920 Image Test:**
  ```bash
  .venv/bin/python init_investigation/test_640x1920_native.py --duration 10
  ```
- **Custom Text Card Test:**
  ```bash
  .venv/bin/python init_investigation/test_clean_text.py --text "HELLO WORLD" --duration 10
  ```

---

## 5. Proven Facts Table
| Feature | Status | Notes |
| :--- | :--- | :--- |
| **USB Enumeration** | `CONFIRMED LIVE` | `33c3:f101` Interface 1 |
| **Panel Resolution** | `CONFIRMED LIVE` | 640x1920 Portrait |
| **Keep-Alive Requirement** | `CONFIRMED LIVE` | Stream frame every <= 4.0s |
| **Frame Header** | `CONFIRMED LIVE` | `0a 10 08 00 80 02 80 07 00 00 01 00` |
| **Live Stats Daemon** | `CONFIRMED LIVE` | `msdisplay_system_stats.py` working |
