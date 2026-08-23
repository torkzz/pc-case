import re
import json

il_path = "/home/tor/pc-case-lcd/DeviceCommunicationLibrary.il"
with open(il_path, "r", encoding="utf-8", errors="ignore") as f:
    il_text = f.read()

# Map of command classes and their CMD opcodes, payloads, and CTRL logic
commands = [
    {"name": "HandshakeRequest", "cmd": 0x0080, "resp_cmd": 0x00C0, "class": "HandshakeRequest"},
    {"name": "GetHardwareInfoRequest", "cmd": 0x0072, "resp_cmd": 0x00B2, "class": "GetHardwareInfoRequest"},
    {"name": "GetFlashInfoRequest", "cmd": 0x0062, "resp_cmd": 0x00A2, "class": "GetFlashInfoRequest"},
    {"name": "GetGifInfoRequest", "cmd": 0x0061, "resp_cmd": 0x00A1, "class": "GetGifInfoRequest"},
    {"name": "GetDownloadStatusRequest", "cmd": 0x0085, "resp_cmd": 0x00C5, "class": "GetDownloadStatusRequest"},
    {"name": "RequestDownloadRequest", "cmd": 0x0081, "resp_cmd": 0x00C1, "class": "RequestDownloadRequest"},
    {"name": "DownloadDataRequest", "cmd": 0x0082, "resp_cmd": 0x00C2, "class": "DownloadDataRequest"},
    {"name": "DownloadCompleteRequest", "cmd": 0x008F, "resp_cmd": 0x00CF, "class": "DownloadCompleteRequest"},
    {"name": "ChangeStatusRequest", "cmd": 0x0071, "resp_cmd": 0x00B1, "class": "ChangeStatusRequest"},
    {"name": "RestartRequest", "cmd": 0x0070, "resp_cmd": 0x00B0, "class": "RestartRequest"},
    {"name": "ExitRunningRequest", "cmd": 0x0063, "resp_cmd": None, "class": "ExitRunningRequest"},
]

def build_frame(cmd, content=b"", is_crc=False):
    payload_len = len(content)
    ctrl_val = (payload_len + 4) & 0x0FFF
    if is_crc:
        ctrl_val |= (1 << 12)
    ctrl_bytes = ctrl_val.to_bytes(2, 'big')
    cmd_bytes = cmd.to_bytes(2, 'big')
    body = ctrl_bytes + cmd_bytes + content
    
    # CRC
    if is_crc:
        crc = 0xFFFF
        for b in body:
            crc ^= b
            for _ in range(8):
                if crc & 1:
                    crc = (crc >> 1) ^ 0xA001
                else:
                    crc >>= 1
        crc_bytes = (crc & 0xFFFF).to_bytes(2, 'big')
    else:
        crc_bytes = b"\x00\x00"
        
    return b"AH" + body + crc_bytes + b"MI"

frames_json = []

for c in commands:
    # Build default frame (no CRC, as initialized in DLL .ctor)
    frame_bytes = build_frame(c["cmd"], is_crc=False)
    entry = {
        "command_name": c["name"],
        "request_opcode": f"0x{c['cmd']:04X}",
        "response_opcode": f"0x{c['resp_cmd']:04X}" if c["resp_cmd"] else None,
        "ctrl_default": f"0x{(len(b'') + 4):04X}",
        "crc_enabled_by_default": False,
        "payload_length": 0,
        "payload_hex": "",
        "frame_hex": frame_bytes.hex(),
        "source_class": f"DeviceCommunicationLibrary.{c['class']}",
        "evidence": "CONFIRMED STATIC (DeviceCommunicationLibrary.il)"
    }
    frames_json.append(entry)

# Write to vmax_frames.json
with open("/home/tor/pc-case-lcd/vmax_frames.json", "w") as f:
    json.dump(frames_json, f, indent=2)

print(f"Generated /home/tor/pc-case-lcd/vmax_frames.json with {len(frames_json)} command definitions.")

