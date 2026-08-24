#!/bin/bash
echo "=== KERNEL USBMON CAPTURE DURING MONO HARNESS EXECUTION ==="
sudo modprobe usbmon 2>/dev/null || true

# Bus 001, Device 002 (33c3:f101) -> usbmon1
if [ -c /dev/usbmon1 ]; then
    echo "Starting usbmon1 capture..."
    sudo timeout 6 cat /dev/usbmon1 > /home/tor/pc-case-lcd/raw_usbmon1.txt &
    MON_PID=$!
    sleep 0.5
    sudo mono /home/tor/vmax_bundle/bin/Release/test_vendor_api.exe /dev/ttyACM0
    wait $MON_PID 2>/dev/null || true
    echo "usbmon capture complete."
    grep -iE '33c3|f101| 1:002:' /home/tor/pc-case-lcd/raw_usbmon1.txt | head -50
else
    echo "usbmon1 device node not available."
fi
