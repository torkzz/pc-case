import sys
from vmax_bruteforce import run_fuzzing_session

KNOWN_COMMANDS = [0x0062, 0x0071, 0x0072, 0x0080, 0x0082, 0x0085]

def main():
    send_live = "--send" in sys.argv
    device = "/dev/ttyACM0"

    items = []
    for cmd in KNOWN_COMMANDS:
        # Test CRC enabled bit (0x8002) with 0x0000 CRC
        items.append({"cmd": cmd, "payload": b"", "ctrl": 0x8002})

    print("=== PHASE 5: TESTING KNOWN COMMANDS WITH CRC BIT ENABLED (CTRL | 0x8000) ===")
    run_fuzzing_session(
        device=device,
        items=items,
        send=send_live,
        timeout_sec=3.0,
        delay_ms=300,
        use_crc=True,
        log_usbmon=True
    )

if __name__ == "__main__":
    main()
