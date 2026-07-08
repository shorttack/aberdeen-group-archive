#!/usr/bin/env bash
# legacy_moves_v1.sh — Move superseded scripts to _legacy/ (WORKLIST #5)
#
# Authored 2026-07-08 during session close-out. Ships as a single git commit
# on the Mac. Run from Pete's clone of shorttack/aberdeen-group-archive.
#
# Total moves: 68 files
#   scripts/build/  -> scripts/build/_legacy/   (15 files: phase scripts + _llm_helper_v1-v3)
#   scripts/        -> scripts/_legacy/         (53 files: orchestrators + apply/promote/diag one-offs)
#
# Nothing is deleted. `git mv` preserves rename history so a future
# `git log --follow` on any moved file traces its full history.
#
# Rationale per file family:
#   - Phase scripts: v1.8 canonical chain is 01_v3, 02_v5, 03_v3, 04_v6, 05_v3, 06_v2, 07_v1.
#     Older versions retired. 05_v4 was the REJECTED qwen candidate (2026-07-01).
#   - _llm_helper: canonical is v4 (used by 04_generate_indices_v6). v1-v3 retired.
#   - Orchestrators: pipeline_canonical_v2.sh (this session) is canonical; overnight_v1/v2/v3_resume,
#     monitor_phases, prep_overnight, eod_commit_v1 all subsumed.
#   - Apply scripts v1: superseded by v2 idempotent versions (this session).
#   - One-offs: audited via version-family sweep; each family keeps only the highest version.
#
# NOTE: run_prescience_pass_c_v5.py is superseded by v7 (v6 exists only in the
# repo, not on Mac). The kastner-archive-pipeline skill v1.8 still names v5 as
# canonical — that's a stale reference that needs a v1.9 skill patch.

set -euo pipefail

REPO=~/Desktop/Archive/aberdeen-group-archive
cd "$REPO"

# Confirm we're at the top of the working tree
if [ ! -d ".git" ] || [ ! -f "_master_studies.csv" ]; then
  echo "ERROR: not at repo root. Expected $REPO with .git and _master_studies.csv"
  exit 1
fi

# Confirm clean working tree before we start (so any conflicts surface as
# obvious mv failures, not silent stomps)
if ! git diff --quiet || ! git diff --cached --quiet; then
  echo "ERROR: working tree not clean. Commit or stash local changes first."
  git status --short
  exit 1
fi

# Confirm target dirs exist
mkdir -p scripts/build/_legacy scripts/_legacy

DRY_RUN=1
if [ "${1:-}" = "--commit" ]; then
  DRY_RUN=0
fi

echo ""
echo "═══════════════════════════════════════════════════════════════════"
echo "  LEGACY MOVES v1 — Kastner archive"
echo "  Mode: $([ "$DRY_RUN" = "1" ] && echo DRY-RUN || echo COMMIT)"
echo "═══════════════════════════════════════════════════════════════════"

MOVED=0
SKIPPED=0

do_move() {
  local src="$1"
  local dst_dir="$2"
  local base=$(basename "$src")
  local dst="$dst_dir/$base"

  if [ ! -f "$src" ]; then
    echo "  [skip] $src (not present)"
    SKIPPED=$((SKIPPED+1))
    return 0
  fi
  if [ -f "$dst" ]; then
    echo "  [skip] $src -> $dst (already at target)"
    SKIPPED=$((SKIPPED+1))
    return 0
  fi

  if [ "$DRY_RUN" = "1" ]; then
    echo "  [dry ] git mv $src -> $dst"
  else
    git mv "$src" "$dst"
    echo "  [ mv ] $src -> $dst"
  fi
  MOVED=$((MOVED+1))
}

# ─── scripts/build/ → scripts/build/_legacy/ ─────────────────────────────

echo ""
echo "── Phase scripts (build/) ──"

# 01_load_csvs
do_move scripts/build/01_load_csvs_v2.py                    scripts/build/_legacy

# 02_build_data_layer
do_move scripts/build/02_build_data_layer_v4.py             scripts/build/_legacy

# 03_generate_vault
do_move scripts/build/03_generate_vault_v2.py               scripts/build/_legacy

# 04_generate_indices (v6 canonical; retire v2, v3, v4, v5)
do_move scripts/build/04_generate_indices_v2.py             scripts/build/_legacy
do_move scripts/build/04_generate_indices_v3.py             scripts/build/_legacy
do_move scripts/build/04_generate_indices_v4.py             scripts/build/_legacy
do_move scripts/build/04_generate_indices_v5.py             scripts/build/_legacy

# 05_compute_embeddings (v3 canonical; v4 was the REJECTED qwen candidate)
do_move scripts/build/05_compute_embeddings_v4.py           scripts/build/_legacy

# 06_emit_scaffolding (v2 canonical; retire v1, v3, v4, v5)
do_move scripts/build/06_emit_scaffolding_v1.py             scripts/build/_legacy
do_move scripts/build/06_emit_scaffolding_v3.py             scripts/build/_legacy
do_move scripts/build/06_emit_scaffolding_v4.py             scripts/build/_legacy
do_move scripts/build/06_emit_scaffolding_v5.py             scripts/build/_legacy

# _llm_helper (v4 canonical)
# NOTE: v1 STAYS in build/ for now — 03_generate_vault_v3.py hardcodes
#   `import _llm_helper_v1 as llm` at line 45. Moving v1 to _legacy/ would
#   break Phase 3 at import time (dies before the first LLM call). Deferred
#   to a follow-up session that ships 03_generate_vault_v4 with the import
#   swap. Meanwhile keep v1 alongside v4.
# do_move scripts/build/_llm_helper_v1.py                     scripts/build/_legacy   # BLOCKED (Phase 3 dependency)
do_move scripts/build/_llm_helper_v2.py                     scripts/build/_legacy
do_move scripts/build/_llm_helper_v3.py                     scripts/build/_legacy

# ─── scripts/ (flat) → scripts/_legacy/ ─────────────────────────────

echo ""
echo "── Orchestrators + EOD helpers ──"

do_move scripts/overnight_v1.sh                             scripts/_legacy
do_move scripts/overnight_v2.sh                             scripts/_legacy
do_move scripts/overnight_v3_resume.sh                      scripts/_legacy
do_move scripts/pipeline_canonical_v1.sh                    scripts/_legacy
do_move scripts/monitor_phases_3to6_v1.sh                   scripts/_legacy
do_move scripts/eod_commit_v1.sh                            scripts/_legacy
do_move scripts/prep_overnight_v1.sh                        scripts/_legacy

echo ""
echo "── Apply-script v1s (v2 idempotent versions supersede) ──"

do_move scripts/apply_entity_aliases_v1_sap.py              scripts/_legacy
do_move scripts/apply_entity_metadata_v1.py                 scripts/_legacy
do_move scripts/apply_tech_mislabel_v1.py                   scripts/_legacy
do_move scripts/apply_passb_reconcile_v1.py                 scripts/_legacy
do_move scripts/apply_passb_transcripts_v1.py               scripts/_legacy
do_move scripts/apply_unindexed_quotes_v2.py                scripts/_legacy   # v3 canonical

echo ""
echo "── Other version-family supersessions ──"

do_move scripts/anchor_year_resolver_v1.py                  scripts/_legacy
do_move scripts/backfill_blank_horizon_3y_v1.py             scripts/_legacy
do_move scripts/build_format_mismatch_review_v1.py          scripts/_legacy
do_move scripts/build_quotations_corpus_page_v1.py          scripts/_legacy
do_move scripts/change_local_model_v1.sh                    scripts/_legacy
do_move scripts/change_local_model_v2.sh                    scripts/_legacy
do_move scripts/compute_qwen_master_kappa_v1.py             scripts/_legacy
do_move scripts/detect_article_boundaries_v1.py             scripts/_legacy
do_move scripts/diag_admit_orphan_sources_v1.py             scripts/_legacy
do_move scripts/diagnose_pdf_format_mismatch_v1.py          scripts/_legacy
do_move scripts/diagnose_pdf_format_mismatch_v2.py          scripts/_legacy
do_move scripts/diagnose_pdf_format_mismatch_v3.py          scripts/_legacy
do_move scripts/discover_unindexed_kastner_quotes_v1.py     scripts/_legacy
do_move scripts/ingest_dectp_press_conf_v1.py               scripts/_legacy
do_move scripts/pre_filter_scoreable_obs_v4.py              scripts/_legacy
do_move scripts/pre_filter_scoreable_obs_v5.py              scripts/_legacy
do_move scripts/pre_filter_scoreable_obs_v6.py              scripts/_legacy
do_move scripts/prepare_for_ingest.py                       scripts/_legacy   # v3 canonical (unversioned original was v2.x)
do_move scripts/promote_l7_access_journeys_v1.py            scripts/_legacy
do_move scripts/promote_quotations_to_master_v1.py          scripts/_legacy
do_move scripts/promote_quotations_to_master_v2.py          scripts/_legacy
do_move scripts/reconcile_masters_mac_to_repo_v1.py         scripts/_legacy
do_move scripts/route_quotations_to_horizon_v1.py           scripts/_legacy
do_move scripts/run_prescience_calibration_v3.py            scripts/_legacy
do_move scripts/run_prescience_calibration_v4.py            scripts/_legacy
do_move scripts/run_prescience_calibration_v5_qwen_30obs.py scripts/_legacy
do_move scripts/run_prescience_calibration_v6_qwen_30obs.py scripts/_legacy
do_move scripts/run_prescience_pass_c_v5.py                 scripts/_legacy   # v7 canonical
do_move scripts/run_prescience_pass_c_v6.py                 scripts/_legacy   # v7 canonical
do_move scripts/run_prescience_short_horizon_v8.py          scripts/_legacy
do_move scripts/run_prescience_short_horizon_v9.py          scripts/_legacy
do_move scripts/score_quotations_calibration_v1.py          scripts/_legacy
do_move scripts/synthesize_17_transcripts_v1.py             scripts/_legacy
do_move scripts/union_article_corpus_v1.py                  scripts/_legacy

echo ""
echo "═══════════════════════════════════════════════════════════════════"
if [ "$DRY_RUN" = "1" ]; then
  echo "  DRY-RUN COMPLETE"
  echo "  Would move: $MOVED files"
  echo "  Skipped:    $SKIPPED (missing at source or already at target)"
  echo ""
  echo "  Re-run with --commit to actually move + stage the files:"
  echo "    bash $0 --commit"
else
  echo "  MOVES COMPLETE"
  echo "  Moved:   $MOVED files"
  echo "  Skipped: $SKIPPED"
  echo ""
  echo "  Staged changes (not yet committed). Review with:"
  echo "    git status --short | head -80"
  echo ""
  echo "  Commit with:"
  echo "    git commit -F ~/Desktop/Archive/scripts/legacy_moves_v1_msg.txt"
  echo "    git push"
fi
echo "═══════════════════════════════════════════════════════════════════"
