il_comm = open("DeviceCommunicationLibrary.il", "r", encoding="utf-8", errors="ignore").read()

def extract_method(method_name):
    lines = il_comm.splitlines()
    capturing = False
    result = []
    depth = 0
    for line in lines:
        if f"method " in line and method_name in line:
            capturing = True
        if capturing:
            result.append(line)
            if "{" in line:
                depth += line.count("{")
            if "}" in line:
                depth -= line.count("}")
                if depth == 0 and len(result) > 5:
                    break
    return "\n".join(result)

print("=== METHOD: ConnectDeviceAsync ===")
print(extract_method("ConnectDeviceAsync"))

print("\n=== METHOD: Connect ===")
print(extract_method("Connect"))

