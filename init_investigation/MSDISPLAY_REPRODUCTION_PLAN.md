# MSDisplay Linux Reproduction Plan (`MSDISPLAY_REPRODUCTION_PLAN.md`)

## Evidence Classification
- Target USB Transport & Architecture: [CONFIRMED STATIC]
- Host Topology & Device Status: [CONFIRMED LIVE]
- Control Payload Bytes & Packet Header: [UNKNOWN]

## Ranked Technical Strategies

1. **Option A: USBPcap Capture on Windows (`REQUIRED FOR 100% PROTOCOL RECOVERY`)**
   - Record genuine Windows Vmax startup using USBPcap / Wireshark on a Windows PC.
   - Extract exact raw USB setup packets, control transfers (SET_REPORT / GET_REPORT payload bytes), and Bulk OUT packet headers during `Wrraper_MSDisplayStart()` and `Wrraper_MSDisplaySendPicture()`.

2. **Option B: Reverse-Engineer Data Structures via Ghidra / IDA (`HIGH CONFIDENCE`)**
   - Decompile data structure allocation routines inside `MSDISPLAYSDKWRRAPER.dll` to reconstruct control transfer buffer fields.

3. **Option C: Linux Python/C `libusb-1.0` Driver Prototype (`READY FOR IMPLEMENTATION UPON PAYLOAD RECOVERY`)**
   - Build a Linux `libusb-1.0` script (`msdisplay_probe.py` / `msdisplay_driver.py`) that claims Interface 3 and streams TurboJPEG compressed frames to EP 0x04.
