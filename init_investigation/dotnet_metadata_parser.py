#!/usr/bin/env python3
"""
dotnet_metadata_parser.py
Direct binary parser for .NET Portable Executable (PE) CLI metadata streams.
Parses #US (User Strings), #Strings, #Blob, and Metadata tables from Vmax.exe.
"""

import os
import sys
import struct
import json
import re

def parse_pe_cli_metadata(filepath):
    with open(filepath, "rb") as f:
        data = f.read()

    # Verify DOS header 'MZ'
    if data[:2] != b'MZ':
        return {"error": "Not a valid PE file (missing MZ signature)"}

    # e_lfanew offset
    e_lfanew = struct.unpack_from("<I", data, 0x3C)[0]
    
    # Check PE signature 'PE\0\0'
    if data[e_lfanew:e_lfanew+4] != b'PE\x00\x00':
        return {"error": "Not a valid PE file (missing PE signature)"}

    coff_header_offset = e_lfanew + 4
    num_sections = struct.unpack_from("<H", data, coff_header_offset + 2)[0]
    opt_header_size = struct.unpack_from("<H", data, coff_header_offset + 16)[0]
    opt_header_offset = coff_header_offset + 20
    
    magic = struct.unpack_from("<H", data, opt_header_offset)[0]
    is_pe32_plus = (magic == 0x20B)

    # Data directories: CLI Header is DataDirectory[14]
    cli_dir_offset = opt_header_offset + (112 if is_pe32_plus else 96) + (14 * 8)
    cli_rva, cli_size = struct.unpack_from("<II", data, cli_dir_offset)

    if cli_rva == 0 or cli_size == 0:
        return {"error": "No CLI Header found in executable"}

    # Section Headers
    section_headers_offset = opt_header_offset + opt_header_size
    sections = []
    for i in range(num_sections):
        s_off = section_headers_offset + (i * 40)
        s_name = data[s_off:s_off+8].rstrip(b'\x00').decode('ascii', errors='ignore')
        s_vsize, s_rva, s_raw_size, s_raw_ptr = struct.unpack_from("<IIII", data, s_off + 8)
        sections.append({
            "name": s_name,
            "vsize": s_vsize,
            "rva": s_rva,
            "raw_size": s_raw_size,
            "raw_ptr": s_raw_ptr
        })

    def rva_to_offset(rva):
        for s in sections:
            if s["rva"] <= rva < s["rva"] + s["vsize"]:
                return s["raw_ptr"] + (rva - s["rva"])
        return None

    cli_header_file_offset = rva_to_offset(cli_rva)
    if cli_header_file_offset is None:
        return {"error": "Could not map CLI Header RVA to file offset"}

    cb, major_ver, minor_ver = struct.unpack_from("<IHH", data, cli_header_file_offset)
    meta_rva, meta_size = struct.unpack_from("<II", data, cli_header_file_offset + 8)

    meta_file_offset = rva_to_offset(meta_rva)
    if meta_file_offset is None:
        return {"error": "Could not map Metadata Header RVA to file offset"}

    # Metadata Header parsing
    magic_meta = struct.unpack_from("<I", data, meta_file_offset)[0]
    if magic_meta != 0x424A5342: # BSJB (0x424A5342)
        return {"error": f"Invalid Metadata Header signature: 0x{magic_meta:08X}"}

    version_len = struct.unpack_from("<I", data, meta_file_offset + 12)[0]
    version_str = data[meta_file_offset+16:meta_file_offset+16+version_len].rstrip(b'\x00').decode('ascii', errors='ignore')

    streams_offset = meta_file_offset + 16 + version_len
    # Align to 4 bytes
    if (16 + version_len) % 4 != 0:
        streams_offset += 4 - ((16 + version_len) % 4)

    flags, num_streams = struct.unpack_from("<HH", data, streams_offset)
    stream_headers_offset = streams_offset + 4

    streams = {}
    cur_off = stream_headers_offset
    for _ in range(num_streams):
        s_offset, s_size = struct.unpack_from("<II", data, cur_off)
        name_bytes = bytearray()
        c_idx = cur_off + 8
        while data[c_idx] != 0:
            name_bytes.append(data[c_idx])
            c_idx += 1
        c_idx += 1
        # Align to 4 bytes
        pad = (4 - ((c_idx - cur_off) % 4)) % 4
        cur_off = c_idx + pad
        s_name = name_bytes.decode('ascii', errors='ignore')
        streams[s_name] = {
            "file_offset": meta_file_offset + s_offset,
            "size": s_size
        }

    # Extract #US (User Strings)
    user_strings = []
    if "#US" in streams:
        us_off = streams["#US"]["file_offset"]
        us_end = us_off + streams["#US"]["size"]
        u_ptr = us_off + 1 # skip first 0 byte
        while u_ptr < us_end:
            # Read 7-bit encoded int for length
            length_byte = data[u_ptr]
            u_ptr += 1
            if length_byte == 0:
                continue
            if length_byte & 0x80:
                # 2 or 4 byte length
                if (length_byte & 0xC0) == 0x80:
                    str_len = ((length_byte & 0x3F) << 8) | data[u_ptr]
                    u_ptr += 1
                else:
                    str_len = ((length_byte & 0x1F) << 24) | (data[u_ptr] << 16) | (data[u_ptr+1] << 8) | data[u_ptr+2]
                    u_ptr += 3
            else:
                str_len = length_byte

            if str_len > 0 and u_ptr + str_len <= us_end:
                raw_str_bytes = data[u_ptr:u_ptr+str_len-1] # last byte is terminal flag
                try:
                    s_val = raw_str_bytes.decode('utf-16le')
                    user_strings.append(s_val)
                except:
                    pass
                u_ptr += str_len

    # Extract #Strings
    string_heap = []
    if "#Strings" in streams:
        st_off = streams["#Strings"]["file_offset"]
        st_end = st_off + streams["#Strings"]["size"]
        s_bytes = data[st_off:st_end].split(b'\x00')
        for sb in s_bytes:
            if len(sb) >= 2:
                try:
                    string_heap.append(sb.decode('utf-8'))
                except:
                    pass

    return {
        "assembly": filepath,
        "clr_version": version_str,
        "streams": list(streams.keys()),
        "user_strings": sorted(list(set(user_strings))),
        "string_heap_sample": sorted(list(set(string_heap)))
    }

def main():
    vmax_meta = parse_pe_cli_metadata("/home/tor/vmax_bundle/bin/Release/Vmax.exe")
    dcl_meta = parse_pe_cli_metadata("/home/tor/vmax_bundle/bin/Release/DeviceCommunicationLibrary.dll")

    output_dir = "/home/tor/pc-case-lcd/init_investigation"
    os.makedirs(output_dir, exist_ok=True)

    with open(os.path.join(output_dir, "vmax_user_strings.json"), "w") as f:
        json.dump(vmax_meta, f, indent=2)

    with open(os.path.join(output_dir, "dcl_user_strings.json"), "w") as f:
        json.dump(dcl_meta, f, indent=2)

    print("Vmax meta:", vmax_meta)
    print("DCL meta:", dcl_meta)
    print(f"Extracted {len(vmax_meta.get('user_strings', []))} User Strings from Vmax.exe")
    print(f"Extracted {len(dcl_meta.get('user_strings', []))} User Strings from DeviceCommunicationLibrary.dll")

if __name__ == "__main__":
    main()
