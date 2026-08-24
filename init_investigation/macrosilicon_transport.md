# MacroSilicon USB Display Transport Analysis

## Native Wrapper Architecture (`MSDISPLAYSDKWRRAPER.dll`)

`MSDISPLAYSDKWRRAPER.dll` is the native C/C++ display driver wrapper for MacroSilicon USB Display controllers.

### Exported C Functions

```c
// Device Enumeration & Control
int Wrraper_MSDisplayGetDeviceList(void* deviceListBuffer, int* deviceCount);
int Wrraper_MSDisplayGetDeviceInfo(void* handle, void* infoBuffer);
int Wrraper_MSDisplayStart(void* handle);
int Wrraper_MSDisplayStop(void* handle);
int Wrraper_MSDisplayPause(void* handle);
int Wrraper_MSDisplayResume(void* handle);

// Display & Frame Streaming
int Wrraper_MSDisplayEnableSDKScreenProcessor(void* handle, bool enable);
int Wrraper_MSDisplaySetVideoParam(void* handle, int width, int height, int fps);
int Wrraper_MSDisplaySendPicture(void* handle, const unsigned char* jpegBuffer, int bufferSize);
int Wrraper_MSDisplayCheckDeviceScreenCapability(void* handle, void* capBuffer);

// Flash & EEPROM Management
int Wrraper_MSDisplayReadSN(void* handle, char* snBuffer, int bufferLen);
int Wrraper_MSDisplayReadEEPROM(void* handle, int address, unsigned char* data, int len);
int Wrraper_MSDisplayWriteEEPROM(void* handle, int address, const unsigned char* data, int len);
int Wrraper_MSDisplayReadFlash(void* handle, int address, unsigned char* data, int len);
int Wrraper_MSDisplayWriteFlash(void* handle, int address, const unsigned char* data, int len);
int Wrraper_MSDisplayFlashErase(void* handle, int address, int len);
```

---

## Driver INF File Analysis (`MSUSBDisplay.inf`)

- **Manufacturer**: `MS` (MacroSilicon)
- **Device Name**: `MS USB Display`
- **Device ID**: `USB\VID_345F&PID_9132&MI_03`
- **Class**: `MSDisplay` (`ClassGUID = {FB781AAF-9C70-4523-A5DF-642A87ECA567}`)
- **Driver Service**: `libusb0` kernel driver (`libusb0.sys`)
- **Interface Index**: Interface 3 (`MI_03`) of a composite USB device.

---

## Frame Processing & Compression Engine
- `MSDISPLAYSDKWRRAPER.dll` statically links **TurboJPEG / libjpeg-turbo** (`tj3Init`).
- Framebuffers captured from desktop/Vmax scenes are JPEG-compressed in memory and transmitted via Bulk OUT transfers directly to `345f:9132`.
