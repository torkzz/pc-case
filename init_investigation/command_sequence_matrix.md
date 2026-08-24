# Command Sequence Matrix Execution Report

## Execution Summary

| Seq | Command Chain | TX Count | Bulk OUT URBs | Bulk IN URBs | Int IN URBs | Total RX Bytes | Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| A | handshake | 1 | 0 | 0 | 0 | 0 | 0 Bytes / Timeout |
| B | hardware_info -> handshake | 2 | 0 | 0 | 0 | 0 | 0 Bytes / Timeout |
| C | handshake -> hardware_info | 2 | 0 | 0 | 0 | 0 | 0 Bytes / Timeout |
| D | restart -> handshake | 2 | 0 | 0 | 0 | 0 | 0 Bytes / Timeout |
| E | change_status -> handshake | 2 | 0 | 0 | 0 | 0 | 0 Bytes / Timeout |
| F | exit_running -> handshake | 2 | 0 | 0 | 0 | 0 | 0 Bytes / Timeout |
| G | restart -> change_status -> handshake | 3 | 0 | 0 | 0 | 0 | 0 Bytes / Timeout |
| H | change_status -> restart -> handshake | 3 | 0 | 0 | 0 | 0 | 0 Bytes / Timeout |
| I | hardware_info -> flash_info -> handshake | 3 | 0 | 0 | 0 | 0 | 0 Bytes / Timeout |

## Detailed Execution Logs & Endpoint URBs

### Sequence A: handshake
#### Application Level TX/RX Log:
```
Exception: [Errno 13] Permission denied: '/dev/ttyACM0'
```
#### Raw usbmon URB Summary:
```
Bulk OUT URBs: 0
Bulk IN URBs: 0
Interrupt IN URBs: 0
```

### Sequence B: hardware_info -> handshake
#### Application Level TX/RX Log:
```
Exception: [Errno 13] Permission denied: '/dev/ttyACM0'
```
#### Raw usbmon URB Summary:
```
Bulk OUT URBs: 0
Bulk IN URBs: 0
Interrupt IN URBs: 0
```

### Sequence C: handshake -> hardware_info
#### Application Level TX/RX Log:
```
Exception: [Errno 13] Permission denied: '/dev/ttyACM0'
```
#### Raw usbmon URB Summary:
```
Bulk OUT URBs: 0
Bulk IN URBs: 0
Interrupt IN URBs: 0
```

### Sequence D: restart -> handshake
#### Application Level TX/RX Log:
```
Exception: [Errno 13] Permission denied: '/dev/ttyACM0'
```
#### Raw usbmon URB Summary:
```
Bulk OUT URBs: 0
Bulk IN URBs: 0
Interrupt IN URBs: 0
```

### Sequence E: change_status -> handshake
#### Application Level TX/RX Log:
```
Exception: [Errno 13] Permission denied: '/dev/ttyACM0'
```
#### Raw usbmon URB Summary:
```
Bulk OUT URBs: 0
Bulk IN URBs: 0
Interrupt IN URBs: 0
```

### Sequence F: exit_running -> handshake
#### Application Level TX/RX Log:
```
Exception: [Errno 13] Permission denied: '/dev/ttyACM0'
```
#### Raw usbmon URB Summary:
```
Bulk OUT URBs: 0
Bulk IN URBs: 0
Interrupt IN URBs: 0
```

### Sequence G: restart -> change_status -> handshake
#### Application Level TX/RX Log:
```
Exception: [Errno 13] Permission denied: '/dev/ttyACM0'
```
#### Raw usbmon URB Summary:
```
Bulk OUT URBs: 0
Bulk IN URBs: 0
Interrupt IN URBs: 0
```

### Sequence H: change_status -> restart -> handshake
#### Application Level TX/RX Log:
```
Exception: [Errno 13] Permission denied: '/dev/ttyACM0'
```
#### Raw usbmon URB Summary:
```
Bulk OUT URBs: 0
Bulk IN URBs: 0
Interrupt IN URBs: 0
```

### Sequence I: hardware_info -> flash_info -> handshake
#### Application Level TX/RX Log:
```
Exception: [Errno 13] Permission denied: '/dev/ttyACM0'
```
#### Raw usbmon URB Summary:
```
Bulk OUT URBs: 0
Bulk IN URBs: 0
Interrupt IN URBs: 0
```

