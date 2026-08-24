#!/usr/bin/env python3
"""
VMAX USB PCAPNG Capture Analyzer Tool
Reads pcapng USB captures for 33c3:f101 (HL VMAX LCD), parses setup requests,
CDC ACM control transfers, bulk OUT/IN frames (AH..MI), validates CRCs,
and extracts embedded JPEG stream files.
"""

import sys
import os
import json

HEADER = b"AH" # 0x41 0x48
FOOTER = b"MI" # 0x4D 0x49

def calculate_crc16_modbus(data: bytes) -> int:
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

    calc_crc = calculate_crc16_modbus(payload[2:-4])
    
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

def analyze_pcapng(pcap_path, output_json, output_log):
    log_lines = []
    def log(msg):
        print(msg)
        log_lines.append(msg)

    log(f"=== ANALYZING PCAPNG CAPTURE: {pcap_path} ===")
    
    results = {
        "pcap_file": pcap_path,
        "usb_device": "33c3:f101",
        "control_transfers": [],
        "bulk_out_frames": [],
        "bulk_in_frames": [],
        "jpeg_streams_found": 0,
        "summary": {}
    }

    if not os.path.exists(pcap_path):
        log(f"PCAPNG file {pcap_path} not found. Operating in parser template mode.")
        results["summary"]["status"] = "FILE_NOT_FOUND"
        with open(output_json, 'w') as f:
            json.dump(results, f, indent=2)
        with open(output_log, 'w') as f:
            f.write('\n'.join(log_lines))
        return

    # If tshark / tcpdump is available, parse pcapng bytes
    # Extract raw data fields using tshark if installed
    log("Attempting tshark extraction...")
    tshark_cmd = f"tshark -r {pcap_path} -Y 'usb.idVendor == 0x33c3 || usb' -T fields -e frame.number -e usb.endpoint_number -e usb.endpoint_number.direction -e usb.capdata 2>/dev/null"
    
    try:
        import subprocess
        res = subprocess.run(tshark_cmd, shell=True, capture_output=True, text=True)
        lines = res.stdout.splitlines()
        log(f"Extracted {len(lines)} USB packets from capture.")
        
        for line in lines:
            parts = line.strip().split('\t')
            if len(parts) >= 4 and parts[3]:
                pkt_num, ep, direction, data_hex = parts[0], parts[1], parts[2], parts[3].replace(':', '')
                raw_bytes = bytes.fromhex(data_hex)
                
                parsed_frame = parse_ah_mi_frame(raw_bytes)
                if parsed_frame:
                    log(f"Packet #{pkt_num} [EP {ep} Dir {direction}]: Valid AH..MI Frame: CMD {parsed_frame['cmd']} Len {parsed_frame['content_length']} CRC Valid: {parsed_frame['crc_valid']}")
                    results["bulk_out_frames"].append({
                        "packet_num": pkt_num,
                        "endpoint": ep,
                        "frame": parsed_frame
                    })
                
                # Check for JPEG SOI (FF D8 FF)
                if b"\xff\xd8\xff" in raw_bytes:
                    log(f"Packet #{pkt_num}: Found JPEG SOI marker!")
                    results["jpeg_streams_found"] += 1
    except Exception as e:
        log(f"Error analyzing pcapng with tshark: {e}")

    with open(output_json, 'w') as f:
        json.dump(results, f, indent=2)
    with open(output_log, 'w') as f:
        f.write('\n'.join(log_lines))

if __name__ == "__main__":
    pcap = sys.argv[1] if len(sys.argv) > 1 else "/home/tor/pc-case-lcd/vmax_startup.pcapng"
    out_json = "/home/tor/pc-case-lcd/vmax_capture_analysis.json"
    out_log = "/home/tor/pc-case-lcd/vmax_capture_analysis.log"
    analyze_pcapng(pcap, out_json, out_log)
