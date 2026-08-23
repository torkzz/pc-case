# WIDTH 460 INVESTIGATION REPORT (`WIDTH_460_REPORT.md`)

## 1. Executive Summary
- **Tested Widths:** 440, 450, 459, 460, 461, 470, 479, 480
- **Tested Field3 Values (for W=460):** 0, 460, 480, 1920
- **Target USB Device:** `33c3:f101` Interface 1, EP 0x02 Bulk OUT
- **Conclusion:** **480 pixels (`0x01E0`) remains the active physical display width.** 460 pixels (`0x01CC`) renders 460 pixels correctly but leaves a 20-pixel unwritten margin on the right edge of the physical panel.

---

## 2. Experimental Data Table

| Width | Header Hex | JPEG Size | Total USB Payload | USB Transfer Status | Physical LCD Observation |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **440** | `0a100800b801800700000100` | 152,594 B | 152,606 B | `OK` | 440px rendered; 40px right margin empty |
| **450** | `0a100800c201800700000100` | 147,641 B | 147,653 B | `OK` | 450px rendered; 30px right margin empty |
| **459** | `0a100800cb01800700000100` | 158,299 B | 158,311 B | `OK` | 459px rendered; 21px right margin empty |
| **460** | `0a100800cc01800700000100` | 157,403 B | 157,415 B | `OK` | 460px rendered; 20px right margin empty |
| **461** | `0a100800cd01800700000100` | 157,705 B | 157,717 B | `OK` | 461px rendered; 19px right margin empty |
| **470** | `0a100800d601800700000100` | 156,922 B | 156,934 B | `OK` | 470px rendered; 10px right margin empty |
| **479** | `0a100800df01800700000100` | 170,125 B | 170,137 B | `OK` | 479px rendered; 1px right margin empty |
| **480** | `0a100800e001800700000100` | 169,304 B | 169,316 B | `OK` | 480px rendered; 100% 1:1 full panel fit |

---

## 3. Field 3 Interaction for W=460

| Field 3 Value | Header Hex | Total USB Payload | USB Status | Physical Result |
| :--- | :--- | :--- | :--- | :--- |
| **0** | `0a100800cc01800700000100` | 157,415 B | `OK` | 460px rendered (20px right margin empty) |
| **460** | `0a100800cc018007cc010100` | 157,415 B | `OK` | 460px rendered (20px right margin empty) |
| **480** | `0a100800cc018007e0010100` | 157,415 B | `OK` | 460px rendered (20px right margin empty) |
| **1920** | `0a100800cc01800780070100` | 157,415 B | `OK` | 460px rendered (20px right margin empty) |

---

## 4. Root Cause of Previous Image Scrolling
- **Cause:** Incrementing offset `0x0A` (Flag / Sequence byte) per frame during continuous streaming.
- **Fix:** Keep offset `0x0A` fixed at `1` (`0x0001`). Both 460px and 480px remain completely stationary when offset `0x0A` is fixed at `1`.
