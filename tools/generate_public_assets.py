"""Generate neutral, code-owned icons for the public source release.

The author's original brand art and music live in the ignored path/self folder.
Run this script with Pillow installed to regenerate the PNG/ICO files.
"""

from math import cos, pi, sin
from pathlib import Path

from PIL import Image, ImageDraw


OUT = Path(__file__).resolve().parents[1] / "assets" / "public"
OUT.mkdir(parents=True, exist_ok=True)
SCALE = 4
INK = "#153454"
TEAL = "#16b6b5"
CORAL = "#f46d66"


def box(x0, y0, x1, y1):
    return tuple(round(v * SCALE) for v in (x0, y0, x1, y1))


def points(*vertices):
    return [(round(x * SCALE), round(y * SCALE)) for x, y in vertices]


def glyph(kind, color):
    image = Image.new("RGBA", (64 * SCALE, 64 * SCALE), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    width = 4 * SCALE

    if kind == "play":
        draw.rounded_rectangle(box(8, 8, 56, 56), radius=13 * SCALE, outline=color, width=width)
        draw.polygon(points((27, 20), (27, 44), (46, 32)), fill=color)
    elif kind == "settings":
        for i in range(8):
            theta = i * pi / 4
            draw.line(points((32 + 20 * cos(theta), 32 + 20 * sin(theta)),
                             (32 + 25 * cos(theta), 32 + 25 * sin(theta))),
                      fill=color, width=width)
        draw.ellipse(box(14, 14, 50, 50), outline=color, width=width)
        draw.ellipse(box(26, 26, 38, 38), outline=color, width=width)
    elif kind == "add":
        draw.rounded_rectangle(box(9, 9, 55, 55), radius=12 * SCALE, outline=color, width=width)
        draw.line(points((32, 21), (32, 43)), fill=color, width=width)
        draw.line(points((21, 32), (43, 32)), fill=color, width=width)
    elif kind == "chart":
        draw.line(points((11, 50), (53, 50)), fill=color, width=width)
        draw.rounded_rectangle(box(15, 33, 23, 48), radius=2 * SCALE, fill=color)
        draw.rounded_rectangle(box(28, 24, 36, 48), radius=2 * SCALE, fill=color)
        draw.rounded_rectangle(box(41, 15, 49, 48), radius=2 * SCALE, fill=color)
    elif kind == "home":
        draw.line(points((10, 29), (32, 12), (54, 29)), fill=color, width=width, joint="curve")
        draw.line(points((17, 28), (17, 51), (47, 51), (47, 28)),
                  fill=color, width=width, joint="curve")
        draw.line(points((28, 51), (28, 38), (36, 38), (36, 51)),
                  fill=color, width=width, joint="curve")
    elif kind == "pause":
        draw.rounded_rectangle(box(18, 14, 27, 50), radius=3 * SCALE, fill=color)
        draw.rounded_rectangle(box(37, 14, 46, 50), radius=3 * SCALE, fill=color)
    elif kind == "refresh":
        draw.arc(box(13, 13, 51, 51), start=35, end=315, fill=color, width=width)
        draw.polygon(points((48, 14), (53, 31), (37, 27)), fill=color)
    else:
        raise ValueError(kind)

    return image.resize((64, 64), Image.Resampling.LANCZOS)


def clock(accent):
    image = Image.new("RGBA", (256 * SCALE, 256 * SCALE), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    draw.rounded_rectangle(box(8, 8, 248, 248), radius=56 * SCALE, fill="#12253b")
    draw.ellipse(box(47, 47, 209, 209), outline=accent, width=17 * SCALE)
    for i in range(12):
        angle = i * pi / 6 - pi / 2
        draw.line(points((128 + 65 * cos(angle), 128 + 65 * sin(angle)),
                         (128 + 73 * cos(angle), 128 + 73 * sin(angle))),
                  fill="#a9e5e5", width=3 * SCALE)
    draw.line(points((128, 128), (128, 83)), fill="#ffffff", width=12 * SCALE)
    draw.line(points((128, 128), (164, 148)), fill="#ffffff", width=12 * SCALE)
    draw.ellipse(box(120, 120, 136, 136), fill="#ffffff")
    return image.resize((256, 256), Image.Resampling.LANCZOS)


for name, kind, color in [
    ("play.png", "play", INK),
    ("play-alt.png", "play", TEAL),
    ("settings.png", "settings", INK),
    ("settings-alt.png", "settings", TEAL),
    ("add.png", "add", INK),
    ("chart.png", "chart", TEAL),
    ("chart-alt.png", "chart", INK),
    ("home.png", "home", INK),
    ("pause.png", "pause", INK),
    ("refresh.png", "refresh", INK),
]:
    glyph(kind, color).save(OUT / name)

idle = clock(TEAL)
idle.save(OUT / "clock.png")
clock(CORAL).save(OUT / "clock-active.png")
idle.save(OUT / "clock.ico", sizes=[(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)])

print(f"Generated neutral icons in {OUT}")
