import os
import glob
import struct
import fcntl
import ctypes

USBDEVFS_CLAIMINTERFACE = 0x8004550F
USBDEVFS_RELEASEINTERFACE = 0x80045510
USBDEVFS_BULK = 0xC0185502

def find_target_usb_device(vid=0x33c3, pid=0xf101):
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

class MSDisplayDevice:
    def __init__(self, dev_node=None, interface=1, endpoint=0x02):
        self.dev_node = dev_node or find_target_usb_device()
        self.interface = interface
        self.endpoint = endpoint
        self.fd = None

    def open(self):
        if not self.dev_node:
            raise RuntimeError("MSDisplay USB device 33c3:f101 not found.")
        unbind_cdc_acm()
        self.fd = os.open(self.dev_node, os.O_RDWR)
        iface_buf = struct.pack("I", self.interface)
        fcntl.ioctl(self.fd, USBDEVFS_CLAIMINTERFACE, iface_buf)

    def send_payload(self, payload_bytes, timeout_ms=2000):
        if self.fd is None:
            raise RuntimeError("Device not open.")
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
            os.close(self.fd)
            self.fd = None

    def __enter__(self):
        self.open()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
