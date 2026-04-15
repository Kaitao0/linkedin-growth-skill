"""
analyze_profile_image.py

Technical analysis of a LinkedIn profile photo.
Reports objective metrics that complement Claude's vision-based qualitative review.

Usage:
    python analyze_profile_image.py <path_to_image>

Outputs:
    - Resolution and aspect ratio
    - File size and format
    - Average brightness and contrast
    - Sharpness estimate (Laplacian variance proxy)
    - Dominant colors (background hint)
    - Square crop check (LinkedIn displays in circle, square works best)

Requires: Pillow, numpy
"""

import argparse
import json
import sys
from pathlib import Path

try:
    from PIL import Image, ImageStat, ImageFilter
    import numpy as np
except ImportError:
    print("ERROR: install with: pip install Pillow numpy", file=sys.stderr)
    sys.exit(1)


def sharpness_score(img: Image.Image) -> float:
    """Approximation of image sharpness via edge variance."""
    gray = img.convert("L")
    edges = gray.filter(ImageFilter.FIND_EDGES)
    arr = np.array(edges, dtype=np.float32)
    return float(arr.var())


def dominant_colors(img: Image.Image, n: int = 5) -> list:
    small = img.copy()
    small.thumbnail((100, 100))
    small = small.convert("RGB")
    quantized = small.quantize(colors=n)
    palette = quantized.getpalette()[: n * 3]
    counts = sorted(quantized.getcolors(), reverse=True)
    return [
        {
            "rgb": [palette[i * 3], palette[i * 3 + 1], palette[i * 3 + 2]],
            "share": round(count / sum(c for c, _ in counts), 3),
        }
        for (count, i) in counts
    ]


def analyze(path: Path) -> dict:
    img = Image.open(path)
    width, height = img.size
    is_square = width == height
    stat = ImageStat.Stat(img.convert("RGB"))

    return {
        "file": str(path),
        "format": img.format,
        "size_kb": round(path.stat().st_size / 1024, 1),
        "resolution": {"width": width, "height": height},
        "aspect_ratio": round(width / height, 3),
        "is_square": is_square,
        "min_recommended_400px": min(width, height) >= 400,
        "brightness_per_channel": [round(m, 1) for m in stat.mean],
        "stddev_per_channel": [round(s, 1) for s in stat.stddev],
        "sharpness_proxy": round(sharpness_score(img), 1),
        "dominant_colors": dominant_colors(img),
        "issues": flag_issues(img, path, stat),
    }


def flag_issues(img: Image.Image, path: Path, stat: ImageStat.Stat) -> list:
    issues = []
    if min(img.size) < 400:
        issues.append(f"Resolution too low ({img.size[0]}x{img.size[1]}). LinkedIn recommends at least 400x400.")
    if img.size[0] != img.size[1]:
        issues.append("Image is not square. LinkedIn crops to circle from a square — non-square crops badly.")
    if path.stat().st_size > 8 * 1024 * 1024:
        issues.append("File over 8MB — LinkedIn may compress aggressively.")
    avg_brightness = sum(stat.mean[:3]) / 3
    if avg_brightness < 60:
        issues.append("Image is very dark. Consider re-shoot with better lighting.")
    if avg_brightness > 220:
        issues.append("Image is very bright / washed out. Reduce exposure.")
    contrast = sum(stat.stddev[:3]) / 3
    if contrast < 30:
        issues.append("Very low contrast — face may not stand out from background.")
    return issues


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("image_path", type=Path)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    if not args.image_path.exists():
        print(f"ERROR: file not found: {args.image_path}", file=sys.stderr)
        sys.exit(1)

    result = analyze(args.image_path)
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
