import re

il_path = "/home/tor/pc-case-lcd/DeviceCommunicationLibrary.il"
with open(il_path, "r", encoding="utf-8", errors="ignore") as f:
    text = f.read()

print("Length of IL file:", len(text))

# Search for methods in DeviceCommunicator
pattern = re.compile(r'\.method\s+public.*?(\w+)\s*\(.*?\)\s*cil\s+managed', re.DOTALL)
methods = re.findall(r'\.method\s+.*?([A-Za-z0-9_]+)\s*\([^)]*\)\s*cil\s+managed', text)
print("Found methods:", set(methods[:50]))

# Search for baudRate, serial port init, write, read in DeviceCommunicator
lines = text.splitlines()
in_dev_comm = False
current_method = ""
method_lines = []

dev_comm_methods = {}

for idx, line in enumerate(lines):
    if ".class public auto ansi beforefieldinit DeviceCommunicator" in line:
        in_dev_comm = True
    elif in_dev_comm and line.startswith(".class ") and "DeviceCommunicator" not in line:
        in_dev_comm = False
    
    if in_dev_comm:
        if ".method" in line:
            current_method = line.strip()
            dev_comm_methods[current_method] = []
        elif current_method:
            dev_comm_methods[current_method].append(line)

print(f"Captured {len(dev_comm_methods)} methods inside DeviceCommunicator.")

for m, mlines in dev_comm_methods.items():
    mcode = "\n".join(mlines)
    if any(k in mcode for k in ['b115200', '115200', '9600', 'SerialPort', 'Handshake', 'Send', 'Write', 'Read', 'Dtr', 'Rts', 'baudRate']):
        print(f"\n--- Method Header: {m} ---")
        print("\n".join(mlines[:40]))

