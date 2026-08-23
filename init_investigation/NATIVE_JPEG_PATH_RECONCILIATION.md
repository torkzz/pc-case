# NATIVE RAW/JPEG PATH RECONCILIATION REPORT (`NATIVE_JPEG_PATH_RECONCILIATION.md`)

## 1. Discrepancy Resolution Summary
- **Question:** Does the native SDK send raw RGBA pixels or TurboJPEG compressed frame payloads?
- **Conclusion:** **SAME PATH**. The native SDK (`MSDISPLAYSDKWRRAPER.dll`) encodes desktop frames to TurboJPEG via `turbojpeg.dll`, prepends the exact 12-byte MSDisplay header (`0x0008100A`, Width, Height, Stride, Flag), and transmits the payload over USB Bulk OUT.
- **Payload Inspection:** Offset `0x0C` (byte 12) starts with `FF D8` (JPEG SOI marker) followed by `FF FE` (JPEG Comment marker `Lavc`).

---

## 2. Detailed Call Chain & Function Tracing

```
Application (Vmax.exe)
    ↓
Wrraper_MSDisplaySendPicture (RVA 0x14a70)
    ↓ (Passes rdx=struct pointer {wWidth, wHeight, pImageData}, r8b=bFlag)
Internal Payload Encapsulator (RVA 0x18820)
    ↓ (Calculates worst-case buffer size, mallocs total payload size)
Header Construction (RVA 0x18927)
    ├── pBuffer[0..3]   = 0x0008100A (Magic Signature)
    ├── pBuffer[4..5]   = wWidth (480 / 0x01E0)
    ├── pBuffer[6..7]   = wHeight (1920 / 0x0780)
    ├── pBuffer[8..9]   = wStride (0x01E0 / 480 or 0)
    └── pBuffer[10..11] = bFlag (1 or 0)
    ↓
memcpy(pBuffer + 12, pImageData, jpeg_bytes)  (RVA 0x18942)
    ↓
DeviceIoControl (IOCTL 0x304054) / USB Bulk OUT EP 0x02  (RVA 0x1897e)
    ↓
Hardware LCD Controller & JPEG Decoder
```

---

## 3. Disassembly Tracing & Verification

### `Wrraper_MSDisplaySendPicture` Entry Point (`0x180014a70`)
```assembly
180014a74: cmpl $0x1, 0x93b85(%rip)     ; Verify driver initialized
180014a87: mov 0x4(%rdx), %eax          ; eax = Height (from struct +4)
180014a8a: mov (%rdx), %r9d             ; r9d = Width  (from struct +0)
180014a8d: mov %r8b, 0x28(%rsp)         ; stack arg 6 = bFlag
180014a92: mov 0x8(%rdx), %r8           ; r8 = pImageData (from struct +8)
180014a96: mov %ecx, %edx               ; edx = dwCmd / IOCTL code
180014a98: mov 0x93b79(%rip), %rcx      ; rcx = g_hDeviceHandle
180014a9f: mov %eax, 0x20(%rsp)         ; stack arg 5 = Height / Stride
180014aa3: call 0x180018820             ; Encapsulate and transmit frame!
```

### Encapsulation Function (`0x180018820`)
```assembly
1800188b8: mov 0x1e0(%rsp), %esi        ; esi = Stride argument (0x1E0 = 480 decimal)
1800188bf: imul %esi, %eax              ; Max buffer calculation
1800188d0: lea 0xc(%rbp), %rdi          ; Allocation size = buffer_size + 12
1800188ee: call malloc                  ; Allocate header + payload buffer
180018927: movl $0x8100a, (%rbx)        ; Write Magic 0x0008100A
180018930: mov %r15w, 0x4(%rbx)         ; Write Width (480)
180018935: mov %r12w, 0x6(%rbx)         ; Write Height (1920)
18001893a: mov %si, 0x8(%rbx)           ; Write Stride (480 or 0)
18001893e: mov %ax, 0xa(%rbx)           ; Write Flag (1 or 0)
180018942: call memcpy                  ; Copy JPEG bytes to pBuffer + 12
18001897e: call DeviceIoControl         ; Submit to Endpoint 0x02 Bulk OUT
```

---

## 4. Final Protocol Matrix & Layer Summary

| Parameter | Native SDK (`MSDISPLAYSDKWRRAPER.dll`) | Linux Native Driver (`msdisplay/`) | Status |
| :--- | :--- | :--- | :--- |
| **Target Device** | `33c3:f101` / `345f:9132` | `33c3:f101` | `CONFIRMED LIVE` |
| **USB Endpoint** | Bulk OUT `0x02` | Bulk OUT `0x02` (`USBDEVFS_BULK`) | `CONFIRMED LIVE` |
| **Header Magic** | `0x0008100A` (`0a 10 08 00`) | `0x0008100A` (`0a 10 08 00`) | `CONFIRMED STATIC & LIVE` |
| **Header Size** | 12 Bytes | 12 Bytes | `CONFIRMED STATIC & LIVE` |
| **Payload Offset** | Offset `0x0C` (Byte 12) | Offset `0x0C` (Byte 12) | `CONFIRMED STATIC & LIVE` |
| **Payload Format**| TurboJPEG (Starts with `FF D8`) | TurboJPEG (Starts with `FF D8`) | `CONFIRMED STATIC & LIVE` |
| **Width / Height**| 480 × 1920 | 480 × 1920 | `CONFIRMED STATIC & LIVE` |
