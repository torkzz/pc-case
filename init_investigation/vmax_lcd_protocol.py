#!/usr/bin/env python3
"""
HL VMAX PC-Case LCD Protocol Offline Tool (READ-ONLY / NO USB DISPATCH)
Decompiled and Verified from DeviceCommunicationLibrary.dll and MSDISPLAYSDKWRRAPER.dll
"""

import sys
import struct

HEADER = b"AH" # 0x41 0x48
FOOTER = b"MI" # 0x4D 0x49

# Command Opcodes
CMD_HANDSHAKE_REQ          = 0x0080
CMD_HANDSHAKE_RESP         = 0x00C0
CMD_GET_HW_INFO_REQ        = 0x0072
CMD_GET_HW_INFO_RESP        = 0x00B2
CMD_REQUEST_DOWNLOAD_REQ   = 0x0081
CMD_REQUEST_DOWNLOAD_RESP  = 0x00C1
CMD_DOWNLOAD_DATA_REQ      = 0x0082
CMD_DOWNLOAD_DATA_RESP      = 0x00C2
CMD_DOWNLOAD_COMPLETE_REQ  = 0x008F
CMD_DOWNLOAD_COMPLETE_RESP  = 0x00CF
CMD_CHANGE_STATUS_REQ      = 0x0071
CMD_CHANGE_STATUS_RESP      = 0x00B1
CMD_RESTART_REQ            = 0x0070
CMD_RESTART_RESP            = 0x00B0
CMD_EXIT_RUNNING           = 0x0063

def calculate_crc(data: bytes) -> int:
    """
    Standard Modbus / XMODEM CRC16 or sum checksum placeholder per BaseFrame IL.
    In BaseFrame IL: CalculateCRC returns checksum over body (CTRL + CMD + Content).
    """
    crc = 0xFFFF
    for b in data:
        crc ^= b
        for _ in range(8):
            if crc & 1:
                crc = (crc >> 1) ^ 0xA001
            else:
                crc >>= 1
    return crc & 0xFFFF

def build_frame(cmd: int, content: bytes = b"", is_crc_enabled: bool = True) -> bytes:
    """
    Builds a complete AH..MI frame per BaseFrame.ToBytes() IL disassembly.
    
    Layout:
      0..1: HEADER (0x41 0x48 "AH")
      2..3: CTRL (16-bit Big-Endian: ContentLength | (IsCRC << 12))
      4..5: CMD (16-bit Big-Endian Command Opcode)
      6..N: CONTENT (Payload bytes)
      N..N+2: CRC (16-bit Big-Endian calculated over CTRL..Content)
      N+2..N+4: FOOTER (0x4D 0x49 "MI")
    """
    payload_len = len(content)
    # ContentLength in CTRL represents length of CMD (2) + Content (N) + CRC (2) = N + 4 bytes
    content_len_field = payload_len + 4
    ctrl_val = content_len_field & 0x0FFF
    if is_crc_enabled:
        ctrl_val |= (1 << 12)

    ctrl_bytes = ctrl_val.to_bytes(2, 'big')
    cmd_bytes = cmd.to_bytes(2, 'big')
    
    body = ctrl_bytes + cmd_bytes + content
    
    if is_crc_enabled:
        crc_val = calculate_crc(body)
    else:
        crc_val = 0x0000

    crc_bytes = crc_val.to_bytes(2, 'big')
    
    return HEADER + body + crc_bytes + FOOTER

def parse_frame(frame: bytes):
    """
    Parses and validates an AH..MI frame per BaseFrame.Parse() IL disassembly.
    """
    if len(frame) < 10:
        raise ValueError("Frame size too small (< 10 bytes)")
        
    if frame[:2] != HEADER:
        raise ValueError("Invalid Header (expected AH / 0x41 0x48)")
        
    if frame[-2:] != FOOTER:
        raise ValueError("Invalid Footer (expected MI / 0x4D 0x49)")
        
    ctrl_val = int.from_bytes(frame[2:4], 'big')
    cmd_val = int.from_bytes(frame[4:6], 'big')
    crc_val = int.from_bytes(frame[-4:-2], 'big')
    
    content = frame[6:-4]
    
    # Check CRC
    body_for_crc = frame[2:-4]
    calc_crc = calculate_crc(body_for_crc)
    
    return {
        "ctrl": ctrl_val,
        "cmd": hex(cmd_val),
        "content_length": len(content),
        "content_hex": content.hex(),
        "crc": hex(crc_val),
        "crc_valid": (crc_val == calc_crc)
    }

def main():
    print("=== HL VMAX LCD PROTOCOL OFFLINE TEST TOOL ===")
    
    # 1. Generate Handshake Request Frame
    hs_req = build_frame(CMD_HANDSHAKE_REQ)
    print("\n[1] Built Handshake Request Frame (TX):")
    print("Hex Data:", ' '.join(f"{b:02x}" for b in hs_req))
    
    parsed_hs = parse_frame(hs_req)
    print("Parsed Verification:", parsed_hs)
    
    # 2. Simulate Parsing Handshake Response Frame
    # HandshakeResponse content: 4-byte uint32 MaxPackageSize = 4096 (0x00001000)
    mock_hs_resp_content = (4096).to_bytes(4, 'big')
    hs_resp_frame = build_frame(CMD_HANDSHAKE_RESP, mock_hs_resp_content)
    print("\n[2] Simulated Handshake Response Frame (RX):")
    print("Hex Data:", ' '.join(f"{b:02x}" for b in hs_resp_frame))
    
    parsed_resp = parse_frame(hs_resp_frame)
    max_pkg_size = int.from_bytes(bytes.fromhex(parsed_resp["content_hex"]), 'big')
    print("Parsed Verification:", parsed_resp)
    print(f"Decoded MaxPackageSize: {max_pkg_size} bytes")

    # 3. Simulate Parsing Hardware Info Response Frame
    # Layout: IcId (8B ASCII), MaxAcfSize (2B BE uint16), DisplayHeight (2B BE uint16), DisplayWidth (2B BE uint16), ProductId (32B ASCII)
    ic_id = b"VMAX_001" # 8 bytes
    max_acf = (2048).to_bytes(2, 'big') # 2 bytes
    disp_h = (666).to_bytes(2, 'big')   # 2 bytes (666 px)
    disp_w = (2560).to_bytes(2, 'big')  # 2 bytes (2560 px)
    prod_id = b"HL-VMAX-2560x666-SECONDARY-LCD".ljust(32, b'\x00') # 32 bytes
    
    hw_info_content = ic_id + max_acf + disp_h + disp_w + prod_id
    hw_info_frame = build_frame(CMD_GET_HW_INFO_RESP, hw_info_content)
    
    print("\n[3] Simulated GetHardwareInfo Response Frame (RX):")
    print("Hex Data:", ' '.join(f"{b:02x}" for b in hw_info_frame))
    
    parsed_hw = parse_frame(hw_info_frame)
    content_b = bytes.fromhex(parsed_hw["content_hex"])
    res_ic_id = content_b[:8].decode('ascii').strip('\x00')
    res_max_acf = int.from_bytes(content_b[8:10], 'big')
    res_disp_h = int.from_bytes(content_b[10:12], 'big')
    res_disp_w = int.from_bytes(content_b[12:14], 'big')
    res_prod_id = content_b[14:46].decode('ascii').strip('\x00')
    
    print("Decoded Hardware Info:")
    print(f"  IC ID          : {res_ic_id}")
    print(f"  Max ACF Size   : {res_max_acf}")
    print(f"  Display Height : {res_disp_h} px")
    print(f"  Display Width  : {res_disp_w} px")
    print(f"  Product ID     : {res_prod_id}")

if __name__ == "__main__":
    main()
