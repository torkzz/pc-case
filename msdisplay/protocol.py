import struct

MSDISPLAY_MAGIC_SIGNATURE = 0x0008100A
DEFAULT_WIDTH = 460
DEFAULT_HEIGHT = 1920
DEFAULT_STRIDE = 0
DEFAULT_FLAG = 1

def pack_msdisplay_header(width=DEFAULT_WIDTH, height=DEFAULT_HEIGHT, stride=DEFAULT_STRIDE, flag=DEFAULT_FLAG):
    """
    Packs 12-byte MSDisplay Header:
    - Offset 0x00: uint32 Magic Signature (0x0008100A)
    - Offset 0x04: uint16 Width
    - Offset 0x06: uint16 Height
    - Offset 0x08: uint16 Stride
    - Offset 0x0A: uint16 Flag
    """
    return struct.pack("<IHHHH", MSDISPLAY_MAGIC_SIGNATURE, width, height, stride, flag)

def build_frame_payload(jpeg_bytes, width=DEFAULT_WIDTH, height=DEFAULT_HEIGHT, stride=DEFAULT_STRIDE, flag=DEFAULT_FLAG):
    """
    Prepends the 12-byte MSDisplay header to a JPEG byte stream.
    Validates that jpeg_bytes starts with JPEG SOI marker (0xFF 0xD8).
    """
    if not jpeg_bytes or not jpeg_bytes.startswith(b'\xff\xd8'):
        raise ValueError("Payload must be a valid JPEG byte stream starting with 0xFF 0xD8.")
    header = pack_msdisplay_header(width, height, stride, flag)
    return header + jpeg_bytes
