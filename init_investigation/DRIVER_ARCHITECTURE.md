# MSDisplay Linux Native Driver Architecture (`DRIVER_ARCHITECTURE.md`)

## 1. Executive Summary
- **Device:** HL-VMAX PC-Case LCD Display (`33c3:f101`)
- **Connection:** Single USB-C cable (5V Power + Data)
- **USB Interface:** Interface `1` (`CDC Data`)
- **USB Endpoint:** Endpoint `0x02` Bulk OUT (High Speed USB 2.0, 512-byte max packet size)
- **Native Geometry:** `480 × 1920` (1:4 Portrait aspect ratio)
- **Driver Architecture:** Modular Python package (`msdisplay/`) utilizing direct `usbfs` ioctls (`USBDEVFS_BULK`) for Linux kernel execution.

---

## 2. Verified Protocol Specification

### 12-Byte MSDisplay Header
Prepend to every TurboJPEG/JPEG frame payload:

```
+------------------------------------------------------------------------------------+
| Offset (Hex) | Size (Bytes) | Field Name             | Type       | Value          |
+------------------------------------------------------------------------------------+
| 0x00 - 0x03  | 4            | Magic Header Signature | uint32_le  | 0x0008100A     |
| 0x04 - 0x05  | 2            | Frame Width            | uint16_le  | 480 (0x01E0)   |
| 0x06 - 0x07  | 2            | Frame Height           | uint16_le  | 1920 (0x0780)  |
| 0x08 - 0x09  | 2            | Frame Stride           | uint16_le  | 480 (0x01E0)   |
| 0x0A - 0x0B  | 2            | Quality / Flag         | uint16_le  | 1 (0x0001)     |
| 0x0C - End   | N            | TurboJPEG Frame Data   | Bytes      | Starts 0xFFD8  |
+------------------------------------------------------------------------------------+
```

Python Struct Packer:
```python
header = struct.pack("<IHHHH", 0x0008100A, width, height, stride, flag)
```

Working Hex Header (480×1920):
```text
0a 10 08 00 e0 01 80 07 e0 01 01 00
```

---

## 3. Package Architecture (`msdisplay/`)

```
msdisplay/
├── __init__.py       # Package metadata and top-level exports
├── protocol.py       # Header packing and payload encapsulation
├── usb.py            # Device discovery, cdc_acm unbinding, usbfs ioctls
├── jpeg.py           # Image loading, crop/resize, JPEG encoding
├── display.py        # High-level MSDisplayController API
└── cli.py            # Command Line Interface (grid, solid, image)
```

### Module Responsibilities

1. **`protocol.py`**:
   - `pack_msdisplay_header(width, height, stride, flag)`
   - `build_frame_payload(jpeg_bytes, width, height, stride, flag)`

2. **`usb.py`**:
   - `find_target_usb_device(vid, pid)`
   - `unbind_cdc_acm()`
   - `MSDisplayUSBDevice`: Manages file descriptor `os.open`, `USBDEVFS_CLAIMINTERFACE`, `USBDEVFS_BULK`, and `USBDEVFS_RELEASEINTERFACE`.

3. **`jpeg.py`**:
   - `prepare_image(image, width=480, height=1920, preserve_aspect=False)`: Slices/crops or resizes images wider than 480 pixels.
   - `encode_jpeg(image, quality=95, subsampling=0)`: Encodes PIL Image to JPEG byte payload.
   - `create_solid_color_jpeg(r, g, b, width=480, height=1920)`
   - `create_test_grid_jpeg(width=480, height=1920)`

4. **`display.py`**:
   - `MSDisplayController`:
     - `connect()`
     - `close()`
     - `send_jpeg(jpeg_bytes, width=480, height=1920, stride=480, flag=1)`
     - `show_image(image_or_path, preserve_aspect=False)`
     - `solid_color(r, g, b)`
     - `test_grid()`

5. **`cli.py`**:
   - CLI interface for `msdisplay test-grid`, `msdisplay solid red|green|blue|white`, `msdisplay image <path>`.

---

## 4. Evidence Boundary
- **Confirmed Fact:** Native SDK disassembly uses `0x1E0` (480) for stride allocation (`imul %esi, %eax`).
- **Confirmed Fact:** Physical panel renders 480×1920 framebuffers 100% correctly.
- **Confirmed Fact:** Framebuffers wider than 480 pixels (e.g. 640px) transmit completely over USB, but pixels beyond X=479 are truncated outside the physical panel display viewport.
- **Unclaimed Boundary:** The LCD controller IC's internal address-window register has NOT been directly decompiled or probed via JTAG/hardware tracing; conclusions are grounded in native assembly and USB live behavior.
