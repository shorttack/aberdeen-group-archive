"""
diag_admit_orphan_sources_v1.py — investigate where the 10 admit-orphan
headlines actually live (or don't).

Background:
  10 row_ids were admitted to P1 via _format_mismatch_admits_v1.json but
  route_v2 cannot match them to any of the 179 corpus.articles entries
  even with recomputed normalize_text(). Their normalized headlines look
  clean (no dashes/slashes/punct), so this isn't a Gotcha-9 normalization
  drift. They are simply not in the corpus.

Question: for each of the 10 orphans, is the source article findable in
  the raw substrate (RTF, PDF segments, Media Quotations.md), or are they
  truly external (web-only, never archived)?

Probes (read-only):
  P1. Headline substring (normalized) in ANY corpus.articles[*].body
      (the corpus stores both rtf+pdf extracted bodies)
  P2. Headline first-6-words appears in _pdf_segments_unclaimed_v1.json
      (PDF segments that the detector dropped — never made it to corpus)
  P3. Headline appears in Peter S Kastner Media Quotations.md
      (Pete's recently-staged ingest file, not yet processed)
  P4. Headline appears in raw RTF substrate (sanity: if it's here but not
      in corpus, the RTF extractor missed it)

Triage classes:
  A — orphan IS in unclaimed-PDF-segments (corpus extractor dropped it,
      could be recovered)
  B — orphan IS in Media Quotations.md (new ingest, expected)
  C — orphan IS in raw RTF but not in corpus (RTF extractor gap)
  D — orphan NOT found in any local substrate (truly external/web-only)

No writes.
"""

from __future__ import annotations
import csv, json, re, sys
from pathlib import Path

ARCHIVE      = Path.home() / "Desktop/Archive/aberdeen-group-archive"
QUOTATIONS   = ARCHIVE / "kastner-author/quotations"
CORPUS_JSON  = QUOTATIONS / "article_corpus_v1.json"
ADMITS_JSON  = QUOTATIONS / "_format_mismatch_admits_v1.json"
UNCLAIMED    = QUOTATIONS / "_pdf_segments_unclaimed_v1.json"
MEDIA_MD     = QUOTATIONS / "Peter S Kastner Media Quotations.md"
CSV_PATH     = QUOTATIONS / "kastner_quotes_clean.csv"
RTF_PATH     = Path.home() / "Desktop/Archive/Kastner_cleaned_quotes.rtf"

def normalize_text(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", (s or "").lower()).strip()

def first_n_words(norm: str, n: int = 6) -> str:
    return " ".join(norm.split()[:n])

def main() -> int:
    print("=== diag_admit_orphan_sources_v1 ===\n")

    # ---- Load 10 orphan row_ids ----
    if not ADMITS_JSON.exists():
        print(f"FATAL: missing {ADMITS_JSON}", file=sys.stderr); return 1
    admit_rids = sorted(int(r) for r in json.loads(ADMITS_JSON.read_text()).get("admit_row_ids", []))
    print(f"admits: {len(admit_rids)} row_ids: {admit_rids}\n")

    # ---- Master CSV: pull headline for each orphan ----
    with open(CSV_PATH, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        by_rid = {}
        for r in reader:
            rid_s = r.get("row_id", "").strip()
            if rid_s.isdigit():
                by_rid[int(rid_s)] = r
    orphans: list[tuple[int, str, str]] = []  # (rid, raw_headline, norm)
    for rid in admit_rids:
        r = by_rid.get(rid)
        if not r:
            orphans.append((rid, "(NOT FOUND IN MASTER)", ""))
            continue
        h = r.get("headline", "")
        orphans.append((rid, h, normalize_text(h)))

    # ---- Load corpus ----
    corpus = json.loads(CORPUS_JSON.read_text())
    articles = corpus.get("articles", [])
    corpus_norms = {normalize_text(a.get("headline", "")) for a in articles if a.get("headline")}
    print(f"corpus: {len(articles)} articles, {len(corpus_norms)} distinct recomputed norms\n")

    # Build a flat corpus-body normalized blob for substring probes (P1).
    # Articles include 'body' (or 'text') field — try both keys.
    corpus_body_blob = ""
    for a in articles:
        body = a.get("body") or a.get("text") or ""
        corpus_body_blob += " " + normalize_text(body)
    print(f"corpus body blob: {len(corpus_body_blob):,} chars (normalized)\n")

    # ---- Load unclaimed PDF segments ----
    unclaimed_norm_blob = ""
    unclaimed_count = 0
    if UNCLAIMED.exists():
        unc = json.loads(UNCLAIMED.read_text())
        # File is either {segments: [...]} or [...]
        segs = unc.get("segments", unc) if isinstance(unc, dict) else unc
        unclaimed_count = len(segs)
        for s in segs:
            if isinstance(s, dict):
                t = s.get("text") or s.get("body") or ""
            else:
                t = str(s)
            unclaimed_norm_blob += " " + normalize_text(t)
    print(f"unclaimed PDF segments: {unclaimed_count} (normalized blob: {len(unclaimed_norm_blob):,} chars)\n")

    # ---- Load Media Quotations.md ----
    media_norm_blob = ""
    if MEDIA_MD.exists():
        media_norm_blob = normalize_text(MEDIA_MD.read_text(errors="replace"))
    print(f"Media Quotations.md: {'present' if media_norm_blob else 'MISSING'} "
          f"(normalized: {len(media_norm_blob):,} chars)\n")

    # ---- Load raw RTF ----
    rtf_norm_blob = ""
    if RTF_PATH.exists():
        # Strip RTF control words crudely for the substring probe
        raw = RTF_PATH.read_text(errors="replace")
        # Remove \word and {...} control groups
        stripped = re.sub(r"\\[a-zA-Z]+-?\d*\s?", " ", raw)
        stripped = re.sub(r"[{}]", " ", stripped)
        rtf_norm_blob = normalize_text(stripped)
    print(f"raw RTF: {'present' if rtf_norm_blob else 'MISSING'} "
          f"(normalized: {len(rtf_norm_blob):,} chars)\n")

    # ---- Per-orphan triage ----
    print(f"--- per-orphan triage (10 rows) ---\n")
    headers = ["rid", "headline (truncated)", "P1:corpus-body", "P2:unclaimed-PDF",
               "P3:Media-md", "P4:raw-RTF", "class"]
    print(f"{headers[0]:>5}  {headers[1]:<58} {headers[2]:<14} {headers[3]:<16} {headers[4]:<10} {headers[5]:<10} {headers[6]}")
    triage_counts = {"A":0,"B":0,"C":0,"D":0,"AB":0,"AC":0,"BC":0,"ABC":0}

    for rid, h, nh in orphans:
        if not nh:
            print(f"{rid:>5}  {h[:56]:<58} —              —                —          —          (no headline)")
            continue
        probe = first_n_words(nh, 6)
        p1 = probe in corpus_body_blob
        p2 = probe in unclaimed_norm_blob
        p3 = probe in media_norm_blob
        p4 = probe in rtf_norm_blob

        # Class: A=in_unclaimed_PDF, B=in_media_md, C=in_RTF_only, D=nowhere
        hits = []
        if p2: hits.append("A")
        if p3: hits.append("B")
        if p4 and not p1: hits.append("C")  # RTF has it but corpus body doesn't
        if not (p1 or p2 or p3 or p4):
            cls = "D"
        elif hits:
            cls = "+".join(hits)
        else:
            cls = "(in_corpus_body_only)"  # P1 hit but headline isn't standalone — weird

        # Count primary class
        key = "".join(hits) or "D"
        if key in triage_counts:
            triage_counts[key] += 1

        print(f"{rid:>5}  {h[:56]:<58} {'YES' if p1 else 'no':<14} "
              f"{'YES' if p2 else 'no':<16} {'YES' if p3 else 'no':<10} "
              f"{'YES' if p4 else 'no':<10} {cls}")

    print(f"\n--- triage summary ---")
    print(f"  A  (recoverable from unclaimed PDF segments): see counts above")
    print(f"  B  (Media Quotations.md ingest pending)")
    print(f"  C  (raw RTF has it; corpus extractor gap)")
    print(f"  D  (truly external — no local substrate)")
    print(f"\nraw counts: {triage_counts}")

    return 0

if __name__ == "__main__":
    sys.exit(main())
