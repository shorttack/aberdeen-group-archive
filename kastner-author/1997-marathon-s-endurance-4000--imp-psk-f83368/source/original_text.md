The Wayback Machine - https://web.archive.org/web/19970604114333/http://www.aberdeen.com:80/secure/impacts/1997/mar/body.htm
February 7, 1997
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
. . . . . . . . . . . . . .
Marathon's Endurance™ 4000:
Bringing Fault Tolerance to NT Servers &
Clusters
New enterprise applications are increasingly targeted for lower-cost hardware
platforms running Microsoft's NT Server operating system. Marathon's
Endurance 4000 brings fault tolerance to mission-critical NT applications.
Caution Ahead
Aberdeen research shows an ever-increasing trend towards using the NT
Server® operating system for a wide variety of enterprise applications,
including transaction processing, electronic mail and groupware, and internet
and intranet sites. Moreover, NT is also being used for network management
activities such as hosting software-based firewalls.
Here's the caution: NT Server was never designed to run mission-critical appli-
cations without failing. No general purpose operating system makes that claim.
So, as more and more of the enterprise application jewels are hosted by NT
servers, the risk of significant business disruption from an NT server failure
rises exponentially as these servers are deployed like popcorn. What's a savvy
but paranoid Information Technology executive to do?
Microsoft's Wolfpack is an Answer, But Not The
Answer
Wolfpack is the widely discussed software from Microsoft that will provide NT
server-failover clustering when it is delivered later in 1997. Wolf-pack
technology will restart an application on an attached cluster partner. But please
note that the recovery process will be measured in minutes as a reboot is
required.
While "minutes to recover" will be good enough for many applications, it
should not be considered acceptable for truly mission-critical applications
where business and customer interactions are most important. We would put
almost all OLTP, system management, and firewall applications in the critical
category — but also many e-mail, file serving and groupware applications.
But to date, IT buyers could not really protect their mission-critical servers,
only wait for Wolfpack to be delivered, or use one of the cluster-software
middleware solutions from suppliers including DEC, NCR, and Tandem.
However, most cluster software solutions require special application versions to
ride through a failure, a problem. And there has been no true fault-tolerant
solution in the NT cluster market.
Marathon Runs NT With Endurance
Marathon Technologies Corp. of Box-borough, Massachusetts (telephone 800
884-6425) has a unique solution that brings fault tolerance to any Windows NT
Server or cluster node. The Endurance® 4000 product, now in qualified
release, has no single point of failure. It is fault tolerant. By riding through any
failure without operator intervention, it then recovers automatically and
transparently when the failed component is restored.
Importantly, the NT operating system and all user shrink-wrapped applications
are unaware that the Endurance 4000 is providing fault tolerance — no special
application software versions are required. In fact, Wolfpack or other cluster
software can run on Endurance-hardened servers.
Architecture & Operation
Four computers are required to make an Endurance 4000 configuration. Two
computers are a "mirrored" pair of Computing Elements (CE) running lock-
stepped that can be any matched, uni-processor Pentium Pro desktop or server
PC. The other two computers are Pentium Pro-class I/O Processors (IOP).
Marathon has tested its product with the leading server hardware platforms
such as Compaq, Dell, HP, IBM, and Micron.
The Endurance 4000 hardware connects a Computing Element to its IOP at the
NT hardware abstraction layer (HAL) — that is, under the level of accessibility
by normal programs. In effect, NT's processing of services is split between the
CE and the IOP. The Endurance 4000 automatically synchronizes the NT
operating system, applications, data storage, and Ethernet interfaces.
More-over, site disaster recovery is built in — each half of the configuration is
connected by an optical fiber cable that can be 1.5 kilometers (a mile) from the
other half; enough for a building or campus environment. This is an important
feature as building fires and floods that disrupt access to facilities are more
common than generally known. Thus, the Endurance 4000 is ideally suited as a
fault-tolerant server or as a fault-tolerant cluster node.
It Just Keeps on Ticking …
Because both halves — one each CE and IOP — are operating in
synchronization, no instructions are missed or data lost when either CE or IOP
is lost. Users do not see even a hiccup on failure. There is even a port to alert an
external alarm system. When the failed electronics, disk, network interface, or
power supply is replaced, CEs are synchronized by copying memory, and IOPs
are synchronized by automatically copying up-to-the-moment data to the new
disk. This is true continuous processing for NT servers and cluster nodes.
Aberdeen Group Conclusions
Users have been asking their NT servers to perform ever-more business-critical
application processing. When these application systems fail, business is
disrupted and costs and lost opportunities can sky-rocket. And fail they will.
Marathon's Endurance 4000 is a well-architected, affordable, hardware-based
solution that adds almost two orders of magnitude to NT application
availability — to about 99.99% application up-time. This is accomplished as if
by magic to the shrink-wrapped applications running on otherwise industry-
standard Intel hardware platforms.
To us, the benefits of the Endurance 4000 are obvious and compelling. The
$24,995 price is also reasonable given the value of the applications likely to be
protected. If, as we expect, Marathon's Endurance 4000 breezes through its
server hardware compatibility tests, then this valuable new product category —
fault-tolerant NT servers and clusters — will have a break-away leader.
— Peter S. Kastner
AberdeenGroup, Inc.
One Boston Place
Boston, Massachusetts 02108 USA
Tel: 617.723.7890
Fax: 617.723.7897
Contact Information:
Susan Rinehart, Client Services Manager (direct #: 617.854.5212)
David Borde, Marketing Manager (direct #: 617.854.5226)
Email: rinehart@aberdeen.com or borde@aberdeen.com
This Document is for Electronic Distribution Only
-- REPRODUCTION PROHIBITED --
Copyright © 1997 Aberdeen Group, Inc., Boston, Massachusetts

---

## Frictionless Data Package Metadata

**study_id:** 1997-marathon's-endurance-4000--imp-psk-f83368
**archive_url:** https://web.archive.org/web/19970604114333/http://www.aberdeen.com:80/secure/impacts/1997/mar/body.htm

| Field | Value |
|-------|-------|
| study_id | 1997-marathon's-endurance-4000--imp-psk-f83368 |
| title | Marathon's Endurance 4000: Bringing Fault Tolerance to NT Servers & Clusters |
| author | Peter S. Kastner |
| date | 1997-02-07 |
| type | impact-brief |
| subject_domain | server-high-availability |
| source_file | 1997 Marathon's Endurance™ 4000_ imp PSK.pdf |
| license | CC-BY-4.0 |

### Abstract

Peter S. Kastner of Aberdeen Group evaluates Marathon Technologies' Endurance 4000, a hardware-based fault-tolerant solution for Windows NT servers. With NT increasingly hosting mission-critical applications, the study examines why Microsoft's forthcoming Wolfpack clustering software provides only minutes-level failover—inadequate for true mission-critical needs—while Marathon's Endurance 4000 provides continuous, transparent fault tolerance at 99.99% uptime for ~$24,995. The study concludes the Endurance 4000 is a well-architected breakthrough that creates a new 'fault-tolerant NT servers' category.

### Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | high | First major analyst evaluation of hardware-based NT fault tolerance; Peter S. Kastner accurately identified the reliability gap in NT for mission-critical applications and positioned Marathon as a category-creating leader just as NT adoption was accelerating. |
| **Relevance** | medium | The architectural concepts (lock-step mirroring, HAL interception, campus-distance disaster recovery) are historically significant; modern HA architectures for VMs and containers evolved from these principles. |
| **Prescience** | high | Kastner correctly predicted the Endurance 4000 would become a 'breakaway leader'; Marathon survived, pivoted to software, and was acquired by Stratus Technologies in 2012 for its fault-tolerance IP. His critique of Wolfpack's 'minutes to recover' limitation proved accurate. |

### Prescience Detail

**Prediction 1:** Endurance 4000 market leadership prediction
- **Claimed:** Endurance 4000 will be 'breakaway leader' in fault-tolerant NT servers category
- **Year:** 1997
- **Confidence at time:** medium

**Actual Outcome 1:** Marathon Technologies commercial outcome
- **Result:** Marathon achieved significant commercial success; HP signed reseller agreement (2000); Aberdeen analyst confirmed '5 nines' claim in 2000 Computerworld article; Marathon grew to 1,800 customers and raised $26M funding by 2007; acquired by Stratus Technologies September 24, 2012 for fault-tolerance IP
- **Confidence:** verified
- **Notes:** Sources: Computerworld June 2000; Computerworld Sept 2012; Stratus press release. The prediction largely proved correct.

**Prediction 2:** Wolfpack inadequacy prediction
- **Claimed:** Wolfpack's minutes-to-recover model is not acceptable for truly mission-critical applications
- **Year:** 1997
- **Confidence at time:** high

**Actual Outcome 2:** Wolfpack/MSCS actual limitations outcome
- **Result:** MSCS v1 (shipped Sept 1997) had serious reliability problems; initial poor reviews from analysts; failover often took longer than expected and caused additional failures. MSCS only improved significantly with Windows 2000. Wolfpack was also delayed from Q1 1997 to Sept 1997. Kastner's assessment proved accurate.
- **Confidence:** verified
- **Notes:** Sources: Wikipedia MSCS history; Microsoft TechCommunity 2013 article; mediaroom.com Feb 1997 article on Wolfpack delay.

### Entities Referenced (10)

| Entity | Type | Status | Successor |
|--------|------|--------|-----------|
| Marathon Technologies Corp. | company | acquired | Stratus Technologies (2012) |
| Microsoft Corporation | company | active | |
| Aberdeen Group | firm | acquired | Harte-Hanks (2001) |
| Compaq Computer Corporation | company | acquired | Hewlett-Packard (2002) |
| Dell Computer Corporation | company | active | |
| Hewlett-Packard | company | active-restructured | HP Inc. + HPE (2015) |
| IBM | company | active | |
| Tandem Computers | company | acquired | Compaq (1997) -> HP (2002) |
| Digital Equipment Corporation | company | acquired | Compaq (1998) -> HP (2002) |
| NCR Corporation | company | active | |

### Technologies Referenced (6)

| Technology | Category | Vendor | Lifecycle (at study) | Lifecycle (current) |
|------------|----------|--------|---------------------|---------------------|
| Marathon Endurance 4000 | hardware | Marathon Technologies | emerging | obsolete |
| Microsoft Windows NT Server | operating-system | Microsoft | emerging | obsolete |
| Microsoft Wolfpack / MSCS | clustering-software | Microsoft | pre-release | obsolete |
| NT Hardware Abstraction Layer (HAL) | os-component | Microsoft | mature | legacy-supported |
| Marathon everRun | software | Marathon Technologies | future | acquired |
| Intel Pentium Pro | processor | Intel | mature | obsolete |

### Observation Summary

- Total observations: 21
- By type: technology-assessment (7), market-data (2), viability-prediction (2), actual-outcome (3), expert-opinion (3), benchmark-result (1), strategy-classification (1)
