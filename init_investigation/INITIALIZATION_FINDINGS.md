# INITIALIZATION FINDINGS
# HL VMAX 33c3:f101 PC-Case LCD
# Master Reverse Engineering & Physical Evidence Report (2026-08-23)

---

## Executive Summary

**The vendor application uses a dual-engine architecture: AICDisp for CDC ACM telemetry (`33c3:f101` / `DeviceCommunicationLibrary.dll`) [CONFIRMED STATIC & CONFIRMED LIVE] and MSDisplay for live video rendering (`MSDISPLAYSDKWRRAPER.dll` / WinUSB / Indirect Display Driver) [CONFIRMED STATIC].**

---

## CONTROLLED JPEG CHROMA SUBSAMPLING EXPERIMENT MATRIX [CONFIRMED LIVE]

- **SOURCE IMAGE**: 4-quarter block diagnostic pattern (Red, Green, Blue, White).
- **DIMENSIONS**: `2560 x 666`
- **HEADER**: `0a 10 08 00 00 0a 9a 02 00 00 00 00` (`0x0008100A`, W=2560, H=666)
- **TARGET**: `33c3:f101` Interface 1 Endpoint 0x02 Bulk OUT (`USBDEVFS_BULK`)

| Test | Subsampling Mode | JPEG Size | Total Payload | USB Result Code | Physical Observation | Status |
|---|---|---|---|---|---|---|
| **TEST 1** | YUV 4:2:0 (`yuv420p`) | 27,063 bytes | 27,075 bytes | `27075` OK [CONFIRMED LIVE] | NOT_MACHINE_OBSERVABLE | EXECUTED |
| **TEST 2** | YUV 4:4:4 (`yuv444p`) | 50,049 bytes | 50,061 bytes | `50061` OK [CONFIRMED LIVE] | NOT_MACHINE_OBSERVABLE | EXECUTED |
| **TEST 3** | YUV 4:2:2 (`yuv422p`) | 32,449 bytes | 32,461 bytes | `32461` OK [CONFIRMED LIVE] | NOT_MACHINE_OBSERVABLE | EXECUTED |
| **TEST 4** | YUV 4:0:0 (`gray`) | TBD | TBD | Not Executed | PENDING | UNEXECUTED |

---

## Master Evidence Ledger

| Component / Parameter | Value / Finding | Evidence Level |
|---|---|---|
| **CDC ACM Device** | VID:PID = `33c3:f101`, EP OUT `0x02`, EP IN `0x81` | [CONFIRMED LIVE] |
| **Video Transport DLL** | `MSDISPLAYSDKWRRAPER.dll` / `libusb0.dll` | [CONFIRMED STATIC] |
| **Video Interface & EP** | Interface 1/3, Endpoint `0x02`/`0x04` Bulk OUT | [CONFIRMED STATIC & LIVE] |
| **Frame Header Signature** | `0x0008100A` (DWORD 0 at Offset 0x00) | [CONFIRMED STATIC] |
| **TEST 1 Execution** | 27,075 bytes (YUV 4:2:0) submitted to EP 0x02 Bulk OUT OK | [CONFIRMED LIVE] |
| **TEST 2 Execution** | 50,061 bytes (YUV 4:4:4) submitted to EP 0x02 Bulk OUT OK | [CONFIRMED LIVE] |
| **TEST 3 Execution** | 32,461 bytes (YUV 4:2:2) submitted to EP 0x02 Bulk OUT OK | [CONFIRMED LIVE] |
| **Camera Sensor Check** | `/dev/video*` devices absent | [CONFIRMED LIVE] |
