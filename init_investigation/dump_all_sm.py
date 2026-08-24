il_comm = open("DeviceCommunicationLibrary.il", "r", encoding="utf-8", errors="ignore").read()

import re

def get_class_block(class_name):
    pos = il_comm.find(class_name)
    if pos == -1: return ""
    end_pos = il_comm.find("  } // end of class", pos)
    if end_pos == -1: end_pos = pos + 10000
    return il_comm[pos:end_pos]

for sm in [
    "<ConnectDeviceAsync>d__47",
    "<HandshakeAsync>d__34",
    "<GetHardwareInfoAsync>d__35",
    "<GetFlashInfoAsync>d__46",
    "<ChangeStatusAsync>d__43",
    "<RestartAsync>d__44",
    "<ExitRunningAsync>d__48"
]:
    block = get_class_block(sm)
    print(f"\n==============================================")
    print(f"=== {sm} ===")
    print(f"==============================================")
    for line in block.splitlines():
        if "call" in line or "ldc.i4" in line or "newobj" in line or "IL_" in line:
            if not ("System.Runtime" in line or "System.Threading" in line or "AsyncTaskMethodBuilder" in line):
                print(line.strip())

