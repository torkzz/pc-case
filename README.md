# HL VMAX PC-Case LCD Display — Cyberpunk HUD Linux Driver & Telemetry Monitor

Native, high-performance Linux driver, rendering engine, and real-time cyberpunk HUD telemetry monitor for **HL VMAX PC-Case LCD displays** (`33c3:f101`).

```
┌─────────────────────────────────────────┐
│ [CPU] NECTARINES       12:34:56        │
│ UPTIME: 1d 4h | IP: 192.168.1.150       │
├─────────────────────────────────────────┤
│ [CPU] 45.2%                  TEMP: 54°C │
│ LOAD: 1.25   0.98   0.84                │
│ [████████████████░░░░░░░░░░░░░░░░░░░]   │
│ [ ~~~ Live Oscilloscope Graph ~~~ ]     │
├─────────────────────────────────────────┤
│ [GPU] 68.4%                  TEMP: 65°C │
│ VRAM: 4.2 / 12.0 GB (35.0%)             │
│ [ ~~~ Live Oscilloscope Graph ~~~ ]     │
├─────────────────────────────────────────┤
│ [RAM] 42.8%           13.7 / 32.0 GB    │
│ [ ::: 100-Dot Matrix Telemetry Grid :::]│
├─────────────────────────────────────────┤
│ [DISK] ROOT (/): 282.0 / 413.8 GB (68%) │
├─────────────────────────────────────────┤
│ [NET] ↓ 126.5 KB/s      ↑ 1.2 MB/s      │
│ [ ~~~ Dual-Line RX/TX Telemetry ~~~ ]   │
├─────────────────────────────────────────┤
│ Torkzz                                  │
└─────────────────────────────────────────┘
```

---

## 🔒 License & Usage Notice

**PROPRIETARY SOFTWARE — NOT AUTHORIZED FOR DISTRIBUTION.**  
Copyright (c) 2026. All Rights Reserved. See [LICENSE](LICENSE) for terms.  
*Distribution, redistribution, publication, hosting, or sharing of this codebase or derivative works is strictly prohibited.*

---

## 🚀 Quick Setup & Execution

Clone the repository and execute `setup.sh`:

```bash
git clone git@github.com:torkzz/pc-case.git pc-case-lcd
cd pc-case-lcd
chmod +x setup.sh start.sh
./setup.sh
```

To quickly start/restart the service at any time:

```bash
./start.sh
```

`setup.sh` automatically:
1. Creates the Python virtual environment (`.venv`) and installs Pillow (`PIL`) dependencies.
2. Configures udev permission rules (`/etc/udev/rules.d/99-vmax-lcd.rules`).
3. Installs and registers the systemd service (`msdisplay-stats.service`).
4. Launches the real-time cyberpunk telemetry dashboard daemon.

---

## 🛠️ Architecture & Core Components

```
pc-case-lcd/
├── msdisplay_system_stats.py   # Systemd entrypoint & CLI executable daemon
├── msdisplay-stats.service     # Systemd boot service definition
├── setup.sh                    # Automated installer & environment provisioner
├── start.sh                    # Service launcher / restarter
└── msdisplay/
    ├── dashboard.py            # Main refresh loop & USB auto-reconnect coordinator
    ├── metrics.py              # Real-time Linux telemetry collector (/proc & /sys)
    ├── renderer.py             # PIL-based Cyberpunk HUD rendering engine
    ├── display.py              # High-level LCD controller
    ├── usb.py                  # Direct Linux usbfs bulk OUT transfer layer
    ├── protocol.py             # MSDisplay 12-byte framing header packer
    └── jpeg.py                 # TurboJPEG / PIL encoder pipeline
```

---

## 🎨 Customizing the Cyberpunk HUD Renderer (`msdisplay/renderer.py`)

All visual UI elements are rendered programmatically via `msdisplay/renderer.py` at `460 × 1920` native resolution.

### 1. Modifying Theme Colors

Color definitions are centralized in `DashboardRenderer.render()` inside `msdisplay/renderer.py`:

```python
# Color Palette Constants (RGB Tuples)
CYAN_ACCENT = (0, 255, 240)    # Electric Cyan
CYAN_TEXT   = (0, 220, 240)    # Primary Cyan Text
CYAN_DIM    = (0, 140, 160)    # Dim Cyan Dividers & Borders
NEON_PINK   = (255, 0, 128)    # Hot Magenta / Neon Pink Highlights
GLOW_PINK   = (130, 0, 65)     # Glowing Text Backdrops
```

To adjust colors, edit `msdisplay/renderer.py` and restart the background daemon:

```bash
sudo systemctl restart msdisplay-stats.service
```

### 2. Customizing Glitch Effects & Animation

The `draw_glitch_text()` method in `msdisplay/renderer.py` controls the 12 FPS quantum glitch loop:

* **Frequency**: `quantum % 37 in (0, 1)` (Triggers glitch every ~3 seconds).
* **Displacement**: `dx, dy` offsets up to ±3 pixels.
* **Glitch Palette**: Dynamically picks between Neon Purple `(220, 60, 255)`, Neon Green `(0, 255, 128)`, and Bright Green `(50, 255, 50)`.

### 3. Customizing Footer Identity

To change the footer marquee name (default: `"Torkzz"`), edit line ~377 in `msdisplay/renderer.py`:

```python
self.draw_glitch_text(draw, (x0 + 28, 1839), "YOUR_NAME", self.font_title, base_color=CYAN_TEXT, quantum_offset=33)
```

---

## 🎮 Manual CLI Commands

Run test patterns, custom colors, or specific display modes:

```bash
# Debug logging mode (prints frame size without flooding journald)
python3 msdisplay_system_stats.py --debug --interval 1.0

# Display 460x1920 test grid
sudo .venv/bin/python -m msdisplay.cli test-grid --duration 5

# Display solid color background
sudo .venv/bin/python -m msdisplay.cli solid red --duration 5

# Display custom image file
sudo .venv/bin/python -m msdisplay.cli image /path/to/image.png --preserve-aspect --duration 5
```

---

## ⚙️ Managing the Background Daemon

```bash
# Check service status
sudo systemctl status msdisplay-stats.service

# View live systemd logs (logging set to quiet debug)
sudo journalctl -u msdisplay-stats.service -f

# Restart daemon after editing renderer code
sudo systemctl restart msdisplay-stats.service

# Stop daemon
sudo systemctl stop msdisplay-stats.service
```

---

## 🧪 Running Unit Tests

Run the test suite offline without requiring physical LCD hardware attached:

```bash
.venv/bin/python -m unittest discover tests
```

---

## 🔬 Hardware Protocol Architecture

* **Device Hardware:** VID `0x33c3` (`HL VMAX`), PID `0xf101`
* **USB Interface:** CDC Data Pipe / Endpoint `0x02` Bulk OUT
* **Native Resolution:** `460 × 1920` (1:4 Portrait aspect ratio)
* **Keep-Alive Interval:** `<= 3.5s` required frame update rate to keep display active.
