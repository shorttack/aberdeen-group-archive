#!/usr/bin/env python3
"""
build_sh_calibration_sample_v1.py — Stratified 100-obs short-horizon calibration sample.

Spec: short_horizon_calibration_plan_v1.md
Sister to: Tier A stratification (`Perplexity_Only/prescience_tier_a_sample_v1.csv`)

What this does:
  1. Load _master_observations.csv + _master_studies.csv
  2. Resolve anchor_year for every obs via anchor_year_resolver_v2
  3. Filter to anchor_year ≤ 2020 (both 3y and 5y windows elapsed by 2026-06-15)
  4. Reuse Tier A's `_bucket` taxonomy by joining on obs_id (or by recomputing
     bucket from `collection` + study `type` if the obs isn't in Tier A)
  5. Stratified random draw: ~4 obs per bucket × 25 buckets = ~100 obs
     - Random seed = 20260615 (today YYYYMMDD)
     - Without replacement within bucket
     - Exclude obs already in Tier A and Tier B results (independence)
     - If bucket has < 4 eligible, draw what's available; oversample top buckets
       to reach n=100
  6. Emit CSV with full row + _bucket + _study_type + _study_date + _anchor_year
     + _anchor_source + placeholder human verdict columns

Pre-flight invariants (asserted):
  - Every output row resolves to anchor_year ≤ 2020
  - No obs_id overlap with Tier A or Tier B sample CSVs (if provided via flag)
  - Exactly 100 rows OR a printed reason why fewer

Usage:
  python3 build_sh_calibration_sample_v1.py \
    --obs        ~/Desktop/Archive/aberdeen-group-archive/_master_observations.csv \
    --studies    ~/Desktop/Archive/aberdeen-group-archive/_master_studies.csv \
    --tier-a     ~/Desktop/Archive/aberdeen-group-archive/Perplexity_Only/prescience_tier_a_sample_v1.csv \
    --tier-b     ~/Desktop/Archive/pass_c_v6_tier_b_results.csv \
    --output     ~/Desktop/Archive/prescience_calibration_sh_sample_v1.csv \
    --target-n   100 \
    --per-bucket 4 \
    --seed       20260615
"""
from __future__ import annotations
import argparse
import csv
import random
import sys
from collections import defaultdict, Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from anchor_year_resolver_v2 import resolve_anchor_year, AnchorResolutionError

TODAY_YEAR = 2026
ANCHOR_MAX = 2020   # both windows must be elapsed (5y cutoff at today=2026)

# Output column ordering: master_observations cols, then enrichment, then placeholders
ENRICHMENT_COLS = ["_bucket", "_study_type", "_study_date",
                   "_anchor_year", "_anchor_source"]
PLACEHOLDER_COLS = ["human_verdict_3y", "human_verdict_5y", "human_note"]


def load_csv(path: Path) -> list[dict]:
    with open(path, newline="") as f:
        return list(csv.DictReader(f))


def load_obs_id_set(path: Path | None) -> set:
    if not path or not path.exists():
        return set()
    s = set()
    with open(path, newline="") as f:
        for r in csv.DictReader(f):
            oid = r.get("obs_id")
            if oid:
                s.add(oid)
    return s


def derive_bucket(obs_row: dict, study_row: dict, tier_a_bucket: dict) -> str:
    """Reuse Tier A bucket if obs is in Tier A; else derive from collection + study type.

    Tier A's 25 macro-buckets are:
      market-research, employer-internal, other, memoir, white-paper, dct,
      profile-case, topic-viewpoint, press-trade, consulting-advisory,
      press-news, report, tech-topic, brief, vendor-study, presentation,
      ai-response, transcript, analyst-note, case-study, engineering-tech,
      vendor-marketing, product, whitepaper, employer.
    """
    oid = obs_row.get("obs_id")
    if oid and oid in tier_a_bucket:
        return tier_a_bucket[oid]

    coll = (obs_row.get("collection") or "").strip().lower()
    stype = (study_row.get("type") or "").strip().lower()

    # Quick map for known collection signals (these dominate the corpus)
    if coll == "transcript":
        return "transcript"
    if coll == "kastner-author":
        return "memoir"
    if coll == "ai-arc":
        return "ai-response"
    if coll == "kastner-longitudinal":
        return "topic-viewpoint"

    # Fallback: map common study types to Tier A's 25 buckets
    type_to_bucket = {
        "market-study": "market-research",
        "market-research-report": "market-research",
        "market-viewpoint": "market-research",
        "market viewpoint": "market-research",
        "employer-record": "employer-internal",
        "employer": "employer-internal",
        "memoir": "memoir",
        "white-paper": "white-paper",
        "whitepaper": "white-paper",
        "executive white paper": "white-paper",
        "white paper": "white-paper",
        "dct": "dct",
        "product-profile": "profile-case",
        "vendor profile": "profile-case",
        "profile": "profile-case",
        "company-profile": "profile-case",
        "case-analysis": "profile-case",
        "case study": "case-study",
        "case-study": "case-study",
        "topic-analysis": "topic-viewpoint",
        "viewpoint": "topic-viewpoint",
        "technology-viewpoint": "topic-viewpoint",
        "technology viewpoint": "topic-viewpoint",
        "news-article": "press-news",
        "press-article": "press-news",
        "press-release": "press-news",
        "trade-press-article": "press-trade",
        "trade-press-feature": "press-trade",
        "trade-press-news-feature": "press-trade",
        "consulting-report": "consulting-advisory",
        "advisory-report": "consulting-advisory",
        "report": "report",
        "tech-topic": "tech-topic",
        "technology-impact-report": "tech-topic",
        "brief": "brief",
        "impact-brief": "brief",
        "vendor-study": "vendor-study",
        "benchmark": "vendor-study",
        "benchmark-report": "vendor-study",
        "presentation": "presentation",
        "webinar-presentation": "presentation",
        "conference-presentation": "presentation",
        "ai-response": "ai-response",
        "transcript": "transcript",
        "analyst-note": "analyst-note",
        "analyst-profile": "analyst-note",
        "expert-report": "analyst-note",
        "engineering-tech": "engineering-tech",
        "internal-engineering-document": "engineering-tech",
        "internal-engineering-memo": "engineering-tech",
        "vendor-marketing": "vendor-marketing",
        "vendor-marketing-brochure": "vendor-marketing",
        "marketing-material": "vendor-marketing",
        "product": "product",
        "product-viewpoint": "product",
    }
    return type_to_bucket.get(stype, "other")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--obs",        type=str, required=True)
    ap.add_argument("--studies",    type=str, required=True)
    ap.add_argument("--tier-a",     type=str, default=None,
                    help="Tier A sample CSV (for bucket reuse + obs_id exclusion)")
    ap.add_argument("--tier-b",     type=str, default=None,
                    help="Tier B results CSV (for obs_id exclusion)")
    ap.add_argument("--output",     type=str, required=True)
    ap.add_argument("--target-n",   type=int, default=100)
    ap.add_argument("--per-bucket", type=int, default=4)
    ap.add_argument("--seed",       type=int, default=20260615)
    ap.add_argument("--dry-run",    action="store_true",
                    help="Print bucket allocation, write nothing")
    args = ap.parse_args()

    rng = random.Random(args.seed)
    obs_rows = load_csv(Path(args.obs))
    studies = {r["study_id"]: r for r in load_csv(Path(args.studies))}
    print(f"[load] obs={len(obs_rows)} studies={len(studies)}")

    # Tier A bucket lookup (obs_id -> bucket)
    tier_a_bucket = {}
    if args.tier_a:
        for r in load_csv(Path(args.tier_a)):
            oid = r.get("obs_id"); b = r.get("_bucket")
            if oid and b:
                tier_a_bucket[oid] = b
        print(f"[load] tier_a buckets: {len(tier_a_bucket)}")

    # Exclude obs already scored in Tier A or Tier B
    exclude = load_obs_id_set(Path(args.tier_a) if args.tier_a else None) \
            | load_obs_id_set(Path(args.tier_b) if args.tier_b else None)
    print(f"[exclude] tier_a+tier_b obs_ids: {len(exclude)}")

    # Resolve anchor + filter to anchor ≤ 2020, build bucket index
    bucket_pool = defaultdict(list)
    n_no_anchor = 0
    n_too_recent = 0
    n_excluded = 0
    n_eligible = 0
    for obs in obs_rows:
        oid = obs.get("obs_id")
        if not oid or oid in exclude:
            n_excluded += 1
            continue
        study = studies.get(obs.get("study_id") or "", {})
        try:
            anchor = resolve_anchor_year(obs, study)
        except AnchorResolutionError:
            n_no_anchor += 1
            continue
        if anchor.year > ANCHOR_MAX:
            n_too_recent += 1
            continue
        b = derive_bucket(obs, study, tier_a_bucket)
        # Enrich row with metadata we need downstream
        enriched = dict(obs)
        enriched["_bucket"] = b
        enriched["_study_type"] = study.get("type") or ""
        enriched["_study_date"] = study.get("date") or ""
        enriched["_anchor_year"] = str(anchor.year)
        enriched["_anchor_source"] = anchor.source
        bucket_pool[b].append(enriched)
        n_eligible += 1

    print(f"[filter] eligible (anchor≤{ANCHOR_MAX}, not in Tier A/B): {n_eligible}")
    print(f"[filter] excluded by Tier A/B membership: {n_excluded}")
    print(f"[filter] dropped (anchor > {ANCHOR_MAX}):  {n_too_recent}")
    print(f"[filter] dropped (no anchor):              {n_no_anchor}")

    # Buckets ranked by pool size; show top
    bucket_sizes = {b: len(rows) for b, rows in bucket_pool.items()}
    print(f"[buckets] {len(bucket_sizes)} buckets with eligible obs")
    for b, n in sorted(bucket_sizes.items(), key=lambda x: -x[1]):
        print(f"  {n:6d}  {b}")

    # Stratified draw
    selected = []
    bucket_draws = {}
    for b, rows in bucket_pool.items():
        draw = rng.sample(rows, min(args.per_bucket, len(rows)))
        bucket_draws[b] = len(draw)
        selected.extend(draw)
    print(f"[draw] initial: {len(selected)} from {len(bucket_pool)} buckets")

    # Topup if under target — oversample largest buckets without replacement
    if len(selected) < args.target_n:
        deficit = args.target_n - len(selected)
        # Build a residual pool: every eligible obs not yet selected
        sel_ids = {r["obs_id"] for r in selected}
        residual = []
        for b in sorted(bucket_pool.keys(), key=lambda b: -bucket_sizes[b]):
            for r in bucket_pool[b]:
                if r["obs_id"] not in sel_ids:
                    residual.append(r)
        rng.shuffle(residual)
        topup = residual[:deficit]
        for r in topup:
            bucket_draws[r["_bucket"]] = bucket_draws.get(r["_bucket"], 0) + 1
        selected.extend(topup)
        print(f"[draw] topup: +{len(topup)} (deficit was {deficit})")

    # Trim to target if over
    if len(selected) > args.target_n:
        selected = selected[:args.target_n]
        print(f"[draw] trimmed to {args.target_n}")

    print(f"[draw] FINAL: {len(selected)} rows")
    print("[draw] per-bucket distribution:")
    final_dist = Counter(r["_bucket"] for r in selected)
    for b, n in sorted(final_dist.items(), key=lambda x: -x[1]):
        print(f"  {n:3d}  {b}")

    # Sanity invariants
    anchors = [int(r["_anchor_year"]) for r in selected]
    assert all(y <= ANCHOR_MAX for y in anchors), \
        f"INVARIANT FAIL: anchor > {ANCHOR_MAX} in selection"
    overlap = {r["obs_id"] for r in selected} & exclude
    assert not overlap, f"INVARIANT FAIL: {len(overlap)} obs overlap with Tier A/B"
    print(f"[ok] all anchors ≤ {ANCHOR_MAX}; 0 Tier A/B overlap")

    if args.dry_run:
        print("[dry-run] not writing output")
        return

    # Write output. Column order: master_obs cols + enrichment + placeholders.
    if not selected:
        print("[abort] no rows to write")
        return

    obs_cols = list(obs_rows[0].keys())  # match master order
    out_cols = obs_cols + ENRICHMENT_COLS + PLACEHOLDER_COLS

    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=out_cols, quoting=csv.QUOTE_ALL)
        w.writeheader()
        for r in selected:
            # Placeholders are intentionally blank — Pete or adjudicator fills later
            row = {k: r.get(k, "") for k in obs_cols + ENRICHMENT_COLS}
            for k in PLACEHOLDER_COLS:
                row[k] = ""
            w.writerow(row)
    print(f"[write] {out_path}  ({len(selected)} rows, {len(out_cols)} cols)")
    print(f"[done] seed={args.seed}  per_bucket={args.per_bucket}  "
          f"target_n={args.target_n}")


if __name__ == "__main__":
    main()
