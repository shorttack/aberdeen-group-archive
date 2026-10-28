# The 1993 Leon County Grand Jury Presentment: Effect on the Case, and Plan for Updating the Archive

Prepared October 26, 2026. This document makes no edits to published papers.

**Decisions recorded October 26, 2026 (Kastner):**
1. A compressed, searchable PDF is filed in the GitHub `FLORIDA/` folder.
2. Rows 55 and 57 are **not** immediate-fix exceptions; all paper changes wait for the sweep and are logged as PENDING-CHANGES rows 55–71.
3. Routine register updates are approved and applied: the request log, REQUESTS-AWAITING-RESPONSE, and the PENDING-CHANGES append.

**Source.** The source is the Presentment of the Leon County Grand Jury, Fall Term 1992. It was presented in open court and filed on August 18, 1993, by Dave Lang, Clerk. Deputy State Attorney Anthony S. Guarisco and Assistant State Attorney Dennis Valente certified it. The document is 63 pages, with 102 numbered fact paragraphs, 14 special findings, 26 recommendations, and a conclusion. The Leon County Clerk produced it in round 1 of P022996-082026 after the $63 invoice was paid on October 26, 2026.

The same production included two letters about Viann Hardy and Judy Mitchell, the defendants. Both report that no information was found. The working transcript is `sources/leon-grand-jury-presentment-1993-08-18-ocr.md`, an uncorrected OCR text marked by page.

---

## 1. Evidentiary weight: how to cite it

The presentment is the most detailed contemporaneous account the archive holds of what happened inside HRS Management Systems between 1987 and 1993. It also has a particular kind of evidentiary standing:

- **What it is.** A presentment states a grand jury's findings from sworn testimony and documents. It was not cross-examined, and it is not a verdict. People named in it had rights to respond under § 905.28, and several of them exercised those rights in September 1993. Defense counsel described the proceeding as one-sided.
- **What happened afterward.** The jury indicted Hardy and Mitchell. The state dropped the charges against Hardy. Mitchell was acquitted of the felonies and convicted of two misdemeanor counts of false statements about roughly $11 million in EDS payments ([Tampa Bay Times, May 26, 1994](https://www.tampabay.com/archive/1994/05/26/ex-computer-chief-receives-a-split-verdict/)). The trial court then granted Mitchell's renewed motion for judgment of acquittal, and the First District Court of Appeal affirmed on January 4, 1996, holding that the State had not proved she knowingly made false statements with intent to mislead a public servant; Judge Miner dissented ([State v. Mitchell, Fla. 1st DCA 1996](https://www.courtlistener.com/opinion/7756441/state-v-mitchell/)). No conviction arising from the FLORIDA investigation survived. The presentment's characterizations of individuals therefore did not hold up in court in their strongest form. (Corrected October 27, 2026: an earlier version of this note said the conviction was "later thrown out" without a source.)
- **Citation rule for the archive.** Use "the grand jury found" or "the presentment states (¶N)." Do not use bare assertion. Give technical claims the most caution: "40% or more" of machine time, the IRLM "would not work," and the Snapshot as a "marketing tool." These are a lay jury's summaries of witness testimony, chiefly that of HRS technicians Joe Duggar and Mark Spencer. They are not engineering measurements.
- **Attribution rule.** These are the grand jury's observations and its witnesses' observations. They are not Kastner's, and they are not Aberdeen's. Where Kastner's own 1988–89 testimony or later analysis agrees or disagrees, say so separately and label it.

---

## 2. Effect on the case, thesis by thesis

### 2.1 Architecture: "specified distributed, delivered centralized, and the federal government is why"

**This is the most consequential effect. It partly contradicts a headline claim in print.**

The README, in "What we established," § 1, attributes the distributed-to-centralized outcome to federal competition policy. FNS forced the APD's distributed requirement down to a "preference" (DOAH 88-2942BID ¶26). That fact stands. The presentment adds a second, later, and decisive step that the archive does not record:

| ¶ | Presentment |
|---|---|
| 18 | Unisys's second protest alleged that "the Ohio System (model used by EDS) was not really operational" and that "EDS misrepresented what they could do regarding the Distributive System." |
| 20 | The May 1989 contract "called for a Distributive System." |
| 36 | "Around October 1989, EDS stated that there would be problems with a Distributive System and proposed going to a Centralized System to handle the 'Statewide Clearance' problem." It was also "a way to complete the Project's schedule within the twenty-nine (29) month period." |
| 37 | Secretary Coler "did not think there was a computer large enough." EDS "stated that they would find a computer that would do the job." Coler "signed off … without rebidding the RFP." ITRPAC and the IRC approved the switch "without checking into whether or not it was technologically sound." |
| 38 | EDS favored centralization "because their model, the Ohio System, was a Centralized System, so there would be no major modifications." |
| 39 | "The Federal Government had reached the conclusion that the Centralized System (one large computer) was not the way to go … No one paid attention to this study." |
| 83 | Lt. Gov. MacKay testified that the change to a centralized system should have been rebid. |

**Effect.** The chain now has three links. (1) Federal competition policy lowered the bar, so a centralized transfer base could compete. (2) The evaluators scored that base higher despite knowing what it was. That point is unchanged. (3) About five months after award, EDS proposed and HRS accepted a change-order to centralize. No rebid was held and there was no independent technical review. The grand jury also places a federal study on the opposite side, against centralization. "The federal government is why" overstates the case. A defensible statement would be: "federal competition policy opened the door, and a post-award state decision walked through it."

**Insight that still applies, with 1989 tools.** EDS's stated reason, the "Statewide Clearance" problem, was a real engineering problem. Clearance meant checking every applicant against all districts for duplicate participation. Doing that across a distributed database before mature distributed-transaction products existed was hard. Centralizing was a defensible engineering answer to that one problem. What made it indefensible was going ahead without re-modeling capacity for the new topology and without re-competing a fundamentally different design. This is an inference by the archive, not a finding of the grand jury, and it should be labeled that way. It is also exactly the "unvalidated assumption" pattern the archive's central thesis describes.

**Kastner relevance (label separately).** The ¶18 allegations are the Unisys protest positions in which Kastner testified. The presentment supports those positions, from a separate body and four years later. Kastner's own testimony is still documented only through the DOAH orders.

### 2.2 The capacity thesis and SNAP/SHOT

**The presentment says nothing about the 1988–89 proposal modeling.** It neither supports nor undercuts the archive's position that the modeling tool was sound and the workload inputs were not validated.

It does describe a **second, different IBM capacity study**. The archive must keep the two apart:

- ¶53: HRS "contracted with IBM to do a 'Snapshot' (capacity and analysis of the System) on the 720/600 IRLM Computers in an effort to justify the purchase of a larger computer, the 900." The study "was quickly done and the machines were not tuned. This capacity test was really not a valid one, it was just used as a marketing tool. IBM recommended an 860 Computer but Secretary Williams ordered the 900."
- ¶55(5): after the subpoenas, "more money in the way of sole sources was expended for a 'Snapshot' review and capacity analysis."

**Reading.** This was a 1992 measurement-based study of a running, untuned system. It is not the 1988 predictive model. It is probably the same IBM methodology family; that is an inference to verify. The grand jury's complaint is about inputs and conditions ("not tuned"), not about the tool. That is consistent with the archive's thesis, not against it. One detail cuts against the "marketing tool" characterization: **IBM's study recommended a smaller machine (860) than the one HRS bought (900).** The decision to oversize was the Secretary's, not IBM's.

**Risk to manage.** A reader who sees "Snapshot … not a valid one … marketing tool" could carry it back to the 1988 SNAP/SHOT modeling. Every paper that discusses SNAP/SHOT needs a one-sentence distinction.

### 2.3 As-built topology: the machine lineage is now fuller

The presentment supplies the configuration sequence from 1991 to 1992 that the topology paper lacks:

| Date | Configuration | ¶ |
|---|---|---|
| By Oct. 1991 | **IBM 300J** (read: 3090-300J) | 49 |
| Oct. 18, 1991 (MOU) | 300J upgraded to an **ES/9000-720**; HRS buys a **3090-600J** from EDS; the two are coupled by an **IRLM hookup** | 49–50 |
| 1991–92 | IRLM coupling: "40% or more of the machine's time was used by the machines communicating with each other." Duggar's single-720-with-more-memory recommendation is rejected | 50 |
| By mid-1992 | HRS "determined that the IRLM hook up was no good and put all the programs on the 720." WIC/PI memory is moved to the 720 | 53 |
| Mid-Aug. 1992 | **IBM 900** (ES/9021-900) installed without ITRPAC approval | 54 |

**Effect.** This corroborates and sharpens AG 12061 and PENDING-CHANGES row 32: two mainframes, communications overhead, and consolidation as the remedy. It also adds the cause, the IRLM, and the start date, the October 1991 MOU. The README's statement "One IBM 3090-class mainframe … at any point" is now contradicted for roughly October 1991 to August 1992. Row 32 already flags that. The presentment raises its evidentiary weight.

**IMS connection (inference, needs verification).** In IBM terminology of the period, IRLM is the IMS Resource Lock Manager. It coordinates locks when two hosts share IMS databases (IMS data sharing). If that is what was installed, the "40% or more" overhead is production evidence of **cross-system IMS lock and buffer-coherency cost**. That bears directly on the README's open question, "whether SNAP/SHOT's host model accounted for IMS lock contention." It also agrees with row 49's IMS correction. Verify against IBM IMS/VS data-sharing documentation of about 1990 before stating it in print.

### 2.3a IRLM verified against IBM documentation, and where the bottleneck sat (added October 27, 2026)

<!-- irlm-correction-2026-10-27 -->

The inference recorded in § 2.3 and in PENDING-CHANGES row 59 was checked against IBM's own documentation on October 27, 2026. This section records what is confirmed, what remains testimony, Kastner's technical reading offered for confirmation, and the assessment of it.

**Confirmed.**

| Point | Source |
|---|---|
| IRLM is the IMS/VS Resource Lock Manager, "a component of the IMS/VS Data Base System," and "for block level sharing, the IMS/VS Resource Lock Manager (IRLM) is required." | [IMS/VS Version 1 General Information Manual, GH20-1260-12 (1984)](https://bitsavers.trailing-edge.com/pdf/ibm/370/IMS_VS/GH20-1260-12_IMS_VS_Version_1_General_Information_Manual_198402.pdf) |
| "For block level sharing, the IMS/VS systems can be running in a maximum of two processors." | GH20-1260-12 |
| "IRLM must be defined as an OS/VS2 MVS subsystem and as an ACF/VTAM application in each processor." | GH20-1260-12 |
| IRLM "provides global locking in an environment that consists of two MVS systems and any number of IMS/VS subsystems." "The IRLM uses ACF/VTAM to perform intersystem locking notification." Sharing "minimizes intersystem communication with a two-level lock hierarchy, a resource name-hashing scheme, and a request-batching technique." "When a data set lock is held only by IMS/VSs executing within a single MVS, intersystem notification is not required before a lock is granted on a data item within the data set." | [IBM Systems Journal 21(4), 1982, "IMS/VS: An evolving system"](http://www.bitsavers.org/pdf/ibm/IBM_Systems_Journal/214/ibmsj2104G.pdf) |
| Two-image sharing: "by running an IRLM address space on each of the two OS/390 images. The IRLMs communicate using VTAM but maintain lock tables in each IRLM address space." Block-level locking "is at a higher level than with program isolation ... Because of this coarser level of locking, there is an increased risk of deadlocks and contention." | [IMS Primer, SG24-5352](https://www.redbooks.ibm.com/redbooks/pdfs/sg245352.pdf) |
| An IRLM holds "a primary session and a secondary session (also called an alternate session)" with its partner IRLM. | [IBM IMS Problem Investigator glossary](https://www.ibm.com/docs/de/ims-pi/2.5.0?topic=250-glossary) |
| Coupling-facility sharing: "In a Sysplex that includes a coupling facility and the IBM Internal Resource Lock Manager (IRLM) Version 2, IMS can share data at the block level among as many as 32 systems. In a Sysplex, IMS is no longer limited by IRLM to two central processor complexes (CPCs)." This is IMS Version 5 (1994–95). | [IMS Licensed Program Specifications](https://public.dhe.ibm.com/software/data/ims/shelf/dfsl10e0.pdf) |
| "IRLM locking has longer path length and uses more storage than PI locking, so most users tend to use program isolation when not sharing data." IBM's planning estimate for coupling-facility data sharing: "an additional 10–15% CPU than an equivalent workload running on a single IMS without any data sharing overhead." | [IMS in the Parallel Sysplex Vol. II, SG24-6928](https://www.redbooks.ibm.com/redbooks/pdfs/sg246928.pdf) |
| IRLM must run at the highest dispatching priority, above VTAM: "If this higher dispatching priority is not specified, response times are lengthened." | [IMS Performance and Tuning Guide, SG24-7324](https://www.redbooks.ibm.com/redbooks/pdfs/sg247324.pdf) |

**Consequence.** In October 1991 the 720 + 600J pair was the only form of inter-host IMS data sharing the product offered, at its two-image limit, with lock notification over a VTAM session pair. The 1998 three-machine Sysplex in Report 13287 is the later coupling-facility technology. Duggar's recommendation to run on one host with more memory is what IBM's documentation steers users toward unless sharing is required.

**Still testimony.** The "40% or more" figure (¶50). IBM publishes no overhead figure for the 1991 VTAM-notified form; the 10–15% figure is for the far more efficient coupling-facility form and is a floor, not a comparison. Advanced Computer Services' July–August 1992 finding (AG 12061 ¶¶49–59) that the two-mainframe configuration and its communications overhead contributed to poor response time is independent corroboration of direction, not of magnitude.

**Kastner's technical reading, recorded verbatim (October 27, 2026):**

> I read "before Parallel Sysplex, that sharing was limited to exactly two processors" as "one processor in each multi-processor machine could pass VTAM messages; that processor could become (and did?) a bottleneck holding up the other processors."

**Assessment.** The intuition that the pair was serialized is correct; the location is not. IBM's "processor" in this context is a processor complex running one MVS image, not a CPU engine. The 1982 paper says "two MVS systems"; the Primer says "two OS/390 images"; current specifications say "one IRLM on each z/OS system." Each image could be an N-way multiprocessor (the 600J was six-way). MVS dispatched the IRLM and VTAM address spaces on any free engine, so no CPU was dedicated to the link and none was the choke point. The serialization lived in four places:

1. **One IRLM address space per image.** All global lock requests on a host funnel through one address space that keeps the lock tables and latches its own work. IBM's requirement that it run above VTAM in priority, or "response times are lengthened," is the fingerprint of a serialized service.
2. **One VTAM session pair between the two IRLMs.** All intersystem notification goes down one pipe. The "request-batching technique" exists because the pipe is serial.
3. **The requesting program waits.** A lock that needs the other side's agreement suspends the dependent region until the grant returns; IRLM's timeout and deadlock machinery exists to interrupt "dependent regions that have been waiting for a lock." While waiting, the region holds all its other locks, so contention cascades. This cost appears as response time, not CPU.
4. **The hierarchy optimization was defeated by the split.** Intersystem notification is skipped only when a data set lock is held within a single MVS. The sole reason to place the 600J beside the 720 was to have both update the same production databases, which forces notification on nearly every data-item lock and buffer invalidation plus DASD re-read on every changed block. FLORIDA's configuration was the worst case for the protocol.

The "40 percent" therefore compresses three costs: IRLM and VTAM path length on both hosts, extra DASD I/O for buffer re-reads, and suspended-region wait time. Plausible as a combined figure; not a measurement.

**Nuance for any published use.** The engine-spinning behavior Kastner described does exist, but in the later Parallel Sysplex form: a synchronous coupling-facility request keeps "one processor engine ... in a busy state" (SG24-6928). The 1991 VTAM form did not spin an engine; the request went out as channel I/O and the task was suspended. The cost moved from engine time to latency and path length.

**Still unverified, label as inference in print.** Which databases were shared and in what mode (full update sharing on both hosts, or read-only/batch on the 600J); whether the overhead was dominated by lock notification or buffer invalidation; processor capacities (the archive holds no period MIPS or ITR source for any FLORIDA machine; see PENDING-CHANGES row 78); the RFP's definition of "transaction" behind the 5-million-per-day target.

**Pending rows.** 76 (this verification; row 59 promoted to P2), 77 (State v. Mitchell sourced), 78 (processor capacities unsourced).

### 2.4 The October 1991 MOU: EDS released from performance requirements

¶49: "all performance requirements that EDS was responsible for were waived. This Memorandum released EDS from further obligation." ¶80 adds that IRC staff "did not know" the MOU released EDS.

**This is new to the archive and important.** The archive's account runs through AG 12061's two-part SLA, Webster's finding on the March 1991 assumption error, the August 1992 EDS suit, and the $42.8 million settlement. That account treats EDS as still bound by its performance standards. If the grand jury's reading of the MOU is right, the State signed away its leverage in October 1991. That is seven months before the May 1992 test at 2.8 minutes, and before HRS's warranty claim, which Hardy urged in ¶100.

The two accounts conflict: Hardy's testimony assumes a live warranty, and the jury says the MOU released EDS. The MOU itself is now the highest-value document the archive lacks. It also explains the 65/35 hardware cost split.

### 2.5 Money: the $5.1 million upgrade problem

- ¶58: "IBM got about 9.1 million dollars but refused the check because the ESCON DASD had been removed from the package." A second ITRPAC package paid IBM **$600,000** "for services rendered rental of the ESCON DASD, and software maintenance." This is consistent with AG 12061, which records $9,150,000 paid on February 12, 1993.
- ¶49: the October 1991 720/600 upgrade cost "over 11 million dollars," split 65% EDS and 35% HRS.
- **Neither figure is $5.1 million.** The remediation table, row 7, and the cost reconciliation both carry the Los Angeles Times "$5.1 million" figure as the first CPU upgrade. Two documents now point to about $9.1 million for the 900 plus $600,000, and to more than $11 million for the 720/600. The $5.1 million figure is unexplained. It may be a reporter's figure, a net figure, or a different line item. Downgrade it to "reported" and carry both primary-source figures.
- ¶59: Donna Dye's projection of the original FLORIDA System cost was $94,874,000. She projected **$166 million by June 30, 1993**, and Lucy Hadi reported lower figures to the Legislature. This adds a contemporaneous internal estimate to the cost reconciliation.
- ¶¶76–77, Medicaid: a February 1993 reconciliation found **235,000** people listed as eligible who were not eligible. That information "could have saved the State … about $173,000,000." This is a counterfactual savings estimate, not an improper-payment total. Row 33 calls AG 12061's roughly $28 million "the largest dollar figure in the archive tied to a control failure." That wording must change or carry the qualifier.
- ¶¶69–75 and Recommendation 25: automatic food stamp recertification of about 200,000 households, millions of dollars in ineligible benefits, and duplicate PINs and warrants that remained unremedied as of August 1993.

### 2.6 Dates that turn reconstructions into facts

| Item | Archive now | Presentment |
|---|---|---|
| Production cutover | "c. H1 1991 (reconstructed)" in CHRONOLOGY | Williams approved cutover effective **July 1, 1991**, after Arnold argued against leaving the pilot on June 24, 1991. The old system was taken down (¶¶45–46) |
| Ohio warning | not in the archive | **May 7, 1990**: do not go beyond acceptance testing and pilot (¶42) |
| EDS's own slow-down warning | not in the archive | **March–April 1991**: acceptance testing was not complete, and Hardy threatened to sue (¶44) |
| HRS takeover from EDS | not in the archive | **June 1, 1992** (¶52) |
| "Black Tuesday" crash | not in the archive | **June 2, 1992**: a promoted application program corrupted the database (¶52) |
| Centralization change | not in the archive | **c. October 1989** (¶36) |
| ITRPAC after-the-fact approval of the 900 | AG 12061, Dec. 29, 1992 | Agrees; Comptroller Lewis's letter of Dec. 28, 1992 to Meggs (¶57) |

The March 1991 discovery of EDS's capacity-assumption error (Webster) can now be placed precisely. It came after the vendor's own March–April warning to slow down and before a July 1, 1991 cutover that HRS ordered over objections.

### 2.7 Oversight: the strongest support yet for "no independent validation"

¶¶79–82, Findings 10–12, and the Governor's testimony in ¶101 give firsthand admissions from the oversight bodies. ITRPAC "takes at face value what an agency says" (Dozier Johnson, DMS). Hale and IRC staff "completely ignored the 720/600 IRLM hook up" and "just accepted what was stated." Governor Chiles said ITRPAC "was overwhelmed by the FLORIDA System Project." The IRC's on-site monitor "lost her objectivity" and was later hired by HRS at about a 106% raise.

**Recommendations 2, 3, 11, and 12** call for a "full-time neutral authoritative body" with "two persons with expert technical skills." They would require that "no state agency should be taken at face value," and would prohibit vendor lobbying of reviewers. This is, in 1993, a description of independent verification and validation (IV&V) as federal rules later required for large state benefit systems. **This is a prescience item** for "One Model, Forty Years" and "One Bad RFP Away." It is the grand jury's foresight, not Kastner's, and should be scored as the jury's.

¶¶96–99 give Dr. Jim Zingale's three-part test: need, business case, technological soundness. They also give his four-signature sign-off procedure. These belong in the same lessons discussion.

### 2.8 Root causes, multi-factor (Operating Conditions paper)

Zingale's diagnosis in ¶95 lists six causes:
1. a massive caseload;
2. field staff who were poorly trained and had to carry the caseload while also converting it, producing database errors that drove benefit-payment errors;
3. data-access design;
4. programming and functionality;
5. an untuned system that needed reprogramming;
6. platform configuration.

The presentment confirms that the operational failure was not only a capacity failure. That supports the archive's multi-cause framing and its separation of capacity from conversion and data quality.

### 2.9 The federal-deadline framing (Empty Center paper)

Finding 2(e) says Hardy misled the Steering Committee, Williams, and ITRPAC by claiming that missing the COBRA date would cut off federal funding and that no extensions were possible. "This was not true because there have been some extensions." The archive's federal-policy paper treats federal deadline pressure as a structural driver. The presentment says that at least some of the pressure was overstated internally. Both can be true; the paper should carry the qualifier.

### 2.10 Vendor bias beyond FLORIDA: Wang, DEC, StorageTek, CAMBEX

¶¶60–68 and Findings 3 and 6 cover these:
- The Office of Disability Determination procurement: Wang won on points and price. An emergency award went to IBM instead, and a hearing officer found favoritism and a "contrived" emergency.
- The 1991 mid-range strategy: DEC won by one point. The procedure was then recast as an RFI with a new cost sheet, and IBM won with the RISC System/6000.
- The WIC IBM 3081 bought for $1,000, split sole sources kept under ITRPAC's $500,000 threshold, the StorageTek tape-cartridge leak, and the CAMBEX used-equipment episode.

**Disclosure.** Kastner was a developer at Wang and a marketing executive at DEC. These episodes are outside the FLORIDA papers' scope. They are relevant to Aberdeen-era analysis of 1990s state-government buying patterns, and to any memoir passage on IBM account control. Record them as grand jury findings. Do not frame them as Kastner's observations.

### 2.11 People: new and confirmed entities

**Confirmed or new roles:**
- Viann Hardy, Deputy Secretary for Management Systems
- Tom Johnson, Assistant Deputy Secretary
- Judy Mitchell, Project Manager
- Lou Gettis, Assistant Project Manager
- Marilyn VanDusseldorp, Manager/Director
- Don Winstead, Deputy Secretary
- Tom Arnold, Assistant Secretary for Economic Services
- Lucy Hadi, Hardy's successor
- Robert Williams, Secretary
- Greg Coler, former Secretary
- Mike Hale, IRC Executive Director
- Dozier Johnson, DMS and ITRPAC
- Carol Pettyjohn, IRC
- David Coburn, Governor's Office of Planning and Budget
- Dr. Jim Zingale

**Technical witnesses:** Joe Duggar, Mark Spencer, Karin Morris, Donna Dye, Gerald Lourcey, and Charles Ray.

**Evaluators:** Martha Crabb and Karen Girard.

**Vendors:** John Lyons (IBM), Tom Edwards (Unisys), and John Agliato (CAMBEX, as the letter's recipient).

**Prosecutors:** Willie Meggs, Anthony Guarisco, and Dennis Valente.

**Bodies:** MAXIMUS (the RFP author) and the subcontractors MSD and FSU.

---

## 3. Update plan

The plan follows the protocol in `FLORIDA/PENDING-CHANGES.md`: file the source, write the findings note, append rows, and leave the papers alone until a sweep.

### Step A. File the source material

| # | Action | Location | Needs your OK? |
|---|---|---|---|
| A1 | OCR transcript, marked by page | `FLORIDA-system/sources/leon-grand-jury-presentment-1993-08-18-ocr.md` in the project repo (**done**; existing folder) | No |
| A2 | Source PDF. **It is 103.6 MB, which is over GitHub's 100 MB per-file limit.** Produce a searchable, compressed PDF (OCR text layer, about 150 dpi grayscale, likely 10–20 MB) and keep the original scan on the Mac | GitHub: either the existing `FLORIDA/PDFs/records-requests/` folder or a **new** `FLORIDA/PDFs/courts/` folder. Mac: `~/Desktop/Archive/FLORIDA/` | **Yes: folder choice.** A new folder needs approval |
| A3 | Hardy and Mitchell "no information found" letters | Same folder as A2 | Same |
| A4 | Mirror of the OCR transcript | GitHub `FLORIDA/sources/courts/` (existing) | No |
| A5 | Corrected OCR. Hand-check the paragraphs quoted in § 2 against the PDF images: ¶¶18, 20, 36–39, 45–46, 49–50, 53–59, 76–77, 95, and Recommendations 2, 3, 11, and 12 | In place | No |

### Step B. Findings note

B1. File this document's § 2 as `FLORIDA/PRESENTMENT-1993-FINDINGS.md` on GitHub, alongside the AG and DOAH findings notes. A copy stays in the project repo.

### Step C. Proposed PENDING-CHANGES rows (55 onward)

| # | Change | Source | Targets | Priority |
|---|---|---|---|---|
| 55 | **Architecture causation is overstated.** "The federal government is why" omits the post-award change of about October 1989: EDS proposed centralization, Coler approved without rebid, and ITRPAC and IRC did no technical review. A federal study opposed centralization. Rewrite as a three-link chain (federal policy, then the evaluators, then the post-award change-order) | Presentment ¶¶20, 36–39, 83 | README, "What we established," § 1; main report; Empty Center; Whose Model; Three Seconds | **P1** (ask whether to treat it as an immediate-fix exception) |
| 56 | **The October 18, 1991 MOU released EDS and waived all performance requirements** (grand jury's reading). It is new to the archive. Reconcile it with the AG 12061 SLA account, the Webster finding, the EDS suit, and the settlement narrative. Add the MOU to the collection plan as a top-priority target | ¶¶49, 80, 100 | Main report; Cost Reconciliation; Remediation; Webster Addendum; COLLECTION-PLAN | **P1** where papers state EDS remained bound; otherwise P2 |
| 57 | **"$5.1M first upgrade" is unsupported by primary sources.** The 900 cost about $9.1M plus $600K (presentment), consistent with AG's $9.15M. The 720/600 upgrade cost more than $11M at 65/35. Recast $5.1M as an LA Times figure that remains unreconciled | ¶¶49, 58; AG 12061 ¶¶18–21; reinforces row 27 | Remediation table, row 7, and lines 44 and 76; main report lines 134, 149, and 216; Cost Reconciliation | **P1** |
| 58 | **Machine lineage, 1991–92**: 3090-300J, then the MOU, then ES/9000-720 plus 3090-600J under IRLM (40%+ overhead claimed), then all work on the 720, then the 900 in August 1992. Strengthens row 32 | ¶¶49–50, 53–54 | As-Built Topology; README "one 3090-class mainframe"; CHRONOLOGY | P2 |
| 59 | **IRLM as IMS lock manager: production evidence of cross-host lock overhead** (inference; verify in IBM docs). Bears on the README's open question about IMS lock contention and on row 49 | ¶50; row 49 | README "open questions"; Three Seconds; Whose Model; workload-assumption concept page | P3 (P2 once verified) |
| 60 | **Distinguish the 1992 IBM "Snapshot" from the 1988–89 SNAP/SHOT proposal modeling.** The 1992 study ran on untuned machines and recommended an 860; Williams ordered the 900. Add a one-sentence guard wherever SNAP/SHOT appears | ¶¶53, 55 | README § 3; Three Seconds; Whose Model; Unisys Protests paper; Consistency Audit | P2 |
| 61 | **Cutover date: July 1, 1991**, approved by Williams over Arnold's June 24 objection. Replace "c. H1 1991 (reconstructed)." Add the May 7, 1990 Ohio warning, EDS's March–April 1991 slow-down warning, the June 1, 1992 takeover, and June 2, 1992 "Black Tuesday" | ¶¶42, 44–46, 52 | CHRONOLOGY (lines 37 and 116); main report timeline; Operating Conditions | P2 |
| 62 | **Medicaid $173M counterfactual vs. the $28M "largest" figure.** Qualify row 33's superlative. Carry 235,000 ineligible people (February 1993 reconciliation) as a separate data point | ¶¶76–77 | Cost Reconciliation; main report cost-of-failure section | P2 |
| 63 | **Cost projection: $94.874M to $166M** (Dye, June 30, 1993), with lower figures reported to the Legislature | ¶59 | Cost Reconciliation | P3 |
| 64 | **Oversight admissions and the 1993 IV&V-like recommendations.** Score them as grand jury prescience, not Kastner's | ¶¶79–82, 96–99, 101; Findings 10–12; Recs. 2, 3, 11, 12, 24 | One Model, Forty Years; One Bad RFP Away; Remembered by Auditors | P3 |
| 65 | **Federal-deadline pressure was overstated internally** (COBRA extensions existed) | Finding 2(e); ¶¶37, 85 | Empty Center | P2 |
| 66 | **Root causes, multi-factor** (Zingale's six) | ¶95 | Operating Conditions; Making It Workable | P3 |
| 67 | **Evaluation tampering corroborates DOAH 89-0003BID**, and the Unisys protest positions are supported by a separate body (¶18) | ¶¶15–19; Findings 3(c), 5(e), 7(a) | Unisys Protests paper; Kastner protest analysis | P3 |
| 68 | **Non-FLORIDA vendor-bias episodes** (Wang ODD, DEC mid-range, StorageTek, CAMBEX, WIC 3081). Disclose Kastner's Wang and DEC history. Out of scope for the FLORIDA papers; candidate for a memoir or Aberdeen note | ¶¶60–68; Findings 3, 6 | Memoir study package; COLLECTION-PLAN | P3 |
| 69 | **Citation discipline for the presentment** (the § 1 rule above). Pair every use with the outcome: Hardy's charges were dropped, and Mitchell was convicted of misdemeanors only, with that conviction later thrown out | Presentment; TBT 1993-08-19 and 1994-05-26 | All papers on the sweep | P2 |
| 70 | **Records-request state: Leon County round 1 delivered.** The presentment was produced. The Hardy and Mitchell letters report "no information found." Do not read those letters as proof that the case files were destroyed or never existed (same logic as row 53) | Clerk production, Oct. 2026 | Request log; REQUESTS-AWAITING-RESPONSE; README file table | P2 (operational register: apply now) |
| 71 | **Close the "statewide grand jury" correction loop.** The caption confirms "Circuit Court, Second Judicial Circuit, Leon County, Grand Jury Fall Term 1992." On the sweep, convert the September 23 banners into clean text | Caption, p. 1 | Remediation table; Unisys analysis; main report; SOURCES; records-request drafts | P2 |

### Step D. Operational registers (not published papers; can be applied now)

- **D1.** Request log (`FOLLOWUP-records-requests-2026-09.md`). Leon County P022996-082026: round 1 received, presentment produced (63 pages, filed August 18, 1993), and the Hardy and Mitchell letters report "no information found." Ask the Clerk whether a round 2 is coming, covering the § 905.28 objection file and the indictment or case dockets.
- **D2.** GitHub `REQUESTS-AWAITING-RESPONSE`. Refresh it the same way.
- **D3.** PENDING-CHANGES header. Count, date, and the rows 55–71 above.

### Step E. Metadata and finding aids (on the sweep, or now if you prefer)

| File | Update |
|---|---|
| SOURCES.md | New primary-source entry: the presentment with citation, Clerk request number, and file paths. Mark the 1993 press pieces as corroborated by it |
| CHRONOLOGY.md | Rows from § 2.6. Mark the cutover as documented, not reconstructed. Close gap row 116 for the cutover date |
| COLLECTION-PLAN.md § 1.6 | Presentment: **acquired.** New targets: (1) the **October 18, 1991 HRS–EDS MOU**; (2) the IBM 1992 "Snapshot" report and Williams's executive summary to the Governor (¶53); (3) the Ohio warning of May 7, 1990 (¶42); (4) the federal centralized-vs-distributed study (¶39); (5) Zingale's needs-analysis book (¶97); (6) the § 905.28 responses; (7) the Mitchell trial record. The likely holders are the State Archives (Chiles and Williams records), DCF, and HHS. Some can be added to the pending HHS FOIA by amendment |
| README.md | File table: add the two new files. "What remains" item 5: mark it acquired. Remove the remediation table's "names of indicted administrators" gap, lines 76 and 177 |
| research-florida-remediation.md, gaps 9–10 | Mark them answered by the presentment where applicable |
| Archival-ingest study package | Add the presentment as a source document in the Unisys/FLORIDA study (5b4524) or as its own court-record study. Entities from § 2.11 go to the entity cache. Technologies: IBM 3090-300J, 3090-600J, ES/9000-720, ES/9021-900, IRLM, ESCON DASD, RISC System/6000. Observations: tag as grand jury, not Kastner |
| Knowledge wiki (`florida-hrs-archive`) | Add a short entry: presentment acquired; architecture-causation correction pending; MOU is the new top target |

### Step F. Sequencing

1. **Now, no approval needed:** A1 (done), A4, A5, B1, D1 through D3, and appending rows 55–71.
2. **Your decision:** the A2 and A3 folder, and whether row 55, 57, or both are immediate-fix exceptions.
3. **On your sweep instruction:** rows 55–69 and 71 across the papers, with Step E finding aids.
4. **Records:** a new request for the MOU and the 1992 Snapshot. The best routes are probably DCF and State Archives; they need drafts and your approval before sending.
