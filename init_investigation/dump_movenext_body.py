il_comm = open("DeviceCommunicationLibrary.il", "r", encoding="utf-8", errors="ignore").read()

def dump_movenext(sm_name):
    print(f"\n==========================================")
    print(f"=== FULL MOVENEXT: {sm_name} ===")
    print(f"==========================================")
    idx = il_comm.find(sm_name)
    if idx == -1: return
    idx2 = il_comm.find("MoveNext", idx)
    if idx2 == -1: return
    end_idx = il_comm.find("} // end of method", idx2)
    lines = il_comm[idx2:end_idx].splitlines()
    for l in lines:
        if any(k in l for k in ["call", "ldc", "newobj", "stfld", "ldfld", "IL_"]):
            print("  ", l.strip())

dump_movenext("<ConnectDeviceAsync>d__47")
dump_movenext("<HandshakeAsync>d__34")
dump_movenext("<GetHardwareInfoAsync>d__35")
dump_movenext("<Connect>d__")
