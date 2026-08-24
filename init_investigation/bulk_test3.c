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
    command.ifno = 0; command.ioctl_code = USBDEVFS_DISCONNECT; command.data = NULL;
    ioctl(fd, USBDEVFS_IOCTL, &command);
    command.ifno = 1; ioctl(fd, USBDEVFS_IOCTL, &command);

    int ifnum0 = 0, ifnum1 = 1;
    ioctl(fd, USBDEVFS_CLAIMINTERFACE, &ifnum0);
    ioctl(fd, USBDEVFS_CLAIMINTERFACE, &ifnum1);

    unsigned char tx[] = {0x41, 0x48, 0x10, 0x04, 0x00, 0x80, 0x85, 0x44, 0x4d, 0x49};
    struct usbdevfs_bulktransfer bulk;
    memset(&bulk, 0, sizeof(bulk));
    bulk.ep = 0x02; // EP 2 OUT
    bulk.len = sizeof(tx);
    bulk.timeout = 2000;
    bulk.data = tx;

    printf("Writing 10 bytes to EP 0x02...\n");
    int res = ioctl(fd, USBDEVFS_BULK, &bulk);
    printf("Bulk OUT result: %d\n", res);

    // Read Interrupt EP 0x83
    unsigned char rx[64];
    memset(&bulk, 0, sizeof(bulk));
    bulk.ep = 0x83; // EP 83 IN Interrupt
    bulk.len = sizeof(rx);
    bulk.timeout = 1000;
    bulk.data = rx;

    printf("Reading from Interrupt EP 0x83...\n");
    res = ioctl(fd, USBDEVFS_BULK, &bulk);
    if (res >= 0) {
        printf("EP 0x83 read %d bytes: ", res);
        for (int i = 0; i < res; i++) printf("%02x ", rx[i]);
        printf("\n");
    } else {
        perror("EP 0x83 read");
    }

    // Reattach
    command.ifno = 0; command.ioctl_code = USBDEVFS_CONNECT; ioctl(fd, USBDEVFS_IOCTL, &command);
    command.ifno = 1; ioctl(fd, USBDEVFS_IOCTL, &command);
    close(fd);
    return 0;
}
