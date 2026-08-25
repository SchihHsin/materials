#!/usr/bin/env python3
"""Annotate UI screenshots with click markers, arrows, and label bars."""
from PIL import Image, ImageDraw, ImageFont
import math
import argparse

FONT_CANDIDATES = [
    "/System/Library/Fonts/PingFang.ttc",
    "/System/Library/Fonts/Supplemental/Arial Unicode.ttf",
    "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",
    "/usr/share/fonts/truetype/noto/NotoSansCJK-Regular.ttc",
]


def _font(size, font_path=None):
    for path in ([font_path] if font_path else []) + FONT_CANDIDATES:
        try:
            return ImageFont.truetype(path, size)
        except Exception:
            continue
    return ImageFont.load_default()


def _hex(color):
    color = color.lstrip("#")
    return tuple(int(color[i : i + 2], 16) for i in (0, 2, 4))


def annotate(src, out, anns, crop=None, pad=120, fsz=30, font_path=None, marker_alpha=140, radius=15):
    base = Image.open(src).convert("RGBA")
    if crop:
        base = base.crop(tuple(crop))
    width, height = base.size
    canvas = Image.new("RGBA", (width, height + pad), (255, 255, 255, 255))
    canvas.paste(base, (0, 0))

    overlay = Image.new("RGBA", (width, height + pad), (0, 0, 0, 0))
    od = ImageDraw.Draw(overlay)
    for ann in anns:
        if ann.get("x") is None:
            continue
        color = _hex(ann["color"])
        x, y = ann["x"], ann["y"]
        od.ellipse([x - radius, y - radius, x + radius, y + radius], outline=color + (marker_alpha,), width=6)
        od.ellipse([x - 6, y - 6, x + 6, y + 6], fill=color + (marker_alpha,))

    canvas = Image.alpha_composite(canvas, overlay)
    draw = ImageDraw.Draw(canvas)
    font = _font(fsz, font_path)

    for ann in anns:
        color = _hex(ann["color"])
        label = ann["label"]
        lx = ann.get("lx") or (ann["x"] if ann.get("x") is not None else width // 2)
        ly = height + pad - fsz - 24
        tb = draw.textbbox((0, 0), label, font=font)
        tw = tb[2] - tb[0]
        th = tb[3] - tb[1]
        lx = max(tw // 2 + 18, min(lx, width - tw // 2 - 18))
        draw.rounded_rectangle([lx - tw // 2 - 16, ly - 10, lx + tw // 2 + 16, ly + th + 14], radius=12, fill=color)
        draw.text((lx - tw // 2, ly - tb[1] + 2), label, font=font, fill=(255, 255, 255))
        if ann.get("x") is not None:
            x, y = ann["x"], ann["y"]
            ay = ly - 10
            draw.line([lx, ay, x, y + radius + 2], fill=color, width=5)
            angle = math.atan2((y + radius + 2) - ay, x - lx)
            length = 18
            for side in (0.4, -0.4):
                draw.line(
                    [
                        x,
                        y + radius + 2,
                        x - length * math.cos(angle - side),
                        (y + radius + 2) - length * math.sin(angle - side),
                    ],
                    fill=color,
                    width=5,
                )

    canvas.convert("RGB").save(out)
    return out


def _parse_ann(value):
    parts = value.split(",")
    x = None if parts[0] in ("None", "", "-") else int(parts[0])
    y = None if len(parts) < 2 or parts[1] in ("None", "", "-") else int(parts[1])
    return {
        "x": x,
        "y": y,
        "label": parts[2],
        "color": parts[3],
        "lx": int(parts[4]) if len(parts) > 4 and parts[4] else None,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Annotate UI screenshots with click markers")
    parser.add_argument("src")
    parser.add_argument("out")
    parser.add_argument("--ann", action="append", default=[], help="x,y,label,#color[,lx]; x=None for note only")
    parser.add_argument("--crop", default=None, help="left,top,right,bottom")
    parser.add_argument("--pad", type=int, default=120)
    parser.add_argument("--fsz", type=int, default=30)
    parser.add_argument("--font", default=None)
    args = parser.parse_args()

    anns = [_parse_ann(item) for item in args.ann]
    crop = tuple(int(v) for v in args.crop.split(",")) if args.crop else None
    annotate(args.src, args.out, anns, crop, args.pad, args.fsz, args.font)
    print("saved", args.out)
