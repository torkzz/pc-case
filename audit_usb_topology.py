import subprocess

def run(cmd):
    try:
        res = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=10)
        return res.stdout
    except Exception as e:
        return str(e)

out = []
out.append("=== FULL USB TOPOLOGY AUDIT ===")
out.append("\n--- lsusb -nn ---")
out.append(run("lsusb -nn"))

out.append("\n--- lsusb -t ---")
out.append(run("lsusb -t"))

out.append("\n--- SYSFS USB DEVICES ENUMERATION ---")
out.append(run("find /sys/bus/usb/devices/ -maxdepth 2 -name 'idVendor' -o -name 'idProduct' -o -name 'product' -o -name 'manufacturer' | xargs -n1 -I{} sh -c 'echo -n \"{} \"; cat {}'"))

out.append("\n--- KERNEL DMESG USB MESSAGES ---")
out.append(run("dmesg | grep -iE 'usb|33c3|f101|345f|9132|cdc_acm' | tail -n 40"))

with open("/home/tor/pc-case-lcd/current_usb_topology.txt", "w") as f:
    f.write("\n".join(out))

print("Saved /home/tor/pc-case-lcd/current_usb_topology.txt")
