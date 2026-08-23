# 345F9132 ENUMERATION ANALYSIS (`345F9132_ENUMERATION_ANALYSIS.md`)

## Evidence Classification
- Target Hardware Identifiers in DLLs/INFs: [CONFIRMED STATIC]
- Current Host USB Topology (`lsusb`): [CONFIRMED LIVE]
- Enumeration Hypotheses: [STRONGLY SUPPORTED]

---

## 1. Why `345f:9132` is Absent on Current Linux Host [CONFIRMED LIVE & STATIC]

1. **Physical Cable Observation**: Physical inspection confirms a single USB-C cable powers and connects the LCD module to the host PC. [CONFIRMED LIVE]
2. **Current Device Enumeration**: `lsusb` shows `33c3:f101` (HL VMAX CDC ACM USB Device) active on USB bus 1 port 9. `345f:9132` is not listed in standard USB root hub device lists. [CONFIRMED LIVE]
3. **Hypotheses for Absence**:
   - **Hypothesis A (Dynamic Mode Switch)**: The CDC ACM MCU (`33c3:f101`) requires a specific vendor initialization sequence to power up or enable the MacroSilicon `345f:9132` IC on the internal USB bus. [STRONGLY SUPPORTED]
   - **Hypothesis B (Alternate VID/PID)**: The device on this hardware revision uses an alternate VID/PID (e.g. `345f:9133`, `345f:374a`, `345f:a101`) or presents as a secondary interface under `33c3:f101`. [PLAUSIBLE]
   - **Hypothesis C (Composite Interface / Driver Claim)**: The video endpoint is accessed via a alternate interface on the composite USB device when properly initialized. [PLAUSIBLE]
