# MSDISPLAY NATIVE SDK ASSEMBLY & RECONSTRUCTION ANALYSIS

## 1. Function Reconstruction (`Wrraper_MSDisplaySendPicture` -> `0x180018820`)
- **Binary:** `MSDISPLAYSDKWRRAPER.dll`
- **Entry Point:** `Wrraper_MSDisplaySendPicture` (RVA `0x14a70`, Address `0x180014a70`)
- **Internal Encapsulator:** RVA `0x18820` (Address `0x180018820`)
- **Purpose:** Receives frame struct pointer, calculates worst-case buffer size, allocates 12-byte header + payload buffer, writes 12-byte MSDisplay header (`0x0008100A`, Width, Height, Stride, Flag), copies JPEG image bytes into buffer starting at offset `+12` (`0x0C`), and transmits payload to USB Bulk Endpoint via IOCTL `0x304054` / `usb_bulk_write`.

### Entry Point Assembly (`Wrraper_MSDisplaySendPicture` @ `0x180014a70`)
```assembly
180014a74: cmpl $0x1, 0x93b85(%rip)     ; Verify driver initialized
180014a87: mov 0x4(%rdx), %eax          ; eax = struct->dwHeight (offset +4)
180014a8a: mov (%rdx), %r9d             ; r9d = struct->dwWidth  (offset +0)
180014a8d: mov %r8b, 0x28(%rsp)         ; Stack Arg #6 = bFlag
180014a92: mov 0x8(%rdx), %r8           ; r8 = struct->pImageData (JPEG buffer!)
180014a96: mov %ecx, %edx               ; edx = dwCmd / IOCTL code
180014a98: mov 0x93b79(%rip), %rcx      ; rcx = g_hDeviceHandle
180014a9f: mov %eax, 0x20(%rsp)         ; Stack Arg #5 = dwHeight / wStride
180018820: call 0x180018820             ; Internal encapsulation call
```

### Encapsulation Function Assembly (`0x180018820`)
```assembly
180018820: mov %rbx, 0x10(%rsp)         ; Save non-volatile registers
180018830: sub $0x180, %rsp              ; Allocate 0x180 bytes local stack frame
1800188b5: mov %r12d, %eax              ; eax = Height (r12d = 1920 / 0x780)
1800188b8: mov 0x1e0(%rsp), %esi        ; esi = Stack Arg #5 (0x1e0 = 480 decimal)
1800188bf: imul %esi, %eax              ; eax = Height * 480 (Width Stride)
1800188c2: movzwl 0x140(%rcx), %r15d    ; r15d = Frame Width (wWidth)
1800188ca: shl $0x2, %eax               ; eax = (Height * 480) * 4 (32-bit RGBA pixel size)
1800188cd: movslq %eax, %rbp            ; rbp = Total frame payload size
1800188d0: lea 0xc(%rbp), %rdi          ; rdi = rbp + 12 (12-byte header size)
1800188ee: call 0x18005ec58             ; realloc/malloc(total_payload_size)
1800188f6: mov %rax, %rbx               ; rbx = allocated payload buffer pointer
180018927: movl $0x8100a, (%rbx)        ; pBuffer[0..3]  = Magic Signature 0x0008100A
180018930: mov %r15w, 0x4(%rbx)         ; pBuffer[4..5]  = Width (r15w = 480)
180018935: mov %r12w, 0x6(%rbx)         ; pBuffer[6..7]  = Height (r12w = 1920)
18001893a: mov %si, 0x8(%rbx)           ; pBuffer[8..9]  = Stride (si = 480 or 0)
18001893e: mov %ax, 0xa(%rbx)           ; pBuffer[10..11]= Flag / Quality
180018942: call 0x1800569d0             ; memcpy(pBuffer + 12, pImageData, frame_bytes)
180018974: mov $0x304054, %edx          ; edx = IOCTL 0x304054
18001897e: call DeviceIoControl         ; Transmit payload to USB Endpoint
```

---

## 2. Equivalent C Pseudocode

```c
int Wrraper_MSDisplaySendPicture(
    HANDLE hDevice,            // rcx (g_hDeviceHandle)
    DWORD dwIoctlCode,         // rdx
    FRAME_PARAMS *pParams,     // struct pointer: { dwWidth, dwHeight, pImageData }
    BYTE bFlag                 // r8b
)
{
    DWORD dwWidth  = pParams->dwWidth;   // r9d (480 / 0x01E0)
    DWORD dwHeight = pParams->dwHeight;  // eax (1920 / 0x0780)
    BYTE *pJpegData = pParams->pImageData; // r8 (JPEG byte array)

    // Call internal encapsulator:
    return MSDisplaySendFrameInternal(hDevice, dwIoctlCode, pJpegData, dwWidth, dwHeight, bFlag);
}

int MSDisplaySendFrameInternal(
    HANDLE hDevice,            // rcx
    DWORD dwCmd,               // rdx
    BYTE *pJpegData,           // r8
    DWORD dwWidth,             // r9d
    DWORD dwHeight,            // stack arg 5 (0x20(%rsp))
    BYTE bFlag                 // stack arg 6 (0x28(%rsp))
)
{
    WORD wStride = 480; // esi = 0x1E0

    // Worst-case buffer allocation calculation:
    DWORD alloc_size = (dwHeight * wStride * 4) + 12;
    BYTE *pBuffer = (BYTE*)malloc(alloc_size);

    // Construct 12-byte MSDisplay Header:
    *(DWORD*)(pBuffer + 0x00) = 0x0008100A; // Magic signature
    *(WORD*) (pBuffer + 0x04) = (WORD)dwWidth; // Width (480)
    *(WORD*) (pBuffer + 0x06) = (WORD)dwHeight;// Height (1920)
    *(WORD*) (pBuffer + 0x08) = wStride;       // Stride (480 or 0)
    *(WORD*) (pBuffer + 0x0A) = (WORD)bFlag;   // Flag (1 or 0)

    // Copy JPEG data into buffer after 12-byte header:
    memcpy(pBuffer + 12, pJpegData, jpeg_data_len);

    // Submit payload over USB:
    return DeviceIoControl(hDevice, 0x304054, pBuffer, jpeg_data_len + 12, ...);
}
```

---

## 3. Discrepancy Resolution
- **RAW vs JPEG Payload**: The native SDK receives pre-compressed TurboJPEG data (starting with `FF D8`) in `pImageData`. The `(dwHeight * wStride * 4)` calculation is a worst-case allocation bound. The actual `memcpy` copies the JPEG payload starting at offset `+12` (`0x0C`).
- **IOCTL 0x304054**: Indirect Display Driver IOCTL mapped to USB Bulk OUT EP `0x02` (`33c3:f101`).
- **480 Width Enforcement**: Both Native SDK buffer manager (`wStride = 480` / `0x1E0`) and LCD firmware scanout viewport (`480 × 1920`) enforce the 480-pixel width boundary.
