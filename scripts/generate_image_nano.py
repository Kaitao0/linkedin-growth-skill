"""
generate_image_nano.py

Generates or edits images via Google Gemini 2.5 Flash Image (a.k.a. "Nano Banana").

Two modes:
    1. text-to-image  — generate a new image from a prompt (post images, banners).
    2. image-edit     — edit an existing image (profile photo touch-ups).

Requires GEMINI_API_KEY in environment, OR pass via --api-key.

Usage:
    # Generate a post image
    python generate_image_nano.py generate "ERP migration in retail, abstract" --output post.png

    # Edit a profile photo
    python generate_image_nano.py edit photo.jpg "Replace background with neutral light gray studio backdrop, keep face untouched" --output photo_v2.png

    # Carousel (multiple slides from a JSON spec)
    python generate_image_nano.py carousel slides.json --output-dir ./carousel/

Install: pip install google-genai pillow
"""

import argparse
import base64
import json
import os
import sys
from pathlib import Path

try:
    from google import genai
    from google.genai import types
    from PIL import Image
    from io import BytesIO
except ImportError:
    print("ERROR: install with: pip install google-genai pillow", file=sys.stderr)
    sys.exit(1)


MODEL_ID = "gemini-2.5-flash-image"


def get_client(api_key: str | None) -> "genai.Client":
    key = api_key or os.environ.get("GEMINI_API_KEY")
    if not key:
        print(
            "ERROR: GEMINI_API_KEY not set. Set the env var or pass --api-key.\n"
            "Get a key at: https://aistudio.google.com/apikey",
            file=sys.stderr,
        )
        sys.exit(2)
    return genai.Client(api_key=key)


def save_response_images(response, output: Path) -> list[Path]:
    saved = []
    idx = 0
    for part in response.candidates[0].content.parts:
        if getattr(part, "inline_data", None) and part.inline_data.data:
            data = part.inline_data.data
            if isinstance(data, str):
                data = base64.b64decode(data)
            img = Image.open(BytesIO(data))
            target = output if idx == 0 else output.with_stem(f"{output.stem}_{idx}")
            target.parent.mkdir(parents=True, exist_ok=True)
            img.save(target)
            saved.append(target)
            idx += 1
    return saved


def cmd_generate(args):
    client = get_client(args.api_key)
    response = client.models.generate_content(
        model=MODEL_ID,
        contents=[args.prompt],
    )
    saved = save_response_images(response, args.output)
    if not saved:
        print("ERROR: model returned no image data.", file=sys.stderr)
        sys.exit(3)
    for p in saved:
        print(f"Saved: {p}")


def cmd_edit(args):
    client = get_client(args.api_key)
    src = Image.open(args.input_image)
    response = client.models.generate_content(
        model=MODEL_ID,
        contents=[args.prompt, src],
    )
    saved = save_response_images(response, args.output)
    if not saved:
        print("ERROR: model returned no image data.", file=sys.stderr)
        sys.exit(3)
    for p in saved:
        print(f"Saved: {p}")


def cmd_carousel(args):
    """
    Carousel spec JSON format:
    {
        "title": "n8n vs cron jobs",
        "slides": [
            {"prompt": "Cover slide showing two paths splitting...", "filename": "slide_1.png"},
            {"prompt": "Slide 2 content visual...", "filename": "slide_2.png"},
            ...
        ]
    }
    """
    spec = json.loads(args.spec.read_text(encoding="utf-8"))
    args.output_dir.mkdir(parents=True, exist_ok=True)
    client = get_client(args.api_key)
    for i, slide in enumerate(spec.get("slides", []), start=1):
        filename = slide.get("filename", f"slide_{i}.png")
        target = args.output_dir / filename
        print(f"[{i}/{len(spec['slides'])}] generating {filename}...")
        response = client.models.generate_content(
            model=MODEL_ID,
            contents=[slide["prompt"]],
        )
        save_response_images(response, target)
    print(f"Carousel saved to {args.output_dir}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--api-key", default=None, help="Override GEMINI_API_KEY env var")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_gen = sub.add_parser("generate", help="Generate image from text prompt")
    p_gen.add_argument("prompt", type=str)
    p_gen.add_argument("--output", type=Path, required=True)
    p_gen.set_defaults(func=cmd_generate)

    p_edit = sub.add_parser("edit", help="Edit existing image with prompt")
    p_edit.add_argument("input_image", type=Path)
    p_edit.add_argument("prompt", type=str)
    p_edit.add_argument("--output", type=Path, required=True)
    p_edit.set_defaults(func=cmd_edit)

    p_car = sub.add_parser("carousel", help="Generate carousel from JSON spec")
    p_car.add_argument("spec", type=Path)
    p_car.add_argument("--output-dir", type=Path, required=True)
    p_car.set_defaults(func=cmd_carousel)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
