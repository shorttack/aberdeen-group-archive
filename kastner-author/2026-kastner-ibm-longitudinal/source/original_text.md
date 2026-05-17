# IBM Corporation Across Six Decades of the Kastner Archive: Mainframe Survival, Platform Pivots, and the Services Transformation

> Archived from: ibm_longitudinal_study_source.md
> Original publication date: 2026-05-17
> Author: Peter S. Kastner (assembled with Perplexity Computer using archival-ingest v16)

---

## Original Document Text

# IBM Corporation Across Six Decades of the Kastner Archive: Mainframe Survival, Platform Pivots, and the Services Transformation

**Study type:** longitudinal-entity-study (second archive-as-protagonist framework study; follows Intel builder template)
**Author:** Peter S. Kastner (assembled with Perplexity Computer using archival-ingest v16)
**Date:** 2026-05-17
**License:** CC-BY-4.0
**Companion wiki page:** `ibm-corporation-longitudinal`
**Cross-references:** [[kastner-prescience-methodology-demo]] · [[kastner-top-100-economic-calls]] · [[kastner-core-arguments-framework]] · [[2026-kastner-intel-longitudinal-776f7e]]

---

## 1. Why IBM as the second single-entity study

IBM is the most-observed company in the Kastner IT Research Archive, with 1,054 observations across 174 distinct studies spanning 1967–2026 and 724 IBM-vendor technology rows. This is nearly twice the Intel count (562 observations / 102 studies), reflecting the single most consequential relationship in Kastner's forty-year analyst career.

IBM was the firm against which all other enterprise technology vendors were measured. In the 1980s and early 1990s, the defining question of the IT market was: *when will IBM mainframes be displaced?* The archive contains the contemporaneous record of those predictions — and the forty-year outcome.

The study follows the Intel builder template: eleven thematic threads, per-thread confidence histograms with named exemplars, a prediction-vs-outcome scorecard, a technology emergence/decline matrix, and full replication instructions via DuckDB.

---

## 2. Headline result

| Metric | Value |
|---|---|
| IBM observations in archive | **1,054** |
| Distinct studies | **174** |
| Decade span | **1967 → 2026 (6 decades)** |
| Viability predictions about IBM | 98 |
| Actual-outcome rows about IBM | 115 |
| Verified outcomes | 51 |
| Formally-tagged refuted outcomes | **0** |
| IBM-vendor technology rows | 724 |
| Decade with highest IBM coverage | 1990s — 659 observations |
| Top single IBM study | `aberdeen-1995-ibm-as400-sap-r3` (80 obs) |

The **zero IBM refutations** contrast with Intel's 9.7% refutation rate. This is not because IBM was always right — IBM's Watson Health was a visible failure, and the OS/2 strategy was a documented blunder. It reflects a deeper pattern: IBM's institutional durability as an analyst subject means that even when IBM was wrong, *IBM as a company* survived and adapted. The archive has plenty of IBM product failures; it has no instance of an IBM entity-level prediction being formally tagged as refuted.

---

## 3. The six-decade arc

### 3.1 Coverage by decade

| Decade | Studies | Observations | Dominant threads |
|---|---:|---:|---|
| 1960s | 5 studies | 5 obs | System/360 delivery failures; mainframe pricing |
| 1970s | 1 study | 1 obs | 4300 family; SNA |
| 1980s | ~22 studies | 50 obs | Mainframe displacement prediction; AS/400 launch; PS/2 |
| 1990s | ~100 studies | 659 obs | AS/400 viability; OS/2 vs NT; DB2; services pivot; DEC/HP competition |
| 2000s | ~50 studies | 238 obs | IBM services leadership; Linux bet; Rational/Tivoli acquisitions; Watson origins |
| 2010s | ~10 studies | 14 obs | Watson AI; hybrid cloud; Kyndryl precursor |
| 2020s | ~5 studies | 21 obs | Watson Health failure; Red Hat/OpenShift; Kyndryl spinout; quantum |

### 3.2 The three IBMs

1. **IBM-as-Mainframe-Incumbent (1964–1992).** System/360 architecture makes IBM the defining enterprise computing platform. Mainframe displacement is predicted from 1987 onward but never materializes. RISC/Unix challenges are documented; IBM AS/400 launched as midrange alternative.

2. **IBM-as-Transformer (1993–2012).** Gerstner arrives, cancels the planned breakup, pivots to services. ISSC becomes IBM Global Services; PwC Consulting acquired; Linux bet placed; OS/2 abandoned; ThinkPad sold to Lenovo; x86 server business flagged for divestiture. IBM becomes the world's largest IT services firm.

3. **IBM-as-Cognitive-Cloud (2013–2026).** Watson AI over-promises and partially fails; Watson Health sold 2022. Red Hat acquired 2019 for $34B (largest IBM acquisition). Kyndryl spun out 2021. IBM hybrid cloud / AI positioning around watsonx and OpenShift is the current strategic thesis.

---

## 4. Eleven thematic threads

### THREAD-1 — Mainframe Survival (1987–2026)

**Claim.** IBM mainframes would be displaced by x86/RISC Unix platforms within the 1988–2000 prediction horizon.

**Filter spec.**
```
entity_id IN (ibm*ids)
AND text_contains('mainframe','z/os','zseries','os/390','mvs','system/360',
                  'system/370','parallel sysplex','escon','big iron')
```

**Population.** 126 obs; verified 10 / high 105 / medium 11 / refuted 0. Confidence-weighted: **100% technically** — zero refuted outcomes, but the main directional prediction (displacement) has been **counter-factually false for 39 years**.

**Named predictions and outcomes:**
- 1987 prediction → "Mainframe displacement: not a matter of whether but when; 10-15 year horizon" (high confidence as of 2026 — still pending)
- 1993 prediction → "IBM mainframes will be gradually phased out over next decade" (medium)
- 1998 verified outcome → "IBM S/390 evolved to zSeries (2000) then IBM Z; never discontinued"
- 2022 verified outcome → "IBM z16 actively sold; z17 roadmap confirmed; $2B+ annual revenue"
- 2024 high outcome → "Parallel Sysplex still the highest-availability commercial computing standard"
- 2025 high outcome → "CICS TS 6.3 released; 56-year-old product; oldest continuously-shipped enterprise software"

**Reading.** The mainframe thread is the archive's most striking ARG-1 counter-example. The prediction of mainframe displacement — the defining consensus of the 1988–2000 IT analyst community — was wrong. IBM's mainframe survived by *becoming the economic winner* for specific high-availability, high-throughput, compliance-heavy workloads where x86/Linux alternatives remain more expensive at total cost of ownership. The archive documents both the original prediction and the 39-year-and-counting counter-factual.

**Proof studies.** `volume-1-ch06-dec-mainframes-last-stand-1987-1988` · `aberdeen-1995-ibm-as400-sap-r3` · `10ibmiss-f66945` · `ibmtpc92-c32789`

---

### THREAD-2 — AS/400 & Midrange (1989–2026)

**Claim.** The AS/400 was a platform at risk from Windows NT and Unix; its long-term viability was contested throughout the 1989–2002 archive window.

**Filter spec.**
```
entity_id IN (ibm*ids)
AND text_contains('as/400','as400','iseries','i-series','rs6000','rs/6000',
                  'aix','power systems','db2/400','system/38')
```

**Population.** 348 obs — the largest single thread in the entire IBM archive. Verified 17 / high 302 / medium 25 / refuted 0. **This thread alone accounts for 33% of all IBM observations.**

**Named predictions and outcomes:**
- 1989 prediction → "AS/400 lacks a growth path today; multiple-AS/400 cluster architecture an awkward workaround" (high)
- 1995 prediction → "AS/400 + SAP R/3 credibility requires sub-5-minute response at 1,000-user scale" (Aberdeen benchmark study)
- 1997 prediction → "RS/6000 commercial growth to continue as datacenter Unix consolidation proceeds" (high)
- 2008 verified outcome → "iSeries merged into Power Systems as IBM i"
- 2014 verified outcome → "IBM sold x86/Netfinity server to Lenovo for $2.1B" (strategic exit from commodity)
- 2026 high outcome → "IBM i continues on Power10; installed base 150,000+ systems worldwide"

**Reading.** The AS/400 thread parallels the mainframe thread: a platform repeatedly predicted to be displaced, which instead evolved through four brand generations (AS/400 → iSeries → System i → IBM i) and is still actively sold in 2026. The Aberdeen 1995 SAP R/3 benchmark study (80 obs) is the single largest IBM-study in the archive and the primary proof of AS/400 enterprise credibility at the moment of maximum NT competitive pressure.

**Proof studies.** `aberdeen-1995-ibm-as400-sap-r3` · `sun-as400-main-report-2002-c37e2a` · `aberdeen-1996-evaluating-system36-migration-strategies` · `1997-the-new-as-400e-series-aa9cac` · `ibm-rs6000-midran~1-88f049`

---

### THREAD-3 — OS/2 & PC Exit (1993–2014)

**Claim.** IBM's conflicted OS strategy (OS/2 vs NT) was a strategic misstep, and IBM would exit the consumer/commodity PC hardware business.

**Filter spec.**
```
entity_id IN (ibm*ids)
AND text_contains('os/2','os2','warp','thinkpad','ps/2','microchannel',
                  'ibm pc','x-series','lenovo','netfinity')
```

**Population.** 44 obs; verified 10 / high 27 / medium 6 / refuted 0. Confidence-weighted: **100% — every major prediction in this thread was verified.**

**Named predictions and outcomes:**
- 1995 prediction → "IBM OS/2 Warp missed the window; can never recover market from Windows 95" (high) → **VERIFIED 2001**
- 1997 prediction → "OS/2 being abandoned despite operational stability" (high) → **VERIFIED 2006 (end of support)**
- 1996 prediction → "IBM's conflicted OS strategy and lack of developer marketing will permanently cede the client OS market" (high) → **VERIFIED**
- 2001 verified outcome → "OS/2 Warp never recovered; mainstream support ended"
- 2005 verified outcome → "IBM sold ThinkPad/PC division to Lenovo for $1.75B"
- 2014 verified outcome → "IBM sold x86 server business to Lenovo for $2.1B"

**Reading.** The OS/2 thread is the archive's cleanest IBM prediction cluster — every prediction was correct. Kastner correctly called OS/2's non-recovery in 1995, four years before IBM formally abandoned it. The two Lenovo divestitures complete IBM's exit from commodity hardware as both predicted and documented.

**Proof studies.** `aberdeen-1996-ibm-os2-warp-server` · `1997-ibm-when-a-pc-is-simply-platform-ov-5e9364` · `1997-digital-ramps-up-for-the-leadership-fb5854`

---

### THREAD-4 — DB2 & Software (1990–2026)

**Claim.** IBM's database and middleware software stack (DB2, Tivoli, WebSphere, MQ, Rational) would be a durable revenue engine independent of hardware.

**Filter spec.**
```
entity_id IN (ibm*ids)
AND text_contains('db2','lotus','websphere','mqseries','mq series',
                  'tivoli','rational','informix','lotus notes','domino')
```

**Population.** 159 obs; verified 9 / high 128 / medium 21 / refuted 0.

**Named predictions and outcomes:**
- 1990 IBM/EDS claim → "Mainframe + DB2 can handle volume at lower perceived risk than Unix/RDBMS" → 1992 **outcome: FAILED** — response times in minutes; corrected over 18 months (`10ibmiss-f66945`)
- 1996 prediction → "Tivoli TME unconvincing without major rearchitecture" → **partially verified** (Tivoli was repeatedly rearchitected)
- 2007 high outcome → "VisualAge discontinued April 30 2007; Eclipse lineage preserved"
- 2015 high outcome → "MQSeries renamed IBM MQ; dominant enterprise messaging standard"
- 2019 high outcome → "IBM sold Lotus Notes/Domino to HCL after 24-year ownership"
- 2026 high outcome → "IBM Db2 family active on cloud and on-premise; 43-year product line"

**Reading.** The DB2/software thread is a slow-burn durability story: WebSphere, MQ, and Db2 are still active after 25–43 years. The one notable near-miss is the Tivoli rearchitecture — Kastner's 1996 skepticism was directionally correct (Tivoli was indeed repeatedly rearchitected) but the product survived. The IBM/EDS mainframe DB2 failure (1992) is the clearest single IBM product failure documented in the archive with a named outcome.

**Proof studies.** `aberdeen-1995-ibm-db2-common-server` · `10ibmiss-f66945` · `1997-ibm-information-integration-family--29351c` · `1997-ibm-business-intelligence-family-pr-43c37e`

---

### THREAD-5 — Services Transformation (1993–2021)

**Claim.** IBM would pivot from a hardware company to a services-led company, with IBM Global Services becoming the world's largest IT services organization.

**Filter spec.**
```
entity_id IN (ibm*ids, ibm-global-services, ibm-issc, ibm-bcs, kyndryl)
AND text_contains('global services','igs','issc','outsourcing',
                  'ibm services','business consulting','gts','managed services')
```

**Population.** 35 matching observations (tight filter); verified 3 / high 27 / medium 5 / refuted 0.

**Named predictions and outcomes:**
- 1993 verified outcome → "Gerstner cancels IBM breakup; pivots to services strategy"
- 2000 prediction → "IBM services revenue will grow; IBM GTS will become largest IT services firm" (high) → **VERIFIED 2005**
- 2002 high outcome → "IBM acquired PwC Consulting for $3.5B; became IBM Business Consulting Services"
- 2005 verified outcome → "IBM became world's largest IT services firm; services exceeded 50% of revenue"
- 2021 verified outcome → "IBM spun out managed infrastructure services as Kyndryl (NYSE: KD)"

**Reading.** The services transformation is the **strongest single prediction cluster in the IBM archive** and one of the strongest in the entire Kastner corpus. The directional call — IBM services will overtake IBM hardware — was correct at the decade scale, the revenue scale, and the organizational scale. The Kyndryl spinout (2021) marks the completion of the transformation: IBM is now an AI/hybrid-cloud company, not a services-plus-hardware conglomerate.

**Proof studies.** `aberdeen-1996-ibm-transformation-business-machines-information-service` · `ibm-aberdeen-wip-deck-2-704ff9` · `ibm-major-account-plan-8-cc6400`

---

### THREAD-6 — Linux & Open Source (2000–2026)

**Claim.** IBM's billion-dollar Linux investment would transform open-source credibility, give IBM cloud-native leverage, and ultimately be expressed as the Red Hat acquisition.

**Filter spec.**
```
entity_id IN (ibm*ids, ibm-linux, red-hat)
AND text_contains('linux','open source','eclipse','ibm linux',
                  'billion dollar','gnu/linux','open standards ibm')
```

**Population.** 19 obs; verified 1 / high 16 / medium 2 / refuted 0.

**Named predictions and outcomes:**
- 1997 prediction → "IBM Java/VisualAge strategy key to IBM network-computing success" (medium) → partially verified
- 2000 verified outcome → "IBM $1B Linux investment; mainframe Linux, WebSphere Linux, DB2 Linux all delivered"
- 2001 high outcome → "Eclipse IDE origin: VisualAge evolved into Eclipse; donated to open source 2004"
- 2019 high outcome → "IBM acquired Red Hat for $34B — largest IBM acquisition; Linux bet ultimately expressed at $34B scale"
- 2026 high outcome → "Red Hat OpenShift serving 4,000+ enterprise customers; 90%+ Fortune 500 on hybrid cloud"

**Reading.** The open-source thread connects two dots across 26 years: the 2000 Linux bet and the 2019 Red Hat acquisition. They are the same strategic thesis at different scales. The archive documents the 2000 entry point; the Red Hat outcome is the verification.

**Proof studies.** `1997-ibm-application-development-product-895c4d` · `ibm-scm-murray2-tm-4a0fbf`

---

### THREAD-7 — Watson & AI (1997–2026)

**Claim.** IBM Watson would become the world's leading enterprise AI platform, especially in healthcare and regulated industries.

**Filter spec.**
```
entity_id IN (ibm*ids, ibm-watson, ibm-watson-health, ibm-watsonx)
AND text_contains('watson','cognitive computing','jeopardy','watson health',
                  'deep blue','ibm ai','watsonx')
```

**Population.** 7 matching observations (narrow filter); verified 0 / high 4 / medium 3 / refuted 0. **This thread is sparse in the archive — the Watson era (2011-2022) is outside the main Kastner Aberdeen observation window.**

**Named predictions and outcomes:**
- 1997 outcome → "IBM Deep Blue defeated Kasparov in May 1997 chess match" (runs on IBM RS/6000 SP2)
- 2011 high outcome → "IBM Watson defeated Jeopardy champions Ken Jennings and Brad Rutter"
- 2013 prediction → "Watson will dominate enterprise AI in healthcare and financial services" (medium) → **partially refuted qualitatively**
- 2015 prediction → "Watson Health will transform oncology; standard for AI-assisted diagnosis" (medium) → **qualitatively refuted by Watson Health sale 2022**
- 2022 high outcome → "IBM Watson Health sold to Francisco Partners"
- 2023 high outcome → "IBM rebranded as watsonx AI platform; watsonx.ai, watsonx.data, watsonx.governance"

**Reading.** Watson is IBM's most visible partial-miss. No formal 'refuted' tag appears in the archive because the IBM entity survived; but Watson Health's failure and the WatsonX reboot represent the clearest outcome reversal in IBM's post-2010 history. Deep Blue (1997) and the Jeopardy win (2011) are the genuine AI achievements; the commercial Watson Health story is the failure. This thread is **explicitly marked as a build-out target** — future studies should populate Watson-era observations more densely.

**Proof studies.** Sparse; archive build-out needed. Cross-reference `ENT-S2-009` (IBM Watson Health entity).

---

### THREAD-8 — Hybrid Cloud & Red Hat (2013–2026)

**Claim.** IBM would use the SoftLayer acquisition and then the Red Hat acquisition to define the hybrid-cloud market and challenge AWS/Azure.

**Population.** ~5 observations (extremely sparse — this is a post-2013 story; archive predates main coverage window). High 2 / verified 2 / refuted 0. **Build-out target.**

**Named outcomes:**
- 2013 high outcome → "IBM acquired SoftLayer for $2B; became IBM Cloud 2017"
- 2019 high outcome → "IBM closed $34B Red Hat acquisition; largest IBM acquisition ever"
- 2021 high outcome → "Kyndryl spinout enables IBM cloud focus without managed-infrastructure drag"
- 2026 high outcome → "Red Hat OpenShift at 4,000+ customers; IBM's primary hybrid-cloud delivery vehicle"

**Reading.** The archive has not yet caught up to the 2019–2026 hybrid-cloud story. This thread is deliberately sparse — future studies should land here as IBM hybrid-cloud outcomes mature. The strategic thesis (IBM = enterprise hybrid cloud via Red Hat) is IBM's current identity; the archive verification of that thesis is in-flight.

---

### THREAD-9 — Quantum Computing (2016–2026)

**Claim.** IBM would establish quantum computing leadership via IBM Q / Qiskit cloud access and the quantum volume roadmap.

**Population.** 2 observations (near-zero — entirely post-archive window). **Build-out target.**

**Named outcomes:**
- 2016 high outcome → "IBM Q Experience launched; first publicly accessible quantum computer"
- 2021 high outcome → "IBM Eagle 127-qubit processor released"
- 2023 high outcome → "IBM Condor 1121-qubit processor; largest superconducting quantum processor"
- 2023 medium prediction → "IBM roadmap: 100,000-qubit fault-tolerant system by 2033"

**Reading.** The archive has no substantive quantum observations because quantum computing became a named IBM strategy after the main Kastner archive window. This thread is the IBM equivalent of Intel's THREAD-11 (foundry pivot) — a future-state build-out target. As of May 2026, IBM has the most accessible quantum platform (Qiskit, IBM Quantum Network) but enterprise quantum advantage remains undemonstrated.

---

### THREAD-10 — TPC Benchmarks (1992–2003)

**Claim.** IBM was a dominant TPC benchmark participant and Kastner used TPC results extensively as a competitive-analysis anchor.

**Filter spec.**
```
entity_id IN (ibm*ids)
AND text_contains('tpc','tpmc','tpc-c','tpc-a','benchmark result')
```

**Population.** 48 obs; high 39 / medium 8 / verified 0 / refuted 0.

**Named predictions and outcomes:**
- 1992 verified personal-recollection → "Kastner served as TPC audit client for IBM; found needle in IBM performance data IBM itself missed" — highest direct Kastner-IBM technical engagement
- 1995 high outcome → "AS/400 SAP R/3 TPC-C demonstrated at 1,000-user scale" (`aberdeen-1995-ibm-as400-sap-r3`)
- 2003 high outcome → "IBM zSeries holds TPC-C world record at >4M tpmC"
- 1997 prediction → "IBM positioned in top 3-5 absolute commercial performance on TPC-C across all platform tiers" (high)

**Reading.** The TPC benchmark thread is where Kastner's analytical expertise most directly intersected with IBM's product claims. The 1992 audit engagement — finding a performance anomaly in IBM's own data — is the single most technically specific Kastner-IBM direct interaction in the archive. TPC remains active; IBM continues to publish benchmark results.

**Proof studies.** `ibmtpc92-c32789` · `aberdeen-1995-ibm-as400-sap-r3` · `10ibmiss-f66945`

---

### THREAD-11 — Kastner Direct Engagements (1992–2009)

**Claim.** Kastner had direct executive access to IBM at VP and SVP level; IBM AR trained by Kastner; IBM as a high-quality analyst relations account.

**Population.** 34 matching observations; verified 4 / high 24 / medium 5 / refuted 0.

**Named direct engagements:**
- 1992–1996 verified → "Kastner served as TPC audit client for IBM benchmark submissions"
- 1996 verified → "One-on-one briefing with IBM SVP John M. Thompson; Kastner finds needle in IBM performance data IBM itself had missed"
- c.2000 verified → "Kastner sat at Ginni Rometty's left at six-person executive dinner (Rometty then GM of IBM Services)"
- c.2003 verified → "Post-2000 Aberdeen training: Kastner and Logan took IBM Somers session; Kastner trained IBM AR staff on analyst engagement excellence"
- ongoing high → "IBM 'no one ever got fired for buying IBM' brand trust heuristic — tracking persistence"

**Reading.** The IBM AR relationship was one of Kastner's most substantive — IBM invested in analyst training, gave direct senior-executive access, and maintained a structured program. This contrasts with the AR vulnerability described in Aberdeen memoir materials. IBM is the positive exemplar of how AR programs should work.

**Proof studies.** `10ibmiss-f66945` · `ibm-major-account-plan-8-cc6400` · Memoir chapter materials.

---

## 5. Technology emergence and decline matrix

The 724 IBM-vendor tech rows produce a rich emergence/decline timeline.

| Decade | Emerging (then) | Now status | Notes |
|---|---|---|---|
| 1960s | System/360, CICS, SNA | obsolete/evolved/active | System/360 architecture lives in z/OS; CICS still shipping 2026 |
| 1970s | System/370, MVS, DB2 precursors | obsolete/evolved | MVS evolved into z/OS; DB2 lineage to Db2 |
| 1980s | AS/400, RS/6000, AIX, OS/2, PS/2, SNA declining | mixed | AS/400 active as IBM i; AIX active; OS/2 ended 2006; SNA legacy |
| 1990s | Lotus Notes, WebSphere, MQSeries, Tivoli, SP2, DB2/400 | mixed-active | Most still shipping under evolved names; Tivoli brand retired |
| 2000s | Eclipse, Rational, Blade servers, Linux on Z | active/evolved | Eclipse Foundation active; Rational to IBM ELM; Linux on Z mature |
| 2010s | Watson, SoftLayer/IBM Cloud, Bluemix | partially-evolved | Watson → watsonx; SoftLayer → IBM Cloud; Bluemix → IBM Cloud |
| 2020s | watsonx, OpenShift, IBM Quantum, IBM Z16 | active/emerging | All current IBM strategic platforms |

### 5.1 Technologies IBM created and discontinued

**Killed or exited by IBM:**
- OS/2 (general support ended 2006); IBM PC division (sold Lenovo 2005); x86 server business (sold Lenovo 2014); VisualAge (discontinued 2007); IBM SNA as primary protocol (displaced ~2000); Bluemix brand (absorbed into IBM Cloud); Rational brand (absorbed into IBM Engineering); Watson Health (sold 2022); Lotus brand (sold to HCL 2019); IBM ThinkPad (sold to Lenovo 2005); IBM Netfinity brand (sold to Lenovo 2014)

**Currently active (2026):**
- IBM z16 / z/OS 3.1 / z/Architecture; IBM i on Power10; IBM AIX 7.3; IBM Db2; IBM MQ 9.3; IBM CICS TS 6.3; IBM Parallel Sysplex; IBM WebSphere/Liberty; Red Hat OpenShift; IBM watsonx; IBM Quantum (Qiskit); IBM Cloud

**Evolved (technology preserved, brand retired):**
- MVS → OS/390 → z/OS; System/360 architecture → z/Architecture; AS/400 → iSeries → System i → IBM i; RS/6000 → Power Systems; VisualAge → Eclipse; MQSeries → IBM MQ; Tivoli TME → IBM Observability/AIOps; Watson → watsonx; SoftLayer → IBM Cloud; Bluemix → IBM Cloud Functions; Rational → IBM Engineering Lifecycle Management; ISSC → IBM Global Services → IBM Consulting + Kyndryl

### 5.2 The asymmetry

IBM killed or transferred roughly 11 of its own major technologies in the archive's coverage window. Around 14 remain active or evolved. The **survival rate (~56%) is significantly better than Intel's 2:1 kill ratio** — reflecting IBM's pattern of brand retirement and technology preservation rather than outright architectural abandonment. IBM's deepest technologies (System/360 architecture, CICS, DB2 lineage) have survived 40–60 years.

---

## 6. Kastner predictions about IBM: the scorecard

Across 98 viability-prediction rows directly tagged to IBM:

| Confidence | Count | % |
|---|---:|---:|
| Verified | 51 | 48.6% |
| High | 857 | — (all obs, not just predictions) |
| Refuted | 0 | 0% |

The zero-refuted prediction rate is the most striking statistical finding. Compared to Intel's 9.7% refutation rate, IBM's 0% rate reflects:

1. **IBM's institutional durability.** Predicting IBM failure at the entity level has never been correct in the archive window.
2. **Platform longevity.** IBM's core technologies (mainframe, DB2, MQ, CICS) have continuously evolved rather than being discontinued, making technology-level predictions difficult to formally refute.
3. **Services pivot absorber.** As hardware revenue declined, IBM pivoted to services — so hardware-displacement predictions were technically correct but IBM-as-entity survived.

**Named verifications:**
- Services transformation → verified (world's largest IT services firm by 2005)
- OS/2 non-recovery → verified (support ended 2001/2006)
- ThinkPad divestiture → verified (Lenovo 2005)
- x86 server divestiture → verified (Lenovo 2014)
- AS/400 iSeries rebrand → verified (Power Systems IBM i 2008)

**Named qualitative near-misses (not formally tagged refuted):**
- Mainframe displacement (1987 prediction) — still not materialized 39 years later
- Watson Health enterprise AI leadership — not achieved; Watson Health sold 2022
- OS/2 enterprise recovery (1993 loyal-account prediction) — partially accurate but limited in scope

---

## 7. How IBM's transformation mapped to Kastner's predictions

### 7.1 The 1987 mainframe displacement call

> "Mainframe displacement is not a matter of whether but when."

**Outcome:** the most famous wrong call in the analyst industry. IBM mainframes are still shipping in 2026 — 39 years after the prediction. The archive documents both the prediction and the 39-year non-event. This is not a Kastner-specific miss; it was the consensus analyst prediction of the era.

**Why it was wrong:** IBM mainframes competed and won on TCO for specific high-availability, high-throughput workloads — large banks, insurance companies, and government agencies where the cost of x86 Linux equivalency at the same uptime SLA exceeded the mainframe cost. The economic winner argument (ARG-1) ran in IBM's favor, not against it.

### 7.2 The services pivot call

> "IBM under Gerstner will pivot successfully to services as hardware revenues decline."

**Outcome:** verified. IBM Global Services became the world's largest IT services firm. The PwC Consulting acquisition ($3.5B, 2002), the Kyndryl spinout ($19B valuation, 2021), and IBM's current hybrid-cloud positioning are all downstream of this call.

### 7.3 The OS/2 abandonment call

> "IBM OS/2 Warp missed the window. Can never recover."
> — Kastner, 1995

**Outcome:** verified. IBM ended mainstream OS/2 support 2001, general support 2006. Every prediction in the OS/2 thread was correct. This is Kastner's clearest IBM call cluster.

### 7.4 The Watson AI call

The archive tracks the Watson Health failure without a formal refutation tag. The qualitative reading is clear: IBM over-promised on Watson's enterprise AI capabilities, especially in healthcare. Watson Health was sold in 2022 — a visible strategic failure. The WatsonX reboot in 2023 is IBM's acknowledgment.

### 7.5 The synthesis

IBM is the archive's most complex single entity because it has been right, wrong, and partially-right in roughly equal measure — yet the entity always survived. The archive correctly predicted the services pivot, the OS/2 abandonment, and the PC exit. It incorrectly predicted mainframe displacement. It over-estimated Watson Health. In every case, IBM as a company continued operating. The zero-refutation rate at the entity level is the fundamental IBM pattern.

---

## 8. How to use this study

| Mode | Steps |
|---|---|
| **Replicate a thread** | Pick a thread. Take its filter spec. Run against `_master_observations.csv` filtered to IBM entity IDs. Compare population to published count. |
| **Audit a Kastner IBM call** | Find the prediction obs_id in §6. Trace forward via `entity_id` and `metric_name` to the matched actual-outcome row. |
| **Audit an IBM company claim** | Find an IBM-issued claim (e.g., Watson Health oncology). Look for corresponding outcome rows. |
| **Extend** | Add THREAD-12 (e.g., IBM hybrid cloud ROI from 2024-onward). Define keywords. Run the filter. Publish. |
| **Build out Watson/Cloud/Quantum** | Threads 7, 8, 9 are explicitly sparse — add targeted studies for these eras. |

---

## 9. Methodology notes

- **Entity disambiguation.** "IBM" is one of the archive's most consistently-tagged entities but still appears under 72 distinct entity_id values (ibm, ibm-corporation, ibm-corp, ENT-002, ENT-003, etc.). The canonical filter is the 72-ID set published in this study's `observations.csv`.
- **Thread membership is multi-valued.** An observation can belong to several threads. Thread populations therefore sum to more than 1,054.
- **Watson thread sparse by design.** The Watson era (2011-2022) is outside the main Kastner/Aberdeen archive window. Future studies will fill in this thread.
- **Hybrid cloud and quantum threads are build-out targets.** Both threads contain fewer than 10 observations and are explicitly flagged for future expansion.
- **Zero refutations is not zero failures.** IBM had documented product failures (Watson Health, OS/2, mainframe DB2 performance failure at EDS) but none resulted in IBM entity-level refutations. The distinction between product failure and entity refutation is methodologically important.

---

## 10. Replication

```bash
git clone https://github.com/shorttack/aberdeen-group-archive
cd aberdeen-group-archive
duckdb <<SQL
  CREATE TABLE obs AS SELECT * FROM '_master_observations.csv';
  CREATE TABLE ent AS SELECT * FROM '_master_entities.csv';
  -- Build IBM entity ID set (72 IDs)
  CREATE TABLE ibm_ids AS
    SELECT DISTINCT entity_id FROM ent
    WHERE LOWER(TRIM(entity_name)) IN ('ibm','ibm corporation','international business machines',
                                        'ibm corp.','international business machines corporation')
       OR LOWER(entity_id) LIKE 'ibm%'
       OR entity_id IN ('enc-03','e89-03','e91-03','ent-001','ent-005','ent-03',
                        'ENT-002','ENT-003','ENT-004','ENT-005','ENT-006','ENT-008',
                        'e2-04','e3-05','e4-01','e5-01','ENT-IBM','IBM','IBM-SP2');
  -- Headline count
  SELECT COUNT(*) AS ibm_obs FROM obs WHERE entity_id IN (SELECT entity_id FROM ibm_ids);
  -- THREAD-1 mainframe
  SELECT COUNT(*) AS mainframe_obs, confidence
  FROM obs
  WHERE entity_id IN (SELECT entity_id FROM ibm_ids)
    AND (metric_name ILIKE '%mainframe%' OR metric_value ILIKE '%mainframe%'
         OR metric_name ILIKE '%zseries%' OR metric_name ILIKE '%z/os%')
  GROUP BY confidence;
SQL
```

---

## 11. Limitations

1. **Threads 7, 8, 9 are structurally undersized.** Watson, hybrid cloud, and quantum computing all post-date the main Kastner/Aberdeen archive window. The archive's 659 observations in the 1990s vs 14 in the 2010s reflects analyst career peak, not IBM strategic importance.
2. **Zero refutations may mask qualitative failures.** Watson Health was a strategic failure but is not tagged 'refuted' at the entity level. Future studies should consider adding a `qualitative_miss` field to capture this.
3. **Thread-2 (AS/400) dominates the archive.** 348 of 1,054 IBM observations (33%) are AS/400/midrange — reflecting Kastner's Aberdeen specialty in that platform tier. Other IBM platform threads are relatively thinner.
4. **Entity ID fragmentation.** IBM appears under 72 distinct entity_id values. The canonical ID set published here is based on the May 2026 archive state; future entity consolidation passes may shift counts.
5. **IBM-issued claims vs Kastner-issued predictions not formally tagged.** The Watson Health prediction (a mix of IBM marketing and analyst expectations) illustrates the tagging problem. A future audit study should separate IBM-issued promises from Kastner-issued predictions.

---

## 12. Cross-references

- [[kastner-core-arguments-framework]] — ARG-1 (economic winner) runs in IBM's favor for mainframe; ARG-2 (proprietary platforms fund displacement) applies to OS/2 and PC exit
- [[kastner-top-100-economic-calls]] — services transformation and x86 server exit both appear in top-100 list
- [[kastner-prescience-methodology-demo]] — methodology pattern used to score IBM predictions in §6
- [[2026-kastner-intel-longitudinal-776f7e]] — Intel builder template; IBM study follows same 11-thread structure
- `aberdeen-1995-ibm-as400-sap-r3` — 80 obs; largest single IBM study in archive; AS/400 benchmark credibility
- `10ibmiss-f66945` — 28 obs; IBM ISS study; mainframe DB2 at scale; EDS performance failure
- `aberdeen-1996-ibm-transformation-business-machines-information-service` — services pivot analysis


---

## Frictionless Data Package Metadata

> Auto-generated by Archival Ingest Skill v16

### Study Record

| Field | Value |
|-------|-------|
| study_id | 2026-kastner-ibm-longitudinal |
| title | IBM Corporation Across Six Decades of the Kastner Archive: Mainframe Survival, Platform Pivots, and the Services Transformation |
| author | Peter S. Kastner (assembled with Perplexity Computer using archival-ingest v16) |
| date | 2026-05-17 |
| type | topic-analysis |
| subject_domain | computing-industry-history |
| methodology | archive-mining,longitudinal-single-entity,prediction-vs-outcome-scorecard,thematic-thread-decomposition,wiki-driven-replication |
| source_file | ibm_longitudinal_study_source.md |
| abstract | A longitudinal archive study of IBM Corporation across six decades of the Kastner IT Research Archive. IBM is the single most-referenced company in the archive — 1,054 observations across 174 distinct studies spanning 1967 to 2026, with 724 IBM-vendor technology rows. The study decomposes IBM coverage into eleven thematic threads (mainframe survival, AS/400 & midrange, OS/2 & PC exit, DB2 & software pivot, services transformation, Linux & open source bet, Watson & AI, hybrid cloud & Red Hat, quantum computing, TPC benchmarks, and Kastner direct engagements), computes per-thread confidence histograms with named exemplars and refutations, and audits how IBM's actual transformation mapped to Kastner's documented predictions. Headline finding: IBM's mainframe was documented as 'doomed' in 1987 yet remains the archive's most durable technology-survival story through 2026; the services pivot from 'Big Blue hardware' to the world's largest IT services firm was predicted correctly; Watson AI significantly underdelivered its 2013-era promises. The archive contains zero formally-tagged IBM refutations in the viability-prediction rows — a contrast with Intel's 9.7% refutation rate that reflects IBM's unique institutional durability as an analyst subject. This is the second longitudinal single-entity study in the archive, following the Intel builder template. |
| license | CC-BY-4.0 |
| importance | high |
| importance_rationale | Second longitudinal single-entity study in the archive; IBM is the most-observed company and provides the strongest test of mainframe displacement predictions — the defining call of the 1988-1993 Kastner corpus. |
| relevance | high |
| relevance_rationale | IBM's hybrid-cloud and Red Hat pivot, Watson Health exit, and quantum computing investments are all active strategic bets as of 2026. The archive mainframe-survival thread is directly relevant to organizations still running z/OS workloads. |
| prescience | high |
| prescience_rationale | Services transformation prediction (THREAD-5) verified; mainframe displacement timeline (THREAD-1) refuted in the strongest possible way — IBM mainframes are still shipping in 2026. OS/2 abandonment prediction (THREAD-3) verified. Watson AI overreach (THREAD-7) partially refuted. |

### Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | high | Second longitudinal single-entity study in the archive; IBM is the most-observed company and provides the strongest test of mainframe displacement predictions — the defining call of the 1988-1993 Kastner corpus. |
| **Relevance** | high | IBM's hybrid-cloud and Red Hat pivot, Watson Health exit, and quantum computing investments are all active strategic bets as of 2026. The archive mainframe-survival thread is directly relevant to organizations still running z/OS workloads. |
| **Prescience** | high | Services transformation prediction (THREAD-5) verified; mainframe displacement timeline (THREAD-1) refuted in the strongest possible way — IBM mainframes are still shipping in 2026. OS/2 abandonment prediction (THREAD-3) verified. Watson AI overreach (THREAD-7) partially refuted. |

### Prescience Detail

See observations.csv: 21 viability-prediction rows.

### Entities Referenced (16)

| Entity | Type | Status | Successor |
|--------|------|--------|-----------|
| IBM Corporation | company | active |  |
| IBM Global Services | company | active-renamed | IBM Consulting + Kyndryl |
| IBM ISSC (Integrated Systems Solutions Corp.) | company | absorbed | IBM Global Services |
| IBM AS/400 Division | company | evolved | IBM Power Systems (IBM i) |
| IBM Tivoli | company | absorbed | IBM Software (Observability/AIOps) |
| IBM Rational | company | absorbed | IBM Engineering Lifecycle Management |
| IBM Business Consulting Services | company | renamed | IBM Consulting |
| Kyndryl | company | active |  |
| Red Hat | company | acquired | IBM (subsidiary) |
| Lenovo (IBM PC/x86 buyer) | company | active |  |
| IBM Watson Health | company | divested | Francisco Partners (2022) |
| Peter S. Kastner | person | active |  |
| John M. Thompson | person | retired |  |
| Ginni Rometty | person | retired |  |
| Lou Gerstner | person | retired |  |
| IBM Somers (analyst relations team) | company | active |  |

### Technologies Referenced (29)

| Technology | Category | Vendor | Lifecycle (at study) | Lifecycle (current) |
|------------|----------|--------|---------------------|---------------------|
| IBM System/360 | platform | IBM | obsolete | discontinued |
| IBM System/370 | platform | IBM | obsolete | discontinued |
| IBM 4341 (4300 family) | platform | IBM | obsolete | discontinued |
| IBM 3090 Mainframe | platform | IBM | mature | discontinued |
| IBM zSeries / IBM Z | platform | IBM | emerging | active |
| IBM OS/390 / z/OS | platform | IBM | emerging | active |
| IBM MVS (Multiple Virtual Storage) | platform | IBM | mature | evolved-to-zos |
| IBM CICS (Customer Information Control System) | application | IBM | mature | active |
| IBM AS/400 (iSeries / IBM i) | platform | IBM | mature | active |
| IBM AIX | platform | IBM | mature | active |
| IBM RS/6000 (POWER) | platform | IBM | mature | active-as-power10 |
| IBM OS/2 Warp | platform | IBM | declining | discontinued |
| IBM DB2 / Db2 | application | IBM | mature | active |
| IBM WebSphere | application | IBM | emerging | active |
| IBM MQSeries (IBM MQ) | application | IBM | mature | active |
| Lotus Notes / Domino | application | IBM | mature | active-as-hcl |
| IBM SP2 (Scalable POWER2) | platform | IBM | mature | discontinued |
| IBM SNA (Systems Network Architecture) | protocol | IBM | declining | legacy-maintained |
| IBM Watson | application | IBM | emerging | partially-divested |
| IBM watsonx | application | IBM | emerging | active |
| Red Hat OpenShift | platform | IBM/Red Hat | emerging | active |
| IBM Quantum (IBM Q / Qiskit) | platform | IBM | emerging | active-research |
| TPC Benchmark (TPC-A, TPC-C, TPC-E) | framework | TPC / IBM (founding member) | active | active |
| Eclipse IDE | framework | IBM (founded) / Eclipse Foundation | emerging | active |
| IBM VisualAge | application | IBM | declining | discontinued |
| IBM Parallel Sysplex | platform | IBM | mature | active |
| PowerPC Architecture | platform | IBM/Apple/Motorola (AIM) | mature | evolved-to-power10 |
| IBM Deep Blue | application | IBM | experimental | discontinued |
| IBM SoftLayer (IBM Cloud) | platform | IBM | emerging | active-as-ibm-cloud |

### Observation Summary

- Total observations: 117
- By type: actual-outcome: 48, analytical-finding: 30, viability-prediction: 21, framework-factor: 11, expert-opinion: 4, longitudinal-decomposition: 3
