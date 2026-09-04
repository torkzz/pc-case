#include <stdio.h>
#include <stdlib.h>
#include <libusb-1.0/libusb.h>

int main() {
    libusb_context *ctx = NULL;
    if (libusb_init(&ctx) < 0) {
        printf("libusb_init failed\n");
        return 1;
    }

    libusb_device_handle *handle = libusb_open_device_with_vid_pid(ctx, 0x33c3, 0xf101);
    if (!handle) {
        printf("Could not open 33c3:f101 (Permission issue or device missing)\n");
        libusb_exit(ctx);
        return 1;
    }

    printf("Successfully opened 33c3:f101 via libusb!\n");
    libusb_close(handle);
    libusb_exit(ctx);
    return 0;
}
