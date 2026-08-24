#!/usr/bin/env python3
"""
VMAX PCAPNG / USBMON Runtime Traffic Analyzer (Task 8)
Parses USB traffic captures, extracts CDC ACM and libusb transfers,
reconstructs AH..MI protocol frames, and isolates JPEG image streams.
"""

import sys
import os
import json
import struct

HEADER = b"AH" # 0x41 0x48
FOOTER = b"MI" # 0x4D 0x49

def crc16_modbus(data: bytes) -> int:
    crc = 0xFFFF
    for b in data:
        crc ^= b
        for _ in range(8):
            if crc & 1:
                crc = (crc >> 1) ^ 0xA001
            else:
                crc >>= 1
    return crc & 0xFFFF

def parse_ah_mi_frame(payload: bytes):
    if len(payload) < 10:
        return None
    if payload[:2] != HEADER or payload[-2:] != FOOTER:
        return None

    ctrl = int.from_bytes(payload[2:4], 'big')
    cmd = int.from_bytes(payload[4:6], 'big')
    crc_wire = int.from_bytes(payload[-4:-2], 'big')
    content = payload[6:-4]
    calc_crc = crc16_modbus(payload[2:-4])

    return {
        "header": "AH",
        "ctrl": ctrl,
        "ctrl_hex": f"0x{ctrl:04X}",
        "cmd": f"0x{cmd:04X}",
        "content_length": len(content),
        "content_hex": content.hex(),
        "crc_wire": f"0x{crc_wire:04X}",
        "crc_calc": f"0x{calc_crc:04X}",
        "crc_valid": (crc_wire == calc_crc),
        "footer": "MI"
    }

def analyze_capture(pcap_path, output_json, output_md):
    log_lines = []
    def log(msg):
        print(msg)
        log_lines.append(msg)

    log(f"# VMAX USB Traffic Capture Analysis\n")
    log(f"Capture file: `{pcap_path}`\n")
    
    results = {
        "pcap_file": pcap_path,
        "usb_device": "33c3:f101",
        "control_transfers": [],
        "bulk_out_frames": [],
        "bulk_in_frames": [],
        "jpeg_streams": [],
        "summary": {}
    }

    if not os.path.exists(pcap_path):
        log("`vmax_runtime.pcapng` file not present. Analyzer template ready.")
        results["summary"]["status"] = "PENDING_CAPTURE"
        with open(output_json, 'w') as f:
            json.dump(results, f, indent=2)
        with open(output_md, 'w') as f:
            f.write('\n'.join(log_lines))
        return

    # Extract via tshark if available
    try:
        import subprocess
        tcmd = f"tshark -r {pcap_path} -Y 'usb.idVendor == 0x33c3 || usb' -T fields -e frame.number -e usb.endpoint_number -e usb.endpoint_number.direction -e usb.capdata 2>/dev/null"
        res = subprocess.run(tcmd, shell=True, capture_output=True, text=True)
        lines = res.stdout.splitlines()
        log(f"Extracted {len(lines)} USB packet records.")
        
        for line in lines:
            parts = line.strip().split('\t')
            if len(parts) >= 4 and parts[3]:
                pkt, ep, direction, hex_data = parts[0], parts[1], parts[2], parts[3].replace(':', '')
                raw = bytes.fromhex(hex_data)
                
                frame_info = parse_ah_mi_frame(raw)
                if frame_info:
                    log(f"- **Pkt #{pkt}** (EP {ep} Dir {direction}): AH..MI CMD `{frame_info['cmd']}` Len `{frame_info['content_length']}` CRC Valid: `{frame_info['crc_valid']}`")
                    results["bulk_out_frames"].append({"pkt": pkt, "ep": ep, "frame": frame_info})

                if b"\xff\xd8\xff" in raw:
                    log(f"- **Pkt #{pkt}**: JPEG SOI marker detected (`0xFFD8FF`).")
                    results["jpeg_streams"].append({"pkt": pkt, "offset": raw.find(b"\xff\xd8\xff")})
    except Exception as e:
        log(f"Capture parsing error: {e}")

    with open(output_json, 'w') as f:
        json.dump(results, f, indent=2)
    with open(output_md, 'w') as f:
        f.write('\n'.join(log_lines))

if __name__ == "__main__":
    pcap = sys.argv[1] if len(sys.argv) > 1 else "/home/tor/pc-case-lcd/vmax_runtime.pcapng"
    analyze_capture(pcap, "/home/tor/pc-case-lcd/runtime_analysis.json", "/home/tor/pc-case-lcd/runtime_analysis.md")
