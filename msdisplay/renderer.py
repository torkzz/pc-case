import os
import time
from PIL import Image, ImageDraw, ImageFont

WIDTH = 460
HEIGHT = 1920

def find_system_font(size=24, bold=True):
    candidates = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/TTF/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/TTF/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
        "/usr/share/fonts/truetype/ubuntu/Ubuntu-B.ttf" if bold else "/usr/share/fonts/truetype/ubuntu/Ubuntu-R.ttf"
    ]
    for font_path in candidates:
        if os.path.exists(font_path):
            try:
                return ImageFont.truetype(font_path, size)
            except Exception:
                pass
    return ImageFont.load_default()

class DashboardRenderer:
    def __init__(self, width=WIDTH, height=HEIGHT):
        self.width = width
        self.height = height
        
        # Pre-load fonts
        self.font_header = find_system_font(size=32, bold=True)
        self.font_title  = find_system_font(size=26, bold=True)
        self.font_val    = find_system_font(size=36, bold=True)
        self.font_sub    = find_system_font(size=20, bold=False)
        self.font_micro  = find_system_font(size=16, bold=False)

    def draw_progress_bar(self, draw, x, y, w, h, pct, fg_color, bg_color=(25, 35, 55), border_color=None):
        draw.rectangle([x, y, x + w - 1, y + h - 1], fill=bg_color, outline=border_color, width=1)
        fill_w = max(0, min(w, int(w * (pct / 100.0))))
        if fill_w > 0:
            draw.rectangle([x, y, x + fill_w - 1, y + h - 1], fill=fg_color)

    def draw_sparkline(self, draw, x, y, w, h, values, min_v=0.0, max_v=100.0, line_color=(0, 220, 255), fill_color=None):
        draw.rectangle([x, y, x + w - 1, y + h - 1], fill=(15, 22, 38), outline=(40, 55, 80), width=1)
        if not values or len(values) < 2:
            return
        
        dx = float(w - 2) / float(len(values) - 1)
        pts = []
        range_v = max_v - min_v if max_v > min_v else 1.0
        
        for i, val in enumerate(values):
            norm = max(0.0, min(1.0, (val - min_v) / float(range_v)))
            px = x + 1 + int(i * dx)
            py = y + h - 2 - int(norm * (h - 4))
            pts.append((px, py))
            
        if fill_color and len(pts) >= 2:
            poly_pts = [(x + 1, y + h - 2)] + pts + [(x + 1 + int((len(values) - 1) * dx), y + h - 2)]
            draw.polygon(poly_pts, fill=fill_color)
            
        for i in range(len(pts) - 1):
            draw.line([pts[i], pts[i+1]], fill=line_color, width=2)

    def render(self, metrics_data):
        img = Image.new('RGB', (self.width, self.height), (10, 16, 28))
        draw = ImageDraw.Draw(img)

        # Main Outer Border
        draw.rectangle([8, 8, self.width - 9, self.height - 9], outline=(0, 180, 240), width=3)

        sys_info = metrics_data['sys_info']
        cpu = metrics_data['cpu']
        ram = metrics_data['ram']
        gpu = metrics_data['gpu']
        storage = metrics_data['storage']
        net = metrics_data['net']
        cpu_temp = metrics_data['cpu_temp']
        hist = metrics_data['history']

        # ----------------------------------------------------
        # TOP HEADER CARD (Y: 20 - 180)
        # ----------------------------------------------------
        draw.rectangle([20, 20, 460, 180], fill=(18, 28, 48), outline=(0, 180, 240), width=2)
        draw.rectangle([20, 20, 460, 70], fill=(0, 140, 210))
        draw.text((35, 30), sys_info['hostname'], fill=(255, 255, 255), font=self.font_header)
        
        clk_str = time.strftime("%H:%M:%S")
        draw.text((35, 85), f"UPTIME: {sys_info['uptime']}", fill=(0, 230, 118), font=self.font_sub)
        draw.text((35, 125), f"KERNEL: {sys_info['kernel']}", fill=(180, 200, 220), font=self.font_micro)
        draw.text((320, 120), clk_str, fill=(255, 215, 0), font=self.font_title)

        # ----------------------------------------------------
        # SECTION 1: CPU MONITOR (Y: 200 - 520)
        # ----------------------------------------------------
        draw.rectangle([20, 200, 460, 520], fill=(18, 28, 48), outline=(0, 200, 255), width=2)
        draw.rectangle([20, 200, 460, 250], fill=(0, 120, 200))
        draw.text((35, 210), "CPU PROCESSOR", fill=(255, 255, 255), font=self.font_title)
        
        cpu_pct = cpu['utilization']
        cpu_color = (0, 230, 118) if cpu_pct < 70 else (255, 170, 0) if cpu_pct < 85 else (255, 23, 68)
        draw.text((35, 265), f"{cpu_pct:.1f}%", fill=cpu_color, font=self.font_val)
        
        if cpu_temp:
            draw.text((280, 275), f"TEMP: {cpu_temp}°C", fill=(255, 170, 0), font=self.font_sub)
            
        load_str = f"LOAD: {cpu['load_avg'][0]}  {cpu['load_avg'][1]}  {cpu['load_avg'][2]}"
        draw.text((35, 325), load_str, fill=(180, 200, 220), font=self.font_micro)
        
        # Progress bar
        self.draw_progress_bar(draw, 35, 360, 410, 30, cpu_pct, cpu_color)
        # Sparkline
        self.draw_sparkline(draw, 35, 405, 410, 95, hist['cpu'], min_v=0.0, max_v=100.0, line_color=(0, 220, 255), fill_color=(0, 80, 120, 80))

        # ----------------------------------------------------
        # SECTION 2: GPU MONITOR (Y: 540 - 860)
        # ----------------------------------------------------
        draw.rectangle([20, 540, 460, 860], fill=(18, 28, 48), outline=(118, 255, 3), width=2)
        draw.rectangle([20, 540, 460, 590], fill=(85, 180, 0))
        draw.text((35, 550), "GPU GRAPHICS" if gpu else "GPU N/A", fill=(255, 255, 255), font=self.font_title)
        
        if gpu:
            gpu_pct = gpu['utilization']
            draw.text((35, 605), f"{gpu_pct:.1f}%", fill=(118, 255, 3), font=self.font_val)
            draw.text((280, 615), f"TEMP: {gpu['temp_c']}°C", fill=(255, 170, 0), font=self.font_sub)
            vram_str = f"VRAM: {gpu['vram_used_gb']} / {gpu['vram_total_gb']} GB ({gpu['vram_pct']}%)"
            draw.text((35, 665), vram_str, fill=(180, 200, 220), font=self.font_micro)
            self.draw_progress_bar(draw, 35, 700, 410, 30, gpu['vram_pct'], (118, 255, 3))
            self.draw_sparkline(draw, 35, 745, 410, 95, hist['gpu'], min_v=0.0, max_v=100.0, line_color=(118, 255, 3), fill_color=(40, 100, 0, 80))
        else:
            draw.text((35, 620), "NVIDIA GPU NOT DETECTED", fill=(150, 160, 180), font=self.font_sub)

        # ----------------------------------------------------
        # SECTION 3: RAM MEMORY (Y: 880 - 1200)
        # ----------------------------------------------------
        draw.rectangle([20, 880, 460, 1200], fill=(18, 28, 48), outline=(0, 230, 118), width=2)
        draw.rectangle([20, 880, 460, 930], fill=(0, 180, 90))
        draw.text((35, 890), "RAM MEMORY", fill=(255, 255, 255), font=self.font_title)
        
        ram_pct = ram['pct']
        draw.text((35, 945), f"{ram_pct:.1f}%", fill=(0, 230, 118), font=self.font_val)
        draw.text((260, 955), f"{ram['used_gb']} / {ram['total_gb']} GB", fill=(180, 200, 220), font=self.font_sub)
        self.draw_progress_bar(draw, 35, 1010, 410, 30, ram_pct, (0, 230, 118))
        self.draw_sparkline(draw, 35, 1055, 410, 125, hist['ram'], min_v=0.0, max_v=100.0, line_color=(0, 230, 118), fill_color=(0, 90, 40, 80))

        # ----------------------------------------------------
        # SECTION 4: DISK STORAGE (Y: 1220 - 1460)
        # ----------------------------------------------------
        draw.rectangle([20, 1220, 460, 1460], fill=(18, 28, 48), outline=(255, 170, 0), width=2)
        draw.rectangle([20, 1220, 460, 1270], fill=(210, 140, 0))
        draw.text((35, 1230), "ROOT STORAGE", fill=(255, 255, 255), font=self.font_title)
        
        disk_pct = storage['pct']
        draw.text((35, 1285), f"{disk_pct:.1f}%", fill=(255, 170, 0), font=self.font_val)
        draw.text((260, 1295), f"{storage['used_gb']} / {storage['total_gb']} GB", fill=(180, 200, 220), font=self.font_sub)
        self.draw_progress_bar(draw, 35, 1350, 410, 30, disk_pct, (255, 170, 0))
        draw.text((35, 1400), "MOUNT: / (EXT4/BTRFS)", fill=(180, 200, 220), font=self.font_micro)

        # ----------------------------------------------------
        # SECTION 5: NETWORK TRAFFIC (Y: 1480 - 1800)
        # ----------------------------------------------------
        draw.rectangle([20, 1480, 460, 1800], fill=(18, 28, 48), outline=(247, 37, 133), width=2)
        draw.rectangle([20, 1480, 460, 1530], fill=(200, 25, 100))
        draw.text((35, 1490), "NETWORK TRAFFIC", fill=(255, 255, 255), font=font_title if 'font_title' in locals() else self.font_title)
        
        draw.text((35, 1545), f"RX: {net['rx_mb_s']} MB/s", fill=(0, 230, 118), font=self.font_sub)
        draw.text((260, 1545), f"TX: {net['tx_mb_s']} MB/s", fill=(247, 37, 133), font=self.font_sub)
        
        self.draw_sparkline(draw, 35, 1590, 410, 95, hist['net_rx'], min_v=0.0, max_v=max(5.0, max(hist['net_rx'] or [1.0])), line_color=(0, 230, 118))
        self.draw_sparkline(draw, 35, 1695, 410, 95, hist['net_tx'], min_v=0.0, max_v=max(5.0, max(hist['net_tx'] or [1.0])), line_color=(247, 37, 133))

        # ----------------------------------------------------
        # FOOTER BADGE (Y: 1820 - 1890)
        # ----------------------------------------------------
        draw.rectangle([20, 1820, 460, 1890], fill=(14, 22, 36), outline=(0, 180, 240), width=1)
        draw.text((35, 1835), "VMAX LINUX DRIVER", fill=(0, 200, 255), font=self.font_sub)
        draw.text((300, 1835), "480x1920 NATIVE", fill=(180, 200, 220), font=self.font_sub)

        return img
