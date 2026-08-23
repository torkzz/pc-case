# HL VMAX PC-Case LCD Display — Linux Native Driver & System Monitor

Native, high-performance Linux driver and real-time system stats telemetry monitor for **HL VMAX PC-Case LCD displays** (`33c3:f101`).

```
┌────────────────────────────┐
│       SYSTEM STATUS        │
├────────────────────────────┤
│ CPU UTILIZATION    24.5%   │
│ [██████████░░░░░░]         │
├────────────────────────────┤
│ GPU GRAPHICS       48°C    │
│ VRAM 4.2 / 12.0 GB         │
├────────────────────────────┤
│ RAM MEMORY         32.9%   │
│ 10.5 / 32.0 GB             │
├────────────────────────────┤
│ ROOT STORAGE       45.2%   │
│ 180.4 / 412.0 GB           │
├────────────────────────────┤
│ NETWORK TRAFFIC            │
│ RX: 2.4 MB/s | TX: 0.8 MB/s│
├────────────────────────────┤
│ UPTIME: 3d 14h 22m         │
└────────────────────────────┘
```

---

## Features
- **Zero Windows Dependencies**: Runs 100% natively on Linux via direct `usbfs` USB Bulk OUT transfers (`33c3:f101` Endpoint `0x02`).
- **460 × 1920 Native Resolution**: 1:4 Portrait layout customized for tall PC-case LCD panels.
- **Auto-Boot Service**: Systemd service auto-starts stats monitoring on system reboot.
- **Auto-Reconnect**: Robust against USB disconnects or kernel driver re-attachments.
- **Low Resource Overhead**: Uses fast in-memory PIL drawing (< 5% CPU usage).

---

## 🚀 Quick Setup (Automated)

Clone the repository and run `setup.sh`:

```bash
git clone git@github.com:torkzz/pc-case.git pc-case-lcd
cd pc-case-lcd
chmod +x setup.sh
./setup.sh
```

`setup.sh` automatically:
1. Creates Python virtual environment (`.venv`) and installs dependencies.
2. Configures udev rules (`/etc/udev/rules.d/99-vmax-lcd.rules`).
3. Installs and enables systemd boot service (`msdisplay-stats.service`).
4. Starts real-time system stats monitor immediately.

---

## 🎮 CLI Manual Usage

Run test patterns, solid colors, or custom images:

```bash
# Display 460x1920 Grid Test Pattern (3 columns x 4 rows)
sudo .venv/bin/python -m msdisplay.cli test-grid --duration 5

# Display Solid Color
sudo .venv/bin/python -m msdisplay.cli solid red --duration 5
sudo .venv/bin/python -m msdisplay.cli solid 0 255 0 --duration 5

# Display Custom Image
sudo .venv/bin/python -m msdisplay.cli image /path/to/picture.jpg --preserve-aspect --duration 5
```

---

## ⚙️ Managing the Background Service

```bash
# View service status
sudo systemctl status msdisplay-stats.service

# View live telemetry logs
sudo journalctl -u msdisplay-stats.service -f

# Stop background service
sudo systemctl stop msdisplay-stats.service

# Start background service
sudo systemctl start msdisplay-stats.service

# Disable auto-start on boot
sudo systemctl disable msdisplay-stats.service
```

---

## 🧪 Unit Tests

Run offline test suite without requiring hardware:

```bash
.venv/bin/python -m unittest discover tests
```

---

## 📜 License
MIT License.
