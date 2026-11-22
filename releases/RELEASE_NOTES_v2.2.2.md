# Release v2.2.2 — FLORIDA evidence intake, October–November 2026

**November 22, 2026**

A content release. It ships everything added to the FLORIDA study since v2.2.1 (September 6, 2026) and one correction to the master tables. No published paper was rewritten for this release. Per the archive's sweep rule, new evidence is logged in `FLORIDA/PENDING-CHANGES.md` and applied to the papers in scheduled sweeps, not one item at a time.

## Primary sources added

- **1993 Leon County grand jury presentment.** A compressed, searchable copy, with a page-marked OCR transcript and a findings note (`PRESENTMENT-1993-FINDINGS.md`). Produced by the Leon County Clerk under request P022996-082026, round 1. The two Clerk letters reporting "no information found" are also filed.
- **E.D.S. Federal Corp. v. State of Florida, DHRS, and Gerald A. Lewis, as Comptroller,** Leon County Circuit Court, Case No. 1992 CA 003618. The original complaint of August 21, 1992, with Exhibits A–E. These include the standard contract, the October 4, 1991 MOU and Amendment One, and RFP 88-74-BC §§ 7.30–7.32. The release includes the page-marked OCR transcript, the docket OCR text and a findings note (`EDS-v-HRS-1992-COMPLAINT-FINDINGS.md`). The 245 MB scanned PDF and its searchable copy are kept locally, not on GitHub, because of GitHub's file-size limits.
- **DCF records request P257878-072926.** The Department of Children and Families procurement file for ITN 03F12GC1, *ACCESS Florida System Replacement* (June 22, 2012 – March 8, 2013): 22 born-digital PDFs, 207 pages, with a SHA-256 manifest and the processing run.

## Working papers added

- `CAPACITY-OVER-TIME-BRIEF-2026-10-29.md` and *FLORIDA System — Processor Capacity Over Time, 1988–1998*. These follow every processor the record places under the FLORIDA System.

## Corrections

- **Study 5b4524: IMS, not DB2.** The masters (`_master_studies.csv`, `_master_tech_studies.csv`, `_master_observations.csv`) now name IBM IMS as the database, replacing DB2. This was applied October 28, 2026 as PENDING-CHANGES row 49.
- **Full pending-changes sweep of October 28, 2026.** Rows 4–78 were applied to the GitHub copies. Mac-only targets are listed in § 5 of PENDING-CHANGES and await a second pass.
- **`FLORIDA/SOURCES.md` recounted.** The total rose from 140 to 145 sources. The administrative-record count had not been updated for four entries added in September–October.

## The pending-changes register

`FLORIDA/PENDING-CHANGES.md` now has 42 pending items, logged for the next sweep. Rows 79–89 come from the capacity brief, rows 90–107 from the 1992 complaint and rows 111–119 from the DCF production. Row 120 is the testimony-date question: the memoir layer dates Kastner's Tallahassee protest testimony to c. 1990–91, but the DOAH record places it between December 1988 and early 1989. It awaits Kastner's confirmation. GitHub first recorded it as row 79; it was renumbered when the two copies of the register were merged.

**OCR caution.** Rows marked † rest on OCR text that has not yet been checked against the page images. The complaint transcript passed the technical checks of its OCR run, but it is not yet verified for citation. Quote from the page image, not the transcript, until that check is done.

## Other

- Skills: the workload-4 local-model bakeoff verdict was updated on October 13, 2026. Run outputs were removed from `_skills/local-model-upgrade-gates/assets/fixtures/`, because skill folders hold no run outputs. The `florida-changes` skill was revised.
- `AG-13256-vol1.pdf` (65 MB) is no longer tracked. It is kept locally.
