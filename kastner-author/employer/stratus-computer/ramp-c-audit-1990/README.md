# RAMP-C Audit Report — Aberdeen Group for Stratus Computer (March 1990)

## Historical Significance

This document is the complete **RAMP-C Conversion Document** — IBM's
proprietary synthetic benchmark for interactive commercial transaction
processing — marked **"IBM INTERNAL USE ONLY"** and dated April 17, 1984.
It was used by Aberdeen Group in a March 1990 audit engagement for
**Stratus Computer, Inc.** of Marlboro, Massachusetts, assessing Stratus
fault-tolerant system performance on RAMP-C alongside the emerging
TCA-A and TPC-B industry-standard benchmarks.

RAMP-C is historically significant because:

1. **It was IBM's proprietary competitive weapon.** IBM used RAMP-C
   internally to generate performance comparisons across the System/34,
   System/36, System/38, and 43xx product lines — and against competitors.
   The benchmark was never publicly released, and IBM refused to let
   independent auditors verify results derived from it.

2. **It sparked the benchmarking standards movement.** Industry frustration
   with IBM's proprietary benchmarks (RAMP-C and the related Ramp-C variant
   for midrange systems) was a direct catalyst for the founding of the
   **Transaction Processing Performance Council (TPC)** in 1988. As John
   Logan of Aberdeen Group told the *Wall Street Journal* in June 1988:
   *"It was one of the cheapest tricks IBM could have pulled. A benchmark
   should be something that is widely circulated and can be duplicated and
   verified."*

3. **Peter Kastner was present at the TPC's founding.** Then at DEC's
   competitive marketing group, Kastner championed DEC's immediate
   membership in the new benchmark standards body. He told *Computerworld*
   in August 1988: *"For MIS users, this is one of the significant events
   of the 1980s. For the first time, MIS users can make apple-to-apple,
   vendor-to-vendor comparisons."*

4. **This copy documents the benchmark's actual mechanics.** Little has been
   publicly disclosed about RAMP-C's internals. This 94-page document
   contains the full application description, COBOL pseudocode walk-through,
   database file specifications, display file layouts, TPNS terminal
   simulation scripts, and program flow charts — making it one of the only
   surviving detailed records of the benchmark that shaped an era of
   computing competition.

## Document Details

| Field | Value |
|-------|-------|
| **Title** | RAMP-C Audit Report / RAMP-C Conversion Document |
| **Prepared by** | Aberdeen Group, Inc., 92 State Street, Boston, MA 02109 |
| **Date of audit** | March 1990 |
| **Original document date** | April 17, 1984 (IBM internal) |
| **Classification** | IBM INTERNAL USE ONLY |
| **Pages** | 94 |
| **Client** | Stratus Computer, Inc. (Marlboro, MA) |
| **Kastner role** | Aberdeen Group consultant auditing Stratus performance on TCA-A, TPC-B, and RAMP-C |
| **File** | `IBM-RAMP-C-Pseudocode-1990.pdf` |

## Contents

The document contains ten sections:

1. **Introduction** — Conversion package contents and step-by-step
   conversion procedure for porting RAMP-C to non-IBM systems
2. **RAMP-C History** — Origin as System/38 RAMP (RPG-III, converted to
   COBOL 1982), evolution into the cross-platform RAMP-C
3. **Application Description** — Four transaction classes with detailed I/O
   profiles (reads, updates, adds, display fields, COBOL statement counts)
4. **Measurement Environment** — Workload mixtures (Light, Medium, Heavy),
   workstation configurations, think-time specifications
5. **Execution** — Measurement run procedures and warm-up/cool-down rules
6. **Code Walk-Through** — Complete COBOL pseudocode for all eight programs
   (CLASS1X–CLASS4X main programs + SUBR1X–SUBR4X sub-programs), covering
   Data Division, File Section, Working-Storage, Linkage Section, and
   Procedure Division
7. **Appendix A** — Database file definitions (FILEA through FILEE)
8. **Appendix B** — Display file layouts for all four transaction classes
9. **Appendix C** — TPNS (Teleprocessing Network Simulator) scripts
10. **Appendix D** — Program flow charts

## Archival Context

This document resides in the Kastner personal archive under
`employer/stratus-computer/` because it originates from Kastner's
consulting engagement at Aberdeen Group auditing Stratus Computer
performance. Stratus was a leading vendor of fault-tolerant
transaction-processing systems, directly competing with Tandem and
IBM in the financial services and telecommunications markets.

The audit work connecting Kastner to RAMP-C, TCA-A, and TPC-B
demonstrates his deep involvement in the commercial benchmarking
ecosystem — from IBM's proprietary era through the founding of the
TPC standards body and into the open-benchmark era that followed.

### Related items in this archive

- **Logan WSJ 1988 quote** — John Logan's critique of IBM's Ramp-C
  benchmark practices (*Wall Street Journal*, June 17, 1988)
- **Kastner TPC founding quote** — Kastner on DEC joining the benchmark
  standards body (*Computerworld*, August 1988)
- **Archive 7 (NTI workbooks)** — Kastner and Logan's video reports on
  OLTP benchmarking and transaction processing (1990–1991)

## License

CC-BY-4.0 — The original IBM document classification ("IBM INTERNAL USE
ONLY") is historical. This copy is preserved as part of the Kastner
personal archive for historical research purposes.
