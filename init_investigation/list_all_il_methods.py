il_comm = open("DeviceCommunicationLibrary.il", "r", encoding="utf-8", errors="ignore").read()

lines = il_comm.splitlines()
for idx, line in enumerate(lines):
    if ".method " in line:
        print(f"Line {idx+1}: {line.strip()}")
