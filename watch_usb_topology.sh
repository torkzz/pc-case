#!/bin/bash
# Continuous Linux USB Topology & Enumeration Watcher

LOG_FILE="/home/tor/pc-case-lcd/usb_topology_watcher.log"

echo "=== USB TOPOLOGY WATCHER STARTED AT $(date) ===" > "$LOG_FILE"

while true; do
    TS=$(date +"%Y-%m-%d %H:%M:%S.%3N")
    echo "[$TS] --- USB DEVICES ---" >> "$LOG_FILE"
    lsusb -nn >> "$LOG_FILE"
    
    # Check specifically for 345f MacroSilicon devices
    MS_DEV=$(lsusb -nn | grep -i "345f")
    if [ -n "$MS_DEV" ]; then
        echo "[$TS] *** MACROSILICON DEVICE DETECTED: $MS_DEV ***" >> "$LOG_FILE"
        echo "[$TS] *** MACROSILICON DEVICE DETECTED: $MS_DEV ***"
    fi
    
    sleep 0.2
done
