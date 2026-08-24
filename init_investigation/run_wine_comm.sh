#!/bin/bash
export WINEPREFIX=$HOME/.wine-vmax
export WINEDEBUG=+comm

echo "=== RUNNING VMAX UNDER WINE WITH COMM LOGGING ==="
timeout 10 wine /home/tor/vmax_bundle/bin/Release/Vmax.exe 2>&1 | tee /home/tor/pc-case-lcd/wine_vmax_comm.log || true
