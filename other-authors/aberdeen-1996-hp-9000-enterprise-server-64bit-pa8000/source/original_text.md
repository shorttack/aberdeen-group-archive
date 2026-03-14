# HP 9000 Enterprise Server Performance Leadership Again: The 64-bit PA-8000 Has Arrived

> Archived from: https://web.archive.org/web/19970112011513/http://www.aberdeen.com:80/secure/profiles/hp9000/hp9000.htm
> Original publication date: September 17, 1996
> Author: Aberdeen Group

---

## Original Document Text

Hewlett-Packard Company
19091 Pruneridge Avenue
Cupertino, CA 95014
1-408-447-4000 | http://www.hp.com

**September 17, 1996** — In today's enterprise-level computing environment, performance counts. RDBMS (relational database management system) performance is key for user acceptance of a new generation of client-server applications, integrated-process applications, data warehousing applications, batch processing applications, and web-enabled commerce applications. And to obtain the fastest throughput capability today while planning for potentially geometric growth in performance requirements in the future, IS decision makers want to commit their newest applications to the most powerful line of servers possible that run a production-quality, dependable operating environment. And all the core technologies should be acquired from a supplier whose long-term viability and commitment to their success they trust. Within the context of today's RDBMS-centric computing environment — and after several years of telling the industry how good its 64-bit PA-8000 running HP-UX would be for improving the performance of the HP 9000 line — HP today made good on its promises to meet IS executives' requirements for significantly more enterprise server performance.

### Executive Summary

HP today announced the first 64-bit PA-8000-based commercial application servers for its HP 9000 product line. The significance of this announcement lies in the dramatic performance improvement (up to 2.5 times) that users of existing HP 9000 systems can obtain through upgrading and the competitive performance and price/performance advantages HP can now claim in the Unix marketplace.

The PA-8000 processor will be incorporated in HP's D-, K-, T-Class, and EPS servers. It will be shipping in 180MHz and 160MHz versions.

To demonstrate the dramatic effect on performance of the PA-8000 processors, the new K460 server incorporating 4-180MHz PA-8000 processors has now been proven to run at a performance level of **12,321 tpmC** (transactions per minute as defined by the Transaction Processing Council's TPC-C benchmark and audited by an independent expert during HP's testing) with a price/performance of **$186/tpmC**. This performance compares to the former high-end of the K-Class, the very popular K420 built with 4-120MHz PA-7200 processors, that was rated at **4,939 tpmC**. The increase in performance with the PA-8000 represents an approximately **2.5 times improvement** that existing K420 users can capture through a simple in-box upgrade on-site. Similarly, the new PA-8000-based 2-processor D370 is rated at **5,300 tpmC** — 2.3 times the similarly configured PA-7200 based D350.

In a world where a 35% performance improvement per year is considered respectable, a 200%–250% advance from one product generation to the next within a year while maintaining systems compatibility and in-box upgradeability is remarkable.

In addition, HP announced that existing T500 and T520 systems can now be upgraded to the PA-8000 processors and HP will be shipping a replacement for the T500 line, the new T600, in 1Q97. T500/T520 customers will be provided with an allowance for upgrading to PA-8000 processors now and then installing the T600 upgrade into their existing T500/T520 frames when it ships. HP estimates that the T600 will have a performance rating of over **15,000 tpmC** when it is delivered.

T600s will be used as SMP nodes to create the new EPS31 highly parallel processing system to be delivered also in 1Q97. HP projects that a 4-node EPS31 using 48 PA-8000 processors will be capable of delivering performance of over **35,000 tpmC**. Based upon today's published TPC-C results, this performance would make the EPS31 the most powerful commercial application computing system ever delivered — more than doubling the throughput capabilities of HP's current high-end parallel system, the EPS30.

HP is continuing to execute successfully upon its strategy of leading the performance charge in Unix enterprise servers as well as protecting its customers' past investments. It is confident enough in its ability to deliver to show roadmaps that promise faster future processors — the PA-8200 and then the PA-8500 (projected to be double the performance of the PA-8000) followed by the jointly developed HP-Intel P7/Merced processor, anticipated for delivery in servers by mid-1998. In addition, HP is encouraging ISVs to optimize their applications for and customers to install HP-UX 10.2, the operating system that supports the PA-8000, with the assurance that it will be compatible with HP-UX 11.0, delivering very large memory (VLM) support by mid-1997, and HP-UX 11.X — merely a dot-release of version 11 — for supporting the HP-Intel Merced processor.

### CPU Performance Matters

Processor performance matters. A supplier cannot provide its customers with better-than-the-competition's servers unless it has a comparative advantage in processor technology.

The **180MHz PA-8000** has a performance rating of **3,200–3,300 tpm, 11.8 SPECint95, and 20.2 SPECfp95**. This makes it more powerful than any processor available in any general purpose commercial server. By comparison:

| Processor | Speed | TPC-C (tpm) |
|-----------|-------|-------------|
| HP PA-8000 | 180MHz | 3,200–3,300 |
| Intel PentiumPro (Data General Unix) | 200MHz | 1,900–2,000 |
| DEC Alpha DECchip | 400MHz | 1,600–1,700 |
| Sun UltraSPARC | 200MHz | 1,600–1,700 |
| IBM PowerPC 604 | 112MHz | 800–900 |
| SGI R4400 | 250MHz | 500–600 |

### The New PA-8000-based HP Enterprise Servers

The new PA-8000-based server models are described below. The D- and K-Class models are merely a CPU board replacement for existing servers that were specifically designed to be PA-8000 ready. The T600 is a simple upgrade for the T500/T520 that includes both the PA-8000 and new I/O adapters that can be plugged into existing frames.

- **K460**: 4-way midrange server; 12,321 tpmC; flagship product; suitable for majority of RDBMS, OLTP, and web server applications
- **D270/D370**: Low-cost high-performance nodes; D370 at 5,300 tpmC; price/performance web servers
- **T600**: High-end; large user counts and data volumes; >15,000 tpmC (projected 1Q97)
- **EPS31**: 4-node parallel system using T600 nodes; >35,000 tpmC (projected 1Q97)

Aberdeen projects that the PA-8200 may provide a 50% performance increase over the PA-8000 with systems released during 3Q97 and the PA-8500 a 100% increase over the PA-8000 at the end of the first-half of 1998.

### Competitive Positioning

HP's competitive positioning for the new PA-8000-based enterprise server line is simply that it is the industry's most powerful.

**vs IBM**: IBM's newest midrange server RS/6000 R40 (8-CPU PowerPC 604, 112MHz) delivers 5,775 tpmC at $248/tpmC. HP's comparable D370 (2-CPU) delivers estimated 5,300 tpmC at approximately 30% better price/performance.

**vs Sun**: Sun's 12-CPU Ultra Enterprise 5000 rated at 11,466 tpmC vs HP K460 (4-way) at 12,321 tpmC — HP achieves more performance with fewer processors. TPC-C price/performance results within 3% of each other.

**vs NT**: Most powerful Intel/NT Server systems top off at approximately 5,900 tpm — HP's PA-8000 servers merely broaden the performance gap between departmental NT and high-end RDBMS-centric HP 9000s.

**vs IBM RS/6000 SP**: HP will position EPS21 and EPS31 as operational equivalent of parallel MVS but without Y2K issues and costly mainframe support requirements.

### HP's PRISM Blueprint for Enterprise Computing

HP's mantra for building production-quality Unix operating environments is **"PRISM"** — an acronym for **Performance, Resilience, Integration, Security, and Management**.

- **Performance**: PA-8000 processors; new disk array and tape library storage devices
- **Resilience**: Clustering technology (MC/ServiceGuard); high-availability HP-UX features
- **Integration**: Common framework managing HP-UX and Microsoft NT; interoperability standards
- **Security**: Praesidium technology — transaction gateways, smartcards, antivirus, non-repudiation
- **Management**: HP OpenView framework with business partner solutions

### Aberdeen Conclusions

The primary benefit HP's customers will be obtaining from today's announcement is "protection of investment" in terms of hardware, operating environment, applications, and, most importantly, staff knowledge and training. Aberdeen continues to be impressed with HP's ability to deliver on its long-term performance roadmap in a timely manner — and to do so with technology solutions that are refinements and extensions of existing products yet can provide HP customers with significantly improved performance and operational capabilities.

The new HP 9000 64-bit PA-8000-based models demonstrate that HP's continued dedication to the Unix-based enterprise-server marketplace is serving its customers well. Their investments are being protected — their ability to improve application throughput is most often merely an in-box upgrade away — and their supplier is providing a realistic roadmap that makes it easier for them to implement the information technology innovations of the mid-1990s without disrupting their existing operations. Competitors will be hard pressed to match HP across the entire spectrum of PRISM functionality that IS executives are seeking for their business-critical, production applications.

---

*AberdeenGroup, Inc., One Boston Place, Boston, Massachusetts 02108 USA*
*Contact: Chris Stevenson | Voice: (617)723-7890 | Email: stevens@aberdeen.com*
*Copyright © 1996 Aberdeen Group, Inc.*

---

## Frictionless Data Package Metadata

> Auto-generated by Archival Ingest Skill v13

### Study Record

| Field | Value |
|-------|-------|
| study_id | aberdeen-1996-hp-9000-enterprise-server-64bit-pa8000 |
| title | HP 9000 Enterprise Server Performance Leadership Again: The 64-bit PA-8000 Has Arrived |
| author | Aberdeen Group |
| date | 1996-09-17 |
| type | market-study |
| subject_domain | unix-enterprise-servers |
| methodology | benchmarking, competitive-profiling, industry-analysis |
| source_file | 1996 HP 9000 Enterprise Server Performance L... Again_ The 64-bit PA-8000 Has Arrived pr.pdf |
| license | CC-BY-4.0 |

### Abstract

Aberdeen Group evaluates HP's September 1996 announcement of PA-8000-based HP 9000 enterprise servers, documenting benchmark performance results (K460 at 12,321 tpmC — a 2.5x improvement over its PA-7200 predecessor) and positioning HP's PRISM framework as the standard for Unix enterprise server selection.

### Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | high | Documented the first PA-8000 TPC-C benchmark results at a pivotal moment in Unix server competition; the 2.5x performance leap was significant for IS decision-makers. |
| **Relevance** | low | Specific benchmarks and processors are obsolete; HP 9000 discontinued 2003. Retains archival value for 1990s Unix competitive dynamics. |
| **Prescience** | medium | Short-term PA-8200/PA-8500 roadmap largely met; Merced/Itanium delayed 3 years and failed commercially; HP 9000 discontinued 2003. |

### Prescience Detail

**Prediction 1:** PA-8200 performance and delivery timeline
- **Claimed:** 50% performance increase over PA-8000; systems in 3Q97
- **Year:** 1997
- **Confidence at time:** medium

**Actual Outcome 1:** PA-8200 delivery actual outcome
- **Result:** PA-8200 (240MHz) shipped 1997 as projected; PA-8500 delayed to mid-1999
- **Confidence:** verified
- **Notes:** PA-8200 timeline largely met. Source: OpenPA.net HP PA-RISC history (https://www.openpa.net/systems/hp-9000_pa-risc_story.html).

---

**Prediction 2:** HP-Intel Merced processor delivery in servers
- **Claimed:** Anticipated mid-1998 delivery in servers
- **Year:** 1998
- **Confidence at time:** low

**Actual Outcome 2:** Merced/Itanium actual delivery
- **Result:** Itanium (Merced) shipped in servers in 2001; 3 years later than predicted
- **Confidence:** verified
- **Notes:** Prediction significantly wrong; HP 9000 discontinued 2003. Source: Wikipedia HP 9000 (https://en.wikipedia.org/wiki/HP_9000).

---

**Prediction 3:** PA-8500 performance and delivery timeline
- **Claimed:** 100% improvement over PA-8000 at end of first-half 1998
- **Year:** 1998
- **Confidence at time:** medium

**Actual Outcome 3:** HP 9000 server line fate
- **Result:** HP 9000 server line discontinued 2003; replaced by Itanium-based Integrity Servers
- **Confidence:** verified
- **Notes:** PA-8500 delivered mid-1999 (one year late); platform ultimately discontinued. Source: Wikipedia HP 9000 (https://en.wikipedia.org/wiki/HP_9000).

### Entities Referenced (9)

| Entity | Type | Status | Successor |
|--------|------|--------|-----------|
| Hewlett-Packard Company | company | split | HP Inc. / Hewlett Packard Enterprise |
| Aberdeen Group | firm | acquired | Aberdeen Strategy & Research |
| IBM Corporation | company | active | — |
| Sun Microsystems, Inc. | company | acquired | Oracle Corporation (2010) |
| Digital Equipment Corporation | company | acquired | Compaq (1998) -> HP (2002) |
| Intel Corporation | company | active | — |
| Data General Corporation | company | acquired | EMC Corporation (1999) |
| Silicon Graphics, Inc. (SGI) | company | acquired | Rackable Systems (2009) |
| Transaction Processing Performance Council | institution | active | — |

### Technologies Referenced (10)

| Technology | Category | Vendor | Lifecycle (at study) | Lifecycle (current) |
|------------|----------|--------|---------------------|---------------------|
| HP 9000 (HP-UX) | platform | Hewlett-Packard | mature | obsolete |
| PA-8000 Processor (64-bit, 180MHz) | platform | Hewlett-Packard | emerging | obsolete |
| PA-7200 Processor (120MHz) | platform | Hewlett-Packard | mature | obsolete |
| PA-8200 Processor | platform | Hewlett-Packard | emerging | obsolete |
| PA-8500 Processor | platform | Hewlett-Packard | emerging | obsolete |
| HP-Intel P7/Merced (Itanium) | platform | HP/Intel | emerging | obsolete |
| HP-UX 10.2 / 11.0 | platform | Hewlett-Packard | mature | legacy-supported |
| TPC-C Benchmark | framework | TPC | mature | active |
| IBM RS/6000 SP | platform | IBM | mature | obsolete |
| Sun Ultra Enterprise 5000 | platform | Sun Microsystems | mature | obsolete |

### Observation Summary

- Total observations: 27
- By type: benchmark-result (9), technology-assessment (3), framework-factor (3), viability-prediction (3), actual-outcome (3), strategy-classification (2), market-data (2), expert-opinion (1)
