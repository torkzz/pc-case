#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <fcntl.h>
#include <unistd.h>
#include <errno.h>
#include <sys/ioctl.h>
#include <linux/usbdevice_fs.h>

int main() {
    printf("=== PHASE 8: CRC VARIANT ENDPOINT TEST ===\n");

    int fd = open("/dev/bus/usb/001/002", O_RDWR);
    if (fd < 0) {
        perror("open /dev/bus/usb/001/002");
        return 1;
    }

    int ifnum = 1;
    ioctl(fd, USBDEVFS_CLAIMINTERFACE, &ifnum);

    // Frame A: CRC bit 0 (Standard vendor frame, 10 bytes)
    unsigned char frameA[] = {0x41, 0x48, 0x00, 0x02, 0x00, 0x80, 0x00, 0x00, 0x4d, 0x49};
    // Frame B: CRC bit 1 (CTRL=0x8002, 12 bytes with 00 00 CRC)
    unsigned char frameB[] = {0x41, 0x48, 0x80, 0x02, 0x00, 0x80, 0x00, 0x00, 0x00, 0x00, 0x4d, 0x49};

    struct usbdevfs_bulktransfer bulk;
    unsigned char rx[512];

    printf("\n--- Test Frame A (CRC Bit 0, 10B): 41 48 00 02 00 80 00 00 4D 49 ---\n");
    memset(&bulk, 0, sizeof(bulk));
    bulk.ep = 0x02; bulk.len = sizeof(frameA); bulk.timeout = 1000; bulk.data = frameA;
    int res = ioctl(fd, USBDEVFS_BULK, &bulk);
    printf("TX Frame A Result: %d bytes written\n", res);

    memset(rx, 0, sizeof(rx));
    memset(&bulk, 0, sizeof(bulk));
    bulk.ep = 0x81; bulk.len = sizeof(rx); bulk.timeout = 1000; bulk.data = rx;
    res = ioctl(fd, USBDEVFS_BULK, &bulk);
    printf("RX Frame A Result: %d bytes (errno: %d - %s)\n", res, errno, strerror(errno));

    usleep(500000); // 500ms delay

    printf("\n--- Test Frame B (CRC Bit 1, 12B): 41 48 80 02 00 80 00 00 00 00 4D 49 ---\n");
    memset(&bulk, 0, sizeof(bulk));
    bulk.ep = 0x02; bulk.len = sizeof(frameB); bulk.timeout = 1000; bulk.data = frameB;
    res = ioctl(fd, USBDEVFS_BULK, &bulk);
    printf("TX Frame B Result: %d bytes written\n", res);

    memset(rx, 0, sizeof(rx));
    memset(&bulk, 0, sizeof(bulk));
    bulk.ep = 0x81; bulk.len = sizeof(rx); bulk.timeout = 1000; bulk.data = rx;
    res = ioctl(fd, USBDEVFS_BULK, &bulk);
    printf("RX Frame B Result: %d bytes (errno: %d - %s)\n", res, errno, strerror(errno));

    close(fd);
    return 0;
}
