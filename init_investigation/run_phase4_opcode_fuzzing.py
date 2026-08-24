import sys
from vmax_bruteforce import run_fuzzing_session

# Neighborhoods: 0x0050-0x0090 and 0x00A0-0x00D0
opcodes_range_1 = list(range(0x0050, 0x0091))
opcodes_range_2 = list(range(0x00A0, 0x00D1))

all_fuzz_opcodes = sorted(list(set(opcodes_range_1 + opcodes_range_2)))

items = [{"cmd": op, "payload": b""} for op in all_fuzz_opcodes]

print(f"=== PHASE 4: FUZZING {len(items)} OPCODES IN RANGES 0x0050-0x0090 AND 0x00A0-0x00D0 ===")
send_mode = "--send" in sys.argv
run_fuzzing_session("/dev/ttyACM0", items, send=send_mode, timeout_sec=2.0, delay_ms=250, use_crc=False)
