# Manifest — Kastner IT Research Archive v2.2.2

**Repository:** `shorttack/aberdeen-group-archive`
**Release:** [Aberdeen Archive v2.2.2](https://github.com/shorttack/aberdeen-group-archive/releases/tag/v2.2.2), published 2026-11-22T14:37:17Z
**Tag:** `v2.2.2`, an annotated tag object `cd1dc24ca4d395a60e5f29818c1c0ed81eb72802`, created 2026-11-22T14:37:14Z
**Commit:** `6156de1d3378ef042d3e6a565de9fc492bde8736`, "FLORIDA: Oct-Nov 2026 evidence intake; release v2.2.2"
**Previous release:** v2.2.1, September 6, 2026. 14 commits and 300 changed files separate the two tags.
**Zenodo:** concept DOI `10.5281/zenodo.20245076`, all versions. `.zenodo.json` and `CITATION.cff` are at version 2.2.2, date-released 2026-11-22. The Zenodo record for v2.2.2 was not checked when this manifest was written.

## Contents

- 12,404 files, 807,967,111 bytes, as served in GitHub's v2.2.2 tarball. That count equals the number of files in the git tree at the tag, so nothing was left out.
- Per-file identities are in `MANIFEST_v2.2.2.sha256`: one line per file, in `shasum -a 256 -c` format, with paths relative to the repository root, sorted bytewise.
- SHA-256 of `MANIFEST_v2.2.2.sha256`: `bf1d917a6f967b8b1e63b5ae8ed6831b0e241105a60844baede7943f946b8fb4`

| Top-level folder | Files |
|---|--:|
| other-authors | 5,492 |
| kastner-author | 4,805 |
| FLORIDA | 377 |
| aberdeen-group-inc | 320 |
| scripts | 239 |
| project_examples | 175 |
| reports | 93 |
| Archive | 44 |
| _local_backups | 30 |
| releases | 13 |
| _skills | 13 |
| everything else | 803 |

## Not in the release

These are git-ignored and kept only on the Mac:
- `FLORIDA/PDFs/courts/EDS-v-HRS-1992CA003618-complaint-1992-08-21.pdf`, the 245 MB scan. It is also preserved, with its searchable copy, under `/Users/scott/Desktop/Memoirs/FLORIDA-documents/run_20261121t161910Z_prod/`, receipt `pres_20261121T230408Z`.
- `FLORIDA/PDFs/**/*_ocr.pdf`, the searchable copies.
- `FLORIDA/PDFs/auditor-general/AG-13256-vol1.pdf`, 65 MB.

## How the release was made and checked

1. GitHub had one commit the Mac lacked, `cd9bc10d` (the October 28 PENDING-CHANGES row 79, on the testimony date). It was brought in by fast-forward. The Mac's own row 79 is the capacity brief, so GitHub's row was renumbered 120. The Mac's copy of `PENDING-CHANGES.md` before the merge had SHA-256 `0d8d5857…e296`; the merged copy has `df7214d6…9aa6`.
2. `scripts/eod.sh --commit --archive-only --release 2.2.2` updated the version metadata, committed 355 files (53,533 insertions, 2,161 deletions), pushed `cd9bc10d..6156de1d`, tagged `v2.2.2` and published the release. GitHub reported that the push bypassed the "changes must be made through a pull request" rule on `main`.
3. eod.sh's remote checks all passed. The archive README has no banned phrases. No private paths are in the tree. `.zenodo.json` reads 2.2.2 on GitHub. The wiki's SETUP and USER_GUIDE pages have no brand references.
4. This manifest was computed from GitHub's v2.2.2 tarball, not from the Mac. Then `shasum -a 256 -c MANIFEST_v2.2.2.sha256` was run in `/Users/scott/Desktop/Archive/aberdeen-group-archive` on the Mac. All 12,404 files matched (12,404 OK, 0 failed). So the Mac copy, the GitHub tag and this manifest agree byte for byte.

## Not claimed

- That Zenodo minted the v2.2.2 version DOI. Check the concept DOI's versions list.
- That an independent backup of the release exists, beyond GitHub and the Mac.
- That OCR text in this release is citation-grade. See the OCR caution in `RELEASE_NOTES_v2.2.2.md`.

This manifest and its `.sha256` file were written after the tag, so they are not part of v2.2.2. They go to GitHub in the next end-of-day batch.
