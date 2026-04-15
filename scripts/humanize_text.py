"""
humanize_text.py

Flags AI-typical patterns in text. Run before showing rewrites/posts to the user.
Returns a JSON report of detected issues. Does NOT auto-rewrite — the rewrite
is the assistant's job, this script just audits.

Usage:
    python humanize_text.py path/to/text.md
    echo "some text" | python humanize_text.py -
"""

import argparse
import json
import re
import sys
from pathlib import Path


HARD_BAN_WORDS = [
    # English
    r"\bdelve(s|d|ing)?\b",
    r"\bnavigat(e|ing)\s+the\s+complexit(y|ies)\b",
    r"\bin\s+today'?s\s+fast[- ]paced\s+world\b",
    r"\bin\s+the\s+realm\s+of\b",
    r"\bunlock(ing)?\s+(the\s+)?potential\b",
    r"\bharness(ing)?\s+the\s+power\b",
    r"\btapestry\b",
    r"\bgame[- ]chang(er|ing)\b",
    r"\brevolutioniz(e|ing|es|ed)\b",
    r"\bin\s+conclusion\b",
    r"\bI\s+hope\s+this\s+helps\b",
    r"\bfeel\s+free\s+to\b",
    r"\bpassionate\s+about\b",
    r"\bresults[- ]driven\b",
    r"\bsynerg(y|ies)\b",
    r"\bleverag(e|ing|es|ed)\b",
    r"\bmore\s+than\s+just\b",
    r"\bit'?s\s+not\s+just\s+\w+,?\s+it'?s\b",
    # Portuguese
    r"\bno\s+mundo\s+acelerado\s+de\s+hoje\b",
    r"\bno\s+universo\s+d[ao]\b",
    r"\bnavegando\s+pelas\s+complexidades\b",
    r"\brica\s+tapeçaria\b",
    r"\bdivisor\s+de\s+águas\b",
    r"\brevolucionar\b",
    r"\bem\s+conclusão\b",
    r"\bespero\s+que\s+isso\s+ajude\b",
    r"\bfique\s+à\s+vontade\s+para\b",
    r"\bapaixonado\s+por\s+tecnologia\b",
    r"\borientado\s+a\s+resultados\b",
    r"\bsinergia\b",
    r"\bao\s+final\s+do\s+dia\b",
    r"\bmais\s+do\s+que\s+apenas\b",
]


def count_em_dashes(text: str) -> int:
    return text.count("—")


def parallel_bullets(text: str) -> int:
    """Count consecutive bullet lines that start with the same word class (verb-ing or capitalized verb)."""
    lines = [l.strip() for l in text.splitlines() if l.strip().startswith(("-", "•", "*"))]
    if len(lines) < 3:
        return 0
    starts = [l.lstrip("-•* ").split()[0].lower() if l.lstrip("-•* ").split() else "" for l in lines]
    runs = 0
    for i in range(2, len(starts)):
        if starts[i].endswith(("ing", "ar", "er", "ir")) and starts[i - 1].endswith(("ing", "ar", "er", "ir")) and starts[i - 2].endswith(("ing", "ar", "er", "ir")):
            runs += 1
    return runs


def sentence_length_variance(text: str) -> float:
    sentences = re.split(r"(?<=[.!?])\s+", text)
    lengths = [len(s.split()) for s in sentences if s.strip()]
    if len(lengths) < 3:
        return 0.0
    mean = sum(lengths) / len(lengths)
    var = sum((l - mean) ** 2 for l in lengths) / len(lengths)
    return round(var ** 0.5, 2)


def find_banned(text: str) -> list[dict]:
    hits = []
    for pattern in HARD_BAN_WORDS:
        for m in re.finditer(pattern, text, flags=re.IGNORECASE):
            hits.append({"pattern": pattern, "match": m.group(0), "position": m.start()})
    return hits


def audit(text: str) -> dict:
    word_count = len(text.split())
    em_dashes = count_em_dashes(text)
    em_dash_ratio = round(em_dashes / max(word_count / 300, 1), 2)
    banned = find_banned(text)
    parallel = parallel_bullets(text)
    sd = sentence_length_variance(text)

    score = 100
    score -= len(banned) * 15
    score -= max(0, em_dashes - 1) * 5 if word_count < 300 else max(0, em_dashes - (word_count // 300)) * 5
    score -= parallel * 10
    if sd < 4 and word_count > 80:
        score -= 15  # too uniform
    score = max(0, min(100, score))

    return {
        "word_count": word_count,
        "human_score": score,
        "verdict": (
            "PASS" if score >= 80
            else "REVIEW" if score >= 60
            else "REWRITE"
        ),
        "banned_phrases_found": banned,
        "em_dashes": em_dashes,
        "em_dashes_per_300_words": em_dash_ratio,
        "parallel_bullet_runs": parallel,
        "sentence_length_stddev": sd,
        "recommendations": build_recommendations(banned, em_dashes, parallel, sd, word_count),
    }


def build_recommendations(banned, em_dashes, parallel, sd, wc) -> list[str]:
    recs = []
    if banned:
        recs.append(f"Remove or replace {len(banned)} banned phrase(s). See banned_phrases_found.")
    if em_dashes > max(1, wc // 300):
        recs.append(f"Too many em-dashes ({em_dashes}). Replace most with commas, parentheses, or new sentences.")
    if parallel > 0:
        recs.append("Parallel bullet structure detected. Vary the opening word class across bullets.")
    if sd < 4 and wc > 80:
        recs.append("Sentences too uniform in length. Mix short, medium, and long.")
    if not recs:
        recs.append("No major issues detected. Still read aloud as a final check.")
    return recs


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=str, help="Path to text file, or '-' for stdin")
    args = parser.parse_args()

    if args.path == "-":
        text = sys.stdin.read()
    else:
        text = Path(args.path).read_text(encoding="utf-8")

    report = audit(text)
    print(json.dumps(report, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
