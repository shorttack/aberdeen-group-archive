#!/usr/bin/env python3
"""
ingest_dectp_press_conf_v2.py
Finish-only pass for the DECtp Press Conference 1988 ingest.

The master CSV row was already written by v1 (1434→1435, backup taken).
This script ONLY copies the source files to their archive destinations.
It does NOT touch _master_studies.csv.

What it copies:
  SRC_DIR/DECtp-NYC-1988-07-cleaned.md
    → DEST/source/DECtp-NYC-1988-07-cleaned.md
  SRC_DIR/DECtp 1988 tps rdbms.png
    → DEST/media/DECtp 1988 tps rdbms.png
  SRC_DIR/DECtp-flatfiles-tps-1988-08.19.41.png
    → DEST/media/DECtp-flatfiles-tps-1988-08.19.41.png
  SRC_DIR/DECtp 1988 tps flat files.png
    → DEST/media/DECtp 1988 tps flat files.png
  SRC_DIR/DECtp 1988 price-performance.png
    → DEST/media/DECtp 1988 price-performance.png
  SRC_DIR/DECtp 1988 avg system cost.png
    → DEST/media/DECtp 1988 avg system cost.png

NOTE: dectp-press-conf-1988.md (the study with observations) is already in the
repo at kastner-author/1988-dectp-press-conference-nyc/dectp-press-conf-1988.md
— no copy needed for that file.

Usage:
  python3 ~/Desktop/Archive/scripts/ingest_dectp_press_conf_v2.py           # dry-run
  python3 ~/Desktop/Archive/scripts/ingest_dectp_press_conf_v2.py --commit  # apply
"""

import sys, shutil
from pathlib import Path

# ── Source (ingest queue) ─────────────────────────────────────────────────────
SRC_DIR = Path.home() / "Desktop/Archive/_ingest_queue/DECtp-press-conference-with-images"

SRC_MD = SRC_DIR / "DECtp-NYC-1988-07-cleaned.md"

SRC_IMAGES = [
    SRC_DIR / "DECtp 1988 tps rdbms.png",
    SRC_DIR / "DECtp-flatfiles-tps-1988-08.19.41.png",
    SRC_DIR / "DECtp 1988 tps flat files.png",
    SRC_DIR / "DECtp 1988 price-performance.png",
    SRC_DIR / "DECtp 1988 avg system cost.png",
]

# ── Destination (archive repo working tree) ───────────────────────────────────
DEST_DIR    = Path.home() / "Desktop/Archive/aberdeen-group-archive" \
              / "kastner-author/1988-dectp-press-conference-nyc"
DEST_MEDIA  = DEST_DIR / "media"
DEST_SOURCE = DEST_DIR / "source"

ALL_COPIES = [(SRC_MD, DEST_SOURCE / SRC_MD.name)] + \
             [(img, DEST_MEDIA / img.name) for img in SRC_IMAGES]

def main():
    commit = "--commit" in sys.argv
    print(f"Mode: {'COMMIT' if commit else 'DRY-RUN'}")
    print()

    # Verify all source files exist
    missing = [src for src, _ in ALL_COPIES if not src.exists()]
    if missing:
        print("ABORT: missing source files:")
        for m in missing:
            print(f"  {m}")
        sys.exit(1)
    print(f"Source files OK: {len(ALL_COPIES)} files found")
    print()

    # Show what will be copied
    print("=== File copies ===")
    for src, dst in ALL_COPIES:
        status = "EXISTS" if dst.exists() else "new"
        print(f"  [{status}] {src.name}")
        print(f"        → {dst}")
    print()

    if not commit:
        print("DRY-RUN complete. Pass --commit to write.")
        return

    # Create destination directories
    DEST_MEDIA.mkdir(parents=True, exist_ok=True)
    DEST_SOURCE.mkdir(parents=True, exist_ok=True)

    # Copy files
    copied = 0
    for src, dst in ALL_COPIES:
        shutil.copy2(src, dst)
        print(f"Copied: {src.name} → {dst.parent.name}/")
        copied += 1

    print()
    print(f"=== Done: {copied}/{len(ALL_COPIES)} files copied ===")
    print()
    print("Next steps:")
    print("  1. git add kastner-author/1988-dectp-press-conference-nyc/")
    print("     git commit -m 'Add DECtp 1988 source transcript + 5 benchmark images'")
    print("     git push")
    print("  2. Run Phase 1+2 to rebuild DuckDB:")
    print("     python3 ~/Desktop/Archive/scripts/build/01_load_csvs_v2.py \\")
    print("       --archive ~/Desktop/Archive/aberdeen-group-archive \\")
    print("       --wiki ~/Repos/kastner-aberdeen-wiki")
    print("     python3 ~/Desktop/Archive/scripts/build/02_build_data_layer_v4.py \\")
    print("       --wiki ~/Repos/kastner-aberdeen-wiki")
    print("  3. Run Phases 3-5 if kw ask should find this study.")
    print("  4. EOD batch commit of _master_studies.csv via kastner-github skill.")

if __name__ == "__main__":
    main()
