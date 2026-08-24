il_comm = open("DeviceCommunicationLibrary.il", "r", encoding="utf-8", errors="ignore").read()

import re

# Find all nested state machine classes
sm_classes = re.findall(r'\.class nested [^{]+\'<[^\'>]+\>d__\d+\'[^{]*\{', il_comm)

print(f"Found {len(sm_classes)} async state machine classes.")
for smc in sm_classes:
    print(" ", smc.strip())

def print_sm_movenext(sm_name):
    print(f"\n==========================================")
    print(f"=== STATE MACHINE: {sm_name} ===")
    print(f"==========================================")
    pattern = r'\.class nested [^{]+' + re.escape(sm_name) + r'[^{]*\{'
    match = re.search(pattern, il_comm)
    if not match:
        print("Not found.")
        return
    start_pos = match.start()
    sub_text = il_comm[start_pos:start_pos+30000]
    # Print MoveNext method
    mn_match = re.search(r'\.method private final hidebysig virtual instance default void MoveNext \(\)', sub_text)
    if mn_match:
        mn_pos = mn_match.start()
        print(sub_text[mn_pos:mn_pos+4000])

print_sm_movenext("<ConnectDeviceAsync>d__47")
print_sm_movenext("<SendRequestAsync>d__52")
print_sm_movenext("<HandshakeAsync>d__46")
print_sm_movenext("<ExitRunningAsync>d__48")
