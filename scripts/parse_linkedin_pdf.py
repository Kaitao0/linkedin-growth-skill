"""
parse_linkedin_pdf.py

Extracts structured sections from a LinkedIn "Save to PDF" export.

Usage:
    python parse_linkedin_pdf.py <path_to_pdf> [--output <path_to_md>]

Requires: pypdf (pip install pypdf)

LinkedIn PDF exports follow a predictable section order:
    Contact -> Top Skills -> Languages -> Certifications -> Honors-Awards
    -> Publications -> Summary -> Experience -> Education

This parser is heuristic (LinkedIn changes the layout occasionally). It
extracts what it can and leaves a TODO marker where it fails so the user
can paste manually.
"""

import argparse
import json
import re
import sys
from pathlib import Path

try:
    from pypdf import PdfReader
except ImportError:
    print("ERROR: pypdf is required. Install with: pip install pypdf", file=sys.stderr)
    sys.exit(1)


SECTION_HEADERS = [
    "Contact",
    "Top Skills",
    "Languages",
    "Certifications",
    "Honors-Awards",
    "Publications",
    "Summary",
    "Experience",
    "Education",
    # Portuguese variants
    "Contato",
    "Principais Competências",
    "Idiomas",
    "Certificações",
    "Honras-Prêmios",
    "Publicações",
    "Resumo",
    "Experiência",
    "Formação acadêmica",
]


def extract_text(pdf_path: Path) -> str:
    reader = PdfReader(str(pdf_path))
    return "\n".join(page.extract_text() or "" for page in reader.pages)


def split_sections(text: str) -> dict:
    sections = {}
    lines = text.splitlines()
    current = "Header"
    sections[current] = []

    for line in lines:
        stripped = line.strip()
        if stripped in SECTION_HEADERS:
            current = stripped
            sections[current] = []
        else:
            sections.setdefault(current, []).append(line)

    return {k: "\n".join(v).strip() for k, v in sections.items()}


def extract_name_and_headline(header_block: str) -> dict:
    lines = [l.strip() for l in header_block.splitlines() if l.strip()]
    name = lines[0] if lines else ""
    headline = lines[1] if len(lines) > 1 else ""
    location_match = next(
        (l for l in lines[2:] if re.search(r"(Brasil|Brazil|United States|,)", l)),
        "",
    )
    return {"name": name, "headline": headline, "location": location_match}


def to_markdown(sections: dict, header_meta: dict) -> str:
    md = []
    md.append(f"# {header_meta.get('name', 'Unknown')}\n")
    md.append(f"**Headline:** {header_meta.get('headline', 'TODO — paste manually')}\n")
    md.append(f"**Location:** {header_meta.get('location', 'TODO')}\n")
    md.append("\n---\n")

    section_order = [
        ("Summary", "Resumo", "## About / Summary"),
        ("Experience", "Experiência", "## Experience"),
        ("Education", "Formação acadêmica", "## Education"),
        ("Top Skills", "Principais Competências", "## Top Skills"),
        ("Certifications", "Certificações", "## Certifications"),
        ("Languages", "Idiomas", "## Languages"),
        ("Honors-Awards", "Honras-Prêmios", "## Honors & Awards"),
        ("Publications", "Publicações", "## Publications"),
    ]

    for en_key, pt_key, header in section_order:
        body = sections.get(en_key) or sections.get(pt_key) or ""
        md.append(f"\n{header}\n")
        if body:
            md.append(body + "\n")
        else:
            md.append("_TODO — section not found in PDF, paste manually._\n")

    md.append("\n---\n")
    md.append("## Sections NOT included in LinkedIn PDF export (paste manually)\n")
    md.append("- Profile photo (upload as separate image)\n")
    md.append("- Banner image (upload as separate image)\n")
    md.append("- Featured section\n")
    md.append("- Recent posts (last 90 days)\n")
    md.append("- Recommendations received\n")
    md.append("- Activity stats (followers, post views)\n")

    return "\n".join(md)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("pdf_path", type=Path)
    parser.add_argument("--output", type=Path, default=None)
    parser.add_argument("--json", action="store_true", help="Also emit JSON")
    args = parser.parse_args()

    if not args.pdf_path.exists():
        print(f"ERROR: file not found: {args.pdf_path}", file=sys.stderr)
        sys.exit(1)

    text = extract_text(args.pdf_path)
    sections = split_sections(text)
    header_meta = extract_name_and_headline(sections.get("Header", ""))
    md = to_markdown(sections, header_meta)

    if args.output:
        args.output.write_text(md, encoding="utf-8")
        print(f"Wrote {args.output}")
    else:
        print(md)

    if args.json:
        json_path = (args.output or args.pdf_path).with_suffix(".json")
        json_path.write_text(
            json.dumps({"meta": header_meta, "sections": sections}, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        print(f"Wrote {json_path}")


if __name__ == "__main__":
    main()
