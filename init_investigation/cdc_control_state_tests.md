# CDC Control & DTR/RTS State Machine Test Report

## Overview
Tested line signal control state transitions (DTR, RTS, timing delays) and monitored `usbmon1` for control requests and endpoint responses.

## Detailed Results Matrix

| Case | Description | Control Transfers | Bulk OUT | Bulk IN URBs | Interrupt IN URBs | RX Byte Count | Result |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| A. open -> no DTR/RTS -> handshake | A. open -> no DTR/RTS -> handshake | 0 | 0 | 0 | 0 | 0 | 0 Bytes RX |
| B. open -> DTR only -> handshake | B. open -> DTR only -> handshake | 0 | 0 | 0 | 0 | 0 | 0 Bytes RX |
| C. open -> RTS only -> handshake | C. open -> RTS only -> handshake | 0 | 0 | 0 | 0 | 0 | 0 Bytes RX |
| D. open -> DTR+RTS -> handshake | D. open -> DTR+RTS -> handshake | 0 | 0 | 0 | 0 | 0 | 0 Bytes RX |
| E. DTR+RTS -> drop both -> wait 100ms -> restore -> handshake | E. DTR+RTS -> drop both -> wait 100ms -> restore -> handshake | 0 | 0 | 0 | 0 | 0 | 0 Bytes RX |
| F. Toggle DTR with delay 0ms -> handshake | F. Toggle DTR with delay 0ms -> handshake | 0 | 0 | 0 | 0 | 0 | 0 Bytes RX |
| F. Toggle DTR with delay 10ms -> handshake | F. Toggle DTR with delay 10ms -> handshake | 0 | 0 | 0 | 0 | 0 | 0 Bytes RX |
| F. Toggle DTR with delay 100ms -> handshake | F. Toggle DTR with delay 100ms -> handshake | 0 | 0 | 0 | 0 | 0 | 0 Bytes RX |
| F. Toggle DTR with delay 500ms -> handshake | F. Toggle DTR with delay 500ms -> handshake | 0 | 0 | 0 | 0 | 0 | 0 Bytes RX |
| F. Toggle DTR with delay 1000ms -> handshake | F. Toggle DTR with delay 1000ms -> handshake | 0 | 0 | 0 | 0 | 0 | 0 Bytes RX |
| F. Toggle DTR with delay 3000ms -> handshake | F. Toggle DTR with delay 3000ms -> handshake | 0 | 0 | 0 | 0 | 0 | 0 Bytes RX |

## Raw Control Transfer Details

### A. open -> no DTR/RTS -> handshake
```
No control events recorded.
```

### B. open -> DTR only -> handshake
```
No control events recorded.
```

### C. open -> RTS only -> handshake
```
No control events recorded.
```

### D. open -> DTR+RTS -> handshake
```
No control events recorded.
```

### E. DTR+RTS -> drop both -> wait 100ms -> restore -> handshake
```
No control events recorded.
```

### F. Toggle DTR with delay 0ms -> handshake
```
No control events recorded.
```

### F. Toggle DTR with delay 10ms -> handshake
```
No control events recorded.
```

### F. Toggle DTR with delay 100ms -> handshake
```
No control events recorded.
```

### F. Toggle DTR with delay 500ms -> handshake
```
No control events recorded.
```

### F. Toggle DTR with delay 1000ms -> handshake
```
No control events recorded.
```

### F. Toggle DTR with delay 3000ms -> handshake
```
No control events recorded.
```

