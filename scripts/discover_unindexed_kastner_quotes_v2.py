#!/usr/bin/env python3
"""
discover_unindexed_kastner_quotes_v2.py

v2 of the silent-loss discovery script. Same R1/R2/R1+R3 substrate-only
discovery rules as v1, but the output CSV now mirrors
`kastner_quotes_clean.csv`'s 18-column schema with provenance columns
appended, and a leading `reject` column for Pete's review pass.

Schema (column order, left to right):

  0  reject                           ← Pete-prescribed. Default empty = ADMIT.
                                       Any non-whitespace character = REJECT.
                                       The apply script will check
                                       `bool(row["reject"].strip())`.
  1-18 canonical kastner_quotes_clean.csv columns (verbatim, same order):
     row_id, article_seq, date, headline, publication, author, content_type,
     kastner_quotation, immediate_context, is_predictive, prescience_score,
     prescience_rationale, forecast_horizon_years, theme, decade,
     accuracy_outcome, verdict_rationale, verdict_sources
  19+ provenance columns (v2 additions, kept at the right edge so importing
      tools see the canonical schema first):
     source_segment_idx, classification, discovery_rule,
     discovery_confidence, detector_headline_attempted

Auto-fill rules per row:

  reject                  → "" (blank; Pete fills)
  row_id                  → "" (apply script generates fresh IDs)
  article_seq             → "" (analyst judgment)
  date                    → "" (no reliable substrate inference)
  headline                → detector_headline_attempted (Pete edits)
  publication             → _guess_pub() best-effort scan of body
  author                  → "" (analyst judgment)
  content_type            → "" (analyst judgment)
  kastner_quotation       → 500-char window centered on the Kastner/Aberdeen hit
  immediate_context       → wider 1000-char window centered on the hit
  is_predictive           → "" (analyst judgment)
  prescience_score        → "" (analyst judgment / downstream Pass C)
  prescience_rationale    → "" (analyst judgment)
  forecast_horizon_years  → "" (analyst judgment)
  theme                   → "" (analyst judgment)
  decade                  → "" (analyst judgment; date unknown)
  accuracy_outcome        → "" (analyst judgment)
  verdict_rationale       → "" (analyst judgment)
  verdict_sources         → "" (analyst judgment)

Provenance (auto-fill, never edited by Pete):
  source_segment_idx, classification, discovery_rule (R1 / R2 / R1+R3),
  discovery_confidence (high / medium / low), detector_headline_attempted

Output CSV: `kastner-author/quotations/_unindexed_kastner_candidates_v2.csv`
Dry-run by default; --commit writes the CSV.
"""
import csv, json, re, sys
from datetime import datetime, timezone
from pathlib import Path
from collections import Counter

ARCHIVE_REPO = Path("/Users/scott/Desktop/Archive/aberdeen-group-archive")
QUOTATIONS_DIR = ARCHIVE_REPO / "kastner-author/quotations"
CORPUS = QUOTATIONS_DIR / "article_corpus_v1.json"
UNCLAIMED = QUOTATIONS_DIR / "_pdf_segments_unclaimed_v1.json"
CSV_PATH = QUOTATIONS_DIR / "kastner_quotes_clean.csv"
OUT_CSV = QUOTATIONS_DIR / "_unindexed_kastner_candidates_v2.csv"

NAME_RX = re.compile(r"\bKastner\b", re.IGNORECASE)
ABERDEEN_RX = re.compile(r"\bAberdeen(?:\s+Group)?\b", re.IGNORECASE)
ATTR_RX = re.compile(
    r"\b(said|told|noted|argued|predicted|expects?|believes?|forecasts?|"
    r"observed|commented|added|explained|claimed|warned|cautioned)\b",
    re.IGNORECASE,
)

QUOTE_WINDOW = 500       # chars around the hit for kastner_quotation
CONTEXT_WINDOW = 1000    # chars around the hit for immediate_context

# Canonical CSV header (verified from /tmp/quotes.csv against the live
# kastner_quotes_clean.csv). DO NOT REORDER — apply_unindexed_quotes_v2.py
# will rely on this exact order for append-to-master alignment.
CANONICAL_COLS = [
    "row_id", "article_seq", "date", "headline", "publication", "author",
    "content_type", "kastner_quotation", "immediate_context", "is_predictive",
    "prescience_score", "prescience_rationale", "forecast_horizon_years",
    "theme", "decade", "accuracy_outcome", "verdict_rationale",
    "verdict_sources",
]
PROVENANCE_COLS = [
    "source_segment_idx", "classification", "discovery_rule",
    "discovery_confidence", "detector_headline_attempted",
]
OUTPUT_COLS = ["reject"] + CANONICAL_COLS + PROVENANCE_COLS


def context_window(text: str, start: int, end: int, w: int) -> str:
    a = max(0, start - w // 2)
    b = min(len(text), end + w // 2)
    snippet = text[a:b].strip()
    return re.sub(r"\s+", " ", snippet)


def find_all(rx, text):
    return [(m.start(), m.end()) for m in rx.finditer(text)]


def near(spans_a, spans_b, dist: int = 100) -> bool:
    for a0, a1 in spans_a:
        for b0, b1 in spans_b:
            if abs(a0 - b0) < dist or abs(a1 - b1) < dist:
                return True
    return False


def _guess_pub(body: str, csv_pubs: list) -> str:
    body_lo = body.lower()
    hits = [p for p in csv_pubs if p and p.lower() in body_lo]
    return hits[0] if hits else ""


def _make_row(seg, body, s, e, rule, confidence, csv_pubs):
    """Build one output row with canonical schema + provenance + blank reject."""
    quotation = context_window(body, s, e, QUOTE_WINDOW)
    context = context_window(body, s, e, CONTEXT_WINDOW)
    pub = _guess_pub(body, csv_pubs)
    headline = seg.get("headline_attempted") or ""

    return {
        # Pete's review column — blank by default = ADMIT
        "reject": "",
        # Canonical schema (auto-filled where possible, blank otherwise)
        "row_id": "",
        "article_seq": "",
        "date": "",
        "headline": headline,
        "publication": pub,
        "author": "",
        "content_type": "",
        "kastner_quotation": quotation,
        "immediate_context": context,
        "is_predictive": "",
        "prescience_score": "",
        "prescience_rationale": "",
        "forecast_horizon_years": "",
        "theme": "",
        "decade": "",
        "accuracy_outcome": "",
        "verdict_rationale": "",
        "verdict_sources": "",
        # Provenance
        "source_segment_idx": seg["segment_idx"],
        "classification": seg["classification"],
        "discovery_rule": rule,
        "discovery_confidence": confidence,
        "detector_headline_attempted": headline,
    }


def main(commit: bool = False):
    print(f"[discover_unindexed_kastner_quotes_v2] {datetime.now(timezone.utc).isoformat()}")
    print(f"Mode: {'COMMIT' if commit else 'DRY-RUN'}")
    print()

    corpus = json.loads(CORPUS.read_text())
    unclaimed = json.loads(UNCLAIMED.read_text())
    with open(CSV_PATH) as f:
        csv_rows = list(csv.DictReader(f))

    print(f"  corpus articles       : {corpus['article_count']}")
    print(f"  unclaimed segments    : {unclaimed['unclaimed_segment_count']}")
    print(f"  CSV rows              : {len(csv_rows)}")
    print(f"  quote window (chars)  : {QUOTE_WINDOW}")
    print(f"  context window (chars): {CONTEXT_WINDOW}")

    csv_pubs = sorted({(r.get("publication") or "").strip()
                       for r in csv_rows if r.get("publication")})

    rows = []
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

        # R1: every Kastner hit → candidate (with R3 confidence bump)
        for s, e in kastner_hits:
            r1_plus_r3 = (near([(s, e)], aberdeen_hits, 200)
                          and near([(s, e)], attr_hits, 100))
            confidence = "high" if r1_plus_r3 else "medium"
            rule = "R1+R3" if r1_plus_r3 else "R1"
            rows.append(_make_row(seg, body, s, e, rule, confidence, csv_pubs))
            rule_counter[rule] += 1
            class_counter[cls] += 1

        # R2: Aberdeen + attribution but no Kastner-by-name
        if not kastner_hits:
            if aberdeen_hits and near(aberdeen_hits, attr_hits, 100):
                for s, e in aberdeen_hits:
                    if near([(s, e)], attr_hits, 100):
                        rows.append(_make_row(seg, body, s, e, "R2", "low", csv_pubs))
                        rule_counter["R2"] += 1
                        class_counter[cls] += 1
                        break  # one R2 candidate per segment is enough

    print()
    print(f"=== Candidate counts ===")
    print(f"  TOTAL candidates              : {len(rows)}")
    print(f"  by discovery_rule             : {dict(rule_counter)}")
    print(f"  by classification             : {dict(class_counter)}")
    seg_universe = {r["source_segment_idx"] for r in rows}
    print(f"  unique segments with candidates: {len(seg_universe)} / {unclaimed['unclaimed_segment_count']}")
    print()

    # Schema audit: every row must have exactly the OUTPUT_COLS keys
    bad = [i for i, r in enumerate(rows) if set(r.keys()) != set(OUTPUT_COLS)]
    if bad:
        print(f"  !! SCHEMA AUDIT FAIL: {len(bad)} rows have wrong keys (first idx: {bad[0]})")
        sys.exit(1)
    print(f"  schema audit                  : OK ({len(OUTPUT_COLS)} cols per row)")
    print()

    print(f"=== Sample (4 high-confidence R1+R3, 500-char quote window) ===")
    n = 0
    for r in rows:
        if r["discovery_rule"] != "R1+R3":
            continue
        print(f"  seg {r['source_segment_idx']:>4} [{r['classification']}] "
              f"hdl_attempted={r['detector_headline_attempted']!r}")
        print(f"     pub_guess: {r['publication']!r}")
        print(f"     quotation (500c): {r['kastner_quotation'][:400]!r}...")
        print()
        n += 1
        if n >= 4:
            break

    if not commit:
        print("→ DRY-RUN — no CSV written. Pass --commit to write.")
        print(f"   Would write {len(rows)} rows × {len(OUTPUT_COLS)} cols to {OUT_CSV}")
        return

    with open(OUT_CSV, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=OUTPUT_COLS, quoting=csv.QUOTE_ALL)
        w.writeheader()
        for r in rows:
            w.writerow(r)
    print(f"→ WROTE: {OUT_CSV} ({OUT_CSV.stat().st_size:,} bytes, "
          f"{len(rows)} rows × {len(OUTPUT_COLS)} cols)")


if __name__ == "__main__":
    main(commit=("--commit" in sys.argv))
