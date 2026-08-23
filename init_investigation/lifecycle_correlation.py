#!/usr/bin/env python3
"""
lifecycle_correlation.py
Automated timestamped USB/TTY lifecycle monitor for HL VMAX LCD (33c3:f101).

Monitors:
- Host USB device enumeration (33c3:f101)
- Serial port device presence (/dev/ttyACM0)
- Kernel events (dmesg)
- Timestamped lifecycle log (T0: plug, T1: GIF, T2: image, T3: shutdown)
"""

import sys
import os
import time
import json
import subprocess

TARGET_VID_PID = "33c3:f101"
TARGET_PORT = "/dev/ttyACM0"
OUTPUT_DIR = "/home/tor/pc-case-lcd/init_investigation"

def check_usb_connected():
    try:
        res = subprocess.run(["lsusb", "-d", TARGET_VID_PID], capture_output=True, text=True)
        return res.returncode == 0
    except:
        return False

def check_tty_present():
    return os.path.exists(TARGET_PORT)

def get_dmesg_tail(lines=30):
    try:
        res = subprocess.run(["dmesg", "--ctime"], capture_output=True, text=True)
        lines_list = res.stdout.splitlines()
        return lines_list[-lines:] if lines_list else []
    except:
        return []

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    print("=" * 70)
    print("AUTOMATED USB & TTY LIFECYCLE MONITOR")
    print("=" * 70)
    print(f"TARGET DEVICE: {TARGET_VID_PID}")
    print(f"TARGET PORT:   {TARGET_PORT}")
    print()

    print("Starting continuous observation log...")
    print("----------------------------------------------------------------------")
    print("Timestamp    | USB State     | TTY State | Log Entry")
    print("----------------------------------------------------------------------")

    timeline = []
    start_time = time.time()

    prev_usb = None
    prev_tty = None

    try:
        # Observe for up to 60 seconds
        deadline = start_time + 60.0
        while time.time() < deadline:
            t_now = time.time()
            t_rel = t_now - start_time
            t_str = time.strftime("%H:%M:%S", time.localtime(t_now)) + f".{int((t_now % 1) * 1000):03d}"

            usb_curr = check_usb_connected()
            tty_curr = check_tty_present()

            state_change = (usb_curr != prev_usb) or (tty_curr != prev_tty)

            if state_change or len(timeline) == 0:
                usb_status = "CONNECTED" if usb_curr else "GONE     "
                tty_status = "YES" if tty_curr else "NO "

                log_entry = f"{t_str} | USB={usb_status} | TTY={tty_status} | (rel: {t_rel:.2f}s)"
                print(log_entry)

                timeline.append({
                    "timestamp": t_str,
                    "rel_s": round(t_rel, 3),
                    "usb_connected": usb_curr,
                    "tty_present": tty_curr
                })

                prev_usb = usb_curr
                prev_tty = tty_curr

            time.sleep(0.2)

    except KeyboardInterrupt:
        print("\nMonitor stopped by user.")

    end_time = time.time()
    total_elapsed = end_time - start_time

    # Determine Case Classification
    usb_at_end = check_usb_connected()
    tty_at_end = check_tty_present()

    classification = "UNKNOWN"
    if usb_at_end and tty_at_end:
        classification = "DISPLAY_APPLICATION_SHUTDOWN (CASE A: USB & TTY stay alive)"
    elif not usb_at_end and not tty_at_end:
        classification = "DEVICE_POWER_OR_RESET_SHUTDOWN (CASE B: Total USB drop)"

    summary = {
        "start_time": time.ctime(start_time),
        "end_time": time.ctime(end_time),
        "duration_s": round(total_elapsed, 2),
        "timeline_events": timeline,
        "final_classification": classification,
        "dmesg_sample": get_dmesg_tail(20)
    }

    out_json = os.path.join(OUTPUT_DIR, "lifecycle_correlation.json")
    with open(out_json, "w") as f:
        json.dump(summary, f, indent=2)

    out_md = os.path.join(OUTPUT_DIR, "lifecycle_correlation.md")
    with open(out_md, "w") as f:
        f.write("# USB & TTY Lifecycle Correlation Report\n\n")
        f.write(f"**Duration**: `{summary['duration_s']}s`\n")
        f.write(f"**Final Classification**: `{classification}`\n\n")
        f.write("## Timestamped Lifecycle Events\n")
        f.write("| Timestamp | Rel Time (s) | USB Connected | TTY Present |\n")
        f.write("|---|---|---|---|\n")
        for e in timeline:
            f.write(f"| `{e['timestamp']}` | `{e['rel_s']}` | `{e['usb_connected']}` | `{e['tty_present']}` |\n")

    print()
    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(f"Final Classification: {classification}")
    print(f"Saved report to: {out_json} and {out_md}")

if __name__ == "__main__":
    main()
