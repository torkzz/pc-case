il_comm = open("DeviceCommunicationLibrary.il", "r", encoding="utf-8", errors="ignore").read()

def dump_crc_method():
    pos = il_comm.find("CalculateCRC")
    if pos != -1:
        start = il_comm.rfind(".method", max(0, pos-200), pos)
        end = il_comm.find("} // end of method", pos)
        print("=== BaseFrame::CalculateCRC IL Disassembly ===")
        print(il_comm[start:end+20])

    pos_build = il_comm.find("BuildFrame")
    if pos_build != -1:
        start = il_comm.rfind(".method", max(0, pos_build-200), pos_build)
        end = il_comm.find("} // end of method", pos_build)
        print("\n=== BaseFrame::BuildFrame IL Disassembly ===")
        print(il_comm[start:end+20])

dump_crc_method()
