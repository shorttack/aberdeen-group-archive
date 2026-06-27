#!/usr/bin/env python3
"""
write_mx_verdicts_to_studies_v1.py

Writes the computed Pass C v7 verdicts for the 13 scorable -mx studies into
_master_studies.csv:
  - prescience            <- computed enum (high/medium/low/not-applicable)
  - prescience_rationale  <- AUTHORED text preserved, computed audit note APPENDED

VERDICT RULE (locked 2026-06-27): used = integer scores 1..5 only (excludes 0
'cannot-assess', -1 parse-fail, blanks, any other sentinel). No min-count gate.
  mean>=3.5 high; >=2.0 medium; >0 obs but <2.0 low; 0 obs -> not-applicable.

Audit-note format appended to the authored rationale:
  "  | Pass C v7 (2026-06-27): <enum>, mean <m> over <n_used> assessable
   prediction(s); <n_zero> market-data obs scored 0=cannot-assess & excluded,
   <n_neg> parse-fail/excluded. Rule: scores<1 excluded, no min gate."

Only the 13 listed -mx study_ids are touched. All other 1491 rows pass through
verbatim. Backup + QUOTE_ALL + row-parity. Dry-run default; --commit to write.
Prints the enum delta (authored -> computed) for each study.
"""
import csv
import datetime
import shutil
import sys
from collections import defaultdict
from pathlib import Path

ARCH = Path.home() / "Desktop" / "Archive"
REPO = ARCH / "aberdeen-group-archive"
SCORES = ARCH / "pass_c_v7_mx_tier.csv"
STUDIES = REPO / "_master_studies.csv"

STUDIES_COLS = [
    "study_id", "title", "author", "date", "type", "subject_domain",
    "methodology", "source_file", "abstract", "license", "importance",
    "importance_rationale", "relevance", "relevance_rationale",
    "prescience", "prescience_rationale",
]

commit = "--commit" in sys.argv


def parse_int(raw):
    try:
        return int(str(raw).strip())
    except (ValueError, TypeError):
        return None


def verdict(vals):
    used = [v for v in vals if v is not None and 1 <= v <= 5]
    n_zero = sum(1 for v in vals if v == 0)
    n_neg = sum(1 for v in vals if v is not None and v < 0)
    if not used:
        return "not-applicable", None, 0, n_zero, n_neg
    m = sum(used) / len(used)
    v = "high" if m >= 3.5 else "medium" if m >= 2.0 else "low"
    return v, round(m, 2), len(used), n_zero, n_neg


def main():
    # compute verdicts from the v7 batch (-mx studies only)
    by = defaultdict(list)
    with open(SCORES, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            by[r["study_id"]].append(parse_int(r["prescience_score"]))
    computed = {}
    for sid, vals in by.items():
        computed[sid] = verdict(vals)

    with open(STUDIES, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        hdr = reader.fieldnames
        rows = list(reader)
    if hdr != STUDIES_COLS:
        sys.exit(f"FATAL: studies header mismatch.\n have: {hdr}\n want: {STUDIES_COLS}")

    touched = 0
    print(f"{'study_id':46s} {'authored':10s} -> {'computed':14s} {'mean':5s} {'used':4s}")
    print("-" * 92)
    for r in rows:
        sid = r["study_id"]
        if sid not in computed:
            continue
        v, m, nu, nz, nn = computed[sid]
        authored = r.get("prescience", "")
        note = (f"  | Pass C v7 (2026-06-27): {v}, "
                f"mean {m} over {nu} assessable prediction{'s' if nu != 1 else ''}; "
                f"{nz} market-data obs scored 0=cannot-assess & excluded, "
                f"{nn} parse-fail/excluded. Rule: scores<1 excluded, no min gate.")
        # idempotency guard: don't double-append if already present
        existing = r.get("prescience_rationale", "")
        if "Pass C v7 (2026-06-27)" not in existing:
            r["prescience_rationale"] = existing + note
        r["prescience"] = v
        touched += 1
        flag = "" if authored == v else "  <-- ENUM CHANGED"
        print(f"{sid:46s} {authored:10s} -> {v:14s} {str(m):5s} {nu:<4d}{flag}")

    print(f"\nstudies touched: {touched} (expected 13)")
    print(f"mode: {'COMMIT' if commit else 'DRY-RUN'}")
    if touched != 13:
        sys.exit(f"FATAL: expected to touch 13 studies, touched {touched}. Aborting.")

    if not commit:
        print("\nDRY-RUN only — pass --commit to write.")
        return

    ts = datetime.datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
    bak = STUDIES.with_suffix(f".csv.bak_mx_verdicts_{ts}")
    shutil.copy2(STUDIES, bak)
    print(f"\nBackup: {bak}")

    with open(STUDIES, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=STUDIES_COLS, quoting=csv.QUOTE_ALL)
        w.writeheader()
        w.writerows(rows)

    with open(STUDIES, newline="", encoding="utf-8") as f:
        back = list(csv.DictReader(f))
    assert len(back) == len(rows), f"parity FAIL: wrote {len(rows)}, read {len(back)}"
    print(f"Wrote {STUDIES}: {len(rows)} rows. Read-back parity PASS.")


if __name__ == "__main__":
    main()
