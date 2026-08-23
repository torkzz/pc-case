#!/usr/bin/env bash
# ==============================================================================
# HL VMAX PC-Case LCD Display Auto-Setup Script
# Configures Python environment, udev rules, systemd boot service.
# ==============================================================================

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV_DIR="${SCRIPT_DIR}/.venv"
SERVICE_NAME="msdisplay-stats.service"
UDEV_RULE_FILE="/etc/udev/rules.d/99-vmax-lcd.rules"
SYSTEMD_SERVICE_FILE="/etc/systemd/system/${SERVICE_NAME}"

echo "========================================================================"
echo "  HL VMAX PC-Case LCD Driver & System Monitor Automated Setup"
echo "========================================================================"
echo "Working Directory: ${SCRIPT_DIR}"
echo ""

# 1. Check Python 3
if ! command -v python3 &> /dev/null; then
    echo "[ERROR] python3 is required but not installed."
    exit 1
fi

# 2. Setup Virtual Environment
if [ ! -d "${VENV_DIR}" ]; then
    echo "[1/4] Creating Python virtual environment in .venv..."
    python3 -m venv "${VENV_DIR}"
else
    echo "[1/4] Python virtual environment already exists in .venv."
fi

echo "Installing/updating dependencies (Pillow)..."
"${VENV_DIR}/bin/pip" install --quiet --upgrade pip Pillow

# 3. Create udev Rules
echo "[2/4] Setting up udev USB permissions rule..."
sudo bash -c "cat << 'EOF' > ${UDEV_RULE_FILE}
SUBSYSTEM==\"usb\", ATTR{idVendor}==\"33c3\", ATTR{idProduct}==\"f101\", MODE=\"0666\", GROUP=\"users\"
EOF"

echo "Reloading udev rules..."
sudo udevadm control --reload-rules
sudo udevadm trigger

# 4. Create systemd System Service
echo "[3/4] Creating systemd service for boot auto-start..."
sudo bash -c "cat << EOF > ${SYSTEMD_SERVICE_FILE}
[Unit]
Description=HL VMAX PC-Case LCD Real-Time System Monitor Service
After=multi-user.target network.target

[Service]
Type=simple
User=root
WorkingDirectory=${SCRIPT_DIR}
ExecStart=${VENV_DIR}/bin/python ${SCRIPT_DIR}/msdisplay_system_stats.py
Restart=always
RestartSec=3

[Install]
WantedBy=multi-user.target
EOF"

# 5. Enable and Start Systemd Service
echo "[4/4] Enabling and starting systemd service..."
sudo systemctl daemon-reload
sudo systemctl enable "${SERVICE_NAME}"
sudo systemctl restart "${SERVICE_NAME}"

echo ""
echo "========================================================================"
echo "  [SUCCESS] HL VMAX LCD System Monitor is installed and running!"
echo "========================================================================"
echo "Service Status:"
sudo systemctl status "${SERVICE_NAME}" --no-pager -l || true
echo ""
echo "Useful Commands:"
echo "  View status : sudo systemctl status ${SERVICE_NAME}"
echo "  View logs   : sudo journalctl -u ${SERVICE_NAME} -f"
echo "  Stop service: sudo systemctl stop ${SERVICE_NAME}"
echo "  Start service: sudo systemctl start ${SERVICE_NAME}"
