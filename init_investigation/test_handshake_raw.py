import os, sys, time, termios, fcntl

DEV = "/dev/ttyACM0"
TX = bytes.fromhex("41 48 10 04 00 80 85 44 4d 49")

print(f"Checking device node {DEV}...")
if not os.path.exists(DEV):
    print(f"Node {DEV} not present in sandbox scope.")
    sys.exit(0)

try:
    print(f"Opening {DEV}...")
    fd = os.open(DEV, os.O_RDWR | os.O_NOCTTY | os.O_NONBLOCK)
    print("Opened descriptor:", fd)
    
    # Configure termios (raw 9600 baud)
    attrs = termios.tcgetattr(fd)
    attrs[0] = 0 # iflag
    attrs[1] = 0 # oflag
    attrs[2] = termios.CS8 | termios.CREAD | termios.CLOCAL # cflag
    attrs[3] = 0 # lflag
    termios.tcsetattr(fd, termios.TCSANOW, attrs)
    
    # Clear non-blocking
    flags = fcntl.fcntl(fd, fcntl.F_GETFL)
    fcntl.fcntl(fd, fcntl.F_SETFL, flags & ~os.O_NONBLOCK)

    print("TX:", TX.hex(" "))
    os.write(fd, TX)

    time.sleep(0.2)

    try:
        rx = os.read(fd, 256)
        print("RX length:", len(rx))
        print("RX:", rx.hex(" ") if rx else "<NO RESPONSE>")
    except Exception as e:
        print(f"Read timeout / error: {e}")

    os.close(fd)
except Exception as e:
    print(f"Device open/access error: {e}")

