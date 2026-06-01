#!/usr/bin/env bash
#
# download_aberdeen_pdfs.sh
#
# Downloads all 469 Aberdeen.com PDFs harvested from the Wayback Machine
# (163 from Oct-1998–Jan-2004 + 306 from Jan-2004–Jun-2007) to your Mac
# Desktop, with polite pacing to comply with Wayback Machine usage norms.
#
# Settings (chosen on 2026-05-21):
#   • 5-second pause between downloads (≈40 min total)
#   • flat folder ~/Desktop/aberdeen_pdfs/
#   • collisions resolved by prefixing the Wayback capture year (e.g. 2003_sap.pdf)
#   • 3 retries with 10s / 30s / 60s backoff on transient failures
#   • HTTP 429 (rate-limit) triggers an extra 120-second cool-down
#   • resumable: skips files that already exist
#
# USAGE:
#   1. Put both NOT_FOUND CSVs on your Desktop:
#        ~/Desktop/aberdeen_pdfs_NOT_FOUND.csv             (163 rows, 1998–2004)
#        ~/Desktop/aberdeen_2004_2007_NOT_FOUND.csv        (306 rows, 2004–2007)
#   2. chmod +x ~/Desktop/download_aberdeen_pdfs.sh
#   3. ~/Desktop/download_aberdeen_pdfs.sh
#
# Output:
#   ~/Desktop/aberdeen_pdfs/                  the PDFs
#   ~/Desktop/aberdeen_pdfs/_download_log.csv timestamp,status,bytes,saved_as,url
#   ~/Desktop/aberdeen_pdfs/_errors.csv       any URLs that failed after all retries

set -u  # error on unset vars; we don't use -e so one bad URL doesn't kill the run

# ---------- config ----------
DESKTOP="$HOME/Desktop"
OUTDIR="$DESKTOP/aberdeen_pdfs"
PAUSE=5                       # seconds between successful downloads
RETRY_WAITS=(10 30 60)        # backoff between retry attempts
RATELIMIT_COOLDOWN=120        # extra wait after an HTTP 429
TIMEOUT=90                    # per-request seconds (curl --max-time)
CONNECT_TIMEOUT=20            # connect-phase seconds (curl --connect-timeout)
USER_AGENT="AberdeenArchiveHarvester/1.0 (research; contact: pete.kastner@bluebridgegrp.com)"

CSV_LIST=(
  "$DESKTOP/aberdeen_pdfs_NOT_FOUND.csv"
  "$DESKTOP/aberdeen_2004_2007_NOT_FOUND.csv"
)

# ---------- prep ----------
mkdir -p "$OUTDIR"
LOG="$OUTDIR/_download_log.csv"
ERR="$OUTDIR/_errors.csv"
[[ -f "$LOG" ]] || echo "timestamp,status,bytes,saved_as,url" > "$LOG"
[[ -f "$ERR" ]] || echo "timestamp,filename,url,reason" > "$ERR"

# Verify CSVs exist
for csv in "${CSV_LIST[@]}"; do
  if [[ ! -f "$csv" ]]; then
    echo "ERROR: missing input file: $csv" >&2
    echo "Place both NOT_FOUND CSVs on your Desktop, then re-run." >&2
    exit 1
  fi
done

# ---------- build the list of (filename, year, url) triples ----------
# Both CSVs have header: filename,original_url,wayback_url
# We extract: <filename>\t<year-from-wayback-ts>\t<wayback_url>
WORKLIST="$(mktemp -t aberdeen.XXXXXX)"
trap 'rm -f "$WORKLIST"' EXIT

awk -F',' '
  FNR == 1 { next }                       # skip header of EACH file
  $1 == ""  { next }                       # skip blank lines
  {
    fn  = $1
    url = $3
    # Strip CR (CSVs are CRLF per RFC 4180) and any whitespace
    gsub(/[\r\n[:space:]]+$/, "", fn)
    gsub(/[\r\n[:space:]]+$/, "", url)
    # Wayback URL pattern: https://web.archive.org/web/YYYYMMDD...id_/http://...
    if (match(url, /web\/[0-9]{4}/)) {
      year = substr(url, RSTART+4, 4)
    } else {
      year = "0000"
    }
    printf "%s\t%s\t%s\n", fn, year, url
  }' "${CSV_LIST[@]}" > "$WORKLIST"

TOTAL=$(wc -l < "$WORKLIST" | tr -d ' ')
echo "----------------------------------------------------------"
echo "Aberdeen PDF batch download"
echo "  input files : ${#CSV_LIST[@]} CSV(s)"
echo "  URLs queued : $TOTAL"
echo "  output dir  : $OUTDIR"
echo "  pause       : ${PAUSE}s between downloads"
echo "  retries     : ${#RETRY_WAITS[@]} (waits: ${RETRY_WAITS[*]})"
echo "  est. time   : ~$(( TOTAL * (PAUSE + 2) / 60 )) min (best case)"
echo "----------------------------------------------------------"

# ---------- main loop ----------
i=0
ok=0
skipped=0
failed=0

while IFS=$'\t' read -r filename year url; do
  i=$((i+1))

  # Resolve target filename (with year prefix if a different file already exists there)
  target="$OUTDIR/$filename"
  if [[ -e "$target" ]]; then
    # Same filename already on disk — is this URL likely the same file or a collision?
    # Conservative: always prefix with year for any new download whose plain name exists.
    target="$OUTDIR/${year}_${filename}"
  fi
  # If even the year-prefixed target exists and is non-empty, treat as already done.
  if [[ -s "$target" ]]; then
    skipped=$((skipped+1))
    printf "[%3d/%d] SKIP  %s (already on disk)\n" "$i" "$TOTAL" "$(basename "$target")"
    continue
  fi

  # Try with backoff
  status=""
  bytes=0
  attempt=0
  max_attempts=$(( 1 + ${#RETRY_WAITS[@]} ))
  while (( attempt < max_attempts )); do
    attempt=$((attempt+1))
    # -w writes status + size on a single line; -f makes 4xx/5xx an error so $? is nonzero
    response=$(curl -sS -L \
                  --max-time "$TIMEOUT" \
                  --connect-timeout "$CONNECT_TIMEOUT" \
                  -A "$USER_AGENT" \
                  -w 'HTTP_CODE:%{http_code} SIZE:%{size_download}' \
                  -o "$target.partial" \
                  "$url" 2>&1) || true
    http_code=$(printf '%s' "$response" | sed -nE 's/.*HTTP_CODE:([0-9]+).*/\1/p' | tail -1)
    size=$(printf '%s' "$response" | sed -nE 's/.*SIZE:([0-9]+).*/\1/p' | tail -1)
    http_code="${http_code:-000}"
    size="${size:-0}"

    if [[ "$http_code" == "200" && "$size" -gt 0 ]]; then
      # Verify it actually starts with %PDF — Wayback occasionally returns an HTML error page with 200
      magic=$(head -c 5 "$target.partial" 2>/dev/null || true)
      if [[ "$magic" == "%PDF-" ]] || [[ "$magic" == "%PDF" ]]; then
        mv "$target.partial" "$target"
        status="OK"
        bytes="$size"
        break
      else
        rm -f "$target.partial"
        status="NOT_PDF_HTTP_${http_code}"
      fi
    elif [[ "$http_code" == "429" ]]; then
      rm -f "$target.partial"
      status="RATE_LIMITED"
      printf "[%3d/%d] 429 rate-limited; cooling down %ds...\n" "$i" "$TOTAL" "$RATELIMIT_COOLDOWN"
      sleep "$RATELIMIT_COOLDOWN"
    else
      rm -f "$target.partial"
      status="HTTP_${http_code}"
    fi

    if (( attempt < max_attempts )); then
      wait_s="${RETRY_WAITS[$((attempt-1))]}"
      printf "[%3d/%d] retry %d/%d after %ds (last: %s) — %s\n" \
        "$i" "$TOTAL" "$attempt" "$((max_attempts-1))" "$wait_s" "$status" "$filename"
      sleep "$wait_s"
    fi
  done

  ts=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
  if [[ "$status" == "OK" ]]; then
    ok=$((ok+1))
    printf "[%3d/%d] OK    %s (%s bytes)\n" "$i" "$TOTAL" "$(basename "$target")" "$bytes"
    echo "$ts,OK,$bytes,$(basename "$target"),$url" >> "$LOG"
  else
    failed=$((failed+1))
    printf "[%3d/%d] FAIL  %s (%s)\n" "$i" "$TOTAL" "$filename" "$status"
    echo "$ts,FAIL,$bytes,$(basename "$target"),$url" >> "$LOG"
    echo "$ts,$filename,$url,$status" >> "$ERR"
  fi

  # Polite pause before next URL (skip after the very last one)
  if (( i < TOTAL )); then
    sleep "$PAUSE"
  fi
done < "$WORKLIST"

echo "----------------------------------------------------------"
echo "DONE."
echo "  attempted : $TOTAL"
echo "  ok        : $ok"
echo "  skipped   : $skipped (already on disk from a prior run)"
echo "  failed    : $failed"
echo "  log       : $LOG"
[[ "$failed" -gt 0 ]] && echo "  errors    : $ERR"
echo "----------------------------------------------------------"
