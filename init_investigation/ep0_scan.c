#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/ioctl.h>
#include <linux/usbdevice_fs.h>

void test_req(int fd, unsigned char rtype, unsigned char req, unsigned short val, unsigned short idx, unsigned char *data, int len, const char *label) {
    struct usbdevfs_ctrltransfer ctrl;
    memset(&ctrl, 0, sizeof(ctrl));
    ctrl.bRequestType = rtype;
    ctrl.bRequest     = req;
    ctrl.wValue       = val;
    ctrl.wIndex       = idx;
    ctrl.wLength      = len;
    ctrl.timeout      = 500;
    ctrl.data         = data;

    int res = ioctl(fd, USBDEVFS_CONTROL, &ctrl);
    printf("Test %-45s (0x%02X, 0x%02X, 0x%04X, 0x%04X, len %d): ", label, rtype, req, val, idx, len);
    if (res >= 0) {
        printf("SUCCESS (%d bytes)\n", res);
    } else {
        printf("FAILED (errno %d)\n", res);
    }
}

int main() {
    int fd = open("/dev/bus/usb/001/002", O_RDWR);
    if (fd < 0) {
        perror("open /dev/bus/usb/001/002");
        return 1;
    }

    struct usbdevfs_ioctl command;
    command.ifno = 0; command.ioctl_code = USBDEVFS_DISCONNECT; command.data = NULL; ioctl(fd, USBDEVFS_IOCTL, &command);
    command.ifno = 1; ioctl(fd, USBDEVFS_IOCTL, &command);

    int ifnum0 = 0, ifnum1 = 1;
    ioctl(fd, USBDEVFS_CLAIMINTERFACE, &ifnum0);
    ioctl(fd, USBDEVFS_CLAIMINTERFACE, &ifnum1);

    unsigned char payload[] = {0xA6, 0x01, 0x07, 0x02, 0x00, 0x00, 0x00, 0x00};
    unsigned char line_coding[] = {0x00, 0xC2, 0x01, 0x00, 0x00, 0x00, 0x08}; // 115200 8N1

    printf("=== TESTING CDC & VENDOR CONTROL SETUP REQUESTS ===\n");
    test_req(fd, 0x21, 0x22, 0x0003, 0x0000, NULL, 0, "CDC SET_CONTROL_LINE_STATE (DTR|RTS)");
    test_req(fd, 0x21, 0x20, 0x0000, 0x0000, line_coding, 7, "CDC SET_LINE_CODING (115200 8N1)");
    test_req(fd, 0x40, 0x09, 0x0300, 0x0000, payload, 8, "Vendor Device OUT (0x40/0x09/0x0300)");
    test_req(fd, 0x41, 0x09, 0x0300, 0x0000, payload, 8, "Vendor Interface OUT (0x41/0x09/0x0300)");

    // Test Bulk OUT Handshake right after SET_CONTROL_LINE_STATE
    unsigned char tx[] = {0x41, 0x48, 0x10, 0x04, 0x00, 0x80, 0x85, 0x44, 0x4d, 0x49};
    struct usbdevfs_bulktransfer bulk;
    memset(&bulk, 0, sizeof(bulk));
    bulk.ep = 0x02; bulk.len = sizeof(tx); bulk.timeout = 1000; bulk.data = tx;
    int res = ioctl(fd, USBDEVFS_BULK, &bulk);
    printf("Bulk OUT EP 0x02 result: %d\n", res);

    unsigned char rx[256];
    memset(&bulk, 0, sizeof(bulk));
    bulk.ep = 0x81; bulk.len = sizeof(rx); bulk.timeout = 1000; bulk.data = rx;
    res = ioctl(fd, USBDEVFS_BULK, &bulk);
    printf("Bulk IN EP 0x81 result: %d\n", res);
    if (res > 0) {
        printf("Bulk IN Data: ");
        for (int i = 0; i < res; i++) printf("%02x ", rx[i]);
        printf("\n");
    }

    command.ifno = 0; command.ioctl_code = USBDEVFS_CONNECT; ioctl(fd, USBDEVFS_IOCTL, &command);
    command.ifno = 1; ioctl(fd, USBDEVFS_IOCTL, &command);
    close(fd);
    return 0;
}
