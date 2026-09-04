import re

il_comm = open("DeviceCommunicationLibrary.il", "r", encoding="utf-8", errors="ignore").read()

def search_methods_and_fields():
    print("=== 1. SERIALPORT INSTANTIATION & CONFIGURATION ===")
    ctor_idx = il_comm.find("DeviceCommunicator::.ctor")
    if ctor_idx != -1:
        end = il_comm.find("} // end of method", ctor_idx)
        print("DeviceCommunicator .ctor:")
        print(il_comm[ctor_idx:end])

    connect_idx = il_comm.find("DeviceCommunicator::Connect")
    if connect_idx != -1:
        end = il_comm.find("} // end of method", connect_idx)
        print("\nDeviceCommunicator Connect:")
        print(il_comm[connect_idx:end])

    print("\n=== 2. SERIALPORT EVENT REGISTRATION & HANDLERS ===")
    for m in ["OnDataReceived", "OnSerialDataReceived", "DataReceived", "ProcessReceiveBuffer", "ProcessCompleteFrame"]:
        pos = il_comm.find(f"DeviceCommunicator::{m}")
        if pos != -1:
            end = il_comm.find("} // end of method", pos)
            print(f"\nMethod {m}:")
            print(il_comm[pos:end])

search_methods_and_fields()
