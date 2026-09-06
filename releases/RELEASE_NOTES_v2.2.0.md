# Release v2.2.0 — The FLORIDA System archive joins the corpus

**September 6, 2026**

This release adds the FLORIDA System study to the Aberdeen archive as a top-level `FLORIDA/` directory, and lands a sweep of primary-source corrections to the papers it contains.

## What FLORIDA is

A primary-source reconstruction of Florida's 1988–1996 integrated public-assistance eligibility procurement — RFP 88-74-BC, the EDS award, the IBM subcontract, the collapse, and the $42.8 million settlement. Eight analytical papers plus the evidentiary apparatus behind them.

The study belongs in this archive by provenance: it began as a Kastner Aberdeen project on Unisys, the bidder that lost RFP 88-74-BC by 4.4 points and later ran the winner's programming shop under a contract that reached roughly $58.7 million.

## New in this release

**Auditor General reports obtained and read.** Reports 11178 (1989), 11619 (1991), 12061 (1993), and 13256 (1998) were supplied by the Auditor General's office on September 5, 2026 and OCR'd locally at 300 dpi. None is available online. Reports 12581 (1995) and 13043 (1998) were supplied August 11, 2026.

**Four P1 corrections applied to the published papers:**

- **The RFP did specify a quantified performance standard.** The archive previously inferred from the silence of the appellate and protest records that RFP 88-74-BC set no numeric performance requirement. That inference was wrong. Report 12061 ¶51 documents a contractual requirement that response times fall between one and eight seconds for at least 95 percent of the time, sampled every fifteen minutes on a randomly selected day each month at randomly selected workstations, with system availability of at least 97 percent during normal working hours over any consecutive thirty-day period. The structural argument is relocated from "no standard existed" to "the standard existed and its acceptance mechanism never ran."

- **The October 4, 1991 memorandum of understanding, in full.** Report 12061 ¶57 reproduces the MOU's terms: benchmark testing deferred until after IBM hardware upgrades; EDS released from evidence of successful tests for implementation stages already completed; liquidated damages waived for benchmark-test delay; revised response-time requirements to be jointly developed, which never happened before EDS's termination on May 31, 1992. The auditor's own assessment is that "the legal effect of this modification is unknown and is currently the subject of litigation."

- **CPU utilization figures reattributed.** The 95 percent regular-day and 100 percent peak figures come from an October 11, 1994 report by an independent consultant the Department hired, not from an Auditor General measurement. The 65 percent industry comparison is data the Department obtained.

- **Cost floor corrected.** $310,621,339 through fiscal year 1996–97, the Department's own estimate (Report 13287, p. 14), superseding the archive's earlier $245.3 million figure. Overrun of roughly 188 percent on the $107,658,141 bid.

**Two null returns documented.** The Department of Children and Families holds no responsive records for RFP 88-74-BC. The Division of Administrative Hearings destroyed the Case 88-002942 file under routine retention around 1998; its Records Disposition Documents are preserved in the archive as the evidence of destruction.

**A methodology standard added.** The README now records that log entries claiming completed work are claims requiring verification against the destination artifact, not facts. This was learned from a July 28, 2026 log entry recording a URL repair that had never been applied to the papers it named.

## Pending

`FLORIDA/PENDING-CHANGES.md` carries 38 open items, all P2 or P3, deferred by design. No blockers.

## Handling

Source PDFs and reading-order Markdown are committed under `FLORIDA/PDFs/`. Derived OCR artifacts — sidecar text, run logs, searchable-layer duplicates, and one intermediate rotation-corrected re-OCR — are excluded and regenerable from the source PDFs via `scripts/ocr_pdf_v1.sh`.
