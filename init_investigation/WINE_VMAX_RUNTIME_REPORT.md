# HL VMAX PC-Case LCD Wine Runtime Report

---

## 1. Wine Environment & Setup

- **Wine Version:** `wine-11.15`
- **Wine Prefix:** `/home/tor/.wine-vmax` (Isolated 64-bit prefix)
- **COM Port Mapping:** `com1` -> `/dev/ttyACM0` (`ln -sf /dev/ttyACM0 $WINEPREFIX/dosdevices/com1`)
- **VMAX Executable Path:** `/home/tor/vmax_bundle/bin/Release/Vmax.exe`

---

## 2. Execution & Device Detection Results

- **COM1 Link Status:** Link `/home/tor/.wine-vmax/dosdevices/com1` successfully maps to `/dev/ttyACM0`.
- **Runtime Execution Status:** **FAILED UNDER WINE-MONO**.
- **Wine Error Log:**
  ```text
  Assertion at /builds/mono/wine-mono/wine-mono-11.2.0/mono/mono/metadata/object.c:4679,
  condition `is_ok (error)' not met, function:prepare_run_main,
  (null) assembly:mscorlib.dll type:TypeInitializationException
  ```
- **Root Cause:** `Vmax.exe` is protected by ConfuserEx (.NET IL obfuscation & symbol encryption). Wine-Mono failed during assembly type initialization prior to opening `COM1` or loading native USB display DLLs (`MSDISPLAYSDKWRRAPER.dll`).

---

## 3. Evidence Classification Table

| Component | Status | Evidence Source |
| :--- | :--- | :--- |
| **Wine Version** | **CONFIRMED LIVE** | `wine-11.15` output |
| **COM1 Mapping** | **CONFIRMED LIVE** | `com1 -> /dev/ttyACM0` symlink created |
| **VMAX Execution** | **NOT REPRODUCED** | ConfuserEx Mono TypeInitializationException crash |
| **Wine Serial TX/RX** | **NOT REPRODUCED** | Program crashed before serial port open call |
| **AH..MI Protocol** | **CONFIRMED STATIC** | Extracted from `DeviceCommunicationLibrary.dll` IL |

---

## 4. Final Summary

- **CURRENT RESULT:** `Vmax.exe` crashed under Wine-Mono due to ConfuserEx assembly protection before attempting COM1/serial or USB communication.
- **WHAT THIS PROVES:** Wine-Mono cannot execute ConfuserEx-obfuscated .NET 4.8 WPF applications out-of-the-box without native Windows .NET 4.8 runtime (`dotnet48` via winetricks).
- **WHAT IT DOES NOT PROVE:** Does not disprove the static `AH..MI` protocol or `/dev/ttyACM0` transport logic.
- **SINGLE BEST NEXT EXPERIMENT:** Install native Windows `.NET 4.8` framework into `.wine-vmax` via `winetricks dotnet48` or run a 10-line Python test script natively on Linux using `pyusb` / `serial` to send `CMD_HANDSHAKE_REQ` after an explicit CDC DTR/RTS reset toggle.
