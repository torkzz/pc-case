import os, sys, json
from vmax_bruteforce import run_fuzzing_session

def main():
    send_live = "--send" in sys.argv
    device = "/dev/ttyACM0"
    for arg in sys.argv[1:]:
        if arg.startswith("--device="):
            device = arg.split("=", 1)[1]

    # Load discovered opcodes
    with open("/home/tor/pc-case-lcd/discovered_opcodes.json", "r") as f:
        discovered = json.load(f)

    phase3_opcodes = sorted(list(set([item["opcode_dec"] for item in discovered])))
    
    # Phase 4 ranges
    range1 = list(range(0x0050, 0x0091))
    range2 = list(range(0x00A0, 0x00D1))
    
    all_opcodes = sorted(list(set(phase3_opcodes + range1 + range2)))

    items = [{"cmd": cmd, "payload": b"", "ctrl": 2} for cmd in all_opcodes]

    print(f"=== PHASE 3 & 4: DISCOVERED OPCODES & SYSTEMATIC NEIGHBORHOOD FUZZING ===")
    print(f"Total unique opcodes to test: {len(all_opcodes)}")
    print(f"Ranges covered: Discovered ({len(phase3_opcodes)}), 0x0050-0x0090, 0x00A0-0x00D0")

    run_fuzzing_session(
        device=device,
        items=items,
        send=send_live,
        timeout_sec=3.0,
        delay_ms=300,
        use_crc=False,
        log_usbmon=True
    )

if __name__ == "__main__":
    main()
