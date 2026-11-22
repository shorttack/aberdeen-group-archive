# FLORIDA System — Processor Capacity Over Time, 1988–1998

*Brief prepared October 29, 2026. Working document for the IEEE Annals article ("Bought After the Fact") and the next PENDING-CHANGES sweep. It changes no published paper. New facts here are logged as proposed pending rows in § 6 rather than carried into the papers.*

---

## 1. Purpose and bottom line

This brief lists every IBM processor the record places under the FLORIDA System, from the November 1988 bid to the 1998 as-built system, with the source and evidentiary standing for each step. It then adds the first IBM-published capacity figures the archive has held for these machines.

Bottom line, stated as inference from the figures in § 3:

- The bid machine (3090-300E) had roughly **one-fifteenth** of the nominal processor capacity installed by 1998, and about **one-seventh** of the capacity in production in 1995, which still ran at 90–97 percent busy.
- Each upgrade came after the workload had already overrun the machine in place: the 300J was replaced in 1991, the 720 and 600J pair was collapsed in 1992, the 900 was installed before it was approved, and the 900 was saturated by 1995. Capacity was bought after the fact at every step.
- The ES/9000 Model 720 used the same engine as the 3090-J. The 720 and 600J pair was therefore two six-way J-class machines with the same nominal capacity, coupled by IRLM. The single ES/9021-900 that replaced them in 1992 equals the pair's combined nominal capacity on IBM's own constants, in one MVS image and without the IRLM overhead. On IBM's announcement dates the 900 was shipping before the October 1991 MOU, so Duggar's single-host alternative existed as a product when the coupled configuration was chosen. (Inference; see § 4.)

## 2. Standing key

| Tag | Meaning |
|---|---|
| **Documentary** | Stated in an Auditor General report, DOAH order, court opinion, or IBM publication |
| **Testimony** | Stated in the 1993 Leon County grand jury presentment, which rests on uncross-examined testimony |
| **IBM reference** | IBM product or constant data, not a FLORIDA record |
| **Inference** | Kastner's or the archive's reasoning from the above; not to be printed as fact |

## 3. Timeline with capacity proxy

**Capacity proxy.** IBM publishes an SRM constant (service units per CPU-second) for each processor model. IBM describes the constant as the factor that "relates processor execution time to the CPU/SRB portion of service" calculated by the MVS System Resources Manager ([IBM, Processor version codes and SRM constants](https://www.ibm.com/support/pages/processor-version-codes-and-srm-constants)). Multiplying the per-engine constant by the engine count gives a nominal total. **This is a relative indicator, not MIPS and not an LSPR workload measurement.** It already includes some multiprocessor fall-off, because the per-engine constant drops as engine count rises, but it does not capture cache, I/O, IMS, or IRLM effects. The "× bid" column divides each total by the 3090-300E's total.

| Date | Processor | Engines | SU/sec per engine | Nominal total | × bid | Role and event | Standing | Source |
|---|---|---:|---:|---:|---:|---|---|---|
| Nov. 1988 | 3090-300E | 3 | 724.7 | 2,174 | 1.00 | Production host as bid by EDS | Documentary | [DOAH 89-0003BID](<PDFs/Unisys v. HRS — DOAH Case 89-0003BID Recommended Order (Mar. 14, 1989).pdf>) ¶¶71–72 |
| Nov. 1988 | 3090-400E | 4 | 700.0 | 2,800 | 1.29 | Machine the EDS demonstration actually ran on; hearing officer noted the discrepancy and let it stand | Documentary | [DOAH 89-0003BID](<PDFs/Unisys v. HRS — DOAH Case 89-0003BID Recommended Order (Mar. 14, 1989).pdf>) ¶¶71–72 |
| Before Oct. 1991 | 3090-300J | 3 | 1,069.4 | 3,208 | 1.48 | Production host at the MOU; when and how the 300E became a 300J is undocumented | Testimony | [Presentment](sources/courts/leon-grand-jury-presentment-1993-08-18-ocr.md) ¶49 |
| Oct. 1991 (Oct. 4 per AG; "on or about Oct. 18" per grand jury) | ES/9021-720 | 6 | 941.6 | 5,649 | 2.60 | Replaces the 300J under the MOU; "over 11 million dollars" for the pair, 65% EDS / 35% HRS | Testimony; AG dates the MOU | [Presentment](sources/courts/leon-grand-jury-presentment-1993-08-18-ocr.md) ¶49; [AG 12061](PDFs/auditor-general/AG-12061.md) ¶57 |
| Oct. 1991 | 3090-600J | 6 | 941.6 | 5,649 | 2.60 | Bought from EDS; coupled to the 720 by IRLM (two-image IMS block-level data sharing) | Testimony; IBM reference | [Presentment](sources/courts/leon-grand-jury-presentment-1993-08-18-ocr.md) ¶¶49–50; [PRESENTMENT-1993-FINDINGS](PRESENTMENT-1993-FINDINGS.md) § 2.3a |
| Oct. 1991–mid-1992 | 720 + 600J pair | 12 | — | 11,298 nominal | 5.20 nominal | Nominal sum before IRLM, VTAM notification, and buffer re-read overhead; the grand jury's "40 percent or more" overhead remains testimony | Inference | [PRESENTMENT-1993-FINDINGS](PRESENTMENT-1993-FINDINGS.md) § 2.3a |
| July–Aug. 1992 | ES/9021-720 alone | 6 | 941.6 | 5,649 | 2.60 | Pair consolidated onto the 720 after Advanced Computer Services traced response problems partly to the two-machine configuration; memory from the WIC/PI machine added | Documentary (consultant via AG); testimony | [AG 12061](PDFs/auditor-general/AG-12061.md) ¶¶18, 49–59; [Presentment](sources/courts/leon-grand-jury-presentment-1993-08-18-ocr.md) ¶53 |
| (Recommended, not bought) | ES/9021-860 | 5 | 1,976.3 | 9,881 | 4.54 | IBM's own "Snapshot" study recommended this model | Testimony | [Presentment](sources/courts/leon-grand-jury-presentment-1993-08-18-ocr.md) ¶54 |
| Mid-Aug. 1992 | ES/9021-900 | 6 | 1,883.2 | 11,299 | 5.20 | Installed on trial before ITRPAC review; approved after the fact Dec. 29, 1992; $9,150,000 paid Feb. 12, 1993 | Documentary (AG); testimony | [AG 12061](PDFs/auditor-general/AG-12061.md) ¶¶18–21; [Presentment](sources/courts/leon-grand-jury-presentment-1993-08-18-ocr.md) ¶¶53–58 |
| 1993–Apr. 1995 | ES/9021-900 | 6 | 1,883.2 | 11,299 | 5.20 | "Approximately 95 percent capacity during regular workday hours"; deemed inadequate | Documentary | [AG 12581](PDFs/auditor-general/AG-12581.pdf) p. 29; [AG-12581-13043-FINDINGS](AG-12581-13043-FINDINGS.md) |
| Apr. 22–23, 1995 | ES/9021-982 | 8 (six active per AG) | 2,323.9 (8-way) | 18,591 (8-way); about 14,668 if six-active is read as the 962 constant | 8.55 / about 6.75 | Replaces the 900; $5,438,079.75; measured 90–97.5% busy on May 1, 1995 | Documentary; six-active reading is inference | [AG 12581](PDFs/auditor-general/AG-12581.pdf) pp. 29, 55, ¶¶9, 23 |
| 1995 | 3090-600J | 6 | 941.6 | 5,649 | 2.60 | Still installed, "utilized for training, development, and data communications"; about 16,000 network devices | Documentary; "offload" reading is inference | [AG 12581](PDFs/auditor-general/AG-12581.pdf) ¶9, p. 27 |
| 1998 | ES/9021-982 + 9672-R83 + 9672-R44 | 8 + 8 + 4 | 2,323.9 / 904.7 / 2,038.2 | 33,982 combined | 15.63 | Three machines "linked together in a Sysplex environment"; no 3090 present. Sysplex is documented only here | Documentary | [AG 13287 via AG-1998-SYSTEMS-REVIEW-FINDINGS](AG-1998-SYSTEMS-REVIEW-FINDINGS.md); AG 13287 p. 15 |

All SU/sec constants come from the [IBM SRM constants table](https://www.ibm.com/support/pages/processor-version-codes-and-srm-constants). The table lists the 9021-720 as a six-engine model, with a separate "partitioned 5-way" entry. That resolves the archive's earlier gap on the 720's engine count, subject to confirming which form HRS had.

## 4. Supporting IBM product facts

| Fact | Standing | Source |
|---|---|---|
| The lower six water-cooled ES/9000 models, including the 720, "used the same processor as the 3090-J," with unchanged per-engine performance; only the 820 and 900 were a new design | IBM reference (secondary; confirm against IBM announcement letter before print) | [Wikipedia, IBM ES/9000 water-cooled models](https://en.wikipedia.org/?title=IBM_9672), citing IBM's ES/9000 announcement |
| 9021-720 shipping from September 1990; 9021-900 shipping from September 1991 | IBM reference (secondary; confirm) | [Wikipedia, IBM ES/9000 water-cooled models](https://en.wikipedia.org/?title=IBM_9672) |
| Model 900 commercial performance "1.7 to 1.9 times that of the Model 600J"; double the 600J's processor storage | IBM claim, reproduced from IBM Archives text (secondary copy; locate the IBM original) | [IBM ES/9000 archive text as reproduced](https://drhart.ucoz.com/index/ibm/0-118) |
| Pre-Sysplex IRLM data sharing limited to two MVS images; each image could be an N-way multiprocessor | Documentary (IBM) | [PRESENTMENT-1993-FINDINGS](PRESENTMENT-1993-FINDINGS.md) § 2.3a |

**Cross-check.** IBM's SRM constants put the 900 at 2.0× the 600J (11,299 ÷ 5,649). IBM's marketing claim was 1.7–1.9× on commercial work. The two agree in direction and differ by about what one would expect between a dispatching constant and a workload measurement. This is why the brief treats the SRM figures as a proxy only.

## 5. Gaps still open

1. The 300E-to-300J step: date, cost, and approval are undocumented.
2. Which form of the 720 HRS installed: six-way or partitioned five-way.
3. The 982's "six active" engines: confirm the exact AG 12581 wording, and whether IBM capacity-on-demand or a 962-equivalent microcode setting applied.
4. No workload-measured capacity (LSPR ITR ratios) is in hand for the 3090-E/J or 9021 lines. The SRM proxy should be replaced or corroborated with period LSPR tables before any capacity ratio goes into the Annals text.
5. The 9672-R83 per-engine constant (904.7) is lower than the R44's (2,038.2). This reflects different 9672 generations, which should be confirmed before the 1998 total is quoted.

## 6. Proposed pending rows (for the next sweep; not applied)

| Row | Priority | Change |
|---|---|---|
| 80 | P2 | Row 78 (no period capacity source) is partly resolved: IBM SRM constants are now cited as a relative proxy, labeled "not MIPS." Keep the prohibition on printing MIPS. |
| 81 | P2 | 9021-720 engine count: six-way per IBM SRM table (confirm against HRS configuration). |
| 82 | P3 | 720 used the 3090-J engine, and the 900 was shipping from September 1991. Supports the inference that a single-host alternative existed at the October 1991 MOU. Confirm against the IBM announcement letter, then use in Annals § on the MOU. |

## 7. Archive files referenced

- [PRESENTMENT-1993-FINDINGS.md](PRESENTMENT-1993-FINDINGS.md)
- [AG-12061-FINDINGS.md](AG-12061-FINDINGS.md)
- [AG-12581-13043-FINDINGS.md](AG-12581-13043-FINDINGS.md)
- [AG-1998-SYSTEMS-REVIEW-FINDINGS.md](AG-1998-SYSTEMS-REVIEW-FINDINGS.md)
- [DOAH-2026-09-06-FINDINGS.md](DOAH-2026-09-06-FINDINGS.md)
- [PENDING-CHANGES.md](PENDING-CHANGES.md)
- [SOURCES.md](SOURCES.md)
