import serial
import time
import os

DEV = "/dev/ttyACM0"
TX = bytes.fromhex("41 48 10 04 00 80 85 44 4d 49")

print(f"Checking device node {DEV}...")
if not os.path.exists(DEV):
    print(f"Node {DEV} not present in sandbox environment.")
else:
    try:
        print(f"Opening {DEV}...")
        with serial.Serial(DEV, baudrate=9600, timeout=2, write_timeout=2, exclusive=True) as s:
            print("Opened:", s.name)
            s.reset_input_buffer()
            s.reset_output_buffer()
            print("TX:", TX.hex(" "))
            s.write(TX)
            s.flush()
            time.sleep(0.2)
            rx = s.read(256)
            print("RX length:", len(rx))
            print("RX:", rx.hex(" ") if rx else "<NO RESPONSE>")
    except Exception as e:
        print(f"Error opening/accessing {DEV}: {e}")

