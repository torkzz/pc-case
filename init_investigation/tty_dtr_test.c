#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <fcntl.h>
#include <unistd.h>
#include <termios.h>
#include <sys/ioctl.h>

int main() {
    printf("=== TESTING CDC ACM TTY WITH DTR/RTS SIGNALING ===\n");
    int fd = open("/dev/ttyACM0", O_RDWR | O_NOCTTY | O_NDELAY);
    if (fd < 0) {
        perror("open /dev/ttyACM0");
        return 1;
    }

    // Set raw mode & baud
    struct termios options;
    tcgetattr(fd, &options);
    cfsetispeed(&options, B115200);
    cfsetospeed(&options, B115200);
    options.c_cflag |= (CLOCAL | CREAD | CS8);
    options.c_cflag &= ~(PARENB | CSTOPB | CSIZE);
    options.c_lflag &= ~(ICANON | ECHO | ECHOE | ISIG);
    options.c_iflag &= ~(IXON | IXOFF | IXANY | IGNBRK | BRKINT | PARMRK | ISTRIP | INLCR | IGNCR | ICRNL);
    options.c_oflag &= ~OPOST;
    tcsetattr(fd, TCSANOW, &options);

    // Assert DTR & RTS signals via TIOCMSET ioctl
    int status;
    ioctl(fd, TIOCMGET, &status);
    status |= (TIOCM_DTR | TIOCM_RTS);
    ioctl(fd, TIOCMSET, &status);
    printf("Asserted DTR and RTS lines.\n");

    tcflush(fd, TCIOFLUSH);

    unsigned char tx[] = {0x41, 0x48, 0x10, 0x04, 0x00, 0x80, 0x85, 0x44, 0x4d, 0x49};
    printf("TX: 41 48 10 04 00 80 85 44 4d 49\n");
    int w = write(fd, tx, sizeof(tx));
    printf("Wrote %d bytes.\n", w);

    usleep(200000); // 200ms

    unsigned char rx[256];
    memset(rx, 0, sizeof(rx));
    int r = read(fd, rx, sizeof(rx));
    if (r > 0) {
        printf(">>> CDC TTY READ SUCCESS (%d bytes): <<<\n  RX Hex: ", r);
        for (int i = 0; i < r; i++) printf("%02x ", rx[i]);
        printf("\n");
    } else {
        printf("CDC TTY Read: %d (No data / timeout)\n", r);
    }

    close(fd);
    return 0;
}
