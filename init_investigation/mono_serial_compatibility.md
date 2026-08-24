# Mono vs Native Windows .NET Serial Compatibility Analysis

## Overview
Evaluation of Mono runtime's `System.IO.Ports.SerialPort` Linux implementation compared to native Windows `.NET`.

## Feature Comparison Matrix

| SerialPort Feature | Windows .NET Implementation | Mono Linux Implementation | Linux System Primatives | Kernel / USB Verification |
| :--- | :--- | :--- | :--- | :--- |
| **Port Opening** | `CreateFileW("\\\\.\\COMx")` | `open("/dev/ttyACM0", O_RDWR)` | `open()` | **PASS**: CDC ACM driver bound |
| **Line Coding (115200 8N1)** | `SetCommState` (DCB) | `tcsetattr` + CDC Control Transfer | `0x21/0x20 SET_LINE_CODING` | **PASS**: Control transfer confirmed in usbmon |
| **DTR / RTS Signaling** | `EscapeCommFunction` (SETDTR/SETRTS) | `ioctl(fd, TIOCMSET)` + CDC Control Transfer | `0x21/0x22 SET_CONTROL_LINE_STATE` | **PASS**: Control transfer confirmed in usbmon |
| **Buffer Flushing** | `PurgeComm` | `tcflush(fd, TCIOFLUSH)` | `tcflush()` | **PASS**: Termios input/output flush confirmed |
| **Read Polling / Events** | Win32 WaitCommEvent | Background thread with `select()` / `poll()` | `select()` | **PASS**: Event handler registration verified |

## Key Conclusion
Mono's `SerialPort` implementation on Linux maps correctly to standard Linux termios and CDC ACM USB control transfers (`0x21/0x20` and `0x21/0x22`). The zero-byte RX behavior is NOT caused by Mono runtime incompatibility.
