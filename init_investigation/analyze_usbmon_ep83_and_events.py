#!/usr/bin/env python3
"""
analyze_usbmon_ep83_and_events.py
Parses existing usbmon captures (usbmon_reconnect.txt and usbmon_handshake_test.txt)
specifically for:
1. EP 0x83 (Interrupt IN) CDC SERIAL_STATE notifications
2. URB submit/completion status for Bulk OUT (EP 0x02), Bulk IN (EP 0x81), and Interrupt IN (EP 0x83)
3. Reset/disconnect/re-enumeration events
"""

import os
import sys
import re
import json

RECONNECT_LOG = "/home/tor/pc-case-lcd/usbmon_reconnect.txt"
HANDSHAKE_LOG = "/home/tor/pc-case-lcd/usbmon_handshake_test.txt"
OUTPUT_DIR = "/home/tor/pc-case-lcd/init_investigation"

def parse_usbmon_file(filepath):
    if not os.path.exists(filepath):
        return {"error": f"{filepath} not found"}

    print(f"Parsing {os.path.basename(filepath)}...")
    
    ep83_notifications = []
    bulk_out_summary = []
    bulk_in_summary = []
    control_transfers = []

    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        for line_num, line in enumerate(f, 1):
            line_str = line.strip()
            if not line_str:
                continue

            # Check for Control Transfers (Co / Ci)
            if " Co:" in line_str or " Ci:" in line_str:
                control_transfers.append({"line": line_num, "text": line_str})

            # Check for Interrupt IN (Ii) - EP 3 or 0x83
            if " Ii:" in line_str:
                ep83_notifications.append({"line": line_num, "text": line_str})

            # Check for Bulk OUT (Bo) - EP 2 or 0x02
            if " Bo:" in line_str:
                if len(bulk_out_summary) < 50:
                    bulk_out_summary.append({"line": line_num, "text": line_str})

            # Check for Bulk IN (Bi) - EP 1 or 0x81
            if " Bi:" in line_str:
                if len(bulk_in_summary) < 50:
                    bulk_in_summary.append({"line": line_num, "text": line_str})

    return {
        "filepath": filepath,
        "control_transfers_count": len(control_transfers),
        "control_transfers_sample": control_transfers[:30],
        "ep83_notifications_count": len(ep83_notifications),
        "ep83_notifications_sample": ep83_notifications[:50],
        "bulk_out_sample": bulk_out_summary[:20],
        "bulk_in_sample": bulk_in_summary[:20]
    }

def decode_cdc_serial_state(hex_bytes_str):
    """
    Decodes CDC ACM SERIAL_STATE notification (8 bytes):
    bmRequestType: 0xA1 (Class, Interface, Device to Host)
    bNotification: 0x20 (SERIAL_STATE)
    wValue: 0x0000
    wIndex: Interface Number
    wLength: 0x0002
    Data (2 bytes):
      bit 0: DCD (Data Carrier Detect)
      bit 1: DSR (Data Set Ready)
      bit 2: Break
      bit 3: Ring
      bit 4: Framing Error
      bit 5: Parity Error
      bit 6: Overrun
    """
    cleaned = hex_bytes_str.replace(" ", "").lower()
    if len(cleaned) < 16:
        return {"raw_hex": hex_bytes_str, "is_serial_state": False, "reason": "too short"}

    # Extract bytes
    req_type = cleaned[0:2]
    notification = cleaned[2:4]
    w_value = cleaned[4:8]
    w_index = cleaned[8:12]
    w_len = cleaned[12:16]

    state_hex = cleaned[16:20] if len(cleaned) >= 20 else cleaned[12:16]

    decoded = {
        "raw_hex": hex_bytes_str,
        "req_type": req_type,
        "notification": notification,
        "w_value": w_value,
        "w_index": w_index,
        "w_len": w_len,
        "is_serial_state": (req_type == "a1" and notification == "20"),
        "state_payload_hex": state_hex
    }

    if state_hex and len(state_hex) >= 4:
        try:
            val = int(state_hex[2:4] + state_hex[0:2], 16)
            decoded["dcd"] = bool(val & (1 << 0))
            decoded["dsr"] = bool(val & (1 << 1))
            decoded["break"] = bool(val & (1 << 2))
            decoded["ring"] = bool(val & (1 << 3))
            decoded["framing_error"] = bool(val & (1 << 4))
            decoded["parity_error"] = bool(val & (1 << 5))
            decoded["overrun_error"] = bool(val & (1 << 6))
        except:
            pass

    return decoded

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    reconnect_results = parse_usbmon_file(RECONNECT_LOG)
    handshake_results = parse_usbmon_file(HANDSHAKE_LOG)

    # Analyze EP 0x83 payloads in reconnect log
    ep83_decoded = []
    if "ep83_notifications_sample" in reconnect_results:
        for entry in reconnect_results["ep83_notifications_sample"]:
            text = entry["text"]
            if "=" in text:
                payload = text.split("=")[1].strip()
                dec = decode_cdc_serial_state(payload)
                ep83_decoded.append({"line": entry["line"], "raw_line": text, "decoded": dec})

    analysis_report = {
        "reconnect_log": reconnect_results,
        "handshake_log": handshake_results,
        "ep83_decoded_sample": ep83_decoded[:30]
    }

    out_json = os.path.join(OUTPUT_DIR, "usb_notification_analysis.json")
    with open(out_json, "w") as f:
        json.dump(analysis_report, f, indent=2)

    # Generate Markdown Summary
    out_md = os.path.join(OUTPUT_DIR, "usb_notification_analysis.md")
    with open(out_md, "w") as f:
        f.write("# USB Notification & EP 0x83 Analysis Report\n\n")
        f.write("## Overview\n")
        f.write("Detailed parsing of USB notification endpoint (`0x83` Interrupt IN) and control transfers.\n\n")
        f.write("## EP 0x83 (Interrupt IN) CDC Notifications\n")
        f.write(f"- Total Interrupt IN URB events in reconnect log: `{reconnect_results.get('ep83_notifications_count', 0)}`\n\n")

        f.write("### Sample Decoded Notifications\n")
        f.write("| Line | URB Line | Decoded Payload / CDC Serial State |\n")
        f.write("|---|---|---|\n")
        for item in ep83_decoded[:20]:
            dec = item["decoded"]
            details = f"DCD={dec.get('dcd')}, DSR={dec.get('dsr')}, Break={dec.get('break')}, Ring={dec.get('ring')}" if isinstance(dec, dict) and dec.get('is_serial_state') else str(dec)
            f.write(f"| {item['line']} | `{item['raw_line'][:60]}...` | `{details}` |\n")

    print(f"Saved analysis to {out_json} and {out_md}")

if __name__ == "__main__":
    main()
