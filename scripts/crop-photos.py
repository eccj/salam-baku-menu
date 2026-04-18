"""Crop dish photos from the rotated menu page images."""
from PIL import Image
from pathlib import Path

SRC = Path("/Users/emrew/Desktop/Öğelerle Yeni Klasör/jpg-rotated")
OUT = Path("/Users/emrew/Desktop/menu-design/assets/photos")
OUT.mkdir(parents=True, exist_ok=True)

crops = [
    # (src_file, out_name, box(left, top, right, bottom))
    ("IMG_8280.jpg", "salad-caesar.jpg",    (400,  3100, 2200, 5000)),
    ("IMG_8282.jpg", "soup-solyanka.jpg",   (500,  2900, 2000, 4300)),
    ("IMG_8282.jpg", "soup-ramen.jpg",      (2700, 1950, 4150, 3250)),
    ("IMG_8285.jpg", "az-khashlama.jpg",    (1650, 400,  3024, 1750)),
    ("IMG_8285.jpg", "az-piti.jpg",         (600,  2450, 2600, 3700)),
    ("IMG_8291.jpg", "shashlik-mix.jpg",    (2450, 1100, 4200, 2550)),
    ("IMG_8291.jpg", "shashlik-fish.jpg",   (1800, 3850, 4200, 5400)),
    ("IMG_8278.jpg", "cover-logo-bg.jpg",   (100,  100,  1800, 2400)),
]

for src, name, box in crops:
    im = Image.open(SRC / src)
    W, H = im.size
    l, t, r, b = box
    l, t = max(0, l), max(0, t)
    r, b = min(W, r), min(H, b)
    cropped = im.crop((l, t, r, b))
    # Resize if too large (keep aspect)
    max_dim = 1600
    if cropped.width > max_dim or cropped.height > max_dim:
        cropped.thumbnail((max_dim, max_dim), Image.LANCZOS)
    cropped.convert("RGB").save(OUT / name, "JPEG", quality=85, optimize=True)
    print(f"{name}: {cropped.size}")

print(f"\n{len(crops)} photos cropped → {OUT}")
