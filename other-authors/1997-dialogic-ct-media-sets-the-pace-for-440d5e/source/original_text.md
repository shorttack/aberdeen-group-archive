# Original Document

The Wayback Machine - https://web.archive.org/web/19971007155702/http://www.aberdeen.com:80/secure/proﬁles/1997/dialogic/body.htm
Dialogic Corporation
1515 Route Ten
Parsippany, NJ 07054-4596
(973) 993-3000
http://www.dialogic.com
Dialogic® CT Media™ Sets The Pace For Open-
Standards Computer Telephony Development
Preface
Companies choose computer telephony (CT) solutions as a cost-effective way
to add business functionality to their existing voice and data communications
systems. This functionality usually comes from software applications that run
on a computer connected to a telephony switch. Examples of such applications
include advanced call routing and messaging, screen pops, voice mail and fax
management. In an ideal world corporate end users would simply pick and
choose the CT applications that best met their requirements, just as they do now
with desktop applications.
Many of these corporate end users ﬁnd themselves in a state of constant change
— the result of growth and corporate acquisitions. In the course of this change,
companies encounter a plethora of proprietary CT technologies. These
proprietary systems restrict their ability to choose and integrate a variety of CT
applications. End users are accustomed to open platforms within their existing
IT environments; they can pick and choose a variety of applications that are
independent of their databases or computing platforms. Because a CT platform
directly affects a company’s ability to make the most of a set of strategic CT
applications over time, it is more than a straight technology choice — it is a
business decision.
Executive Summary
Computer telephony standards initially focused on issues of hardware
interoperability, but the advent of hardware communications buses like SC Bus,
MVIP, and the recent ECTF H.100 speciﬁcation, has moved the CT industry
toward a standard means for hardware interoperability. Standards for
interoperability of different software products, however, have been slower to
develop. But with the advent of de facto standards — TAPI for call control, and
the interoperability speciﬁcations outlined in the ECTF architectural framework
such as the S.100 standard media API, the S.300 service provider interface
(SPI) to hardware devices, and the proposed S.400 object-oriented API — the
foundation has been prepared for interoperable software applications to share a
computer telephony server.
Aberdeen Group has found that standards compliance is not enough to ensure
interoperability - CT servers need a software framework to manage the
interaction between standards compliant hardware and standards compliant
applications. Aberdeen research of CT development platforms has covered a
wide variety of products — some proprietary, and some written to open
standards. In evaluating platforms that handle both media processing and call
control, Aberdeen believes that there is currently only one open platform for
CT application development and deployment. This Proﬁle is intended to
provide decision support to software developers and CT integrators who are
choosing a CT development platform.
Dialogic’s CT Media manages hardware resources on a CT server, supporting
multiple client applications through standard interfaces. Because it abstracts
hardware resource management from any S.100 CT application (TAPI support
to come in 1998), CT Media dramatically simpliﬁes the application
development cycle, and promises to lower the overall integration and support
costs for CT implementation, resulting in better investment protection for users.
The strategic advantage of a standards-based platform is that it is open to
multiple vendors’ software applications. Aberdeen ﬁnds that developing
software for CT Media servers is as sound a business decision as it is a
technology choice.
Market Position

Dialogic hardware, in the form of voice and fax boards, is commonly used in
voice mail, automatic call distribution and fax server systems. This hardware is
supplemented by a variety of applications written by third-party developers and
integrated by a computer telephony value-added reseller (VAR).
As the market leader in computer telephony hardware, Dialogic has been a
proponent of open standards, advocating the delineation between hardware and
software components within CT systems. Dialogic is a founding member of the
Enterprise Computer Telephony Forum (ECTF) and has worked with other
leading CT companies to develop a common CT architecture supported by a
variety of open interfaces. Furthermore, Dialogic has also been closely
involved in the deﬁnition and implementation of de facto standards such as
TAPI. CT Media is a development platform that implements these standards.
Today, CT application developers and CT VARs spend much of their time
managing the interface between speciﬁc hardware and individual applications.
Open standards enable a software developer to focus on writing a single
application that runs across multiple hardware platforms. This simpliﬁes the
development and integration processes, speeding time-to-market and lowering
ongoing operational costs.
CT Media is Dialogic’s ﬁrst open standard development platform — it is the
only NT-based enterprise S.100 CT platform available today.
CT Media — Product Analysis
Figure 1 outlines the architecture within which CT Media is intended to
function. CT Media is a resource management platform with basic call control
functionality. It supports the S.100 API and more advanced call control APIs
including TAPI, TSAPI and the CT Connect API via the Intelligent Switch
Extension (ISE).
Figure 1: CT Media Architecture In A Standards-Based World
Source: Aberdeen Group, September 1997
In addition, CT Media is open to other APIs, providing a comprehensive
framework that will enable multiple applications, from a variety of vendors, to
share a common set of hardware resources. Ultimately, this will allow end users
to maximize investments in CT hardware through best-of-breed applications.
S.100 is an object-oriented programming model for media processing with a C-
language API that insulates the developer from the speciﬁcs of the hardware
platform. Applications developers can now focus on developing better
applications, as opposed to managing speciﬁc hardware details.
Yet, S.100 compliance does not imply that a CT server will allow multiple
S.100 applications to share a common set of hardware resources. This is where
CT Media distinguishes itself, because CT Media allows applications from
multiple vendors to share a single CT server and its hardware resources in a
true client-server environment. An efﬁcient utilization of hardware resources
results in a system-wide maximization of port density. This is important,
because many vendors are still focused on maximizing port density between
speciﬁc hardware and proprietary applications. Applications cannot share the
same hardware, thus canceling port density beneﬁts by adding redundant
hardware and servers to accommodate additional CT applications.
With CT Media, CT system optimization is good, as one call center software
designer told Aberdeen, "because adding T-1 line cards is costly, and adding
servers is an even more costly managerial hassle." CT Media efﬁciently
manages expensive hardware resources across a client-server environment.
CT Media provides an open software interface to any SCbus or H.100 hardware
(when available) via the Dialogic Resource Developers Kit (RDK). The RDK is
available to third-party developers who wish to support multi-vendor hardware
within CT Media. When the S.300 Service Provider Interface is approved by
the ECTF, CT Media will incorporate S.300 and will support any hardware that
provides a device driver written to the standard SPI.
Competitive Analysis
Aberdeen evaluated several computer telephony development platforms from a
variety of hardware manufacturers. Since software has traditionally been linked
to the hardware upon which it runs, it has been the responsibility of the
hardware vendor to provide an API to which developers write their
applications. In Figure 2, Aberdeen compares the development platforms

according to the most important features that developers and end users require
for open standards.
Brooktrout – BOSTON
Brooktrout entered the open CT middleware arena in June 1997 with the
announcement of its BOSTON architecture. While some components of
BOSTON are available today, support for the S.100 API is not expected until
1998. BOSTON promises to adopt a similar model of open standards similar to
Dialogic’s, with a most appealing plan to support boards from a variety of
vendors, including Dialogic and Natural MicroSystems.
In the interim, BOSTON provides the promise of an future open architecture
with backwards compatibility to applications written for Brooktrout’s API on
the TR112 and TR114 Series hardware products. BOSTON does not provide a
resource manager product comparable to CT Media today.
Dialogic – Release 4 drivers
An established and mature product in the CT application development space,
R4 is a robust development platform for writing applications to control
Dialogic’s hardware. While the Release 4 drivers support TAPI, they do not
provide neither resource management services, as in CT Media, nor standard
media interfaces, like S.100, that support multiple vendors’ applications. The
R4 drivers compete with CT Media in places where applications are already
written to the current hardware.
However, some integrators will have legitimate reasons for moving to CT
Media. Beyond customer demand for open standards-based products, these
reasons include the need to share a common set of hardware resources among
multiple applications and the long-term ﬂexibility of adopting new technologies
without changing existing applications.
Mitel – MediaPath
Introduced in 1996 to perform client-server call control, MediaPath is Mitel's
open, server-based PBX that supports other vendors’ media applications.
However, MediaPath restricts a user to Mitel's switching and call control
platform, limiting a user's choices to media processing applications only. Nor
does MediaPath support the S.100 API.
Natural MicroSystems – CT Access
CT Access is NMS' proprietary development environment and API for NMS
MVIP-90 hardware. Though CT Access supports the H.100 hardware standard,
it does not support the S.100 API, TAPI, or other industry standard APIs.
Lacking the resource management services such as those provided by CT
Media, CT Access does not service multiple client applications from different
vendors. Further, CT Access is not a complete SDK — developers and
integrators must purchase other NMS development platforms to add
functionality, such as fax and speech recognition.
Rhetorex – RealCT
RealCT is a high level C++ development environment for Rhetorex and other
MVIP hardware. RealCT manages hardware resources, shielding the developer
from the inner workings of the hardware. In this way, RealCT has similar
functionality to CT Media, though it neither enables multiple applications to
share a server, nor does it provide abstraction from the hardware and platform.
Figure 2: Comparison Of CT Development Environments
Product
Dialogic
CT
Media
Dialogic
R4
Natural
MicroSystems
CT Access
Rhetorex
Real CT
Brooktrout
BOSTON
Availability?
Now
Now
Now
Now
Now
Support for
S.100 media
API?
Yes
No
No
No
No (S.100
In 1998)
Resource
Management
For Multiple
Apps?
Yes
No
No
No
No
Client-
Server?
Yes
No
No
No
No
Open
Interface To
Hardware
Via RDK?
Yes,
S.300
When
Approved.
No
No
Yes, With
No S.300
Plans
No, S.300
When
Approved
Abstraction
From
Hardware
Complete
None
Device
Device
Device

Supports 3rd
Party
Hardware
And
Technologies?
Yes
Dialogic
Only
NMS HW
Only
MVIP
Only
Scheduled
Supports
Other
Standard
APIs?
TAPI
TSAPI
CT
Connect
TAPI
No
TAPI
TAPI
And Others
In Future
Source: Aberdeen Group, September 1997
RealCT is also not standards-compliant, either to the S.100 API or the H.100
bus standard. RealCT is an essentially proprietary model and API, and as such
cannot become the de facto standard for the planned S.400 model and object-
oriented API; S.400 will be consistent with the existing S.100 object-oriented
model.
Customer Beneﬁts
Aberdeen Group interviewed CT Media users to ﬁnd out what had motivated
them to move their development efforts to the CT Media platform. The users
represented each of the following CTI market constituencies:
1. Switch vendors developing call center applications;
2. CTI voice processing system manufacturers;
3. CTI hardware and software voice processing distributors;
4. CTI independent software vendors (ISVs).
Aberdeen found that for each of these constituencies, the single most important
driving factor in moving to CT Media was grass-roots customer demand for
standards-based applications, especially S.100 compliance. While this demand
was especially strong on the part of larger, enterprise-class customers, it held
also for smaller installations. These installations require both sophisticated,
best-in-class application functionality and complete customization capability.
According to the users interviewed, customers demand standards compliance
for three reasons. They want:
To choose best-of-breed and new CT applications as these become
available;
Faster development and integration cycles for deploying computer
telephony applications of strategic importance to their businesses;
The lower support costs that they anticipate from S.100 implementations.
Each of the parties interviewed was unanimous in saying that CT Media is the
one available middleware platform today that actually enables them to satisfy
this grass-roots demand for open standards here and now.
Beyond this, Aberdeen has found several independent reasons among the
developers, distributors, and ISVs for favoring a long term investment CT
Media. The most signiﬁcant involved the evolution of existing CT channels.
Channel Advantages Of CT Media
Traditionally, the CT integrator has performed the task of writing applications
to run on proprietary platforms, in addition to assembling and integrating the
hardware. In this model, CT has been more of a craft than a standardized mass
market solution.
The delineation between developers, integrators, and resellers has been unclear,
as the industry has not fully developed. Vertical integration within CT suppliers
has kept development costs for CT solutions high, reﬂecting the labor and time
involved in their implementation.
Open standards allow for applications and hardware to be quickly and easily
integrated. Applications developers spend less time managing hardware details,
and integrators spend less time writing software to make a particular
conﬁguration work. CT products can be stocked and sold in a broader channel,
requiring less support to work properly. This clariﬁes the distinction between
applications developers, systems integrators, distributors and resellers.
Open standards also provide market incentives for each type of CT business.
Application developers encounter a larger market and can focus on what they
do best — delivering specialized applications to niche markets. This contrasts
to the existing CT model in which they devote valuable time and resources
managing time slots on a particular vendor’s hardware. If they want their
application to work on other hardware platforms, they must rewrite their code
to meet the speciﬁc characteristics of a different set of hardware.
Distributors can sell higher volumes of open standard products, with lower
support costs. Interoperability between hardware and software reduces the
amount of time integrators spend resolving conﬂicts and ﬁxing bugs.
Integrators and distributors can support a higher volume of CT sales with a
given head count, improving their overall proﬁtability and their

competitiveness with alternative technologies. One CT distributor told
Aberdeen:
[CT Media] is all about channels and development costs. If I can stock a ﬁnite
combination of hardware and software — that works with a variety of
applications, then I can sell it over and over again. And, I can support it with
fewer people. This is about my long term proﬁtability and industry
survivability.
However, the largest beneﬁciary of open standards is the corporate user
organization who knows that standardized solutions offer faster time-to-market
at lower costs than vertically integrated solutions. They have experienced the
difﬁculty of getting proprietary CT platforms to work with one another. Today,
they specify open standards CT solutions.
Interviews with CT integrators, developers and distributors show that CT
Media is the only way for them to get the beneﬁts of open standards CT today.
Because CT Media beneﬁts suppliers and their customers alike, it creates a
multiplier effect in the computer telephony market as a whole. CT Media is a
catalyst that facilitates the interaction between computer telephony suppliers
and their customers.
Vision/Market Strategy
Dialogic has invested in open CT standards, because it believes that standards
are the catalyst by which the CT industry will transition to a much broader
marketplace. Aberdeen agrees with this perspective and has veriﬁed it in the
marketplace.
This is a vision that Dialogic has consistently expressed, whether through its
involvement in the ECTF or in the broad range of training programs they offer.
Aberdeen believes that this is the only long-term strategy in computer
telephony.
Conclusion
CT Media is a development platform focused squarely on the business models
of computer telephony distributors, application developers, and end users. By
capitalizing and elaborating on the beneﬁts of open-standards CT development,
CT Media generates the impetus needed to move computer telephony to a much
broader market.
Aberdeen ﬁnds that integrators, developers, and large user organizations require
standards-based solutions. As organizations grow and change, they need to be
able to pick and choose from a set of scalable CT applications. Standards are a
means to this end.
The CT Media resource management framework supports multiple standard
APIs, including TAPI and S.100, and it is open to support future standard APIs.
It makes possible the coexistence of S.100, TAPI and other applications,
providing investment protection. Many so-called standards-based CT platforms
may support aspects of open standards CT, but they are not frameworks
designed to facilitate the integration of CT servers.
The long-term viability of any standard hinges upon the rapid deployment of
standards-based development platforms. This applies for both hardware and
software. Companies interested in incorporating TAPI, S.100, and other ECTF
standards need to begin their migration today. Aberdeen believes that CT Media
is today’s best choice for developing open telecommunications servers.
 
 
 
 
 
 
AberdeenGroup,
Inc.
One Boston Place
Boston,
Massachusetts
02108 USA
Tel: 617.723.7890
Fax: 617.723.7897
Contact Information:
For further information on AberdeenGroup's
products and services please contact us at
info@aberdeen.com
This Document is for Electronic Distribution
Only

-- REPRODUCTION PROHIBITED --
Copyright 1997 Aberdeen Group, Inc., Boston, Massachusetts
The trademarks and registered trademarks of the corporations mentioned in this publication are
the property of their respective holders. Unless otherwise noted, the entire contents of this
publication are copyrighted by Aberdeen Group, Inc. and may not be reproduced, stored in a
retrieval system, or transmitted in any form or by any means without prior written consent of
the publisher.


---

## Frictionless Data Package Metadata Appendix

*Appended by archival pipeline — not part of original document*

### Study Record

| Field | Value |
|-------|-------|
| study_id | 1997-dialogic-ct-media-sets-the-pace-for-440d5e |
| title | Dialogic® CT Media™ Sets The Pace For Open-Standards Computer Telephony Development |
| author | Aberdeen Group |
| date | September 1997 |
| type | Vendor Profile |
| subject_domain | Computer Telephony / Telecommunications Software |
| license | CC-BY-4.0 |
| source_url | https://web.archive.org/web/19971007155702/http://www.aberdeen.com:80/secure/profiles/1997/dialogic/body.htm |

### Abstract

Aberdeen Group evaluated the computer telephony (CT) development platform landscape in 1997 and concluded that Dialogic's CT Media was the sole open-standards framework for CT application development and deployment available at the time. The study analyzes CT Media's S.100-compliant resource management architecture, its competitive advantages over proprietary platforms, and argues that open-standards CT (TAPI, S.100, ECTF H.100) would catalyze a broader CT market.

### Document Assessment

| Dimension | Score (1-5) | Rationale |
|-----------|-------------|-----------|
| Importance | 3 | Captures a pivotal moment in CT's transition from proprietary craft to open-standards middleware, documenting market dynamics that presaged the VoIP revolution. |
| Relevance | 3 | Directly relevant to understanding how open-standards strategies disrupt proprietary technology markets; foreshadows API-economy model for telecom. |
| Prescience | 3 | Correctly predicted open-standards would win; Dialogic's $780M Intel acquisition validated commercial assessment. ECTF-specific standards were superseded by VoIP/SIP but the architectural principle was sound. |

### Prescience Detail

Aberdeen's central prediction — that open-standards CT would prevail over proprietary frameworks — proved correct, though the specific standards differed from those Aberdeen championed. ECTF S.100 and H.100 were eventually superseded by VoIP/SIP standards (H.323, SIP, MGCP), but the open-platform, multi-vendor interoperability principle Aberdeen advocated became the industry's organizing model. Dialogic's acquisition by Intel for approximately $780 million in 1999 validated Aberdeen's assessment of CT infrastructure commercial value. CT Media as a specific product was superseded, but Dialogic survived multiple ownership changes (Intel 1999→2013, private equity 2013) and the Dialogic brand continues today. Aberdeen's prediction that Brooktrout would deliver S.100 support (1998) was partially fulfilled before Brooktrout's acquisition path led it ultimately back to Dialogic Group in 2007. Aberdeen's characterization of CT Media as "today's best choice" was defensible but the longer-term prediction of CT Media as de facto standard proved overstated — the market leapfrogged ECTF entirely in favor of VoIP.

### Entities Referenced

| entity_id | entity_name | type | status | successor |
|-----------|-------------|------|--------|-----------|
| ENT-S1-001 | Dialogic Corporation | Vendor | Acquired | Intel (1999); Dialogic Group (2013) |
| ENT-S1-002 | Aberdeen Group | Research Firm | Acquired | Harte-Hanks/Informa |
| ENT-S1-003 | Brooktrout Technologies | Vendor | Acquired | Cantata Technology → Dialogic Group |
| ENT-S1-004 | Natural MicroSystems | Vendor | Acquired | Comverse Technology |
| ENT-S1-005 | Mitel Networks | Vendor | Active (changed owners) | Enghouse Systems (2022) |
| ENT-S1-006 | Rhetorex Inc. | Vendor | Defunct | Absorbed into CT market |
| ENT-S1-007 | ECTF | Standards Body | Defunct | N/A |

### Technologies Referenced

| tech_id | tech_name | era | lifecycle_at_study | lifecycle_current |
|---------|-----------|-----|--------------------|-------------------|
| TECH-S1-001 | CT Media | 1997 | Emerging | Obsolete |
| TECH-S1-002 | ECTF S.100 | 1995–1997 | Emerging | Obsolete |
| TECH-S1-003 | TAPI | 1993–1997 | Growth | Legacy |
| TECH-S1-004 | ECTF H.100 | 1996–1997 | Emerging | Obsolete |
| TECH-S1-005 | SC Bus | 1990s | Mature | Obsolete |
| TECH-S1-006 | MVIP | 1990s | Mature | Obsolete |
| TECH-S1-007 | TSAPI | 1993–1997 | Growth | Legacy |
| TECH-S1-008 | Brooktrout BOSTON | 1997 | Emerging | Abandoned |
| TECH-S1-009 | ECTF S.300/S.400 | 1997 (proposed) | Proposed | Never adopted |

### Observation Summary

25 observations recorded: 3 market-data, 6 technology-assessment, 1 benchmark-result, 3 framework-factor, 1 expert-opinion, 2 strategy-classification, 4 viability-prediction, 5 actual-outcome.

**Key Predictions and Outcomes:**

1. *CT Media as de facto open CT platform* → Partially correct. CT Media led briefly but was superseded by VoIP/SIP. However, open-platform principle prevailed.
2. *ECTF S.100 adoption* → Incorrect. S.100 was never widely adopted; VoIP architecture replaced the framework.
3. *Open standards CT market growth* → Correct. The CT/telecom software market expanded dramatically via open standards (through VoIP).
4. *Brooktrout BOSTON S.100 by 1998* → Partially fulfilled; company acquired before full realization.
