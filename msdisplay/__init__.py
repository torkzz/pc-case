"""
MSDisplay Native Linux Driver Package
"""

from .protocol import pack_msdisplay_header, build_frame_payload, DEFAULT_WIDTH, DEFAULT_HEIGHT
from .usb import MSDisplayUSBDevice, find_target_usb_device, unbind_cdc_acm
from .jpeg import prepare_image, encode_jpeg, create_solid_color_jpeg, create_test_grid_jpeg
from .display import MSDisplayController

__all__ = [
    "pack_msdisplay_header",
    "build_frame_payload",
    "MSDisplayUSBDevice",
    "find_target_usb_device",
    "unbind_cdc_acm",
    "prepare_image",
    "encode_jpeg",
    "create_solid_color_jpeg",
    "create_test_grid_jpeg",
    "MSDisplayController",
    "DEFAULT_WIDTH",
    "DEFAULT_HEIGHT",
]

__version__ = "1.0.0"
