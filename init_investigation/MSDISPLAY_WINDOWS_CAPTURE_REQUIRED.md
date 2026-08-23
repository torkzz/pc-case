# MSDISPLAY WINDOWS CAPTURE REQUIRED (`MSDISPLAY_WINDOWS_CAPTURE_REQUIRED.md`)

## 1. Executive Justification
Static disassembly of `MSDISPLAYSDKWRRAPER.dll`, `MSUSBDisplay.inf`, and `Vmax.exe` has 100% proven:
- **Interface**: `Interface 3` (`usb_claim_interface(dev, 3)`) [CONFIRMED STATIC]
- **Bulk OUT Endpoint**: `Endpoint 0x04` (`usb_bulk_write(dev, 0x04, buffer, length, 3000)`) [CONFIRMED STATIC]
- **Setup Control Transfers**: `bmRequestType=0x21/0xa1`, `bRequest=0x09/0x01`, `wValue=0x0300`, `wIndex=0` [CONFIRMED STATIC]
- **Header Magic Signature**: `0x0008100A` (DWORD 0 at Offset 0x00) [CONFIRMED STATIC]

However, the exact runtime bytes contained inside the SET_REPORT setup buffer (`0x21`/`0x09`/`0x0300`) and the exact byte alignment of the Bulk OUT Endpoint 0x04 JPEG packet header cannot be 100% reconstructed without a runtime packet trace.

To prevent sending malformed payloads or invalid state corruption to Interface 3, a **Windows USBPcap capture** is required.

---

## 2. Windows USBPcap / Wireshark Capture Procedure

### Step A: Prerequisites
1. Windows 10/11 PC with USBPcap and Wireshark installed.
2. Official VMAX Vendor Software suite installed (`Vmax.exe` & `UsbDisplayDriver.exe`).
3. VMAX PC-Case LCD connected via USB-C.

### Step B: Execution Sequence
1. Launch USBPcapCMD or Wireshark as Administrator.
2. Select the USB Root Hub / Port corresponding to the connected VMAX LCD device.
3. Start packet capture.
4. Launch `Vmax.exe`.
5. Observe the LCD panel illuminate and begin live desktop video rendering.
6. Allow continuous frame streaming for 5 to 10 seconds.
7. Stop `Vmax.exe`.
8. Stop USBPcap capture and save file as `vmax_msdisplay_startup.pcapng`.

---

## 3. Required Filter & Correlation Matrix

In Wireshark, apply the following filters to isolate the MSDisplay video transport:

```wireshark
usb.src == "host" || usb.dst == "host"
```

To isolate control setup transfers on Interface 3:
```wireshark
usb.bmRequestType == 0x21 || usb.bmRequestType == 0xa1
```

To isolate live video frames on Bulk OUT Endpoint 0x04:
```wireshark
usb.endpoint_address == 0x04
```

### Correlation Targets:
| Target Parameter | Wireshark Field | Native Function Origin | Expected Value |
|---|---|---|---|
| Control Setup Request | `usb.bRequest` | `usb_control_msg` (0x180018c9e) | `0x09` (SET_REPORT) / `0x01` (GET_REPORT) |
| Control Setup Value | `usb.wValue` | `usb_control_msg` (0x180018c9e) | `0x0300` |
| Control Payload Bytes | `usb.data_fragment` | Setup buffer | Raw hex bytes sent during `Wrraper_MSDisplayStart` |
| Bulk Frame Header | `usb.capdata[0:12]` | `Wrraper_MSDisplaySendPicture` | `0A 10 08 00 [W_16] [H_16] [FMT_16] [FLAG_16]` |
