#!/usr/bin/env bash
# ==============================================================================
# HL VMAX PC-Case LCD Display — Service Controller Script (`start.sh`)
# Starts or restarts the msdisplay-stats systemd service.
# ==============================================================================

set -e

SERVICE_NAME="msdisplay-stats.service"

echo "========================================================================"
echo "  Starting HL VMAX PC-Case LCD System Stats Monitor Service"
echo "========================================================================"

# Enable service if disabled
if ! systemctl is-enabled "${SERVICE_NAME}" &>/dev/null; then
    echo "Enabling ${SERVICE_NAME} auto-start..."
    sudo systemctl enable "${SERVICE_NAME}"
fi

# Restart/Start the service
echo "Starting ${SERVICE_NAME}..."
sudo systemctl restart "${SERVICE_NAME}"

echo ""
echo "[SUCCESS] ${SERVICE_NAME} started successfully."
echo "Current Service Status:"
sudo systemctl status "${SERVICE_NAME}" --no-pager -l || true
