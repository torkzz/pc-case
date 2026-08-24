# Systematic Command Matrix Execution Report

## Matrix Execution Summary

| Seq | Description | TX Count | Total RX Bytes | usbmon Data Length | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| A | OPEN -> WAIT 100ms -> HANDSHAKE 0x0080 | 1 | 0 | 392192 B | 0 Bytes / Timeout |
| B | OPEN -> WAIT 10ms -> HANDSHAKE | 1 | 0 | 369664 B | 0 Bytes / Timeout |
| C | OPEN -> WAIT 100ms -> HANDSHAKE | 1 | 0 | 391168 B | 0 Bytes / Timeout |
| D | OPEN -> WAIT 500ms -> HANDSHAKE | 1 | 0 | 489472 B | 0 Bytes / Timeout |
| E | OPEN -> DTR ON -> RTS ON -> WAIT 50ms -> HANDSHAKE | 1 | 0 | 384000 B | 0 Bytes / Timeout |
| F | OPEN -> DTR OFF -> RTS OFF -> WAIT 50ms -> HANDSHAKE | 1 | 0 | 386048 B | 0 Bytes / Timeout |
| G | HANDSHAKE -> HARDWARE_INFO | 2 | 0 | 754688 B | 0 Bytes / Timeout |
| H | HANDSHAKE -> CHANGE_STATUS 0x0071 -> HANDSHAKE | 3 | 0 | 1143808 B | 0 Bytes / Timeout |
| I | HANDSHAKE -> RESTART 0x0070 -> WAIT 1s -> HANDSHAKE | 3 | 0 | 1360896 B | 0 Bytes / Timeout |
| J | CHANGE_STATUS -> HANDSHAKE -> HARDWARE_INFO | 3 | 0 | 1143808 B | 0 Bytes / Timeout |
| K | RESTART -> WAIT 100ms -> HANDSHAKE -> HARDWARE_INFO | 3 | 0 | 1143808 B | 0 Bytes / Timeout |
| L | HARDWARE_INFO -> HANDSHAKE | 2 | 0 | 754688 B | 0 Bytes / Timeout |

## Detailed Per-Sequence Logs

### Sequence A: OPEN -> WAIT 100ms -> HANDSHAKE 0x0080
#### Transmission Log:
```json
[
  {
    "time_offset_s": 0.1024,
    "cmd": "HANDSHAKE",
    "frame_hex": "41 48 00 02 00 80 00 00 4d 49",
    "bytes_written": 10
  }
]
```
#### Reception Log:
```
No application RX bytes received.
```

### Sequence B: OPEN -> WAIT 10ms -> HANDSHAKE
#### Transmission Log:
```json
[
  {
    "time_offset_s": 0.0122,
    "cmd": "HANDSHAKE",
    "frame_hex": "41 48 00 02 00 80 00 00 4d 49",
    "bytes_written": 10
  }
]
```
#### Reception Log:
```
No application RX bytes received.
```

### Sequence C: OPEN -> WAIT 100ms -> HANDSHAKE
#### Transmission Log:
```json
[
  {
    "time_offset_s": 0.1023,
    "cmd": "HANDSHAKE",
    "frame_hex": "41 48 00 02 00 80 00 00 4d 49",
    "bytes_written": 10
  }
]
```
#### Reception Log:
```
No application RX bytes received.
```

### Sequence D: OPEN -> WAIT 500ms -> HANDSHAKE
#### Transmission Log:
```json
[
  {
    "time_offset_s": 0.503,
    "cmd": "HANDSHAKE",
    "frame_hex": "41 48 00 02 00 80 00 00 4d 49",
    "bytes_written": 10
  }
]
```
#### Reception Log:
```
No application RX bytes received.
```

### Sequence E: OPEN -> DTR ON -> RTS ON -> WAIT 50ms -> HANDSHAKE
#### Transmission Log:
```json
[
  {
    "time_offset_s": 0.0724,
    "cmd": "HANDSHAKE",
    "frame_hex": "41 48 00 02 00 80 00 00 4d 49",
    "bytes_written": 10
  }
]
```
#### Reception Log:
```
No application RX bytes received.
```

### Sequence F: OPEN -> DTR OFF -> RTS OFF -> WAIT 50ms -> HANDSHAKE
#### Transmission Log:
```json
[
  {
    "time_offset_s": 0.0754,
    "cmd": "HANDSHAKE",
    "frame_hex": "41 48 00 02 00 80 00 00 4d 49",
    "bytes_written": 10
  }
]
```
#### Reception Log:
```
No application RX bytes received.
```

### Sequence G: HANDSHAKE -> HARDWARE_INFO
#### Transmission Log:
```json
[
  {
    "time_offset_s": 0.0023,
    "cmd": "HANDSHAKE",
    "frame_hex": "41 48 00 02 00 80 00 00 4d 49",
    "bytes_written": 10
  },
  {
    "time_offset_s": 1.6033,
    "cmd": "HARDWARE_INFO",
    "frame_hex": "41 48 00 02 00 72 00 00 4d 49",
    "bytes_written": 10
  }
]
```
#### Reception Log:
```
No application RX bytes received.
```

### Sequence H: HANDSHAKE -> CHANGE_STATUS 0x0071 -> HANDSHAKE
#### Transmission Log:
```json
[
  {
    "time_offset_s": 0.003,
    "cmd": "HANDSHAKE",
    "frame_hex": "41 48 00 02 00 80 00 00 4d 49",
    "bytes_written": 10
  },
  {
    "time_offset_s": 1.604,
    "cmd": "CHANGE_STATUS",
    "frame_hex": "41 48 00 03 00 71 01 00 4d 49",
    "bytes_written": 10
  },
  {
    "time_offset_s": 3.2057,
    "cmd": "HANDSHAKE",
    "frame_hex": "41 48 00 02 00 80 00 00 4d 49",
    "bytes_written": 10
  }
]
```
#### Reception Log:
```
No application RX bytes received.
```

### Sequence I: HANDSHAKE -> RESTART 0x0070 -> WAIT 1s -> HANDSHAKE
#### Transmission Log:
```json
[
  {
    "time_offset_s": 0.0022,
    "cmd": "HANDSHAKE",
    "frame_hex": "41 48 00 02 00 80 00 00 4d 49",
    "bytes_written": 10
  },
  {
    "time_offset_s": 1.6032,
    "cmd": "RESTART",
    "frame_hex": "41 48 00 02 00 70 00 00 4d 49",
    "bytes_written": 10
  },
  {
    "time_offset_s": 4.1042,
    "cmd": "HANDSHAKE",
    "frame_hex": "41 48 00 02 00 80 00 00 4d 49",
    "bytes_written": 10
  }
]
```
#### Reception Log:
```
No application RX bytes received.
```

### Sequence J: CHANGE_STATUS -> HANDSHAKE -> HARDWARE_INFO
#### Transmission Log:
```json
[
  {
    "time_offset_s": 0.0023,
    "cmd": "CHANGE_STATUS",
    "frame_hex": "41 48 00 03 00 71 01 00 4d 49",
    "bytes_written": 10
  },
  {
    "time_offset_s": 1.6039,
    "cmd": "HANDSHAKE",
    "frame_hex": "41 48 00 02 00 80 00 00 4d 49",
    "bytes_written": 10
  },
  {
    "time_offset_s": 3.2056,
    "cmd": "HARDWARE_INFO",
    "frame_hex": "41 48 00 02 00 72 00 00 4d 49",
    "bytes_written": 10
  }
]
```
#### Reception Log:
```
No application RX bytes received.
```

### Sequence K: RESTART -> WAIT 100ms -> HANDSHAKE -> HARDWARE_INFO
#### Transmission Log:
```json
[
  {
    "time_offset_s": 0.0026,
    "cmd": "RESTART",
    "frame_hex": "41 48 00 02 00 70 00 00 4d 49",
    "bytes_written": 10
  },
  {
    "time_offset_s": 1.6043,
    "cmd": "HANDSHAKE",
    "frame_hex": "41 48 00 02 00 80 00 00 4d 49",
    "bytes_written": 10
  },
  {
    "time_offset_s": 3.206,
    "cmd": "HARDWARE_INFO",
    "frame_hex": "41 48 00 02 00 72 00 00 4d 49",
    "bytes_written": 10
  }
]
```
#### Reception Log:
```
No application RX bytes received.
```

### Sequence L: HARDWARE_INFO -> HANDSHAKE
#### Transmission Log:
```json
[
  {
    "time_offset_s": 0.003,
    "cmd": "HARDWARE_INFO",
    "frame_hex": "41 48 00 02 00 72 00 00 4d 49",
    "bytes_written": 10
  },
  {
    "time_offset_s": 1.6041,
    "cmd": "HANDSHAKE",
    "frame_hex": "41 48 00 02 00 80 00 00 4d 49",
    "bytes_written": 10
  }
]
```
#### Reception Log:
```
No application RX bytes received.
```

