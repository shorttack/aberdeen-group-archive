# v1.8.0 calibration A/B report

Generated: 2026-06-19T17:00:18.502110Z

- Calibration set size (P1-scorable ∩ analyst-truth): **150**
- Both pipelines scored: **144**
- Bucket agreement (Rule A: high/medium/low): **119 / 144 = 82.6%**

Verdict: **Pipeline 2 (quote-alone) is good enough — use as default for full corpus.**

## Bucket distributions

| Bucket | P1 (full article) | P2 (quote only) |
|---|---:|---:|
| high | 82 | 81 |
| medium | 40 | 34 |
| low | 22 | 29 |
| parse_fail | 0 | 0 |

## Bucket transition matrix (P1 → P2)

| P1 \ P2 | high | medium | low | parse_fail |
|---|---:|---:|---:|---:|
| high | 74 | 6 | 2 | 0 |
| medium | 6 | 26 | 8 | 0 |
| low | 1 | 2 | 19 | 0 |
| parse_fail | 0 | 0 | 0 | 0 |

## Largest disagreements (|P1 - P2| ≥ 2)


### row_id=980 (SH-3y, P1=4 high / P2=0 low)

**Headline:** IBM adds EISA server to PS/2 family (Computerworld, 1994-06-20)

**Quote:** IBM really needed to jump-start its server business.

- P1 rationale: By 1994 IBM had clearly lost momentum in Intel-based servers and PC hardware to Compaq and other clone vendors, so characterizing its server business as needing a jump-start accurately reflected its weakened competitive position. Over the next three years IBM undertook a major revamp of its server p

- P2 rationale: The quotation is a normative, present‑tense assessment (“IBM really needed to jump‑start its server business”), not a falsifiable prediction about how IBM’s server business would perform or change over the following three years. While IBM did subsequently emphasize servers across S/390, AS/400, and 

### row_id=908 (SH-3y, P1=0 low / P2=4 high)

**Headline:** DEC energizes Unix OLTP line (Computerworld, 1992-06-01)

**Quote:** It should not be difficult for DEC to do the port to Alpha once that environment is production-ready.

- P1 rationale: Within three years of the 1992 article, DEC had introduced Alpha systems and OSF/1 (later Digital UNIX) as its strategic Unix, and provided various migration tools for moving software from MIPS/Ultrix to Alpha. However, there is little widely documented evidence about whether TPframe or its Ultrix/S

- P2 rationale: DEC introduced the 64-bit Alpha AXP architecture in 1992 and had both OSF/1 AXP (later Digital UNIX/Tru64) and OpenVMS AXP in production within roughly a year, with these operating systems quickly reaching sufficient maturity for general use. Over the next few years, DEC successfully ported major la

### row_id=959 (SH-3y, P1=4 high / P2=0 low)

**Headline:** NetFrame gives servers flexibility (Computerworld, 1993-08-02)

**Quote:** To get Concerto to work, you have to walk a very fine line,

- P1 rationale: Kastner’s point was that making Concerto work was technically delicate because coordinating peripherals and shared memory across multiple concurrent operating systems on one server was very complex. In the mid‑1990s, multi‑OS shared‑memory PC superservers such as NetFrame’s remained niche and were q

- P2 rationale: The statement is a generic caution that making Concerto work required carefully balancing flexibility and performance, without specifying a falsifiable outcome within the three-year horizon. While NetFrame’s superserver approach and similar multi-OS, shared-memory partitioned systems did face comple

### row_id=883 (SH-3y, P1=3 medium / P2=0 low)

**Headline:** Unix draws a crowd (Computerworld, 1990-03-19)

**Quote:** went out of [its] way to be nothing like Stratus.

- P1 rationale: Through the early 1990s Tandem’s Integrity and NonStop product lines continued to use their own process-pair and voting-style fault-tolerant designs, remaining architecturally distinct from Stratus’s lockstep pair-and-spare systems as Kastner characterized.[8][11] The two vendors maintained differen

- P2 rationale: The statement is a characterization of Tandem’s design and product-strategy intent relative to Stratus at a point in time, not a falsifiable prediction about future technology or market evolution. While Tandem and Stratus did maintain distinct architectural approaches in the early 1990s, there is no

### row_id=975 (SH-3y, P1=3 medium / P2=0 low)

**Headline:** NEW! GREAT! LATE! (Computerworld, 1994-01-03)

**Quote:** That's the line you walk [when] talking about the future,

- P1 rationale: The quotation is a general observation that vendors must balance between forward-looking roadmaps that help customers plan and hype that overpromises or locks out competitors, and this dynamic clearly persisted through the mid‑1990s but was already true well before 1994. From 1994–1997, high‑profile

- P2 rationale: The statement is a generic remark about the inherent tension between forward-looking marketing and overhyping future products, not a concrete, time-bounded prediction about specific technologies or market outcomes. While later history offers many examples of both successful and backfiring preannounc

### row_id=944 (SH-3y, P1=3 medium / P2=0 low)

**Headline:** CA gets on Microsoft bandwagon (Computerworld, 1993-04-19)

**Quote:** would at least want to kick the tires of Unicenter on NT,

- P1 rationale: Between 1993 and 1996, Windows NT matured through versions 3.5, 3.51 and 4.0 and saw growing evaluation and pilot deployment in large enterprises, including mainframe-centric sites investigating client/server downsizing. CA promoted Unicenter as a cross-platform manager for Unix and NT and many main

- P2 rationale: Between 1993 and 1996, Windows NT matured rapidly in the enterprise and Computer Associates pushed Unicenter and then Unicenter TNG for distributed environments including NT, amid a broader wave of mainframe downsizing experiments. However, there is no reliable historical data on what fraction of CA

### row_id=941 (SH-3y, P1=3 medium / P2=0 low)

**Headline:** Software AG extends Unix tools strategy (Computerworld, 1993-03-15)

**Quote:** That takes time. Software AG is going about it very methodically.

- P1 rationale: Over the mid-1990s, Software AG did in fact migrate Adabas and Natural from mainframes to multiple Unix platforms in a gradual, incremental fashion, extending existing products rather than rapidly reinventing them for open systems. The company remained slower-moving and more conservative than Unix-n

- P2 rationale: The statement that porting Software AG’s products to Unix and open systems would 'take time' and be done 'methodically' is essentially a generic characterization of any multi-platform porting effort rather than a concrete, risky prediction. Historically, Software AG did continue to roll out Unix and

### row_id=990 (SH-3y, P1=0 low / P2=3 medium)

**Headline:** AT&T GIS dives into vertical markets (Computerworld, 1994-10-31)

**Quote:** But until AT&T's announcement ... customers had to select and buy multiple technologies and then build the applications, which are not trivial.

- P1 rationale: The quoted sentence is essentially a backward-looking characterization of the pre-1994 data warehousing market, not a forward-looking prediction about what would happen by ~1997. While it was broadly true that early data warehouses required customers to assemble multiple technologies and build custo

- P2 rationale: In the early-to-mid 1990s, most data warehousing efforts did require enterprises to combine a separate database platform (such as Teradata or Oracle), ETL tools (like Prism or early Informatica), and front-end query/BI tools, with substantial custom application development to make them work together

### row_id=812 (SH-3y, P1=2 medium / P2=0 low)

**Headline:** Apple's Supercomputing Scientists (Forbes, 2004-01-12)

**Quote:** I think 2004 is the year when Apple will make up its mind whether to seriously go back into the enterprise space.

- P1 rationale: From 2004–2007 Apple did not launch a serious, broad enterprise push; Xserve and Mac OS X Server remained niche, and Apple’s revenue and strategic focus shifted overwhelmingly to consumer products like the iPod, iTunes, and then the 2007 iPhone rather than classic enterprise infrastructure or corpor

- P2 rationale: The claim hinges on Apple internally “making up its mind” about enterprise focus in 2004, which is not directly observable from public product or strategy signals. While Apple did continue Xserve and related server products through the mid‑2000s, its primary strategic emphasis remained on consumer a

### row_id=925 (SH-3y, P1=2 medium / P2=0 low)

**Headline:** Legent increases options, flexibility in desktop line (Computerworld, 1992-11-02)

**Quote:** These things let Legent write and maintain one set of code and then say, `Let many blossoms bloom.

- P1 rationale: The claim assumed that Legent's use of Visix Galaxy and related technologies would sustainably support one code base across many desktop GUI environments, but within three years enterprise desktops had largely standardized on Microsoft Windows while OS/2 Presentation Manager and most alternative Uni

- P2 rationale: The quotation is a narrow claim about Legent’s ability to use specific tools or architectures to maintain a single code base across multiple platforms, and there is little widely documented historical evidence on whether this internal engineering goal was actually achieved in practice. Public record