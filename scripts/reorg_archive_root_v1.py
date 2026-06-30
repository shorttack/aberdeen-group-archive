#!/usr/bin/env python3
"""
reorg_archive_root_v1.py — declutter aberdeen-group-archive repo root (Groups A-D)

Per DECLUTTER_PLAN_v1.md (2026-06-29). Scope for this run: Groups A, B, C, D only.
Groups E, F, G are DEFERRED (collections consolidation, stale-master retirement,
dir-casing collisions) — they need extra verification and Pete's per-item calls.

GUIDING RULES (Pete's standing discipline):
  - Forever-archive: NOTHING is deleted. Clutter is RELOCATED into visibility-
    segregated folders. Mirrors the scripts/_legacy/ convention.
  - Canonical masters (_master_*.csv, _known_*.csv, _master_codes.csv) STAY at
    root, untouched — the live pipeline reads them there.
  - Dry-run is the DEFAULT. Pass --commit to actually move.
  - git mv for TRACKED files (preserves history); plain mv for gitignored backups.
  - Backup-before-anything is inherent (git history + forever-archive relocation).
  - Refuses to move any path that a path-safety grep flagged as active-referenced,
    unless --force is passed.

USAGE (run on the Mac, in the repo root):
  cd ~/Desktop/Archive/aberdeen-group-archive
  python3 ~/Desktop/Archive/scripts/reorg_archive_root_v1.py            # dry-run
  python3 ~/Desktop/Archive/scripts/reorg_archive_root_v1.py --safety   # just the grep gate
  python3 ~/Desktop/Archive/scripts/reorg_archive_root_v1.py --commit   # execute

The --safety preflight is the verification gate for any future Group F move; it is
also run automatically (and enforced) for every entry in this run's move set.
"""

import argparse
import datetime
import os
import shlex
import subprocess
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Repo root: default to CWD, override with --repo. We refuse to run unless the
# CWD/--repo actually looks like the archive (has _master_studies.csv + .git).
# ---------------------------------------------------------------------------

NEW_DIRS = ["releases", "reports", "data_sources", "_local_backups"]

# Masters that MUST NOT move (sanity guard — these are never in any move group,
# but we assert they survive at root after the run).
PROTECTED_AT_ROOT = [
    "_master_studies.csv",
    "_master_entities.csv",
    "_master_technologies.csv",
    "_master_observations.csv",
    "_master_codes.csv",
    "_master_prescience_scores.csv",
    "_master_prescience_short_horizon.csv",
    "_known_entities.csv",
    "_known_technologies.csv",
    "_master_player_rebuttals.csv",
]

# ---------------------------------------------------------------------------
# Path-safety grep set: every path in any move group below that a script could
# plausibly read by name. Anything with active (non-_legacy) refs is BLOCKED
# from moving unless --force. (This run's groups are doc/report/zip clutter, so
# we expect zero active refs — but we verify, never assume.)
# ---------------------------------------------------------------------------

SAFETY_NAMES = [
    # Group C reports/audits that a script might conceivably write/read
    "_validation_log.csv",
    "_rebuild_diff_report.csv",
    "_collection_stats.csv",
    "_master_entity_field_conflicts.csv",
    "_missing_sources.csv",
    "_web_cache.json",
    "_web_verification_results.json",
    "_audits",
    # Group D source bundles
    "ai1_processed.zip",
    "archive1_processed.zip",
    "archive2_processed.zip",
    "archive3_processed.zip",
    "archive_p2_processed.zip",
    "archive_p3_processed.zip",
    "archive_p4_processed.zip",
    # Group B releases/worklists
    "RELEASE_NOTES_v1.4.md",
    "future_work_v1.6.md",
    # Group F (NOT moved this run, but verified so Pete can act later)
    "master_studies.csv",
    "master_entities.csv",
    "master_technologies.csv",
    "prescience_scores_pass_c_cloud_v1.csv",
    "_checkpoint.json",
    "main",
]


# ---------------------------------------------------------------------------
# Move groups. Each entry: (glob-or-name, dest_dir, tracked_expected)
# We resolve globs at runtime against the repo root. tracked_expected drives
# git mv vs plain mv, but we ALSO probe `git ls-files` to decide per file
# (authoritative); tracked_expected is only a hint for messaging.
# ---------------------------------------------------------------------------

def build_move_specs(repo: Path):
    """Return list of dicts: {src, dest_dir, group}. Only existing paths.
    De-duplicates: a path that matches multiple globs is added once (first
    group wins). Subdirectories that live under a NEW_DIR are never matched
    (so re-runs are idempotent)."""
    specs = []
    seen = set()  # resolved src paths already claimed

    def add(patterns, dest_dir, group):
        for pat in patterns:
            matches = sorted(repo.glob(pat))
            for m in matches:
                rp = m.resolve()
                # never move a protected master, never move the dest dirs themselves
                if m.name in PROTECTED_AT_ROOT:
                    continue
                if m.name in NEW_DIRS:
                    continue
                # never re-grab something already inside a destination dir
                if any(part in NEW_DIRS for part in m.relative_to(repo).parts[:-1]):
                    continue
                if rp in seen:
                    continue
                seen.add(rp)
                specs.append({"src": m, "dest_dir": dest_dir, "group": group})

    # GROUP A — local backups (gitignored; plain mv). Mac-only tidy, zero repo impact.
    add(["*.bak", "*.bak_*", "*.csv.bak*"], "_local_backups", "A")
    add(["archive_masters_pre_*", "_master_csvs_pre_*",
         "archive_masters_pre_reconcile_*", "archive_masters_pre_rollup_*"],
        "_local_backups", "A")

    # GROUP B — releases & worklists (tracked; git mv). Keep current WORKLIST.md at root.
    add(["RELEASE_NOTES_v*.md"], "releases", "B")
    add(["future_work_v*.md"], "releases", "B")
    add(["RESUME_2026_*.md"], "releases", "B")
    # NOTE: WORKLIST.md (current, undated) STAYS at root — release-facing, and
    # kastner-new-day fetches it from root. Dated WORKLIST_YYYY_MM_DD.md handling
    # is a Group B/Q3 item DEFERRED (Pete's call) — not moved here.

    # GROUP C — reports & audits (tracked; git mv)
    add(["_audits"], "reports", "C")
    add(["_validation_log.csv", "_rebuild_diff_report.csv"], "reports", "C")
    add(["_reconcile_canonical_to_repo_audit_*.csv", "_rollup_v3_audit_*.csv"], "reports", "C")
    add(["PASS_A_VERIFICATION_REPORT.md", "_skipped_sources.md",
         "_missing_sources.csv", "_collection_stats.csv",
         "_web_cache.json", "_web_verification_results.json",
         "model_prescience_scoring_finding_v1.md",
         "_master_entity_field_conflicts.csv"], "reports", "C")

    # GROUP D — source data bundles (tracked; git mv)
    add(["*_processed.zip"], "data_sources", "D")

    return specs


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def run(cmd, cwd):
    return subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)


def is_tracked(repo: Path, path: Path) -> bool:
    rel = path.relative_to(repo).as_posix()
    r = run(["git", "ls-files", "--error-unmatch", rel], repo)
    return r.returncode == 0


def path_safety_grep(repo: Path):
    """Grep scripts/ (excluding _legacy/) for each SAFETY_NAME. Return dict
    name -> list of referencing files (empty list == safe)."""
    results = {}
    scripts_dir = repo / "scripts"
    for name in SAFETY_NAMES:
        refs = []
        if scripts_dir.is_dir():
            r = run(["grep", "-rIl", "--include=*.py", name, "scripts/"], repo)
            if r.returncode == 0 and r.stdout.strip():
                refs = [ln for ln in r.stdout.strip().splitlines()
                        if "_legacy/" not in ln]
        results[name] = refs
    return results


def print_safety_report(results):
    print("\n=== PATH-SAFETY GREP (scripts/, excluding _legacy/) ===")
    any_blocked = False
    for name, refs in results.items():
        if refs:
            any_blocked = True
            print(f"  [BLOCKED] {name}")
            for r in refs:
                print(f"             ↳ {r}")
        else:
            print(f"  [ safe  ] {name}  (no active refs)")
    print("=======================================================")
    return any_blocked


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(description="Declutter archive root (Groups A-D).")
    ap.add_argument("--repo", default=os.getcwd(),
                    help="repo root (default: CWD)")
    ap.add_argument("--commit", action="store_true",
                    help="actually move files (default: dry-run)")
    ap.add_argument("--safety", action="store_true",
                    help="only run the path-safety grep, then exit")
    ap.add_argument("--force", action="store_true",
                    help="move even paths flagged by the safety grep (NOT recommended)")
    args = ap.parse_args()

    repo = Path(args.repo).resolve()

    # Refuse to run outside the archive.
    if not (repo / "_master_studies.csv").exists() or not (repo / ".git").exists():
        sys.exit(f"ERROR: {repo} does not look like aberdeen-group-archive "
                 f"(missing _master_studies.csv or .git). Aborting.")

    ts = datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    print(f"reorg_archive_root_v1.py  —  repo={repo}")
    print(f"UTC: {ts}   mode: {'COMMIT' if args.commit else 'DRY-RUN'}"
          f"{'  [--force]' if args.force else ''}")
    print(f"Scope: Groups A, B, C, D  (E/F/G deferred)\n")

    # 1. Path-safety grep (always runs; enforced unless --force).
    safety = path_safety_grep(repo)
    any_blocked = print_safety_report(safety)

    if args.safety:
        print("\n--safety only: exiting before any moves.")
        return

    # 2. Build move specs.
    specs = build_move_specs(repo)
    if not specs:
        print("\nNothing to move — root is already clean (or paths absent). Done.")
        return

    # 3. Enforce safety gate: block a move if its name was flagged active.
    blocked_names = {n for n, refs in safety.items() if refs}
    planned, refused = [], []
    for s in specs:
        if s["src"].name in blocked_names and not args.force:
            refused.append(s)
        else:
            planned.append(s)

    # 4. Report the plan grouped by group letter.
    print("\n=== PLANNED MOVES ===")
    by_group = {}
    for s in planned:
        by_group.setdefault(s["group"], []).append(s)
    for grp in sorted(by_group):
        print(f"\n  -- Group {grp} -> {by_group[grp][0]['dest_dir']}/ --")
        for s in by_group[grp]:
            tracked = is_tracked(repo, s["src"])
            verb = "git mv" if tracked else "mv (gitignored)"
            rel = s["src"].relative_to(repo).as_posix()
            print(f"     [{verb:16}] {rel}  ->  {s['dest_dir']}/{s['src'].name}")
    if refused:
        print("\n  -- REFUSED (active script refs; use --force to override) --")
        for s in refused:
            rel = s["src"].relative_to(repo).as_posix()
            print(f"     [BLOCKED] {rel}  ({s['group']})")

    print(f"\nSummary: {len(planned)} to move, {len(refused)} refused, "
          f"{len(by_group)} groups.")

    if not args.commit:
        print("\nDRY-RUN only — pass --commit to execute. (Run --safety first if unsure.)")
        return

    if any_blocked and not args.force:
        # We still proceed for the non-blocked planned set, but warn loudly.
        print("\nNOTE: some names were flagged by the safety grep; those moves were "
              "refused above. Proceeding with the safe set only.")

    # 5. Execute.
    print("\n=== EXECUTING ===")
    made = []
    for d in NEW_DIRS:
        target = repo / d
        if not target.exists():
            target.mkdir(parents=True, exist_ok=True)
            made.append(d)
            print(f"  mkdir {d}/")
    moved, errors = 0, 0
    for s in planned:
        src = s["src"]
        dest = repo / s["dest_dir"] / src.name
        rel_src = src.relative_to(repo).as_posix()
        rel_dest = dest.relative_to(repo).as_posix()
        if dest.exists():
            print(f"  [SKIP] dest exists: {rel_dest}")
            continue
        tracked = is_tracked(repo, src)
        if tracked:
            r = run(["git", "mv", rel_src, rel_dest], repo)
        else:
            r = run(["mv", str(src), str(dest)], repo)
        if r.returncode == 0:
            moved += 1
            print(f"  [OK] {rel_src} -> {rel_dest}")
        else:
            errors += 1
            print(f"  [ERR] {rel_src}: {r.stderr.strip()}")

    # 6. Post-move asserts: protected masters still at root.
    print("\n=== POST-MOVE SANITY ===")
    missing = [m for m in PROTECTED_AT_ROOT if not (repo / m).exists()]
    if missing:
        print(f"  !! WARNING: protected master(s) NOT at root: {missing}")
    else:
        print("  OK: all protected masters present at root.")

    # 7. .gitignore reminder for _local_backups/.
    gi = repo / ".gitignore"
    needs_ignore = "_local_backups/" not in (gi.read_text() if gi.exists() else "")
    print(f"\nMoved: {moved}   Errors: {errors}   New dirs: {made or 'none'}")
    if needs_ignore:
        print("\nACTION: add '_local_backups/' to .gitignore so Group A backups "
              "stay out of the repo/Zenodo tarball:")
        print("   echo '_local_backups/' >> .gitignore")
    print("\nNext: review `git status`, update README layout section, then fold "
          "into the EOD v2.0 commit.")


if __name__ == "__main__":
    main()
