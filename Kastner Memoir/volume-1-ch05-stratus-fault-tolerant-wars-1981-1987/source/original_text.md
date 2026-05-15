# Chapter 5: Stratus Computer — Six Years in the Fault-Tolerant Wars (1981-1987)

> Archived from: MASTER-EBOOK-ASSEMBLED-v4.md (Chapter 5: Stratus Computer — Six Years in the Fault-Tolerant Wars (1981-1987))
> Original publication date: 2026-05-14
> Author: Peter S. Kastner

---

## Original Document Text

# Chapter 5: Stratus Computer — Six Years in the Fault-Tolerant Wars
### *(1981–1987)*

---

I joined Stratus Computer on November 1, 1981, six weeks before the company announced its first product.

That timing was not accidental. I was hired as Manager of Marketing Development precisely because the company needed someone who could translate radical engineering into a market-moving story — and who could do it before the product was public. The engineering was extraordinary. The problem, as always, was making it matter in the marketplace. I landed running.

---

## The Problem That Created the Company

The computing world of 1981 had a problem it did not yet know how to name. Mainframes were powerful, but they were not built for uninterrupted operation. When a component in an IBM 4300 failed, the system crashed. You rebooted, recovered from logs, and restarted. In a batch-processing world, a thirty-minute recovery window was annoying but survivable. In the emerging world of ATM networks, airline reservation systems, and stock trading floors, thirty minutes was a catastrophe. Thirty seconds was unacceptable.

The industry had produced two competing answers.

**Tandem Computers**, founded in 1974 in Cupertino (CA), addressed the problem through software. Its NonStop architecture used pairs of processors, each with a complete copy of the application. Programmers had to explicitly write "checkpointing" code — periodic state saves — so the backup processor could pick up where the primary left off after a failure. Tandem was technically sound. It was also expensive in the currency that mattered most: programmer time.

**Stratus** took the opposite approach. The engineers in Natick (MA) decided that software should never know a failure had occurred. They built hardware-based fault tolerance using a **lockstep architecture**: four physical microprocessors doing the work of one, arranged in two pairs. A hardware comparator checked the results of each pair continuously. If one CPU failed, the comparator instantly took that pair offline and continued executing on the surviving pair — without losing a single clock cycle, without any software awareness of the event, without interruption of the running program.

> **Sidebar: What Is Fault-Tolerant Computing?**
>
> Most computers are designed on the assumption that hardware will be reliable most of the time, and that occasional failures are acceptable events that trigger recovery procedures — rebooting, restoring from backup, rerunning failed jobs. This assumption is workable for batch processing, where work can be interrupted and restarted.
>
> Fault-tolerant computing starts from the opposite assumption: for certain applications, *any* interruption is unacceptable. An ATM network that goes down for thirty minutes doesn't merely inconvenience customers; it processes zero transactions for thirty minutes — real revenue, real costs, real reputational damage. A stock exchange that drops off for ten seconds during peak trading creates legal and financial exposure.
>
> Fault tolerance is achieved in two broad ways. *Software fault tolerance*, as Tandem implemented it, requires the application developer to explicitly handle failure scenarios — detecting failures, saving state, switching to backup processes. This works but imposes significant development and testing burden.
>
> *Hardware fault tolerance*, as Stratus implemented it, hides failures from the software entirely. The application runs on hardware that has been designed to keep running through component failures. The software does not need to know a failure occurred because, from its perspective, nothing unusual happened. This approach costs more hardware but eliminates the programming complexity.
>
> The business case for both approaches was identical: calculate your cost of downtime per hour, compare it to the price premium for fault-tolerant hardware, and determine when the math works. Stratus's marketing job was to make that math vivid, personal, and unavoidable.

---

## The Pull-the-Plug Demonstration

We could not outspend IBM or Tandem on field sales. We had to be louder, faster, and more viscerally convincing. Trade shows became our proving ground.

The centerpiece of the Stratus demonstration was breathtakingly simple: we invited prospects to pull a CPU board out of a running system while it was processing transactions. The system did not crash. A red LED lit up on the failed component. The demonstration continued without interruption.

Ten seconds of theater replaced fifty pages of white papers.

The theater was not without its backstage drama. The evening before our public launch, VP of Hardware Gardner Hendrie could not reliably pull a board without crashing the system. Marketing had a sleepless night — as did Engineering. The culprit turned out to be the shiny Lexan plastic covers on the circuit boards, which generated static electricity when pulled from the slot. Dousing the demo-room carpet with water solved the launch-day problem, and Engineering Change Order #1 replaced the elegant plastic with cardboard.

The product launch was a success. The future of fault tolerance was briefly cardboard-covered.

---

## The Economics of Downtime

Marketing fault tolerance required building a new vocabulary for customers who had never been asked to quantify the cost of outages. Most IT managers in 1981 thought about systems in terms of performance and capacity. Availability was assumed; downtime was an operational embarrassment, not a financial metric.

We changed that by asking a single question: *What does one hour of downtime cost you?*

For an ATM network processing 10,000 transactions an hour at $40 average value, the arithmetic was straightforward. For a brokerage trading desk, the number was larger and more frightening. For a point-of-sale network at a large retailer, it translated directly into lost sales. We created direct-mail pieces with cost-of-downtime calculators customized by industry. We ran competitive displacement programs targeting Tandem users frustrated by the programming complexity of NonStop. The message was clean: *Keep your programmers. Change your hardware.*

The most powerful marketing development of my Stratus years was not a campaign or a brochure. It was a deal.

IBM came to us. After we nudged them.

IBM's sales force was watching their enterprise customers evaluate fault-tolerant systems, and IBM had nothing to offer them. After negotiations I contributed to but was not party to at the executive level, IBM agreed to rebrand the Stratus FT200 as the **IBM System/88**. Our marketing shifted overnight to a new anchor: *"The Technology IBM Chose."*

That single phrase neutralized every startup-risk objection. If your customer's primary concern was that Stratus was an unknown company with an uncertain future, you now had IBM's name on the machine. "No one ever got fired for buying IBM."

> **Sidebar: What the IBM OEM Deal Meant Strategically**
>
> Original equipment manufacturer (OEM) agreements — where one company's product is sold under another company's brand — were common in the minicomputer era. What made the IBM/Stratus deal remarkable was the direction: IBM, the most dominant technology brand in the world, was putting its name on a startup's product because it had no competitive alternative.
>
> For Stratus, it was validation that money couldn't buy. For IBM, it was a pragmatic solution to a gap in their portfolio. For prospects considering fault-tolerant systems, it answered the vendor-risk question entirely.
>
> The deal also created an interesting internal challenge: IBM's own salesforce now carried a product that competed with conventional IBM mainframes in certain use cases. We had to develop "battlecard" materials explaining the swim lanes — when to sell the System/88, when to sell a 3090, and how to keep the sale inside the IBM family rather than losing it to Tandem. The battlecards were essentially a conflict-resolution document for a company that was simultaneously our distributor and our competitor.

---

## The Debit-Credit Wars

By the mid-1980s the principal battlefield was banking and financial services, where ATM networks and point-of-sale authorization systems were expanding rapidly. Tandem and Stratus competed for every significant deal.

The competitive argument was sharp. Tandem claimed that our hardware approach was brute-force redundancy and that their software approach was architecturally elegant. We countered that their architectural elegance was being paid for by every application developer who had to write, test, and maintain recovery code. Our advantage was visceral: when a board failed, a red light came on. You pulled the board while the system kept running. You mailed it back to Stratus. No expensive on-site service engineer. No emergency maintenance contract clause.

We had turned hardware redundancy into a maintenance model. We called it "the board that mails itself."

The battlecard we developed for the IBM System/88 versus conventional IBM mainframes was particularly crisp. The argument centered on a concept we called the **"zero-code advantage"**: on a Stratus or System/88 system, you wrote standard COBOL or FORTRAN. Fault tolerance was invisible infrastructure. On Tandem, you paid a team of specialized programmers to write and maintain NonStop software. Total cost of ownership over five years — including programmer time, training, and ongoing maintenance — often reversed the hardware price advantage. We made that arithmetic easy to do and hard to argue with.

---

## A Men's Room Pivot

Sometimes the most important market planning does not happen in conference rooms.

I made one of the pivotal recommendations of my Stratus career in a men's room. The observation was simple: Rolm Corporation's digital PBX telephone systems needed exactly the reliability we provided. A PBX switching millions of calls was an always-on application if ever there was one. Telecommunications had the highest cost of downtime of any industry.

That insight, formalized and presented properly, led to a breakthrough in the telecom market. Stratus became embedded infrastructure for SS7 signaling and emerging digital switching systems, where five-nines uptime (99.999% — less than six minutes of downtime per year) was not a sales argument but an entry requirement for the contract.

The telecom DNA built in those years would eventually define Stratus's long-term trajectory, leading to its acquisition by Ascend and eventual integration into Nortel. The PBX observation in the men's room was the genesis of that arc.

---

## Cheyenne Mountain: The $50 Million Proof Point

In 1982, I received a cold call to present at Mitre Corporation, a federally funded research organization that works primarily with the Defense Department. Fifty silent engineers sat in the auditorium. They declined to state their requirements. I had one hour.

I made a calculated decision not to pitch fault tolerance alone. Instead I covered the full architecture: our programmable communications controllers, the modularity, the unusual data protocols we could handle, our spares strategy and field logistics. My assumption was that anyone who had arranged this meeting without stating requirements was dealing with a complex defense systems integration problem, not a simple uptime calculation.

The assumption was correct.

The meeting set off a slow chain reaction: Mitre brought in GTE Sylvania and Systems Development Corporation. The result, after an extended procurement process, was a landmark contract for NORAD — the North American Aerospace Defense Command.

By the late 1980s, Stratus had delivered $10 million in systems hardware and $40 million in spares to Cheyenne Mountain, Colorado, the granite-shielded nerve center monitoring the skies for nuclear threats.

The reference value of that contract was incalculable. When a prospect raised vendor risk — could they trust a startup for mission-critical infrastructure? — the answer wrote itself: if the United States Air Force trusted this machine inside a mountain during a nuclear threat, it could handle your department store's credit card authorizations.

---

## The Boss's Daughter

John Morgridge was my Vice President of Sales and Marketing at Stratus — ex-Honeywell, direct, likable, and very funny. He would later become Cisco's first non-founder CEO and build that company into a generation-defining enterprise.

After I had spent two and a half years running our trade show program, which kept me on the road, John called me in.

"Peter," he said, "I've got a management problem for you."

"How can I help?" I replied, with the wariness that phrase always deserves.

"Well, my daughter Kate's getting married next year, and I thought in the meantime she could do the trade shows for you. Free you up."

I considered this. "John, I take it the management problem is that if she's unhappy, you're unhappy?"

"You got that straight."

Kate Morgridge turned out to be excellent — organized, energetic, genuinely good at the work. Except for the first show, where she wore a T-shirt to a union work-site that read: *Stratus Computers Never Go Down On You.* She learned a great deal that day about human nature in the technology industry of the 1980s. We never discussed it further.

---

## The XA 2000 and the Exit

By 1987, I had been at Stratus for six years. The technology had matured from a regional curiosity to a recognized platform in financial services, telecommunications, and mission-critical retail. I led the market and product team for the **XA 2000** announcement — machines built on Motorola 68020 processors that delivered dramatic performance gains while preserving the lockstep fault-tolerant architecture.

Before departing for Digital Equipment Corporation, I left a parting gift to Stratus and the industry. John Logan, a former colleague from Prime who had settled at Yankee Group, retained me to ghostwrite a 100-page market research study titled *The Future of Transaction Processing*. Published in January 1987, the report predicted that the price-performance of microprocessor-based OLTP systems was about to explode — that Moore's Law was finally meeting the economics of departmental and/or distributed transaction processing, and that the displacement of the mainframe was inevitable.

Stratus later quoted that study in its 1987 annual report, which created a mildly interesting conflict of interest for my next employer. More on that in Chapter 7.

---

## What the Fault-Tolerant Wars Taught

Six years in a market that did not exist when I arrived produced a set of convictions that shaped everything I did afterward.

**Superior engineering is necessary but not sufficient.** Stratus's architecture was genuinely elegant — arguably more elegant than Tandem's, because it achieved the same outcome with less burden on application developers. But elegant architecture does not walk into a data center and sell itself. The pull-the-plug demonstration, the downtime calculator, the IBM OEM deal, the NORAD reference — these were the instruments that translated engineering advantage into market reality.

**Quantify the problem you solve.** "We prevent downtime" is a marketing claim. "Your ATM network loses $400,000 of transaction revenue per hour of outage, and our hardware costs $180,000 more than the alternative" is an argument. Stratus won deals when we made the second argument. We lost deals when the conversation stayed at the level of the first.

**The right market is not always the obvious one.** We launched into banking because the downtime math was visible and quantifiable. The telecom breakthrough — which ultimately defined Stratus's long-term position — came from a sideways observation in a men's room. Market planning that stays in conference rooms misses the oblique angles.

**Red lights sell more than white papers.** The most sophisticated technical sales tool we ever deployed was a demonstration that a customer could interrupt with their own hands. There is something irreplaceable about physical proof to humans. You could argue against a benchmark. You could not argue against the fact that the machine was still running after you had just pulled a CPU board out of it.

Stratus eventually transitioned from proprietary Motorola chips to Intel architectures, maintaining the lockstep edge as commodity hardware improved. The vision the company articulated in the 1980s — that computing infrastructure should be invisible, reliable, and self-healing — became the baseline expectation for digital commerce. Tandem disappeared into HP. Stratus survived as a specialized platform for environments where hardware failure cannot wait for a technician: remote oil rigs, manufacturing floors, telecom nodes.

The engineering approach evolved. The insight did not. In mission-critical computing, downtime is not merely expensive. It is unacceptable.

That is what Stratus proved, one pulled circuit board at a time.

---

*Next: Chapter 6 — Digital Equipment Corporation: Benchmarks, the TPC, and the Mainframe's Last Stand*



---




---

## Frictionless Data Package Metadata

> Auto-generated by Archival Ingest Skill v16

### Study Record

| Field | Value |
|-------|-------|
| study_id | volume-1-ch05-stratus-fault-tolerant-wars-1981-1987 |
| title | Chapter 5: Stratus Computer — Six Years in the Fault-Tolerant Wars (1981-1987) |
| author | Peter S. Kastner |
| date | 2026-05-14 |
| type | memoir |
| subject_domain | memoir/volume-1 |
| methodology | oral-history |
| source_file | MASTER-EBOOK-ASSEMBLED-v4.md (Chapter 5: Stratus Computer — Six Years in the Fault-Tolerant Wars (1981-1987)) |
| license | CC-BY-4.0 |

### Abstract

Peter S. Kastner recounts his six years (1981–1987) as Manager of Marketing Development at Stratus Computer in Natick, MA, where he helped market a hardware-based fault-tolerant computing architecture competing primarily against Tandem Computers and IBM. The chapter traces key milestones including the IBM OEM deal (branding Stratus FT200 as the IBM System/88), the NORAD Cheyenne Mountain contract, and a telecom market breakthrough sparked by a hallway observation about Rolm PBX systems. Kastner distills enduring marketing lessons about quantifying downtime economics, physical demonstration as proof, and finding non-obvious market angles.

### Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | high | Provides a rare insider account of Stratus Computer's early marketing strategy and the IBM OEM deal, capturing pivotal moments in fault-tolerant computing history from a senior participant. |
| **Relevance** | high | Directly covers the OLTP, fault-tolerant computing market, and ATM/financial-services IT segments with specific product, competitor, customer, and deal details relevant to 1980s technology industry analysis. |
| **Prescience** | high | Kastner's 1987 ghostwritten report predicted microprocessor-based OLTP price-performance explosion and mainframe displacement — a forecast confirmed by subsequent market history; his telecom pivot insight foreshadowed Stratus's long-term trajectory. |

### Prescience Detail


**Prediction 1:** OLTP price-performance explosion prediction
- **Claimed:** Report predicted microprocessor-based OLTP price-performance was about to explode — Moore's Law meeting economics of departmental/distributed transaction processing.
- **Year:** 1987
- **Confidence at time:** high

**Prediction 2:** Mainframe displacement prediction
- **Claimed:** Report predicted displacement of the mainframe was inevitable as microprocessor-based OLTP price-performance improved.
- **Year:** 1987
- **Confidence at time:** high


### Entities Referenced (21)

| Entity | Type | Status | Successor |
|--------|------|--------|-----------|
| Stratus Computer | company | active | Stratus Technologies |
| Peter S. Kastner | person | active |  |
| Tandem Computers | company | acquired | Compaq (then HP) |
| IBM | company | active |  |
| Gardner Hendrie | person | unknown |  |
| John Morgridge | person | active |  |
| John Logan | person | unknown |  |
| Kate Morgridge | person | unknown |  |
| Prime Computer | company | acquired | [DEFERRED] |
| Mitre Corporation | institution | active |  |
| GTE Sylvania | company | acquired | [DEFERRED] |
| Systems Development Corporation | company | acquired | [DEFERRED] |
| NORAD (North American Aerospace Defense Command) | agency | active |  |
| Rolm Corporation | company | acquired | IBM (acquired 1984) |
| Ascend Communications | company | acquired | Lucent Technologies |
| Nortel | company | dissolved | Various acquirers (2009 bankruptcy) |
| Yankee Group | firm | dissolved | [DEFERRED] |
| Digital Equipment Corporation | company | acquired | Compaq |
| Honeywell | company | active |  |
| Cisco Systems | company | active |  |
| Jim Treybig | person | unknown |  |

### Technologies Referenced (17)

| Technology | Category | Vendor | Lifecycle (at study) | Lifecycle (current) |
|------------|----------|--------|---------------------|---------------------|
| Fault-Tolerant Computing | platform | Stratus Computer / Tandem Computers | growing | active |
| Lockstep Fault-Tolerant Architecture | platform | Stratus Computer | emerging | active |
| NonStop Architecture (Tandem) | platform | Tandem Computers | growing | legacy-supported |
| Stratus FT200 | platform | Stratus Computer | growing | legacy-end-of-life |
| IBM System/88 | platform | IBM (OEM of Stratus FT200) | growing | legacy-end-of-life |
| IBM-Stratus OEM Agreement | platform | IBM / Stratus Computer | growing | legacy-end-of-life |
| Stratus XA 2000 | platform | Stratus Computer | emerging | legacy-end-of-life |
| Motorola 68020 | platform | Motorola | growing | legacy-end-of-life |
| COBOL | language | Various | mature | legacy-supported |
| FORTRAN | language | Various | mature | active |
| OLTP (Online Transaction Processing) | application | Various | growing | active |
| SS7 (Signaling System No. 7) | protocol | ITU / telecom carriers | emerging | legacy-supported |
| Hardware Fault Tolerance | platform | Stratus Computer | emerging | active |
| IBM 4300 Series | platform | IBM | mature | legacy-end-of-life |
| Fault-Tolerant Systems Market Forecast | framework | Stratus / Kastner | growing | legacy-end-of-life |
| Future of Transaction Processing (1987 Report) | framework | Yankee Group / Kastner (ghostwriter) | emerging | legacy-end-of-life |
| Moore's Law | framework | Intel (concept) | growing | active |

### Observation Summary

- Total observations: 100
- By type: personal-recollection: 41, expert-opinion: 35, market-data: 12, topic-insight: 10, viability-prediction: 2
