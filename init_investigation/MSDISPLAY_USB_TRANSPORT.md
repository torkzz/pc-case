# MSDISPLAY USB TRANSPORT (`MSDISPLAY_USB_TRANSPORT.md`)

## 1. Native USB Transport Architecture [CONFIRMED STATIC]

The VMAX video rendering engine uses a direct native USB transport stack separate from the CDC ACM serial telemetry interface (`33c3:f101`).

```
Application Layer (Vmax.exe)
        ↓
Native MSDisplay Wrapper (MSDISPLAYSDKWRRAPER.dll)
        ↓
Indirect Display Driver (Idd) / libusb0 User Driver
        ↓
USB Interface 3 (Claimed via usb_claim_interface(dev, 3))
        ↓
Endpoint 0x04 (Bulk OUT, Timeout 3000ms via usb_bulk_write)
        ↓
MacroSilicon Video Display Controller (345f:9132)
```

---

## 2. Proven USB Transport Parameters [CONFIRMED STATIC]

| Parameter | Value | Evidence Level |
|---|---|---|
| **Target VID** | `0x345f` (MacroSilicon) | [CONFIRMED STATIC] |
| **Target PIDs** | `0x9132`, `0x9133`, `0x374a`, `0xa101` | [CONFIRMED STATIC] |
| **Driver Service** | `libusb0.sys` / `MSUSBDisplay.inf` | [CONFIRMED STATIC] |
| **Interface GUID** | `{FB781AAF-9C70-4523-A5DF-642A87ECA567}` | [CONFIRMED STATIC] |
| **Device Path** | `\\\\.\\WinUsbDisplay\\` | [CONFIRMED STATIC] |
| **Target USB Interface** | `Interface 3` (`USB\VID_345F&PID_9132&MI_03`) | [CONFIRMED STATIC] |
| **Bulk OUT Endpoint** | `Endpoint 0x04` | [CONFIRMED STATIC] |
| **Bulk Write Timeout** | `3000 ms` | [CONFIRMED STATIC] |
| **Control Setup Request (SET)** | `bmRequestType=0x21`, `bRequest=0x09`, `wValue=0x0300`, `wIndex=0` | [CONFIRMED STATIC] |
| **Control Setup Request (GET)** | `bmRequestType=0xa1`, `bRequest=0x01`, `wValue=0x0300`, `wIndex=0` | [CONFIRMED STATIC] |

---

## 3. Discovered Frame Structure [CONFIRMED STATIC]

The payload submitted to Endpoint 0x04 Bulk OUT consists of a proprietary 12-byte header followed by TurboJPEG compressed frame data:

```
+-----------------------------------------------------------------------+
| Offset (Hex) | Field Name            | Type   | Proven Value / Value  |
+-----------------------------------------------------------------------+
| 0x00 - 0x03  | Magic Header Sign     | DWORD  | 0x0008100A            |
| 0x04 - 0x05  | Frame Width           | WORD   | Width (e.g. 2560)     |
| 0x06 - 0x07  | Frame Height          | WORD   | Height (e.g. 666)     |
| 0x08 - 0x09  | Frame Format / Stride | WORD   | Format Specifier      |
| 0x0A - 0x0B  | Frame Flag / Quality  | WORD   | Flag Specifier        |
| 0x0C - End   | JPEG Compressed Data  | Bytes  | TurboJPEG Frame Data  |
+-----------------------------------------------------------------------+
```

---

## 4. Current Host Topology Status [CONFIRMED LIVE]

- **CDC Telemetry MCU (`33c3:f101`)**: Active on Linux host USB bus (Bus 001 Device 003, `cdc_acm`). [CONFIRMED LIVE]
- **MacroSilicon Video Controller (`345f:9132`)**: Absent from current `lsusb` topology. [CONFIRMED LIVE]
- **Reason for Absence**: Video IC unpowered or requires driver activation sequence. [STRONGLY SUPPORTED]
