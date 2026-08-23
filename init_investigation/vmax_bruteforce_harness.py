#!/usr/bin/env python3
"""
vmax_bruteforce_harness.py
Systematic Automated Protocol & Configuration Test Harness for HL VMAX LCD (33c3:f101)

Features:
- Exhaustive matrix of SAFE read-only / init commands extracted from vendor IL
- Systematic baud rate matrix (9600, 19200, 38400, 57600, 115200, 230400, 460800, 921600)
- Systematic DTR/RTS matrix (0/0, 1/0, 0/1, 1/1)
- Clean per-test port isolation (open -> test -> listen -> close)
- Instant STOP condition on ANY RX byte > 0
- Detailed timing & JSON/MD report generation
"""

import sys
import os
import time
import json
import argparse

# ── Frame Definitions (All Safe Opcodes Extracted from IL) ───────────────────────

SAFE_FRAMES = {
    "HANDSHAKE_0x0080": {
        "cmd": "0x0080",
        "description": "HandshakeRequest (CMD 0x0080)",
        "bytes": bytes([0x41, 0x48, 0x00, 0x02, 0x00, 0x80, 0x00, 0x00, 0x4D, 0x49]),
        "expected_resp": "0x00C0"
    },
    "HW_INFO_0x0072": {
        "cmd": "0x0072",
        "description": "GetHardwareInfoRequest (CMD 0x0072)",
        "bytes": bytes([0x41, 0x48, 0x00, 0x02, 0x00, 0x72, 0x00, 0x00, 0x4D, 0x49]),
        "expected_resp": "0x00B2"
    },
    "GET_FLASH_INFO_0x0062": {
        "cmd": "0x0062",
        "description": "GetFlashInfoRequest / ConnectDeviceRequest (CMD 0x0062)",
        "bytes": bytes([0x41, 0x48, 0x00, 0x02, 0x00, 0x62, 0x00, 0x00, 0x4D, 0x49]),
        "expected_resp": "0x00A2"
    },
    "GET_GIF_INFO_0x0061": {
        "cmd": "0x0061",
        "description": "GetGifInfoRequest (CMD 0x0061)",
        "bytes": bytes([0x41, 0x48, 0x00, 0x02, 0x00, 0x61, 0x00, 0x00, 0x4D, 0x49]),
        "expected_resp": "0x00A1"
    },
    "GET_DL_STATUS_0x0085": {
        "cmd": "0x0085",
        "description": "GetDownloadStatusRequest (CMD 0x0085)",
        "bytes": bytes([0x41, 0x48, 0x00, 0x02, 0x00, 0x85, 0x00, 0x00, 0x4D, 0x49]),
        "expected_resp": "0x00C5"
    },
    "EXIT_RUNNING_0x0063": {
        "cmd": "0x0063",
        "description": "ExitRunningRequest (CMD 0x0063)",
        "bytes": bytes([0x41, 0x48, 0x00, 0x02, 0x00, 0x63, 0x00, 0x00, 0x4D, 0x49]),
        "expected_resp": "0x00A2"
    },
    "CHANGE_STATUS_AHMI_0x0071": {
        "cmd": "0x0071",
        "description": "ChangeStatusRequest STATUS_AHMI=0x20 (CMD 0x0071)",
        "bytes": bytes([0x41, 0x48, 0x00, 0x03, 0x00, 0x71, 0x20, 0x00, 0x00, 0x4D, 0x49]),
        "expected_resp": "0x00B1"
    },
    "CHANGE_STATUS_READY_0x0071": {
        "cmd": "0x0071",
        "description": "ChangeStatusRequest STATUS_DOWNLOAD_READY=0x10 (CMD 0x0071)",
        "bytes": bytes([0x41, 0x48, 0x00, 0x03, 0x00, 0x71, 0x10, 0x00, 0x00, 0x4D, 0x49]),
        "expected_resp": "0x00B1"
    },
    "REGISTER_SET_VALUE_0x0090": {
        "cmd": "0x0090",
        "description": "SetValueRegisterRequest Reg=0 Val=0 (CMD 0x0090)",
        # CTRL = 2 + 7 = 9 (0x0009), CMD = 0x0090
        # Content: ControlByte=0x81 (NeedReply=1, Func=0, Count=1), RegId=0x0000, Val=0x00000000
        "bytes": bytes([0x41, 0x48, 0x00, 0x09, 0x00, 0x90, 0x81, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x4D, 0x49]),
        "expected_resp": "0x00D0"
    }
}

BAUD_RATES = [115200, 9600, 19200, 38400, 57600, 230400, 460800, 921600]
CONTROL_LINE_STATES = [
    (False, False, "DTR=0 RTS=0 (Windows default)"),
    (True, False,  "DTR=1 RTS=0"),
    (False, True,  "DTR=0 RTS=1"),
    (True, True,   "DTR=1 RTS=1 (Linux default)")
]

def run_single_test(port_name, baud, dtr, rts, frame_name, frame_info, timeout_s=2.0):
    try:
        import serial
    except ImportError:
        return {"error": "pyserial not installed"}

    try:
        ser = serial.Serial(
            port=None,
            baudrate=baud,
            bytesize=8,
            parity='N',
            stopbits=1,
            timeout=timeout_s,
            xonxoff=False,
            rtscts=False,
            dsrdtr=False
        )
        ser.port = port_name
        ser.open()
    except Exception as e:
        return {"error": f"Open failed: {e}"}

    rx_data = bytearray()
    elapsed = 0
    try:
        ser.dtr = dtr
        ser.rts = rts
        time.sleep(0.05)
        ser.reset_input_buffer()
        ser.reset_output_buffer()

        t0 = time.time()
        ser.write(frame_info["bytes"])

        deadline = time.time() + timeout_s
        while time.time() < deadline:
            chunk = ser.read(ser.in_waiting or 1)
            if chunk:
                rx_data.extend(chunk)
                if len(rx_data) >= 10 and rx_data[-2:] == b'\x4D\x49':
                    break
            time.sleep(0.01)
        elapsed = time.time() - t0

    except Exception as e:
        return {"error": f"Transmission error: {e}"}
    finally:
        try:
            ser.close()
        except:
            pass

    return {
        "status": "DATA_RECEIVED" if rx_data else "NO_RESPONSE",
        "rx_hex": rx_data.hex(' ').upper() if rx_data else "",
        "rx_len": len(rx_data),
        "elapsed_s": round(elapsed, 4)
    }

def main():
    parser = argparse.ArgumentParser(description="VMAX LCD Automated Protocol Test Harness")
    parser.add_argument("--send", action="store_true", help="Execute live tests on /dev/ttyACM0")
    parser.add_argument("--port", default="/dev/ttyACM0", help="Serial port device")
    parser.add_argument("--timeout", type=float, default=2.0, help="Read timeout per test")
    parser.add_argument("--opcodes-only", action="store_true", help="Test safe opcodes at 115200 8N1 DTR=0 RTS=0 only")
    args = parser.parse_args()

    print("=" * 70)
    print("VMAX LCD AUTOMATED PROTOCOL & CONFIGURATION TEST HARNESS")
    print("=" * 70)
    print(f"PORT:    {args.port}")
    print(f"MODE:    {'LIVE EXECUTION' if args.send else 'DRY RUN / STATIC MATRIX GENERATION'}")
    print(f"TIMEOUT: {args.timeout}s per test")
    print()

    # Generate complete matrix plan
    matrix_plan = []
    if args.opcodes_only:
        for fname, finfo in SAFE_FRAMES.items():
            matrix_plan.append((115200, False, False, fname, finfo))
    else:
        # Phase 1: All safe opcodes at default 115200 DTR=0 RTS=0
        for fname, finfo in SAFE_FRAMES.items():
            matrix_plan.append((115200, False, False, fname, finfo))
        # Phase 2: DTR/RTS sweep on Handshake
        for dtr, rts, desc in CONTROL_LINE_STATES:
            if not (dtr == False and rts == False):
                matrix_plan.append((115200, dtr, rts, "HANDSHAKE_0x0080", SAFE_FRAMES["HANDSHAKE_0x0080"]))
        # Phase 3: Baud rate sweep on Handshake
        for baud in BAUD_RATES:
            if baud != 115200:
                matrix_plan.append((baud, False, False, "HANDSHAKE_0x0080", SAFE_FRAMES["HANDSHAKE_0x0080"]))

    print(f"Total test matrix size: {len(matrix_plan)} combinations.")
    print()

    if not args.send:
        print("DRY RUN SUMMARY:")
        print("----------------------------------------------------------------------")
        print("Test # | Baud   | DTR   | RTS   | Frame                     | CMD")
        print("----------------------------------------------------------------------")
        for idx, (b, d, r, fname, finfo) in enumerate(matrix_plan, 1):
            print(f"{idx:6d} | {b:6d} | {str(d):5s} | {str(r):5s} | {fname:25s} | {finfo['cmd']}")
        print("----------------------------------------------------------------------")
        print("\nTo execute live harness on host: rerun with --send (and sudo if needed).")

        # Save dry run matrix to JSON
        output_file = "/home/tor/pc-case-lcd/init_investigation/safe_opcode_matrix.json"
        with open(output_file, "w") as f:
            json.dump([
                {
                    "test_idx": idx,
                    "baud": b,
                    "dtr": d,
                    "rts": r,
                    "frame_name": fname,
                    "cmd": finfo["cmd"],
                    "description": finfo["description"],
                    "hex": finfo["bytes"].hex(' ').upper()
                } for idx, (b, d, r, fname, finfo) in enumerate(matrix_plan, 1)
            ], f, indent=2)
        print(f"Saved matrix plan to {output_file}")
        return 0

    # Live execution
    if not os.path.exists(args.port):
        print(f"ERROR: Port {args.port} does not exist. (Sandbox detected — run on host system).")
        return 1

    results = []
    rx_found = False

    print("STARTING SYSTEMATIC MATRIX EXECUTION...")
    print("----------------------------------------------------------------------")

    for idx, (b, d, r, fname, finfo) in enumerate(matrix_plan, 1):
        print(f"[{idx}/{len(matrix_plan)}] Testing {fname} @ {b} baud (DTR={d}, RTS={r})... ", end="", flush=True)
        res = run_single_test(args.port, b, d, r, fname, finfo, args.timeout)
        
        test_rec = {
            "test_idx": idx,
            "baud": b,
            "dtr": d,
            "rts": r,
            "frame_name": fname,
            "cmd": finfo["cmd"],
            "tx_hex": finfo["bytes"].hex(' ').upper(),
            "result": res
        }
        results.append(test_rec)

        if "error" in res:
            print(f"ERROR ({res['error']})")
        elif res["status"] == "DATA_RECEIVED":
            print(f"*** DATA RECEIVED! ({res['rx_len']} bytes: {res['rx_hex']}) ***")
            rx_found = True
            break
        else:
            print(f"0 RX ({res['elapsed_s']}s)")

    # Save results
    res_json_path = "/home/tor/pc-case-lcd/init_investigation/bruteforce_results.json"
    with open(res_json_path, "w") as f:
        json.dump(results, f, indent=2)

    print()
    print("=" * 70)
    print("HARNESS EXECUTION COMPLETE")
    print("=" * 70)
    print(f"Total tests executed: {len(results)}")
    print(f"Data received:        {'YES' if rx_found else 'NO (All 0 RX)'}")
    print(f"Results saved to:     {res_json_path}")

    return 0

if __name__ == "__main__":
    sys.exit(main())
