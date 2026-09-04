content = """# Hardware & Architecture Investigation Report (`HARDWARE_ARCHITECTURE_INVESTIGATION.md`)

## Executive Summary
This report synthesizes all static, host-level, and wire-level evidence to reconstruct the physical hardware architecture and display transport path of the HL VMAX PC-Case LCD module.

---

## 1. Confirmed Facts & Technical Baseline

1. **Host USB TX & Endpoint Clearance (`WIRE_TX_CONFIRMED`)**:
   - Device `33c3:f101` enumerates as High-Speed (480Mbps) USB 2.0 IAD CDC ACM (`239/2/1`).
   - Linux kernel `cdc_acm` driver creates node `/dev/ttyACM0`.
   - Host USB controller submits 10-byte handshake frame (`41 48 00 02 00 80 00 00 4D 49`) to Bulk OUT Endpoint `0x02`.
   - `usbmon1` kernel tracing and direct `USBDEVFS_BULK` ioctls confirm completion status `0` (`10 bytes written`).

2. **Endpoint RX Timeout (`DEVICE_RESPONSE_NOT_OBSERVED`)**:
   - Direct `USBDEVFS_BULK` ioctls on Bulk IN Endpoint `0x81` return `-1` (errno 110: `Connection timed out`).
   - Interrupt IN Endpoint `0x83` produces no data.
   - The Linux `cdc_acm` driver and tty serial abstraction are **100% exonerated**; zero-byte RX occurs directly at the physical USB hardware endpoint level.

3. **Vendor Dual-Engine Architecture (`CONFIRMED STATIC`)**:
   - `Vmax.exe` (49 MB master application) embeds **two distinct display/communication engines**:
     - **`AICDisp` (`DeviceCommunicationLibrary.dll`)**: Targets `33c3:f101` over CDC ACM serial (`/dev/ttyACM0`). Handles telemetry, status config, and static asset storage (CMD `0x0082`).
     - **`MSDisplay` (`MSDISPLAYSDKWRRAPER.dll`)**: Native MacroSilicon C/C++ SDK driver targeting MacroSilicon USB Display Controllers (`345f:9132`, `345f:9133`, `345f:374a`, `345f:a101`). Handles real-time TurboJPEG desktop video frame streaming (`Wrraper_MSDisplaySendPicture`).

4. **Absent Video Controller (`HOST_USB_CONFIRMED`)**:
   - `lsusb -nn` and sysfs confirm `33c3:f101` (`HL-VMAX-USB-Device`) is present on Bus 001 (`1-9`).
   - No `345f:*` (MacroSilicon) device is currently enumerated on the USB bus.

---

## 2. Master System Architecture Map

```
Vmax.exe (Master Application)
  │
  ├── 1. Control & Telemetry Engine (AICDisp)
  │     │
  │     └── DeviceCommunicationLibrary.dll
  │            │
  │            └── Linux /dev/ttyACM0 (CDC ACM Serial, 115200 8N1)
  │                   │
  │                   └── 33c3:f101 MCU (Interface 0: EP 0x83 Int IN, Interface 1: EP 0x02 Bulk OUT, EP 0x81 Bulk IN)
  │                          │
  │                          └── Telemetry, Status Config, & Internal Flash Asset Storage (CMD 0x0082)
  │
  └── 2. Real-Time Video Display Engine (MSDisplay)
        │
        └── MSDISPLAYSDKWRRAPER.dll (TurboJPEG Compression)
               │
               └── Native USB Display Driver (MSUSBDisplay.inf / libusb0)
                      │
                      └── 345f:9132 / 345f:9133 / 345f:374a / 345f:a101 (MacroSilicon USB Display Controller IC)
                             │
                             └── Direct High-Speed Video Stream -> LCD Panel
```

---

## 3. Competing Hardware Architecture Hypotheses

### Hypothesis 1: Dual USB Connection / Secondary Header Missing
- **Description**: The PC-case LCD module contains two distinct ICs: `33c3:f101` (telemetry MCU) connected via micro-USB/Type-C, and `345f:9132` (MacroSilicon display controller) connected via a secondary internal 9-pin motherboard USB header or internal USB hub.
- **Evidence For**: `MSDISPLAYSDKWRRAPER.dll` and `MSUSBDisplay.inf` explicitly target `345f:9132` for video streaming. `Vmax.exe` calls `Wrraper_MSDisplayGetDeviceList` during startup.
- **Evidence Against**: `345f:9132` is not currently enumerated in `lsusb`.

### Hypothesis 2: Auxiliary Power Rail Disconnected (SATA/Molex 5V/12V)
- **Description**: The LCD board requires auxiliary power (SATA/Molex power cable from PC power supply) to supply 5V/12V to the LCD backlight, MCU application core, and MacroSilicon video IC. Without auxiliary power, USB bus power only energizes the USB SIE (Serial Interface Engine) of `33c3:f101`.
- **Evidence For**: Explains why `33c3:f101` USB SIE responds to USB setup and bulk OUT packets with status 0, but inner MCU core produces zero application RX bytes. Explains why MacroSilicon IC is unpowered and absent from USB enumeration.
- **Evidence Against**: Requires physical board inspection to verify.

### Hypothesis 3: MCU Core Held in Reset / Bootloader State
- **Description**: `33c3:f101` is stuck in an internal hardware bootloader or standby state waiting for a hardware pin pulse or firmware entry command.
- **Evidence For**: USB SIE responds to control and bulk OUT transfers while inner core remains silent.
- **Evidence Against**: Controlled test matrix of 12 command sequences (including `0x0070 Restart` and `0x0071 ChangeStatus`) produced no state transition.

---

## 4. Unanswered Questions & Highest-Value Physical PCB Tests

### Unanswered Questions
1. Is there an unplugged SATA or Molex power connector on the rear of the PC-case LCD module?
2. Does the LCD module PCB contain a secondary internal 9-pin motherboard USB header or USB-C connector for the MacroSilicon `345f:9132` video controller?
3. Is a MacroSilicon IC (e.g. MS9132 / MS9133) physically present on the LCD module PCB?

### Highest-Value Physical Tests
1. **Visual PCB Inspection**: Examine the LCD display PCB for IC markings (`MS9132`, `MS9133`, `STM32`, `GD32`, `CH340`, `Sonix`).
2. **Power Cable Verification**: Verify whether a SATA power or 4-pin Molex power cable is connected to the LCD module from the ATX power supply.
3. **USB Connector Inspection**: Check if the LCD module has two separate USB cables or a dual-connector internal header.

---

## 5. Physical Decision Tree

```mermaid
graph TD
    A[Physical PCB & Wiring Inspection] --> B{Auxiliary Power Connected?}
    B -- No --> C[Connect SATA/Molex Power Cable]
    C --> D[Check lsusb for 345f:9132 & Re-test ttyACM0 RX]
    B -- Yes --> E{Secondary USB Header Present?}
    E -- Yes --> F[Connect Secondary USB Header to Motherboard]
    F --> G[MacroSilicon 345f:9132 Enumerates -> Run MSDisplay Engine]
    E -- No --> H[Inspect Board for MacroSilicon IC & MCU UART Pins]
```
"""

with open("/home/tor/pc-case-lcd/HARDWARE_ARCHITECTURE_INVESTIGATION.md", "w") as f:
    f.write(content)

print("Generated /home/tor/pc-case-lcd/HARDWARE_ARCHITECTURE_INVESTIGATION.md")
