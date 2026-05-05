# Kastner Technology Breadth Memoir: Forty-Seven Years Across the Computing Stack

> Archived from: kastner_breadth_memoir.md
> Original publication date: 2026-05-05
> Author: Peter S. Kastner

---

## Original Document Text

# A Wide Field: A Memoir on the Breadth of My Technology Coverage

*A first-person reflection by Peter S. Kastner, drawn from a quantitative pass across 592 studies in the Aberdeen-Group Archive (kastner-author + studies in which I am cited or quoted).*

---

## The numbers, before the stories

Most analysts pick a patch and stay in it. Storage. Networking. Databases. They build careers ten centimeters wide and a thousand meters deep. I never did that, and the archive — now at 915 unique studies and 17,819 observations — holds the receipts.

When I pulled the corpus that is either authored by me or in which I am quoted by another author, the count came back at **592 studies**. Inside those, the technologies table has **4,628 mentions of 2,537 distinct technologies**. Two thousand five hundred and thirty-seven. That number surprised even me. The earliest study in the corpus is dated 1979 (an ADL client engagement on two-way power-line communications), the latest references material projected through 2026 — a working span of forty-seven years.

By **publication-decade distribution** of those technology mentions, the curve tells you where I was actively writing:

| Decade  | Tech mentions |
| ------- | ------------- |
| 1950s   | 24            |
| 1960s   | 112           |
| 1970s   | 259           |
| 1980s   | 756           |
| 1990s   | 1,503         |
| 2000s   | 1,808         |
| 2010s   | 37            |
| 2020s   | 1             |
| unknown | 123           |

The Aberdeen years (1990s–2000s) are the bulk. But the back-catalog — Prime, Stratus, ADL, Wang, PHI — accounts for 1,151 mentions on its own, which is more technology surface area than most working analysts cover in their entire careers.

The other quantitative anchor is **subject domains**. In the 592-study corpus there are **479 distinct subject_domain values**. That's not 479 categories of technology; it's 479 distinct *problems* I wrote against. Retail PC pricing, fault-tolerant computing marketing, enterprise storage, semiconductor process nodes, IT supply-chain pandemic risk, ERP migration economics, AS/400 longevity, decision support, Y2K remediation, broadband ISP economics, AI readiness — the list does not repeat.

And the **vendor surface**: across the corpus, the leading vendor distribution looks like this — Microsoft (377 mentions), Intel (358), IBM (249), AMD (109), DEC (54), Oracle (50), Sun Microsystems (47), Dell (36), HP (36), Stratus (36), Computer Associates (35). Below that long head sits a broad torso — Cisco, EMC, Sequent, Tandem, Wang, Prime, Data General, NetApp, Sybase, Informix, Teradata, Veritas, BEA, TIBCO, webMethods, Tivoli, BMC, NVIDIA, ATI — and then a tail of hundreds of smaller vendors. I did not avoid any layer of the stack. I covered all of it.

---

## How the breadth distributes — a quantitative table

To write a memoir by category, I needed two views. The first uses the **raw `category` field** that the archive's per-study extractions emit. The second is a **curated thematic rollup** I built across those raw labels, because the raw set has 200+ values (analysts and AI helpers tag things variously: `platform`, `application`, `framework`, `protocol`, `processor`, `chip`, `RDBMS`, `OLAP`, `tp-monitor`, `middleware`, `architecture-framework`, etc.).

**Raw `category` field — top buckets in the Kastner corpus:**

| Category         | Mentions | Unique tech_ids |
| ---------------- | -------- | --------------- |
| platform         | 1,218    | 778             |
| application      | 679      | 452             |
| framework        | 441      | 325             |
| protocol         | 357      | 210             |
| hardware         | 210      | 158             |
| operating-system | 205      | 90              |
| processor        | 154      | 30              |
| storage          | 132      | 62              |
| language         | 64       | 36              |
| chip             | 63       | 34              |
| benchmark        | 36       | 23              |
| middleware       | 25       | 23              |
| analytics        | 16       | 12              |

**Curated thematic rollup — the same corpus regrouped by technology theme:**

| Theme                          | Mentions | Unique tech_ids |
| ------------------------------ | -------- | --------------- |
| Other / long-tail proprietary  | 2,033    | 1,450           |
| Personal Computers & OS        | 753      | 243             |
| Databases                      | 349      | 159             |
| Storage & Hardware             | 296      | 110             |
| Networking & Internet          | 284      | 164             |
| Mainframes & Midrange          | 208      | 107             |
| SOA, BPM & Integration         | 175      | 98              |
| Unix & Open Systems            | 111      | 34              |
| Semiconductors & Chips         | 77       | 49              |
| Security & Reliability         | 63       | 52              |
| ERP & Enterprise Apps          | 54       | 22              |
| Outsourcing & Services         | 52       | 35              |
| Displays & Peripherals         | 46       | 14              |
| AI, Analytics & Emerging       | 44       | 22              |
| Programming & Dev Tools        | 40       | 17              |

The shape of that table is itself an argument. Fourteen named themes carry meaningful mass, and the 2,033-mention "other / long-tail" bucket is filled with named products and codenames so specific that no rollup catches them — Intel Westmere, Dell|EMC AX100, Sequent Symmetry SE70, Sapiens 4GL, Bluestone, IBM Tivoli, NetWeaver, Itanium 2, ATI TV Wonder, MicroVAX, ardes-2k, Trustworthy Computing, ILM, FDDI, DDR2 SDRAM, Centrino, 3GIO/PCIe, 3D Tri-Gate, RFID-edge-computing. That tail *is* the breadth. A specialist's archive would not have it.

Now the memoir.

---

## I — Mainframes and Midrange (208 mentions / 107 distinct technologies)

I started where the data was: glass houses with raised floors, IBM card readers, line printers that shook the building. The first technologies to appear in my career are also the first themes I want to claim. The corpus shows me writing across IBM mainframes (S/360, S/370, S/390, 3090, zSeries, z/Architecture), DEC's VAX line including MicroVAX and OpenVMS, the Prime 50-series running PRIMOS, HP 3000 with MPE, Data General Eclipse and Eclipse S/230, Stratus' fault-tolerant Continuum and forms-management system, and the IBM AS/400 — System/36 and System/38 lineage right through to iSeries. Sequent Symmetry SE70 with SMP. RS/6000 SMP. ACMS as a transaction-processing monitor. Mainframe clustering. Mainframe-distributed strategies. Cluster-coordination and cluster-interconnect.

I covered midrange because I lived inside it. I worked at PHI Computer Services, then Wang. I marketed Prime's Industry Product Plan in 1981 — the corpus's earliest Kastner-authored study. I marketed Stratus' fault-tolerant computers and ghost-wrote one of the early IEEE Computer pieces on Stratus/32. By the time the AS/400 came of age I had an opinion on its longevity (yes, it would last; I wrote that down) and I deposed about it in *Intelligent Electronics v. Andersen Consulting* in 1999. The 107 distinct mainframe-and-midrange technologies in the corpus are not a list of things I read about. They are platforms I knew by feel.

## II — Unix and Open Systems (111 / 34)

Unix shows up later in my chronology and I came to it as someone whose proprietary-OS instincts had to be beaten back. The corpus has me on AIX, HP-UX, Solaris, SunOS, POSIX-1003, X-Windows, BSD lineage and — the whole second half of the 1990s — Linux: Linux desktop, Linux server, Linux 64-bit, Linux embedded, Linux kernel, Linuxcare University, the early Linux knowledgebase movement. The 34 distinct technologies in the Unix bucket understate the influence: Linux's appearance as a competitive force against Windows Server and against legacy Unix is woven into another fifty studies in adjacent themes. My take, then as now: open systems would not kill the proprietary stacks; they would domesticate them.

## III — Personal Computers and OS (753 / 243)

This is the loudest theme by mention count, and for a reason. From 2002 forward I ran a weekly Aberdeen tracking franchise on what we called the **Digital Consumer Technology** market — the post-bubble PC retail price war. Best Buy, CompUSA, Circuit City, Dell direct, HP Shopping, Gateway Online, Sony Style. Every Dell Dimension and Inspiron SKU, every Compaq Presario, eMachines, Alienware, VPR Matrix, every Pentium 4, Celeron, Athlon XP, Athlon 64, Opteron, Xeon, Itanium and Itanium 2. Centrino. Intel Core i3, Core 2 Duo. The DCT subdomain alone holds 76 of my studies.

But PCs in this archive are not just retail SKUs. They are also Windows 95, 98, Me, 2000, XP Home/Pro, OS/2, Mac OS, Aero Glass UI, Trustworthy Computing, all-in-one PCs, 15-inch and 17-inch LCDs, the entire Pentium-to-Core transition. I wrote a 2003 survey of 250 companies on PC replacement buying plans that ended up cited in a 2007 *AMD v. Intel* outreach. I field-tested an Intel Classmate PC in Haiti in 2008 and wrote a six-page bug log that any product manager would recognize as honest — *"speaker volume initial setting is maximum loud — a distraction"*; *"battery life only a couple of days even after full charge"*; *"Internet Explorer default web site is microsoft.com — there ought to be a better landing place."* That, too, is in the corpus.

## IV — Storage and Hardware (296 / 110)

A specialty I never owned but always had to cover. RAID, SCSI, SATA, iSCSI. SAN, NAS, DAS internal and external. Fibre Channel — which I'd put under Networking by today's logic, but in the era it was its own world. Tape. Optical. CD-RW. DVD. Maxtor RAMP — I wrote the Maxtor Reliability And Migration Protection program. Seagate. EMC including Dell|EMC AX100. NetApp. PowerVault NAS. Information Lifecycle Management (ILM), remote mirroring, automated backup-restore, network backup, datakeeper. DDR-266 and DDR-400 SDRAM, DDR2 SDRAM, DDR-SDRAM 64-bit. Hard disks all the way through to 3D XPoint Optane. **One hundred and ten** distinct storage and adjacent-hardware technologies. A dedicated storage analyst would call this their entire career; for me it was Tuesdays.

## V — Databases (349 / 159)

Databases were where I learned that benchmarks are a craft and a weapon. The corpus has me on DB2 in every flavor (DB2/6000, DB2 AIX, DB2 z/OS), Oracle 7 through later releases, SQL Server, Sybase, Informix, MySQL, PostgreSQL, Teradata, Ingres, Allbase/SQL, ANSI SQL, Codasyl DBMS, hierarchical-database thinking, OODBMS and ORDBMS extensions (Informix DataBlade, Universal Server), ROLAP, OLAP, decision support, the early data warehouse and data-warehouse-appliance concept, MPP databases, OLTP on every platform that mattered, and the TPC benchmark family — TPC-A, TPC-B, TPC-C (TPM-C as a metric I quoted often), TPC-D — including a strong opinion on which TPC results were honest and which were configured for the press release. **One hundred and fifty-nine distinct database technologies** is the kind of number a database-only firm would aspire to.

## VI — ERP and Enterprise Applications (54 / 22)

Smaller in raw count but heavy in influence. SAP R/2 and R/3, SAP NetWeaver, the SAP/Oracle pairing on AS/400, PeopleSoft including PeopleSoft HR, Siebel CRM, Baan, JD Edwards, generic CRM and ERP and SCM frameworks. SAP-SD as a benchmark workload. Sapiens 4GL. The 22 distinct technologies in this theme drove ten times their weight in observations because every ERP project I covered hit infrastructure: which platform runs it, which database under it, which TP monitor, which OS. An ERP study was always a stack study.

## VII — SOA, BPM and Integration (175 / 98)

By the mid-2000s I had a sub-specialty — Service-Oriented Architecture, Business Process Management, Enterprise Information Integration, ESB. The SOA ingestion completed earlier this very session added 27 studies (15 of mine) covering SOA, BPM, EII, ESB, web services, SOAP, WSDL, UDDI, BPEL, composite applications, MQSeries, WebSphere, IBM Webify, BEA's WebLogic-era integration moves, Bluestone, IT outsourcing, ADM outsourcing, and SOA governance. The number 98 distinct integration technologies — middleware, transaction monitors, integration platforms, application-lifecycle-management for SOA — is a domain category most analysts only entered from one direction. I came at it from the database side, the application side, and the architectural-framework side, and the corpus shows that triangulation in the variety of vendors I named.

## VIII — Networking and the Internet (284 / 164)

This theme is the biggest in *uniqueness ratio* (164 distinct techs / 284 mentions = high diversity-per-mention). Why? Because networking churns vocabulary fast, and I covered every churn. TCP/IP. HTTP, HTML, URL, DNS. Token-Ring, Ethernet, 10/100 Ethernet, 10GbE. ISDN, DSL, broadband, 56K modem, ultra-wideband. 802.11a/b/g/n. 3G cellular and wireless networks. 3GIO before it was renamed PCIe; PCIe itself. FDDI. Infiniband. Fibre Channel as fabric. WebEx, internet telephony / VoIP. Mobility infrastructure, Centrino as the integrated mobility platform, mobile platforms, edge devices. E-commerce, B2B, B2C frameworks. Internet Email Solutions and ISP services. The corpus shows me pivoting from token-ring opinions into wireless-LAN opinions into 3G-cellular opinions without ever stopping to specialize. Most analysts would have planted a flag in one of those eras. I refused.

## IX — Semiconductors and Chip Process (77 / 49)

A theme most analysts don't even attempt. I wrote on 8-inch and 300mm and 450mm wafers, the 90nm/45nm/32nm process transitions, 3D Tri-Gate, 3D XPoint / Optane, Hyper-Threading as a CPU feature, math coprocessors, the canterwood chipset, instruction-set architecture as a strategic question, RISC vs. CISC, Itanium IA-64 and Itanium 2 as a decade-long bet, AMD Athlon 64, Westmere (32nm Nehalem), and the Intel "tick-tock" cadence as a competitive strategy. There is also a fault-tolerant-server line under Stratus and Tandem that touched silicon decisions. Forty-nine distinct semiconductor and chip-architecture topics is a specialty most semi-only analysts don't carry. I covered it because the chip drove the platform drove the workload drove the customer.

## X — Security and Reliability (63 / 52)

A theme with high uniqueness because every product is its own subdomain. Firewalls, intrusion detection, PKI, encryption, SSL/TLS, BitLocker, Cisco Security Agent, ardes-2k, enterprise-security framework, malware, hardware-security, platform-security, the Trustworthy Computing initiative, Y2K (Y2K bug as a software-defect class, Y2K tools as a category), clustering and high-availability for both fault-tolerance and disaster recovery, and the explicit fault-tolerant-computing market — Stratus, Tandem, the math of how mainframe-class availability migrates down-stack. I was a fault-tolerance partisan and the corpus has 36 mentions of Stratus alone.

## XI — AI, Analytics and Emerging (44 / 22)

The most recent and the most deliberately strategic. Server virtualization, desktop virtualization, Intel VT, RFID and RFID-edge-computing, sensors, neural-network-agents, expert-systems lineage, SAS analytics, business intelligence, data warehousing for analytics, speech technology, 3D-VR interface, ARM-architecture and ARM-embedded CPUs, AI-archival-analysis as a methodology — the latest of which is what we are doing right now to produce this very memoir. The number 44 understates the centrality of AI in my current work because most AI-as-applied-to-broadband and AI-readiness-assessment studies live in the Adoptex line of work that has only just started landing in the archive. This category is where the next 500 mentions will come from.

## XII — Programming and Development Tools (40 / 17)

Smaller than the others because I rarely wrote code reviews. But the corpus has me writing about COBOL, Fortran, Fortran 77, C, C++, Java, J2EE, JavaScript, Visual Basic VBA, Perl, Ruby, PL/1, RPG, CASE-tools, IDE concepts, the 4GL movement, COBOL OS/360 legacy migration. I cared about programming languages as workforce questions — which language is your team actually shipping in, and what does that imply about your cost structure — more than as technology questions. Seventeen distinct languages and dev-tools is enough to engage on most enterprise IT programs without ever having to ask "what's your stack?"

## XIII — Outsourcing, Cloud and Managed Services (52 / 35)

Late-career and growing. ADM outsourcing, BPO general, IT outsourcing including India and China and full-onshore-offshore hybrid models, the ASP service-delivery model, cloud computing as it emerged, cloud desktop, hosted apps, managed services, enterprise systems management with Tivoli and CA Unicenter TNG and OpenView, SaaS as a business model. I wrote two full studies in 2007 on outsourcing economics and one in 2025 on cloud-and-AI for broadband ISPs that pulls this thread forward.

## XIV — Displays and Peripherals (46 / 14)

A small but real theme. Flat-panel monitors, LCD 15-inch and 17-inch, IBM 2260 terminals, color inkjet printers, plasma display TV, Dell LCD TV, CRT monitors, printer ink as a consumable economics question. The corpus shows my consumer-electronics tracking spilling beyond the PC into the adjacent display and peripheral market — a habit from the DCT franchise.

---

## What the long tail says

The most striking single statistic is not in any of the fourteen named themes. It is the **2,033 mentions across 1,450 unique long-tail technologies** — items so specific they don't rollup. *Sequent Symmetry SE70.* *Dell|EMC AX100.* *DDR2-400 SDRAM.* *Sapiens 4GL.* *Bluestone.* *NetWeaver.* *Canterwood chipset.* *3D-VR interface.* *ARDES-2K.* *MicroVAX.* *Workgroup OLTP.* *ATI TV Wonder.*

That is the part of the picture I am proudest of. Specialists win in deep verticals. Generalists win in the long tail — by being the one analyst a vendor or a litigator or a strategy team can call when their specific named product doesn't fit any specialist's beat. The 1,450 distinct long-tail technologies in the corpus are 1,450 phone calls I could take that other analysts could not. And the **479 distinct subject domains** on top of those technologies are 479 problem types I had a credible point of view on.

Specialization compounds; generalism cross-pollinates. Both work. But cross-pollination is where the unconventional bets came from — the Stratus/32 IEEE article in 1983, the Prime Industry Product Plan in 1981, the fifteen high-prescience calls dated 1981 through 2003 that the `llms-full.txt` now highlights, the SARS supply-chain insight written with Craig in 2003, the AS/400 longevity call that survived twenty-five years of "the AS/400 is dead next year" predictions, and the entire Aberdeen DCT franchise that I built and ran solo because no one else wanted to count Best Buy SKUs every Friday for two years.

The archive is now a count of those bets. **2,537 distinct technologies. 479 distinct subject domains. 4,628 technology mentions. 592 studies authored or cited. 1979 to ~2026.** Forty-seven years.

Most analysts stay in a small technology patch. I covered a wide field — and the data, for the first time, can prove it.

---

## How and why did I do this?

The quantitative case is on the page. What is left is the human one — how a single career covered this much ground, and why it did.

### The how was a fortuitous curriculum

I did not set out to cover everything. I arrived at it through a sequence of jobs, each of which forced me to look at computing from a different angle, and none of which I would have predicted from the one before.

It started with a teenage job organizing and counting paper slips. The work was numbingly manual, and I remember thinking, very specifically, that this was the kind of thing a machine ought to do — except the machines that could do it did not yet exist at any price a small employer could afford. That gap between *what should be automated* and *what currently is* turned out to be the single question I have been chasing ever since. It is the same question, restated, at every layer of the stack the archive now documents.

From paper slips I went into **computer operations**, where the lesson is that running a data center is reliable manufacturing — every job a unit, every shift a production schedule, every failure a defect to be classified and prevented. Operations teaches you that computing is not a pile of clever ideas; it is an industrial process with uptime requirements.

From operations into **programming, systems analysis, project management, and OEM systems building** — the core of the software business when computers were very expensive and time on them was rationed. You learned to think before you typed because compile cycles cost money. You learned to specify before you coded because rework cost more money. You learned to manage projects because budgets were measured in CPU-hours, not headcount-months. That discipline never left.

From there into **computer marketing** — product planning, market planning, pre-sales, trade shows, competitive analysis. This is where I learned that a feature does not exist until a customer can use it, and a product does not exist until a buyer can describe it. Marketing also taught me that the technical truth and the commercial story are usually different, and the analyst's job is to know both.

And finally **market research**, where you had to be productive, right on the facts and the strategy, articulate, and trustworthy — all four, every time, on every study, or you would not be invited back. Market research is the discipline that ties the previous four together, because every research call draws on operations sense, software sense, and marketing sense to be worth anything.

Five rungs, each of which widened the field of view rather than narrowing it. By the time I was at Aberdeen, I had already learned to look at any technology question from five sides. The breadth in the archive is the residue of that path.

### The why has four reasons that all point the same direction

First, **I am an architect by temperament** — Myers-Briggs calls it INTJ, and I take the designation seriously. Architects do not specialize in a material. They specialize in fitting materials together, which means they need to understand all of them at least well enough to know what they will and will not bear. That instinct, applied to enterprise IT, produces an analyst who refuses to stay in one technology patch.

Second, **I may have a touch of restless attention** — not diagnosed, but real enough that I notice it. Change, for me, is oxygen. A new platform, a new vendor, a new market dynamic, a new policy regime — these do not feel like distractions to me; they feel like the natural state of the field. Most analysts treat change as the thing that interrupts their specialty. I treated change as the specialty.

Third, **the press was my partner**. Two journalists in particular — **Bill Bulkeley** at the *Wall Street Journal* and **Hiawatha Bray** at the *Boston Globe* — taught me what it meant to be a useful source. They needed people who could explain a complicated technology question in a paragraph that a Wednesday-morning business reader could understand, with the nuance still intact, on deadline. I tried to be that person for them, and for the dozens of other reporters I worked with over the Aberdeen years. The trade press paid me back with the kind of free distribution no marketing budget could buy. I have over 500 documented personal press quotes. The relationship was symbiotic, and I respected it.

Fourth, and this is the one that matters most, **I genuinely cared about the IT decision-makers**. They had half the facts, too much marketing hype from the vendors, and the obligation to be right on the decision — or, failing that, to be wrong for a good reason that they could defend in a budget meeting. They needed someone whose loyalty was to the decision quality, not to a vendor relationship and not to a research firm's house thesis. Aberdeen shipped some single research studies in print runs of up to 100,000 copies. Multiply that across hundreds of studies and the audience is in the millions. My research helped a meaningful share of the people in those millions make nuanced IT decisions, and I am very proud of that.

### One throughline

The four reasons look independent on the page, but they are not. Architect temperament, restless attention, a working press relationship, and a duty to the buyer all selected for the same trait: **the willingness to follow a problem out of its native category**. A specialist will not do that, because their authority lives inside the category. A generalist with my particular wiring has no choice — the problem is wherever the problem is, and you go after it with whatever tools the problem requires, picked from whatever shelf they sit on.

That is, in the end, what the 2,537 distinct technologies and 479 distinct subject domains in this archive really are. They are not a brag. They are the documented residue of forty-seven years of going wherever the problem went, because **I am, and always have been, all about solving business problems with technology** — and business problems do not respect category boundaries.

---

*Counts in this memoir are derived from `_master_studies.csv`, `_master_technologies.csv`, and `_master_observations.csv` in the `aberdeen-group-archive` repository as of May 5, 2026. The Kastner corpus is defined as: studies whose `collection` begins with `kastner-author`, OR whose `author` field contains "Kastner", OR whose observations or metadata contain a Kastner mention while authored by another. Theme rollups are heuristic over `tech_id` and `tech_name` patterns; raw `category` field counts are reported alongside for transparency. The full classifier is preserved at `/home/user/workspace/breadth_analysis.py`.*


---

## Frictionless Data Package Metadata

> Auto-generated by Archival Ingest Skill v16

### Study Record

| Field | Value |
|-------|-------|
| study_id | kastner-technology-breadth-memoir-2026 |
| title | Kastner Technology Breadth Memoir: Forty-Seven Years Across the Computing Stack |
| author | Peter S. Kastner |
| date | 2026-05-05 |
| type | memoir |
| subject_domain | memoir/career-arc |
| methodology | oral-history, archive-quantification |
| source_file | kastner_breadth_memoir.md |
| license | CC-BY-4.0 |

### Abstract

First-person memoir by Peter S. Kastner quantifying the technology breadth of his 47-year career as analyst, marketer, and expert witness. Drawing on the Kastner-authored + Kastner-quoted corpus (592 of the archive's 915 studies), the memoir documents 2,537 distinct technologies across 4,628 mentions and 479 subject domains, organized into 14 thematic rollups from Personal Computers & OS through AI/Analytics & Emerging. A concluding section ('How and Why Did I Do This?') traces the five-rung curriculum (paper slips, operations, programming, marketing, market research) that produced the breadth, and credits a working trade-press partnership with Bill Bulkeley (Wall Street Journal) and Hiawatha Bray (Boston Globe), Aberdeen print runs of up to 100,000 copies, and 500+ documented personal press quotes for amplifying the work to millions of readers.

### Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | high | Quantified meta-analysis of the entire archive's coverage breadth; canonical reference for any career-arc query and the only study that aggregates the full Kastner corpus. |
| **Relevance** | high | Maps directly to the live archive's master indices and provides the rollup tables (themes, decades, vendors) used to navigate 915 studies and 2,537 technologies. |
| **Prescience** | not-applicable | Reflective memoir — makes no forward predictions; instead summarizes which prior calls were validated. |

### Prescience Detail

This study did not make forward-looking claims.

### Entities Referenced (17)

| Entity | Type | Status | Successor |
|--------|------|--------|-----------|
| Peter S. Kastner | person | active |  |
| Aberdeen Group | company | acquired | Spiceworks Ziff Davis |
| Wang Laboratories | company | dissolved | filed bankruptcy 1992 |
| Arthur D. Little | firm | active |  |
| Prime Computer | company | dissolved | Computervision then PTC |
| Stratus Computer | company | acquired | Stratus Technologies (private) |
| Digital Equipment Corporation (DEC) | company | acquired | Compaq, then HP |
| Yankee Group | firm | acquired | 451 Research, then S&P Global |
| Obian Group | firm | active |  |
| Adoptex LLC | company | active |  |
| William M. Bulkeley | person | retired |  |
| Hiawatha Bray | person | active |  |
| The Wall Street Journal | institution | active |  |
| The Boston Globe | institution | active |  |
| Microsoft Corporation | company | active |  |
| Intel Corporation | company | active |  |
| International Business Machines Corporation | company | active |  |

### Technologies Referenced (15)

| Technology | Category | Vendor | Lifecycle (at study) | Lifecycle (current) |
|------------|----------|--------|---------------------|---------------------|
| Personal Computers & Operating Systems (theme rollup) | platform | various | mature | mature |
| Databases & RDBMS (theme rollup) | platform | various | mature | mature |
| Storage & Hardware (theme rollup) | platform | various | mature | mature |
| Networking & Internet (theme rollup) | protocol | various | mature | mature |
| Mainframes & Midrange (theme rollup) | platform | IBM/HP/Stratus/DEC | mature | legacy-supported |
| SOA / BPM / Integration (theme rollup) | framework | various | mature | legacy-supported |
| Unix & Open Systems (theme rollup) | platform | various | mature | mature |
| Semiconductors & Chips (theme rollup) | platform | Intel/AMD/IBM/etc. | mature | mature |
| Security & Reliability (theme rollup) | framework | various | mature | mature |
| ERP & Enterprise Applications (theme rollup) | application | SAP/Oracle/PeopleSoft/etc. | mature | mature |
| Outsourcing & Services (theme rollup) | framework | various | mature | mature |
| Displays & Peripherals (theme rollup) | platform | various | mature | mature |
| AI / Analytics & Emerging (theme rollup) | application | various | emerging | active |
| Programming & Dev Tools (theme rollup) | language | various | mature | mature |
| Other / Misc (long tail) | platform | various | varies | varies |

### Observation Summary

- Total observations: 74
- By type: market-data: 49, topic-insight: 16, personal-recollection: 9
