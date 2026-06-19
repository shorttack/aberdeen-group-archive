#!/usr/bin/env bash
# eod_quotations_reconcile_batch_commit_v1.sh
#
# One-shot Mac-side reconcile commit for 2026-06-19 EOD.
# Builds one batch commit on shorttack/aberdeen-group-archive main that:
#   1. UPDATEs kastner-author/quotations/kastner_quotes_clean.csv
#   2. ADDs 17 new files under kastner-author/quotations/
#   3. APPENDs N decisions-log entries to _decisions_log.md
#   4. UPDATEs WORKLIST.md at repo root
#
# Pre-flight assumptions:
#   - Run from Mac (has gh auth + jq + base64 + python3)
#   - $REPO = shorttack/aberdeen-group-archive
#   - $ARCHIVE_LOCAL = ~/Desktop/Archive/aberdeen-group-archive (repo clone)
#   - Mac files live under $ARCHIVE_LOCAL/kastner-author/quotations/
#   - Sandbox-staged files (decisions log entries, WORKLIST) are in
#     the same clone under known paths (Pete will git pull before running)
#
# Behavior: dry-run by default. Pass --commit to execute.
#
# Output: prints planned tree, blob shas, final commit sha. Aborts on any HTTP error.

set -euo pipefail

REPO="shorttack/aberdeen-group-archive"
ARCHIVE_LOCAL="${HOME}/Desktop/Archive/aberdeen-group-archive"
QDIR="${ARCHIVE_LOCAL}/kastner-author/quotations"
DLOG_LOCAL="${ARCHIVE_LOCAL}/_decisions_log.md"
WORKLIST_LOCAL="${ARCHIVE_LOCAL}/WORKLIST.md"

COMMIT=false
for arg in "$@"; do
  case "$arg" in
    --commit) COMMIT=true ;;
    *) echo "Unknown arg: $arg" >&2; exit 2 ;;
  esac
done

# -- File manifest (path-on-Mac : path-in-repo : action) ------------------------
# UPDATE row first (master), then ADDs alphabetically.
declare -a MANIFEST=(
  "${QDIR}/kastner_quotes_clean.csv|kastner-author/quotations/kastner_quotes_clean.csv|UPDATE"
  "${QDIR}/_format_mismatch_admits_v1.json|kastner-author/quotations/_format_mismatch_admits_v1.json|ADD"
  "${QDIR}/_format_mismatch_review_v1.csv|kastner-author/quotations/_format_mismatch_review_v1.csv|ADD"
  "${QDIR}/_format_mismatch_review_v2.csv|kastner-author/quotations/_format_mismatch_review_v2.csv|ADD"
  "${QDIR}/_format_mismatch_review_v3.csv|kastner-author/quotations/_format_mismatch_review_v3.csv|ADD"
  "${QDIR}/_horizon_backfill_3y_v1_applied.txt|kastner-author/quotations/_horizon_backfill_3y_v1_applied.txt|ADD"
  "${QDIR}/_pdf_segments_unclaimed_v1.json|kastner-author/quotations/_pdf_segments_unclaimed_v1.json|ADD"
  "${QDIR}/_unindexed_kastner_candidates_v2.csv|kastner-author/quotations/_unindexed_kastner_candidates_v2.csv|ADD"
  "${QDIR}/_unindexed_kastner_candidates_v3.csv|kastner-author/quotations/_unindexed_kastner_candidates_v3.csv|ADD"
  "${QDIR}/calibration_ab_v1.csv|kastner-author/quotations/calibration_ab_v1.csv|ADD"
  "${QDIR}/calibration_ab_v1.jsonl|kastner-author/quotations/calibration_ab_v1.jsonl|ADD"
  "${QDIR}/calibration_ab_v1_report.md|kastner-author/quotations/calibration_ab_v1_report.md|ADD"
  "${QDIR}/pipeline_1_routing_v1.json|kastner-author/quotations/pipeline_1_routing_v1.json|ADD"
  "${QDIR}/quotations_corpus_v1.csv|kastner-author/quotations/quotations_corpus_v1.csv|ADD"
  "${QDIR}/quotations_corpus_v1.jsonl|kastner-author/quotations/quotations_corpus_v1.jsonl|ADD"
  "${QDIR}/quotations_corpus_v1_report.md|kastner-author/quotations/quotations_corpus_v1_report.md|ADD"
  "${QDIR}/quote_only_rows_v1.csv|kastner-author/quotations/quote_only_rows_v1.csv|ADD"
  "${QDIR}/routing_summary.csv|kastner-author/quotations/routing_summary.csv|ADD"
  "${DLOG_LOCAL}|_decisions_log.md|UPDATE"
  "${WORKLIST_LOCAL}|WORKLIST.md|UPDATE"
)

# -- Pre-flight checks ---------------------------------------------------------
echo "== Pre-flight =="
for entry in "${MANIFEST[@]}"; do
  local_path="${entry%%|*}"
  if [[ ! -f "$local_path" ]]; then
    echo "MISSING: $local_path" >&2
    exit 3
  fi
done
echo "All ${#MANIFEST[@]} files present on disk."

# -- Print plan ----------------------------------------------------------------
echo ""
echo "== Reconcile plan =="
printf "%-7s  %-9s  %s\n" "ACTION" "SIZE" "REPO PATH"
for entry in "${MANIFEST[@]}"; do
  local_path="${entry%%|*}"; rest="${entry#*|}"
  repo_path="${rest%%|*}"; action="${rest##*|}"
  size=$(wc -c < "$local_path" | tr -d ' ')
  printf "%-7s  %-9s  %s\n" "$action" "$size" "$repo_path"
done

echo ""
if ! $COMMIT; then
  echo "DRY-RUN. Re-run with --commit to execute."
  exit 0
fi

# -- Create blobs --------------------------------------------------------------
echo ""
echo "== Creating blobs =="
declare -a TREE_ENTRIES=()
for entry in "${MANIFEST[@]}"; do
  local_path="${entry%%|*}"; rest="${entry#*|}"
  repo_path="${rest%%|*}"
  echo -n "  blob: $repo_path ... "
  base64 -i "$local_path" | tr -d '\n' > /tmp/blob.b64
  python3 -c "import json; print(json.dumps({'content': open('/tmp/blob.b64').read(), 'encoding': 'base64'}))" > /tmp/blob_req.json
  BLOB_SHA=$(gh api --method POST "/repos/${REPO}/git/blobs" --input /tmp/blob_req.json --jq '.sha')
  echo "$BLOB_SHA"
  TREE_ENTRIES+=("{\"path\":\"${repo_path}\",\"mode\":\"100644\",\"type\":\"blob\",\"sha\":\"${BLOB_SHA}\"}")
done

# -- Build tree -------------------------------------------------------------
echo ""
echo "== Building tree =="
MAIN_SHA=$(gh api "/repos/${REPO}/git/refs/heads/main" --jq '.object.sha')
TREE_SHA=$(gh api "/repos/${REPO}/git/commits/${MAIN_SHA}" --jq '.tree.sha')
echo "  base_tree: $TREE_SHA (HEAD $MAIN_SHA)"

TREE_JSON=$(IFS=,; echo "[${TREE_ENTRIES[*]}]")
jq -n --arg base "$TREE_SHA" --argjson tree "$TREE_JSON" \
  '{base_tree: $base, tree: $tree}' > /tmp/tree_req.json
NEW_TREE_SHA=$(gh api --method POST "/repos/${REPO}/git/trees" --input /tmp/tree_req.json --jq '.sha')
echo "  new tree:  $NEW_TREE_SHA"

# -- Commit ---------------------------------------------------------------
echo ""
echo "== Creating commit =="
MSG="EOD 2026-06-19: v1.8.0 quotations corpus reconcile + decisions log + WORKLIST

Adds full v1.8.0 quotations work (corpus scoring, calibration, format-mismatch
review, routing) to kastner-author/quotations/.

Files (${#MANIFEST[@]} total):
- UPDATE kastner_quotes_clean.csv (horizon backfill + format-mismatch admits)
- ADD quotations_corpus_v1.{csv,jsonl,md} (334 verdicts: 184 high / 84 med / 66 low)
- ADD calibration_ab_v1.{csv,jsonl,md} (300-row A/B, 82.6% agreement)
- ADD _format_mismatch_review_v{1,2,3}.csv + _format_mismatch_admits_v1.json
- ADD _horizon_backfill_3y_v1_applied.txt (audit trail)
- ADD _pdf_segments_unclaimed_v1.json
- ADD _unindexed_kastner_candidates_v{2,3}.csv
- ADD pipeline_1_routing_v1.json + routing_summary.csv
- ADD quote_only_rows_v1.csv
- APPEND _decisions_log.md (N entries — see file)
- UPDATE WORKLIST.md"

jq -n --arg msg "$MSG" --arg tree "$NEW_TREE_SHA" --arg parent "$MAIN_SHA" \
  '{message: $msg, tree: $tree, parents: [$parent]}' > /tmp/commit_req.json
NEW_COMMIT_SHA=$(gh api --method POST "/repos/${REPO}/git/commits" --input /tmp/commit_req.json --jq '.sha')
echo "  commit: $NEW_COMMIT_SHA"

# -- Move ref ---------------------------------------------------------
echo ""
echo "== Moving main ref =="
jq -n --arg sha "$NEW_COMMIT_SHA" '{sha: $sha}' > /tmp/ref_req.json
gh api --method PATCH "/repos/${REPO}/git/refs/heads/main" --input /tmp/ref_req.json --jq '.object.sha'

echo ""
echo "== DONE =="
echo "Commit: https://github.com/${REPO}/commit/${NEW_COMMIT_SHA}"
