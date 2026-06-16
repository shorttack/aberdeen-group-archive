#!/usr/bin/env python3
"""
count_eligible_le_2015_v1.py — one-shot inventory of SH-sweep eligible obs.

Walks _master_observations.csv, excludes Tier A + Tier B manifests, resolves
each obs anchor year via anchor_year_resolver_v2 (obs.year_observed first,
study.date fallback), and prints eligibility counts at three cutoffs:
  - anchor <= 2020  (matches calibration sample filter)
  - anchor <= 2018
  - anchor <= 2015  (TARGET for full short-horizon sweep)

Usage (run from aberdeen-group-archive repo root):
  python3 scripts/count_eligible_le_2015_v1.py
"""
import csv
import sys
from pathlib import Path

# Resolver lives at scripts/anchor_year_resolver_v2.py — same dir as this script
SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))
from anchor_year_resolver_v2 import resolve_anchor_year, AnchorResolutionError  # noqa: E402

REPO_ROOT = Path.cwd()
OBS_CSV = REPO_ROOT / "_master_observations.csv"
STUDIES_CSV = REPO_ROOT / "_master_studies.csv"
TIER_A = REPO_ROOT / "Perplexity_Only" / "prescience_tier_a_sample_v1.csv"
TIER_B = REPO_ROOT / "Perplexity_Only" / "prescience_tier_b_sample_v1.csv"


def load_obs_ids(path: Path) -> set:
    if not path.exists():
        return set()
    ids = set()
    with open(path, newline="") as f:
        for r in csv.DictReader(f):
            oid = r.get("obs_id")
            if oid:
                ids.add(oid)
    return ids


def main() -> int:
    if not OBS_CSV.exists():
        print(f"[err] missing {OBS_CSV}", file=sys.stderr)
        return 2
    if not STUDIES_CSV.exists():
        print(f"[err] missing {STUDIES_CSV}", file=sys.stderr)
        return 2

    tier_a = load_obs_ids(TIER_A)
    tier_b = load_obs_ids(TIER_B)
    print(f"[tier_a] {len(tier_a)} obs_ids ({'present' if tier_a else 'EMPTY/MISSING'})")
    print(f"[tier_b] {len(tier_b)} obs_ids ({'present' if tier_b else 'EMPTY/MISSING'})")

    studies = {}
    with open(STUDIES_CSV, newline="") as f:
        for r in csv.DictReader(f):
            studies[r["study_id"]] = r
    print(f"[studies] {len(studies)} entries")

    total = 0
    excluded_tier = 0
    no_anchor = 0
    anchor_too_late = 0
    elig_2020 = 0
    elig_2018 = 0
    elig_2015 = 0
    anchor_source_counts = {"obs": 0, "study": 0}

    with open(OBS_CSV, newline="") as f:
        for r in csv.DictReader(f):
            total += 1
            oid = r.get("obs_id") or ""
            if oid in tier_a or oid in tier_b:
                excluded_tier += 1
                continue
            sid = r.get("study_id") or ""
            try:
                a = resolve_anchor_year(r, studies.get(sid, {}))
            except AnchorResolutionError:
                no_anchor += 1
                continue
            if a.year > 2020:
                anchor_too_late += 1
                continue
            elig_2020 += 1
            anchor_source_counts[a.source] = anchor_source_counts.get(a.source, 0) + 1
            if a.year <= 2018:
                elig_2018 += 1
            if a.year <= 2015:
                elig_2015 += 1

    print()
    print(f"[total obs]              {total}")
    print(f"[excluded Tier A/B]      {excluded_tier}")
    print(f"[no anchor]              {no_anchor}")
    print(f"[dropped anchor>2020]    {anchor_too_late}")
    print(f"[eligible anchor<=2020]  {elig_2020}")
    print(f"[eligible anchor<=2018]  {elig_2018}")
    print(f"[eligible anchor<=2015]  {elig_2015}   <-- TARGET")
    print()
    print(f"[anchor source within <=2020 eligible pool]")
    for k, v in sorted(anchor_source_counts.items()):
        pct = (100 * v / elig_2020) if elig_2020 else 0
        print(f"    {k:>5}: {v:5d}  ({pct:5.1f}%)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
