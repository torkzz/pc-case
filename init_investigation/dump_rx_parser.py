il_comm = open("DeviceCommunicationLibrary.il", "r", encoding="utf-8", errors="ignore").read()

def dump_method_by_name(mname):
    print(f"\n=============================================")
    print(f"=== METHOD: {mname} ===")
    print(f"=============================================")
    pos = 0
    while True:
        idx = il_comm.find(mname, pos)
        if idx == -1: break
        # find method start
        mstart = il_comm.rfind(".method", max(0, idx-200), idx)
        if mstart == -1: mstart = idx
        mend = il_comm.find("} // end of method", idx)
        if mend == -1: mend = idx + 2000
        print(il_comm[mstart:mend+20])
        pos = mend + 1

dump_method_by_name("ProcessReceiveBuffer")
dump_method_by_name("FindFrameStart")
dump_method_by_name("DataReceived")
