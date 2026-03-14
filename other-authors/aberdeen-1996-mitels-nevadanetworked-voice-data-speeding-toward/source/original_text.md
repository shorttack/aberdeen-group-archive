# Mitel's NeVaDa (Networked Voice and Data) – Speeding Toward Convergence

> Archived from: https://web.archive.org/web/19970112011929/http://www.aberdeen.com:80/secure/profiles/mitel/mitel.htm
> Original publication date: 1996-04-02
> Author: Aberdeen Group

---

## Original Document Text

Mitel's NeVaDa™(Networked Voice and Data) – Speeding Toward Convergence
Executive Summary
April 2, 1996 — Mitel Corporation, a pioneer in the development of Computer Telephony Integration (CTI) solutions, today announced NeVaDa™ (Networked Voice and Data), an integrated
broadband enterprise backbone system architecture. NeVaDa represents the next logical step in the company's realization of its vision of a truly converged voice, data and video multimedia
network within the enterprise.
Mitel, a major presence in the international telecommunications field, provides enterprise, workgroup, and desktop solutions, as well as gateway and open server-based communications
products, systems and components. Mitel is known for its expertise in fiber-linked customer premises equipment, call center applications, and CTI solutions featuring flexible and open
distributed architectures, such as the MediaPath software platform. Relationships with Digital Equipment Corpora-tion, Intel Corporation, Microsoft Corporation and Madge Networks have
strengthened the company's position in the information technology and networking arenas.
Mitel's mission is to distinguish itself as a global leader in Computer Telephony Integration by creating communications solutions that offer value to the end-user through CTI. The company
has partnered with Madge Networks, an important player in intelligent LAN switching and WAN technologies, to create a common enterprise backbone infrastructure capable of melding
both voice and data.
NeVaDa represents the continuing metamorphosis of Mitel's traditional SX-2000® PBX platform into an integrated call server on a common enterprise backbone. This solution is based on a
Madge Networks switch module that has the capacity to transport voice, video and data traffic over a single, integrated fiber backbone, thus simplifying the backbone cabling infrastructure.
This broadband solution also extends network management capabilities in order to provide end-to-end control and traffic management through a unified management interface.
Intelligent Evolution Toward CTI
Since the late 1980's, an architectural framework has been evolving to link computer and telecommunications platforms. Known as CTI (Computer Telephony Integration), this framework
originally combined mainframe platforms with proprietary telecommunications application programming interfaces. As the shift toward distributed computing, open standards and increased
bandwidth expands, CTI is evolving from a limited solution to more widespread technology. It promises accelerated, less complicated methods for both customers and employees to access
critical information resources.
Aberdeen research reveals that enterprise end-users are investigating migration paths to high-speed, "on-demand" multimedia local- and wide-area network transmission technologies such as
Asynchronous Transmission Mode (ATM) or Synchronous Optical NETwork (SONET). Most importantly, they are also seeking ways to optimize their communications resources by
leveraging their existing networks. The current movement to integrate telecommunications as part of the IT planning agenda is being driven by the realization that there are cost benefits
which accrue from simplifying and combining infrastructures, including improved support and better leveraging of the enterprise backbone for the consolidation of LAN/WAN traffic.
Mitel's CTI Vision
In response to this trend, Mitel's approach has been to evolve the PBX into an integrated server on a broadband transport backbone. The company's vision, first articulated in 1991, reaches
beyond the traditional model of CTI, and is centered on the belief that true computer and telephony convergence will result in the provision of information through a single IT-centric
infrastructure.
The first step Mitel took to accomplish the transformation of PBX-to-integrated call server was to break the PBX into modular elements that provided adaptability and scalable functionality
for up to 192 users on each node. The nodes were then linked via fiber and distributed throughout the network.
The next step resulted in peripheral, network gateway and applications gateway nodes that enabled end-users to add or change components without having to modify or replace the entire
system. This was followed by a third phase, in which network management capabilities were added.
By migrating its earlier proprietary architecture toward an open, distributed model of communications switching and delivery, Mitel's solutions are positioned to take advantage of high-
bandwidth opportunities and offer investment protection. In the Mitel model, the PBX would provide all call control services within a broadband-based enterprise network connected to
external interoperable ATM networks, both public or private.
Introducing NeVaDa
The NeVaDa roll-out is the most recent addition in Mitel's realization of its vision of a common voice-and-data enterprise broadband backbone infrastructure. This offering, which migrates
call control to specialized servers on the backbone, consists of a systems architecture which permits the combining of existing separate voice and data networks within the business premises.
At the transport level, this is accomp-lished by integrating voice and data streams using standards-based OC-3 fiber optic technology. This resulting network and its voice and data elements
can be managed from a UNIX workstation running the HP OpenView open management platform.
NeVaDa's Modular Topology
The NeVaDa backbone topology is based on a star architecture referred to as a collapsed backbone network. Individual backbone links connect distributed workgroup hubs to one or more
central collapsed backbone hubs through which all LAN traffic is switched. These collapsed backbone hubs connect to one LIGHT Main Control Node (See Figure 1). Redundancy is
optional and easily available. The high-speed OC-3 fiber optic backbone links have the capability of carrying LAN packet data traffic as well as voice. Ultimately, the product will evolve to
full ATM.
Workgroup hubs typically support one LIGHT Peripheral Node with a capacity of 192 voice ports or desktop telephone sets in each distributed workgroup. Workgroup hubs can support other
LIGHT nodes – for example, DSU, ISDN or Application Gateway Nodes. The collapsed backbone and workgroup hubs support a variety of LAN technologies in switched or shared media
modes of operation, including Ethernet, Token Ring, FDDI and 100 Base-T.
Figure 1: NeVaDa Backbone Topology

Source: AberdeenGroup, April 1996
Each backbone segment or point-to-point connection between the collapsed backbone hub and the workgroup hub requires a backbone interface module, which is located in each hub. For
ATM transmission, this module will convert Ethernet data packets from the LANSwitch bus to ATM data cells which will be multiplexed with the constant bit rate voice streams from the
LIGHT Nodes across the fiberoptic backbone link. The LANswitch does not handle any LIGHT Node voice traffic.
The voice telephony services are provided by the nodes from the SX-2000® LIGHT Controller Node distributed PBX system. The SX-2000 LIGHT Main Control Node is a redundant,
enterprise-level server which offers basic call control as well as advanced individual and telephony groupware features such as hunt, broadcast and Automatic Call Distribution (ACD)
groups.
LAN data traffic moving from a desktop PC in one workgroup hub to another workgroup hub will be switched first to the collapsed backbone hubs and then onto the proper backbone vertical
link to its destination workgroup hub and desktop PC.
WAN access is provided by Mitel's SX-2000 LIGHT DSU (T1/E1 links) or network gateways which provide PRI links. The functionality of these nodes is identical to that of a standard SX-
2000 LIGHT system. Nodes may either be located in the same area as other enterprise-level servers or near the building access point for WAN connectivity. The Network Gateway node can
connect directly to the LIGHT Main Control Node or may be connected over the backbone via a workgroup hub. Analog trunk access can also be supported, if required.
The Madge Networks Relationship
The LAN data network infrastructure and services are provided through the Madge MultiNet series of intelligent switching hubs, modules and Multiman network management products.
MultiNet hubs support both Ethernet and Token Ring shared media LAN segments, as well as high performance switched Ethernet technology, through the high speed 1.28 Gbps LANswitch
bus located with each hub. Dynamically switched point-to-point connections are established between the switched-LAN interface cards within each hub and across backbone links to other
hubs and segments by the Madge LanSwitch bus.
The Benefits
NeVaDa's modular, building block approach simplifies the backbone cabling infrastructure in the enterprise by eliminating wiring redundancies. In addition, this architecture provides flexible
deployment options for telephony and computing servers, and room for growth. Advantages that arise from using a proven LAN switching technology such as Madge Networks' include:
scalability (adding ports does not affect already existing ones), performance improvement and fault tolerance.
Aberdeen considers the main benefit of Mitel's approach ultimately to be the enabling of in-building distribution of all voice and data communications via one big backbone ATM or SONET
pipe. This will result in the capability of end-user access to CTI multimedia applications at the desktop in a cost effective manner, and will permit more effective management of the entire
communications network, while leveraging the potential of new and emerging technologies.
The Challenges
Mitel is venturing forth in a challenging market space. Aberdeen agrees with Mitel's assessment that the Information Technology view of the world is, and will continue to be, the de facto
communications model. As a result, voice will have to be effectively integrated within existing information processing environments. Open systems will be required to enable the integration
of existing networking and desktop operating systems and standards. Telecommunications will, however, continue to play an essential role, bringing to convergence its own set of core
competencies, which include reliability, manageability and uptime.
Telephony and computing have, until very recently, been considered two separate worlds, with distinct outlooks, approaches and cultures. Aberdeen research concludes that data and telecom
systems are still separate in most organizations today. Historically, IT has had little, if anything, to do with telephony decision-making and management.
Within the IT community, there is initial distrust of most telecommunications vendors, due to a perception that telecom companies are lacking strong integra-tion and software development
skills. Additionally, there is concern about the reliability of telecom functions when they are incorporated into the data environ-ment and concerns about the ability to integrate with existing
and future systems.
Mitel is well aware of its challenges here. To its credit, the company recognizes that the ultimate success of CTI depends upon leveraging and melding the technologies and talents from both
the computer and telephony environments. The company has carefully chosen its computer industry partners, which include Digital Equipment Corporation, Intel Corporation and Microsoft
Corporation as well as Madge Networks, who are experts and leaders in their disciplines.
Conclusions
Aberdeen views NeVaDa as a logical and required step in the company's migration of the PBX interface to an integrated digital network. To date, the company has made several important
moves to facilitate the convergence of voice and data – improvements to customer premises equipment with the fiber-connected "LIGHT" products, innovative call center applications, and
the development of new products for multimedia networks, CTI and local area networks. While Mitel is
not alone in its open-architectured approach, it is the first major PBX manufac-turer to take significant steps in implementing full CTI voice and data at the enterprise level.
Aberdeen considers the provision of Token Ring as well as Ethernet support to be a significant differentiator for Mitel. Other competitors in this space have opted to design their CTI
solutions solely around Ethernet solutions. The inclusion of both technologies gives NeVaDa flexibility and a wider appeal.
Mitel is forging ahead toward the multimedia future, but it is still early in the CTI market lifecycle. In order to achieve its goal of leadership in the integrated CTI market, the company will
have to surmount significant hurdles. Because the Computer Telephony Integration arena is becoming an increasingly competitive environment, Mitel must implement its vision quickly and
effectively. It must also secure needed ATM technology in order to meet its proposed ATM-enabled upgrade in a timely fashion.
Because Mitel is not yet a household word within the data community, its strategic partnerships with networking equipment and software suppliers are key to its success. The initial
partnerships the company has formed are helping to establish its credibility in the IT community. The relationship with Madge Networks should be expanded to take advantage of Teleos'
WAN integrated access technology. Additionally, the company needs to leverage its existing relationships with Digital Equipment Corporation, Microsoft Corporation and Intel Corporation
and develop new alliances that can provide access to the video components of multimedia, such as video servers, as well as expanded channel opportunities.
As a migration-path strategy, Mitel's approach makes good common sense. By embracing open standards and a flexible, modular approach, the company has created an alternative to the
traditional PBX approach, leveraging existing invest-ments in telephony and IT infrastructures as well as offering economies of scale.
Aberdeen Group Registration and HTML Market Research
Home Page || General Information || Aberdeen Abstracts
Aberdeen Group Publications||Custom Consulting
Aberdeen Group
One Boston Place
Boston, Massachusetts

02108
Telephone: 617-723-7890
FAX: 617-723-7897
The trademarks and registered trademarks of the corporations mentioned in this publication are the property of their respective holders. Unless otherwise noted, the entire contents of this publication are copyrighted by Aberdeen
Group, Inc. and may not be reproduced, stored in a retrieval system, or transmitted in any form or by any means without prour written consent of the publisher.
Copyright © 1996 Aberdeen Group, Inc., Boston, Massachussetts
This Document is for Electronic Distribution Only -- DO NOT COPY


---

## Frictionless Data Package Metadata

> Auto-generated by Archival Ingest Skill v13

### Study Record

| Field | Value |
|-------|-------|
| study_id | aberdeen-1996-mitels-nevadanetworked-voice-data-speeding-toward |
| title | Mitel's NeVaDa (Networked Voice and Data) – Speeding Toward Convergence |
| author | Aberdeen Group |
| date | 1996-04-02 |
| type | market-study |
| subject_domain | telecommunications-CTI |
| methodology | industry-analysis, competitive-profiling, field-research |
| source_file | 1996 Mitel NeVaDa Networked Voice Data speeding toward.pdf |
| license | CC-BY-4.0 |

### Abstract

Aberdeen Group profiles Mitel Corporation's NeVaDa (Networked Voice and Data) platform, announced April 2, 1996, as a strategic move to transform Mitel's SX-2000 PBX into an integrated voice-data-video server on a broadband ATM/SONET enterprise backbone. The study documents the IT industry's growing demand for voice-data convergence, evaluates NeVaDa's modular collapsed-backbone topology with Madge Networks LAN switching, and assesses Mitel's competitive position and strategic risks in the emerging CTI market. Aberdeen concludes NeVaDa is a logical step toward convergence but notes Mitel must move quickly, secure ATM technology, and build credibility in the data networking community.

### Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | medium | Documented an early enterprise voice-data convergence architecture at a critical juncture, when IT and telecom worlds were just beginning to merge; Mitel's PBX-to-call-server evolution path anticipated UCaaS by a decade, though DEC/Intel/Microsoft partnerships were not yet sufficient to make Mitel a household name in IT. |
| **Relevance** | medium | The architectural vision — converging voice, data, and video over a single enterprise backbone — directly predicts modern UCaaS, SD-WAN, and WebRTC paradigms. The analytical framework for evaluating PBX-to-IP migration remains applicable to ongoing legacy telephony modernization challenges. |
| **Prescience** | medium | Aberdeen correctly identified that voice-data convergence would succeed and that IT culture would ultimately define the model, but overestimated Mitel's ability to lead the space; Mitel went through multiple ownership changes and narrowly avoided extinction before becoming a significant Unified Communications vendor by the 2010s. |

### Prescience Detail

**Prediction 1:** Voice-data convergence inevitability
- **Claimed:** True convergence of voice, data, and video in single IT-centric infrastructure will occur
- **Year:** 1996
- **Confidence at time:** high

**Actual Outcome 1:** Voice-data convergence outcome
- **Result:** VERIFIED — VoIP (SIP/H.323) displaced PBX by ~2005-2010; UCaaS (Microsoft Teams, Zoom, Cisco Webex) fulfills the unified multimedia desktop vision
- **Confidence:** verified
- **Notes:** IT-centric model prevailed exactly as Aberdeen predicted; ATM was bypassed in favor of IP

**Prediction 2:** Mitel CTI market leadership prediction
- **Claimed:** Mitel can achieve CTI market leadership if it implements vision quickly and secures ATM technology
- **Year:** 1996
- **Confidence at time:** medium

**Actual Outcome 2:** Mitel corporate outcome
- **Result:** PARTIAL — Mitel survived multiple ownership changes; became mid-market UC leader through acquisitions; filed Ch.11 bankruptcy March 2025, exited June 2025
- **Confidence:** verified
- **Notes:** Never achieved global CTI leadership but remained a significant vendor. Source: Wikipedia Mitel; https://en.wikipedia.org/wiki/Mitel

### Entities Referenced (7)

| Entity | Type | Status | Successor |
|--------|------|--------|-----------|
| Mitel Corporation | company | active |  |
| Aberdeen Group | firm | acquired | Harte-Hanks / Aberdeen (brand revived) |
| Madge Networks | company | dissolved | Ringdale (via Network Technology UK) |
| Digital Equipment Corporation (DEC) | company | acquired | Compaq / HP |
| Intel Corporation | company | active |  |
| Microsoft Corporation | company | active |  |
| Hewlett-Packard (HP) | company | active | HP Inc. / HPE |

### Technologies Referenced (7)

| Technology | Category | Vendor | Lifecycle (at study) | Lifecycle (current) |
|------------|----------|--------|---------------------|---------------------|
| Mitel NeVaDa (Networked Voice and Data) | platform | Mitel Corporation | emerging | obsolete |
| Mitel SX-2000 LIGHT PBX | platform | Mitel Corporation | mature | obsolete |
| ATM / SONET (OC-3 fiber backbone) | protocol | Multiple | emerging | obsolete |
| Madge MultiNet Intelligent Switching Hub | platform | Madge Networks | mature | obsolete |
| Mitel MediaPath Software Platform | framework | Mitel Corporation | mature | obsolete |
| Computer Telephony Integration (CTI) | framework | Multiple | emerging | active |
| HP OpenView | application | Hewlett-Packard | mature | legacy-supported |

### Observation Summary

- Total observations: 22
- By type: actual-outcome: 3, expert-opinion: 2, framework-factor: 6, market-data: 3, strategy-classification: 2, technology-assessment: 4, viability-prediction: 2
