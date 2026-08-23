import os
import sys
import time
import socket
import platform
import subprocess
from collections import deque

class RingBuffer:
    def __init__(self, maxlen=30):
        self.buf = deque(maxlen=maxlen)

    def append(self, val):
        self.buf.append(val)

    def get_list(self):
        return list(self.buf)

    def __len__(self):
        return len(self.buf)

class SystemMetricsCollector:
    def __init__(self, history_len=30):
        self.history_len = history_len
        self.prev_cpu_time = None
        self.prev_net_time = None
        self.prev_net_bytes = None
        
        # History buffers for sparklines
        self.history_cpu = RingBuffer(maxlen=history_len)
        self.history_gpu = RingBuffer(maxlen=history_len)
        self.history_ram = RingBuffer(maxlen=history_len)
        self.history_net_rx = RingBuffer(maxlen=history_len)
        self.history_net_tx = RingBuffer(maxlen=history_len)
        self.history_temp_cpu = RingBuffer(maxlen=history_len)

    def get_cpu_metrics(self):
        try:
            with open('/proc/stat', 'r') as f:
                lines = f.readlines()
            
            cpu_line = lines[0].split()
            user, nice, system, idle, iowait, irq, softirq, steal = map(int, cpu_line[1:9])
            idle_time = idle + iowait
            total_time = user + nice + system + idle + iowait + irq + softirq + steal
            
            cpu_pct = 0.0
            if self.prev_cpu_time is not None:
                prev_total, prev_idle = self.prev_cpu_time
                total_diff = total_time - prev_total
                idle_diff = idle_time - prev_idle
                if total_diff > 0:
                    cpu_pct = max(0.0, min(100.0, ((total_diff - idle_diff) / float(total_diff)) * 100.0))
            self.prev_cpu_time = (total_time, idle_time)
            
            # Per-core utilization
            per_core = []
            for line in lines[1:]:
                if line.startswith('cpu') and line[3].isdigit():
                    parts = line.split()
                    c_user, c_nice, c_sys, c_idle = map(int, parts[1:5])
                    c_total = c_user + c_nice + c_sys + c_idle
                    c_used = c_user + c_nice + c_sys
                    c_pct = (c_used / float(c_total) * 100.0) if c_total > 0 else 0.0
                    per_core.append(round(c_pct, 1))
                    
            # Load averages
            load1, load5, load15 = os.getloadavg()
            
            return {
                'utilization': round(cpu_pct, 1),
                'per_core': per_core,
                'load_avg': (round(load1, 2), round(load5, 2), round(load15, 2))
            }
        except Exception:
            return {'utilization': 0.0, 'per_core': [], 'load_avg': (0.0, 0.0, 0.0)}

    def get_memory_metrics(self):
        try:
            mem = {}
            with open('/proc/meminfo', 'r') as f:
                for line in f:
                    parts = line.split(':')
                    if len(parts) == 2:
                        key = parts[0].strip()
                        val = int(parts[1].split()[0])
                        mem[key] = val
            total_kb = mem.get('MemTotal', 1)
            avail_kb = mem.get('MemAvailable', mem.get('MemFree', 0))
            used_kb = total_kb - avail_kb
            pct = max(0.0, min(100.0, (used_kb / float(total_kb)) * 100.0))
            
            swap_total = mem.get('SwapTotal', 0)
            swap_free = mem.get('SwapFree', 0)
            swap_used = swap_total - swap_free
            swap_pct = (swap_used / float(swap_total) * 100.0) if swap_total > 0 else 0.0
            
            return {
                'used_gb': round(used_kb / (1024.0 * 1024.0), 1),
                'total_gb': round(total_kb / (1024.0 * 1024.0), 1),
                'pct': round(pct, 1),
                'swap_pct': round(swap_pct, 1)
            }
        except Exception:
            return {'used_gb': 0.0, 'total_gb': 0.0, 'pct': 0.0, 'swap_pct': 0.0}

    def get_gpu_metrics(self):
        try:
            cmd = ['nvidia-smi', '--query-gpu=utilization.gpu,temperature.gpu,memory.used,memory.total', '--format=csv,noheader,nounits']
            res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=1.0)
            if res.returncode == 0:
                line = res.stdout.strip().split('\n')[0]
                parts = [p.strip() for p in line.split(',')]
                gpu_util = float(parts[0])
                gpu_temp = float(parts[1])
                vram_used_mb = float(parts[2])
                vram_total_mb = float(parts[3])
                vram_pct = (vram_used_mb / vram_total_mb * 100.0) if vram_total_mb > 0 else 0.0
                return {
                    'utilization': round(gpu_util, 1),
                    'temp_c': int(gpu_temp),
                    'vram_used_gb': round(vram_used_mb / 1024.0, 1),
                    'vram_total_gb': round(vram_total_mb / 1024.0, 1),
                    'vram_pct': round(vram_pct, 1)
                }
        except Exception:
            pass
        return None

    def _get_mount_info(self, mount_point, label="ROOT"):
        try:
            if not os.path.exists(mount_point):
                return None
            st = os.statvfs(mount_point)
            total_b = st.f_blocks * st.f_frsize
            if total_b == 0:
                return None
            avail_b = st.f_bavail * st.f_frsize
            used_b = total_b - avail_b
            pct = (used_b / float(total_b) * 100.0) if total_b > 0 else 0.0
            return {
                'label': label,
                'mount': mount_point,
                'used_tb': round(used_b / (1024.0 ** 4), 2) if total_b > (1024.0 ** 4) else round(used_b / (1024.0 ** 3), 1),
                'total_tb': round(total_b / (1024.0 ** 4), 2) if total_b > (1024.0 ** 4) else round(total_b / (1024.0 ** 3), 1),
                'used_gb': round(used_b / (1024.0 ** 3), 1),
                'total_gb': round(total_b / (1024.0 ** 3), 1),
                'avail_gb': round(avail_b / (1024.0 ** 3), 1),
                'unit': 'TB' if total_b > (1024.0 ** 4) else 'GB',
                'pct': round(pct, 1)
            }
        except Exception:
            return None

    def get_storage_metrics(self):
        root = self._get_mount_info('/', 'ROOT') or {'label': 'ROOT', 'mount': '/', 'used_gb': 0.0, 'total_gb': 0.0, 'avail_gb': 0.0, 'pct': 0.0, 'unit': 'GB'}
        hdd1 = self._get_mount_info('/mnt/dd', 'HDD1 (/mnt/dd)')
        hdd2 = self._get_mount_info('/mnt/dd2', 'HDD2 (/mnt/dd2)')
        
        return {
            'root': root,
            'hdd1': hdd1,
            'hdd2': hdd2,
            'pct': root['pct'],
            'used_gb': root['used_gb'],
            'total_gb': root['total_gb']
        }

    def get_network_metrics(self):
        try:
            rx_total, tx_total = 0, 0
            with open('/proc/net/dev', 'r') as f:
                lines = f.readlines()[2:]
            for line in lines:
                parts = line.split(':')
                if len(parts) == 2:
                    iface = parts[0].strip()
                    if iface != 'lo' and not iface.startswith('docker') and not iface.startswith('veth'):
                        cols = parts[1].split()
                        rx_total += int(cols[0])
                        tx_total += int(cols[8])
            
            now = time.monotonic()
            rx_rate_mb, tx_rate_mb = 0.0, 0.0
            if self.prev_net_time is not None:
                dt = now - self.prev_net_time
                if dt > 0:
                    prev_rx, prev_tx = self.prev_net_bytes
                    rx_rate_mb = max(0.0, (rx_total - prev_rx) / (1024.0 * 1024.0 * dt))
                    tx_rate_mb = max(0.0, (tx_total - prev_tx) / (1024.0 * 1024.0 * dt))
            
            self.prev_net_time = now
            self.prev_net_bytes = (rx_total, tx_total)
            return {
                'rx_mb_s': round(rx_rate_mb, 2),
                'tx_mb_s': round(tx_rate_mb, 2)
            }
        except Exception:
            return {'rx_mb_s': 0.0, 'tx_mb_s': 0.0}

    def get_cpu_temp(self):
        try:
            sys_path = '/sys/class/thermal'
            if os.path.exists(sys_path):
                for zone in os.listdir(sys_path):
                    if zone.startswith('thermal_zone'):
                        type_f = os.path.join(sys_path, zone, 'type')
                        temp_f = os.path.join(sys_path, zone, 'temp')
                        if os.path.exists(type_f) and os.path.exists(temp_f):
                            ztype = open(type_f).read().strip().lower()
                            if 'x86_pkg_temp' in ztype or 'cpu' in ztype or 'acpitz' in ztype:
                                temp = int(open(temp_f).read().strip()) // 1000
                                return temp
        except Exception:
            pass
        return None

    def get_system_info(self):
        try:
            with open('/proc/uptime', 'r') as f:
                up_sec = float(f.readline().split()[0])
            days = int(up_sec // 86400)
            hours = int((up_sec % 86400) // 3600)
            mins = int((up_sec % 3600) // 60)
            uptime_str = f"{days}d {hours}h {mins}m" if days > 0 else f"{hours}h {mins}m"
        except Exception:
            uptime_str = "N/A"

        return {
            'hostname': socket.gethostname().upper(),
            'kernel': platform.release(),
            'uptime': uptime_str
        }

    def collect_all(self):
        cpu = self.get_cpu_metrics()
        ram = self.get_memory_metrics()
        gpu = self.get_gpu_metrics()
        storage = self.get_storage_metrics()
        net = self.get_network_metrics()
        cpu_temp = self.get_cpu_temp()
        sys_info = self.get_system_info()

        # Update history buffers
        self.history_cpu.append(cpu['utilization'])
        self.history_ram.append(ram['pct'])
        if gpu:
            self.history_gpu.append(gpu['utilization'])
        if cpu_temp:
            self.history_temp_cpu.append(cpu_temp)
        self.history_net_rx.append(net['rx_mb_s'])
        self.history_net_tx.append(net['tx_mb_s'])

        return {
            'cpu': cpu,
            'ram': ram,
            'gpu': gpu,
            'storage': storage,
            'net': net,
            'cpu_temp': cpu_temp,
            'sys_info': sys_info,
            'history': {
                'cpu': self.history_cpu.get_list(),
                'gpu': self.history_gpu.get_list(),
                'ram': self.history_ram.get_list(),
                'net_rx': self.history_net_rx.get_list(),
                'net_tx': self.history_net_tx.get_list(),
                'temp_cpu': self.history_temp_cpu.get_list()
            }
        }
