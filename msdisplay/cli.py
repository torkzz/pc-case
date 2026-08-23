import sys
import argparse
from .display import MSDisplayController

def main():
    parser = argparse.ArgumentParser(description="MSDisplay Native Linux Driver CLI")
    subparsers = parser.add_subparsers(dest="command", help="Driver commands")

    # Command: test-grid
    grid_parser = subparsers.add_parser("test-grid", help="Display 480x1920 3-column grid test pattern")
    grid_parser.add_argument("--duration", type=float, default=5.0, help="Display duration in seconds")

    # Command: solid
    solid_parser = subparsers.add_parser("solid", help="Display solid color (red, green, blue, white, or R G B bytes)")
    solid_parser.add_argument("color_or_r", type=str, help="Color name ('red', 'green', 'blue', 'white') or Red byte (0-255)")
    solid_parser.add_argument("green", type=int, nargs="?", default=None, help="Green byte (0-255)")
    solid_parser.add_argument("blue", type=int, nargs="?", default=None, help="Blue byte (0-255)")
    solid_parser.add_argument("--duration", type=float, default=5.0, help="Display duration in seconds")

    # Command: image
    img_parser = subparsers.add_parser("image", help="Display an image file")
    img_parser.add_argument("path", type=str, help="Path to image file")
    img_parser.add_argument("--preserve-aspect", action="store_true", help="Preserve aspect ratio when scaling")
    img_parser.add_argument("--duration", type=float, default=5.0, help="Display duration in seconds")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    controller = MSDisplayController()

    try:
        controller.connect()
        if args.command == "test-grid":
            print(f"=== Displaying 480x1920 Grid Test Pattern ({args.duration}s) ===")
            controller.test_grid(duration=args.duration)
        elif args.command == "solid":
            color_name = args.color_or_r.lower()
            color_map = {
                "red": (255, 0, 0),
                "green": (0, 255, 0),
                "blue": (0, 0, 255),
                "white": (255, 255, 255),
                "black": (0, 0, 0),
            }
            if color_name in color_map:
                r, g, b = color_map[color_name]
            else:
                r = int(args.color_or_r)
                g = int(args.green) if args.green is not None else 0
                b = int(args.blue) if args.blue is not None else 0

            print(f"=== Displaying Solid Color ({r}, {g}, {b}) ({args.duration}s) ===")
            controller.solid_color(r, g, b, duration=args.duration)
        elif args.command == "image":
            print(f"=== Displaying Image '{args.path}' ({args.duration}s) ===")
            controller.show_image(args.path, preserve_aspect=args.preserve_aspect, duration=args.duration)
    finally:
        controller.close()

if __name__ == "__main__":
    main()
