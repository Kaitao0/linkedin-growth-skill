"""
generate_image_pillow.py

Fallback PNG generator for LinkedIn posts and carousels.
Uses only Pillow — no external API, no costs, no key required.

Generates clean, brand-consistent template-based images. Less "wow" than
Nano Banana, but reliable and customizable.

Usage:
    # Single post image (1080x1080, square)
    python generate_image_pillow.py post --title "Migração de ERP em 47 dias" --subtitle "Lições do retail" --output post.png

    # Carousel (1080x1350 portrait, multiple slides)
    python generate_image_pillow.py carousel slides.json --output-dir ./carousel/

    # LinkedIn banner (1584x396)
    python generate_image_pillow.py banner --headline "Tech Lead | ERP Integration | Retail" --tag "TOTVS · n8n · Oracle" --output banner.png

Carousel JSON format:
    {
        "brand_color": "#0A66C2",
        "accent_color": "#F5F5F5",
        "author": "Nome do Usuário",
        "handle": "@usuario",
        "slides": [
            {"type": "cover", "title": "...", "subtitle": "..."},
            {"type": "content", "title": "...", "body": "..."},
            {"type": "cta", "title": "...", "body": "...", "cta": "..."}
        ]
    }
"""

import argparse
import json
import sys
from pathlib import Path

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    print("ERROR: install with: pip install Pillow", file=sys.stderr)
    sys.exit(1)


DEFAULT_BRAND = "#0A66C2"
DEFAULT_ACCENT = "#F5F5F5"
DEFAULT_TEXT_DARK = "#1A1A1A"
DEFAULT_TEXT_LIGHT = "#FFFFFF"


def load_font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    """Try common system fonts, fall back to default."""
    candidates = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/System/Library/Fonts/Helvetica.ttc",
        "C:\\Windows\\Fonts\\arialbd.ttf" if bold else "C:\\Windows\\Fonts\\arial.ttf",
    ]
    for path in candidates:
        try:
            return ImageFont.truetype(path, size)
        except (OSError, IOError):
            continue
    return ImageFont.load_default()


def wrap_text(text: str, font: ImageFont.FreeTypeFont, max_width: int, draw: ImageDraw.ImageDraw) -> list[str]:
    words = text.split()
    lines: list[str] = []
    current: list[str] = []
    for word in words:
        candidate = " ".join(current + [word])
        bbox = draw.textbbox((0, 0), candidate, font=font)
        if bbox[2] - bbox[0] <= max_width:
            current.append(word)
        else:
            if current:
                lines.append(" ".join(current))
            current = [word]
    if current:
        lines.append(" ".join(current))
    return lines


def draw_post(title: str, subtitle: str, brand: str, accent: str, output: Path, size=(1080, 1080)):
    img = Image.new("RGB", size, accent)
    draw = ImageDraw.Draw(img)

    # Top brand bar
    draw.rectangle([0, 0, size[0], 16], fill=brand)

    title_font = load_font(72, bold=True)
    subtitle_font = load_font(36)

    # Wrap title
    lines = wrap_text(title, title_font, size[0] - 160, draw)
    y = size[1] // 2 - (len(lines) * 90) // 2 - 60
    for line in lines:
        draw.text((80, y), line, fill=DEFAULT_TEXT_DARK, font=title_font)
        y += 90

    # Subtitle
    if subtitle:
        sub_lines = wrap_text(subtitle, subtitle_font, size[0] - 160, draw)
        y += 30
        for line in sub_lines:
            draw.text((80, y), line, fill=brand, font=subtitle_font)
            y += 50

    output.parent.mkdir(parents=True, exist_ok=True)
    img.save(output, "PNG", optimize=True)
    print(f"Saved: {output}")


def draw_banner(headline: str, tag: str, brand: str, accent: str, output: Path):
    size = (1584, 396)
    img = Image.new("RGB", size, brand)
    draw = ImageDraw.Draw(img)

    # Right-side accent block (LinkedIn shows the right portion uncovered by profile photo overlay)
    draw.rectangle([size[0] // 2, 0, size[0], size[1]], fill=accent)

    headline_font = load_font(58, bold=True)
    tag_font = load_font(28)

    lines = wrap_text(headline, headline_font, size[0] // 2 - 80, draw)
    y = size[1] // 2 - (len(lines) * 70) // 2 - 30
    for line in lines:
        draw.text((size[0] // 2 + 40, y), line, fill=DEFAULT_TEXT_DARK, font=headline_font)
        y += 70

    if tag:
        y += 15
        draw.text((size[0] // 2 + 40, y), tag, fill=brand, font=tag_font)

    output.parent.mkdir(parents=True, exist_ok=True)
    img.save(output, "PNG", optimize=True)
    print(f"Saved: {output}")


def draw_carousel_slide(slide: dict, idx: int, total: int, brand: str, accent: str,
                        author: str, handle: str, output: Path, size=(1080, 1350)):
    slide_type = slide.get("type", "content")
    bg, fg = (brand, DEFAULT_TEXT_LIGHT) if slide_type == "cover" else (accent, DEFAULT_TEXT_DARK)
    img = Image.new("RGB", size, bg)
    draw = ImageDraw.Draw(img)

    # Page indicator (top right)
    page_font = load_font(28)
    draw.text((size[0] - 120, 50), f"{idx}/{total}", fill=fg, font=page_font)

    # Title
    title = slide.get("title", "")
    title_font = load_font(70 if slide_type == "cover" else 56, bold=True)
    title_lines = wrap_text(title, title_font, size[0] - 160, draw)
    y = 200 if slide_type == "cover" else 150
    for line in title_lines:
        draw.text((80, y), line, fill=fg, font=title_font)
        y += 80

    # Body
    body = slide.get("body", "")
    if body:
        body_font = load_font(36)
        body_lines = wrap_text(body, body_font, size[0] - 160, draw)
        y += 40
        for line in body_lines:
            draw.text((80, y), line, fill=fg, font=body_font)
            y += 50

    # CTA on last slide
    if slide.get("cta"):
        cta_font = load_font(40, bold=True)
        cta_lines = wrap_text(slide["cta"], cta_font, size[0] - 160, draw)
        y = size[1] - 350
        for line in cta_lines:
            draw.text((80, y), line, fill=brand if slide_type != "cover" else DEFAULT_TEXT_LIGHT, font=cta_font)
            y += 56

    # Footer (author + handle)
    footer_font = load_font(26)
    draw.text((80, size[1] - 80), f"{author}  ·  {handle}", fill=fg, font=footer_font)

    # Bottom brand stripe
    draw.rectangle([0, size[1] - 12, size[0], size[1]], fill=brand if slide_type != "cover" else DEFAULT_TEXT_LIGHT)

    output.parent.mkdir(parents=True, exist_ok=True)
    img.save(output, "PNG", optimize=True)


def cmd_post(args):
    draw_post(args.title, args.subtitle or "", args.brand, args.accent, args.output)


def cmd_banner(args):
    draw_banner(args.headline, args.tag or "", args.brand, args.accent, args.output)


def cmd_carousel(args):
    spec = json.loads(args.spec.read_text(encoding="utf-8"))
    brand = spec.get("brand_color", DEFAULT_BRAND)
    accent = spec.get("accent_color", DEFAULT_ACCENT)
    author = spec.get("author", "Author")
    handle = spec.get("handle", "")
    slides = spec.get("slides", [])
    args.output_dir.mkdir(parents=True, exist_ok=True)
    for i, slide in enumerate(slides, start=1):
        out = args.output_dir / f"slide_{i:02d}.png"
        draw_carousel_slide(slide, i, len(slides), brand, accent, author, handle, out)
        print(f"Saved: {out}")


def main():
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_post = sub.add_parser("post")
    p_post.add_argument("--title", required=True)
    p_post.add_argument("--subtitle", default="")
    p_post.add_argument("--brand", default=DEFAULT_BRAND)
    p_post.add_argument("--accent", default=DEFAULT_ACCENT)
    p_post.add_argument("--output", type=Path, required=True)
    p_post.set_defaults(func=cmd_post)

    p_banner = sub.add_parser("banner")
    p_banner.add_argument("--headline", required=True)
    p_banner.add_argument("--tag", default="")
    p_banner.add_argument("--brand", default=DEFAULT_BRAND)
    p_banner.add_argument("--accent", default=DEFAULT_ACCENT)
    p_banner.add_argument("--output", type=Path, required=True)
    p_banner.set_defaults(func=cmd_banner)

    p_car = sub.add_parser("carousel")
    p_car.add_argument("spec", type=Path)
    p_car.add_argument("--output-dir", type=Path, required=True)
    p_car.set_defaults(func=cmd_carousel)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
