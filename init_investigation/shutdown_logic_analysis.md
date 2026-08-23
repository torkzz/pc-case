# Shutdown & Lifecycle Logic Analysis Report

## Executive Summary

Static disassembly of `DeviceCommunicationLibrary.dll` and `Vmax.exe` reveals that **no application-level shutdown frame or power-off command is sent by the vendor software**.

There are zero methods in `DeviceCommunicator` that issue a shutdown or standby opcode to the `33c3:f101` device. The only lifecycle commands in the assembly are:
1. `RestartRequest` (CMD `0x0070`): Reboots the MCU core.
2. `ExitRunningRequest` (CMD `0x0063`): Signals exit from running mode (fire-and-forget).
3. `ChangeStatusRequest` (CMD `0x0071`): Transitions mode (`STATUS_AHMI = 0x20`, `STATUS_DOWNLOAD_READY = 0x10`, `STATUS_DOWNLOADING = 0x11`).

## Physical Lifecycle & Timeout Analysis

The physical device exhibits the following autonomous boot sequence powered purely via host USB-C:
1. **T0 (USB-C Plugged In)**: MCU SIE enumerates on host USB as `33c3:f101` (`cdc_acm`).
2. **T1 (Boot GIF)**: Firmware autonomously renders animated boot GIF from internal SPI Flash.
3. **T2 (Static Image)**: Firmware renders static image from internal SPI Flash.
4. **T3 (Display Shutdown)**: Display panel turns off after an autonomous timeout.

## Key Discovery
The display panel shutdown is an **autonomous firmware / hardware display standby timeout**. It is NOT triggered by host serial commands, nor does it drop the USB `33c3:f101` SIE controller.

USB `usbmon` captures confirm that during the entire display lifecycle, `33c3:f101` remains enumerated, `cdc_acm` continuously submits Bulk IN URBs to EP `0x81`, and host Bulk OUT frames on EP `0x02` complete with status `0`.
