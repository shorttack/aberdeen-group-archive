# Original Text: Distributed Object Technology: Dead Skunk Or Live Wire

**Source:** Aberdeen Group Technology Viewpoint, Volume 10/Number 16, 1997  
**Wayback Machine URL:** https://web.archive.org/web/19980131061426/http://www.aberdeen.com:80/research/abstract/97080139.htm

---

 
Abstract: Technology Viewpoint
Volume 10/Number 16
Distributed Object Technology: Dead Skunk Or
Live Wire
Distributed object technology (DOT) middleware is at one and
the same time today's biggest example of oversold hype -- and
a key part of tomorrow's bottom-line new-technology benefits.
IS buyers need middleware that supports a myriad of
applications, platforms and hardware requirements. In
particular, IS needs to rapidly build flexible, distributed
(especially Internet) competitive-advantage applications. The
best way to do this is by using distributed objects, modular
pieces of code and data that move anywhere easily. However,
distributed object technology has significant barriers to
overcome in order to benefit an enterprise architecture -- the
products are often immature, unintegrated, or low
performance; standards are limited or the subject of fierce
debate; and the industry has not clearly made a business case
for the technology.
This Technology Viewpoint discusses the business benefits and
barriers to using distributed object technology -- and suggests
an IS plan to implement DOT effectively for real long-term
benefits in using this live-wire technology.
Jeanine Fournier
 Contact Aberdeen
The Wayback Machine - https://web.archive.org/web/19980131061426/http://www.aberdeen.com:80/research/abstract/97080139.htm

---

## Frictionless Data Package Metadata Appendix

### Study Record

| Field | Value |
|-------|-------|
| study_id | 1997-distributed-object-technology--dead-3cf2d1 |
| title | Distributed Object Technology: Dead Skunk Or Live Wire |
| author | Jeanine Fournier |
| date | 1997-08-01 |
| type | Technology Viewpoint |
| subject_domain | Middleware / Distributed Computing |
| source_file | 1997 Distributed Object Technology_ Dead Skunk Or Live Wire tvp.pdf |
| license | CC-BY-4.0 |

### Abstract

Aberdeen Group Technology Viewpoint (Volume 10/Number 16) examining distributed object technology (DOT) middleware. Argues that DOT is simultaneously over-hyped and strategically essential. Identifies barriers including product immaturity, integration gaps, low performance, standards conflicts (CORBA vs DCOM), and lack of a clear business case. Recommends that IS organizations adopt DOT pragmatically for competitive-advantage Internet applications while standards mature.

### Document Assessment

| Dimension | Score (1-5) | Rationale |
|-----------|-------------|-----------|
| Importance | 3 | Brief abstract/viewpoint piece with limited original data, but representative of Aberdeen's technology-assessment practice and captures the CORBA/DCOM standards war accurately. |
| Relevance | 3 | Relevant to historians of enterprise middleware and the 1990s distributed computing era; limited direct applicability to modern practitioners given the complete resolution of the CORBA/DCOM era. |
| Prescience | 5 | Aberdeen's characterization proved highly prescient: DOT did eventually deliver enterprise value but not through CORBA or DCOM — those were superseded by web services (SOAP/REST) and later microservices, exactly the pattern of 'live wire technology requiring patience' the report described. |

### Prescience Detail

The report's central thesis — that distributed object technology was simultaneously over-hyped *and* genuinely valuable — proved remarkably accurate. Aberdeen's framing of DOT as a "live wire" requiring patience was vindicated by history:

1. **CORBA's fate:** CORBA rose to prominence in the mid-to-late 1990s, then declined to niche status by the mid-2000s due to complexity, inter-vendor incompatibility, and high licensing costs. Microsoft eventually dropped DCOM after failed attempts to scale it. Both technologies were superseded by SOAP web services and later REST APIs — a trajectory Aberdeen implicitly anticipated by noting immature standards and fierce debate. (Source: [ACM Queue, "The Rise and Fall of CORBA," 2006](https://queue.acm.org/detail.cfm?id=1142044))

2. **Internet as the killer app:** The report's identification of Internet competitive-advantage applications as the key DOT use case was exactly correct. The Internet did become the dominant distributed computing environment, though via HTTP and REST rather than CORBA or DCOM. (Source: [Wikipedia, CORBA](https://en.wikipedia.org/wiki/Common_Object_Request_Broker_Architecture))

3. **Modular distributed computing won:** The conceptual framework of "modular pieces of code and data that move anywhere easily" is precisely what microservices and containerized architectures (Docker, Kubernetes) delivered two decades later.

**Assessment:** Prescience score 5/5. Aberdeen identified the right technology trajectory, the right use case, and the right barriers — even if the specific standards it was evaluating were superseded.

### Entities

| entity_id | entity_name | entity_type | status | successor |
|-----------|-------------|-------------|--------|-----------|
| ENT-DOT-001 | Aberdeen Group | Research Firm | Acquired | Harte-Hanks (2001) |
| ENT-DOT-002 | Object Management Group (OMG) | Standards Body | Active | — |
| ENT-DOT-003 | Microsoft Corporation | Technology Vendor | Active | — |
| ENT-DOT-004 | Sun Microsystems | Technology Vendor | Acquired | Oracle Corporation (2010) |
| ENT-DOT-005 | Hewlett-Packard (HP) | Technology Vendor | Active (split) | HP Inc. and HPE (2015) |

### Technologies

| tech_id | tech_name | lifecycle_at_study | lifecycle_current |
|---------|-----------|-------------------|------------------|
| TECH-DOT-001 | Distributed Object Technology (DOT) | Emerging/Hyped | Superseded |
| TECH-DOT-002 | CORBA | Emerging | Niche/Legacy |
| TECH-DOT-003 | DCOM | Emerging | Superseded |
| TECH-DOT-004 | Object Request Broker (ORB) | Emerging | Legacy |
| TECH-DOT-005 | Internet/Intranet Applications | Emerging | Mature/Dominant |

### Observation Summary

15 observations recorded: 3 technology-assessment, 2 framework-factor, 4 viability-prediction/actual-outcome pairs, 3 expert-opinion, 1 market-data. Confidence: high for technology characterizations corroborated by historical record; medium for predictions that required contextual interpretation.
