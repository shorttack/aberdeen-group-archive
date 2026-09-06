# Release v2.2.1 — FLORIDA System archive, actually included

**September 6, 2026**

## What this release corrects

Release v2.2.0, cut earlier today, carried release notes describing the addition of the FLORIDA System study to this archive. **Those notes were accurate about the work and wrong about the release.** The FLORIDA directory had not been moved into the repository when v2.2.0 was tagged, so that release contains its own release notes, a Zenodo metadata bump, and nothing else. The Zenodo record generated from v2.2.0 describes content that tag does not hold.

v2.2.0 is not withdrawn or rewritten — this archive does not rewrite published history. It is superseded by this release, which contains what v2.2.0 described.

The error is worth recording rather than quietly fixing, and it is the same error the FLORIDA study's own README documents in another form: **a statement that work was completed is a claim, not a fact, and it has to be verified against the artifact.** The release notes asserted a directory was added. Nobody checked `git status` before tagging. That is the whole failure.

## What v2.2.1 contains

The FLORIDA System study, 59 files, 238 MB, as `FLORIDA/`.

### The study

A primary-source reconstruction of Florida's 1988–1996 integrated public-assistance eligibility procurement — RFP 88-74-BC, the EDS award, the IBM subcontract, the collapse, and the $42.8 million settlement. Eight analytical papers plus the evidentiary apparatus behind them.

The study belongs in this archive by provenance: it began as a Kastner Aberdeen project on Unisys, the bidder that lost RFP 88-74-BC by 4.4 points and later ran the winner's programming shop under a contract that reached roughly $58.7 million.

### Primary sources

Auditor General Reports 11178 (1989), 11619 (1991), 12061 (1993), 12581 (1995), 13043 (1998), 13256 (1998), and 13287 (1998), plus eight freely published later reports. **None of the pre-2000 reports is available online.** They were supplied by the Auditor General's office in August and September 2026 and OCR'd locally at 300 dpi with reading-order text preserved. Also included: the Division of Administrative Hearings docket and records-disposition documents for Case 88-002942, and a mirrored copy of *State, DHRS v. E.D.S. Federal Corp.*, 631 So. 2d 353.

### Four P1 corrections applied to the papers

- **The RFP did specify a quantified performance standard.** The archive previously inferred from the silence of the appellate and protest records that RFP 88-74-BC set no numeric performance requirement. That inference was wrong. Report 12061 ¶51 documents a contractual requirement that response times fall between one and eight seconds for at least 95 percent of the time, sampled every fifteen minutes on a randomly selected day each month at randomly selected workstations, with availability of at least 97 percent during normal working hours over any consecutive thirty-day period. The structural argument moves from "no standard existed" to "the standard existed and its acceptance mechanism never ran."

- **The October 4, 1991 memorandum of understanding, in full.** Report 12061 ¶57 reproduces its terms: benchmark testing deferred until after IBM hardware upgrades; EDS released from evidence of successful tests for implementation stages already completed; liquidated damages waived for benchmark-test delay; revised response-time requirements to be jointly developed, which never happened before EDS's termination on May 31, 1992. The auditor's assessment: "the legal effect of this modification is unknown and is currently the subject of litigation."

- **CPU utilization figures reattributed.** The 95 percent regular-day and 100 percent peak figures come from an October 11, 1994 report by an independent consultant the Department hired, not from an Auditor General measurement. The 65 percent industry comparison is data the Department obtained.

- **Cost floor corrected.** $310,621,339 through fiscal year 1996–97, the Department's own estimate (Report 13287, p. 14), superseding the archive's earlier $245.3 million figure. Overrun of roughly 188 percent on the $107,658,141 bid.

### Two null returns documented

The Department of Children and Families holds no responsive records for RFP 88-74-BC. The Division of Administrative Hearings destroyed the Case 88-002942 file under routine retention around 1998; its Records Disposition Documents are preserved here as the evidence of destruction.

## Pending

`FLORIDA/PENDING-CHANGES.md` carries 38 open items, all P2 or P3, deferred by design. No blockers.

## Handling

Source PDFs and reading-order Markdown are committed under `FLORIDA/PDFs/`. Derived OCR artifacts — sidecar text, run logs, searchable-layer duplicates, and one intermediate rotation-corrected re-OCR — are excluded and regenerable from the source PDFs via `scripts/ocr_pdf_v1.sh`.
