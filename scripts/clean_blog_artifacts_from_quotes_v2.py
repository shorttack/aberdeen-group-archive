#!/usr/bin/env python3
"""
clean_blog_artifacts_from_quotes_v2.py

Dry-run candidate generator for the 11 _master_quotations_prescience.csv rows
flagged with blog_scrape_contamination_flag=true.

v2 improves the v1 review report by flagging proposed quotes that still appear
to begin mid-word after artifact stripping. It still does not modify masters.
"""
from __future__ import annotations

import argparse
import csv
import re
from pathlib import Path


TARGET_ROW_IDS = {
    "1180", "1183", "1186", "1187", "1188", "1190",
    "1193", "1194", "1199", "1200", "1208",
}

FOOTER_RE = re.compile(
    r"\s*(?:--\s*)?Peter S\.?\s+Kastner\s+Posted by Anonymous at\b.*",
    re.IGNORECASE | re.DOTALL,
)
SHARE_RE = re.compile(
    r"No comments:\s*Email ThisBlogThis!Share to TwitterShare to FacebookShare to Pinterest\s*",
    re.IGNORECASE,
)
BLOG_HEADER_RE = re.compile(
    r"^Peter S Kastner Blogging at oncomputerstips\.blogspot\.com\s+",
    re.IGNORECASE,
)
DATE_PREFIX_RE = re.compile(
    r"^(Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday),\s+"
    r"(January|February|March|April|May|June|July|August|September|October|November|December)\s+"
    r"\d{1,2},\s+\d{4}\s+",
    re.IGNORECASE,
)


def clean_quote(q: str) -> tuple[str, str, str]:
    original = " ".join((q or "").split())
    if not original:
        return "", "empty_source", "manual_review"

    q0 = BLOG_HEADER_RE.sub("", original).strip()
    q0 = DATE_PREFIX_RE.sub("", q0).strip()

    m = FOOTER_RE.search(q0)
    if m and m.start() >= 80:
        cleaned = q0[: m.start()].strip(" -")
        return cleaned, "truncate_at_author_footer", "auto_candidate"

    if m and m.start() < 80:
        after = SHARE_RE.split(q0, maxsplit=1)
        if len(after) == 2 and len(after[1].strip()) >= 50:
            cleaned = DATE_PREFIX_RE.sub("", after[1].strip()).strip(" -")
            return cleaned, "drop_leading_footer_keep_after_share_widget", "manual_review"
        return q0, "leading_footer_no_safe_after_segment", "manual_review"

    if q0 != original:
        return q0, "strip_blog_header_or_date_prefix", "manual_review"

    return original, "no_change_pattern_not_found", "manual_review"


def starts_like_fragment(text: str) -> bool:
    t = (text or "").lstrip()
    if not t:
        return True
    first_token = t.split(maxsplit=1)[0].strip("\"'([{")
    if not first_token:
        return True
    if first_token[0].islower():
        return True
    # Known short scrape fragments observed in this batch.
    if first_token.lower() in {"er", "tory", "ilable"}:
        return True
    return False


def recommendation(row: dict[str, str], proposed: str, disposition: str, rule: str) -> str:
    row_id = row.get("row_id", "")
    headline = row.get("headline", "")
    if row_id == "1180" or "Blogging at oncomputerstips.blogspot.com" in headline:
        return "manual_review_probable_non_prediction_bio"
    if starts_like_fragment(proposed):
        return "manual_review_fragment_start"
    if disposition == "auto_candidate":
        return "auto_strip_blog_artifact"
    if rule == "drop_leading_footer_keep_after_share_widget":
        return "manual_review_leading_footer_split"
    return "manual_review"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--master",
        default=str(Path.home() / "Desktop/Archive/aberdeen-group-archive/_master_quotations_prescience.csv"),
    )
    ap.add_argument(
        "--out",
        default=str(Path.home() / "Desktop/Archive/aberdeen-group-archive/Perplexity_Only/blog_artifact_cleaning_candidates_v2.csv"),
    )
    args = ap.parse_args()

    master = Path(args.master)
    out = Path(args.out)

    with master.open(newline="") as f:
        rows = list(csv.DictReader(f))

    candidates = []
    for r in rows:
        rid = str(r.get("row_id", ""))
        if rid not in TARGET_ROW_IDS:
            continue
        old = r.get("quote", "")
        new, rule, disposition = clean_quote(old)
        rec = recommendation(r, new, disposition, rule)
        candidates.append(
            {
                "row_id": rid,
                "headline": r.get("headline", ""),
                "date": r.get("date", ""),
                "final_score": r.get("final_score", ""),
                "final_bucket": r.get("final_bucket", ""),
                "rule": rule,
                "disposition": disposition,
                "recommendation": rec,
                "fragment_start_flag": "true" if starts_like_fragment(new) else "false",
                "old_len": len(old),
                "new_len": len(new),
                "delta_len": len(new) - len(old),
                "old_quote": old,
                "proposed_quote": new,
            }
        )

    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", newline="") as f:
        fieldnames = [
            "row_id", "headline", "date", "final_score", "final_bucket",
            "rule", "disposition", "recommendation", "fragment_start_flag",
            "old_len", "new_len", "delta_len", "old_quote", "proposed_quote",
        ]
        w = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
        w.writeheader()
        w.writerows(candidates)

    print(f"wrote {out}")
    print(f"candidates={len(candidates)}")
    for c in candidates:
        print(
            f"{c['row_id']}: {c['recommendation']} "
            f"old={c['old_len']} new={c['new_len']} bucket={c['final_bucket']}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
