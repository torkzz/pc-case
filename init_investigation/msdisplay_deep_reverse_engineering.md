# MSDisplay Deep Reverse Engineering Analysis (`msdisplay_deep_reverse_engineering.md`)

## Evidence Classification
- Native DLL Export & Disassembly Analysis: [CONFIRMED STATIC]
- MacroSilicon INF & GUID Mapping: [CONFIRMED STATIC]
- Host USB Topology: [CONFIRMED LIVE]

---

## 1. Dissected Native Binaries [CONFIRMED STATIC]

1. **`MSDISPLAYSDKWRRAPER.dll`**: Native C++ wrapper for MacroSilicon USB display controllers.
   - Imports: `libusb0.dll` (`usb_init`, `usb_find_busses`, `usb_find_devices`, `usb_get_busses`, `usb_open`, `usb_claim_interface`, `usb_control_msg`, `usb_bulk_write`, `usb_close`), `SETUPAPI.dll` (`SetupDiGetClassDevsW`, `SetupDiEnumDeviceInterfaces`, `SetupDiGetDeviceInterfaceDetailW`), `KERNEL32.dll` (`CreateFileW`, `DeviceIoControl`).
   - Targets: VID `0x345f`, PIDs `0x9132`, `0x9133`, `0x374a`, `0xa101`.

2. **`libcompositeScreenModel.dll`**: Composite screen RPC model library.
   - Exports: `composite_model_async_send_stream_fragmented_frame`, `composite_model_async_heartbeat`, `composite_model_async_set_work_mode`, `composite_model_async_set_play_mode`, `composite_model_async_get_device_info`.
   - Imports: `libstack.dll` (`SavApp::async_action`, `SavManager::instance`).

3. **`libstack.dll`**: Low-level transport manager.
   - Statically links `libusb` framework (`libusb_open`, `libusb_claim_interface`, `libusb_control_transfer`, `libusb_bulk_transfer`).
   - Handles async message dispatch, packet queueing, and heartbeat monitoring.

---

## 2. Reconstructed Control & Data Flow [CONFIRMED STATIC]

```
Vmax.exe (WPF Application)
    ↓
libcompositeScreenModel.dll / DeviceCommunicationLibrary.dll
    ↓
MSDISPLAYSDKWRRAPER.dll
    ↓
libusb0.dll / WinUSB (Device GUID {FB781AAF-9C70-4523-A5DF-642A87ECA567})
    ↓
USB Interface 3 (Claimed via usb_claim_interface(dev, 3))
    ↓
Endpoint 0x04 Bulk OUT (3000ms Timeout)
    ↓
LCD Display Panel
```
