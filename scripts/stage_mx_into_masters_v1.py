#!/usr/bin/env python3
"""
stage_mx_into_masters_v1.py
===========================

Stage the 50 model-extracted (`-mx`) PC Deals study packages into Pete Kastner's
LIVE Aberdeen archive masters, and create the Pass C scope directories so the new
observations get scored.

WHY THIS SCRIPT EXISTS
----------------------
The `expand-pc-deals` deliverable ends at validated 5-CSV packages + A:B compare.
Promotion into the pipeline (masters merge -> Pass C -> wiki) runs on Pete's Mac.
There was NO existing generic "append packages to masters" script -- `apply_passb_*`
only patches a hardcoded 5-row DECtp manifest. This script fills that gap for the
`-mx` batch, mapping each per-study package's schema onto the master schema.

The `-mx` study_ids are a PARALLEL set: every study_id carries the `-mx` suffix so
the new rows COEXIST with the legacy originals in the masters for live A:B querying.
Promotion (drop legacy, strip `-mx`) is a separate, later, Pete-approved step.

SCHEMA MAPPING (verified on the Mac 2026-06-27)
-----------------------------------------------
Per-study package -> live master, with these deltas:

  studies.csv      16 cols  ->  _master_studies.csv       16 cols   (identical; pass through)
  observations.csv 12 cols  ->  _master_observations.csv  17 cols   (add 5 cols, see below)
  entities.csv      9 cols  ->  _master_entities.csv        8 cols   (DROP study_id; dedup by entity_id)
  technologies.csv  9 cols  ->  _master_technologies.csv    8 cols   (DROP study_id; dedup by tech_id)

observations 12 -> 17 mapping:
  package cols : obs_id, study_id, entity_id, tech_id, observation_type, year_observed,
                 metric_name, metric_value, confidence, methodology_code, source_page, notes
  master  cols : obs_id, study_id, entity_id, tech_id, observation_type, year_observed,
                 metric_name, metric_value, confidence, verification_method, methodology_code,
                 source_page, notes, collection, thread_tag, section, legacy_obs_id
  Added columns and their values for these freshly model-extracted rows:
    verification_method = "ingest-extraction"   (claim sourced from the study text itself; archival-ingest 17.1)
    collection          = "dct"                 (all 50 are DCT PC-Deals studies; archival-ingest 13.6)
    thread_tag          = ""                     (no legacy thread tag)
    section             = ""                     (no section reference captured)
    legacy_obs_id       = ""                     (these IDs are already canonical {study_id}-OBS-NNN; no rewrite)

LIVE MASTER LOCATION (verified 2026-06-27)
------------------------------------------
  ~/Desktop/Archive/aberdeen-group-archive/_master_*.csv
NOTE: the old ~/Desktop/Archive/archive_masters/ was RETIRED to
  ~/Desktop/Archive/_retired_archive_masters_20260624T184237Z/ on 2026-06-24.
Do NOT write to the retired dir. This script targets the aberdeen-group-archive copy.

PASS C SCOPE (verified 2026-06-27)
----------------------------------
run_prescience_pass_c_v5.py scopes work by membership:
    prepared = set(os.listdir(~/Desktop/Archive/prepared))
    in_scope = [r for r in master_observations if r["study_id"] in prepared]
So this script creates one EMPTY directory per study at
  ~/Desktop/Archive/prepared/<study_id>/   (study_id already carries -mx)
That is the ONLY filesystem requirement for Pass C to pick up the new obs.

  *** OPERATOR FLAG (read before running Pass C) ***
  run_prescience_pass_c_v5.py line 63 sets  MASTERS = ARCH / "archive_masters"
  which now points at the RETIRED masters. Pass C will score the WRONG file
  (and will NOT see the -mx rows) until that constant is repointed to
  aberdeen-group-archive/. Fix v5 (bump to _v6) before scoring. This script
  does not touch v5; it only flags the issue.

STANDING INVARIANTS (Pete)
--------------------------
  - csv.QUOTE_ALL on every write (archival-ingest 16.2 Check 4)
  - timestamped backup of EACH touched master BEFORE any write
  - dry-run is default; --commit is opt-in
  - row counts reported before/after for every master
  - script is versioned _v1 (bump on every change; never overwrite)
  - FK integrity: every obs entity_id/tech_id resolves to a master row after merge

USAGE (on Pete's Mac)
---------------------
  # 1. dry-run (default) -- prints the full plan, writes nothing:
  python3 ~/Desktop/Archive/scripts/stage_mx_into_masters_v1.py

  # 2. point at the -mx packages if not at the default staging path:
  python3 ~/Desktop/Archive/scripts/stage_mx_into_masters_v1.py \
      --mx-root ~/Desktop/Archive/Perplexity_Only/expand_pc_deals_full

  # 3. commit (writes masters + creates prepared/ scope dirs):
  python3 ~/Desktop/Archive/scripts/stage_mx_into_masters_v1.py --commit

  # skip prepared/ creation (masters only):
  python3 ~/Desktop/Archive/scripts/stage_mx_into_masters_v1.py --commit --no-prepared

Author: agent, for Pete Kastner. Date: 2026-06-27.
"""

from __future__ import annotations

import argparse
import csv
import datetime
import os
import shutil
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Configuration -- paths verified on the Mac 2026-06-27
# ---------------------------------------------------------------------------

HOME = Path.home()
ARCHIVE = HOME / "Desktop" / "Archive"
MASTERS_DIR = ARCHIVE / "aberdeen-group-archive"          # LIVE masters (post 2026-06-24 move)
PREPARED_DIR = ARCHIVE / "prepared"                       # Pass C scope dir
DEFAULT_MX_ROOT = ARCHIVE / "Perplexity_Only" / "expand_pc_deals_full"

M_STUDIES = MASTERS_DIR / "_master_studies.csv"
M_OBS = MASTERS_DIR / "_master_observations.csv"
M_ENTITIES = MASTERS_DIR / "_master_entities.csv"
M_TECH = MASTERS_DIR / "_master_technologies.csv"

# Canonical master headers (verified 2026-06-27). The script asserts these match
# the live files before doing anything, so a silent schema drift can't corrupt a merge.
H_STUDIES = ["study_id", "title", "author", "date", "type", "subject_domain",
             "methodology", "source_file", "abstract", "license", "importance",
             "importance_rationale", "relevance", "relevance_rationale",
             "prescience", "prescience_rationale"]
H_OBS = ["obs_id", "study_id", "entity_id", "tech_id", "observation_type",
         "year_observed", "metric_name", "metric_value", "confidence",
         "verification_method", "methodology_code", "source_page", "notes",
         "collection", "thread_tag", "section", "legacy_obs_id"]
H_ENTITIES = ["entity_id", "entity_name", "entity_type", "sector", "status",
              "successor", "years_active", "notes"]
H_TECH = ["tech_id", "tech_name", "category", "vendor", "era",
          "lifecycle_at_study", "lifecycle_current", "notes"]

# Defaults injected when widening per-study obs (12) -> master obs (17)
OBS_DEFAULTS = {
    "verification_method": "ingest-extraction",
    "collection": "dct",
    "thread_tag": "",
    "section": "",
    "legacy_obs_id": "",
}

# Enum guards (archival-ingest 16.2 Check 3)
VALID_OBS_CONFIDENCE = {"high", "medium", "low", "verified", "[DEFERRED]",
                        "partially-verified", "refuted", "unknown [REVIEW]"}
VALID_PRESCIENCE = {"high", "medium", "low", "not-applicable", "[DEFERRED]"}
VALID_RATING = {"high", "medium", "low"}


def utc_stamp() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def read_csv(path: Path) -> tuple[list[str], list[dict]]:
    with open(path, newline="", encoding="utf-8") as f:
        rdr = csv.DictReader(f)
        rows = list(rdr)
        return list(rdr.fieldnames or []), rows


def write_csv_quote_all(path: Path, header: list[str], rows: list[dict]) -> None:
    """The ONLY permitted write path (QUOTE_ALL). Writes dict rows in header order."""
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, quoting=csv.QUOTE_ALL)
        w.writerow(header)
        for r in rows:
            w.writerow([r.get(c, "") for c in header])


def assert_header(path: Path, got: list[str], expected: list[str]) -> None:
    if got != expected:
        sys.exit(
            f"FATAL: header mismatch in {path.name}\n"
            f"  expected: {expected}\n"
            f"  got     : {got}\n"
            "Refusing to merge against an unexpected schema. "
            "If the master schema changed intentionally, bump this script to _v2."
        )


# ---------------------------------------------------------------------------
# Discover -mx packages
# ---------------------------------------------------------------------------

def discover_mx(mx_root: Path) -> list[Path]:
    if not mx_root.exists():
        sys.exit(f"FATAL: --mx-root does not exist: {mx_root}")
    dirs = sorted(
        d for d in mx_root.iterdir()
        if d.is_dir() and d.name.endswith("-mx") and (d / "data" / "studies.csv").exists()
    )
    if not dirs:
        sys.exit(f"FATAL: no '*-mx/data/studies.csv' packages found under {mx_root}")
    return dirs


def load_package(study_dir: Path) -> dict:
    """Read the 4 data CSVs for one -mx study. Returns dict of header+rows per table."""
    out = {}
    for name in ("studies", "entities", "technologies", "observations"):
        p = study_dir / "data" / f"{name}.csv"
        if not p.exists():
            sys.exit(f"FATAL: {study_dir.name} missing data/{name}.csv")
        hdr, rows = read_csv(p)
        out[name] = {"header": hdr, "rows": rows}
    return out


# ---------------------------------------------------------------------------
# Build the merged additions
# ---------------------------------------------------------------------------

def main() -> None:
    ap = argparse.ArgumentParser(description="Stage -mx packages into the live masters + Pass C scope.")
    ap.add_argument("--mx-root", type=Path, default=DEFAULT_MX_ROOT,
                    help=f"Directory of *-mx/ packages (default: {DEFAULT_MX_ROOT})")
    ap.add_argument("--commit", action="store_true", help="Write changes (default: dry-run).")
    ap.add_argument("--no-prepared", action="store_true",
                    help="Do NOT create prepared/<study_id>/ scope dirs.")
    args = ap.parse_args()

    commit = args.commit
    print(f"Mode:        {'COMMIT' if commit else 'DRY-RUN'}")
    print(f"Masters dir: {MASTERS_DIR}")
    print(f"-mx root:    {args.mx_root}")
    print()

    for p in (M_STUDIES, M_OBS, M_ENTITIES, M_TECH):
        if not p.exists():
            sys.exit(f"FATAL: master not found: {p}")

    # Load + validate live master headers
    sh, studies_rows = read_csv(M_STUDIES); assert_header(M_STUDIES, sh, H_STUDIES)
    oh, obs_rows = read_csv(M_OBS);        assert_header(M_OBS, oh, H_OBS)
    eh, ent_rows = read_csv(M_ENTITIES);   assert_header(M_ENTITIES, eh, H_ENTITIES)
    th, tech_rows = read_csv(M_TECH);      assert_header(M_TECH, th, H_TECH)

    print("Live master row counts (before):")
    print(f"  studies:      {len(studies_rows)}")
    print(f"  observations: {len(obs_rows)}")
    print(f"  entities:     {len(ent_rows)}")
    print(f"  technologies: {len(tech_rows)}")
    print()

    existing_study_ids = {r["study_id"] for r in studies_rows}
    existing_obs_ids = {r["obs_id"] for r in obs_rows}
    existing_entity_ids = {r["entity_id"] for r in ent_rows}
    existing_tech_ids = {r["tech_id"] for r in tech_rows}

    pkgs = discover_mx(args.mx_root)
    print(f"Discovered {len(pkgs)} -mx packages.\n")

    # Accumulators for additions
    add_studies: list[dict] = []
    add_obs: list[dict] = []
    add_entities: dict[str, dict] = {}   # entity_id -> row (dedup, first wins)
    add_tech: dict[str, dict] = {}        # tech_id  -> row (dedup, first wins)

    errors: list[str] = []
    per_study_counts: list[tuple[str, int, int, int]] = []  # (sid, n_obs, n_ent, n_tech)
    scope_dirs: list[str] = []

    for pkg_dir in pkgs:
        pk = load_package(pkg_dir)
        srow = pk["studies"]["rows"][0]
        sid = srow["study_id"]
        scope_dirs.append(sid)

        # --- studies (16 -> 16, pass through) ---
        if sid in existing_study_ids:
            errors.append(f"{sid}: study_id already present in _master_studies.csv (skipping study row)")
        else:
            # enum guards
            if srow.get("license") != "CC-BY-4.0":
                errors.append(f"{sid}: license != CC-BY-4.0 ({srow.get('license')!r})")
            for col, valid in (("importance", VALID_RATING), ("relevance", VALID_RATING),
                               ("prescience", VALID_PRESCIENCE)):
                if srow.get(col) not in valid:
                    errors.append(f"{sid}: invalid {col}={srow.get(col)!r}")
            add_studies.append({c: srow.get(c, "") for c in H_STUDIES})

        # --- entities (9 -> 8: drop study_id, dedup by entity_id) ---
        local_entity_ids = set()
        for er in pk["entities"]["rows"]:
            eid = er["entity_id"]
            local_entity_ids.add(eid)
            if eid in existing_entity_ids or eid in add_entities:
                continue  # already known; reuse canonical row
            add_entities[eid] = {c: er.get(c, "") for c in H_ENTITIES}

        # --- technologies (9 -> 8: drop study_id, dedup by tech_id) ---
        local_tech_ids = set()
        for tr in pk["technologies"]["rows"]:
            tid = tr["tech_id"]
            local_tech_ids.add(tid)
            if tid in existing_tech_ids or tid in add_tech:
                continue
            add_tech[tid] = {c: tr.get(c, "") for c in H_TECH}

        # known id universe for FK checks (master + all additions so far + this study's locals)
        known_entities = existing_entity_ids | set(add_entities) | local_entity_ids
        known_tech = existing_tech_ids | set(add_tech) | local_tech_ids

        # --- observations (12 -> 17: widen + defaults) ---
        n_obs = 0
        for orow in pk["observations"]["rows"]:
            oid = orow["obs_id"]
            if oid in existing_obs_ids or oid in {r["obs_id"] for r in add_obs}:
                errors.append(f"{sid}: duplicate obs_id {oid}")
                continue
            # FK integrity
            ent = orow.get("entity_id", "").strip()
            tech = orow.get("tech_id", "").strip()
            if ent and ent not in known_entities:
                errors.append(f"{sid}: obs {oid} entity_id {ent!r} not in entities table")
            if tech and tech not in known_tech:
                errors.append(f"{sid}: obs {oid} tech_id {tech!r} not in technologies table")
            # confidence enum
            if orow.get("confidence") not in VALID_OBS_CONFIDENCE:
                errors.append(f"{sid}: obs {oid} invalid confidence={orow.get('confidence')!r}")
            # widen
            new = {c: orow.get(c, "") for c in H_OBS if c in orow}
            new.update(OBS_DEFAULTS)
            # re-copy the 12 source cols (defaults must not clobber real values that share a name)
            for c in ("obs_id", "study_id", "entity_id", "tech_id", "observation_type",
                      "year_observed", "metric_name", "metric_value", "confidence",
                      "methodology_code", "source_page", "notes"):
                new[c] = orow.get(c, "")
            add_obs.append({c: new.get(c, "") for c in H_OBS})
            n_obs += 1

        per_study_counts.append((sid, n_obs, len(local_entity_ids), len(local_tech_ids)))

    # ---- Report ----
    print("Per-study additions (obs / new-entities-seen / new-tech-seen):")
    for sid, no, ne, nt in per_study_counts:
        print(f"  {sid:<46} obs={no:<4} ent={ne:<3} tech={nt}")
    print()
    print("Totals to ADD:")
    print(f"  studies:      +{len(add_studies)}")
    print(f"  observations: +{len(add_obs)}")
    print(f"  entities:     +{len(add_entities)}  (deduped against master + within batch)")
    print(f"  technologies: +{len(add_tech)}  (deduped against master + within batch)")
    print()

    if errors:
        print(f"VALIDATION ERRORS ({len(errors)}) -- nothing will be written:")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)
    print("Validation: PASS (column maps, enums, FK integrity, obs_id uniqueness).")
    print()

    # ---- Compose final tables ----
    final_studies = studies_rows + add_studies
    final_obs = obs_rows + add_obs
    final_entities = ent_rows + list(add_entities.values())
    final_tech = tech_rows + list(add_tech.values())

    print("Live master row counts (after):")
    print(f"  studies:      {len(studies_rows)} -> {len(final_studies)}  (+{len(add_studies)})")
    print(f"  observations: {len(obs_rows)} -> {len(final_obs)}  (+{len(add_obs)})")
    print(f"  entities:     {len(ent_rows)} -> {len(final_entities)}  (+{len(add_entities)})")
    print(f"  technologies: {len(tech_rows)} -> {len(final_tech)}  (+{len(add_tech)})")
    print()

    if not commit:
        print("DRY-RUN only -- pass --commit to write masters and create prepared/ scope dirs.")
        if not args.no_prepared:
            print(f"Would create {len(scope_dirs)} prepared/ scope dirs under {PREPARED_DIR}")
        return

    # ---- Backup every touched master BEFORE writing ----
    stamp = utc_stamp()
    backup_dir = MASTERS_DIR / f"_master_csvs_pre_mx_stage_{stamp}"
    backup_dir.mkdir(parents=True, exist_ok=True)
    for src in (M_STUDIES, M_OBS, M_ENTITIES, M_TECH):
        shutil.copy2(src, backup_dir / src.name)
    print(f"Backup written: {backup_dir}")

    # ---- Write masters (QUOTE_ALL) ----
    write_csv_quote_all(M_STUDIES, H_STUDIES, final_studies)
    write_csv_quote_all(M_OBS, H_OBS, final_obs)
    write_csv_quote_all(M_ENTITIES, H_ENTITIES, final_entities)
    write_csv_quote_all(M_TECH, H_TECH, final_tech)
    print("Masters written.")

    # ---- Read-back parity assertion ----
    _, rb_studies = read_csv(M_STUDIES)
    _, rb_obs = read_csv(M_OBS)
    _, rb_ent = read_csv(M_ENTITIES)
    _, rb_tech = read_csv(M_TECH)
    assert len(rb_studies) == len(final_studies), "studies read-back parity FAILED"
    assert len(rb_obs) == len(final_obs), "observations read-back parity FAILED"
    assert len(rb_ent) == len(final_entities), "entities read-back parity FAILED"
    assert len(rb_tech) == len(final_tech), "technologies read-back parity FAILED"
    print("Read-back parity: PASS.")

    # ---- Create Pass C scope dirs ----
    if not args.no_prepared:
        made = 0
        for sid in scope_dirs:
            d = PREPARED_DIR / sid
            if not d.exists():
                d.mkdir(parents=True, exist_ok=True)
                made += 1
        print(f"prepared/ scope dirs: created {made} new (of {len(scope_dirs)}) under {PREPARED_DIR}")
    else:
        print("prepared/ scope dirs: SKIPPED (--no-prepared).")

    print()
    print("DONE. Next: fix run_prescience_pass_c_v5.py MASTERS path (see OPERATOR FLAG in this script's docstring),")
    print("then run Pass C, roll-up, Phase 1/2 rebuild, release gate, Phase 3-6 wiki. All on the Mac.")


if __name__ == "__main__":
    main()
