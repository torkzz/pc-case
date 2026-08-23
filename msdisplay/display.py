import time
from .usb import MSDisplayUSBDevice
from .protocol import build_frame_payload, DEFAULT_WIDTH, DEFAULT_HEIGHT, DEFAULT_STRIDE, DEFAULT_FLAG

class MSDisplayController:
    def __init__(self, device=None, width=DEFAULT_WIDTH, height=DEFAULT_HEIGHT):
        self.device = device or MSDisplayUSBDevice()
        self.width = width
        self.height = height

    def connect(self):
        self.device.connect()

    def close(self):
        self.device.close()

    def send_jpeg(self, jpeg_bytes, width=None, height=None, stride=0, flag=DEFAULT_FLAG):
        w = width or self.width
        h = height or self.height
        payload = build_frame_payload(jpeg_bytes, w, h, stride, flag)
        return self.device.send_bulk(payload)

    def show_image(self, image_input, preserve_aspect=False, duration=5.0, interval=1.0):
        img = prepare_image(image_input, self.width, self.height, preserve_aspect=preserve_aspect)
        jpeg_bytes = encode_jpeg(img)
        
        start = time.monotonic()
        while (time.monotonic() - start) < duration:
            self.send_jpeg(jpeg_bytes)
            time.sleep(interval)

    def solid_color(self, r, g, b, duration=5.0, interval=1.0):
        jpeg_bytes = create_solid_color_jpeg(r, g, b, self.width, self.height)
        start = time.monotonic()
        while (time.monotonic() - start) < duration:
            self.send_jpeg(jpeg_bytes)
            time.sleep(interval)

    def test_grid(self, duration=5.0, interval=1.0):
        jpeg_bytes = create_test_grid_jpeg(self.width, self.height)
        start = time.monotonic()
        while (time.monotonic() - start) < duration:
            self.send_jpeg(jpeg_bytes)
            time.sleep(interval)

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
