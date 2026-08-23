#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/ioctl.h>
#include <linux/usbdevice_fs.h>

int main() {
    printf("=== PHASE 4: LIVE EP0 CONTROL TRANSFER TEST ===\n");
    int fd = open("/dev/bus/usb/001/002", O_RDWR);
    if (fd < 0) {
        perror("open /dev/bus/usb/001/002");
        return 1;
    }

    // Detach cdc_acm temporarily for control test
    struct usbdevfs_ioctl command;
    command.ifno = 0; command.ioctl_code = USBDEVFS_DISCONNECT; command.data = NULL;
    ioctl(fd, USBDEVFS_IOCTL, &command);
    command.ifno = 1; ioctl(fd, USBDEVFS_IOCTL, &command);

    int ifnum0 = 0, ifnum1 = 1;
    ioctl(fd, USBDEVFS_CLAIMINTERFACE, &ifnum0);
    ioctl(fd, USBDEVFS_CLAIMINTERFACE, &ifnum1);

    // Setup EP0 Control Transfer
    // bmRequestType = 0x21 (Host-to-Device | Class | Interface)
    // bRequest      = 0x09 (SET_REPORT)
    // wValue        = 0x0300 (Feature Report ID 0)
    // wIndex        = 0x0000 (Interface 0)
    // wLength       = 8
    unsigned char ep0_payload[] = {0xA6, 0x01, 0x07, 0x02, 0x00, 0x00, 0x00, 0x00};
    struct usbdevfs_ctrltransfer ctrl;
    memset(&ctrl, 0, sizeof(ctrl));
    ctrl.bRequestType = 0x21;
    ctrl.bRequest     = 0x09;
    ctrl.wValue       = 0x0300;
    ctrl.wIndex       = 0x0000;
    ctrl.wLength      = sizeof(ep0_payload);
    ctrl.timeout      = 1000;
    ctrl.data         = ep0_payload;

    printf("Sending EP0 Control Request: 0x21 / 0x09 / 0x0300 / 0x0000 (Payload: A6 01 07 02 00 00 00 00)...\n");
    int res = ioctl(fd, USBDEVFS_CONTROL, &ctrl);
    if (res < 0) {
        perror("EP0 Control Transfer ERROR");
    } else {
        printf("EP0 Control Transfer SUCCESS: %d bytes transferred.\n", res);
    }

    printf("\n=== PHASE 5: HANDSHAKE DISPATCH (BULK OUT 0x02 -> BULK IN 0x81) ===\n");
    unsigned char tx[] = {0x41, 0x48, 0x10, 0x04, 0x00, 0x80, 0x85, 0x44, 0x4d, 0x49};
    struct usbdevfs_bulktransfer bulk;
    memset(&bulk, 0, sizeof(bulk));
    bulk.ep = 0x02; // EP 2 OUT
    bulk.len = sizeof(tx);
    bulk.timeout = 2000;
    bulk.data = tx;

    printf("TX to EP 0x02 OUT: 41 48 10 04 00 80 85 44 4d 49\n");
    res = ioctl(fd, USBDEVFS_BULK, &bulk);
    if (res < 0) {
        perror("Bulk OUT error");
    } else {
        printf("Bulk OUT written %d bytes.\n", res);
    }

    unsigned char rx[256];
    memset(&bulk, 0, sizeof(bulk));
    bulk.ep = 0x81; // EP 1 IN
    bulk.len = sizeof(rx);
    bulk.timeout = 2000;
    bulk.data = rx;

    printf("Reading Bulk IN EP 0x81...\n");
    res = ioctl(fd, USBDEVFS_BULK, &bulk);
    if (res < 0) {
        perror("Bulk IN error / timeout");
    } else {
        printf("Bulk IN READ SUCCESS (%d bytes):\n  RX Hex: ", res);
        for (int i = 0; i < res; i++) {
            printf("%02x ", rx[i]);
        }
        printf("\n");

        if (res >= 10 && rx[0] == 'A' && rx[1] == 'H' && rx[res-2] == 'M' && rx[res-1] == 'I') {
            printf(">>> HANDSHAKE FRAME VALIDATED! <<<\n");
            int cmd = (rx[4] << 8) | rx[5];
            printf("  Response Command: 0x%04X\n", cmd);
            if (res >= 10) {
                unsigned int max_pkg = (rx[6] << 24) | (rx[7] << 16) | (rx[8] << 8) | rx[9];
                printf("  Decoded MaxPackageSize: %u bytes (0x%08X)\n", max_pkg, max_pkg);
            }
        }
    }

    // Reattach cdc_acm driver
    command.ifno = 0; command.ioctl_code = USBDEVFS_CONNECT; ioctl(fd, USBDEVFS_IOCTL, &command);
    command.ifno = 1; ioctl(fd, USBDEVFS_IOCTL, &command);

    close(fd);
    return 0;
}
