# Serial & Line Control Initialization Matrix (`cdc_init_matrix.md`)

## Overview
Tested line configurations (baud rates and DTR/RTS line control states) without transmitting any vendor commands to observe spontaneous transmission or endpoint activity.

## Test Results Matrix

| Config | Description | Control Transfers | Spontaneous RX Bytes | Bulk IN URBs | Interrupt IN URBs | Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| A | 115200 8N1 DTR+RTS | 0 | 0 | 0 | 0 | 0 Bytes Transmitted |
| B | 115200 8N1 DTR only | 0 | 0 | 0 | 0 | 0 Bytes Transmitted |
| C | 115200 8N1 RTS only | 0 | 0 | 0 | 0 | 0 Bytes Transmitted |
| D | 115200 8N1 DTR/RTS disabled | 0 | 0 | 0 | 0 | 0 Bytes Transmitted |
| E | 9600 8N1 DTR+RTS | 0 | 0 | 0 | 0 | 0 Bytes Transmitted |
| F | 57600 8N1 DTR+RTS | 0 | 0 | 0 | 0 | 0 Bytes Transmitted |
| G | 230400 8N1 DTR+RTS | 0 | 0 | 0 | 0 | 0 Bytes Transmitted |

## CDC Control Transfer Logs

### Config A: 115200 8N1 DTR+RTS
```
No control events recorded.
```

### Config B: 115200 8N1 DTR only
```
No control events recorded.
```

### Config C: 115200 8N1 RTS only
```
No control events recorded.
```

### Config D: 115200 8N1 DTR/RTS disabled
```
No control events recorded.
```

### Config E: 9600 8N1 DTR+RTS
```
No control events recorded.
```

### Config F: 57600 8N1 DTR+RTS
```
No control events recorded.
```

### Config G: 230400 8N1 DTR+RTS
```
No control events recorded.
```

