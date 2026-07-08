#!/usr/bin/env bash
# eod_commit_v1.sh — EOD batch commits for 2026-07-07 overnight cleanse + rebuild.
#
# Runs on Pete's Mac. Two commits, one per repo, per the kastner-github skill's
# canonical EOD pattern.
#
# COMMIT 1 (archive-repo): _master_entities.csv, _master_entity_studies.csv,
#   _master_technologies.csv, _master_tech_studies.csv, 3 apply-audit .txt
#   files, appended _decisions_log.md. Backups (*.bak_*) stay local per skill
#   Gotcha 5.
#
# COMMIT 2 (wiki-repo): all 1588 files changed (regenerated wiki pages, indices,
#   parquets, DuckDB, embeddings, scaffolding docs). Uses `git add -A` to sweep
#   the entire dirty tree.

set -euo pipefail

ARCHIVE_REPO=~/Desktop/Archive/aberdeen-group-archive
WIKI_REPO=~/Repos/kastner-aberdeen-wiki

# ─────────────────────────────────────────────────────────────────────────────
# STEP 1: Prep — append the decisions log appendix on the Mac
# ─────────────────────────────────────────────────────────────────────────────

echo "═══════════════════════════════════════════════════════════════════"
echo "  STEP 1: Prep — decisions log append"
echo "═══════════════════════════════════════════════════════════════════"
cd "$ARCHIVE_REPO"
git pull

# The appendix was committed to the repo by the agent; append it to
# _decisions_log.md, then remove the standalone appendix file.
APPENDIX="$ARCHIVE_REPO/eod_2026_07_07_decisions_log_appendix.md"
if [ ! -f "$APPENDIX" ]; then
  echo "ERROR: $APPENDIX not found. Did the agent commit it?"
  exit 1
fi

# Append (safe: idempotency guard on the "## 2026-07-07 -- Master-CSV cleanse" heading)
if grep -q "## 2026-07-07 -- Master-CSV cleanse + full SH pipeline rebuild" _decisions_log.md; then
  echo "  Decisions-log entry already present. Skipping append."
else
  cat "$APPENDIX" >> _decisions_log.md
  echo "  Appended $(wc -l < $APPENDIX) lines to _decisions_log.md"
fi

# Remove the standalone appendix (it was only staging for the append)
git rm -f "$(basename $APPENDIX)" 2>/dev/null || rm -f "$APPENDIX"

# ─────────────────────────────────────────────────────────────────────────────
# STEP 2: COMMIT 1 — archive-repo
# ─────────────────────────────────────────────────────────────────────────────

echo ""
echo "═══════════════════════════════════════════════════════════════════"
echo "  STEP 2: Commit 1 — archive-repo"
echo "═══════════════════════════════════════════════════════════════════"
cd "$ARCHIVE_REPO"

# Stage: 4 masters + 3 audit trails + _decisions_log.md
git add _master_entities.csv \
        _master_entity_studies.csv \
        _master_technologies.csv \
        _master_tech_studies.csv \
        tech_mislabel_apply_v1_applied_20260707T185429Z.txt \
        entity_metadata_apply_v1_applied_20260707T185429Z.txt \
        entity_aliases_sap_apply_v1_applied_20260707T185429Z.txt \
        _decisions_log.md

# Do NOT stage: *.bak_* (skill Gotcha 5 says these stay local)
# Show what's staged for review
echo ""
echo "→ Staged for archive-repo commit:"
git status --short --cached

echo ""
echo "→ Files intentionally NOT staged (staying local):"
git status --short | grep -E "\.bak_" | head

echo ""
read -p "Proceed with archive-repo commit? [y/N] " ANS
if [[ "$ANS" != "y" && "$ANS" != "Y" ]]; then
  echo "Aborted. Nothing committed."
  exit 0
fi

git commit -m "Master-CSV cleanse (Phases A/B/C-narrow) + full SH pipeline rebuild

Applied 2026-07-07T18:54:29Z; full pipeline rebuild finished 2026-07-08T04:15:51Z
(interrupted at ~21:00 UTC by power failure; resumed via overnight_v3_resume.sh).

Phase A - Tech mislabel repair (8 MERGE_INTO rows):
  data-mining -> service-oriented-architecture
  microsoft-backoffice -> numa-architecture
  sun-ultrasparc -> enterprise-information-integration
  audio-conferencing -> oltp
  webex-training-center -> ms-cluster-server
  titanium -> itanium
  t2-04 -> numa-architecture
  tech-01 -> rolap
_master_technologies.csv: 4376 -> 4368 (delta -8)
_master_tech_studies.csv: 5389 -> 5389 (43 rewrites, 0 dedups)

Phase B - Entity metadata bleed fix (10 rows, 23 field changes):
  informix-software: successor Siemens-Nixdorf -> IBM (2001, \$1B)
  microsoft: successor 'HP Inc./HPE' -> null; status restructured -> active
  microsoft-corporation: successor 'Oracle Corp (1995)' -> null; status active
  intel: successor 'Compaq (1998) then HP (2002)' -> null
  intel-corporation: [DEFERRED] -> null
  sybase: entity_type marketing-services -> software-vendor;
          successor 'Compaq/HP/HPE-NonStop' -> SAP AG (2010, \$5.8B)
  yahoo: successor 'HP Inc./HPE' -> Verizon Media (2017) then Apollo (2021)
  stratus-technologies: successor 'Compaq/HP' -> null
  oracle-corporation: successor 'Accrue/JDA' -> null; entity_type fixed
  ENT-S3-001: successor 'Compaq/HP' -> null
_master_entities.csv: 3293 -> 3293 (row count unchanged)

Phase C-narrow - SAP cluster merge (survivor: sap-ag per CANONICAL_IDS.md):
  MERGE_INTO sap-ag: sap, ENT-SAP, ENT-SAP-001, ENT-BO-002, ENT-IRP-003
  KEEP_SEPARATE: sap-america, sap-america-utilities, paul-wahl-sap
_master_entities.csv: 3293 -> 3288 (delta -5)
_master_entity_studies.csv: 3900 -> 3900 (19 rewrites, 0 dedups)

Phase 0 audit (07_audit_masters_v1.py): ALL PROBES PASS.
  Alias-collision ratio: entities 0.8822 -> 0.8829, tech 0.9250 -> 0.9265.
  Tech ID-vs-name congruence: 0 NEW violators; 8 cleared.
  Successor-bleed: 4 -> 0; all cleared (ENT-S3-001, intel, stratus-technologies, sybase).

Shape audits (BEFORE / AFTER):
  studies: 1504 / 1504
  observations: 24842 / 24842
  entities: 3293 / 3288 (delta -5)
  technologies: 4376 / 4368 (delta -8)
  high_prescience: 876 / 876
  sh_scores: 17030 (live in v_prescience_sh)
  sh_verdicts: 792 (live in v_studies_with_sh_verdicts)

Backups (.bak_phase_*_20260707T185429Z) stay local per skill Gotcha 5.

Refs: candidates CSVs + apply scripts + Phase 0 harness shipped in earlier
commit 56c2e2d2; overnight runners in 4f233e19 / 0fc4fbf2 / 91714d27.
Decisions log entry: see _decisions_log.md tail."

echo ""
echo "→ Pushing archive-repo to origin/main"
git push origin main

# ─────────────────────────────────────────────────────────────────────────────
# STEP 3: COMMIT 2 — wiki-repo
# ─────────────────────────────────────────────────────────────────────────────

echo ""
echo "═══════════════════════════════════════════════════════════════════"
echo "  STEP 3: Commit 2 — wiki-repo"
echo "═══════════════════════════════════════════════════════════════════"
cd "$WIKI_REPO"

# Notes-dir pre-commit check (mandatory per kastner-github skill)
NOTES_STATUS=$(git status --porcelain wiki/notes/ 2>/dev/null)
if [ -n "$NOTES_STATUS" ]; then
  echo ""
  echo "⚠️  WARNING: wiki/notes/ has uncommitted changes:"
  echo "$NOTES_STATUS"
  echo ""
  read -p "Include notes in this commit? [y/N] " NOTES_ANS
  if [[ "$NOTES_ANS" != "y" && "$NOTES_ANS" != "Y" ]]; then
    echo "Notes NOT included. Please handle them separately."
  fi
fi

# Stage all wiki changes
git add -A

# Show summary before committing (1588 files is a lot; show counts only)
echo ""
echo "→ Wiki repo staged summary:"
git diff --cached --stat | tail -5
STAGED=$(git diff --cached --numstat | wc -l | tr -d ' ')
echo "  Total files staged: $STAGED"

echo ""
read -p "Proceed with wiki-repo commit ($STAGED files)? [y/N] " ANS
if [[ "$ANS" != "y" && "$ANS" != "Y" ]]; then
  echo "Aborted. Wiki-repo not committed."
  exit 0
fi

git commit -m "Full pipeline rebuild after 2026-07-07 master-CSV cleanse

Complete regeneration of wiki study/entity/tech markdown pages, indices,
scaffolding docs, parquets, DuckDB, and embeddings via the SH-aware pipeline
chain (Phases 1 v3, 2 v5, 3 v3, 4 v6, 5 v3, 6 v2).

Shape (post-cleanse, verified via DuckDB shape audit):
  studies=1504, observations=24842, entities=3288 (-5 from previous),
  technologies=4368 (-8 from previous), high_prescience=876,
  sh_scores=17030, sh_verdicts=792.

Reflects archive-repo commit landing the Phase A/B/C-narrow cleanse:
- 8 tech mislabel merges (data-mining/microsoft-backoffice/sun-ultrasparc/
  audio-conferencing/webex-training-center/titanium/t2-04/tech-01)
- 10 entity metadata bleed fixes (Microsoft/Intel/Sybase/Yahoo/Informix/etc.)
- 5 SAP alias merges into sap-ag

Wiki changes:
- All 1504 study pages carry prescience_3y_enum frontmatter
- 792 gradeable study pages carry 'Short-horizon prescience' body section
- SH-aware README/AGENTS.md/chat-starter.md via Phase 6 v2
- bge-m3 (1024-dim) re-embed of 10862 pages, ~18 min
- DuckDB now has 32 views incl. 5 new SH views (v_prescience_sh, etc.)

Log locations (Pete's Mac):
  Original: logs/wiki_rebuild_20260707T185429Z/
  Resume:   logs/wiki_rebuild_resume_20260707T213122Z/
  Status:   logs/OVERNIGHT_STATUS_20260707T213122Z.OK

Decisions log entry: archive-repo commit's _decisions_log.md tail."

echo ""
echo "→ Pushing wiki-repo to origin/main"
git push origin main

echo ""
echo "═══════════════════════════════════════════════════════════════════"
echo "  ✓ EOD BATCH COMMITS COMPLETE"
echo "═══════════════════════════════════════════════════════════════════"
