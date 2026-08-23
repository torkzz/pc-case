# MSDISPLAY LINUX PROTOCOL SPECIFICATION (`MSDISPLAY_PROTOCOL.md`)

## 1. Target USB Device
- **Vendor ID (VID):** `0x33c3` (`HL VMAX`)
- **Product ID (PID):** `0xf101` (`HL-VMAX-USB-Device`)
- **Interface:** `1` (`CDC Data`)
- **Endpoint:** `0x02` Bulk OUT
- **Speed:** USB 2.0 High Speed (480 Mbps, 512-byte max packet size)
- **Kernel Claiming:** Unbind `cdc_acm` kernel driver via `/sys/bus/usb/drivers/cdc_acm/unbind` then claim Interface 1 via `usbfs` (`USBDEVFS_CLAIMINTERFACE` ioctl).

---

## 2. MSDisplay 12-Byte Frame Header Format

```
+-----------------------------------------------------------------------------------+
| Offset (Hex) | Size (Bytes) | Field Name             | Type      | Proven Value   |
+-----------------------------------------------------------------------------------+
| 0x00 - 0x03  | 4            | Magic Header Signature | uint32    | 0x0008100A     |
| 0x04 - 0x05  | 2            | Frame Width            | uint16    | 480 (0x01E0)   |
| 0x06 - 0x07  | 2            | Frame Height           | uint16    | 1920 (0x0780)  |
| 0x08 - 0x09  | 2            | Frame Stride           | uint16    | 0 (or 480)     |
| 0x0A - 0x0B  | 2            | Quality / Flag         | uint16    | 1 (or 0)       |
| 0x0C - End   | N            | Image Frame Payload    | Bytes     | TurboJPEG Data |
+-----------------------------------------------------------------------------------+
```

Python Struct Packer (Production Form):
```python
header = struct.pack("<IHHHH", 0x0008100A, 480, 1920, 480, 1)
```

Header Hex String (Production Form):
```text
0a 10 08 00 e0 01 80 07 e0 01 01 00
```

Experimental Form (Also accepted by device):
```text
0a 10 08 00 e0 01 80 07 00 00 01 00
```

---

## 6. Header Stride Discrepancy Note (`stride=0` vs `stride=480`)
- **Experimental Form (`stride=0` / `00 00`):** In early experiments, `stride=0` was submitted and accepted by the device hardware. The firmware JPEG decoder handles `stride=0` by defaulting to the frame width parameter (`wWidth=480`).
- **Production Native Form (`stride=480` / `e0 01`):** Disassembly of `MSDISPLAYSDKWRRAPER.dll` (`0x18001893a`: `mov %si, 0x8(%rbx)`) proves the native C/C++ SDK passes `wStride=480` (`0x01E0`).
- **Production Standard:** The production driver (`msdisplay/protocol.py`) uses `stride=480` (`0a 10 08 00 e0 01 80 07 e0 01 01 00`) matching the native SDK disassembly exactly.
- **Unresolved Semantics:** Whether `stride=0` signifies automatic stride calculation or legacy mode in firmware remains [UNKNOWN]. Both forms function identically on physical hardware.

---

## 3. Geometry & Resolution Limits
- **Native Active Width:** `480` pixels [CONFIRMED LIVE & STATIC]
- **Native Active Height:** `1920` pixels [CONFIRMED LIVE & STATIC]
- **Aspect Ratio:** 1:4 Portrait orientation (`|`)
- **Maximum Accepted Active Width:** `480` pixels

---

## 4. JPEG Stream Requirements
- **Format:** JPEG / JFIF
- **Chroma Subsampling:** YUV 4:4:4 (`subsampling=0` in PIL / `-pix_fmt yuv444p` in FFmpeg)
- **JPEG MCU Block Size:** 8×8 pixels
- **DQT Table:** 1 single DQT table (Len=67)
- **DHT Table:** 1 single combined DHT table (Len=81 or baseline)

---

## 5. Frame Transmission & Keep-Alive Loop
- **Transport Method:** Direct `usbfs` ioctl (`USBDEVFS_BULK`) to EP `0x02` Bulk OUT.
- **Keep-Alive Interval:** Stream periodic frames every `1.0s` (maximum interval <= `4.0s` before firmware backlight auto-turnoff).
- **USB Return Status:** Returns exact byte count submitted (e.g., `30,246 B` for a 480x1920 frame).
