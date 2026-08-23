import os
import glob
import struct
import fcntl
import ctypes

USBDEVFS_CLAIMINTERFACE = 0x8004550F
USBDEVFS_RELEASEINTERFACE = 0x80045510
USBDEVFS_BULK = 0xC0185502

DEFAULT_VID = 0x33c3
DEFAULT_PID = 0xf101
DEFAULT_INTERFACE = 1
DEFAULT_ENDPOINT = 0x02

def find_target_usb_device(vid=DEFAULT_VID, pid=DEFAULT_PID):
    usb_dir = '/sys/bus/usb/devices'
    if not os.path.exists(usb_dir):
        return None
    for entry in os.listdir(usb_dir):
        dev_path = os.path.join(usb_dir, entry)
        v_f = os.path.join(dev_path, 'idVendor')
        p_f = os.path.join(dev_path, 'idProduct')
        if os.path.exists(v_f) and os.path.exists(p_f):
            try:
                v = open(v_f).read().strip().lower()
                p = open(p_f).read().strip().lower()
                if v == f"{vid:04x}" and p == f"{pid:04x}":
                    d_f = os.path.join(dev_path, 'devnum')
                    b_f = os.path.join(dev_path, 'busnum')
                    if os.path.exists(d_f) and os.path.exists(b_f):
                        d = int(open(d_f).read().strip())
                        b = int(open(b_f).read().strip())
                        node = f"/dev/bus/usb/{b:03d}/{d:03d}"
                        if os.path.exists(node):
                            return node
            except Exception:
                pass
    return None

def unbind_cdc_acm():
    unbind_path = "/sys/bus/usb/drivers/cdc_acm/unbind"
    if os.path.exists(unbind_path):
        try:
            with open(unbind_path, 'w') as f:
                f.write("1-9:1.1\n")
        except Exception:
            pass

class MSDisplayUSBDevice:
    def __init__(self, dev_node=None, interface=DEFAULT_INTERFACE, endpoint=DEFAULT_ENDPOINT):
        self.dev_node = dev_node
        self.interface = interface
        self.endpoint = endpoint
        self.fd = None

    def connect(self):
        if not self.dev_node:
            self.dev_node = find_target_usb_device()
        if not self.dev_node:
            raise RuntimeError(f"MSDisplay USB device {DEFAULT_VID:04x}:{DEFAULT_PID:04x} not found.")
        unbind_cdc_acm()
        self.fd = os.open(self.dev_node, os.O_RDWR)
        iface_buf = struct.pack("I", self.interface)
        fcntl.ioctl(self.fd, USBDEVFS_CLAIMINTERFACE, iface_buf)

    def send_bulk(self, payload_bytes, timeout_ms=2000):
        if self.fd is None:
            raise RuntimeError("Device not connected. Call connect() first.")
        data_buf = ctypes.create_string_buffer(payload_bytes)
        bulk_req = struct.pack('IIIIPI', self.endpoint, len(payload_bytes), timeout_ms, 0, ctypes.addressof(data_buf), 0)
        return fcntl.ioctl(self.fd, USBDEVFS_BULK, bulk_req)

    def close(self):
        if self.fd is not None:
            try:
                iface_buf = struct.pack("I", self.interface)
                fcntl.ioctl(self.fd, USBDEVFS_RELEASEINTERFACE, iface_buf)
            except Exception:
                pass
            try:
                os.close(self.fd)
            except Exception:
                pass
            self.fd = None

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
