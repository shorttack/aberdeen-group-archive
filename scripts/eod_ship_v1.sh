#!/bin/bash
# eod_ship_v1.sh
#
# Lightweight end-of-day shipping for the Kastner Aberdeen Archive.
#
# Pulls latest, stages all changed files in the archive clone, commits
# with a single message, and pushes. Does NOT touch the wiki clone (that
# repo is the v1.6 snapshot — full rebuilds use a separate flow).
#
# Dry-run by default. Pass --commit to actually push.
#
# Usage:
#   bash ~/Desktop/Archive/scripts/eod_ship_v1.sh
#   bash ~/Desktop/Archive/scripts/eod_ship_v1.sh --commit
#   bash ~/Desktop/Archive/scripts/eod_ship_v1.sh --commit --message "Custom message"
#
# v1.0  2026-06-05  Pete Kastner / Computer

set -eu

REPO="${HOME}/Desktop/Archive/aberdeen-group-archive"
DEFAULT_MSG="EOD ship $(date -u +%Y-%m-%dT%H:%MZ)"

COMMIT=0
MESSAGE="$DEFAULT_MSG"
while [ $# -gt 0 ]; do
  case "$1" in
    --commit) COMMIT=1; shift ;;
    --message) MESSAGE="$2"; shift 2 ;;
    -m) MESSAGE="$2"; shift 2 ;;
    -h|--help)
      sed -n '2,15p' "$0"
      exit 0
      ;;
    *)
      echo "Unknown arg: $1" >&2
      exit 2
      ;;
  esac
done

if [ ! -d "$REPO/.git" ]; then
  echo "ERROR: $REPO is not a git repo" >&2
  exit 1
fi

cd "$REPO"

echo "===== eod_ship_v1.sh   MODE: $([ $COMMIT -eq 1 ] && echo COMMIT || echo DRY-RUN) ====="
echo "Repo:    $REPO"
echo "Message: $MESSAGE"
echo

# --- 1. Sanity: confirm we're on main and tree is sane ---------------------

BRANCH=$(git rev-parse --abbrev-ref HEAD)
if [ "$BRANCH" != "main" ]; then
  echo "ERROR: on branch '$BRANCH', expected 'main'. Aborting." >&2
  exit 1
fi
echo "[ok]    on branch main"

# --- 2. Pull latest (rebase to keep history linear) ------------------------

echo "[pull]  fetching origin/main..."
git fetch origin main >/dev/null 2>&1
LOCAL=$(git rev-parse HEAD)
REMOTE=$(git rev-parse origin/main)
BASE=$(git merge-base HEAD origin/main)
if [ "$LOCAL" = "$REMOTE" ]; then
  echo "[ok]    already up to date"
elif [ "$LOCAL" = "$BASE" ]; then
  echo "[pull]  remote ahead — fast-forward pulling"
  git pull --ff-only origin main
elif [ "$REMOTE" = "$BASE" ]; then
  echo "[ok]    local ahead — push needed (will do below)"
else
  echo "[warn]  diverged from origin/main"
  echo "        local : $LOCAL"
  echo "        remote: $REMOTE"
  echo "        base  : $BASE"
  echo "        Resolve manually before retrying. Aborting."
  exit 1
fi

# --- 3. What changed? ------------------------------------------------------

echo
echo "[diff]  --- changed files ---"
CHANGED=$(git status --porcelain)
if [ -z "$CHANGED" ]; then
  echo "        (nothing to commit)"
  echo
  echo "[done]  Tree clean. Nothing to ship."
  exit 0
fi
echo "$CHANGED"
echo

# --- 4. Stage + commit + push (commit mode only) ---------------------------

if [ "$COMMIT" -eq 0 ]; then
  echo "[done]  Dry-run only. Re-run with --commit to push."
  exit 0
fi

# Refuse to commit if WORKLIST_<date>.md and WORKLIST.md exist but disagree
# (mirror rule A from kastner-github skill)
if [ -f WORKLIST.md ]; then
  DATED=$(ls WORKLIST_*.md 2>/dev/null | sort -r | head -1 || true)
  if [ -n "$DATED" ]; then
    SHA1=$(shasum -a 256 WORKLIST.md | awk '{print $1}')
    SHA2=$(shasum -a 256 "$DATED" | awk '{print $1}')
    if [ "$SHA1" != "$SHA2" ]; then
      echo "ERROR: WORKLIST.md and $DATED disagree (mirror rule A violation)." >&2
      echo "       Refresh the mirror in workspace and re-stage before shipping." >&2
      exit 1
    fi
    echo "[ok]    WORKLIST mirror clean ($DATED == WORKLIST.md)"
  fi
fi

echo "[stage] git add -A"
git add -A
echo
echo "[stage] --- staged ---"
git status --short
echo

echo "[commit] $MESSAGE"
git commit -m "$MESSAGE"
echo

echo "[push]  origin main"
git push origin main
echo

# --- 5. Final summary ------------------------------------------------------

NEW_HEAD=$(git rev-parse --short HEAD)
echo "[done]  Shipped commit $NEW_HEAD to origin/main."
