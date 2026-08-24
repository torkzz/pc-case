import os, sys, time, fcntl, termios, select, struct, subprocess

DEV = "/dev/ttyACM0"

COMMANDS = {
    "TEST A (0x0070 Restart)": bytes.fromhex("41 48 00 02 00 70 00 00 4D 49"),
    "TEST B (0x0071 ChangeStatus)": bytes.fromhex("41 48 00 03 00 71 01 00 4D 49"),
    "TEST C (0x0072 HardwareInfo)": bytes.fromhex("41 48 00 02 00 72 00 00 4D 49"),
    "TEST D (0x0080 Handshake)": bytes.fromhex("41 48 00 02 00 80 00 00 4D 49"),
    "TEST E (0x0085 DownloadStatus)": bytes.fromhex("41 48 00 02 00 85 00 00 4D 49"),
}

def check_usb_devices():
    try:
        res = subprocess.run("lsusb -nn", shell=True, capture_output=True, text=True).stdout
        c33c3 = "33c3:f101" in res
        c345f = "345f" in res
        return c33c3, c345f, res.strip()
    except Exception as e:
        return False, False, str(e)

def run_experiment(test_name, frame):
    print(f"\n=======================================================")
    print(f"=== RUNNING CONTROLLED EXPERIMENT: {test_name} ===")
    print(f"=======================================================")
    
    # 1. Check pre-test USB state
    pre_33c3, pre_345f, pre_lsusb = check_usb_devices()
    print(f"Pre-Test USB State: 33c3:f101={pre_33c3}, 345f:*={pre_345f}")
    
    # 2. Open serial port & transmit exactly ONE frame
    try:
        fd = os.open(DEV, os.O_RDWR | os.O_NOCTTY | os.O_NONBLOCK)
        attrs = termios.tcgetattr(fd)
        attrs[0], attrs[1] = 0, 0
        attrs[2] = termios.B115200 | termios.CS8 | termios.CREAD | termios.CLOCAL
        attrs[3] = 0
        termios.tcsetattr(fd, termios.TCSANOW, attrs)

        TIOCMSET = 0x5418
        fcntl.ioctl(fd, TIOCMSET, struct.pack('I', 0x002 | 0x004)) # DTR+RTS
        termios.tcflush(fd, termios.TCIOFLUSH)

        print(f"TX ({len(frame)}B): {frame.hex(' ')}")
        os.write(fd, frame)
        os.close(fd)
    except Exception as e:
        print(f"Transmission Exception: {e}")
        return False

    # 3. Monitor for 345f:* enumeration at intervals (100ms, 500ms, 1s, 5s)
    delays = [0.1, 0.4, 0.5, 4.0]
    total_elapsed = 0
    enumerated_345f = False

    for d in delays:
        time.sleep(d)
        total_elapsed += d
        c33c3, c345f, _ = check_usb_devices()
        print(f"  T+{total_elapsed:.1f}s Check: 33c3:f101={c33c3}, 345f:*={c345f}")
        if c345f:
            print(f"*** CRITICAL DISCOVERY: 345f:* ENUMERATED AT T+{total_elapsed:.1f}s AFTER {test_name}! ***")
            enumerated_345f = True
            break

    return enumerated_345f

experiment_results = {}
for name, frame in COMMANDS.items():
    found = run_experiment(name, frame)
    experiment_results[name] = found
    if found:
        print("\n*** STOPPING ALL EXPERIMENTS: MACROSILICON DEVICE ENUMERATED! ***")
        sys.exit(0)
    time.sleep(1.0) # Settle delay between experiments

print("\n=== CONTROLLED STATE-TRANSITION EXPERIMENTS COMPLETE ===")
for k, v in experiment_results.items():
    print(f"  {k}: 345f Enumerated = {v}")

