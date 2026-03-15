# Original Text: Intelligent I/O Initiative: Scaling Bandwidth for System Performance

> Source: https://web.archive.org/web/19980131062404/http://www.aberdeen.com:80/research/abstract/97100185.htm

---

 
Abstract: White Paper
Intelligent I/O Initiative: Scaling Bandwidth for
System Performance
Leading Intel architecture-based server suppliers are now
shipping products with the enigmatic label "I2O-Ready"
attached. I2O™ will be an important functional capability for
servers in the near future. And for IS planners that intend to
upgrade their server operating systems with the next releases or
service patches from Microsoft, Novell, or Santa Cruz
Operations (SCO); or the newest Intel architecture-based server
from Compaq, Hewlett-Packard, IBM or other server suppliers;
acquiring "I2O -Ready" should be a requirement. In this
Executive White Paper, Aberdeen examines the potential
performance and scalability beneﬁts users will obtain from the
industry's wide-spread adoption of I2O, describes how the
members of the I2O Special Interest Group are working
together to make I2O a new industry standard, reviews key
elements of the I2O Architecture, and analyzes what impacts IS
executives should expect from I2O technology in the future.
James Gruener
Click to see the full text of this report
 Contact Aberdeen
The Wayback Machine - https://web.archive.org/web/19980131062404/http://www.aberdeen.com:80/research/abstract/97100185.htm

---

## Frictionless Data Package Metadata

**Package Name:** 1997-intelligent-i-o-initiative--scaling-aae222  
**Archived:** 2026-03-15  
**License:** CC-BY-4.0 (https://creativecommons.org/licenses/by/4.0/)  
**Source URL:** https://web.archive.org/web/19980131062404/http://www.aberdeen.com:80/research/abstract/97100185.htm  
**Observations:** 15  
**Entities:** 8  
**Technologies:** 7  

---

## Prescience Detail

### Assessment: 3/10 — Poor Prescience

This white paper is a cautionary example of confident analyst predictions that failed to materialize. Aberdeen's recommendation that I2O-Ready should be a procurement requirement proved to be wrong on multiple dimensions.

**What Went Wrong:**

1. **I2O adoption failure** — Despite backing from Intel, Microsoft, Compaq, HP, Novell, and many others, I2O never achieved mainstream OS adoption. Windows NT/2000 included I2O support in principle but it was rarely used. The I2O SIG dissolved in the early 2000s.

2. **Problem solved differently** — The I/O bottleneck problem I2O was designed to solve was addressed through entirely different means: PCI-Express (PCIe, released 2004) provided dramatically higher bus bandwidth; modern multicore CPUs absorbed I/O processing that I2O aimed to offload; Windows Driver Model (WDM) and KMDF provided driver portability without I2O.

3. **IA-64 rationale failed** — Aberdeen positioned I2O as critical for IA-64 (Itanium) server compatibility. Itanium itself largely failed in the commercial server market, making this rationale moot.

4. **NetWare-only adoption** — The main OS that embraced I2O was NetWare 5, which itself was in decline by 2000. NetWare's market share collapsed through the 2000s as Linux/Windows Server took over.

**What Aberdeen Got Right:**

- The problem was real: IA server I/O was a genuine bottleneck in 1997, and Aberdeen correctly identified the issue.
- The general direction (offloading I/O processing from the main CPU) proved correct in concept; it just materialized through different mechanisms (smart NICs, NVMe offload, PCIe Direct).
- The prediction that server I/O architecture would need to evolve was accurate; only the specific technology vehicle proved wrong.

**Broader Lesson:** This document illustrates how analyst endorsement of nascent standards can be premature. I2O had strong industry backing but poor execution and faced the classic "chicken-and-egg" OS adoption problem that killed many well-specified standards.
