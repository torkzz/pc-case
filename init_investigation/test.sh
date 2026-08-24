cd /home/tor/pc-case-lcd

sudo modprobe usbmon

# Identify VMAX
lsusb -d 33c3:f101

# Start capture
sudo sh -c 'cat /sys/kernel/debug/usb/usbmon/1u > /tmp/vmax-usbmon.txt' &
USBMON_PID=$!

sleep 1

# Run controlled experiment
.venv/bin/python3 init_investigation/exit_handshake_test.py --send --timeout 5.0

sleep 2

# Stop capture
sudo kill "$USBMON_PID" 2>/dev/null
wait "$USBMON_PID" 2>/dev/null || true

# Kernel messages
sudo dmesg --ctime | tail -100 > /tmp/vmax-dmesg.txt

echo "=== USB CAPTURE ==="
wc -l /tmp/vmax-usbmon.txt
ls -lh /tmp/vmax-usbmon.txt

echo
echo "=== DEVICE ==="
lsusb -d 33c3:f101

echo
echo "=== TEST FRAMES ==="
grep -nEi '41480002006300004d49|41480002008000004d49' \
    /tmp/vmax-usbmon.txt || true

echo
echo "=== KERNEL ==="
cat /tmp/vmax-dmesg.txt
