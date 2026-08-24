import os, sys, time, struct, select, termios, fcntl

PKT_FMT = "<Q c c B B H c c q i i I I 8s i i I I"
PKT_SIZE = struct.calcsize(PKT_FMT) # Should be 64

def run_usbmon_test():
    print(f"Packet size: {PKT_SIZE} bytes")
    dev_path = "/dev/ttyACM0"
    
    usbmon_fd = os.open("/dev/usbmon1", os.O_RDONLY | os.O_NONBLOCK)
    
    tty_fd = os.open(dev_path, os.O_RDWR | os.O_NOCTTY | os.O_NONBLOCK)
    attrs = termios.tcgetattr(tty_fd)
    attrs[0], attrs[1] = 0, 0
    attrs[2] = termios.B115200 | termios.CS8 | termios.CREAD | termios.CLOCAL
    attrs[3] = 0
    termios.tcsetattr(tty_fd, termios.TCSANOW, attrs)
    fcntl.ioctl(tty_fd, 0x5418, struct.pack('I', 0x002 | 0x004))
    termios.tcflush(tty_fd, termios.TCIOFLUSH)

    tx_frame = bytes.fromhex("41480002008000004d49") # 0x0080
    print(f"Transmitting frame: {tx_frame.hex(' ')}")
    os.write(tty_fd, tx_frame)

    time.sleep(0.5)

    buf = bytearray()
    deadline = time.time() + 1.0
    while time.time() < deadline:
        r, _, _ = select.select([usbmon_fd], [], [], 0.1)
        if r:
            try:
                chunk = os.read(usbmon_fd, 65536)
                if chunk: buf.extend(chunk)
            except BlockingIOError:
                pass

    os.close(tty_fd)
    os.close(usbmon_fd)

    print(f"Captured {len(buf)} bytes from usbmon1")

    dev2_pkts = []
    offset = 0
    while offset + PKT_SIZE <= len(buf):
        pkt_bytes = buf[offset:offset+PKT_SIZE]
        offset += PKT_SIZE
        try:
            urb_id, ptype, xfer, epnum, devnum, busnum, fsetup, fdata, sec, usec, status, length, len_cap, setup_data, interval, start_frame, xfer_flags, ndesc = struct.unpack(PKT_FMT, pkt_bytes)
            
            payload = b""
            if len_cap > 0 and offset + len_cap <= len(buf):
                payload = buf[offset:offset+len_cap]
                offset += len_cap

            if devnum == 2:
                dir_str = "IN" if (epnum & 0x80) else "OUT"
                ep_clean = epnum & 0x7F
                ep_hex = f"0x{epnum:02X}"
                ptype_str = ptype.decode('ascii', errors='ignore')
                xfer_types = {0: "Ctrl", 1: "Iso", 2: "Bulk", 3: "Int"}
                xfer_str = xfer_types.get(ord(xfer), str(ord(xfer)))
                
                rec = f"URB=0x{urb_id:x} Type={ptype_str} Xfer={xfer_str} EP={ep_hex} ({dir_str}) Status={status} Len={length} Data={payload.hex(' ')}"
                dev2_pkts.append((ptype_str, xfer_str, epnum, rec))
        except Exception as e:
            print("Unpack error:", e)

    print(f"\n=== DEVNUM 2 KERNEL URB EVENTS ({len(dev2_pkts)}) ===")
    for ptype_str, xfer_str, epnum, rec in dev2_pkts:
        print(" ", rec)

if __name__ == "__main__":
    run_usbmon_test()
