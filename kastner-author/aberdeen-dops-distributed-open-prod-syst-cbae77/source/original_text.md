# Aberdeen Group — Distributed Open Production Systems: The Next Generation Begins (1993)

> Archived from: DOPS-1993-distributed-systems-10.pdf
> Original publication date: 1993-06-01
> Author: Peter S. Kastner — Vice-President, Aberdeen Group, Inc.

---

## Original Document Text

     11 1C2 Tr n ITAH ( ItiA ft
           III IMUlvUj V|Jvl     11
                         A«
         liiAiiAn CiiAi/tnA
   riOCI1U CltOiTvySlwIIIS.
The Next Generation Ibegins

          Peter S. Kastner
           Vice-President

          Aberdeen Group, Inc.
             92 State Street
            Boston, MA 02109
             (617) 723-7890
                                                                      Downsizing
Definition:
 Migrating computer-based functions from the
 central mainframe to dispersed computing systems


 Operational:

  Moving the MIS function down the organization

 Blending enterprise operational
 experience with MIS adventuresome

  Capturing the advantages of the
  computer technologies of the 1990s

                                                                                                                                 Aberdeen Group
______________________________________________________________________________________________________________________________
  Spoke-Node-Ring Planning Model
                      Data Collection
                      Nodes
Corporate                               Productivity
Data Node




MM                 Spoke
Node

    Middle \
     Manager
            Ring
                                          Aberdeen Group
          Future Systems
   The Spoke-Node-Ring Planning Model
   is based on buyer’s demands for:

• Distributed Systems
• Open Systems
• Production-Quality Applications

                                    Aberdeen Group
Applications
 A Distributed, Open Production Application
                                                   II H


                                                          Stratus             Credit OK?
                                                                                                    Credit       IBM S/390
                                    Order                 Encina/DCE
                                                                                                                 CICS/DCE
                                    Processing            Sybase                                    Admin
                       1                                  VOS                  Allocate
                                                                                                                 DB2/DRDA
                                                                                                                 MVS/ESA
                                                                               Credit
                                                                       ■J*.

               Stock on Hand?         No. Use Other                                        We’re Below Reorder Point
                                      Warehouses                                           on Widgets. Make More.




                       RS/6000
        Warehouse
                       Encina/DCE                                                                                  HP 9000
        Distribution
                       Informix                                                                                    Encina/DCE
                                                                                                      Resource
                                                                                                      Planning     Allbase
                                                                                                       (MRP)       HP-UX


               Reserve                                                                                        EDI: Ordering 3,000
               Inventory for                                                                                  Widget Cases.
               This Order


                                                                                                                   Pyramid
                RS/6000                                   RS/6000                                                  Ui-AHas
Warehouse                           Warehouse                                                        Order
                Encina/DCE                                Encina/DCE                                               Ingres
Distribution                        Distribution                                                     Processing
                Informix                                  Informix
                                                                                                                   Unix 5.4 MP



                                                                                                             Aberdeen Group
Intelligent Applications

           • Use More System Services

           • Hide the Complexities
              a   Comm Network
              a   Data Location
              a   How Things Get Done
              a   Where Things Get Done




                            Aberdeen Group
Six Technology Combinations

• Standalone Unix

• Single-Source Database

•    Production Distributed Databases

•    Communications to Open & Proprietary

•     Mainframes: Treating the World as Peers

•    Distributed Data Integrity

                                          Aberdeen Group
Intelligent Applications
                           Will Be Practical Soon


• SQL Access Group’s Database Interoperability

• OSF’s Distributed Computing Environment (DCE)

•    IBM’s Endorsement of DCE

•     New Products for Distributed Production
    Systems



                                           Aberdeen Group


---

## Frictionless Data Package Metadata

> Auto-generated by Archival Ingest Skill v16

### Study Record

| Field | Value |
|-------|-------|
| study_id | aberdeen-dops-distributed-open-prod-syst-cbae77 |
| title | Aberdeen Group — Distributed Open Production Systems: The Next Generation Begins (1993) |
| author | Peter S. Kastner — Vice-President, Aberdeen Group, Inc. |
| date | 1993-06-01 |
| type | conference-presentation |
| subject_domain | distributed-systems-architecture |
| methodology | Aberdeen-Group-presentation-deck |
| source_file | DOPS-1993-distributed-systems-10.pdf |
| license | CC-BY-4.0 |

### Abstract

Aberdeen Group conference presentation deck delivered by Peter S. Kastner (Vice-President, Aberdeen Group) circa 1993 titled 'Distributed Open Production Systems: The Next Generation Begins.' Boston office at 92 State Street, (617) 723-7890. Defines Downsizing as migrating computer-based functions from central mainframe to dispersed computing systems and operationally as moving MIS function down the organization. Presents the Spoke-Node-Ring Planning Model based on three buyer demands: Distributed Systems, Open Systems, Production-Quality Applications. Centerpiece is a complex multi-vendor distributed-application diagram showing: a Stratus Encina/DCE/Sybase/VOS Order Processing node coordinating with IBM S/390 CICS/DCE/DB2/DRDA/MVS/ESA Credit Admin; RS/6000 Encina/DCE/Informix Warehouse Distribution; HP 9000 Encina/DCE/Allbase/HP-UX Resource Planning (MRP); Pyramid Ui-AHas Ingres/Unix 5.4 MP Order Processing — all linked via Encina/DCE distributed transactions. Defines Intelligent Applications as those that 'use more system services and hide the complexities' (comm network, data location, how/where things get done). Six Technology Combinations: standalone Unix; single-source database; production distributed databases; communications to open & proprietary; mainframes treating world as peers; distributed data integrity. Future enablers: SQL Access Group's database interoperability, OSF's Distributed Computing Environment (DCE), IBM's endorsement of DCE, new products for distributed production systems.

### Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | high | Foundational Aberdeen DOPS framework — the core thesis Aberdeen would build the early-90s consulting practice around. Multi-vendor distributed-transaction diagram is the canonical 1993 visualization of what production distributed systems could become. Direct continuation of Spoke-Node-Ring (Study 6) into specific multi-vendor architecture. |
| **Relevance** | high | Documents Kastner/Aberdeen's role positioning DCE/Encina as the production-distributed-system enabler. The Stratus-IBM-RS6000-HP-Pyramid diagram is precisely the heterogeneous multi-vendor world Aberdeen advised Fortune 1000 IT leaders on. Reinforces Aberdeen's neutral-broker positioning across all major Unix and proprietary platforms. |
| **Prescience** | high | DCE-on-Encina vision didn't fully materialize commercially, but the concept of distributed transaction coordination across heterogeneous data stores directly anticipated modern distributed-saga patterns, X/Open XA, and ultimately microservices' transactional complexity. SQL Access Group's interoperability anticipated ODBC and JDBC. The 'hide the complexities of comm network, data location, how/where things get done' definition of Intelligent Applications is prescient of serverless and Kubernetes abstractions. |

### Prescience Detail

This study did not make forward-looking claims.

### Entities Referenced (13)

| Entity | Type | Status | Successor |
|--------|------|--------|-----------|
| Peter S. Kastner | person | active |  |
| Aberdeen Group | firm | acquired | Harte-Hanks (2007); Spiceworks Ziff Davis |
| IBM Corporation | company | active |  |
| Hewlett-Packard | company | split | HP Inc. and Hewlett Packard Enterprise (2015) |
| Stratus Computer | company | acquired | Stratus Technologies (now Penguin Solutions) |
| Transarc Corporation | company | acquired | IBM (1994) |
| Open Software Foundation (OSF) | consortium | merged | Merged with X/Open to form The Open Group (1996) |
| SQL Access Group (SAG) | consortium | merged | Merged into X/Open (1995) |
| IBM RS/6000 | Unix-server | 1990-2000 | production-shipping |
| Pyramid Technology | company | acquired | Siemens-Nixdorf (1995) |
| Informix Software | company | acquired | IBM (2001) |
| Sybase Inc. | company | acquired | SAP (2010) |
| Ingres Corporation | company | acquired | ASK (1990)/CA (1994)/Actian (renamed) |

### Technologies Referenced (10)

| Technology | Category | Vendor | Lifecycle (at study) | Lifecycle (current) |
|------------|----------|--------|---------------------|---------------------|
| Spoke-Node-Ring (S-N-R) Planning Model | architecture-framework | Aberdeen Group | active-Aberdeen-framework | conceptually-superseded-by-cloud-edge |
| IT Downsizing | strategy-pattern | Industry / Aberdeen-popularized | active-strategy-trend | absorbed-into-server-consolidation-then-cloud |
| Distributed Open Production Systems (DOPS) | architecture-framework | Aberdeen Group | active-Aberdeen-framework | absorbed-into-cloud-native-microservices |
| Transarc Encina TP Monitor | TP-monitor | Transarc / IBM after 1994 | active-product | merged-into-IBM-TXSeries-then-discontinued |
| OSF Distributed Computing Environment (DCE) | distributed-systems-runtime | OSF/Open Group | active-product | discontinued-conceptually-superseded-by-grpc-rest |
| IBM DRDA (Distributed Relational Database Architecture) | database-interoperability | IBM Corporation | active-standard | still-shipping-on-Db2 |
| IBM CICS | TP-monitor | IBM Corporation | industry-standard | still-shipping |
| HP Allbase/SQL | relational-DBMS | Hewlett-Packard | active-product | discontinued |
| Intelligent Applications | design-pattern | Aberdeen Group | active-strategy-trend | evolved-into-serverless-and-managed-services |
| Two-Phase Commit (2PC) | distributed-transaction-protocol | Industry / X-Open | industry-standard-X-Open-XA-since-1991 | still-relevant |

### Observation Summary

- Total observations: 12
- By type: dops_definition: 1, multi_vendor_diagram: 1, intelligent_apps_def: 1, six_tech_combinations: 1, dce_endorsement: 1, sag_interoperability: 1, stratus_encina_node: 1, ibm_s390_node: 1, hp_9000_node: 1, kastner_role: 1, dops_year: 1, informix_role: 1
