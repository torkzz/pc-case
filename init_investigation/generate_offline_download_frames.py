#!/usr/bin/env python3
"""
VMAX Offline Frame Generator & Chunk Verification Tool (Tasks 4 & 5)
Splits JPEG image into DownloadDataRequest (CMD 0x0082) frames, writes binary files,
and verifies byte-for-byte SHA256 reconstruction.
"""

import os
import sys
import glob
import json
import hashlib
from vmax_protocol import build_frame, parse_frame, crc16_modbus

JPEG_PATH = "/home/tor/pc-case-lcd/vmax_test_2560x666.jpg"
OUTPUT_DIR = "/home/tor/pc-case-lcd/generated_frames"
MANIFEST_PATH = os.path.join(OUTPUT_DIR, "frame_manifest.json")

def build_download_data_frame(offset: int, chunk_data: bytes, is_crc: bool = False) -> bytes:
    """
    Builds a DownloadDataRequest frame (CMD 0x0082).
    Payload = Offset (4-byte Big-Endian uint32) + chunk_data.
    """
    offset_bytes = offset.to_bytes(4, 'big')
    content = offset_bytes + chunk_data
    return build_frame(0x0082, content, is_crc_enabled=is_crc)

def generate_and_verify(chunk_size=4000, is_crc=False):
    print("=== TASK 4 & 5: OFFLINE FRAME GENERATION AND VERIFICATION ===")
    if not os.path.exists(JPEG_PATH):
        print(f"Error: {JPEG_PATH} not found!")
        return

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    with open(JPEG_PATH, 'rb') as f:
        jpeg_bytes = f.read()

    orig_sha256 = hashlib.sha256(jpeg_bytes).hexdigest()
    total_len = len(jpeg_bytes)
    print(f"Original JPEG Size: {total_len} bytes | SHA256: {orig_sha256}")

    manifest = {
        "original_jpeg": JPEG_PATH,
        "original_size": total_len,
        "original_sha256": orig_sha256,
        "chunk_size": chunk_size,
        "crc_enabled": is_crc,
        "frames": []
    }

    reconstructed_jpeg = bytearray()
    offset = 0
    frame_idx = 0

    while offset < total_len:
        chunk = jpeg_bytes[offset:offset+chunk_size]
        frame_bin = build_download_data_frame(offset, chunk, is_crc=is_crc)
        
        frame_filename = f"frame_{frame_idx:04d}.bin"
        frame_path = os.path.join(OUTPUT_DIR, frame_filename)
        with open(frame_path, 'wb') as ff:
            ff.write(frame_bin)

        frame_sha256 = hashlib.sha256(frame_bin).hexdigest()

        # Parse & Validate Structural Invariants
        parsed = parse_frame(frame_bin)
        expected_ctrl = (len(chunk) + 6) if not is_crc else ((len(chunk) + 6) | (1 << 12))
        assert parsed["ctrl"] == expected_ctrl, f"CTRL mismatch at frame {frame_idx}: expected {expected_ctrl}, got {parsed['ctrl']}"
        assert int(parsed["cmd"], 16) == 0x0082, f"CMD mismatch at frame {frame_idx}"
        
        extracted_offset = int.from_bytes(parsed["content"][:4], 'big')
        extracted_chunk = parsed["content"][4:]
        assert extracted_offset == offset, f"Offset mismatch at frame {frame_idx}"
        assert extracted_chunk == chunk, f"Chunk data mismatch at frame {frame_idx}"

        reconstructed_jpeg.extend(extracted_chunk)

        manifest["frames"].append({
            "frame_idx": frame_idx,
            "filename": frame_filename,
            "offset": offset,
            "chunk_len": len(chunk),
            "frame_len": len(frame_bin),
            "frame_sha256": frame_sha256
        })

        offset += len(chunk)
        frame_idx += 1

    recon_sha256 = hashlib.sha256(bytes(reconstructed_jpeg)).hexdigest()
    print(f"Reconstructed {frame_idx} chunks into {len(reconstructed_jpeg)} bytes.")
    print(f"Reconstructed SHA256: {recon_sha256}")
    
    assert recon_sha256 == orig_sha256, "RECONSTRUCTION SHA256 MISMATCH!"
    print(">>> ALL STRUCTURAL INVARIANTS AND SHA256 RECONSTRUCTION VERIFIED 100%! <<<")

    with open(MANIFEST_PATH, 'w') as mf:
        json.dump(manifest, mf, indent=2)

    # Print first 3 frames and final frame hex dumps
    print("\n--- HEX DUMPS OF GENERATED FRAMES ---")
    frame_files = sorted(glob.glob(os.path.join(OUTPUT_DIR, "frame_*.bin")))
    selected = frame_files[:3] + [frame_files[-1]] if len(frame_files) >= 4 else frame_files
    for fpath in selected:
        fdata = open(fpath, 'rb').read()
        print(f"\n{os.path.basename(fpath)} ({len(fdata)} bytes):")
        print("  Header :", fdata[:2].hex())
        print("  CTRL   :", fdata[2:4].hex())
        print("  CMD    :", fdata[4:6].hex())
        print("  Offset :", fdata[6:10].hex(), f"(Offset={int.from_bytes(fdata[6:10], 'big')})")
        print("  Data   :", fdata[10:20].hex(), "...", fdata[-6:-4].hex())
        print("  CRC    :", fdata[-4:-2].hex())
        print("  Footer :", fdata[-2:].hex())

if __name__ == "__main__":
    generate_and_verify()
