#!/usr/bin/env python3
"""
extract_costura_embedded_assemblies.py
Extracts Costura.Fody embedded resources / DLLs from Vmax.exe.
"""

import os
import sys
import re
import zlib

VMAX_EXE = "/home/tor/vmax_bundle/bin/Release/Vmax.exe"
OUTPUT_DIR = "/home/tor/pc-case-lcd/init_investigation/extracted_resources"

def main():
    print("=" * 60)
    print("COSTURA & EMBEDDED RESOURCE EXTRACTOR — VMAX.EXE")
    print("=" * 60)

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    with open(VMAX_EXE, "rb") as f:
        data = f.read()

    print(f"Read Vmax.exe: {len(data)} bytes ({len(data)/1024/1024:.2f} MB)")

    # Costura resource names often look like 'costura.assemblyname.dll.compressed' or similar
    # Search for 'costura' string references
    costura_matches = re.findall(rb"costura\.[a-z0-9_\-\.]+", data, re.IGNORECASE)
    print(f"Costura resource matches: {set([c.decode(errors='ignore') for c in costura_matches])}")

    # Search for raw Deflate/Zlib headers (0x78 0x9C or 0x78 0x01 or 0x78 0xDA)
    zlib_header_indices = [m.start() for m in re.finditer(rb"\x78[\x01\x9c\xda]", data)]
    print(f"Found {len(zlib_header_indices)} candidate Zlib compressed blocks.")

    decompressed_count = 0
    for idx in zlib_header_indices:
        try:
            # Try decompressing up to 10MB
            decomp = zlib.decompress(data[idx:idx+10*1024*1024])
            if len(decomp) > 1024 and (decomp[:2] == b'MZ' or b'BSJB' in decomp[:500]):
                decompressed_count += 1
                out_name = f"extracted_{decompressed_count}.dll"
                # Try finding original assembly name inside BSJB
                bsjb_idx = decomp.find(b'BSJB')
                if bsjb_idx != -1:
                    name_match = re.search(rb"([A-Za-z0-9_\.]+\.dll)", decomp[bsjb_idx:bsjb_idx+1000])
                    if name_match:
                        out_name = name_match.group(1).decode(errors='ignore')

                out_path = os.path.join(OUTPUT_DIR, out_name)
                with open(out_path, "wb") as f_out:
                    f_out.write(decomp)
                print(f"  Successfully extracted embedded assembly: {out_name} ({len(decomp)} bytes)")
        except Exception:
            pass

    print(f"\nExtraction complete. Extracted {decompressed_count} embedded assemblies to {OUTPUT_DIR}")

if __name__ == "__main__":
    main()
