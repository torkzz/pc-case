import subprocess

res = subprocess.run(['lsusb', '-v', '-d', '33c3:f101'], capture_output=True, text=True)
print("=== FULL LSUSB -V 33c3:f101 OUTPUT ===")
print(res.stdout)

