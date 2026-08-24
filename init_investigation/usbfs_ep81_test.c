#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <fcntl.h>
#include <unistd.h>
#include <errno.h>
#include <sys/ioctl.h>
#include <linux/usbdevice_fs.h>

int main() {
    printf("=== PHASE 5: RAW USB ENDPOINT TEST (USBDEVFS) ===\n");

    int fd = open("/dev/bus/usb/001/002", O_RDWR);
    if (fd < 0) {
        perror("open /dev/bus/usb/001/002");
        return 1;
    }

    // Detach kernel cdc_acm driver if active
    struct usbdevfs_ioctl command;
    command.ifno = 1; // Interface 1 (CDC Data)
    command.ioctl_code = USBDEVFS_DISCONNECT;
    command.data = NULL;
    int res = ioctl(fd, USBDEVFS_IOCTL, &command);
    printf("Disconnect kernel driver interface 1 result: %d (errno: %d - %s)\n", res, errno, strerror(errno));

    // Claim Interface 1
    int ifnum = 1;
    res = ioctl(fd, USBDEVFS_CLAIMINTERFACE, &ifnum);
    printf("Claim interface 1 result: %d (errno: %d - %s)\n", res, errno, strerror(errno));

    // Initial Bulk IN read on EP 0x81 before TX
    unsigned char rx[512];
    memset(rx, 0, sizeof(rx));
    struct usbdevfs_bulktransfer bulk;
    memset(&bulk, 0, sizeof(bulk));
    bulk.ep = 0x81; // EP 1 IN
    bulk.len = sizeof(rx);
    bulk.timeout = 1000; // 1s timeout
    bulk.data = rx;

    printf("Pre-TX: Reading from Bulk IN EP 0x81 (timeout 1000ms)...\n");
    res = ioctl(fd, USBDEVFS_BULK, &bulk);
    printf("Pre-TX Bulk IN result: %d (errno: %d - %s)\n", res, errno, strerror(errno));

    // Bulk OUT 10B Handshake Frame on EP 0x02
    unsigned char tx[] = {0x41, 0x48, 0x00, 0x02, 0x00, 0x80, 0x00, 0x00, 0x4d, 0x49};
    memset(&bulk, 0, sizeof(bulk));
    bulk.ep = 0x02; // EP 2 OUT
    bulk.len = sizeof(tx);
    bulk.timeout = 1000;
    bulk.data = tx;

    printf("TX Handshake (10B) on Bulk OUT EP 0x02...\n");
    res = ioctl(fd, USBDEVFS_BULK, &bulk);
    printf("Bulk OUT result: %d written (errno: %d - %s)\n", res, errno, strerror(errno));

    // Post-TX Bulk IN read on EP 0x81
    memset(rx, 0, sizeof(rx));
    memset(&bulk, 0, sizeof(bulk));
    bulk.ep = 0x81; // EP 1 IN
    bulk.len = sizeof(rx);
    bulk.timeout = 2000; // 2s timeout
    bulk.data = rx;

    printf("Post-TX: Reading from Bulk IN EP 0x81 (timeout 2000ms)...\n");
    res = ioctl(fd, USBDEVFS_BULK, &bulk);
    printf("Post-TX Bulk IN result: %d bytes (errno: %d - %s)\n", res, errno, strerror(errno));
    if (res > 0) {
        printf("RAW RX DATA (%d bytes): ", res);
        for (int i = 0; i < res; i++) {
            printf("%02X ", rx[i]);
        }
        printf("\n");
    }

    // Re-attach kernel cdc_acm driver
    command.ifno = 1;
    command.ioctl_code = USBDEVFS_CONNECT;
    command.data = NULL;
    ioctl(fd, USBDEVFS_IOCTL, &command);

    close(fd);
    return 0;
}
