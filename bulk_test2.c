#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/ioctl.h>
#include <linux/usbdevice_fs.h>

int main() {
    int fd = open("/dev/bus/usb/001/002", O_RDWR);
    if (fd < 0) {
        perror("open /dev/bus/usb/001/002");
        return 1;
    }

    struct usbdevfs_ioctl command;
    command.ifno = 1;
    command.ioctl_code = USBDEVFS_DISCONNECT;
    command.data = NULL;
    ioctl(fd, USBDEVFS_IOCTL, &command);

    int ifnum = 1;
    if (ioctl(fd, USBDEVFS_CLAIMINTERFACE, &ifnum) < 0) {
        perror("claim interface 1");
        close(fd);
        return 1;
    }

    unsigned char tx[] = {0x41, 0x48, 0x10, 0x04, 0x00, 0x80, 0x85, 0x44, 0x4d, 0x49};
    struct usbdevfs_bulktransfer bulk;
    memset(&bulk, 0, sizeof(bulk));
    bulk.ep = 0x02; // EP 2 OUT
    bulk.len = sizeof(tx);
    bulk.timeout = 2000;
    bulk.data = tx;

    printf("Writing %d bytes to EP 0x02...\n", bulk.len);
    int res = ioctl(fd, USBDEVFS_BULK, &bulk);
    if (res < 0) {
        perror("bulk OUT error");
    } else {
        printf("Bulk OUT written %d bytes.\n", res);
    }

    unsigned char rx[256];
    memset(&bulk, 0, sizeof(bulk));
    bulk.ep = 0x81; // EP 1 IN
    bulk.len = sizeof(rx);
    bulk.timeout = 2000;
    bulk.data = rx;

    printf("Reading from EP 0x81...\n");
    res = ioctl(fd, USBDEVFS_BULK, &bulk);
    if (res < 0) {
        perror("bulk IN error / timeout");
    } else {
        printf("Bulk IN read %d bytes:\n", res);
        for (int i = 0; i < res; i++) {
            printf("%02x ", rx[i]);
        }
        printf("\n");
    }

    // Reattach cdc_acm
    command.ioctl_code = USBDEVFS_CONNECT;
    ioctl(fd, USBDEVFS_IOCTL, &command);

    close(fd);
    return 0;
}
