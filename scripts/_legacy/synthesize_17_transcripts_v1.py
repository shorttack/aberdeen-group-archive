#!/usr/bin/env python3
"""
synthesize_17_transcripts_v1.py

Narrow-scope synthesizer: creates prepared/<study_id>/ Frictionless Data Packages
for the 17 transcripts ingested 2026-06-12, plus DECtp Plaza Hotel if also missing.

Scope is gated by scripts/transcript_manifest_v1_FOR_MAC.csv — NOT the 960-study gap.

Per study, writes:
  prepared/<study_id>/
    data/_studies.csv         (1 row from _master_studies.csv)
    data/_observations.csv    (N rows from _master_observations.csv)
    data/_entities.csv        (M rows from _master_entities.csv)
    data/_technologies.csv    (K rows from _master_technologies.csv)
    data/_codes.csv           (empty; archival-ingest v20 §6 contract)
    source/_raw_text.txt      (abstract + obs text concatenated, since real source not relocatable)
    manifest.json             (with pass_c_eligible flag)

manifest.json pass_c_eligible logic:
  - dectp-press-conference-transcript-and-benchmark-charts-plaza-5e5836 → TRUE
  - dec-blue-monday-internal-sales-training-dectp-vs-ibm-0021cc         → TRUE
  - all 15 others                                                       → FALSE

Read-only on masters; only writes under prepared/.
Idempotent — skips study_ids whose prepared/<id>/data/_studies.csv already exists.

Usage:
  python3 synthesize_17_transcripts_v1.py --dry-run   # show what would happen
  python3 synthesize_17_transcripts_v1.py --apply     # actually create dirs
"""

import argparse
import csv
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

ARCHIVE = Path.home() / "Desktop" / "Archive"
MASTERS = ARCHIVE / "archive_masters"
PREPARED = ARCHIVE / "prepared"
MANIFEST = ARCHIVE / "scripts" / "transcript_manifest_v1_FOR_MAC.csv"

PASS_C_ELIGIBLE = {
    "dectp-press-conference-transcript-and-benchmark-charts-plaza-5e5836",
    "dec-blue-monday-internal-sales-training-dectp-vs-ibm-0021cc",
}


def load_manifest_ids():
    with MANIFEST.open(newline="", encoding="utf-8") as f:
        rdr = csv.DictReader(f)
        return [row["study_id"].strip() for row in rdr if row.get("study_id", "").strip()]


def load_master(path, key="study_id"):
    """Return dict: study_id -> list of rows (entities/obs/tech are 1:N)."""
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
    """csv.QUOTE_ALL per archival-ingest v20 §16."""
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

    # Field orders from canonical masters (read first row keys)
    study_fields = list(study_rows[0].keys())
    obs_fields = list(obs_rows[0].keys()) if obs_rows else ["obs_id", "study_id"]
    ent_fields = list(ent_rows[0].keys()) if ent_rows else ["entity_id", "study_id"]
    tech_fields = list(tech_rows[0].keys()) if tech_rows else ["tech_id", "study_id"]

    write_csv(target / "data" / "_studies.csv", study_rows, study_fields)
    write_csv(target / "data" / "_observations.csv", obs_rows, obs_fields)
    write_csv(target / "data" / "_entities.csv", ent_rows, ent_fields)
    write_csv(target / "data" / "_technologies.csv", tech_rows, tech_fields)
    write_csv(target / "data" / "_codes.csv", [], ["code_id", "study_id", "label"])

    # source/_raw_text.txt — synthesize from abstract + obs.observation_text
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

    # manifest.json
    manifest = {
        "study_id": sid,
        "title": study_rows[0].get("title", ""),
        "date": study_rows[0].get("date", ""),
        "type": study_rows[0].get("type", ""),
        "synthesized_at": datetime.now(timezone.utc).isoformat(),
        "synthesized_by": "synthesize_17_transcripts_v1.py",
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

    print(f"=== synthesize_17_transcripts_v1.py ({'APPLY' if apply_ else 'DRY-RUN'}) ===")
    print(f"manifest: {MANIFEST}")

    ids = load_manifest_ids()
    print(f"manifest study_ids: {len(ids)}")

    studies_map = load_master(MASTERS / "_master_studies.csv")
    obs_map = load_master(MASTERS / "_master_observations.csv")
    ent_map = load_master(MASTERS / "_master_entities.csv")
    tech_map = load_master(MASTERS / "_master_technologies.csv")

    counts = {"CREATED": 0, "SKIP_EXISTS": 0, "MISSING_FROM_MASTER": 0, "WOULD_CREATE": 0}
    obs_total = 0
    eligible_obs = 0

    for sid in ids:
        status, n_obs = synthesize_one(sid, studies_map, obs_map, ent_map, tech_map, apply_)
        counts[status] += 1
        obs_total += n_obs
        if sid in PASS_C_ELIGIBLE:
            eligible_obs += n_obs
        flag = " [PASS_C]" if sid in PASS_C_ELIGIBLE else ""
        print(f"  [{status:18s}] {sid}  obs={n_obs}{flag}")

    print()
    print("=== SUMMARY ===")
    for k, v in counts.items():
        if v:
            print(f"  {k}: {v}")
    print(f"  total observations across 17: {obs_total}")
    print(f"  observations in Pass C scope (2 studies): {eligible_obs}")
    if not apply_:
        print()
        print("Re-run with --apply to create dirs.")


if __name__ == "__main__":
    sys.exit(main() or 0)
