# Immediate Next Physical Test & Checklist (`NEXT_PHYSICAL_TEST.md`)

## Highest-Value Inspection Steps

### Step 1: External Power Cable Verification
- Check the rear of the PC-case LCD panel module for an unconnected **SATA power** or **4-pin Molex power** connector.
- Reason: USB bus power (500mA) may only energize the `33c3:f101` USB SIE, leaving the main MCU application core and MacroSilicon `345f:9132` video IC unpowered.

### Step 2: Secondary USB Connector / Header Check
- Check if the LCD module has **two separate USB cables** or an internal motherboard **9-pin USB header**.
- Reason: Vendor software `Vmax.exe` embeds two separate engines: `MSDisplay` for MacroSilicon `345f:9132` video transport, and `AICDisp` for `33c3:f101` telemetry control.

### Step 3: PCB Visual IC Inspection
If the LCD back cover can be safely removed, inspect the IC chip markings:
- Look for **MacroSilicon** chips: `MS9132`, `MS9133`, `MS374A`.
- Look for **Control MCU** chips: `STM32`, `GD32`, `Sonix`, `CH340`.
- Look for **USB Hub** ICs: `Realtek RTS5411`, `Genesys Logic GL850G`.

---

## Immediate Next Action

Inspect the rear wiring of the PC-case LCD module and verify whether a SATA or Molex auxiliary power connector is attached to the PC power supply.
