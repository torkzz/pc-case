#!/usr/bin/env python3
"""
MSDisplay Real-Time System Monitoring Dashboard Application (`msdisplay_system_stats.py`)

Production Architecture:
- Collects Linux system metrics (CPU, RAM, GPU, Disk, Net, Temp, Uptime).
- Renders 480x1920 1:4 Portrait Dashboard image via PIL.
- Encodes payload via TurboJPEG (subsampling=0, YUV 4:4:4).
- Transmits payload over USB Bulk OUT (33c3:f101 EP 0x02) via MSDisplayController.
- Auto-reconnects on USB disconnect/reconnect.
- Guaranteed keep-alive interval < 4.0s.
"""

import sys
import argparse
import logging
from msdisplay.dashboard import MSDisplayDashboard

def main():
    parser = argparse.ArgumentParser(description="MSDisplay Real-Time System Monitoring Dashboard")
    parser.add_argument('--interval', type=float, default=1.0, help="Metrics & Display refresh interval in seconds (default: 1.0)")
    parser.add_argument('--duration', type=float, default=None, help="Run duration in seconds (default: infinite / until Ctrl+C)")
    parser.add_argument('--quality', type=int, default=95, help="JPEG compression quality (default: 95)")
    parser.add_argument('--debug', action='store_true', help="Enable debug logging")
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.DEBUG if args.debug else logging.INFO,
        format='%(message)s'
    )

    dashboard = MSDisplayDashboard(update_interval=args.interval, jpeg_quality=args.quality)
    try:
        dashboard.run(duration_sec=args.duration)
    except KeyboardInterrupt:
        print("\n[STATUS] Dashboard stopped by user.")
    finally:
        dashboard.cleanup()

if __name__ == "__main__":
    main()
