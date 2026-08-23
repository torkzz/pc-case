# MSDISPLAY FIRST FRAME SPECIFICATION (`MSDISPLAY_FIRST_FRAME.md`)

## Evidence Classification
- Native DLL Assembly Layout: [CONFIRMED STATIC]
- Frame Generator Verification: [CONFIRMED LIVE]
- usbfs Bulk OUT Execution: [CONFIRMED LIVE]

---

## Proven 12-Byte Frame Header Structure [CONFIRMED STATIC & LIVE]

```
+---------------------------------------------------------------------------------+
| Offset (Hex) | Size (Bytes) | Field Name            | Value / Field Specifier   |
+---------------------------------------------------------------------------------+
| 0x00 - 0x03  | 4            | Magic Header Sign     | 0x0008100A                |
| 0x04 - 0x05  | 2            | Frame Width           | 2560 (0x0A00)             |
| 0x06 - 0x07  | 2            | Frame Height          | 666  (0x029A)             |
| 0x08 - 0x09  | 2            | Format Stride / Mode  | 0 (Format Specifier)      |
| 0x0A - 0x0B  | 2            | Quality Flag / Mode   | 0 (Quality Specifier)     |
| 0x0C - End   | N            | TurboJPEG Frame Data  | Compressed Image Payload  |
+---------------------------------------------------------------------------------+
```

---

## Single Frame Execution Verification [CONFIRMED LIVE]

1. **Payload Generation**: `hello_world_frame.bin` (27,895 bytes: 12B Header `0x0008100A` + 2560x666 TurboJPEG image).
2. **usbfs Execution**: Submitted directly via `usbfs_direct_test.py` (`USBDEVFS_BULK` ioctl) to Endpoint 0x02 Bulk OUT.
3. **Execution Status**: Kernel returned `0` (`27895 bytes submitted successfully to EP 0x02 Bulk OUT!`).
