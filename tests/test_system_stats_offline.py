import unittest
from PIL import Image

from msdisplay.metrics import SystemMetricsCollector, RingBuffer
from msdisplay.renderer import DashboardRenderer
from msdisplay.jpeg import encode_jpeg

class TestSystemStatsOffline(unittest.TestCase):

    def test_ring_buffer(self):
        rb = RingBuffer(maxlen=5)
        for i in range(10):
            rb.append(i)
        self.assertEqual(len(rb), 5)
        self.assertEqual(rb.get_list(), [5, 6, 7, 8, 9])

    def test_metrics_collection_offline(self):
        collector = SystemMetricsCollector(history_len=10)
        metrics = collector.collect_all()
        
        self.assertIn('cpu', metrics)
        self.assertIn('ram', metrics)
        self.assertIn('gpu', metrics) # None if no NVIDIA GPU
        self.assertIn('storage', metrics)
        self.assertIn('net', metrics)
        self.assertIn('sys_info', metrics)
        self.assertIn('history', metrics)
        
        self.assertGreaterEqual(metrics['cpu']['utilization'], 0.0)
        self.assertGreaterEqual(metrics['ram']['pct'], 0.0)
        self.assertGreaterEqual(metrics['storage']['pct'], 0.0)

    def test_renderer_dimensions(self):
        collector = SystemMetricsCollector(history_len=10)
        metrics = collector.collect_all()
        
        renderer = DashboardRenderer(width=460, height=1920)
        img = renderer.render(metrics)
        
        self.assertIsInstance(img, Image.Image)
        self.assertEqual(img.size, (460, 1920))
        self.assertEqual(img.mode, 'RGB')

    def test_jpeg_encoding(self):
        collector = SystemMetricsCollector(history_len=10)
        metrics = collector.collect_all()
        
        renderer = DashboardRenderer(width=460, height=1920)
        img = renderer.render(metrics)
        
        jpeg_bytes = encode_jpeg(img, quality=95, subsampling=0)
        self.assertTrue(jpeg_bytes.startswith(b'\xff\xd8'))
        self.assertGreater(len(jpeg_bytes), 1000)

if __name__ == "__main__":
    unittest.main()
