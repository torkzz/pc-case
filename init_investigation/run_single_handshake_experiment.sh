#!/bin/bash
set -e

echo "=== STEP 1: VERIFY DEVICE STATE ==="
lsusb -d 33c3:f101
ls -l /dev/ttyACM* /dev/serial/by-id/*HL* 2>/dev/null || true

echo -e "\n=== STEP 2: START USBMON CAPTURE ==="
sudo modprobe usbmon 2>/dev/null || true
rm -f /home/tor/pc-case-lcd/usbmon_handshake_test.txt

# Start usbmon capture in background
if [ -c /dev/usbmon1 ]; then
    sudo timeout 6 cat /dev/usbmon1 > /home/tor/pc-case-lcd/usbmon_handshake_test.txt &
    MON_PID=$!
    echo "Started usbmon1 capture (PID $MON_PID)"
else
    echo "usbmon1 not available"
    MON_PID=""
fi

sleep 0.5

echo -e "\n=== STEP 3: EXECUTE CONTROLLED HANDSHAKE DISPATCH ==="
sudo python3 /home/tor/pc-case-lcd/vmax_protocol.py --device /dev/ttyACM0 --handshake --send

if [ -n "$MON_PID" ]; then
    wait $MON_PID 2>/dev/null || true
    echo "usbmon capture finished."
fi

echo -e "\n=== STEP 4: ANALYZE USBMON CAPTURE ==="
if [ -f /home/tor/pc-case-lcd/usbmon_handshake_test.txt ]; then
    echo "usbmon line count: $(wc -l < /home/tor/pc-case-lcd/usbmon_handshake_test.txt)"
    echo "Raw URB entries for device 002:"
    grep -E ' 002:|1:002' /home/tor/pc-case-lcd/usbmon_handshake_test.txt | head -40 || true
fi
