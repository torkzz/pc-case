#!/bin/bash
set -e

echo "=== PHASE 1: DEVICE STATE VERIFICATION ==="
lsusb -d 33c3:f101 || true
ls -l /dev/ttyACM0 || true
readlink -f /dev/serial/by-id/usb-HL_VMAX_HL-VMAX-USB-Device-if00 || true
fuser -v /dev/ttyACM0 2>/dev/null || true

echo -e "\n=== PHASE 2: WINE PREFIX SETUP ==="
export WINEPREFIX=$HOME/.wine-vmax
export WINEARCH=win64

echo "Wine Version: $(wine --version)"
wineboot -u

echo -e "\n=== PHASE 3: COM PORT MAPPING ==="
mkdir -p "$WINEPREFIX/dosdevices"
ln -sf /dev/ttyACM0 "$WINEPREFIX/dosdevices/com1"
ls -l "$WINEPREFIX/dosdevices/com1"

echo -e "\n=== PHASE 4: VERIFY VMAX EXECUTABLE ==="
ls -lh /home/tor/vmax_bundle/bin/Release/Vmax.exe
file /home/tor/vmax_bundle/bin/Release/Vmax.exe
