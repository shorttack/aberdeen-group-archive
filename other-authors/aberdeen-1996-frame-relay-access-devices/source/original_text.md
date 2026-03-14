# Frame Relay Access Devices

> Archived from: [https://web.archive.org/web/19970604113801/http://www.aberdeen.com:80/secure/profiles/netlink/netlink2.htm](https://web.archive.org/web/19970604113801/http://www.aberdeen.com:80/secure/profiles/netlink/netlink2.htm)
> Original publication date: 1996-06-01
> Author: Aberdeen Group

---

## Original Document Text

Netlink, Inc.
1881 Worcester Road
Framingham, MA 01701
508-879-6306
http://www.netlink.com
Frame Relay Access Devices
Frame relay packet services are an increasingly popular means for interconnecting enterprise data networks that cover wide areas. For some users, frame relay services offer big savings
versus using leased lines. This profile is intended to provide decision support to end-users choosing frame relay access equipment components to link multiprotocol LANs.
Implementing frame relay access for mixed protocol branch offices using SNA and LAN can result in a risk that mission-critical traffic will experience unacceptable problems, such as
latency and congestion. When using both public and private frame relay service applications, an end-user’s choice of access equipment is a key factor that determines the quality and
continuity of frame-relay connections.
Netlink, located in Framingham, Massachusetts, is a manufacturer of frame relay access devices, or "FRADs." The company markets FRAD products based on a switching architecture that
provides an optimal combination of speed with low cost and ease of management for multiprotocol LANs.
This Profile covers three related Netlink product lines which are each intended to be used as the access connection of a frame relay WAN. TurboFRAD™ is used for branch office
interconnects, and OmniFRAD™ functions as a hub for a star network. Most often, an OmniFRAD interconnects many TurboFRADs. The third product, NetFRAD™, is a network based
access node intended as a carrier solution. In addition to its access products, Netlink offers OmniLinx™8000, an edge switch aimed primarily at private and hybrid frame relay networks.
Potential frame relay users are posed with the choice of purchasing either routers or FRADs. The FRAD handles both SNA and LAN traffic (IP and IPX) and other protocols, such as bisync,
async, X.25, etc. Aberdeen field research finds that geographically distributed enterprises — especially those carrying a substantial SNA traffic mix (over 40%) or those for which SNA is
performance-sensitive and mission critical — will benefit greatly from choosing FRADs. The Aberdeen Group found that many customers consider their Netlink FRADs to have reliable
functionality as a high-end FRAD — and for data rates below T3, as a router.
Frame relay services reduce costs through optimal bandwidth utilization. Choosing a FRAD versus a router can more efficiently utilize allotted bandwidth in order to maximize these savings.
In addition, FRADs provide the level of network priority management required for fastest throughput with fewer conflicts at the WAN interface point. Access devices that handle frame relay
traffic should provide the same quality of service as existing combinations of leased lines. Combining mission critical SNA traffic with LAN traffic introduces a heightened potential for
congestion and conflict that must be managed cautiously.
Market Position
Frame relay is a rapidly growing network service that began with offerings in 1991, and has started to erode a portion of the leased-lines market. Because user needs for bandwidth are
expanding, multi-protocol WAN connections must be scaleable, and should be adaptable to new uses. Currently, cell-relay (ATM) networks for high-throughput (T3 speeds and above) real-
time applications are being developed to integrate with the expanding frame-relay base.
Netlink is focused on one consistent product line that serves the needs for interconnecting data collection centers and network access nodes. Each of the three products can be custom
configured according to the needs of the client, including protocol choice and throughput.
Netlink is well positioned with partnerships that enable it to provide product installation and support tailored to suit any size customer’s needs. IBM and Netlink have a service agreement
that enables quick response times and dependable service nationwide. This is especially convenient to those with SNA networks who already depend on IBM service. Netlink also has
contracted with Anixter, a world-wide systems integrator capable of responding to the needs of any size client.
FRADs meet the widespread need for SNA-compatible integration via frame relay. Especially for the "legacy" category that makes up a sizable part of the installed base, there are significant
price/performance advantages in choosing a Netlink FRAD over a router.
Frame Relay
Frame relay emerged in the last decade as a digital evolution of X.25 packet switching. Because digital transmission facilities have much lower error rates than analog lines, frame relay was
developed as a simplified form of variable-length packet switching that was intended to accommodate "bursty" data transmissions. Frame relay network switches differ from X.25 in that they
do not perform extensive overhead functions for error correction and flow control processing. Rather, these functions are performed by the end-user access device, such as a router or a
FRAD. Reduced network overhead allows more efficient throughput and lowers transmission cost.
Bursty traffic can be accommodated with low latency because frame relay traffic relies on a simple format that encapsulates data in variable lengths. Identifiers in each capsule establish
"virtual circuits" within the WAN. At the access points, these virtual connections are statistically multiplexed in order to reduce WAN line capacity requirements. As time-sensitive data flows
begin to reach capacity, time division multiplexing is imposed on traffic, according to management priorities.
With FRADs, the dynamic prioritization of protocols using software settings is a relatively simple process that takes place at the lower OSI levels. This streamlined scheme of handling is
consistent with the intended efficiencies of the frame relay packet format and other broadband protocols.
Customers
Netlink’s existing customers praise the company and its products. Their initial reasons for choosing Netlink FRADs are consistent:
• Moving to frame relay service costs less than leased lines.
• Their multi-protocol branch offices carry SNA traffic.

• Consolidating branch office traffic via a star topology makes sense.
The needs of Netlink FRAD clients vary, for example: connecting branch bank sites, organizing a major electric utility’s information systems, or establishing points of presence nationwide.
In addition to enterprises that utilize Netlink’s products to connect their SNA and LAN users, frame relay service providers have selected Netlink FRADs as the basis for their SNA and SNA
plus LAN offerings, including at least one service provider that will use NetFRAD to deliver a network-based SNA over frame relay service.
Netlink customers report they like the manner in which Netlink’s FRADs work as routers to handle IP and IPX traffic from the LAN. They are also pleased with the scaleability of the Netlink
Matrix VC™ architecture. Each FRAD handles many different protocols and may be upgraded through the addition of ports and software.
Payback often occurs within 12 to 18 months, due to the 20-25% reduction in those costs associated with leased lines. Some customers cite even more significant savings in MIS labor costs
and reduced network licensing fees.
Customers emphasize the strength of Netlink’s service and support, and most would repeat their purchase if they could. They also cite Netlink’s commitment to making products work for all
applications. One customer, who had previously chosen another FRAD vendor, reported being "able to handle maybe five users," and after changing to OmniFRAD he found its RISC
architecture gave him the capability to "increase the number of users by tenfold." Using the menu-driven interface, this customer noted, configuring new users "usually takes less than five
minutes."
Figure 1: Frame Relay Network Architecture
Source: AberdeenGroup, June 1996
Netlink has a superior product. Netlink’s FRADs "are well built and they work well," said a customer.
Products
Netlink’s products are designed to meet the frame relay needs of a multi-protocol environment in which branch offices consolidate their traffic on a frame relay line for communication with a
central data site. They are designed to handle the conflicting needs of consolidated network traffic.
The FRADs are built around the Matrix VC architecture, and they rely on Intel i960 RISC microprocessors operating in parallel on each port. All network features are software definable,
including prioritization of traffic. The combination of high performance hardware and software represents a sound choice in the face of potentially expanded uses of frame relay.
Each FRAD operates both as a switch and a router, because it handles frame relay switching requirements as well as routing IP and IPX LAN traffic. Netlink’s products switch protocols such
as: SDLC, LLC2, QLLC/X.25, Bisync, Async, Frame relay and HDLC. This combination covers the mix commonly found in branch offices.
Frame relay carrier networks relegate congestion management to the attached equipment; this means that a FRAD or router is given the task of managing network congestion. Congestion is
where routers fall short and FRADs excel. For most LAN traffic, congestion is not much of a concern, because nobody complains when their e-mail takes an extra 30 seconds to reach its
destination or if a file transfer takes a little longer. However, mission critical SNA traffic is highly sensitive to congestion, making applications crawl to a standstill under high-traffic
conditions.
FRADs handle SNA traffic using RFC 1490, a standardized encapsulation method that produces 9 bytes of overhead per frame; this compares to router based methods such as TCP/IP
encapsulation of SDLC frames and Data Link Switching which produce 70 bytes and 50 bytes of overhead respectively per frame. Routers are far less efficient at handling SNA traffic. At
peak loading, router overhead consumes at least 50% of the SNA frame, slowing the SNA data to a trickle.
Table 1: Key Netlink FRAD Features
Turbo FRAD
OmniFRAD
NetFRAD
Std # ports
4
4
2T-1 or 4 serial
Total # ports
8
64
22T-1 or 96 serial
Route IP/IPX
yes
yes
yes
RFC 1490
yes
yes
yes
Storage
flash
hard drive
2 hard drives
LAN connectivity
1 Ethernet or
Token Ring
2 Ethernet or
Token Ring
2 Ethernet and/or Token Ring
Netlink’s OmniLinx 8000 addresses the needs of private and hybrid(public/private) networks with capabilities typically found only in a backbone switch, in addition to the multiprotocol
FRAD and routing functions of Netlink’s existing product family.
Source: AberdeenGroup, June 1996
Netlink FRADs prioritize SNA traffic with SafeLinx™, and they are the only FRADs which can utilize all available bandwidth of the frame relay line. Maintaining local acknowledgment for
SNA sessions reduces WAN traffic load and lowers potential for breakdown. Users can assign bandwidth to individual protocols, SNA logical connections, or MAC addresses for LAN
traffic, thereby guaranteeing a minimum bandwidth to each type of traffic.
SafeLinx also provides transparent backup to dynamically direct traffic around network failures. Customers note this backup feature eliminates the need for extra backup lines and ports
needed by other FRADS. One commented: "We have a network analyzer, and I can see how, when the frame relay network fails, OmniFRAD works around it."
Netlink’s entire product family can be managed by the company’s SNMP-based OmniView™ network management system. OmniView, which is based on an HP OpenView foundation,
provides full operational, maintenance and management control of Netlink devices and of the frame relay network. For traditional SNA networks, Netlink products support an embedded
NetView agent that extends SNA network management from an IBM-mainframe NetView console to include Netlink products.

Key features of Netlink FRADs are:
• Frame Relay access combined with router capability;
• SafeLinx:
• Software management optimizes traffic,
• With all variants of RFC 1490 encapsulation it yields superior SNA conversion, and
• Virtual circuit backup allows dynamic remapping;
• Expansion ports allow customization; and
• Switched architecture is reliable and fast.
Netlink’s FRAD products are designed to provide frame relay connectivity at all levels of the network. They best handle mixed protocol traffic from LANs and SNA legacy systems.
The Future for Frame Relay
Given the low cost of frame relay access devices and the associated savings in line charges, labor costs, and software license fees, some product users report they recover the costs of their
FRADs in less than 12 months. Aberdeen found that the data services market for this technology will remain robust into the next century.
Most larger telecommunications carriers are actively contending for the frame relay services market. Currently, the inter-exchange carriers (IXCs) dominate the frame relay market segment.
In part this is because they have already invested in the required technology, but the driving factor is the underlying demand created by leased line customers seeking new savings. Recent
RBOC efforts at gaining a better foothold into frame relay markets indicate a healthy, competitive frame relay market that will continue to grow.
Figure 2: Frame Relay as an "edge" to an ATM network
Source: AberdeenGroup, June 1996
The anticipated network migration to ATM, a form of real-time cell transmission for integrated voice, video, and data at extremely high speeds, is unlikely to displace frame relay. Aberdeen
predicts that it is far more likely frame relay will remain integral to the ATM migration, with ATM initially appearing as a backbone transmission means, fed primarily by a frame relay "edge
network."
In the light of these developments, Aberdeen Group believes that Netlink FRADs represent a sound investment decision. In the short term, Netlink FRADs bring data transmission savings —
for mixed traffic and SNA users in particular — and they offer tail circuit consolidation savings with greater assurances for quality of service and management than other FRADs. The
associated savings in line costs alone generate a relatively quick return on investment, further amplified by savings in support costs.
In the longer term, Netlink products may confer a distinct advantage as well. As described above, data traffic levels and traffic types will continue to grow. WAN data services will most
likely evolve to accommodate a broad mix of application types, and this mix will require the ability to perform demanding tasks: dynamically managing flows, "toggling" between dedicated
and on-demand circuits, and handling new types of traffic in a flexible, scaleable way. Netlink’s Matrix VC™ architecture represents an elegant approach to meet these needs, and the
software upgradeability of Netlink FRADs provides for a smooth transition to future capabilities.
Conclusion
The reasons for using FRADs are simple: cost savings and reliability. Replacing leased line data transmission with frame relay service can bring savings, and for geographically dispersed
enterprises these savings can be substantial. However, end-users must manage frame relay traffic at the network access point. The unique needs of multi-protocol networks make routers more
costly than FRADS, because routers can cause mission critical SNA network functions to fail. Netlink FRADs are an effective way to scale distributed points in an enterprise-wide frame
relay network.

AberdeenGroup, Inc.
One Boston Place
Boston, Massachusetts
02108 USA
Tel: 617.723.7890
Fax: 617.723.7897
Contact Information:
Susan Rinehart, Client Services Manager(direct #: 617.854.5212)
David Borde, Marketing Manager (direct #: 617.854.5226)
Email: rinehart@aberdeen.com or borde@aberdeen.com
The trademarks and registered trademarks of the corporationsmentioned in this publication are the property of their respective holders. Unless otherwise noted, the entire contents of this publication are copyrighted by Aberdeen
Group, Inc. and may not be reproduced, stored in a retrieval system,or transmitted in any form or by any means without prior written consent of the publisher.
Copyright © 1996 Aberdeen Group, Inc., Boston, Massachussetts
This Document is for Electronic Distribution Only
-- DO NOTCOPY --


---

## Frictionless Data Package Metadata

> Auto-generated by Archival Ingest Skill v13

### Study Record

| Field | Value |
|-------|-------|
| study_id | aberdeen-1996-frame-relay-access-devices |
| title | Frame Relay Access Devices |
| author | Aberdeen Group |
| date | 1996-06-01 |
| license | CC-BY-4.0 |
| source | https://web.archive.org/web/19970604113801/http://www.aberdeen.com:80/secure/profiles/netlink/netlink2.htm |

### Abstract

This Aberdeen Group profile evaluates Netlink, Inc.'s family of Frame Relay Access Devices (FRADs) including TurboFRAD, OmniFRAD, NetFRAD, and the OmniLinx 8000 edge switch. The study examines the technical advantages of FRADs over routers for mixed SNA/LAN enterprise WAN environments, documents customer ROI through 20-25% leased-line cost savings, and predicts that frame relay will remain integral to the eventual ATM migration as an edge network.

### Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | medium | Documented the FRAD vs. router decision at peak frame relay adoption; useful for understanding the SNA-to-IP transition period and WAN technology competitive dynamics of the mid-1990s. |
| **Relevance** | low | Frame relay and SNA are legacy protocols essentially replaced by MPLS, SD-WAN, and IP-native architectures; the study is primarily of historical interest for networking technology evolution. |
| **Prescience** | high | Aberdeen's prediction that frame relay would persist as an ATM edge network rather than being displaced proved accurate; ATM never displaced frame relay which coexisted until both were eventually superseded by MPLS/IP in the 2000s. |

### Prescience Detail


**Prediction 1:** Frame Relay / ATM Migration Prediction
- **Claimed:** Aberdeen predicts ATM will appear first as backbone transmission fed by frame relay 'edge network'; frame relay will NOT be displaced by ATM
- **Year:** 1996
- **Confidence at time:** high

**Actual Outcome 1:** Frame Relay / ATM Migration Actual Outcome
- **Result:** ATM was deployed as backbone in telco networks while frame relay persisted as edge access through early 2000s; both eventually superseded by MPLS/IP, not one replacing the other as Aberdeen predicted
- **Confidence:** verified
- **Notes:** Prediction directionally correct: ATM did appear as backbone while frame relay persisted as edge

**Prediction 2:** Netlink FRAD Market Viability
- **Claimed:** Aberdeen believes Netlink FRADs represent a sound investment decision with robust data services market continuing into next century; Matrix VC provides smooth transition to future capabilities
- **Year:** 1996
- **Confidence at time:** medium

**Actual Outcome 2:** Netlink Actual Outcome
- **Result:** Netlink acquired by Cabletron Systems for ~$158-160M in stock in September 1996 — same month as this profile; Cabletron subsequently dissolved into 4 entities by 2001; frame relay products eventually discontinued
- **Confidence:** verified
- **Notes:** Source: CNET 1996-09-27; WSJ 1996-09-27


### Entities Referenced (6)

| Entity | Type | Status | Successor |
|--------|------|--------|-----------|
| Netlink, Inc. | company | acquired | Cabletron Systems |
| Cabletron Systems | company | dissolved | Enterasys Networks; Aprisma; Global Network Technology |
| Aberdeen Group, Inc. | firm | acquired | Aberdeen (Harte-Hanks) |
| IBM | company | active | — |
| Anixter International | company | acquired | Wesco International |
| Hewlett-Packard Company | company | active | HP Inc / HPE |

### Technologies Referenced (6)

| Technology | Category | Vendor | Lifecycle (at study) | Lifecycle (current) |
|------------|----------|--------|---------------------|---------------------|
| Frame Relay Access Device (FRAD) | platform | Netlink | emerging | obsolete |
| Frame Relay | protocol | Various carriers | emerging | obsolete |
| IBM SNA (Systems Network Architecture) | protocol | IBM | mature | obsolete |
| ATM (Asynchronous Transfer Mode) | protocol | Various | emerging | obsolete |
| OmniLinx 8000 | platform | Netlink | emerging | obsolete |
| Intel i960 RISC Microprocessor | platform | Intel | mature | obsolete |

### Observation Summary

- Total observations: 18
- By type: actual-outcome: 2; benchmark-result: 3; expert-opinion: 1; market-data: 2; strategy-classification: 1; technology-assessment: 7; viability-prediction: 2
