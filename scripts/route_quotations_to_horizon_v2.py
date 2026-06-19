#!/usr/bin/env python3
"""
route_quotations_to_horizon_v2.py — v1.8.0 Quotations Corpus

v2 (2026-06-19) — Gotcha 9 fix: recompute headline_norm from headline
----------------------------------------------------------------------
v1 trusted the corpus's stored `headline_norm` field. That field was
written by the RTF extractor / PDF detector's normalizer, which keeps
dashes, slashes, periods, and commas. union_article_corpus_v2.py's
P1-routing call uses normalize_text(headline) at routing time, which
strips all non-alphanumeric chars. Result: v1 undercounted P1 by 257
rows (217 vs union's 474).

v2 recomputes headline_norm via normalize_text(article.headline) so the
lookup matches union v2 exactly. Verified against diag_routing_vs_union_v1:
recomputed-set yields 474 P1 rows = 464 (non-admit, matches union v2) +
10 admits.

v1.8.0 Quotations Corpus

Read the substrate trinity + format-mismatch admit manifest, then route every
Pipeline-1-eligible CSV row to a horizon bucket. Emit per-(article, horizon)
routing tuples that the v1.8.0 scorer consumes downstream.

INPUTS
------
  kastner-author/quotations/article_corpus_v1.json          (179 articles)
  kastner-author/quotations/kastner_quotes_clean.csv        (1208 rows)
  kastner-author/quotations/_format_mismatch_admits_v1.json (10 admits)

OUTPUTS (written under kastner-author/quotations/ when --commit)
---------------------------------------------------------------
  1. pipeline_1_routing_v1.json    canonical routing artifact
     Schema:
       {
         "schema_version": "v1",
         "generated_at": ISO8601,
         "article_count": int,
         "row_count_eligible": int,
         "routing_tuples": [
           {
             "article_id": "<source>-<source_idx>",  e.g. "rtf-12", "pdf-47"
             "headline_norm": str,
             "horizon_label": "prefilter_skip" | "SH-3y" | "SH-5y" | "LH",
             "horizon_int": int,        # the parsed horizon (range -> exemplar)
             "csv_row_ids": [int, ...]
           }, ...
         ],
         "summary_by_label": {label: count_tuples, ...}
       }

  2. routing_summary.csv           human-spot-check artifact
     Columns: article_id, headline_norm, horizon_label, horizon_int, row_id

HORIZON ROUTING RULES (per WORKLIST item, 2026-06-19)
-----------------------------------------------------
  horizon = 0           -> prefilter_skip   (not predictive)
  1 <= horizon <= 3     -> SH-3y            (short horizon, 3-year window)
  4 <= horizon <= 7     -> SH-5y            (short horizon, 5-year window)
  horizon >= 8          -> LH               (long horizon)

  Range strings like "3-7" split: one row contributes TWO routing tuples
  (one to SH-3y for horizon=3, one to SH-5y for horizon=7).
  Open-ended like "5+" treated as horizon=5 (single tuple).
  Unparseable values: logged as warnings, row excluded from routing.

PIPELINE-1 ELIGIBILITY (matches union_article_corpus_v2.py routing)
-------------------------------------------------------------------
  A CSV row is Pipeline-1-eligible if EITHER:
    (a) normalize(headline) is in the article_corpus headline_norm set, OR
    (b) row_id is in _format_mismatch_admits_v1.json admit list (override)

  For admit-override rows, article membership is best-effort via headline_norm;
  if no corpus article matches, article_id is "admit-orphan-<row_id>" and
  headline_norm is the row's normalized headline.

INVARIANTS
----------
  - Dry-run default; --commit opt-in
  - csv.QUOTE_ALL on every CSV write
  - Read-only on inputs
  - Producer/consumer schema diff: every column referenced is verified to exist
  - Sanity: sum(routing tuple csv_row_ids) preserves Pipeline-1 row count
    (each row may produce 1 or 2 tuples; we track row-level coverage separately)

USAGE
-----
  python3 route_quotations_to_horizon_v1.py            # dry-run
  python3 route_quotations_to_horizon_v1.py --commit   # write artifacts
"""
from __future__ import annotations
import csv, json, re, sys, unicodedata
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

# ---------------------------------------------------------------- paths ----
QUOTATIONS    = Path.home() / "Desktop/Archive/aberdeen-group-archive/kastner-author/quotations"
CORPUS_JSON   = QUOTATIONS / "article_corpus_v1.json"
CSV_PATH      = QUOTATIONS / "kastner_quotes_clean.csv"
ADMITS_JSON   = QUOTATIONS / "_format_mismatch_admits_v1.json"
OUT_JSON      = QUOTATIONS / "pipeline_1_routing_v1.json"
OUT_CSV       = QUOTATIONS / "routing_summary.csv"

# ---------------------------------------------------------------- helpers --
def normalize_text(s: str) -> str:
    """Match union_article_corpus_v1.py normalization."""
    if not s:
        return ""
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = s.lower()
    s = re.sub(r"[^a-z0-9 ]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def parse_horizon(raw: str) -> tuple[list[int], str | None]:
    """Parse forecast_horizon_years cell.

    Returns (list_of_ints, parse_warning_or_None).
      - Empty/whitespace -> ([], None) -- excluded from routing silently
      - Int "5"          -> ([5], None)
      - Range "3-7"      -> ([3, 7], None)  (two tuples: low + high)
      - Open "5+"        -> ([5], None)
      - "0"              -> ([0], None)
      - Garbage          -> ([], "parse_error: <raw>")
    """
    s = (raw or "").strip()
    if not s:
        return [], None
    # Plain int
    if s.isdigit():
        return [int(s)], None
    # Range NN-NN
    m = re.fullmatch(r"(\d+)\s*-\s*(\d+)", s)
    if m:
        lo, hi = int(m.group(1)), int(m.group(2))
        if lo <= hi:
            return [lo, hi], None
        return [], f"parse_error: range out of order {raw!r}"
    # Open-ended NN+
    m = re.fullmatch(r"(\d+)\s*\+", s)
    if m:
        return [int(m.group(1))], None
    return [], f"parse_error: {raw!r}"


def horizon_label(h: int) -> str:
    if h == 0:
        return "prefilter_skip"
    if 1 <= h <= 3:
        return "SH-3y"
    if 4 <= h <= 7:
        return "SH-5y"
    if h >= 8:
        return "LH"
    return "parse_error"  # negative — shouldn't happen


# ---------------------------------------------------------------- main -----
def main() -> int:
    commit = "--commit" in sys.argv
    print(f"=== route_quotations_to_horizon_v1.py — mode={'COMMIT' if commit else 'DRY-RUN'} ===\n")

    # ------ inputs ------------------------------------------------------
    for p in (CORPUS_JSON, CSV_PATH):
        if not p.exists():
            print(f"FATAL: missing input {p}", file=sys.stderr); return 1
    with open(CORPUS_JSON) as f:
        corpus = json.load(f)
    articles = corpus.get("articles", [])
    print(f"corpus: {CORPUS_JSON.name} ({len(articles)} articles)")

    # Build headline_norm -> article lookup
    # v2 FIX: recompute from headline (NOT trust the stored field) — matches
    # union_article_corpus_v2.py's routing-time normalize_text() call. The
    # stored corpus.articles[*].headline_norm field uses a producer-stage
    # normalizer that keeps dashes/slashes/commas (Gotcha 9).
    article_by_norm = {}
    field_vs_recomp_diffs = 0
    for a in articles:
        stored_norm = a.get("headline_norm", "")
        nh = normalize_text(a.get("headline", ""))
        if stored_norm and stored_norm != nh:
            field_vs_recomp_diffs += 1
        if nh:
            # First-wins (matches union dedup behavior; RTF wins ties already)
            article_by_norm.setdefault(nh, a)
    print(f"  distinct headline_norms in corpus (recomputed): {len(article_by_norm)}")
    if field_vs_recomp_diffs:
        print(f"  v2: {field_vs_recomp_diffs} corpus articles where stored "
              f"headline_norm field differs from recomputed (Gotcha 9 fix "
              f"applies — trusting recomputed)")

    with open(CSV_PATH, newline="") as f:
        reader = csv.DictReader(f)
        master_cols = reader.fieldnames or []
        rows = list(reader)
    print(f"\nmaster: {CSV_PATH.name} ({len(rows)} rows, {len(master_cols)} cols)")

    # producer/consumer schema diff (Gotcha 9)
    required = ["row_id", "headline", "forecast_horizon_years"]
    missing = [c for c in required if c not in master_cols]
    if missing:
        print(f"FATAL: master missing required cols: {missing}", file=sys.stderr); return 1

    # ------ admit manifest ---------------------------------------------
    admit_row_ids: set[int] = set()
    if ADMITS_JSON.exists():
        with open(ADMITS_JSON) as f:
            _adm = json.load(f)
        admit_row_ids = {int(r) for r in _adm.get("admit_row_ids", [])}
        print(f"\nadmits: {ADMITS_JSON.name} ({len(admit_row_ids)} row_ids force-routed to P1)")
    else:
        print(f"\nadmits: (absent — no overrides)")

    # ------ Pipeline-1 eligibility partition ----------------------------
    p1_rows: list[dict] = []
    p2_rows: list[dict] = []
    for r in rows:
        nh = normalize_text(r.get("headline", ""))
        try:
            rid = int(r.get("row_id", ""))
        except (ValueError, TypeError):
            rid = None
        if (rid is not None and rid in admit_row_ids) or (nh and nh in article_by_norm):
            p1_rows.append(r)
        else:
            p2_rows.append(r)

    print(f"\nPipeline-1 eligible: {len(p1_rows)} rows")
    print(f"Pipeline-2 (ineligible for routing): {len(p2_rows)} rows")
    assert len(p1_rows) + len(p2_rows) == len(rows), "row partition lost rows"

    # ------ horizon parse + route ---------------------------------------
    # Group by article_id within P1
    # routing_buckets: (article_id, headline_norm, horizon_label, horizon_int) -> [row_ids]
    routing_buckets: dict[tuple, list[int]] = defaultdict(list)
    parse_warnings: list[tuple[int, str]] = []
    excluded_empty_horizon: list[int] = []
    admit_orphans: list[int] = []
    horizons_per_row: Counter = Counter()  # count of routing tuples each row produces

    for r in p1_rows:
        try:
            rid = int(r["row_id"])
        except (ValueError, TypeError):
            continue
        nh = normalize_text(r.get("headline", ""))

        # Resolve article_id
        article = article_by_norm.get(nh)
        if article is not None:
            article_id = f"{article.get('source', 'unk')}-{article.get('source_idx', '?')}"
            art_norm = nh
        else:
            # Admit-override orphan (row admitted via manifest but headline doesn't
            # match any corpus article — expected for F1/F3/F5/F6 admits)
            article_id = f"admit-orphan-{rid}"
            art_norm = nh
            admit_orphans.append(rid)

        # Parse horizon
        horizons, warn = parse_horizon(r.get("forecast_horizon_years", ""))
        if warn:
            parse_warnings.append((rid, warn))
            continue
        if not horizons:
            excluded_empty_horizon.append(rid)
            continue

        # For range, both endpoints get a tuple. For single, one tuple.
        for h in horizons:
            label = horizon_label(h)
            key = (article_id, art_norm, label, h)
            routing_buckets[key].append(rid)
            horizons_per_row[rid] += 1

    # ------ summarize ---------------------------------------------------
    label_counter = Counter(k[2] for k in routing_buckets)
    print(f"\nrouting tuples: {len(routing_buckets)}")
    print(f"  by label: {dict(label_counter)}")
    print(f"\nrows producing N routing tuples:")
    n_dist = Counter(horizons_per_row.values())
    for n, count in sorted(n_dist.items()):
        print(f"  rows producing {n} tuple(s): {count}")
    rows_routed = len(horizons_per_row)
    print(f"\ntotal P1 rows routed:      {rows_routed}")
    print(f"P1 rows excluded (empty):  {len(excluded_empty_horizon)}")
    print(f"P1 rows excluded (parse):  {len(parse_warnings)}")
    assert rows_routed + len(excluded_empty_horizon) + len(parse_warnings) == len(p1_rows), \
        "row coverage broken"

    print(f"\nadmit-orphans (admitted rows with no corpus article match): {len(admit_orphans)}")
    if admit_orphans:
        print(f"  row_ids: {admit_orphans}")

    if parse_warnings[:8]:
        print(f"\nfirst 8 parse warnings:")
        for rid, w in parse_warnings[:8]:
            print(f"  row_id={rid}  {w}")

    # ------ build artifact ---------------------------------------------
    routing_tuples = []
    for (article_id, art_norm, label, horizon_int), row_ids in sorted(routing_buckets.items()):
        routing_tuples.append({
            "article_id": article_id,
            "headline_norm": art_norm,
            "horizon_label": label,
            "horizon_int": horizon_int,
            "csv_row_ids": sorted(set(row_ids)),
        })

    payload = {
        "schema_version": "v1",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "source_corpus": CORPUS_JSON.name,
        "source_csv": CSV_PATH.name,
        "source_admits": ADMITS_JSON.name if ADMITS_JSON.exists() else None,
        "article_count": len(articles),
        "row_count_eligible": len(p1_rows),
        "row_count_routed": rows_routed,
        "row_count_excluded_empty_horizon": len(excluded_empty_horizon),
        "row_count_parse_warnings": len(parse_warnings),
        "routing_tuple_count": len(routing_tuples),
        "summary_by_label": dict(label_counter),
        "routing_tuples": routing_tuples,
        "parse_warnings": [{"row_id": rid, "warning": w} for rid, w in parse_warnings],
        "excluded_empty_horizon_row_ids": sorted(excluded_empty_horizon),
        "admit_orphan_row_ids": sorted(admit_orphans),
    }

    # ------ dry-run or write -------------------------------------------
    if not commit:
        print(f"\nDRY-RUN: no writes. Pass --commit to ship artifacts.")
        print(f"\nWould write:")
        print(f"  {OUT_JSON} (~{len(json.dumps(payload)):,} bytes JSON)")
        print(f"  {OUT_CSV}  ({len(routing_tuples)} routing tuples flattened to rows)")
        return 0

    if not QUOTATIONS.exists():
        print(f"FATAL: output dir missing: {QUOTATIONS}", file=sys.stderr); return 1

    # Write JSON
    OUT_JSON.write_text(json.dumps(payload, indent=2, default=str))
    print(f"\nwrote: {OUT_JSON.name} ({OUT_JSON.stat().st_size:,} bytes)")

    # Write summary CSV (flatten: one row per (tuple, row_id) pair)
    with open(OUT_CSV, "w", newline="") as f:
        w = csv.writer(f, quoting=csv.QUOTE_ALL)
        w.writerow(["article_id", "headline_norm", "horizon_label", "horizon_int", "row_id"])
        for t in routing_tuples:
            for rid in t["csv_row_ids"]:
                w.writerow([t["article_id"], t["headline_norm"], t["horizon_label"],
                            t["horizon_int"], rid])
    print(f"wrote: {OUT_CSV.name} ({OUT_CSV.stat().st_size:,} bytes)")

    print(f"\n=== GREEN — route_quotations_to_horizon_v1 complete ===")
    print(f"\nNEXT: v1.8.0 scorer reads pipeline_1_routing_v1.json and does NOT")
    print(f"re-derive horizon routing from the CSV.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
