import os, sys, glob, struct

# Script to test PyUSB / libusb direct EP 0x02 bulk OUT dispatch (READ-ONLY PREVIEW / GENERATOR)
# Generates the libusb C / Python snippet for host execution.

TX = bytes.fromhex("41 48 10 04 00 80 85 44 4d 49")
print("Handshake Frame TX:", TX.hex(" "))

