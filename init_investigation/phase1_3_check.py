import subprocess
import os
import sys

def run_cmd(cmd):
    try:
        res = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=10)
        return res.stdout.strip()
    except Exception as e:
        return f"Error: {e}"

print("=== PHASE 1: DESCRIPTOR & KERNEL BINDINGS ===")
print("lsusb -d 33c3:f101 -v:")
print(run_cmd("lsusb -d 33c3:f101 -v"))

print("\nlsusb -t:")
print(run_cmd("lsusb -t"))

print("\nfuser /dev/ttyACM0:")
print(run_cmd("sudo fuser -v /dev/ttyACM0 2>&1"))

print("\nlsof /dev/ttyACM0:")
print(run_cmd("sudo lsof /dev/ttyACM0 2>&1"))

print("\nInterface drivers:")
print("  Interface 0 driver:", run_cmd("readlink -f /sys/bus/usb/devices/1-9:1.0/driver 2>/dev/null"))
print("  Interface 1 driver:", run_cmd("readlink -f /sys/bus/usb/devices/1-9:1.1/driver 2>/dev/null"))

