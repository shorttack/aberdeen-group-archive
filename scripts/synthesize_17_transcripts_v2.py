#!/usr/bin/env python3
"""
synthesize_17_transcripts_v2.py

v2 adds Plaza Hotel DECtp Press Conference to the scope (17 transcripts + 1 = 18).
Both DECtp studies are marked pass_c_eligible.

CHANGE FROM v1:
- EXTRA_STUDY_IDS now contains 1 study (Plaza Hotel) that isn't in the manifest
  but needs the same Frictionless package + Pass C treatment.
- Renamed "17" semantics internally to "manifest+extras" but kept v2 filename
  for traceability to v1.

Per-study output and behavior identical to v1: prepared/<id>/data/*.csv + source/ + manifest.json.
csv.QUOTE_ALL per archival-ingest v20 §16. Idempotent.

Usage:
  python3 synthesize_17_transcripts_v2.py --dry-run
  python3 synthesize_17_transcripts_v2.py --apply
"""

import argparse
import csv
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ARCHIVE = Path.home() / "Desktop" / "Archive"
MASTERS = ARCHIVE / "archive_masters"
PREPARED = ARCHIVE / "prepared"
MANIFEST = ARCHIVE / "scripts" / "transcript_manifest_v1_FOR_MAC.csv"

# Studies not in the manifest but still in scope for this run
EXTRA_STUDY_IDS = [
    "dectp-press-conference-transcript-and-benchmark-charts-plaza-5e5836",
]

PASS_C_ELIGIBLE = {
    "dectp-press-conference-transcript-and-benchmark-charts-plaza-5e5836",
    "dec-blue-monday-internal-sales-training-dectp-vs-ibm-0021cc",
}


def load_manifest_ids():
    with MANIFEST.open(newline="", encoding="utf-8") as f:
        rdr = csv.DictReader(f)
        return [row["study_id"].strip() for row in rdr if row.get("study_id", "").strip()]


def load_master(path, key="study_id"):
    if not path.exists():
        print(f"  WARN: master not found: {path}")
        return {}
    out = {}
    with path.open(newline="", encoding="utf-8") as f:
        rdr = csv.DictReader(f)
        for row in rdr:
            sid = row.get(key, "").strip()
            if sid:
                out.setdefault(sid, []).append(row)
    return out


def write_csv(path, rows, fieldnames):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in fieldnames})


def synthesize_one(sid, studies_map, obs_map, ent_map, tech_map, apply_):
    target = PREPARED / sid
    studies_csv = target / "data" / "_studies.csv"

    if studies_csv.exists():
        return ("SKIP_EXISTS", 0)

    study_rows = studies_map.get(sid, [])
    if not study_rows:
        return ("MISSING_FROM_MASTER", 0)

    obs_rows = obs_map.get(sid, [])
    ent_rows = ent_map.get(sid, [])
    tech_rows = tech_map.get(sid, [])

    if not apply_:
        return ("WOULD_CREATE", len(obs_rows))

    study_fields = list(study_rows[0].keys())
    obs_fields = list(obs_rows[0].keys()) if obs_rows else ["obs_id", "study_id"]
    ent_fields = list(ent_rows[0].keys()) if ent_rows else ["entity_id", "study_id"]
    tech_fields = list(tech_rows[0].keys()) if tech_rows else ["tech_id", "study_id"]

    write_csv(target / "data" / "_studies.csv", study_rows, study_fields)
    write_csv(target / "data" / "_observations.csv", obs_rows, obs_fields)
    write_csv(target / "data" / "_entities.csv", ent_rows, ent_fields)
    write_csv(target / "data" / "_technologies.csv", tech_rows, tech_fields)
    write_csv(target / "data" / "_codes.csv", [], ["code_id", "study_id", "label"])

    src_dir = target / "source"
    src_dir.mkdir(parents=True, exist_ok=True)
    parts = []
    abstract = study_rows[0].get("abstract", "").strip()
    if abstract:
        parts.append(f"# Abstract\n\n{abstract}")
    if obs_rows:
        parts.append("# Observations\n")
        for o in obs_rows:
            txt = o.get("observation_text", "") or o.get("text", "") or ""
            section = o.get("section", "")
            year = o.get("year_observed", "")
            parts.append(f"## [{section} / {year}]\n{txt}\n")
    (src_dir / "_raw_text.txt").write_text("\n\n".join(parts), encoding="utf-8")

    manifest = {
        "study_id": sid,
        "title": study_rows[0].get("title", ""),
        "date": study_rows[0].get("date", ""),
        "type": study_rows[0].get("type", ""),
        "synthesized_at": datetime.now(timezone.utc).isoformat(),
        "synthesized_by": "synthesize_17_transcripts_v2.py",
        "synthesis_method": "from_masters",
        "pass_c_eligible": sid in PASS_C_ELIGIBLE,
        "pass_c_skip_reason": None if sid in PASS_C_ELIGIBLE else "in-thread Pass B prescience preserved per Pete 2026-06-13",
        "obs_count": len(obs_rows),
        "entity_count": len(ent_rows),
        "tech_count": len(tech_rows),
    }
    (target / "manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")

    return ("CREATED", len(obs_rows))


def main():
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--dry-run", action="store_true")
    g.add_argument("--apply", action="store_true")
    args = ap.parse_args()

    apply_ = args.apply

    print(f"=== synthesize_17_transcripts_v2.py ({'APPLY' if apply_ else 'DRY-RUN'}) ===")
    print(f"manifest: {MANIFEST}")
    print(f"extras  : {len(EXTRA_STUDY_IDS)} (Plaza Hotel DECtp)")

    ids = load_manifest_ids()
    ids_all = ids + [sid for sid in EXTRA_STUDY_IDS if sid not in ids]
    print(f"total study_ids in scope: {len(ids_all)} ({len(ids)} manifest + {len(ids_all) - len(ids)} extras)")

    studies_map = load_master(MASTERS / "_master_studies.csv")
    obs_map = load_master(MASTERS / "_master_observations.csv")
    ent_map = load_master(MASTERS / "_master_entities.csv")
    tech_map = load_master(MASTERS / "_master_technologies.csv")

    counts = {"CREATED": 0, "SKIP_EXISTS": 0, "MISSING_FROM_MASTER": 0, "WOULD_CREATE": 0}
    obs_total = 0
    eligible_obs = 0

    for sid in ids_all:
        status, n_obs = synthesize_one(sid, studies_map, obs_map, ent_map, tech_map, apply_)
        counts[status] += 1
        obs_total += n_obs
        if sid in PASS_C_ELIGIBLE:
            eligible_obs += n_obs
        flag = " [PASS_C]" if sid in PASS_C_ELIGIBLE else ""
        extra = " [EXTRA]" if sid in EXTRA_STUDY_IDS else ""
        print(f"  [{status:18s}] {sid}  obs={n_obs}{flag}{extra}")

    print()
    print("=== SUMMARY ===")
    for k, v in counts.items():
        if v:
            print(f"  {k}: {v}")
    print(f"  total observations across all in scope: {obs_total}")
    print(f"  observations in Pass C scope (2 studies): {eligible_obs}")
    if not apply_:
        print()
        print("Re-run with --apply to create dirs.")


if __name__ == "__main__":
    sys.exit(main() or 0)
