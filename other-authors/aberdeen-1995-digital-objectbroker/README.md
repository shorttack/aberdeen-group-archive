# Study 13: Digital's ObjectBroker — Advanced Integration of Distributed Resources

**Study ID:** `aberdeen-1995-digital-objectbroker`  
**Study Number:** 13  
**Author:** Aberdeen Group  
**Publication Date:** August 1, 1995  
**Study Type:** Product Profile  
**Domain:** Distributed Object Computing  
**Methodology:** Industry Analysis, Competitive Profiling, Field Research  

**Archive URL:** https://web.archive.org/web/19970112012511/http://www.aberdeen.com:80/secure/profiles/objbrk/decobj.htm  
**Archive Snapshot Date:** 1997-01-12  

---

## Abstract

Profile evaluating Digital Equipment Corporation's ObjectBroker, a CORBA-compliant object request broker for integrating distributed heterogeneous resources. Examines ORB technology, legacy system encapsulation, OLE-COM integration, and 19-platform support. Aberdeen characterizes ObjectBroker as a market-leading ORB implementation used primarily by Fortune 1000 enterprises in banking, financial services, and manufacturing to integrate heterogeneous legacy infrastructure.

---

## Study Summary

Aberdeen Group's August 1995 product profile profiles Digital Equipment Corporation's **ObjectBroker 2.5**, an object request broker (ORB) conforming to CORBA 1.2. The study was produced through field research with ObjectBroker customers and covers four main business advantages:

1. **Legacy System Encapsulation** — ObjectBroker wraps legacy procedural systems with CORBA-compliant interfaces via Skeleton Server (APIs) and Script Server (command-line interfaces), making them appear as independent CORBA objects to the outside world.
2. **Multi-Platform Breadth** — ObjectBroker supports 19 hardware/OS combinations, the broadest coverage of any ORB vendor at the time. This allows a single ORB vendor relationship across heterogeneous enterprise infrastructure.
3. **OLE-COM Integration** — Digital bridges the CORBA (Unix server) and OLE/COM (Windows desktop) worlds through the OLE Network Portal and DDE Gateway. Digital and Microsoft were actively collaborating with OMG on OLE-CORBA standards.
4. **Application Partitioning via IML/MML** — Digital's proprietary IDL extensions (Implementation Mapping Language and Method Mapping Language) simplify distributed application development.

### Key Pricing (1995)

| License Type | Price |
|---|---|
| PC Runtime (per seat) | $149 |
| Windows NT Development (per seat) | $980 |
| Unix Development (per seat) | $5,000 |

Runtime priced per-machine based on hardware/OS combination; volume discounts available. Runtime included in Digital's NAS platform (installed on >50% of Digital systems).

### ObjectBroker 2.6 Roadmap (announced August 1995; GA expected early 1996)

- Secure ORB: GSS API for DCE / Kerberos-level security
- OLE Automation: access remote CORBA object data and functionality from OLE clients (e.g. Excel)
- C++ Language Binding: CORBA 2.0 IDL-to-C++ mapping
- Systems Management APIs for non-Digital tools
- "Quick Start" — auto-generate client-server skeleton in 10 minutes from IDL
- Performance improvements
- New platforms: IBM MVS (first ORB to support MVS), OS/400, Windows 95, Silicon Graphics IRIX

### CORBA Compliance

ObjectBroker 2.5 conforms to **CORBA 1.2**. Version 2.6 planned to achieve CORBA 2.0 compliance (inter-ORB communication). CORBA is supported by over 450 companies as of 1995.

---

## Platform Support (19 Combinations)

| # | Platform | OS Family | Arch | Version | Port By |
|---|---|---|---|---|---|
| 1 | Digital UNIX | Unix | Alpha | v2.5 | Digital |
| 2 | ULTRIX | Unix | VAX | v2.5 | Digital |
| 3 | OpenVMS Alpha | VMS | Alpha | v2.5 | Digital |
| 4 | OpenVMS VAX | VMS | VAX | v2.5 | Digital |
| 5 | Windows 3.1 | Windows | x86 | v2.5 | Digital |
| 6 | Windows NT (Intel) | Windows NT | x86 | v2.5 | Digital |
| 7 | Windows NT (Alpha) | Windows NT | Alpha | v2.5 | Digital |
| 8 | HP-UX | Unix | PA-RISC | v2.5 | Digital |
| 9 | AIX | Unix | POWER | v2.5 | Digital |
| 10 | OS/2 | OS/2 | x86 | v2.5 | Digital |
| 11 | SunOS | Unix | SPARC | v2.5 | Digital |
| 12 | Solaris | Unix | SPARC | v2.5 | Digital |
| 13 | Macintosh System 7 | Mac | 68k/PPC | v2.5 | Digital |
| 14 | Tandem Integrity | Integrity | MIPS | v2.5 | Logica N.A. |
| 15 | Tandem NonStop Kernel | NSK | MIPS | v2.5 | Logica N.A. |
| 16 | IBM MVS | Mainframe | S/390 | v2.6 planned | Digital |
| 17 | OS/400 | Midrange | AS/400 | v2.6 planned | Digital |
| 18 | Windows 95 | Windows | x86 | v2.6 planned | Digital |
| 19 | Silicon Graphics IRIX | Unix | MIPS | v2.6 planned | Logica |

---

## Entity Status (as of 2026)

| Entity | Role | Status at Publication | Current Status (2026) |
|---|---|---|---|
| Digital Equipment Corporation | Primary subject | Active | Acquired by Compaq 1998; Compaq by HP 2002 |
| Object Management Group (OMG) | Standards authority | Active | Active |
| Microsoft Corporation | Technology partner | Active | Active |
| Logica North America | Platform port partner | Active | Merged into CGI Group (August 2012) |
| Electronic Data Systems (EDS) | Reseller / integrator | Active | Acquired by HP for $13.9B (August 2008) |
| Protosoft Inc | Tooling partner | Active | Acquired by Platinum Technology (Nov 1995); Platinum acquired by CA (1999) |
| Tandem Computers | Platform partner | Active | Acquired by Compaq 1997; then HP 2002 |
| Aberdeen Group | Author | Active | Active |

**Sources:**  
- Logica/CGI: https://en.wikipedia.org/wiki/Logica  
- EDS/HP: https://www.nytimes.com/2008/05/13/technology/13iht-webhpeds.12839575.html  
- Protosoft/Platinum: https://techmonitor.ai/technology/platinum_gets_acquisition_second_wind_takes_out_softool_protosoft

---

## Technology Lifecycle (as of 2026)

| Technology | Category | Lifecycle Status |
|---|---|---|
| ObjectBroker | Product | Obsolete |
| CORBA | Standard | Legacy |
| IDL | Language | Legacy |
| IML / MML | Language | Obsolete |
| OLE | Standard | Evolved (→ ActiveX → COM+) |
| COM | Architecture | Evolved (→ COM+ / .NET) |
| DDE | Protocol | Obsolete |
| DCE | Standard | Obsolete |
| Visual Basic | Language | Evolved (→ VB.NET) |
| PowerBuilder | Tool | Niche |
| OpenVMS | OS | Active (VSI maintenance) |
| ACA Services | Product | Obsolete |
| ObjectPlus / Paradigm Plus | Tool | Obsolete |
| NAS | Platform | Obsolete |
| GSS-API / Kerberos | Security API | Active |
| C++ | Language | Active |

---

## Data Package Structure

```
aberdeen-1995-digital-objectbroker/
├── datapackage.json          # Frictionless Data Package descriptor
├── README.md                 # This file
├── data/
│   ├── codes.csv             # Reference codes / controlled vocabulary (45 rows)
│   ├── studies.csv           # Study bibliographic metadata (1 row)
│   ├── entities.csv          # Organizations mentioned with status (11 rows)
│   ├── technologies.csv      # Technologies with lifecycle info (19 rows)
│   ├── platforms.csv         # 19 platform combinations (19 rows)
│   └── observations.csv      # Structured observations extracted (50 rows)
├── schema/
│   └── schema_org.json       # Schema.org JSON-LD metadata descriptor
└── scripts/
    └── demo_analysis.py      # Python demonstration analysis script
```

### Table Row Counts

| File | Rows (excl. header) |
|---|---|
| codes.csv | 45 |
| studies.csv | 1 |
| entities.csv | 11 |
| technologies.csv | 19 |
| platforms.csv | 19 |
| observations.csv | 50 |

---

## Foreign Key Relationships

```
studies.study_id
    ← entities.study_id
    ← technologies.study_id
    ← platforms.study_id
    ← observations.study_id

codes.code_id
    ← entities.entity_type  (code_type = entity_type)
    ← entities.status_*     (code_type = entity_status)
    ← technologies.lifecycle_status  (code_type = tech_lifecycle)
    ← observations.obs_code (code_type = observation_category)
    ← platforms.platform_code (code_type = platform)

entities.entity_id
    ← technologies.related_entity_id
    ← platforms.port_by
    ← observations.entity_ref (comma-separated)

technologies.tech_id
    ← observations.tech_ref (comma-separated)
```

---

## Usage Notes

- All CSV files use UTF-8 encoding.
- Date fields use ISO 8601 format (YYYY-MM-DD).
- Numeric values in `observations.csv` use period (`.`) as decimal separator.
- Multi-value FK fields (e.g. `observations.entity_ref`, `observations.tech_ref`, `studies.methodology`) are comma-separated strings; split on `,` to resolve individual references.
- `confidence` in observations: `high` = directly stated in text; `medium` = implied or inferred; `low` = speculative.
- Entity and technology statuses reflect the situation as of **March 2026** (archival date).

---

## Aberdeen Group Contact (as of 1995)

Aberdeen Group  
One Boston Place  
Boston, Massachusetts 02108  
Telephone: 617-723-7890 | FAX: 617-723-7897  

Digital Equipment Corporation — Enterprise Software Group  
110 Spit Brook Road, Nashua, NH 03062-2698  
603-881-2317  
