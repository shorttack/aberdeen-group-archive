**==> picture [441 x 108] intentionally omitted <==**

Information Technology Research 

**==> picture [68 x 9] intentionally omitted <==**

**----- Start of picture text -----**<br>
December 7, 2005<br>**----- End of picture text -----**<br>


## **The ESB in the Land of SOA** 

## **Key Facts** 

As businesses warm up to service-oriented architectures (SOA), the enterprise service bus (ESB) is emerging as a de-facto technology standard for integrating the SOA infrastructure. In fact, our current survey of 286 companies, “How SOA is Changing IT,” indicates that 60% of respondents from large companies are either using shared messaging services or planning to implement them within 12 months. Although an ESB is a critical enabler of application integration and Web services messaging, it must do more in an SOA. What does the ESB vendor landscape look like? 

## **Decision Framework** 

## **SOA Ups the Ante on the ESB** 

The ESB is a set of middleware that has been used traditionally to facilitate and accelerate enterprise integration. At its core, the ESB functions as a shared messaging and integration layer that makes the various applications and services available to each other. But the advent of SOA ups the ante on conventional ESB capabilities. SOA “purists” (such as Cape Clear) feel strongly that a true ESB religiously adheres to the WS-* stack as the underlying technology and that products that simply wrap proprietary legacy middleware do not provide the same characteristics or benefits. But the marketplace is peppered with different flavors of ESB . Aberdeen _Group_ believes there are three build-out phases of ESB evolution (Figure 1), each with a specific capability focus: messaging, orchestration, and mediation. 

**Figure 1: Enterprise Bus Evolution** 

**==> picture [389 x 183] intentionally omitted <==**

**----- Start of picture text -----**<br>
Evolution of Enterprise Bus Technology<br>Mediation • Complex manipulations<br>Process Bus • Long process execution<br>Orchestration • Composite application enablement<br>Service Bus • Event processing & messaging<br>Messaging • Data transformation<br>Message Bus • Reliable routing<br>Source: Aberdeen Group , November 2005<br>**----- End of picture text -----**<br>


**Announcement** 

To read more of Aberdeen’s Technology research, click here. 

The ESB in the Land of SOA Page 2 

_Enterprise Strategies_ 

Figure 1 depicts this evolution. While enterprise integration is a common end-goal to the three phases, the first wave of ESBs provided reliable messaging in the form of an “enterprise messaging bus,” with a focus on data transformation and routing. 

The second wave of ESB capabilities (where most of the market is today) has focused on services orchestration, hence enabling the development of composite applications and eventbased processing, based on real-time message content analysis. 

The third and most advanced stage encompasses the capabilities from the first two phases, but introduces a focus on manipulation of the increasing variety and quantity of information passing through the bus, a result of the decomposition requirements of SOA: applications data, applications logic, web services, XML-based messages, business process models, business rules, policies and external data sources. 

Although the gap between the orchestration and mediation levels is small (some customers see it as one), the gap between messaging and orchestration is a bigger one to cross. 

An enterprise bus that absorbs process-related functionality is able to solve increasingly complex integration challenges, therefore offering higher business-added value. The ESB of the future is morphing into a full-fledged universal exchange for enterprise data, applications, services, and process integration. In essence, it becomes a central intelligence system that benefits any IT resources that interact with it. 

## **ESB Closely Follows Services Availability** 

A recent Aberdeen survey of 286 firms, “How SOA is Changing IT” revealed that 76% have either implemented Web services calls to existing applications or plan to do so within 12 months, and 73% are implementing other applications-related services. In addition, 60% of respondents are implementing or plan to implement shared messaging services in the form of a bus or registry of services. These closely related adoption levels are linked to the interdependence between the availability of services and the need for an ESB. As companies increase the quantity of services they offer, the demands for more comprehensive ESBs will increase commensurably, including the governance and management aspects of an SOA infrastructure. Table 1 outlines the usage patterns of key SOA technologies: 

## **Table 1: SOA Technologies in Use or Planned** 

||**Currently Use or Plan to Use**<br>**Within 12 Months**|
|---|---|
|**Web Services Calls to Existing Applications**|76%|
|**Applications-Related Services**|73%|
|**Business Process/Workflow Services**|69%|
|**XML Gateways/Adapters**|65%|
|**Shared Messaging Services (Registry or Bus)**|60%|
|**Governance/Management of Services**|58%|
|**Composite Applications**|49%|



Source: Aberdeen _Group_ , November 2005 

_© 2005_ **Aberdeen** _**Group** , Inc. 260 Franklin Street Boston, Massachusetts 02110-3112_ 

_Telephone: 617 723 7890 Fax: 617 723 7897 www.aberdeen.com_ 

The ESB in the Land of SOA Page 3 

_Enterprise Strategies_ 

Adopting SOA is about choosing a methodology rather than buying a product, but the traditional ESB was a product that performed finite tasks. However, as ESBs absorb more SOA-related constructs, their boundaries will become less palpable and more part of an SOA architectural fabric. In the ESB of the future, business-level definition and integration will trump technically oriented integration because the SOA exposes business services while facilitating their deployment within the enterprise. 

Aberdeen believes the ESB of the future will: 1) interact with or inherit Services Registry characteristics, 2) exhibit capabilities in policy/governance management of the SOA infrastructure, and 3) undoubtedly interact with a more specialized data bus/layer that is more aptly able to a deliver data services that provide various levels of access, aggregation, and semantic mediation of information for various applications or services. 

## **Vendors Are Vying for the Space** 

The vendor landscape can be characterized by four segments: ESB pioneers with varying flavors of SOA, traditional EAI/EII players, applications/integration platforms, and process-centric vendors. Each set attacks the market differently, i.e. from its position of strength. The reality is best seen from an end-user perspective and will require a combination of message, service, and process bus characteristics, coupled with a mix of web services, new services, and legacy services, and complemented by openness in messaging, orchestration, and mediation capabilities. 

Table 2 offers a breakdown of the various characteristics of each segment and what vendors in those segments must do to evolve their positions. 

**Table 2: ESB Functionality Landscape** 

||**Vendor**|**Strengths**|**Issues**|
|---|---|---|---|
|**ESB Pioneers or**<br>**SOA-specific ESB**|* BEA Aqualogic<br>Service Bus<br>* Cape Clear<br>* Cordys<br>* Fiorano<br>* JBoss ESB<br>* IBM WebSphere ESB<br>* Oracle ESB<br>* PolarLake<br>* Software AG<br>* Sonic Software|> Best-of-breed<br>attractiveness for pure<br>SOAs<br>> Quick to market<br>> Faster ROIs due to<br>limited, but well-defined<br>scope|> May require an extra<br>level of integration with<br>existing infrastructure<br>> Some smaller players<br>risk being absorbed by<br>larger players|
|**Traditional EAI/EII**|* IONA (Artix)<br>* Informatica<br>* iWay<br>* FusionWare<br>* Sterling Commerce<br>* SUN (SeeBeyond)<br>* TIBCO<br>* webMethods|> Good entrenchment into<br>IT application infrastructure<br>> Leverages existing<br>resources<br>> Natural progression of<br>capabilities|> Speed and cost of<br>implementations<br>challenged by SOA<br>pioneers<br>> Expansion into registry<br>and process manipulation<br>services are critical for<br>future viability|



_© 2005_ **Aberdeen** _**Group** , Inc. 260 Franklin Street Boston, Massachusetts 02110-3112_ 

_Telephone: 617 723 7890 Fax: 617 723 7897 www.aberdeen.com_ 

The ESB in the Land of SOA Page 4 

## _Enterprise Strategies_ 

||**Vendor**|**Strengths**|**Issues**|
|---|---|---|---|
|**Part of a platform**|* BEA WebLogic<br>* IBM WebSphere<br>Message Broker<br>* JBoss JEMS<br>* Oracle Fusion<br>Middleware<br>* Microsoft BizTalk<br>* SAP NetWeaver|> Good fit for service-<br>oriented business<br>applications development,<br>including composite<br>applications and legacy<br>SOA enablement|> Inherent latency of<br>implementation and cost<br>overhead dependent on<br>monolithic-nature of<br>applications they support|
|**Process-centric**<br>**integration**|* Axway<br>* IBM WebSphere<br>Process Server<br>* JBoss jBPM<br>* Magic<br>* Metastorm<br>* Vitria|> Strong on business<br>process management<br>(BPM) manipulation<br>> High-added value in<br>vertical applications where<br>BP standards exist|> Does not offer the<br>granularity attractiveness<br>of services<br>> Weak on architectural<br>scalability<br>> A marriage of<br>capabilities with SOA<br>pioneers may be<br>powerful|



Source: Aberdeen _Group_ , November 2005 

## **Aberdeen Conclusions** 

Aberdeen points out the following for end users interested in ESBs: 

- Evaluate the extensibility of your existing ESB or EAI platform for SOA-infrastructure readiness; 

- Existing ESBs need to do more than data messaging, transformation, and routing; 

- Services orchestration, mediation, and complex manipulations will be key to an SOA infrastructure; 

- Don’t forget the relationship with a services registry, the policy/governance aspects of services management in the context of an SOA, and a specialized data bus; and 

- Investigate at least one vendor in each of the four vendor segments detailed in this report. 

||**Related Research**|||
|---|---|---|---|
||_The Service-Oriented Architecture in the_<br>_SOA Success Starts with IT_|_Success_<br>_,_||
||_Supply Chain Benchmark Report_<br>_,_<br>November 2005|||
||October 2005<br>_ERP in the Mid-Market Enterprise_<br>_,_|||
||_AmberPoint 5.0 Boosts Automatic SOA_<br>October 2005|||
||_Management Policies_<br>,December 2005|||
||**Author**: William Mougayar, VP & Service Director, Technology Research,|||
||william.mougayar@aberdeen.com<br>,with Rick Saia,Analyst/Editor,rick.saia@aberdeen.com|||



Founded in 1988, **Aberdeen** _**Group**_ is the technology- driven research destination of choice for the global business executive. **Aberdeen** _**Group**_ has over 100,000 research members in over 36 countries around the world that both participate in and direct the most comprehensive technology-driven value chain research in the market. Through its continued fact-based research, benchmarking, and actionable analysis, **Aberdeen** _**Group**_ offers global business and technology executives a unique mix of actionable research, KPIs, tools, and services. 

This document is the result of research performed by **Aberdeen** _**Group**_ . **Aberdeen** _**Group**_ believes its findings are objective and represent the best analysis available at the time of publication.  Unless otherwise noted, the entire contents of this publication are copyrighted by **Aberdeen** _**Group**_ , Inc. and may not be reproduced, stored in a retrieval system, or transmitted in any form or by any means without prior written consent by **Aberdeen** _**Group**_ , Inc. 

