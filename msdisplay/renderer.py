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

def format_net_rate(mb_s):
    if mb_s is None or mb_s <= 0:
        return "0.0 KB/s"
    b_s = mb_s * 1024.0 * 1024.0
    if b_s >= 1024.0**3:
        return f"{b_s / (1024.0**3):.1f} GB/s"
    elif b_s >= 1024.0**2:
        return f"{b_s / (1024.0**2):.1f} MB/s"
    elif b_s >= 1024.0:
        return f"{b_s / 1024.0:.1f} KB/s"
    else:
        return f"{b_s:.0f} B/s"

class DashboardRenderer:
    def __init__(self, width=WIDTH, height=HEIGHT):
        self.width = width
        self.height = height
        
        # Pre-load fonts (bumped sizes)
        self.font_header = find_system_font(size=30, bold=True)
        self.font_title  = find_system_font(size=26, bold=True)
        self.font_val    = find_system_font(size=34, bold=True)
        self.font_sub    = find_system_font(size=21, bold=False)
        self.font_micro  = find_system_font(size=17, bold=False)

    def draw_cyberpunk_panel(self, draw, x0, y0, x1, y1, title=None, title_color=(0, 220, 240)):
        BLACK_HUD    = (6, 6, 12)
        NEON_MAGENTA = (255, 0, 128)
        GLOW_MAGENTA = (130, 0, 65)
        CYAN_ACCENT  = (0, 255, 240)
        CYAN_DIM     = (0, 140, 160)

        poly_pts = [
            (x0 + 12, y0),
            (x1 - 12, y0),
            (x1, y0 + 12),
            (x1, y1 - 12),
            (x1 - 12, y1),
            (x0 + 12, y1),
            (x0, y1 - 12),
            (x0, y0 + 12)
        ]

        draw.polygon(poly_pts, fill=BLACK_HUD, outline=NEON_MAGENTA)

        glow_pts = [
            (x0 + 13, y0 + 1),
            (x1 - 13, y0 + 1),
            (x1 - 1, y0 + 13),
            (x1 - 1, y1 - 13),
            (x1 - 13, y1 - 1),
            (x0 + 13, y1 - 1),
            (x0 + 1, y1 - 13),
            (x0 + 1, y0 + 13)
        ]
        draw.polygon(glow_pts, outline=GLOW_MAGENTA)

        draw.line([(x0 + 18, y0 - 1), (x0 + 50, y0 - 1)], fill=CYAN_ACCENT, width=2)
        draw.line([(x0 - 1, y0 + 18), (x0 - 1, y0 + 45)], fill=CYAN_ACCENT, width=2)
        draw.rectangle([(x0 + 5, y0 + 5), (x0 + 8, y0 + 8)], fill=CYAN_ACCENT)

        draw.line([(x1 - 50, y0 - 1), (x1 - 18, y0 - 1)], fill=CYAN_ACCENT, width=2)
        draw.line([(x1 + 1, y0 + 18), (x1 + 1, y0 + 45)], fill=CYAN_ACCENT, width=2)
        draw.rectangle([(x1 - 8, y0 + 5), (x1 - 5, y0 + 8)], fill=CYAN_ACCENT)

        draw.line([(x0 + 18, y1 + 1), (x0 + 45, y1 + 1)], fill=CYAN_ACCENT, width=2)
        draw.line([(x1 - 45, y1 + 1), (x1 - 18, y1 + 1)], fill=CYAN_ACCENT, width=2)

    def draw_progress_bar(self, draw, x, y, w, h, pct, fg_color=(0, 220, 250), bg_color=(12, 20, 30), border_color=(0, 140, 160)):
        draw.rectangle([x, y, x + w - 1, y + h - 1], fill=bg_color, outline=border_color, width=1)
        fill_w = max(0, min(w, int(w * (pct / 100.0))))
        if fill_w > 0:
            draw.rectangle([x, y, x + fill_w - 1, y + h - 1], fill=fg_color)

    def draw_sparkline(self, draw, x, y, w, h, values, min_v=0.0, max_v=100.0, line_color=(255, 60, 80), fill_color=(100, 15, 25, 100), bg_color=(30, 10, 15), border_color=(120, 25, 35)):
        if bg_color:
            draw.rectangle([x, y, x + w - 1, y + h - 1], fill=bg_color, outline=border_color, width=1)
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
        # All Dark Cyberpunk Background
        img = Image.new('RGB', (self.width, self.height), (6, 6, 12))
        draw = ImageDraw.Draw(img)

        # Outer Frame Accent Lines
        CYAN_ACCENT = (0, 255, 240)
        CYAN_TEXT   = (0, 220, 240)
        CYAN_DIM    = (0, 140, 160)
        LIGHT_GRAY  = (220, 225, 230)
        NEON_PINK   = (255, 0, 128)
        GLOW_PINK   = (130, 0, 65)

        draw.rectangle([4, 4, self.width - 5, self.height - 5], outline=CYAN_DIM, width=1)
        draw.line([(4, 15), (4, 45)], fill=NEON_PINK, width=2)
        draw.line([(self.width - 5, 15), (self.width - 5, 45)], fill=NEON_PINK, width=2)
        draw.line([(4, self.height - 45), (4, self.height - 15)], fill=CYAN_ACCENT, width=2)
        draw.line([(self.width - 5, self.height - 45), (self.width - 5, self.height - 15)], fill=CYAN_ACCENT, width=2)

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

        # ----------------------------------------------------
        # TOP HEADER CARD (Y: 18 - 175) - Cyberpunk HUD Panel
        # ----------------------------------------------------
        self.draw_cyberpunk_panel(draw, x0, 18, x1, 175)

        # Title (NECTARINES) with subtle neon glow
        draw.text((27, 31), sys_info['hostname'], fill=GLOW_PINK, font=self.font_header)
        draw.text((29, 31), sys_info['hostname'], fill=GLOW_PINK, font=self.font_header)
        draw.text((28, 30), sys_info['hostname'], fill=NEON_PINK, font=self.font_header)

        # Digital Instrument Clock & Date (Right)
        clk_str = time.strftime("%H:%M:%S")
        date_str = time.strftime("%Y-%m-%d")
        draw.text((305, 28), clk_str, fill=(230, 255, 255), font=self.font_title)
        draw.text((320, 54), date_str, fill=CYAN_TEXT, font=self.font_micro)

        # Divider line with cyan end ticks
        draw.line([(28, 74), (432, 74)], fill=CYAN_DIM, width=1)
        draw.line([(28, 72), (28, 76)], fill=CYAN_ACCENT, width=2)
        draw.line([(432, 72), (432, 76)], fill=CYAN_ACCENT, width=2)

        # Compact System Info List
        info_items = [
            ("UPTIME:", sys_info['uptime']),
            ("LOCAL IP:", sys_info['ip_local']),
            ("PUBLIC IP:", sys_info['ip_public']),
            ("KERNEL:", sys_info['kernel'])
        ]

        y_info = 82
        for label, val in info_items:
            draw.text((28, y_info), label, fill=CYAN_TEXT, font=self.font_micro)
            draw.text((125, y_info), val, fill=LIGHT_GRAY, font=self.font_micro)
            y_info += 21

        # ----------------------------------------------------
        # SECTION 1: CPU MONITOR (Y: 190 - 510)
        # ----------------------------------------------------
        self.draw_cyberpunk_panel(draw, x0, 190, x1, 510, title="CPU PROCESSOR", title_color=CYAN_TEXT)
        
        cpu_pct = cpu['utilization']
        draw.text((28, 245), f"{cpu_pct:.1f}%", fill=(240, 250, 255), font=self.font_val)
        
        cpu_temp_str = f"TEMP: {cpu_temp}°C" if cpu_temp else "TEMP: N/A"
        draw.text((250, 250), cpu_temp_str, fill=NEON_PINK, font=self.font_title)
            
        load_str = f"LOAD: {cpu['load_avg'][0]}  {cpu['load_avg'][1]}  {cpu['load_avg'][2]}"
        draw.text((28, 305), load_str, fill=CYAN_TEXT, font=self.font_micro)
        
        self.draw_progress_bar(draw, inner_x, 340, inner_w, 24, cpu_pct, fg_color=(0, 220, 250), bg_color=(12, 20, 30), border_color=CYAN_DIM)
        self.draw_sparkline(draw, inner_x, 380, inner_w, 110, hist['cpu'], min_v=0.0, max_v=100.0, line_color=(0, 240, 255), fill_color=(0, 100, 150, 80), bg_color=(12, 18, 28), border_color=CYAN_DIM)

        # ----------------------------------------------------
        # SECTION 2: GPU MONITOR (Y: 525 - 845)
        # ----------------------------------------------------
        gpu_title = "GPU GRAPHICS" if gpu else "GPU N/A"
        self.draw_cyberpunk_panel(draw, x0, 525, x1, 845, title=gpu_title, title_color=CYAN_TEXT)
        
        if gpu:
            gpu_pct = gpu['utilization']
            draw.text((28, 580), f"{gpu_pct:.1f}%", fill=(240, 250, 255), font=self.font_val)
            draw.text((270, 585), f"TEMP: {gpu['temp_c']}°C", fill=NEON_PINK, font=self.font_sub)
            vram_str = f"VRAM: {gpu['vram_used_gb']} / {gpu['vram_total_gb']} GB ({gpu['vram_pct']}%)"
            draw.text((28, 640), vram_str, fill=CYAN_TEXT, font=self.font_micro)
            self.draw_progress_bar(draw, inner_x, 675, inner_w, 24, gpu['vram_pct'], fg_color=(255, 0, 128), bg_color=(30, 10, 20), border_color=CYAN_DIM)
            self.draw_sparkline(draw, inner_x, 715, inner_w, 110, hist['gpu'], min_v=0.0, max_v=100.0, line_color=(255, 0, 128), fill_color=(140, 0, 70, 80), bg_color=(18, 12, 22), border_color=CYAN_DIM)
        else:
            draw.text((28, 600), "NVIDIA GPU NOT DETECTED", fill=LIGHT_GRAY, font=self.font_sub)

        # ----------------------------------------------------
        # SECTION 3: RAM MEMORY (Y: 860 - 1180)
        # ----------------------------------------------------
        self.draw_cyberpunk_panel(draw, x0, 860, x1, 1180, title="RAM MEMORY", title_color=CYAN_TEXT)
        
        ram_pct = ram['pct']
        draw.text((28, 915), f"{ram_pct:.1f}%", fill=(240, 250, 255), font=self.font_val)
        draw.text((240, 925), f"{ram['used_gb']} / {ram['total_gb']} GB", fill=LIGHT_GRAY, font=self.font_sub)
        self.draw_progress_bar(draw, inner_x, 975, inner_w, 24, ram_pct, fg_color=(0, 240, 200), bg_color=(10, 25, 22), border_color=CYAN_DIM)
        self.draw_sparkline(draw, inner_x, 1015, inner_w, 145, hist['ram'], min_v=0.0, max_v=100.0, line_color=(0, 255, 210), fill_color=(0, 130, 110, 80), bg_color=(12, 22, 22), border_color=CYAN_DIM)

        # ----------------------------------------------------
        # SECTION 4: DISK STORAGE (ROOT, HDD1, HDD2) (Y: 1195 - 1500)
        # ----------------------------------------------------
        self.draw_cyberpunk_panel(draw, x0, 1195, x1, 1500, title="DISK STORAGE MONITOR", title_color=CYAN_TEXT)
        
        # Disk 1: Root /
        root_info = storage['root']
        draw.text((28, 1245), f"ROOT (/): {root_info['used_gb']} / {root_info['total_gb']} GB ({root_info['pct']}%)", fill=LIGHT_GRAY, font=self.font_micro)
        self.draw_progress_bar(draw, inner_x, 1268, inner_w, 18, root_info['pct'], fg_color=(0, 220, 250), bg_color=(12, 20, 30), border_color=CYAN_DIM)

        # Disk 2: HDD1 (/mnt/dd)
        hdd1_info = storage.get('hdd1')
        if hdd1_info:
            draw.text((28, 1298), f"HDD1 (/mnt/dd): {hdd1_info['used_tb']} / {hdd1_info['total_tb']} {hdd1_info['unit']} ({hdd1_info['pct']}%)", fill=LIGHT_GRAY, font=self.font_micro)
            self.draw_progress_bar(draw, inner_x, 1321, inner_w, 18, hdd1_info['pct'], fg_color=(255, 0, 128), bg_color=(30, 10, 20), border_color=CYAN_DIM)

        # Disk 3: HDD2 (/mnt/dd2)
        hdd2_info = storage.get('hdd2')
        if hdd2_info:
            draw.text((28, 1351), f"HDD2 (/mnt/dd2): {hdd2_info['used_tb']} / {hdd2_info['total_tb']} {hdd2_info['unit']} ({hdd2_info['pct']}%)", fill=LIGHT_GRAY, font=self.font_micro)
            self.draw_progress_bar(draw, inner_x, 1374, inner_w, 18, hdd2_info['pct'], fg_color=(0, 240, 200), bg_color=(10, 25, 22), border_color=CYAN_DIM)

        draw.text((28, 1465), "FILESYSTEMS: EXT4 / BTRFS", fill=CYAN_TEXT, font=self.font_micro)

        # ----------------------------------------------------
        # SECTION 5: NETWORK TRAFFIC (Y: 1515 - 1815)
        # ----------------------------------------------------
        self.draw_cyberpunk_panel(draw, x0, 1515, x1, 1815, title="NETWORK TRAFFIC", title_color=CYAN_TEXT)
        
        rx_str = format_net_rate(net.get('rx_mb_s', 0.0))
        tx_str = format_net_rate(net.get('tx_mb_s', 0.0))
        
        # Single dual sparkline graph box overlay (Download = Cyan/Blue, Upload = Bright Pink/Red)
        draw.text((28, 1565), f"▼ {rx_str}", fill=CYAN_ACCENT, font=self.font_sub)
        draw.text((250, 1565), f"▲ {tx_str}", fill=NEON_PINK, font=self.font_sub)

        graph_y, graph_h = 1605, 185
        max_rx_graph = max(5.0, max(hist['net_rx'] or [1.0]))
        max_tx_graph = max(5.0, max(hist['net_tx'] or [1.0]))
        max_net_graph = max(max_rx_graph, max_tx_graph)

        # Base box & Download graph (Cyan / Blue)
        self.draw_sparkline(draw, inner_x, graph_y, inner_w, graph_h, hist['net_rx'], min_v=0.0, max_v=max_net_graph, line_color=CYAN_ACCENT, fill_color=(0, 150, 220, 80), bg_color=(12, 18, 28), border_color=CYAN_DIM)
        # Overlay Upload graph (Bright Pink) into same box
        self.draw_sparkline(draw, inner_x, graph_y, inner_w, graph_h, hist['net_tx'], min_v=0.0, max_v=max_net_graph, line_color=NEON_PINK, fill_color=(200, 0, 100, 60), bg_color=None, border_color=None)

        # ----------------------------------------------------
        # FOOTER BADGE (Y: 1825 - 1885)
        # ----------------------------------------------------
        self.draw_cyberpunk_panel(draw, x0, 1825, x1, 1885)
        draw.text((28, 1840), "CYBERPUNK RIG STATS", fill=(240, 250, 255), font=self.font_sub)
        draw.text((280, 1840), "460x1920 NATIVE", fill=CYAN_TEXT, font=self.font_sub)

        return img
