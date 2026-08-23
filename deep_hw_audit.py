import os, sys, glob, subprocess

def run_cmd(cmd, timeout=10):
    try:
        res = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=timeout)
        return res.stdout.strip()
    except Exception as e:
        return f"Error/Timeout: {e}"

print("=== 1. MOTHERBOARD / DMI INFO ===")
print("Board Vendor:", run_cmd("cat /sys/class/dmi/id/board_vendor 2>/dev/null"))
print("Board Name  :", run_cmd("cat /sys/class/dmi/id/board_name 2>/dev/null"))
print("Board Ver   :", run_cmd("cat /sys/class/dmi/id/board_version 2>/dev/null"))
print("Sys Vendor  :", run_cmd("cat /sys/class/dmi/id/sys_vendor 2>/dev/null"))
print("Product Name:", run_cmd("cat /sys/class/dmi/id/product_name 2>/dev/null"))

print("\n=== 2. I2C / SMBUS / SPI / GPIO DEVICES ===")
print("I2C Adapters in /sys/class/i2c-adapter:")
for adapter in sorted(glob.glob('/sys/class/i2c-adapter/*')):
    name = run_cmd(f"cat {adapter}/name 2>/dev/null")
    target = os.readlink(adapter) if os.path.islink(adapter) else ""
    print(f"  {os.path.basename(adapter)}: '{name}' -> {target}")

print("\nRegistered I2C Devices in /sys/bus/i2c/devices:")
for idev in sorted(glob.glob('/sys/bus/i2c/devices/*')):
    name = run_cmd(f"cat {idev}/name 2>/dev/null")
    modalias = run_cmd(f"cat {idev}/modalias 2>/dev/null")
    print(f"  {os.path.basename(idev)}: name='{name}' modalias='{modalias}'")

print("\nSPI Devices:")
print("  /dev/spidev*:", glob.glob('/dev/spidev*'))
print("  /sys/bus/spi/devices:", glob.glob('/sys/bus/spi/devices/*'))

print("\nGPIO Controllers / Nodes:")
print("  /sys/class/gpio:", glob.glob('/sys/class/gpio/*'))

print("\n=== 3. ACPI / WMI INTERFACES ===")
print("WMI Devices:")
print(run_cmd("find /sys/devices -iname '*asus*' -o -iname '*wmi*' 2>/dev/null"))

print("\n=== 4. SERIAL / UART PORTS ===")
print("TTYS ports linked in /sys/class/tty:")
for tty in sorted(glob.glob('/sys/class/tty/ttyS*')):
    target = os.readlink(tty) if os.path.islink(tty) else ""
    # Filter out standard 8250 platform dummies if possible, or show real PCI/PNP serials
    if 'pnp' in target or 'pci' in target or 'platform' in target:
        print(f"  {os.path.basename(tty)} -> {target}")

print("\n=== 5. RELEVANT KERNEL MODULES (LSMOD) ===")
print(run_cmd("lsmod | grep -Ei 'asus|wmi|nct|i2c|smbus|gpio|spi|hid|panel|display|fb|drm'"))

print("\n=== 6. DRM CONNECTORS (DOUBLE CHECK) ===")
for conn in sorted(glob.glob('/sys/class/drm/card1-*')):
    cname = os.path.basename(conn)
    status = run_cmd(f"cat {conn}/status 2>/dev/null")
    enabled = run_cmd(f"cat {conn}/enabled 2>/dev/null")
    print(f"  {cname:<18}: status={status:<12} enabled={enabled}")

print("\n=== 7. VENDOR / CASE SOFTWARE SEARCH ===")
print("Searching pacman for vendor/case/display tools:")
print(run_cmd("pacman -Qs 'asus|rgb|lcd|screen|display|corsair|nzxt|lian|coolermaster|thermaltake|deepcool'"))

