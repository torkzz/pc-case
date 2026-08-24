import re

il_path = "/home/tor/pc-case-lcd/DeviceCommunicationLibrary.il"
with open(il_path, "r", encoding="utf-8", errors="ignore") as f:
    il_text = f.read()

print(f"Total IL characters: {len(il_text)}")

# Find all methods in DeviceCommunicator
pattern = re.compile(r'\.class\s+public\s+auto\s+ansi\s+beforefieldinit\s+DeviceCommunicator.*?\n(\s*\.class|\Z)', re.DOTALL)
match = pattern.search(il_text)

if match:
    dev_comm_code = match.group(0)
    print("DeviceCommunicator code size:", len(dev_comm_code))
    
    # Extract method names and bodies
    method_pattern = re.compile(r'(\.method.*?\n\s*\{.*?\n\s*\})', re.DOTALL)
    methods = method_pattern.findall(dev_comm_code)
    print(f"Found {len(methods)} method definitions inside DeviceCommunicator.")
    
    for idx, m in enumerate(methods):
        lines = m.splitlines()
        header = lines[0].strip()
        name_search = re.search(r'(?:default|void|bool|int32|string|class|unsigned)\s+([A-Za-z0-9_`<>\$]+)\s*\(', header)
        mname = name_search.group(1) if name_search else f"Method_{idx}"
        print(f"\n--- [{idx+1}/{len(methods)}] {mname} ---")
        print(lines[0])
        # Print relevant calls and field assignments
        for l in lines:
            l_str = l.strip()
            if any(k in l_str for k in ['SerialPort', 'call', 'stfld', 'ldsfld', 'Timeout', 'BaudRate', 'Dtr', 'Rts', 'Write', 'Read', 'Delay', 'Sleep', 'Handshake', 'CMD_']):
                print(f"    {l_str}")
else:
    print("DeviceCommunicator class block not found.")

