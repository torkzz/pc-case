import os
import time
from PIL import Image, ImageDraw, ImageFont

WIDTH = 460
HEIGHT = 1920

def find_system_font(size=20, bold=True):
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
        self.font_header = find_system_font(size=26, bold=True)
        self.font_title  = find_system_font(size=22, bold=True)
        self.font_val    = find_system_font(size=28, bold=True)
        self.font_sub    = find_system_font(size=17, bold=False)
        self.font_micro  = find_system_font(size=14, bold=False)

    def draw_progress_bar(self, draw, x, y, w, h, pct, fg_color=(255, 40, 60), bg_color=(45, 12, 18), border_color=None):
        draw.rectangle([x, y, x + w - 1, y + h - 1], fill=bg_color, outline=border_color, width=1)
        fill_w = max(0, min(w, int(w * (pct / 100.0))))
        if fill_w > 0:
            draw.rectangle([x, y, x + fill_w - 1, y + h - 1], fill=fg_color)

    def draw_sparkline(self, draw, x, y, w, h, values, min_v=0.0, max_v=100.0, line_color=(255, 60, 80), fill_color=(100, 15, 25, 100)):
        draw.rectangle([x, y, x + w - 1, y + h - 1], fill=(30, 10, 15), outline=(120, 25, 35), width=1)
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
        # All Red Dark Background
        img = Image.new('RGB', (self.width, self.height), (18, 6, 8))
        draw = ImageDraw.Draw(img)

        # Main Red Outer Border
        draw.rectangle([5, 5, self.width - 6, self.height - 6], outline=(255, 30, 50), width=2)

        sys_info = metrics_data['sys_info']
        cpu = metrics_data['cpu']
        ram = metrics_data['ram']
        gpu = metrics_data['gpu']
        storage = metrics_data['storage']
        net = metrics_data['net']
        cpu_temp = metrics_data['cpu_temp']
        hist = metrics_data['history']

        x0, x1 = 15, 445
        inner_x, inner_w = 28, 404

        # Red Theme Colors
        RED_CARD_BG    = (32, 10, 14)
        RED_HEADER_BG  = (180, 20, 30)
        RED_BORDER     = (255, 40, 60)
        RED_BAR_FG     = (255, 50, 70)
        RED_TEXT_MUTED = (255, 180, 190)
        WHITE_TEXT     = (255, 255, 255)

        # ----------------------------------------------------
        # TOP HEADER CARD (Y: 18 - 175)
        # ----------------------------------------------------
        draw.rectangle([x0, 18, x1, 175], fill=RED_CARD_BG, outline=RED_BORDER, width=2)
        draw.rectangle([x0, 18, x1, 58], fill=RED_HEADER_BG)
        draw.text((28, 24), sys_info['hostname'], fill=WHITE_TEXT, font=self.font_header)
        
        clk_str = time.strftime("%H:%M:%S")
        draw.text((310, 24), clk_str, fill=WHITE_TEXT, font=self.font_title)

        draw.text((28, 68), f"UPTIME: {sys_info['uptime']}", fill=WHITE_TEXT, font=self.font_sub)
        draw.text((28, 96), f"LOCAL IP: {sys_info['ip_local']}", fill=WHITE_TEXT, font=self.font_micro)
        draw.text((28, 118), f"PUBLIC IP: {sys_info['ip_public']}", fill=WHITE_TEXT, font=self.font_micro)
        draw.text((28, 140), f"KERNEL: {sys_info['kernel']}", fill=RED_TEXT_MUTED, font=self.font_micro)

        # ----------------------------------------------------
        # SECTION 1: CPU MONITOR (Y: 190 - 510)
        # ----------------------------------------------------
        draw.rectangle([x0, 190, x1, 510], fill=RED_CARD_BG, outline=RED_BORDER, width=2)
        draw.rectangle([x0, 190, x1, 235], fill=RED_HEADER_BG)
        draw.text((28, 200), "CPU PROCESSOR", fill=WHITE_TEXT, font=self.font_title)
        
        cpu_pct = cpu['utilization']
        draw.text((28, 250), f"{cpu_pct:.1f}%", fill=WHITE_TEXT, font=self.font_val)
        
        # Display CPU Temperature
        cpu_temp_str = f"TEMP: {cpu_temp}°C" if cpu_temp else "TEMP: N/A"
        draw.text((250, 255), cpu_temp_str, fill=WHITE_TEXT, font=self.font_title)
            
        load_str = f"LOAD: {cpu['load_avg'][0]}  {cpu['load_avg'][1]}  {cpu['load_avg'][2]}"
        draw.text((28, 310), load_str, fill=RED_TEXT_MUTED, font=self.font_micro)
        
        self.draw_progress_bar(draw, inner_x, 345, inner_w, 24, cpu_pct, RED_BAR_FG)
        self.draw_sparkline(draw, inner_x, 385, inner_w, 105, hist['cpu'], min_v=0.0, max_v=100.0, line_color=(255, 70, 90), fill_color=(120, 15, 25, 100))

        # ----------------------------------------------------
        # SECTION 2: GPU MONITOR (Y: 525 - 845)
        # ----------------------------------------------------
        draw.rectangle([x0, 525, x1, 845], fill=RED_CARD_BG, outline=RED_BORDER, width=2)
        draw.rectangle([x0, 525, x1, 570], fill=RED_HEADER_BG)
        draw.text((28, 535), "GPU GRAPHICS" if gpu else "GPU N/A", fill=WHITE_TEXT, font=self.font_title)
        
        if gpu:
            gpu_pct = gpu['utilization']
            draw.text((28, 585), f"{gpu_pct:.1f}%", fill=WHITE_TEXT, font=self.font_val)
            draw.text((270, 590), f"TEMP: {gpu['temp_c']}°C", fill=WHITE_TEXT, font=self.font_sub)
            vram_str = f"VRAM: {gpu['vram_used_gb']} / {gpu['vram_total_gb']} GB ({gpu['vram_pct']}%)"
            draw.text((28, 645), vram_str, fill=RED_TEXT_MUTED, font=self.font_micro)
            self.draw_progress_bar(draw, inner_x, 680, inner_w, 24, gpu['vram_pct'], RED_BAR_FG)
            self.draw_sparkline(draw, inner_x, 720, inner_w, 105, hist['gpu'], min_v=0.0, max_v=100.0, line_color=(255, 70, 90), fill_color=(120, 15, 25, 100))
        else:
            draw.text((28, 605), "NVIDIA GPU NOT DETECTED", fill=RED_TEXT_MUTED, font=self.font_sub)

        # ----------------------------------------------------
        # SECTION 3: RAM MEMORY (Y: 860 - 1180)
        # ----------------------------------------------------
        draw.rectangle([x0, 860, x1, 1180], fill=RED_CARD_BG, outline=RED_BORDER, width=2)
        draw.rectangle([x0, 860, x1, 905], fill=RED_HEADER_BG)
        draw.text((28, 870), "RAM MEMORY", fill=WHITE_TEXT, font=self.font_title)
        
        ram_pct = ram['pct']
        draw.text((28, 920), f"{ram_pct:.1f}%", fill=WHITE_TEXT, font=self.font_val)
        draw.text((250, 930), f"{ram['used_gb']} / {ram['total_gb']} GB", fill=WHITE_TEXT, font=self.font_sub)
        self.draw_progress_bar(draw, inner_x, 980, inner_w, 24, ram_pct, RED_BAR_FG)
        self.draw_sparkline(draw, inner_x, 1020, inner_w, 140, hist['ram'], min_v=0.0, max_v=100.0, line_color=(255, 70, 90), fill_color=(120, 15, 25, 100))

        # ----------------------------------------------------
        # SECTION 4: DISK STORAGE (ROOT, HDD1, HDD2) (Y: 1195 - 1500)
        # ----------------------------------------------------
        draw.rectangle([x0, 1195, x1, 1500], fill=RED_CARD_BG, outline=RED_BORDER, width=2)
        draw.rectangle([x0, 1195, x1, 1235], fill=RED_HEADER_BG)
        draw.text((28, 1202), "DISK STORAGE MONITOR", fill=WHITE_TEXT, font=self.font_title)
        
        # Disk 1: Root /
        root_info = storage['root']
        draw.text((28, 1245), f"ROOT (/): {root_info['used_gb']} / {root_info['total_gb']} GB ({root_info['pct']}%)", fill=WHITE_TEXT, font=self.font_micro)
        self.draw_progress_bar(draw, inner_x, 1268, inner_w, 18, root_info['pct'], RED_BAR_FG)

        # Disk 2: HDD1 (/mnt/dd)
        hdd1_info = storage.get('hdd1')
        if hdd1_info:
            draw.text((28, 1298), f"HDD1 (/mnt/dd): {hdd1_info['used_tb']} / {hdd1_info['total_tb']} {hdd1_info['unit']} ({hdd1_info['pct']}%)", fill=WHITE_TEXT, font=self.font_micro)
            self.draw_progress_bar(draw, inner_x, 1321, inner_w, 18, hdd1_info['pct'], RED_BAR_FG)

        # Disk 3: HDD2 (/mnt/dd2)
        hdd2_info = storage.get('hdd2')
        if hdd2_info:
            draw.text((28, 1351), f"HDD2 (/mnt/dd2): {hdd2_info['used_tb']} / {hdd2_info['total_tb']} {hdd2_info['unit']} ({hdd2_info['pct']}%)", fill=WHITE_TEXT, font=self.font_micro)
            self.draw_progress_bar(draw, inner_x, 1374, inner_w, 18, hdd2_info['pct'], RED_BAR_FG)

        draw.text((28, 1465), "FILESYSTEMS: EXT4 / BTRFS", fill=RED_TEXT_MUTED, font=self.font_micro)

        # ----------------------------------------------------
        # SECTION 5: NETWORK TRAFFIC (Y: 1515 - 1815)
        # ----------------------------------------------------
        draw.rectangle([x0, 1515, x1, 1815], fill=RED_CARD_BG, outline=RED_BORDER, width=2)
        draw.rectangle([x0, 1515, x1, 1560], fill=RED_HEADER_BG)
        draw.text((28, 1525), "NETWORK TRAFFIC", fill=WHITE_TEXT, font=self.font_title)
        
        draw.text((28, 1575), f"RX: {net['rx_mb_s']} MB/s", fill=WHITE_TEXT, font=self.font_sub)
        draw.text((250, 1575), f"TX: {net['tx_mb_s']} MB/s", fill=WHITE_TEXT, font=self.font_sub)
        
        self.draw_sparkline(draw, inner_x, 1610, inner_w, 85, hist['net_rx'], min_v=0.0, max_v=max(5.0, max(hist['net_rx'] or [1.0])), line_color=(255, 70, 90), fill_color=(120, 15, 25, 100))
        self.draw_sparkline(draw, inner_x, 1710, inner_w, 85, hist['net_tx'], min_v=0.0, max_v=max(5.0, max(hist['net_tx'] or [1.0])), line_color=(255, 120, 130), fill_color=(150, 20, 30, 100))

        # ----------------------------------------------------
        # FOOTER BADGE (Y: 1825 - 1885)
        # ----------------------------------------------------
        draw.rectangle([x0, 1825, x1, 1885], fill=(24, 8, 10), outline=RED_BORDER, width=1)
        draw.text((28, 1840), "VMAX LINUX DRIVER", fill=WHITE_TEXT, font=self.font_sub)
        draw.text((280, 1840), "460x1920 NATIVE", fill=RED_TEXT_MUTED, font=self.font_sub)

        return img
