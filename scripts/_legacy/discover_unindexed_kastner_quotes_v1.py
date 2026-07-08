#!/usr/bin/env python3
"""
discover_unindexed_kastner_quotes_v1.py

Discover Kastner-bearing PDF passages that are NOT in
`kastner_quotes_clean.csv`. These are the silent-loss candidates — Kastner
quotes that exist in the source PDF but were never indexed by Pete's
curation pass, and therefore would never reach Pipeline 1 OR Pipeline 2.

Reads ONLY the salvage substrate (`_pdf_segments_unclaimed_v1.json`) — does
NOT re-parse the source PDF. Output is candidates-for-review, not
auto-admissions; Pete reviews each, decides yes/no, and a follow-on script
appends approved rows to `kastner_quotes_clean.csv` + rebuilds the corpus.

Three discovery rules (apply per unclaimed segment):

  R1 — Kastner-by-name mention. Any case-insensitive match of /\\bKastner\\b/
       in the segment body marks a candidate.
  R2 — Aberdeen-attribution mention. /\\bAberdeen Group\\b/ paired with an
       analyst attribution verb ("said", "told", "noted", "argued",
       "predicted", "expects") within 100 chars. Catches Kastner quotes
       attributed only to "Aberdeen Group" when the analyst name is
       implicit. (May produce some non-Kastner Aberdeen analyst false-
       positives — manageable; Pete reviews.)
  R3 — Aberdeen-attribution within Kastner-by-name segment (subset of R1;
       used only for confidence scoring).

Per-segment output (one row per CANDIDATE QUOTE found, not per segment —
a segment with three "Kastner said" passages yields three rows):

  - segment_idx (PDF segment index in _pdf_segments_unclaimed)
  - classification (ARTICLE_HEAD / ARTICLE_CONTINUATION / UNKNOWN)
  - detector_headline_attempted (raw detector output, for context)
  - publication_hint (CSV-cross-reference: any CSV row's publication that
    appears in segment header? best-effort)
  - date_hint (similar; from segment metadata if any)
  - quote_passage (the ~200-char window around the Kastner/Aberdeen hit)
  - confidence (R1+R3 high / R1 medium / R2 low)
  - rule (R1, R2, or R1+R3)
  - in_corpus_already (T/F: does the segment's detector_headline match a
    corpus article? If T, the segment is already represented but might
    have unindexed quotes inside it — Pete may want to add them as
    additional quote rows)

Output CSV: `kastner-author/quotations/_unindexed_kastner_candidates_v1.csv`

Dry-run by default; --commit writes the CSV.
"""
import csv, json, re, sys, unicodedata
from datetime import datetime, timezone
from pathlib import Path
from collections import Counter

ARCHIVE_REPO = Path("/Users/scott/Desktop/Archive/aberdeen-group-archive")
QUOTATIONS_DIR = ARCHIVE_REPO / "kastner-author/quotations"
CORPUS = QUOTATIONS_DIR / "article_corpus_v1.json"
UNCLAIMED = QUOTATIONS_DIR / "_pdf_segments_unclaimed_v1.json"
CSV_PATH = QUOTATIONS_DIR / "kastner_quotes_clean.csv"
OUT_CSV = QUOTATIONS_DIR / "_unindexed_kastner_candidates_v1.csv"

NAME_RX = re.compile(r"\bKastner\b", re.IGNORECASE)
ABERDEEN_RX = re.compile(r"\bAberdeen(?:\s+Group)?\b", re.IGNORECASE)
ATTR_RX = re.compile(
    r"\b(said|told|noted|argued|predicted|expects?|believes?|forecasts?|"
    r"observed|commented|added|explained|claimed|warned|cautioned)\b",
    re.IGNORECASE,
)

WINDOW = 200  # chars of context around each hit


def context_window(text: str, start: int, end: int, w: int = WINDOW) -> str:
    a = max(0, start - w)
    b = min(len(text), end + w)
    snippet = text[a:b].strip()
    return re.sub(r"\s+", " ", snippet)


def find_all(rx, text):
    return [(m.start(), m.end()) for m in rx.finditer(text)]


def near(spans_a, spans_b, dist: int = 100) -> bool:
    """True iff any pair (a,b) has distance < dist."""
    for a0, a1 in spans_a:
        for b0, b1 in spans_b:
            if abs(a0 - b0) < dist or abs(a1 - b1) < dist:
                return True
    return False


def main(commit: bool = False):
    print(f"[discover_unindexed_kastner_quotes_v1] {datetime.now(timezone.utc).isoformat()}")
    print(f"Mode: {'COMMIT' if commit else 'DRY-RUN'}")
    print()

    corpus = json.loads(CORPUS.read_text())
    unclaimed = json.loads(UNCLAIMED.read_text())
    with open(CSV_PATH) as f:
        csv_rows = list(csv.DictReader(f))

    print(f"  corpus articles      : {corpus['article_count']}")
    print(f"  unclaimed segments   : {unclaimed['unclaimed_segment_count']}")
    print(f"  CSV rows             : {len(csv_rows)}")

    served_norms = {a["headline_norm"] for a in corpus["articles"]}
    csv_pubs = sorted({(r.get("publication") or "").strip()
                       for r in csv_rows if r.get("publication")})

    candidates = []
    rule_counter = Counter()
    class_counter = Counter()

    for seg in unclaimed["segments"]:
        body = seg.get("raw_preview", "")
        if not body:
            continue
        cls = seg["classification"]

        kastner_hits = find_all(NAME_RX, body)
        aberdeen_hits = find_all(ABERDEEN_RX, body)
        attr_hits = find_all(ATTR_RX, body)

        # R1: every Kastner hit → candidate (with R3 confidence bump if Aberdeen+attr nearby)
        for s, e in kastner_hits:
            r1_plus_r3 = (near([(s, e)], aberdeen_hits, 200)
                          and near([(s, e)], attr_hits, 100))
            confidence = "high" if r1_plus_r3 else "medium"
            rule = "R1+R3" if r1_plus_r3 else "R1"
            candidates.append({
                "segment_idx": seg["segment_idx"],
                "classification": cls,
                "detector_headline_attempted": seg.get("headline_attempted") or "",
                "rule": rule,
                "confidence": confidence,
                "quote_passage": context_window(body, s, e),
                "publication_hint": _guess_pub(body, csv_pubs),
                "date_hint": "",
                "in_corpus_already": "F",  # by construction; segment is unclaimed
            })
            rule_counter[rule] += 1
            class_counter[cls] += 1

        # R2: Aberdeen + attribution but no Kastner mention (catch implicit-name quotes)
        if not kastner_hits:
            if aberdeen_hits and near(aberdeen_hits, attr_hits, 100):
                for s, e in aberdeen_hits:
                    if near([(s, e)], attr_hits, 100):
                        candidates.append({
                            "segment_idx": seg["segment_idx"],
                            "classification": cls,
                            "detector_headline_attempted": seg.get("headline_attempted") or "",
                            "rule": "R2",
                            "confidence": "low",
                            "quote_passage": context_window(body, s, e),
                            "publication_hint": _guess_pub(body, csv_pubs),
                            "date_hint": "",
                            "in_corpus_already": "F",
                        })
                        rule_counter["R2"] += 1
                        class_counter[cls] += 1
                        break  # one R2 candidate per segment is enough

    print()
    print(f"=== Candidate counts ===")
    print(f"  TOTAL candidates             : {len(candidates)}")
    print(f"  by rule                      : {dict(rule_counter)}")
    print(f"  by classification            : {dict(class_counter)}")
    seg_universe = {c["segment_idx"] for c in candidates}
    print(f"  unique segments with candidates: {len(seg_universe)} / {unclaimed['unclaimed_segment_count']}")
    print()

    print(f"=== Sample (8 high-confidence R1+R3) ===")
    n = 0
    for c in candidates:
        if c["rule"] != "R1+R3":
            continue
        print(f"  seg {c['segment_idx']:>4} [{c['classification']}] hdl_attempted={c['detector_headline_attempted']!r}")
        print(f"     passage: {c['quote_passage'][:300]!r}")
        print()
        n += 1
        if n >= 8:
            break

    if not commit:
        print("→ DRY-RUN — no CSV written. Pass --commit to write.")
        print(f"   Would write {len(candidates)} rows to {OUT_CSV}")
        return

    fieldnames = ["segment_idx", "classification", "rule", "confidence",
                  "detector_headline_attempted", "publication_hint",
                  "date_hint", "in_corpus_already", "quote_passage"]
    with open(OUT_CSV, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
        w.writeheader()
        for c in candidates:
            w.writerow(c)
    print(f"→ WROTE: {OUT_CSV} ({OUT_CSV.stat().st_size:,} bytes, {len(candidates)} rows)")


def _guess_pub(body: str, csv_pubs: list[str]) -> str:
    """If a CSV publication name appears verbatim in segment body, return it."""
    body_lo = body.lower()
    hits = [p for p in csv_pubs if p and p.lower() in body_lo]
    return hits[0] if hits else ""


if __name__ == "__main__":
    main(commit=("--commit" in sys.argv))
