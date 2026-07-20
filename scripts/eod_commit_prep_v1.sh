#!/usr/bin/env bash
# eod_commit_prep_v1.sh — stage + commit the big 2026-07-18 batch across both repos.
# Idempotent-ish: safe to re-run; prints plan, requires --commit to actually commit.
# Run on the Mac. NOT auto-pushed here except where noted — prints push cmds.
set -uo pipefail

ARCHIVE=/Users/scott/Desktop/Archive/aberdeen-group-archive
WIKI=/Users/scott/Repos/kastner-aberdeen-wiki
DO=${1:-}

echo "=================== ARCHIVE REPO ==================="
cd "$ARCHIVE"
# sync the audit baseline repo-copy from the canonical (updated Sat)
cp /Users/scott/Desktop/Archive/Perplexity_Only/audit_masters_baseline.json \
   "$ARCHIVE/Perplexity_Only/audit_masters_baseline.json"
echo "[archive] plan:"
echo "  - 3 masters (prescience_scores, studies, technologies)"
echo "  - audit baseline (synced from canonical)"
echo "  - 3 audit sidecar .txt (batch_verdict, appdev_lifecycle, powerbuilder)"
git add _master_prescience_scores.csv _master_studies.csv _master_technologies.csv \
        Perplexity_Only/audit_masters_baseline.json \
        _master_studies.csv.applied_batch_verdict_*.txt \
        _master_technologies.csv.applied_appdev_lifecycle_*.txt \
        _master_technologies.csv.applied_powerbuilder_*.txt
git status --short | sed 's/^/  /'

echo ""
echo "=================== WIKI REPO ==================="
cd "$WIKI"
# 1. Ensure the untracking ignore rules ARE in .gitignore (Wednesday's edit didn't persist)
for rule in 'data/embeddings.parquet' 'data/_validated/'; do
  grep -qxF "$rule" .gitignore || echo "$rule" >> .gitignore
done
echo "[wiki] .gitignore now:"; sed 's/^/  /' .gitignore
# 2. Re-assert removal-from-tracking of the big regenerated artifacts (keep on disk)
git rm -r --cached --ignore-unmatch data/_validated/ >/dev/null 2>&1
git rm --cached --ignore-unmatch data/embeddings.parquet >/dev/null 2>&1
# 3. Stage everything else (pages, live parquets, scaffolding, .gitignore) — big-file rules now block re-add
git add -A
echo "[wiki] staged summary:"
git status --porcelain | sed 's|^\(..\) \([^/]*\).*|\1 \2|' | sort | uniq -c | sed 's/^/  /'
echo "[wiki] sanity — embeddings/_validated must NOT be staged for add:"
git diff --cached --name-only | grep -E 'embeddings.parquet|_validated/' | sed 's/^/  RE-ADDED?! /' || echo "  OK: not re-added"

if [ "$DO" != "--commit" ]; then
  echo ""; echo ">>> DRY-RUN. Re-run with --commit to create both commits."
  exit 0
fi

echo ""; echo ">>> COMMITTING…"
cd "$ARCHIVE"
git commit -m "EOD 2026-07-18: Pass C full backlog — 4259 scores promoted, 572 verdicts recomputed

- _master_prescience_scores.csv: +4259 backlog scores (17569 -> 21828) from the
  22.4h v8 sweep (4527 obs; 26 parse-fail/-1 dropped).
- _master_studies.csv: 572 verdict recomputes on now-complete scoring (24 memoir
  chapters protected; authored/curated verdicts preserved). High-prescience enum
  507 -> 140 — honest recalibration onto full obs scoring.
- _master_technologies.csv: java/eclipse vendor fixes + powerbuilder lifecycle fix.
- audit baseline refreshed (grandfathers the 3 six-study techs; banks 12 cleared
  violators). Phase 0 audit passes clean.
- audit sidecars for the three value-only master edits."
echo ">>> archive committed. Push: (cd $ARCHIVE && git push origin main)"

cd "$WIKI"
git commit -m "EOD 2026-07-18: full Phase 3-6 rebuild for Pass C backlog recalibration

- Regenerated all study/entity/tech wiki pages (3100+) to reflect the recomputed
  verdicts; re-embedded all pages (bge-m3); refreshed indices + scaffolding.
- .gitignore: stop tracking regenerated data/embeddings.parquet (66MB) +
  data/_validated/ (files remain on disk; rebuilt every Phase 5). Completes the
  2026-07-15 untracking that didn't persist.
- kw_ask.py --cloud fix + page_type backfill (335 quotations pages) already landed."
echo ">>> wiki committed. Push: (cd $WIKI && git push origin main)"
