# Hardware & Architecture Investigation Report — Phase 2 (`HARDWARE_ARCHITECTURE_INVESTIGATION.md`)

## Executive Summary
Timestamped Architecture Investigation update integrating dual-engine disassembly, native SDK wrapper findings, systematic command matrix results, and physical topology analysis.

---

## Evidence Level Classifications
- **CONFIRMED**: Proven statically via IL/native disassembly or live via Linux kernel `usbmon1` / raw `usbfs` ioctls.
- **STRONGLY SUPPORTED**: Direct deduction grounded in vendor assembly structures, drivers, and INF files.
- **POSSIBLE**: Logical candidate hypothesis consistent with existing observations.
- **UNKNOWN**: Unverified physical state requiring hardware inspection.

---

## 1. Confirmed Architecture & Dual Engine Mapping (`CONFIRMED`)

```
Vmax.exe (Master Application)
  │
  ├── 1. Control & Telemetry Engine (AICDisp) [CONFIRMED]
  │     ├── Assembly: DeviceCommunicationLibrary.dll
  │     ├── Target VID:PID: 33c3:f101 (HL-VMAX-USB-Device)
  │     ├── Transport: CDC ACM Serial Port (/dev/ttyACM0, 115200 8N1)
  │     └── Purpose: Hardware info (0x0072), Handshake (0x0080), Status (0x0071), Asset Storage (0x0082)
  │
  └── 2. Real-Time Video Display Engine (MSDisplay) [CONFIRMED]
        ├── Assembly: MSDISPLAYSDKWRRAPER.dll (Native MacroSilicon C/C++ SDK)
        ├── Driver INF: MSUSBDisplay.inf (USB\VID_345F&PID_9132&MI_03)
        ├── Target VID:PIDs: 345f:9132, 345f:9133, 345f:374a, 345f:a101
        ├── Transport: High-Speed USB Bulk OUT (libusb0 / UsbDk)
        └── Purpose: Real-time desktop frame capture -> TurboJPEG compression -> Direct LCD video display
```

---

## 2. Competing Physical Architecture Models

### H1: Same PCB + Two USB-Connected Controllers (Dual Cable / Internal Hub)
- **Status**: **STRONGLY SUPPORTED**
- **Evidence FOR**: `MSDISPLAYSDKWRRAPER.dll` and `MSUSBDisplay.inf` explicitly target `345f:9132`. `Vmax.exe` startup logic enumerates MacroSilicon devices via `Wrraper_MSDisplayGetDeviceList()`.
- **Evidence AGAINST**: `345f:9132` is not currently enumerated in `lsusb`.
- **Missing Evidence**: Verification of secondary internal motherboard USB header.
- **Test Required**: Inspect LCD module for a second USB cable / 9-pin motherboard header.
- **Expected Result**: Connecting the second header causes `345f:9132` to enumerate on Linux.

### H2: Unpowered Auxiliary Power Rail (SATA / Molex 5V/12V Missing)
- **Status**: **STRONGLY SUPPORTED**
- **Evidence FOR**: `33c3:f101` USB SIE responds to USB setup and bulk OUT packets with status 0, but MCU application core produces zero RX bytes. Explains why MacroSilicon video IC is unpowered and absent from `lsusb`.
- **Evidence AGAINST**: Requires physical board inspection to verify power cabling.
- **Missing Evidence**: Physical power cable verification.
- **Test Required**: Check rear of LCD module for SATA/Molex power connector.
- **Expected Result**: Supplying 5V/12V powers on the MCU core and MacroSilicon display controller.

### H3: Standalone Control MCU / Different Hardware Revision
- **Status**: **POSSIBLE**
- **Evidence FOR**: `33c3:f101` CDC ACM interface functions independently under `DeviceCommunicationLibrary.dll`.
- **Evidence AGAINST**: `Vmax.exe` binary imports BOTH `DeviceCommunicationLibrary.dll` AND `MSDISPLAYSDKWRRAPER.dll` simultaneously.
- **Missing Evidence**: Visual confirmation of PCB chips.
- **Test Required**: Visual inspection of LCD PCB.
- **Expected Result**: Identifying whether MacroSilicon IC exists on the board.

---

## 3. Decisive Phase 2 Conclusions

1. **What does 33c3:f101 most likely do?**
   It is the telemetry, status configuration, and static theme asset storage MCU (`DeviceCommunicationLibrary.dll`).
2. **What does 345f:* most likely do?**
   It is the native High-Speed USB video display controller (`MSDISPLAYSDKWRRAPER.dll`) responsible for real-time desktop frame streaming.
3. **Why does 33c3:f101 accept TX but never answer?**
   The USB SIE hardware layer is active and acknowledges USB bulk OUT packets (status 0), but the inner MCU application core is unpowered (missing auxiliary SATA/Molex power) or in standby.
4. **Why is 345f:* absent from lsusb?**
   Because the MacroSilicon display controller IC is unpowered (missing SATA/Molex power) or connected to an unplugged secondary USB header.
5. **Is there evidence for a second USB connection?**
   **YES (STRONGLY SUPPORTED)**. `MSUSBDisplay.inf` (`VID_345F&PID_9132`) and `MSDISPLAYSDKWRRAPER.dll` prove MacroSilicon is a native USB device separate from `33c3:f101`.
6. **Is there evidence for auxiliary power?**
   **YES (STRONGLY SUPPORTED)**. PC-case LCD screens with high-brightness backlights and dual controllers require 5V/12V SATA power beyond standard USB 500mA bus power.
7. **What single physical observation would most strongly confirm the architecture?**
   Inspecting the LCD module PCB for a SATA power connector or a MacroSilicon `MS9132` IC.
8. **What should we do next?**
   Perform physical wiring inspection of the PC-case LCD module per `NEXT_PHYSICAL_TEST.md`.
