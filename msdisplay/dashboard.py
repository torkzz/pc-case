import sys
import time
import logging
from .metrics import SystemMetricsCollector
from .renderer import DashboardRenderer
from .jpeg import encode_jpeg
from .display import MSDisplayController
from .usb import MSDisplayUSBDevice

logger = logging.getLogger("msdisplay")

DEFAULT_UPDATE_INTERVAL = 1.0
DEFAULT_RECONNECT_INTERVAL = 2.0
KEEP_ALIVE_MAX_INTERVAL = 3.5

class MSDisplayDashboard:
    def __init__(self, update_interval=DEFAULT_UPDATE_INTERVAL, jpeg_quality=95, reconnect_interval=DEFAULT_RECONNECT_INTERVAL):
        self.update_interval = min(update_interval, KEEP_ALIVE_MAX_INTERVAL)
        self.jpeg_quality = jpeg_quality
        self.reconnect_interval = reconnect_interval
        
        self.collector = SystemMetricsCollector()
        self.renderer = DashboardRenderer()
        self.controller = None

    def run(self, duration_sec=None):
        print("=== Starting MSDisplay Real-Time System Monitor Dashboard ===")
        print(f"  Target Resolution: 460 x 1920 (1:4 Portrait)")
        print(f"  Update Interval  : {self.update_interval:.1f}s (Keep-Alive Guaranteed < 4.0s)")
        print(f"  JPEG Quality     : {self.jpeg_quality}")

        start_time = time.monotonic()
        frame_seq = 1

        while True:
            if duration_sec and (time.monotonic() - start_time) >= duration_sec:
                print(f"\n[COMPLETED] Reached run duration of {duration_sec}s.")
                break

            # 1. Collect telemetry metrics
            try:
                metrics_data = self.collector.collect_all()
            except Exception as e:
                print(f"[WARN] Metrics collection error: {e}")
                metrics_data = self.collector.collect_all()

            # 2. Render 480x1920 RGB Image
            img = self.renderer.render(metrics_data)

            # 3. Encode to TurboJPEG payload
            jpeg_bytes = encode_jpeg(img, quality=self.jpeg_quality, subsampling=0)

            # 4. Transmit over USB with auto-reconnect logic
            transmitted = False
            while not transmitted:
                if duration_sec and (time.monotonic() - start_time) >= duration_sec:
                    break

                try:
                    if self.controller is None:
                        dev = MSDisplayUSBDevice()
                        self.controller = MSDisplayController(device=dev)
                        self.controller.connect()
                        print("[USB] Successfully connected to 33c3:f101 device.")

                    res = self.controller.send_jpeg(jpeg_bytes)
                    ts = time.strftime("%H:%M:%S")
                    cpu_u = metrics_data['cpu']['utilization']
                    ram_u = metrics_data['ram']['pct']
                    gpu_u = metrics_data['gpu']['utilization'] if metrics_data['gpu'] else 0.0
                    logger.debug(f"[{ts}] Frame #{frame_seq:04d} ({len(jpeg_bytes)}B JPG, {res}B Tx) -> CPU: {cpu_u:.1f}% | RAM: {ram_u:.1f}% | GPU: {gpu_u:.1f}% | OK")
                    frame_seq += 1
                    transmitted = True
                except Exception as e:
                    print(f"[USB DISCONNECT / ERROR] {e}. Reconnecting in {self.reconnect_interval:.1f}s...")
                    if self.controller is not None:
                        try:
                            self.controller.close()
                        except Exception:
                            pass
                        self.controller = None
                    time.sleep(self.reconnect_interval)

            time.sleep(self.update_interval)

        self.cleanup()

    def cleanup(self):
        if self.controller is not None:
            try:
                self.controller.close()
            except Exception:
                pass
            self.controller = None
