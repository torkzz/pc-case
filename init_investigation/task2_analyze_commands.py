import re

il_comm = open("/home/tor/pc-case-lcd/DeviceCommunicationLibrary.il", "r", encoding="utf-8", errors="ignore").read()

def get_class_block(class_name):
    pos = il_comm.find(f".class public auto ansi beforefieldinit {class_name}")
    if pos == -1:
        pos = il_comm.find(f".class public auto ansi {class_name}")
    if pos == -1: return ""
    end_pos = il_comm.find("} // end of class", pos)
    return il_comm[pos:end_pos]

cmds = [
    ("0x0070", "RestartRequest", "RestartResponse"),
    ("0x0071", "ChangeStatusRequest", "ChangeStatusResponse"),
    ("0x0072", "GetHardwareInfoRequest", "GetHardwareInfoResponse"),
    ("0x0080", "HandshakeRequest", "HandshakeResponse"),
    ("0x0085", "GetDownloadStatusRequest", "GetDownloadStatusResponse"),
]

print("=== TASK 2: IL COMMAND SPECIFICATION AUDIT ===")

for opcode, req_cls, resp_cls in cmds:
    print(f"\n=======================================================")
    print(f"=== Command {opcode} ({req_cls} -> {resp_cls}) ===")
    print(f"=======================================================")
    
    req_block = get_class_block(req_cls)
    resp_block = get_class_block(resp_cls)
    
    print(f"--- Request Class: {req_cls} ---")
    for l in req_block.splitlines():
        if any(k in l for k in [".field", ".ctor", "get_Cmd", "BuildFrame", "stfld", "ldc.i4"]):
            print("  ", l.strip())

    print(f"\n--- Response Class: {resp_cls} ---")
    for l in resp_block.splitlines():
        if any(k in l for k in [".field", ".ctor", "get_Cmd", "Parse", "stfld", "ldc.i4"]):
            print("  ", l.strip())

