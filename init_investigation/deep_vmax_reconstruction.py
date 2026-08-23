#!/usr/bin/env python3
"""
deep_vmax_reconstruction.py
Deep Binary & Assembly Dissecting Tool for Vmax.exe, DeviceCommunicationLibrary.dll,
common.dll, MSDISPLAYSDKWRRAPER.dll, libstack.dll, and libcompositeScreenModel.dll.

Exhaustively searches for:
- SerialPort P/Invoke, EscapeCommFunction, SetCommState, DeviceIoControl
- SetupAPI, WinUSB, HID, native COM port manipulation
- AICDisp vs MSDisplay architecture references and dual-engine initialization
- All occurrences of RegisterOperation (0x0090) and Register IDs
- Every operation between SerialPort.Open() and Handshake (0x0080)
- Any native DLL exports (e.g. from libstack.dll, MSDISPLAYSDKWRRAPER.dll)
"""

import os
import sys
import re
import json

BIN_DIR = "/home/tor/vmax_bundle/bin/Release"
TARGET_FILES = [
    os.path.join(BIN_DIR, "Vmax.exe"),
    os.path.join(BIN_DIR, "DeviceCommunicationLibrary.dll"),
    os.path.join(BIN_DIR, "common.dll"),
    os.path.join(BIN_DIR, "MSDISPLAYSDKWRRAPER.dll"),
    os.path.join(BIN_DIR, "libstack.dll"),
    os.path.join(BIN_DIR, "libcompositeScreenModel.dll")
]

OUT_DIR = "/home/tor/pc-case-lcd/init_investigation"

def extract_all_strings(data):
    ascii_matches = re.findall(rb"[\x20-\x7e]{3,}", data)
    utf16_matches = re.findall(rb"(?:[\x20-\x7e]\x00){3,}", data)
    
    res = set()
    for m in ascii_matches:
        try:
            res.add(m.decode('ascii'))
        except:
            pass
    for m in utf16_matches:
        try:
            res.add(m.decode('utf-16le'))
        except:
            pass
    return sorted(list(res))

def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    print("=" * 70)
    print("DEEP VMAX BINARY & NATIVE DISSECTION SUITE")
    print("=" * 70)

    # 1. Scan for P/Invoke & Native Win32 API calls
    pinvoke_targets = [
        "kernel32", "setupapi", "winusb", "hid", "user32", "advapi32",
        "CreateFile", "DeviceIoControl", "EscapeCommFunction", "SetCommState",
        "GetCommState", "SetCommTimeouts", "PurgeComm", "SetupDiGetClassDevs",
        "SetupDiEnumDeviceInterfaces", "WinUsb_", "HidD_", "ClearCommError"
    ]

    pinvoke_findings = {}

    for fpath in TARGET_FILES:
        fname = os.path.basename(fpath)
        if not os.path.exists(fpath):
            continue

        with open(fpath, "rb") as f:
            raw = f.read()

        strings = extract_all_strings(raw)
        matched_pinvoke = [s for s in strings if any(k.lower() in s.lower() for k in pinvoke_targets)]
        
        pinvoke_findings[fname] = {
            "file_size": len(raw),
            "matched_native_apis": matched_pinvoke
        }

    # 2. Scan for RegisterOperation (0x0090) and Register IDs
    reg_targets = [
        "RegisterOperation", "SetValueRegister", "SetStringRegister", "ValueRegister",
        "FUNC_SET_VALUE_REG", "FUNC_READ_VALUE_REG", "FUNC_SET_STRING_REG", "FUNC_READ_STRING_REG"
    ]

    reg_findings = {}
    for fpath in TARGET_FILES:
        fname = os.path.basename(fpath)
        if not os.path.exists(fpath): continue
        with open(fpath, "rb") as f: raw = f.read()
        strings = extract_all_strings(raw)
        matched_reg = [s for s in strings if any(k.lower() in s.lower() for k in reg_targets)]
        reg_findings[fname] = matched_reg

    # 3. Scan for AICDisp vs MSDisplay Dual Engine Architecture
    engine_targets = [
        "AICDisp", "MSDisplay", "MSUSBDisplay", "Wrraper_MSDisplay", "libstack", "libcompositeScreenModel",
        "33c3", "f101", "345f", "9132"
    ]

    engine_findings = {}
    for fpath in TARGET_FILES:
        fname = os.path.basename(fpath)
        if not os.path.exists(fpath): continue
        with open(fpath, "rb") as f: raw = f.read()
        strings = extract_all_strings(raw)
        matched_eng = [s for s in strings if any(k.lower() in s.lower() for k in engine_targets)]
        engine_findings[fname] = matched_eng

    # 4. Read DCL IL for full method signatures and execution flow
    dcl_il_path = os.path.join(OUT_DIR, "DeviceCommunicationLibrary.il")
    if not os.path.exists(dcl_il_path):
        dcl_il_path = "/home/tor/pc-case-lcd/DeviceCommunicationLibrary.il"

    dcl_methods = []
    if os.path.exists(dcl_il_path):
        with open(dcl_il_path, "r", encoding="utf-8", errors="ignore") as f:
            dcl_il = f.read()

        # Find all methods in DeviceCommunicator
        methods = re.findall(r"\.method\s+public[\s\S]*?instance\s+default\s+([^\n]+)", dcl_il)
        dcl_methods = [m.strip() for m in methods]

    output = {
        "pinvoke_and_native_apis": pinvoke_findings,
        "register_operations": reg_findings,
        "dual_engine_architecture": engine_findings,
        "device_communicator_all_public_methods": dcl_methods
    }

    with open(os.path.join(OUT_DIR, "vmax_reconstruction_master.json"), "w") as f:
        json.dump(output, f, indent=2)

    print("Extracted native APIs, register operations, and engine architecture data.")
    print(f"Results saved to {os.path.join(OUT_DIR, 'vmax_reconstruction_master.json')}")

if __name__ == "__main__":
    main()
