"""
diag_route_v2_residuals_v1.py — diagnose route_v2 residuals

Two questions:

Q1 — admit-orphans (10 row_ids): why do these admits NOT match corpus via
  recomputed normalize_text() in route_v2, when diag_routing_vs_union_v1.py
  reported admits add 0 new rows to recomputed-set (i.e., they overlap entirely
  with corpus-recomputed matches)?

  Hypothesis: the two diags use different inputs to normalize_text():
    - diag_routing_vs_union_v1.py: normalize_text(corpus.articles[*].headline)
      vs normalize_text(master_csv_row.headline_norm-field)
    - route_v2.py: normalize_text(master_csv_row.headline) [recomputed at routing
      time, NOT trusting the stored headline_norm field]
  If admits have a master row where master.headline normalizes differently
  from corpus.headline, they'd orphan in route_v2 while still being "covered"
  by the diag that compared field-vs-field.

Q2 — 244 P1 rows excluded as empty horizon: authoring gap (blank cell) or
  parse failure on values that exist? Histogram of forecast_horizon_years
  raw values on the 244 excluded rows.

Read-only diag. No writes.
"""

from __future__ import annotations
import csv, json, re, sys
from collections import Counter
from pathlib import Path

ARCHIVE = Path.home() / "Desktop/Archive/aberdeen-group-archive"
QUOTATIONS = ARCHIVE / "kastner-author/quotations"
CORPUS_JSON = QUOTATIONS / "article_corpus_v1.json"
CSV_PATH = QUOTATIONS / "kastner_quotes_clean.csv"
ADMITS_JSON = QUOTATIONS / "_format_mismatch_admits_v1.json"

def normalize_text(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", (s or "").lower()).strip()

def parse_horizon(raw: str):
    """Mirror route_v2's parse_horizon. Returns (horizons_list, warn_or_None)."""
    if raw is None: return [], None
    s = raw.strip()
    if not s: return [], None
    # range "3-7"
    m = re.match(r"^\s*(\d+)\s*[-\u2013]\s*(\d+)\s*$", s)
    if m:
        lo, hi = int(m.group(1)), int(m.group(2))
        if lo > hi: lo, hi = hi, lo
        if lo == hi: return [lo], None
        return [lo, hi], None
    # open-ended "5+"
    m = re.match(r"^\s*(\d+)\s*\+\s*$", s)
    if m: return [int(m.group(1))], None
    # bare int
    m = re.match(r"^\s*(\d+)\s*$", s)
    if m: return [int(m.group(1))], None
    return [], f"unparseable: {raw!r}"

def is_rejected(r: dict) -> bool:
    return bool(r.get("reject", "").strip())

def main() -> int:
    print("=== diag_route_v2_residuals_v1 ===\n")

    # Load corpus, build the SAME map route_v2 builds
    corpus = json.loads(CORPUS_JSON.read_text())
    article_by_norm: dict[str, dict] = {}
    for a in corpus.get("articles", []):
        nh = normalize_text(a.get("headline", ""))
        if nh:
            article_by_norm.setdefault(nh, a)
    print(f"corpus: {len(article_by_norm)} distinct recomputed headline_norms\n")

    # Load admits
    admits = set()
    if ADMITS_JSON.exists():
        admits = {int(r) for r in json.loads(ADMITS_JSON.read_text()).get("admit_row_ids", [])}
    print(f"admits: {sorted(admits)}\n")

    # Load master CSV
    with open(CSV_PATH, newline="", encoding="utf-8") as f:
        master_rows = list(csv.DictReader(f))
    by_rid = {int(r["row_id"]): r for r in master_rows if r.get("row_id", "").strip().isdigit()}
    print(f"master: {len(master_rows)} rows\n")

    # ---- Q1: admit-orphans ----
    print("--- Q1: admit-orphans (10 row_ids) ---")
    print(f"{'rid':>5} {'master.headline':<60} {'norm(master.headline)':<50} {'in corpus?'}")
    for rid in sorted(admits):
        r = by_rid.get(rid)
        if not r:
            print(f"{rid:>5} (row not found in master)")
            continue
        h = r.get("headline", "")
        nh = normalize_text(h)
        hit = nh in article_by_norm
        print(f"{rid:>5} {h[:58]:<60} {nh[:48]:<50} {'YES' if hit else 'NO'}")
        if not hit and nh:
            # Find closest corpus norm (by prefix)
            cands = [cn for cn in article_by_norm if cn[:20] == nh[:20] or nh[:20] in cn]
            for c in cands[:2]:
                print(f"        ~near corpus: {c[:80]}")
    print()

    # ---- Q2: 244 empty-horizon distribution ----
    print("--- Q2: empty-horizon distribution on P1-eligible rows ---")
    raw_values: Counter = Counter()
    parse_warnings: Counter = Counter()
    blank_count = 0
    nonblank_unparsed = []
    p1_count = 0
    p1_empty_horizon = 0

    for r in master_rows:
        if is_rejected(r):
            continue
        rid_s = r.get("row_id", "").strip()
        if not rid_s.isdigit():
            continue
        rid = int(rid_s)
        nh = normalize_text(r.get("headline", ""))
        in_corpus = bool(nh) and (nh in article_by_norm)
        is_admit = rid in admits
        if not (in_corpus or is_admit):
            continue
        p1_count += 1
        raw = r.get("forecast_horizon_years", "")
        horizons, warn = parse_horizon(raw)
        if not horizons:
            p1_empty_horizon += 1
            stripped = (raw or "").strip()
            if stripped == "":
                blank_count += 1
                raw_values["<blank>"] += 1
            else:
                raw_values[stripped] += 1
                if warn:
                    parse_warnings[warn] += 1
                nonblank_unparsed.append((rid, stripped))

    print(f"P1 rows total: {p1_count}")
    print(f"P1 rows with empty/unparsed horizon: {p1_empty_horizon}")
    print(f"  of which blank: {blank_count}")
    print(f"  of which non-blank but unparsed: {p1_empty_horizon - blank_count}\n")
    print("Top 20 raw values causing empty-horizon:")
    for val, n in raw_values.most_common(20):
        print(f"  {n:>4}  {val!r}")
    print()
    if nonblank_unparsed[:10]:
        print("First 10 non-blank unparsed rows (rid, raw):")
        for rid, raw in nonblank_unparsed[:10]:
            print(f"  rid={rid}  raw={raw!r}")

    return 0

if __name__ == "__main__":
    sys.exit(main())
