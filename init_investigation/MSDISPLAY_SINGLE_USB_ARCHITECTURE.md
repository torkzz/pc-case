# MSDISPLAY SINGLE-USB ARCHITECTURE (`MSDISPLAY_SINGLE_USB_ARCHITECTURE.md`)

## Evidence Classification
- Physical Connection: [CONFIRMED LIVE]
- Panel Power & Initial rendering: [CONFIRMED LIVE]
- Dual Protocol Layering: [CONFIRMED STATIC]
- Mode Switching / Internal Hub: [STRONGLY SUPPORTED]

---

## 1. Physical Hardware Observation [CONFIRMED LIVE]
- **Cable Count**: Exactly ONE physical USB-C cable connects the LCD display module to the host PC motherboard.
- **Power Connectors**: NO SATA power, NO Molex power, NO barrel jack, NO secondary USB cable.
- **Power Delivery**: All power (5V USB rail) and high-speed data pass exclusively through the single USB-C cable.

---

## 2. Display Panel Lifecycle & Transition [CONFIRMED LIVE]

```
T0: USB-C cable plugged into host PC
    ↓
T1: LCD MCU powers up on USB 5V rail; panel backlight illuminates
    ↓
T2: Autonomous boot GIF plays from onboard SPI Flash (`0x08100000` / `Texture.acf`)
    ↓
T3: Static fallback image renders on panel
    ↓
T4: Horizontal corruption band / display transition occurs (MCU awaiting video stream)
    ↓
T5: Panel backlight auto-off / standby timeout (prevent panel burn-in if no stream received)
```

---

## 3. Internal Hardware Architecture Hypotheses [STRONGLY SUPPORTED]

1. **Integrated PCB with Shared USB Controller / Hub**:
   - The LCD panel contains an integrated MCU (`33c3:f101`) and a display controller IC (MacroSilicon / MS9132).
   - Both ICs share the single physical USB-C connector.
   - The CDC ACM MCU (`33c3:f101`) initializes first on USB power-up.

2. **Dynamic Interface / Endpoint Activation**:
   - The CDC ACM interface handles initial telemetry, asset transfers, and hardware status.
   - When active video streaming starts, the display transport streams video frames to Bulk OUT (Endpoint 0x02 or 0x04) or switches interface modes.
