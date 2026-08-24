#!/bin/bash
export WINEPREFIX=$HOME/.wine-vmax

echo "=== TESTING VMAX LAUNCHER UNDER WINE ==="
timeout 5 wine /home/tor/vmax_bundle/Launcher/Vmax.Launcher.exe 2>&1 | head -30
