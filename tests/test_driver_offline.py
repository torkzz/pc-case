import unittest
import struct
from PIL import Image

from msdisplay.protocol import pack_msdisplay_header, build_frame_payload, DEFAULT_WIDTH, DEFAULT_HEIGHT
from msdisplay.jpeg import prepare_image, encode_jpeg, create_solid_color_jpeg, create_test_grid_jpeg

class TestMSDisplayDriverOffline(unittest.TestCase):

    def test_header_packing(self):
        hdr = pack_msdisplay_header(460, 1920, 0, 1)
        self.assertEqual(len(hdr), 12)
        magic, w, h, stride, flag = struct.unpack("<IHHHH", hdr)
        self.assertEqual(magic, 0x0008100A)
        self.assertEqual(w, 460)
        self.assertEqual(h, 1920)
        self.assertEqual(stride, 0)
        self.assertEqual(flag, 1)

    def test_header_hex_signature(self):
        hdr = pack_msdisplay_header(460, 1920, 0, 1)
        self.assertEqual(hdr.hex(), "0a100800cc01800700000100")

    def test_payload_building(self):
        dummy_jpeg = b"\xff\xd8\xff\xe0\x00\x10JFIF"
        payload = build_frame_payload(dummy_jpeg, 460, 1920)
        self.assertEqual(len(payload), 12 + len(dummy_jpeg))
        self.assertTrue(payload.startswith(b"\x0a\x10\x08\x00"))
        self.assertEqual(payload[12:14], b"\xff\xd8")

    def test_invalid_jpeg_payload_raises(self):
        invalid_bytes = b"NOT_A_JPEG"
        with self.assertRaises(ValueError):
            build_frame_payload(invalid_bytes, 480, 1920)

    def test_image_preparation_cropping(self):
        wide_img = Image.new("RGB", (640, 1920), (255, 0, 0))
        prepared = prepare_image(wide_img, width=460, height=1920)
        self.assertEqual(prepared.size, (460, 1920))

    def test_image_preparation_preserve_aspect(self):
        wide_img = Image.new("RGB", (640, 1920), (0, 255, 0))
        prepared = prepare_image(wide_img, width=460, height=1920, preserve_aspect=True)
        self.assertEqual(prepared.size, (460, 1920))

    def test_jpeg_encoding(self):
        img = Image.new("RGB", (460, 1920), (0, 0, 255))
        jpeg_bytes = encode_jpeg(img, quality=95, subsampling=0)
        self.assertTrue(jpeg_bytes.startswith(b"\xff\xd8"))

    def test_solid_color_jpeg(self):
        jpeg_bytes = create_solid_color_jpeg(255, 0, 0)
        self.assertTrue(jpeg_bytes.startswith(b"\xff\xd8"))

    def test_test_grid_jpeg(self):
        jpeg_bytes = create_test_grid_jpeg()
        self.assertTrue(jpeg_bytes.startswith(b"\xff\xd8"))

if __name__ == "__main__":
    unittest.main()
