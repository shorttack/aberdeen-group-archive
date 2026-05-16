# The ESB in the Land of SOA

> Archived from: source/_raw_text.txt
> Original publication date: 2005-12-07
> Author: William Mougayar

---

## Original Document Text

Information Technology Research                                                                    December 7, 2005


                                  The ESB in the Land of SOA
               Key Facts
 As businesses warm up to service-oriented architectures (SOA), the enterprise service bus (ESB)
 is emerging as a de-facto technology standard for integrating the SOA infrastructure. In fact, our
 current survey of 286 companies, “How SOA is Changing IT,” indicates that 60% of respondents
 from large companies are either using shared messaging services or planning to implement them
 within 12 months. Although an ESB is a critical enabler of application integration and Web
 services messaging, it must do more in an SOA. What does the ESB vendor landscape look like?


        Decision Framework
 SOA Ups the Ante on the ESB
 The ESB is a set of middleware that has been used traditionally to facilitate and accelerate
 enterprise integration. At its core, the ESB functions as a shared messaging and integration layer
 that makes the various applications and services available to each other. But the advent of SOA
 ups the ante on conventional ESB capabilities. SOA “purists” (such as Cape Clear) feel strongly
 that a true ESB religiously adheres to the WS-* stack as the underlying technology and that
 products that simply wrap proprietary legacy middleware do not provide the same characteristics
 or benefits. But the marketplace is peppered with different flavors of ESB. AberdeenGroup
 believes there are three build-out phases of ESB evolution (Figure 1), each with a specific
 capability focus: messaging, orchestration, and mediation.
 Figure 1: Enterprise Bus Evolution

                          Evolution of Enterprise Bus Technology

                                   Mediation                                 • Complex manipulations
                                                   Process Bus               • Long process execution




                   Orchestration                              • Composite application enablement
                                         Service Bus          • Event processing & messaging




             Messaging                             • Data transformation
                                  Message Bus      • Reliable routing


                                                                           Source:AberdeenGroup, November 2005




        Announcement               To read more of Aberdeen’s Technology research, click here.
                                                                            The ESB in the Land of SOA
Enterprise Strategies                                                                            Page 2



 Figure 1 depicts this evolution. While enterprise integration is a common end-goal to the three
 phases, the first wave of ESBs provided reliable messaging in the form of an “enterprise
 messaging bus,” with a focus on data transformation and routing.
 The second wave of ESB capabilities (where most of the market is today) has focused on
 services orchestration, hence enabling the development of composite applications and event-
 based processing, based on real-time message content analysis.
 The third and most advanced stage encompasses the capabilities from the first two phases, but
 introduces a focus on manipulation of the increasing variety and quantity of information passing
 through the bus, a result of the decomposition requirements of SOA: applications data,
 applications logic, web services, XML-based messages, business process models, business rules,
 policies and external data sources.
 Although the gap between the orchestration and mediation levels is small (some customers see it
 as one), the gap between messaging and orchestration is a bigger one to cross.
 An enterprise bus that absorbs process-related functionality is able to solve increasingly complex
 integration challenges, therefore offering higher business-added value. The ESB of the future is
 morphing into a full-fledged universal exchange for enterprise data, applications, services, and
 process integration. In essence, it becomes a central intelligence system that benefits any IT
 resources that interact with it.
 ESB Closely Follows Services Availability
 A recent Aberdeen survey of 286 firms, “How SOA is Changing IT” revealed that 76% have
 either implemented Web services calls to existing applications or plan to do so within 12 months,
 and 73% are implementing other applications-related services. In addition, 60% of respondents
 are implementing or plan to implement shared messaging services in the form of a bus or registry
 of services. These closely related adoption levels are linked to the interdependence between the
 availability of services and the need for an ESB. As companies increase the quantity of services
 they offer, the demands for more comprehensive ESBs will increase commensurably, including
 the governance and management aspects of an SOA infrastructure. Table 1 outlines the usage
 patterns of key SOA technologies:
 Table 1: SOA Technologies in Use or Planned

                                                               Currently Use or Plan to Use
                                                                    Within 12 Months
  Web Services Calls to Existing Applications                              76%
  Applications-Related Services                                            73%
  Business Process/Workflow Services                                       69%
  XML Gateways/Adapters                                                    65%
  Shared Messaging Services (Registry or Bus)                              60%
  Governance/Management of Services                                        58%
  Composite Applications                                                   49%
                                                                  Source: AberdeenGroup, November 2005




© 2005 AberdeenGroup, Inc.                                                       Telephone: 617 723 7890
260 Franklin Street                                                                    Fax: 617 723 7897
Boston, Massachusetts 02110-3112                                                      www.aberdeen.com
                                                                                  The ESB in the Land of SOA
Enterprise Strategies                                                                                    Page 3



 Adopting SOA is about choosing a methodology rather than buying a product, but the traditional
 ESB was a product that performed finite tasks. However, as ESBs absorb more SOA-related
 constructs, their boundaries will become less palpable and more part of an SOA architectural
 fabric. In the ESB of the future, business-level definition and integration will trump technically
 oriented integration because the SOA exposes business services while facilitating their
 deployment within the enterprise.
 Aberdeen believes the ESB of the future will: 1) interact with or inherit Services Registry
 characteristics, 2) exhibit capabilities in policy/governance management of the SOA
 infrastructure, and 3) undoubtedly interact with a more specialized data bus/layer that is more
 aptly able to a deliver data services that provide various levels of access, aggregation, and
 semantic mediation of information for various applications or services.
 Vendors Are Vying for the Space
 The vendor landscape can be characterized by four segments: ESB pioneers with varying flavors
 of SOA, traditional EAI/EII players, applications/integration platforms, and process-centric
 vendors. Each set attacks the market differently, i.e. from its position of strength. The reality is
 best seen from an end-user perspective and will require a combination of message, service, and
 process bus characteristics, coupled with a mix of web services, new services, and legacy
 services, and complemented by openness in messaging, orchestration, and mediation capabilities.
 Table 2 offers a breakdown of the various characteristics of each segment and what vendors in
 those segments must do to evolve their positions.
 Table 2: ESB Functionality Landscape
                            Vendor                Strengths                       Issues
   ESB Pioneers or         * BEA Aqualogic       > Best-of-breed                 > May require an extra
   SOA-specific ESB        Service Bus           attractiveness for pure         level of integration with
                           * Cape Clear          SOAs                            existing infrastructure
                           * Cordys
                                                 > Quick to market               > Some smaller players
                           * Fiorano
                                                                                 risk being absorbed by
                           * JBoss ESB           > Faster ROIs due to
                                                                                 larger players
                           * IBM WebSphere ESB   limited, but well-defined
                           * Oracle ESB          scope
                           * PolarLake
                           * Software AG
                           * Sonic Software


   Traditional EAI/EII     * IONA (Artix)        > Good entrenchment into        > Speed and cost of
                           * Informatica         IT application infrastructure   implementations
                           * iWay                                                challenged by SOA
                                                 > Leverages existing
                           * FusionWare                                          pioneers
                                                 resources
                           * Sterling Commerce
                                                                                 > Expansion into registry
                           * SUN (SeeBeyond)     > Natural progression of
                                                                                 and process manipulation
                           * TIBCO               capabilities
                                                                                 services are critical for
                           * webMethods
                                                                                 future viability




© 2005 AberdeenGroup, Inc.                                                            Telephone: 617 723 7890
260 Franklin Street                                                                         Fax: 617 723 7897
Boston, Massachusetts 02110-3112                                                           www.aberdeen.com
                                                                                                         The ESB in the Land of SOA
Enterprise Strategies                                                                                                             Page 4




                                     Vendor                         Strengths                            Issues
    Part of a platform             * BEA WebLogic                 > Good fit for service-              > Inherent latency of
                                   * IBM WebSphere                oriented business                    implementation and cost
                                   Message Broker                 applications development,            overhead dependent on
                                                                  including composite                  monolithic-nature of
                                   * JBoss JEMS                   applications and legacy              applications they support
                                   * Oracle Fusion                SOA enablement
                                   Middleware
                                   * Microsoft BizTalk
                                   * SAP NetWeaver


    Process-centric                * Axway                        > Strong on business                 > Does not offer the
                                   * IBM WebSphere                process management                   granularity attractiveness
    integration
                                   Process Server                 (BPM) manipulation                   of services
                                   * JBoss jBPM                   > High-added value in                > Weak on architectural
                                   * Magic                        vertical applications where          scalability
                                   * Metastorm                    BP standards exist                   > A marriage of
                                   * Vitria                                                            capabilities with SOA
                                                                                                       pioneers may be
                                                                                                       powerful
                                                                                            Source: AberdeenGroup, November 2005

 Aberdeen Conclusions
 Aberdeen points out the following for end users interested in ESBs:
     •     Evaluate the extensibility of your existing ESB or EAI platform for SOA-infrastructure
           readiness;
     •     Existing ESBs need to do more than data messaging, transformation, and routing;
     •     Services orchestration, mediation, and complex manipulations will be key to an SOA
           infrastructure;
     •     Don’t forget the relationship with a services registry, the policy/governance aspects of
           services management in the context of an SOA, and a specialized data bus; and
     •     Investigate at least one vendor in each of the four vendor segments detailed in this report.

                                                        Related Research
    The Service-Oriented Architecture in the                            SOA Success Starts with IT Success,
    Supply Chain Benchmark Report,                                      November 2005
    October 2005
                                                                       ERP in the Mid-Market Enterprise,
    AmberPoint 5.0 Boosts Automatic SOA                                October 2005
    Management Policies, December 2005
     Author: William Mougayar, VP & Service Director, Technology Research,
     william.mougayar@aberdeen.com, with Rick Saia, Analyst/Editor, rick.saia@aberdeen.com

Founded in 1988, AberdeenGroup is the technology- driven research destination of choice for the global business executive.
AberdeenGroup has over 100,000 research members in over 36 countries around the world that both participate in and direct the most
comprehensive technology-driven value chain research in the market. Through its continued fact-based research, benchmarking, and
actionable analysis, AberdeenGroup offers global business and technology executives a unique mix of actionable research, KPIs, tools,
and services.
This document is the result of research performed by AberdeenGroup. AberdeenGroup believes its findings are objective and represent
the best analysis available at the time of publication. Unless otherwise noted, the entire contents of this publication are copyrighted by
AberdeenGroup, Inc. and may not be reproduced, stored in a retrieval system, or transmitted in any form or by any means without prior
written consent by AberdeenGroup, Inc.


---

## Frictionless Data Package Metadata

> Auto-generated by Archival Ingest Skill v16

### Study Record

| Field | Value |
|-------|-------|
| study_id | esb-in-soa-e002b7 |
| title | The ESB in the Land of SOA |
| author | William Mougayar |
| date | 2005-12-07 |
| type | employer-record |
| subject_domain | ESB; SOA integration; enterprise middleware; vendor landscape |
| methodology | Aberdeen survey-based research note; survey of 286 companies 'How SOA is Changing IT'; vendor landscape analysis |
| source_file | source/_raw_text.txt |
| license | CC-BY-4.0 |

### Abstract

Aberdeen research note (5 pages) on the emergence of ESB as de-facto technology standard for integrating SOA infrastructure. Based on survey of 286 companies ('How SOA is Changing IT'): 60% of large company respondents are using or planning shared messaging services within 12 months; 76% implementing Web Services calls to existing applications; 73% implementing applications-related services. Kastner's three-phase ESB evolution framework: Message Bus (messaging) → Service Bus (orchestration) → Process Bus (mediation). Four-segment vendor landscape: ESB pioneers/SOA-specific, traditional EAI/EII players, platform vendors, process-centric integrators. Aberdeen conclusions: evaluate ESB extensibility; existing ESBs need to go beyond messaging to orchestration and mediation; don't neglect services registry and governance.

### Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | high | Rich primary survey data from 286 companies with multiple adoption metrics; comprehensive ESB vendor landscape (20+ named vendors); Aberdeen's three-phase evolution framework; foundational SOA-era ESB analysis with quantified findings. |
| **Relevance** | high | Central to understanding SOA middleware adoption patterns; named-vendor landscape still historically significant; survey data benchmarks enterprise SOA technology adoption in 2005. |
| **Prescience** | high | ESB evolution framework was accurate; the convergence toward service/process bus proved correct; governance/registry integration became standard. However, many ESB vendors were absorbed or became legacy as cloud-native API management and microservices emerged. The 'SOA purist WS-* vs. proprietary wrapper' tension was real but resolved differently than implied. |

### Prescience Detail

This study did not make forward-looking claims.

### Entities Referenced (29)

| Entity | Type | Status | Successor |
|--------|------|--------|-----------|
| William Mougayar | person | active |  |
| Rick Saia | person | unknown |  |
| Peter S. Kastner | person | active |  |
| Aberdeen Group | firm | acquired | Harte-Hanks (Sep 2006) -> Halyard Capital (Apr 2015) -> Spiceworks Ziff Davis (Dec 2020) |
| Cape Clear Software | company | acquired | workday |
| BEA Systems | company | acquired | Oracle Corporation (January 2008) |
| IBM | company | active |  |
| Oracle | company | active |  |
| Software AG | company | active |  |
| TIBCO Software | company | active |  |
| webMethods | company | acquired | software-ag |
| IONA Technologies (Artix) | company | acquired | progress-software |
| Informatica | company | active |  |
| Sterling Commerce | company | acquired | at&t-then-sap |
| Sun Microsystems (SeeBeyond) | company | acquired | oracle |
| SAP | company | active |  |
| Microsoft | company | active |  |
| JBoss (Red Hat) | company | acquired | red-hat |
| Cordys | company | acquired | opentext |
| Fiorano Software | company | active |  |
| PolarLake | company | acquired |  |
| Sonic Software | company | acquired | progress-software |
| iWay Software | company | active |  |
| FusionWare | company | acquired | C9 Capital (February 2021) |
| Axway | company | active |  |
| Magic Software Enterprises | company | active |  |
| Metastorm | company | acquired | opentext |
| Vitria Technology | company | active |  |
| AmberPoint | company | acquired | oracle |

### Technologies Referenced (17)

| Technology | Category | Vendor | Lifecycle (at study) | Lifecycle (current) |
|------------|----------|--------|---------------------|---------------------|
| Enterprise Service Bus (ESB) | integration-middleware | multi-vendor | growth | legacy |
| Service-Oriented Architecture (SOA) | architecture-framework | industry-standard | growth | evolved |
| Web Services (XML/SOAP/WSDL/UDDI) | integration-protocol | industry-standard | growth | mature |
| WS-* Standards Stack | integration-protocol | industry-standard | growth | evolved |
| Message-Oriented Middleware (MOM) / Enterprise Messaging | integration-middleware | multi-vendor | mature | evolved |
| Services Orchestration | integration-middleware | multi-vendor | growth | evolved |
| Business Process Management (BPM) / Process Bus | process-management | multi-vendor | emerging | mature |
| Composite Applications | application-architecture | multi-vendor | emerging | evolved |
| SOA Services Registry / UDDI | soa-governance | multi-vendor | emerging | legacy |
| XML Gateways / Adapters | integration-middleware | multi-vendor | growth | evolved |
| BEA AquaLogic Service Bus | integration-middleware | BEA Systems | emerging | legacy |
| IBM WebSphere ESB | integration-middleware | IBM | growth | legacy |
| SAP NetWeaver | integration-platform | SAP | growth | evolved |
| Microsoft BizTalk Server | integration-platform | Microsoft | mature | active |
| Enterprise Application Integration (EAI) | integration-methodology | multi-vendor | mature | evolved |
| Business Process / Workflow Services | process-management | multi-vendor | growth | mature |
| SOA Governance / Management of Services | soa-governance | multi-vendor | emerging | mature |

### Observation Summary

- Total observations: 16
- By type: survey-finding: 8, technical-claim: 3, competitive-analysis: 3, prediction: 1, strategic-recommendation: 1
