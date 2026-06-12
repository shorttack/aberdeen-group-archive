# archive_masters_pre_reconcile_20260612T105652Z

**Created:** 2026-06-12T10:56:52+00:00
**Source repo HEAD at time of backup:** `1b97c258a9e8b5708209f6959342eb949557ac79`

## Purpose

This directory preserves the repo's pre-reconcile state of four master CSVs
as they existed on `main` before the §11t Mac↔repo masters reconcile
(2026-06-11 PM EDT).

The reconcile shipped the Mac's canonical post-May-24 state (v20 obs_id
normalizer + namespace cleanup + codes rebuild) to the repo, where the
files had been frozen since 2026-05-21 (`11670e87`) / 2026-05-26 (`0d48d9a8`).

## Contents

| File | Repo blob sha (pre-reconcile) | Size (bytes) |
|---|---|---|
| `_master_observations.csv` | `814f8215db7d851ee6238413bcd1ea9966dc7f6b` | 7751306 |
| `_master_entities.csv` | `2e5f5575fe0bf75ce994284de12fb695001ccf67` | 2176162 |
| `_master_technologies.csv` | `e9363ced9e5a97d92b5cc6563bc369371eb98b89` | 1975396 |
| `_master_codes.csv` | `305b7d5a0c0564d0c4f5da8b00365abf26b9e3a4` | 2512305 |

## Rollback

To restore the pre-reconcile state of any single file:

```bash
# Replace WHICH with one of: _master_observations.csv, _master_entities.csv, _master_technologies.csv, _master_codes.csv
WHICH=_master_observations.csv
cd ~/Desktop/Archive/aberdeen-group-archive
git checkout <RECONCILE_COMMIT_SHA>~1 -- $WHICH
git commit -m "Revert §11t reconcile of $WHICH"
git push origin main
```

Or directly from this backup tree:

```bash
cp archive_masters_pre_reconcile_20260612T105652Z/$WHICH ./$WHICH
git add $WHICH
git commit -m "Restore $WHICH from pre-§11t backup"
git push origin main
```

## Forever-archive principle

These blobs are referenced into the §11t commit tree by sha, not re-uploaded.
They are byte-identical to the repo's pre-reconcile state and remain reachable
in git history regardless of future `main` movements.

## Related

- Decisions log entry: `_decisions_log.md` (§11t entry, 2026-06-11)
- Audit artifacts (on Pete's Mac, not committed):
  - `~/Desktop/Archive/_audit_mac_vs_repo_20260612T005318Z.csv`
  - `~/Desktop/Archive/_audit_schema_overlap_20260612T005802Z.json`
- Audit scripts (in repo):
  - `scripts/audit_mac_vs_repo_v1.py` (commit `71ed3165`)
  - `scripts/audit_schema_and_overlap_v1.py` (commit `187be686`)
