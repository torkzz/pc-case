# Download Pipeline & Asset Transfer Analysis

## Overview
Analysis of the `DownloadData` (CMD `0x0082`) pipeline in `DeviceCommunicationLibrary.dll` and its caller chain in `Vmax.exe`.

## Complete Caller Chain for CMD 0x0082

```
Vmax.exe
  │
  └── AICDispSendPicture / AssetManager
        │
        ├── 1. RequestDownloadAsync(mediaType, fileSize, fileName) [CMD 0x0081]
        │     └── Awaits RequestDownloadResponse [CMD 0x00C1] (returns grant & max chunk size)
        │
        ├── 2. DownloadDataAsync(chunkIndex, offset, chunkBytes) [CMD 0x0082]
        │     ├── Splits payload into 512-byte frames
        │     ├── Builds frame: 41 48 [LEN] 00 82 [CHUNK_INDEX(2B) OFFSET(4B) PAYLOAD] [CRC] 4D 49
        │     └── Transmits over SerialPort Bulk OUT (EP 0x02)
        │
        └── 3. DownloadCompleteAsync(fileId, checksum) [CMD 0x008F]
              └── Awaits DownloadCompleteResponse [CMD 0x00CF]
```

## Key Findings & Conclusions
1. **Is CMD 0x0082 a real-time pixel stream?**
   No. CMD 0x0082 is an **asset upload protocol** for storing static image/GIF themes or telemetry layout templates into the `33c3:f101` internal flash memory.
2. **Is CMD 0x0082 invoked during normal execution?**
   Yes, but only when uploading custom user themes, background GIFs, or updating display assets.
3. **What is the primary display transport for live real-time video/frames?**
   Real-time video/display streaming is handled by **`MSDISPLAYSDKWRRAPER.dll`** (`Wrraper_MSDisplaySendPicture`), which targets MacroSilicon USB Display Controllers (`345f:9132`).
