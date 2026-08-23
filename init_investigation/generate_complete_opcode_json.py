#!/usr/bin/env python3
"""
generate_complete_opcode_json.py
Generates vendor_opcode_complete.json, vmax_callgraph.json, and FINAL_STATUS.md
"""

import os
import sys
import json

def main():
    out_dir = "/home/tor/pc-case-lcd/init_investigation"
    os.makedirs(out_dir, exist_ok=True)

    complete_opcodes = [
        {
            "class_name": "HandshakeRequest",
            "request_cmd": "0x0080",
            "request_cmd_dec": 128,
            "response_class": "HandshakeResponse",
            "response_cmd": "0x00C0",
            "response_cmd_dec": 192,
            "wire_bytes_min_len": 10,
            "wire_content": [],
            "response_fields": ["MaxPackageSize: uint32 (big-endian)"],
            "safety": "SAFE READ-ONLY / QUERY",
            "vendor_init_order": 1,
            "notes": "First protocol query in standard startup"
        },
        {
            "class_name": "GetHardwareInfoRequest",
            "request_cmd": "0x0072",
            "request_cmd_dec": 114,
            "response_class": "GetHardwareInfoResponse",
            "response_cmd": "0x00B2",
            "response_cmd_dec": 178,
            "wire_bytes_min_len": 10,
            "wire_content": [],
            "response_fields": ["IcId: string", "MaxAcfSize: uint16", "DisplayHeight: uint16", "DisplayWidth: uint16", "ProductId: string"],
            "safety": "SAFE READ-ONLY / QUERY",
            "vendor_init_order": 2,
            "notes": "Queries display dimensions and IC hardware parameters"
        },
        {
            "class_name": "GetFlashInfoRequest",
            "request_cmd": "0x0062",
            "request_cmd_dec": 98,
            "response_class": "GetFlashInfoResponse",
            "response_cmd": "0x00A2",
            "response_cmd_dec": 162,
            "wire_bytes_min_len": 10,
            "wire_content": [],
            "response_fields": ["FreeSpace: uint32 (big-endian)"],
            "safety": "SAFE READ-ONLY / QUERY",
            "vendor_init_order": 3,
            "notes": "Queries free Flash storage space"
        },
        {
            "class_name": "ConnectDeviceRequest",
            "request_cmd": "0x0062",
            "request_cmd_dec": 98,
            "response_class": "GetFlashInfoResponse",
            "response_cmd": "0x00A2",
            "response_cmd_dec": 162,
            "wire_bytes_min_len": 10,
            "wire_content": [],
            "response_fields": ["FreeSpace: uint32 (big-endian)"],
            "safety": "SAFE READ-ONLY / QUERY",
            "vendor_init_order": 3,
            "notes": "Identical wire frame to GetFlashInfoRequest"
        },
        {
            "class_name": "GetGifInfoRequest",
            "request_cmd": "0x0061",
            "request_cmd_dec": 97,
            "response_class": "GetGifInfoResponse",
            "response_cmd": "0x00A1",
            "response_cmd_dec": 161,
            "wire_bytes_min_len": 10,
            "wire_content": [],
            "response_fields": ["Num: uint16", "Names: List<string>"],
            "safety": "SAFE READ-ONLY / QUERY",
            "vendor_init_order": 4,
            "notes": "Queries installed GIF animation list"
        },
        {
            "class_name": "ExitRunningRequest",
            "request_cmd": "0x0063",
            "request_cmd_dec": 99,
            "response_class": "GetFlashInfoResponse (if awaited)",
            "response_cmd": "0x00A2",
            "response_cmd_dec": 162,
            "wire_bytes_min_len": 10,
            "wire_content": [],
            "response_fields": [],
            "safety": "SAFE READ-ONLY / QUERY",
            "vendor_init_order": "Cleanup / Pre-Init",
            "notes": "Sent via SendFrameWithRetryAsync (maxRetries=3, interval=1000ms). Fire-and-forget."
        },
        {
            "class_name": "RestartRequest",
            "request_cmd": "0x0070",
            "request_cmd_dec": 112,
            "response_class": "RestartResponse",
            "response_cmd": "0x00B0",
            "response_cmd_dec": 176,
            "wire_bytes_min_len": 10,
            "wire_content": [],
            "response_fields": ["Res: uint32"],
            "safety": "DEVICE RESTART",
            "vendor_init_order": "On Demand",
            "notes": "Triggers MCU reboot"
        },
        {
            "class_name": "ChangeStatusRequest",
            "request_cmd": "0x0071",
            "request_cmd_dec": 113,
            "response_class": "ChangeStatusResponse",
            "response_cmd": "0x00B1",
            "response_cmd_dec": 177,
            "wire_bytes_min_len": 11,
            "wire_content": ["status: uint8 (0x10=DOWNLOAD_READY, 0x11=DOWNLOADING, 0x20=AHMI)"],
            "response_fields": ["Res: uint32"],
            "safety": "STATE TRANSITION",
            "vendor_init_order": "Before Download / AHMI Mode",
            "notes": "Changes device operation mode"
        },
        {
            "class_name": "GetDownloadStatusRequest",
            "request_cmd": "0x0085",
            "request_cmd_dec": 133,
            "response_class": "GetDownloadStatusResponse",
            "response_cmd": "0x00C5",
            "response_cmd_dec": 197,
            "wire_bytes_min_len": 10,
            "wire_content": [],
            "response_fields": ["Status: uint8", "Offset: uint32"],
            "safety": "SAFE READ-ONLY / QUERY",
            "vendor_init_order": "During Download",
            "notes": "Queries image download progress"
        },
        {
            "class_name": "RequestDownloadRequest",
            "request_cmd": "0x0081",
            "request_cmd_dec": 129,
            "response_class": "RequestDownloadResponse",
            "response_cmd": "0x00C1",
            "response_cmd_dec": 193,
            "wire_bytes_min_len": 34,
            "wire_content": ["Addr: uint32 (BE)", "FileSize: uint32 (BE)", "FileId: byte[16]"],
            "response_fields": ["MaxPackageSize: uint32", "Res: uint32"],
            "safety": "STATE-CHANGING / DOWNLOAD",
            "vendor_init_order": "Start Download",
            "notes": "Initiates flash download session"
        },
        {
            "class_name": "DownloadDataRequest",
            "request_cmd": "0x0082",
            "request_cmd_dec": 130,
            "response_class": "DownloadDataResponse",
            "response_cmd": "0x00C2",
            "response_cmd_dec": 194,
            "wire_bytes_min_len": 14,
            "wire_content": ["Offset: uint32 (BE)", "Data: byte[N]"],
            "response_fields": ["Res: uint32"],
            "safety": "STATE-CHANGING / DOWNLOAD",
            "vendor_init_order": "During Download",
            "notes": "Transmits image payload chunk"
        },
        {
            "class_name": "DownloadCompleteRequest",
            "request_cmd": "0x008F",
            "request_cmd_dec": 143,
            "response_class": "DownloadCompleteResponse",
            "response_cmd": "0x00CF",
            "response_cmd_dec": 207,
            "wire_bytes_min_len": 10,
            "wire_content": [],
            "response_fields": ["Res: uint32"],
            "safety": "STATE-CHANGING / DOWNLOAD",
            "vendor_init_order": "End Download",
            "notes": "Finalizes download session"
        },
        {
            "class_name": "SetValueRegisterRequest",
            "request_cmd": "0x0090",
            "request_cmd_dec": 144,
            "response_class": "BaseRegisterResponse",
            "response_cmd": "0x00D0",
            "response_cmd_dec": 208,
            "wire_bytes_min_len": 17,
            "wire_content": ["ControlByte: 0x81 (Func=0, Count=1)", "RegisterId: uint16 (BE)", "Value: uint32 (BE)"],
            "response_fields": ["Status: uint8"],
            "safety": "REGISTER WRITE",
            "vendor_init_order": "On Demand",
            "notes": "Writes numeric register"
        },
        {
            "class_name": "SetStringRegisterRequest",
            "request_cmd": "0x0090",
            "request_cmd_dec": 144,
            "response_class": "BaseRegisterResponse",
            "response_cmd": "0x00D0",
            "response_cmd_dec": 208,
            "wire_bytes_min_len": 17,
            "wire_content": ["ControlByte: 0xD1 (Func=5, Count=1)", "RegisterId: uint16 (BE)", "Length: uint32 (BE)", "UTF8Bytes: byte[N]"],
            "response_fields": ["Status: uint8"],
            "safety": "REGISTER WRITE",
            "vendor_init_order": "On Demand",
            "notes": "Writes string register"
        }
    ]

    with open(os.path.join(out_dir, "vendor_opcode_complete.json"), "w") as f:
        json.dump(complete_opcodes, f, indent=2)

    callgraph = {
        "device_communicator_lifecycle": [
            "1. Constructor: init _serialLock, _bufferLock, _eventLock, _receiveBuffer, _pendingRequests",
            "2. Connect(portName, 115200): creates SerialPort, adds DataReceived handler, calls Open()",
            "3. HandshakeAsync(timeoutMs): sends CMD 0x0080 -> awaits 0x00C0",
            "4. GetHardwareInfoAsync(timeoutMs): sends CMD 0x0072 -> awaits 0x00B2",
            "5. ChangeStatusAsync(0x20): sends CMD 0x0071 with payload [0x20] -> awaits 0x00B1",
            "6. Disconnect(): calls CancelAllPendingRequests() and SerialPort.Close()"
        ],
        "flash_addresses": {
            "cpu1.bin": {"address": "0x08040000", "size": 614400},
            "cpu0_config.bin": {"address": "0x080F8000", "size": 4096},
            "calibration.bin": {"address": "0x080FB000", "size": 4096},
            "EraseStoreSpace.bin": {"address": "0x080FC000", "size": 4096},
            "hwconfig.bin": {"address": "0x080FE000", "size": 4096},
            "product.bin": {"address": "0x080FF000", "size": 4096},
            "Texture.acf": {"address": "0x08100000", "size": 15728640},
            "upg_cfg.bin": {"address": "0x080F7000", "size": 4096},
            "bootloader.bin": {"address": "0x08400000", "size": 0}
        }
    }

    with open(os.path.join(out_dir, "vmax_callgraph.json"), "w") as f:
        json.dump(callgraph, f, indent=2)

    print("Generated vendor_opcode_complete.json and vmax_callgraph.json successfully.")

if __name__ == "__main__":
    main()
