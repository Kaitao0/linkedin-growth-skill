"""
post_to_n8n.py — OPTIONAL Phase 2

Sends a generated post to a user-owned n8n webhook for scheduled publishing.
The skill does NOT call this automatically. The user runs it explicitly.

Why optional: there is no fully sanctioned LinkedIn API for personal-account
posting without an approved Marketing Developer Platform app. Most users
end up with one of:
    1. Manual publishing (recommended default — zero risk).
    2. Unipile / similar third-party (paid, somewhat sanctioned).
    3. RPA / browser automation (against ToS, risk of account restriction).

This script just hands the post off to YOUR n8n. What n8n does with it
(schedule, store, post via integration X) is your choice.

Usage:
    export N8N_WEBHOOK_URL=https://n8n.example.com/webhook/linkedin-post
    python post_to_n8n.py path/to/post_folder/

The post_folder must contain copy.md and meta.json (and image.png or slide_*.png).

Requires: requests
"""

import argparse
import base64
import json
import os
import sys
from pathlib import Path

try:
    import requests
except ImportError:
    print("ERROR: install with: pip install requests", file=sys.stderr)
    sys.exit(1)


def encode_image(path: Path) -> dict:
    return {
        "filename": path.name,
        "mime_type": "image/png",
        "base64": base64.b64encode(path.read_bytes()).decode(),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("post_folder", type=Path)
    parser.add_argument("--webhook-url", default=os.environ.get("N8N_WEBHOOK_URL"))
    parser.add_argument("--dry-run", action="store_true", help="Print payload, don't send")
    args = parser.parse_args()

    if not args.webhook_url and not args.dry_run:
        print("ERROR: set N8N_WEBHOOK_URL env var or pass --webhook-url", file=sys.stderr)
        sys.exit(2)

    folder = args.post_folder
    copy_path = folder / "copy.md"
    meta_path = folder / "meta.json"
    if not copy_path.exists() or not meta_path.exists():
        print(f"ERROR: {folder} must contain copy.md and meta.json", file=sys.stderr)
        sys.exit(3)

    images = sorted(folder.glob("*.png"))
    payload = {
        "copy": copy_path.read_text(encoding="utf-8"),
        "meta": json.loads(meta_path.read_text(encoding="utf-8")),
        "images": [encode_image(p) for p in images],
    }

    if args.dry_run:
        # Don't print base64 in dry-run, just sizes
        preview = {
            **payload,
            "images": [{"filename": i["filename"], "size_kb": len(i["base64"]) * 3 // 4 // 1024} for i in payload["images"]],
        }
        print(json.dumps(preview, indent=2, ensure_ascii=False))
        return

    resp = requests.post(args.webhook_url, json=payload, timeout=30)
    resp.raise_for_status()
    print(f"Sent. Status: {resp.status_code}")
    if resp.text:
        print(resp.text)


if __name__ == "__main__":
    main()
