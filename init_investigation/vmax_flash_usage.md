# Flash Address Table & Memory Layout (`vmax_flash_usage.md`)

## Confirmed Flash Memory Map (`ProtocolConstants.FlashAddresses`)

Extracted from `DeviceCommunicationLibrary.dll` static initializer (`.cctor`):

| File / Region | Base Address (Hex) | Base Address (Dec) | Size (Bytes) | Size (KB / MB) | Purpose |
|---|---|---|---|---|---|
| `cpu1.bin` | `0x08040000` | 134,479,872 | 614,400 | 600 KB | MCU Secondary Core Firmware |
| `upg_cfg.bin` | `0x080F7000` | 135,229,440 | 4,096 | 4 KB | Upgrade Configuration |
| `cpu0_config.bin` | `0x080F8000` | 135,233,536 | 4,096 | 4 KB | Primary Core Configuration |
| `calibration.bin` | `0x080FB000` | 135,245,824 | 4,096 | 4 KB | Touch / Sensor Calibration Data |
| `EraseStoreSpace.bin` | `0x080FC000` | 135,249,920 | 4,096 | 4 KB | Storage Scratch Area |
| `hwconfig.bin` | `0x080FE000` | 135,258,112 | 4,096 | 4 KB | Hardware Configuration |
| `product.bin` | `0x080FF000` | 135,262,208 | 4,096 | 4 KB | Product / Model Info |
| `Texture.acf` | `0x08100000` | 135,266,304 | 15,728,640 | 15 MB | Default Boot GIF & Image Storage Space |
| `bootloader.bin` | `0x08400000` | 138,149,888 | 0 | — | Bootloader Entry Base Address |
