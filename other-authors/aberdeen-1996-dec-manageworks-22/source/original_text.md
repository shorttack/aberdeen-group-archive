# ManageWORKS 2.2 Market Profile

> Archived from: https://web.archive.org/web/19970112012044/http://www.aberdeen.com:80/secure/profiles/decmgwk/decmgwk.htm
> Original publication date: 1996-03-01
> Author: Aberdeen Group

---

## Original Document Text

Digital Equipment Corp.
550 King Street
Littleton, MA 01460
800-DIGITAL / 800-344-4825

### ManageWORKS 2.2

#### Market Position

ManageWORKS 2.2 is a LAN management platform and multi-NOS manager designed to integrate all aspects of PC LAN administration. Digital leaves applications that address the areas of performance, accounting, software asset and configuration, network, security, storage, problem and automation management for partners to integrate into the ManageWORKS platform (some of Digital's own applications are also integrated). Digital provides a starting point with basic functionality, into which partner applications can integrate to provide more complete functionality for all areas of LAN management, rather than a complete, end-to-end management solution.

ManageWORKS is targeted at the site and workgroup level, with the number of managed nodes ranging from 10 to 800 or so. In larger installations, Digital offers POLYCENTER Manager on NetView — a higher-end SNMP management platform.

#### Organizational Structure

Dean McMillin, ManageWORKS Product Marketing Manager;
Maxine Brooker, ManageWORKS Product Manager.

#### Key Products

ManageWORKS 2.2 is a Windows application that consolidates the management of Novell NetWare servers, Microsoft LAN Manager, Digital PATHWORKS servers and IBM LAN Servers on one ManageWORKS console. It combines the management of multiple NOSs with the management of distributed SNMP networks. This gives network administrators a consistent, cross-platform view of multiple networks.

ManageWORKS functionality includes:
- discovery of TCP/IP objects across LANs and WANs;
- management of network connection devices;
- event monitoring and viewing;
- print management across disparate networks;
- user and group management, across disparate networks.

ManageWORKS consists of several components: ManageWORKS console, an Event Manager, and local pollers (see Figure 1). The Event Manager acts as a processor and repository for management. The Event Manager processes and logs all the alerts, and forwards SNMP traps to specific enterprise network management platform servers (such as OpenView or NetView servers). The console provides a user interface to view event and network status and to set monitoring parameters.

*Figure 1: ManageWORKS Architecture — Source: AberdeenGroup, March 1996*

To distribute polling responsibility, SNMP pollers can be located throughout the network and tasked with collecting data from specified nodes. The poller has a direct TCP/IP socket connection with an Event Manager and supplies the Event Manager with all status change information detected in polls. Pollers can be configured to monitor specific nodes, subnetworks or networks to minimize network SNMP traffic appropriately.

From the Event Manager, SNMP traps can be passed from ManageWORKS to an enterprise network management platform, such as POLYCENTER Manager on NetView, NetView for AIX, HP OpenView or any other network management platform capable of receiving SNMP traps. Hence, higher-level, enterprise-wide managers get a consistent, real-time view of the entire network. Users specify which information is relevant to a management platform's central server, and the server "subscribes" to only that information — so that it doesn't receive irrelevant or redundant information. This means ManageWORKS servers can act as mid-level managers for enterprise managers, localizing polling and selectively passing on only relevant information.

The ManageWORKS Event Manager is able to send information to multiple managers throughout the enterprise.

Typically, for every Event Manager there is only one corresponding Console, and the two can either reside together on the same Windows PC, or separately. However, in order to allow multiple consoles to access the same information simultaneously (though only one console can update the information at a time), management data from the Event Manager is stored on a separate file server rather than locally with the Event Manager.

The components of ManageWORKS run on Windows 3.1, Windows for Workgroups, Windows 95 and Windows NT on Intel and Digital's Alpha platforms. ManageWORKS can manage network servers running NetWare 3.x or 4.x (in bindery emulation mode), servers running LAN Manager 2.x, LAN Server, PATHWORKS, and can partially manage Windows NT servers. In addition, ManageWORKS manages any SNMP device using either the TCP/IP stack in ManageWORKS, other major vendor stacks, or the native Windows 95 or Windows NT stack.

Another nice feature in ManageWORKS is the addition of Object Creator Facility and Application Launch, which allow you to plug any DOS or Windows application into ManageWORKS without writing any code. Using a dialogue box, a user can integrate an application to have it appear as an icon on the ManageWORKS console. For tighter integration, Digital also offers a software developer's kit extension that lets users bring object management applications into the 32-bit operating environment.

#### Partnerships

A large part of Digital's ManageWORKS strategy relies on third parties to provide a complete management solution. CapaCity's NetCon and Intel's LANDesk are desktop management programs that offer configuration management, hardware and software inventory, software distribution and metering, remote control and virus protection. Also, Help Desk Technology's HelpStar offers trouble ticketing and problem tracking. ManageWORKS can also integrate Digital's own HubWatch program.

Digital has an OEM strategy for ManageWORKS that allows vendors — typically of PC servers and communications devices — to use ManageWORKS as the platform for vendor-specific management applications. These OEM partners can deliver to their customers the event manager, polling and discovery capability to extend their own product-specific offering.

#### Aberdeen Conclusions

ManageWORKS, in conjunction with POLYCENTER Manager on NetView or another enterprise-wide SNMP management platform, offers the advantage of distributing and localizing polling and event management. The product provides benefits at the workgroup level, where it offers SNMP management and management of multiple network operating systems, as well as serving as a key element within an enterprise management strategy. At the site or enterprise level, ManageWORKS gives users a consistent view of disparate networks. No other product offers this.

Competitors such as McAfee and Symantec's Norton Administrator for Networks offer a set of tightly integrated products that work well together but are not designed to incorporate other third-party solutions. Digital, on the other hand, offers the ManageWORKS platform into which users can easily incorporate best-of-breed solutions with minimal effort. This approach is unique in this market, and appeals to those who want to build their own solution out of hand-chosen applications.

---
Aberdeen Group
One Boston Place, Boston, Massachusetts 02108
Telephone: 617-723-7890 | FAX: 617-723-7897
Copyright © 1996 Aberdeen Group, Inc., Boston, Massachusetts

---

## Frictionless Data Package Metadata

> Auto-generated by Archival Ingest Skill v13

### Study Record

| Field | Value |
|-------|-------|
| study_id | aberdeen-1996-dec-manageworks-22 |
| title | ManageWORKS 2.2 Market Profile |
| author | Aberdeen Group |
| date | 1996-03-01 |
| type | market-study |
| subject_domain | LAN-management-software |
| methodology | industry-analysis, competitive-profiling, document-review |
| source_file | 1996 DEC - ManageWORKS 2.2 pr.pdf |
| license | CC-BY-4.0 |

### Abstract

This Aberdeen Group product profile evaluates Digital Equipment Corporation's ManageWORKS 2.2, a multi-NOS LAN management platform designed for site and workgroup environments of 10 to 800 nodes. The study assesses ManageWORKS' architecture, partner ecosystem, and competitive positioning against McAfee and Symantec's Norton Administrator for Networks, concluding that its open, partner-extensible approach is unique in the market.

### Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | medium | Documented an early 1990s LAN management platform at a pivotal moment in multi-NOS administration; Aberdeen endorsement carried weight, but ManageWORKS was niche. |
| **Relevance** | low | ManageWORKS 2.2 and the multi-NOS LAN management category are obsolete; architectures have been entirely replaced by modern network management stacks. |
| **Prescience** | medium | Aberdeen's claim of open platform uniqueness was partly correct short-term, but the platform was discontinued after DEC's 1998 acquisition by Compaq, undercutting the implied prediction. |

### Prescience Detail

**Prediction 1:** ManageWORKS strategic advantage viability
- **Claimed:** Open platform strategy positions ManageWORKS to maintain competitive edge in LAN management market
- **Year:** 1996
- **Confidence at time:** medium

**Actual Outcome 1:** ManageWORKS strategic advantage viability - actual outcome
- **Result:** Digital Equipment Corporation acquired by Compaq in June 1998 for $9.6B; ManageWORKS product line discontinued
- **Confidence:** verified
- **Notes:** DEC's acquisition ended ManageWORKS development; Compaq focused on enterprise hardware, not DEC's LAN software products

### Entities Referenced (11)

| Entity | Type | Status | Successor |
|--------|------|--------|-----------|
| Digital Equipment Corporation | company | acquired | Compaq (1998) -> HP (2002) |
| Aberdeen Group | firm | acquired | Harte-Hanks 2001 |
| Novell, Inc. | company | acquired | Attachmate (2011) -> Micro Focus (2014) |
| Microsoft Corporation | company | active | — |
| IBM Corporation | company | active | — |
| Hewlett-Packard Company | company | active | Split into HP Inc. and HPE in 2015 |
| CapaCity (NetCon) | company | dissolved | — |
| Intel Corporation | company | active | — |
| Help Desk Technology Corporation | company | acquired | Absorbed by ITSM vendors |
| McAfee Associates | company | acquired | Intel 2011; McAfee 2017; STG 2021 |
| Symantec Corporation | company | acquired | Broadcom 2019 |

### Technologies Referenced (8)

| Technology | Category | Vendor | Lifecycle (at study) | Lifecycle (current) |
|------------|----------|--------|---------------------|---------------------|
| ManageWORKS 2.2 | application | Digital Equipment Corporation | mature | obsolete |
| Novell NetWare | platform | Novell | mature | obsolete |
| Microsoft Windows NT | platform | Microsoft | emerging | obsolete |
| SNMP | protocol | IETF | emerging | active |
| POLYCENTER Manager on NetView | application | Digital Equipment Corporation | mature | obsolete |
| HP OpenView | application | Hewlett-Packard | mature | obsolete |
| Intel LANDesk | application | Intel | emerging | active |
| Digital PATHWORKS | platform | Digital Equipment Corporation | mature | obsolete |

### Observation Summary

- Total observations: 20
- By type: strategy-classification (3), technology-assessment (8), framework-factor (3), expert-opinion (2), viability-prediction (1), actual-outcome (1), benchmark-result (0), market-data (0)
