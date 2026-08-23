import re

il_comm = open("DeviceCommunicationLibrary.il", "r", encoding="utf-8", errors="ignore").read()

def get_class_code(class_name):
    pos = il_comm.find(f".class public auto ansi beforefieldinit {class_name}")
    if pos == -1:
        pos = il_comm.find(f".class public auto ansi {class_name}")
    if pos == -1: return ""
    end_pos = il_comm.find("} // end of class", pos)
    return il_comm[pos:end_pos]

frame_classes = [
    "HandshakeRequest", "HandshakeResponse",
    "GetHardwareInfoRequest", "GetHardwareInfoResponse",
    "GetFlashInfoRequest", "GetFlashInfoResponse",
    "GetGifInfoRequest", "GetGifInfoResponse",
    "ExitRunningRequest",
    "RestartRequest",
    "ChangeStatusRequest",
    "RequestDownloadRequest", "RequestDownloadResponse",
    "DownloadDataRequest", "DownloadDataResponse",
    "GetDownloadStatusRequest", "GetDownloadStatusResponse",
    "DownloadCompleteRequest", "DownloadCompleteResponse",
    "ConnectDeviceRequest"
]

print("=== FRAME OPCODES & CALCULATIONS ===")
for fc in frame_classes:
    code = get_class_code(fc)
    # search get_Cmd
    cmd_pos = code.find("get_Cmd")
    if cmd_pos != -1:
        sub = code[cmd_pos:cmd_pos+500]
        match = re.search(r'ldc\.i4(?:\.s)?\s+(0x[0-9a-fA-F]+|\d+)', sub)
        if match:
            v = match.group(1)
            val = int(v, 16) if v.startswith("0x") else int(v)
            print(f"Frame {fc:28s}: Opcode = {val:#06x} ({val})")
        else:
            print(f"Frame {fc:28s}: get_Cmd found but no ldc.i4")
    else:
        # check ctor
        ctor_pos = code.find(".ctor")
        if ctor_pos != -1:
            sub = code[ctor_pos:ctor_pos+500]
            match = re.search(r'ldc\.i4(?:\.s)?\s+(0x[0-9a-fA-F]+|\d+)', sub)
            if match:
                v = match.group(1)
                val = int(v, 16) if v.startswith("0x") else int(v)
                print(f"Frame {fc:28s}: Ctor Opcode = {val:#06x} ({val})")
            else:
                print(f"Frame {fc:28s}: No ldc.i4 in ctor")

