#!/bin/bash
# scripts/new_day.sh — Local-Mac driver for the `kastner-new-day` skill.
#
# Purpose: replace the multi-turn LLM round-trip through the bridge with ONE
# self-verifying Mac-side script. Modeled on `scripts/eod.sh` (kastner-eod).
#
# Inputs (piped as JSON on stdin):
#   {
#     "focus":       "One-paragraph focus/changelog for the Last-updated line",
#     "ship_state":  null | "Full replacement text for the Current ship state line",
#     "next_up":     [ "First bullet", "Second bullet", ... ]  // may be empty
#   }
#
# Behavior:
#   1. Preflight: repo clean-on-main, remote in sync, gh + jq installed,
#      no pre-existing WORKLIST_<today>.md.
#   2. Fetch canonical WORKLIST.md from origin/main via `gh api`, decode,
#      write to WORKLIST_<today>.md (repo root). Save /tmp pre-edit snapshot.
#   3. Pre-edit audit: section count, open-item count, done-item count,
#      section-name list.
#   4. Compute today's date + AM/PM in America/New_York.
#   5. Edit ONLY the four permitted regions:
#        (a) `**Last updated:**` line — replaced verbatim with new focus paragraph.
#        (b) `**Current ship state:**` line — replaced only if --ship-state was
#            provided (JSON key non-null); otherwise byte-frozen.
#        (c) `## Next up` section body — replaced with the new bullet list,
#            preceded by a `### <today> <AM|PM> focus — <first-sentence-of-focus>`
#            sub-header. Any content BELOW the first `## ` after Next up is preserved.
#        (d) `## Done this session` section — prepend a fresh sub-header
#            `### <today> <AM|PM> — <first-sentence-of-focus>` with an empty bullet
#            list, above whatever historical content already lives under it.
#   6. Post-edit diff gate: `diff` pre-edit vs edited file; assert EVERY hunk
#      falls inside the editable line ranges. Any drift => rollback + exit 1.
#   7. Post-edit re-audit: open-item count must equal pre-edit count
#      (no legitimately closed items in a new-day setup — that's an EOD/session
#      job, not a new-day job).
#   8. Mirror: `cp WORKLIST_<today>.md WORKLIST.md`; verify shasums match.
#   9. Print a compact JSON brief on stdout for the LLM to relay to Pete.
#
# Exit codes:
#   0 = success
#   1 = preflight failure (dirty repo, stale, missing tools, file exists)
#   2 = fetch failure
#   3 = audit failure (pre-edit)
#   4 = edit failure (permitted-region drift, or count mismatch)
#   5 = mirror failure (shasum mismatch)
#
# NOTE: This script NEVER commits, tags, or pushes. It only writes the dated
# file + mirror in the repo working tree. EOD batch commit is handled by
# scripts/eod.sh (kastner-eod skill).

set -euo pipefail

# Flags:
#   --skip-fetch : reuse the working-tree WORKLIST.md as the canonical source
#                  (for offline dry-runs and for the `pc bash` sandbox which has
#                  no network access). NOT for production use — the canonical
#                  source of truth remains origin/main.
#   --skip-git-check : skip the clean-tree / in-sync-with-origin preflight
#                      (only paired with --skip-fetch for isolated dry-runs).
SKIP_FETCH=0
SKIP_GIT_CHECK=0
for arg in "$@"; do
    case "$arg" in
        --skip-fetch)     SKIP_FETCH=1 ;;
        --skip-git-check) SKIP_GIT_CHECK=1 ;;
        *) echo "unknown flag: $arg" >&2; exit 1 ;;
    esac
done

ARCHIVE_DIR="${ARCHIVE_DIR:-$HOME/Desktop/Archive/aberdeen-group-archive}"
cd "$ARCHIVE_DIR"

# ─── 1. Preflight ────────────────────────────────────────────────────────────
fail() { echo "❌ $*" >&2; exit "${2:-1}"; }
ok()   { echo "✅ $*" >&2; }

if [ "$SKIP_FETCH" -eq 0 ]; then
    command -v gh >/dev/null || fail "gh CLI not found" 1
fi
command -v jq >/dev/null || fail "jq not found" 1
command -v python3 >/dev/null || fail "python3 not found" 1

# Date in America/New_York
TODAY=$(TZ=America/New_York date +%Y_%m_%d)
HOUR=$(TZ=America/New_York date +%H)
if [ "$HOUR" -lt 12 ]; then APM="AM"; else APM="PM"; fi
TODAY_ISO=$(TZ=America/New_York date +%Y-%m-%d)

DATED_FILE="WORKLIST_${TODAY}.md"
MIRROR_FILE="WORKLIST.md"
PRE_EDIT_SNAPSHOT="/tmp/WORKLIST_${TODAY}_pre_edit.md"

[ -f "$DATED_FILE" ] && fail "$DATED_FILE already exists — today's session already started" 1

# Git state: on main, clean, in sync with origin
if [ "$SKIP_GIT_CHECK" -eq 0 ]; then
    BRANCH=$(git rev-parse --abbrev-ref HEAD)
    [ "$BRANCH" = "main" ] || fail "not on main (on $BRANCH)" 1
    [ -z "$(git status --porcelain)" ] || fail "working tree dirty — commit or stash first" 1

    git fetch --quiet origin main
    LOCAL_SHA=$(git rev-parse HEAD)
    REMOTE_SHA=$(git rev-parse origin/main)
    [ "$LOCAL_SHA" = "$REMOTE_SHA" ] || fail "local main ($LOCAL_SHA) diverged from origin/main ($REMOTE_SHA) — pull or push first" 1

    ok "preflight passed (main clean, in sync at ${LOCAL_SHA:0:8})"
else
    LOCAL_SHA=$(git rev-parse HEAD 2>/dev/null || echo "UNKNOWN")
    ok "preflight SKIPPED (--skip-git-check) at ${LOCAL_SHA:0:8}"
fi

# ─── 2. Fetch canonical WORKLIST from origin/main via gh api ────────────────
# (The local WORKLIST.md is already at origin/main state per preflight, but we
#  fetch fresh anyway per skill invariant #1: source of truth is origin/main,
#  not any workspace/working-tree file.)
if [ "$SKIP_FETCH" -eq 0 ]; then
    gh api /repos/shorttack/aberdeen-group-archive/contents/WORKLIST.md \
      --jq '.content' 2>/dev/null | base64 -d > "$DATED_FILE" \
      || fail "gh api fetch of WORKLIST.md failed" 2
else
    [ -f "$MIRROR_FILE" ] || fail "--skip-fetch requires a local $MIRROR_FILE" 2
    cp "$MIRROR_FILE" "$DATED_FILE"
    ok "fetch SKIPPED (--skip-fetch) — using working-tree $MIRROR_FILE"
fi

[ -s "$DATED_FILE" ] || fail "WORKLIST is empty" 2

cp "$DATED_FILE" "$PRE_EDIT_SNAPSHOT"
ok "canonical WORKLIST → $DATED_FILE ($(wc -l < "$DATED_FILE") lines)"

# ─── 3. Pre-edit audit ──────────────────────────────────────────────────────
PRE_SECTIONS=$(grep -c '^## ' "$DATED_FILE")
PRE_OPEN=$(grep -c '^- \[ \]' "$DATED_FILE" || echo 0)
PRE_DONE=$(grep -c '^- \[x\]' "$DATED_FILE" || echo 0)

# Required anchor lines — the script REFUSES to edit a file that doesn't
# have the expected shape.
grep -q '^\*\*Last updated:\*\*'      "$DATED_FILE" || fail "missing '**Last updated:**' anchor" 3
grep -q '^\*\*Current ship state:\*\*' "$DATED_FILE" || fail "missing '**Current ship state:**' anchor" 3
grep -q '^## Next up$'                 "$DATED_FILE" || fail "missing '## Next up' section" 3
grep -q '^## Done this session$'       "$DATED_FILE" || fail "missing '## Done this session' section" 3

ok "pre-edit audit: sections=$PRE_SECTIONS open=$PRE_OPEN done=$PRE_DONE"

# ─── 4. Parse stdin JSON payload ────────────────────────────────────────────
PAYLOAD=$(cat)
[ -n "$PAYLOAD" ] || fail "no JSON payload on stdin" 1

FOCUS=$(echo "$PAYLOAD" | jq -r '.focus // empty')
SHIP_STATE=$(echo "$PAYLOAD" | jq -r '.ship_state // empty')
NEXT_UP_JSON=$(echo "$PAYLOAD" | jq -c '.next_up // []')

[ -n "$FOCUS" ] || fail "payload missing 'focus'" 1

# First-sentence summary of focus, for sub-headers. Trim to ~80 chars max.
FOCUS_SHORT=$(echo "$FOCUS" | awk 'BEGIN{RS="."} {print $0; exit}' | sed 's/^ *//;s/ *$//' | cut -c1-80)

ok "payload parsed (focus=${#FOCUS} chars, ship_state=${SHIP_STATE:+set}${SHIP_STATE:-unchanged}, next_up_items=$(echo "$NEXT_UP_JSON" | jq 'length'))"

# ─── 5. Edit the four permitted regions ─────────────────────────────────────
# All edits done in Python for correctness (line-boundary safety, unicode).
# Pass values via env vars, NOT heredoc interpolation, so arbitrary chars
# (quotes, backslashes, backticks) survive intact.
export ND_DATED_FILE="$DATED_FILE"
export ND_FOCUS="$FOCUS"
export ND_FOCUS_SHORT="$FOCUS_SHORT"
export ND_SHIP_STATE="$SHIP_STATE"
export ND_NEXT_UP_JSON="$NEXT_UP_JSON"
export ND_TODAY_ISO="$TODAY_ISO"
export ND_APM="$APM"

python3 <<'PYEOF'
import json, os, sys, pathlib

path        = pathlib.Path(os.environ["ND_DATED_FILE"])
focus       = os.environ["ND_FOCUS"]
focus_short = os.environ["ND_FOCUS_SHORT"]
ship_state  = os.environ["ND_SHIP_STATE"]
next_up     = json.loads(os.environ["ND_NEXT_UP_JSON"])
today_iso   = os.environ["ND_TODAY_ISO"]
apm         = os.environ["ND_APM"]

text = path.read_text(encoding="utf-8")
lines = text.split("\n")

# --- (a) Replace the **Last updated:** line ---
new_lu = f"**Last updated:** {today_iso} {apm} ({focus})"
for i, ln in enumerate(lines):
    if ln.startswith("**Last updated:**"):
        lines[i] = new_lu
        break
else:
    sys.exit("ERR: no **Last updated:** line found")

# --- (b) Replace **Current ship state:** line ONLY if ship_state provided ---
if ship_state:
    new_cs = f"**Current ship state:** {ship_state}"
    for i, ln in enumerate(lines):
        if ln.startswith("**Current ship state:**"):
            lines[i] = new_cs
            break
    else:
        sys.exit("ERR: no **Current ship state:** line found")

# --- (c) PREPEND a fresh sub-header + bullets to `## Next up` ---
# The Next up section is APPEND-ONLY across sessions in Pete's actual practice:
# it accumulates historical narrative (session focus blocks, deferred items,
# post-session follow-ups). New-day setup inserts today's focus block at the
# TOP so it appears immediately below the `## Next up` header. All prior
# content is preserved byte-for-byte below it.
next_up_idx = None
for i, ln in enumerate(lines):
    if ln == "## Next up":
        next_up_idx = i
        break
if next_up_idx is None:
    sys.exit("ERR: could not find ## Next up header")

today_block = [
    "",
    f"### {today_iso} {apm} focus — {focus_short}",
    "",
]
if next_up:
    for b in next_up:
        today_block.append(f"- [ ] {b}")
else:
    today_block.append("- [ ] (fill in today's next concrete action)")
today_block.append("")

# Insert immediately after `## Next up`. If the very next line is blank, keep it
# (our today_block starts with a blank too, which will collapse visually).
insert_at = next_up_idx + 1
if insert_at < len(lines) and lines[insert_at] == "":
    # skip the existing blank so we don't double it
    insert_at += 1
lines = lines[:insert_at] + today_block + lines[insert_at:]

# --- (d) Prepend fresh sub-header to `## Done this session` ---
# Same append-only pattern: prior sessions' done blocks stay as historical
# record; today's block goes on top.
done_idx = None
for i, ln in enumerate(lines):
    if ln == "## Done this session":
        done_idx = i
        break
if done_idx is None:
    sys.exit("ERR: no ## Done this session section")

new_done_stub = [
    "",
    f"### {today_iso} {apm} — {focus_short}",
    "",
    "- (accumulate today's completed items here; EOD batch closes them)",
    "",
]
insert_at = done_idx + 1
if insert_at < len(lines) and lines[insert_at] == "":
    insert_at += 1
lines = lines[:insert_at] + new_done_stub + lines[insert_at:]

path.write_text("\n".join(lines), encoding="utf-8")
print("EDIT_OK")
PYEOF

[ "$(tail -c 200 /dev/stdout 2>/dev/null; echo)" ] || true  # noop guard
ok "edits applied to $DATED_FILE"

# ─── 6. Diff gate ────────────────────────────────────────────────────────────
DIFF_OUT=$(diff "$PRE_EDIT_SNAPSHOT" "$DATED_FILE" || true)

# Which line-number ranges in the ORIGINAL file are we allowed to have touched?
# We derive them fresh from the pre-edit snapshot.
LU_LINE=$(grep -n '^\*\*Last updated:\*\*' "$PRE_EDIT_SNAPSHOT" | head -1 | cut -d: -f1)
CS_LINE=$(grep -n '^\*\*Current ship state:\*\*' "$PRE_EDIT_SNAPSHOT" | head -1 | cut -d: -f1)
NEXT_UP_LINE=$(grep -n '^## Next up$' "$PRE_EDIT_SNAPSHOT" | head -1 | cut -d: -f1)
DONE_LINE=$(grep -n '^## Done this session$' "$PRE_EDIT_SNAPSHOT" | head -1 | cut -d: -f1)
# End of Next up section = the next `## ` after NEXT_UP_LINE
NEXT_UP_END=$(awk -v s="$NEXT_UP_LINE" 'NR>s && /^## / {print NR-1; exit}' "$PRE_EDIT_SNAPSHOT")

# Parse diff hunks: lines matching `^[0-9,]+[acd][0-9,]+$` in unified/traditional diff.
# We use traditional (unified would need -u). `diff` default gives us "NaZM" style.
# Extract left-hand (pre-edit) line ranges.
LEFT_RANGES=$(echo "$DIFF_OUT" | grep -E '^[0-9,]+[acd][0-9,]+$' | sed 's/[acd].*//')

drift=0
while IFS= read -r range; do
    [ -z "$range" ] && continue
    start=$(echo "$range" | cut -d, -f1)
    end=$(echo "$range" | cut -d, -f2)
    [ "$end" = "$start" ] || [ -n "$end" ] || end=$start
    [ -z "$end" ] && end=$start

    # Check that [start,end] falls inside one of the permitted regions:
    #   {LU_LINE}                              (single line)
    #   {CS_LINE}                              (single line, only if ship_state provided)
    #   [NEXT_UP_LINE+1, NEXT_UP_END]          (Next up body)
    #   {DONE_LINE+1}                          (insertion point right after Done header)
    permitted=0

    if [ "$start" = "$LU_LINE" ] && [ "$end" = "$LU_LINE" ]; then permitted=1; fi
    if [ -n "$SHIP_STATE" ] && [ "$start" = "$CS_LINE" ] && [ "$end" = "$CS_LINE" ]; then permitted=1; fi
    if [ "$start" -gt "$NEXT_UP_LINE" ] && [ "$end" -le "$NEXT_UP_END" ]; then permitted=1; fi
    # Done insertion: `diff` reports this as an insertion at line DONE_LINE+1 or as
    # a range starting at DONE_LINE+1 (the blank line that already exists there).
    if [ "$start" -ge "$DONE_LINE" ] && [ "$end" -le "$((DONE_LINE + 2))" ]; then permitted=1; fi

    if [ "$permitted" -eq 0 ]; then
        echo "❌ DRIFT: diff hunk at pre-edit lines $start,$end is OUTSIDE permitted regions" >&2
        echo "   Permitted: LU=$LU_LINE, CS=$CS_LINE (only if ship_state), Next up=($NEXT_UP_LINE,$NEXT_UP_END], Done=[$DONE_LINE,$((DONE_LINE+2))]" >&2
        drift=1
    fi
done <<< "$LEFT_RANGES"

if [ "$drift" -ne 0 ]; then
    cp "$PRE_EDIT_SNAPSHOT" "$DATED_FILE"
    fail "diff gate REJECTED — rolled back $DATED_FILE" 4
fi

ok "diff gate passed (all hunks inside permitted regions)"

# ─── 7. Post-edit re-audit ──────────────────────────────────────────────────
POST_SECTIONS=$(grep -c '^## ' "$DATED_FILE")
POST_OPEN=$(grep -c '^- \[ \]' "$DATED_FILE" || echo 0)
POST_DONE=$(grep -c '^- \[x\]' "$DATED_FILE" || echo 0)

# Expected delta: new-day setup adds N `- [ ]` items in Next up (where N =
# len(next_up), or 1 if empty because we insert the placeholder). It never
# removes items. Section count unchanged. Done items unchanged.
EXPECTED_ADDED=$(echo "$NEXT_UP_JSON" | jq 'if length == 0 then 1 else length end')
EXPECTED_OPEN=$((PRE_OPEN + EXPECTED_ADDED))

[ "$POST_SECTIONS" = "$PRE_SECTIONS" ] || fail "section count changed: $PRE_SECTIONS → $POST_SECTIONS" 4
[ "$POST_DONE" = "$PRE_DONE" ]         || fail "done-item count changed: $PRE_DONE → $POST_DONE" 4
[ "$POST_OPEN" = "$EXPECTED_OPEN" ]    || fail "open-item count off: expected $EXPECTED_OPEN (was $PRE_OPEN + $EXPECTED_ADDED), got $POST_OPEN" 4

ok "re-audit passed: sections=$POST_SECTIONS open=$POST_OPEN done=$POST_DONE (Δopen=+$EXPECTED_ADDED)"

# ─── 8. Mirror ──────────────────────────────────────────────────────────────
cp "$DATED_FILE" "$MIRROR_FILE"
SHA_DATED=$(shasum -a 256 "$DATED_FILE" | cut -d' ' -f1)
SHA_MIRROR=$(shasum -a 256 "$MIRROR_FILE" | cut -d' ' -f1)
[ "$SHA_DATED" = "$SHA_MIRROR" ] || fail "mirror shasum mismatch" 5
ok "mirror synced (sha256=${SHA_DATED:0:12})"

# ─── 9. Brief ────────────────────────────────────────────────────────────────
jq -n \
  --arg dated_file "$DATED_FILE" \
  --arg mirror_file "$MIRROR_FILE" \
  --arg today "$TODAY_ISO $APM" \
  --arg sha "$SHA_DATED" \
  --arg upstream "${LOCAL_SHA:0:8}" \
  --argjson pre_sections "$PRE_SECTIONS" \
  --argjson pre_open "$PRE_OPEN" \
  --argjson pre_done "$PRE_DONE" \
  --argjson post_sections "$POST_SECTIONS" \
  --argjson post_open "$POST_OPEN" \
  --argjson post_done "$POST_DONE" \
  --argjson added "$EXPECTED_ADDED" \
  --arg focus_short "$FOCUS_SHORT" \
  '{
     status: "ok",
     dated_file: $dated_file,
     mirror_file: $mirror_file,
     today: $today,
     canonical_from: ("origin/main@" + $upstream),
     sha256: $sha,
     audit: {
       pre:  { sections: $pre_sections, open: $pre_open, done: $pre_done },
       post: { sections: $post_sections, open: $post_open, done: $post_done },
       delta_open: $added
     },
     focus_short: $focus_short,
     next_action: "Brief Pete with the audit summary + proposed first action, then wait for go-ahead."
   }'
