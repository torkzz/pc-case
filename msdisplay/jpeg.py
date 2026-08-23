import io
from PIL import Image, ImageDraw

DEFAULT_WIDTH = 460
DEFAULT_HEIGHT = 1920

def prepare_image(image_input, width=DEFAULT_WIDTH, height=DEFAULT_HEIGHT, preserve_aspect=False):
    """
    Loads, crops, or resizes images for MSDisplay 480x1920 portrait panel.
    Explicitly crops images wider than `width` rather than producing distorted frames.
    """
    if isinstance(image_input, str):
        img = Image.open(image_input).convert('RGB')
    elif isinstance(image_input, Image.Image):
        img = image_input.convert('RGB')
    else:
        raise TypeError("image_input must be a file path string or PIL Image instance.")

    src_w, src_h = img.size

    if preserve_aspect:
        # Scale to fit width while preserving aspect ratio, crop vertically if needed
        scale = width / float(src_w)
        new_h = int(src_h * scale)
        img = img.resize((width, new_h), Image.Resampling.LANCZOS)
        if new_h > height:
            img = img.crop((0, 0, width, height))
        elif new_h < height:
            padded = Image.new('RGB', (width, height), (0, 0, 0))
            padded.paste(img, (0, (height - new_h) // 2))
            img = padded
    else:
        # Direct crop or resize to exact (width, height)
        if src_w > width:
            # Crop center horizontally to target width
            left = (src_w - width) // 2
            img = img.crop((left, 0, left + width, min(src_h, height)))
        if img.size != (width, height):
            img = img.resize((width, height), Image.Resampling.LANCZOS)

    return img

def encode_jpeg(image, quality=95, subsampling=0):
    """
    Encodes PIL Image to JPEG byte stream using YUV 4:4:4 (subsampling=0) by default.
    """
    buf = io.BytesIO()
    image.save(buf, format="JPEG", quality=quality, subsampling=subsampling)
    return buf.getvalue()

def create_solid_color_jpeg(r, g, b, width=DEFAULT_WIDTH, height=DEFAULT_HEIGHT):
    img = Image.new('RGB', (width, height), (r, g, b))
    return encode_jpeg(img)

def create_test_grid_jpeg(width=DEFAULT_WIDTH, height=DEFAULT_HEIGHT):
    img = Image.new('RGB', (width, height), (0, 0, 0))
    draw = ImageDraw.Draw(img)

    col_w = width / 3.0
    row_h = height / 4.0
    colors_grid = [
        [(255, 0, 0),   (0, 255, 0),   (0, 0, 255)],     # Red, Green, Blue
        [(255, 255, 0), (0, 255, 255), (255, 0, 255)],   # Yellow, Cyan, Magenta
        [(255, 128, 0), (0, 255, 128), (128, 0, 255)],   # Orange, Mint, Purple
        [(128, 0, 0),   (0, 128, 0),   (0, 0, 128)]      # Dark Red, Dark Green, Dark Blue
    ]
    for row_idx in range(4):
        y0 = int(row_idx * row_h)
        y1 = int((row_idx + 1) * row_h)
        for col_idx in range(3):
            x0 = int(col_idx * col_w)
            x1 = int((col_idx + 1) * col_w)
            c = colors_grid[row_idx][col_idx]
            draw.rectangle([x0, y0, max(x0, x1 - 1), max(y0, y1 - 1)], fill=c)

    return encode_jpeg(img)
