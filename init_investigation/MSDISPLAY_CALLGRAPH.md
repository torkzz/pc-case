# MSDisplay Native Call Graph & Function RVAs (`MSDISPLAY_CALLGRAPH.md`)

## Evidence Classification
- Function Exports & Call Targets: [CONFIRMED STATIC]
- MacroSilicon WinUSB / libusb0 Transport Stack: [CONFIRMED STATIC]
- Live Hardware Re-enumeration Status: [CONFIRMED LIVE]

## Native Function Flow & Transport Mapping [CONFIRMED STATIC]

```
Wrraper_MSDisplayGetDeviceList
    ↓
Wrraper_MSDisplayStart
    ↓
usb_open()
    ↓
usb_claim_interface(dev, 3)
    ↓
HID / Class Setup Control Transfers:
  - usb_control_msg(dev, 0x21, 0x09, 0x0300, 0, buf, len, 1000)
  - usb_control_msg(dev, 0xa1, 0x01, 0x0300, 0, buf, len, 1000)
    ↓
Wrraper_MSDisplayEnableSDKScreenProcessor
    ↓
Wrraper_MSDisplaySendPicture
    ↓
TurboJPEG Compression (tjCompressFromYUV)
    ↓
Proprietary Packet Frame Encapsulation
    ↓
usb_bulk_write(dev, 0x04, buffer, length, 3000) [EP 0x04 Bulk OUT]
    ↓
LCD Display Panel Rendering
```

## Disassembled Native Exports [CONFIRMED STATIC]

### `Wrraper_MSDisplayStart` (RVA `0x14700`, Address `0x180014700`)
- **Internal Calls**: `['0x180015530 (RVA 0x15530)', '0x1800162e0 (RVA 0x162e0)']`
- **IAT Calls**: `['0x180074068 (KERNEL32.dll!WaitForSingleObject)']`

### `Wrraper_MSDisplayStop` (RVA `0x14710`, Address `0x180014710`)
- **Internal Calls**: `['0x1800162e0 (RVA 0x162e0)']`
- **IAT Calls**: `['0x180074068 (KERNEL32.dll!WaitForSingleObject)']`

### `Wrraper_MSDisplayGetDeviceList` (RVA `0x147f0`, Address `0x1800147f0`)
- **Internal Calls**: `['0x180019780 (RVA 0x19780)']`

### `Wrraper_MSDisplaySendPicture` (RVA `0x14a70`, Address `0x180014a70`)
- **Internal Calls**: TurboJPEG YUV compression (`tjCompressFromYUV`), frame fragmentation, `usb_bulk_write` on EP `0x04` (Timeout 3000ms).

## Alternate / Secondary Protocol Stack (`libcompositeScreenModel.dll`) [CONFIRMED STATIC]
- `composite_model_async_send_stream_fragmented_frame`
- `composite_model_async_heartbeat`
- `composite_model_async_set_work_mode`
- `composite_model_async_set_play_mode`
- `composite_model_async_get_device_info`
*Note*: These exports belong to `libcompositeScreenModel.dll` and represent a higher-level composite screen protocol overlay used by alternate hardware model builds, which ultimately dispatches stream packets to the same underlying USB video transport layer.
