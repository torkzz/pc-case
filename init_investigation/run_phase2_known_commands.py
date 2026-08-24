import os, sys, time, struct, json
from vmax_bruteforce import run_fuzzing_session

KNOWN_COMMANDS = [0x0062, 0x0071, 0x0072, 0x0080, 0x0082, 0x0085]

PAYLOADS = [
    ("Empty", b""),
    ("1B 0x00", b"\x00"),
    ("1B 0x01", b"\x01"),
    ("1B 0xFF", b"\xFF"),
    ("2B 00 00", b"\x00\x00"),
    ("2B FF FF", b"\xFF\xFF"),
    ("4B 00 00 00 00", b"\x00\x00\x00\x00"),
    ("4B FF FF FF FF", b"\xFF\xFF\xFF\xFF")
]

def main():
    send_live = "--send" in sys.argv
    device = "/dev/ttyACM0"
    for arg in sys.argv[1:]:
        if arg.startswith("--device="):
            device = arg.split("=", 1)[1]

    items = []
    for cmd in KNOWN_COMMANDS:
        for label, payload in PAYLOADS:
            items.append({
                "cmd": cmd,
                "payload": payload,
                "ctrl": 2 + len(payload),
                "label": label
            })

    print(f"=== PHASE 2: TESTING KNOWN COMMAND FAMILY ===")
    print(f"Commands ({len(KNOWN_COMMANDS)}): {[hex(c) for c in KNOWN_COMMANDS]}")
    print(f"Payloads per command ({len(PAYLOADS)})")
    print(f"Total tests: {len(items)}")

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
