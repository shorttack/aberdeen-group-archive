#!/usr/bin/env python3
"""
build_mx_pass_c_manifest_v1.py

Builds a Pass C input manifest containing ONLY the scorable -mx observations
(the 50 expand-pc-deals -mx packages staged into the live masters 2026-06-27).

Scope logic mirrors run_prescience_pass_c_v7.py:
  • select obs whose obs_id contains "-mx-OBS-"
  • EXCLUDE obs whose parent study has prescience in {not-applicable, n/a, na}
    (v7 would skip these anyway via --skip-not-applicable; we exclude them here
     so the manifest count == the actual API work count)

Output schema is the full 17-col _master_observations.csv schema (QUOTE_ALL),
which is a superset of what v7's load_master_obs / scorer reads.

Dry-run by default. Pass --commit to write the manifest CSV.

Usage:
  python3 build_mx_pass_c_manifest_v1.py            # dry-run: print counts
  python3 build_mx_pass_c_manifest_v1.py --commit   # write the manifest
"""
import csv
import sys
from pathlib import Path

ARCH = Path.home() / "Desktop" / "Archive" / "aberdeen-group-archive"
OBS = ARCH / "_master_observations.csv"
STUD = ARCH / "_master_studies.csv"
OUT = Path.home() / "Desktop" / "Archive" / "pass_c_mx_manifest_v1.csv"

NA_VALUES = {"not-applicable", "n/a", "na"}
MX_MARKER = "-mx-OBS-"

commit = "--commit" in sys.argv


def main():
    # study -> prescience verdict
    verdict = {}
    with open(STUD, newline="") as f:
        for r in csv.DictReader(f):
            verdict[r["study_id"]] = (r.get("prescience") or "").strip().lower()

    with open(OBS, newline="") as f:
        reader = csv.DictReader(f)
        header = reader.fieldnames
        rows = list(reader)

    mx_rows = [r for r in rows if MX_MARKER in r["obs_id"]]
    scorable = [r for r in mx_rows if verdict.get(r["study_id"], "") not in NA_VALUES]
    excluded = len(mx_rows) - len(scorable)

    studies_in_manifest = sorted({r["study_id"] for r in scorable})

    print(f"obs master:                  {len(rows)} rows, {len(header)} cols")
    print(f"-mx obs total:               {len(mx_rows)}")
    print(f"-mx excluded (not-applic.):  {excluded}")
    print(f"-mx scorable -> manifest:    {len(scorable)}")
    print(f"distinct scorable studies:   {len(studies_in_manifest)}")
    print(f"mode:                        {'COMMIT' if commit else 'DRY-RUN'}")
    print(f"output path:                 {OUT}")

    if not commit:
        print("\nDRY-RUN only — pass --commit to write the manifest.")
        return

    with open(OUT, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=header, quoting=csv.QUOTE_ALL)
        w.writeheader()
        w.writerows(scorable)

    # read-back parity
    with open(OUT, newline="") as f:
        back = list(csv.DictReader(f))
    assert len(back) == len(scorable), f"parity FAIL: wrote {len(scorable)}, read {len(back)}"
    print(f"\nWrote {len(scorable)} rows. Read-back parity PASS.")


if __name__ == "__main__":
    main()
