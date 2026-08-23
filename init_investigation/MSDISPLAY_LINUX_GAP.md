# MSDisplay Linux Gap (`MSDISPLAY_LINUX_GAP.md`)

| Windows Vmax Does | Linux Currently Does | Missing Component | Evidence Level |
|---|---|---|---|
| Discovers display device via `Wrraper_MSDisplayGetDeviceList` using GUID `{FB781AAF-9C70-4523-A5DF-642A87ECA567}` | Scans `/dev/ttyACM0` via `pyserial` | Native display device discovery & `libusb0` interface handle | [CONFIRMED STATIC] |
| Claims Interface 3 and sends HID Class control requests (`bmRequestType=0x21`/`0xa1`, `bRequest=0x09`/`0x01`, `wValue=0x0300`) | Sends serial opcodes to `33c3:f101` CDC ACM | MacroSilicon video engine startup & HID setup control transfers | [CONFIRMED STATIC] |
| Enables host screen processor via `Wrraper_MSDisplayEnableSDKScreenProcessor` | Does not enable video processor | Processor activation call | [CONFIRMED STATIC] |
| Encodes desktop frames via TurboJPEG (`tjCompressFromYUV`) and streams to Endpoint 0x04 Bulk OUT via `Wrraper_MSDisplaySendPicture` | Does not stream desktop video frames | Real-time JPEG video frame transport loop over Bulk OUT EP 0x04 | [CONFIRMED STATIC] |
| Display panel remains illuminated continuously by live video stream | Display panel boots, plays SPI Flash boot GIF, renders static image, then turns off (standby timeout) | Active video frame stream over EP 0x04 to prevent panel burn-in auto-off | [CONFIRMED LIVE] |
| Runtime transmission of exact setup & frame header bytes | Aborts Interface 3 write when payload is unverified | Exact control setup payload bytes & frame packet header | [UNKNOWN] |
