# NCR 3000 Server Cabinet Engineering Diagram (1992): Intel486 50MHz Multiprocessor Boards, Micro Channel, Hot-Pluggable Storage

> Archived from: NCR-3000-cabinet-engineering-1992-2.pdf
> Original publication date: 1992
> Author: NCR Corporation (engineering documentation)

---

## Original Document Text


===== NCR-3000-cabinet-engineering-1992-2.txt =====
                                                                Processor Boards with Two 50MHz
                                                                Intel486 Microprocessors Each
        Top View
                                                   Power Supply Interface               Memory Board

                                                        Power Supplies                          Micro Channel Interface Chipset


                                                                                                                  Local Peripheral
                                                                                                                  Board for VGA
                                                                                                                  Monitor, Mouse,
                                                                                                                  Keyboard,
                                                                                                                  Diagnostic
                                                                                                                  Monitor and
                                                                                                                  Parallel Printer

                                                                                                                  Primary Micro
                                                                                                                  Channel Slots (8)

                                                                                                                  Internal SCSI Cables

                                                                                                                  Hot Pluggable
             Micro Channel Cable Access                                                                            75" Fans

                                                                                                                    ? Full-Height or
                                                                                                                   18 Half-Height
                             Back View                                                                            Hot Pluggable
                             Primary Side                                                                         Fixed Disks



                                                                         Power Distribution Assembly
Front View
Optional Side
                      Processor Boards with Two 50MHz      4 Full-Height or 8 Half-Height
                      Intel486 Microprocessors Each        Removeable Devices                   Power/Standby Switch
                    Memory Board                                                                                     Security Lock

                                                                                                                    LEDs
                                                                                                                      Power
                                                                                                                      Status
                                                                                                                      Battery

Optional Micro -                                                                                                    4 Full-Height or
Channel Slots (8)                                                                                                   8 Half-Height
                                                                                                                    Removeable Devices
Hot Pluggable —                                                                                                     Standard Devices
6.75" Fans                                                                                                          Include:
                                                                                                                    One 525 MB QIC Tape
Up to 14                                                                                                            One 1.44 MB Flex Disk
Full-Height or
                                                                                                                    Optional Devices Include:
28 Half-Height-
                                                                                                                    600 MB CD-ROM
Hot Pluggable
                                                                                                                    1.3 GB Digital
Fixed bisks
                                                                                                                    Audio Tape




                                                                                                                 Removable Media
                               Power Back Up System Batteries                                                    Access Door


---

## Frictionless Data Package Metadata

> Auto-generated by Archival Ingest Skill v16

### Study Record

| Field | Value |
|-------|-------|
| study_id | ncr-3000-cabinet-engineering-diagram-199-fa564f |
| title | NCR 3000 Server Cabinet Engineering Diagram (1992): Intel486 50MHz Multiprocessor Boards, Micro Channel, Hot-Pluggable Storage |
| author | NCR Corporation (engineering documentation) |
| date | 1992 |
| type | engineering-diagram |
| subject_domain | server-hardware-architecture |
| methodology | vendor-engineering-documentation |
| source_file | NCR-3000-cabinet-engineering-1992-2.pdf |
| license | CC-BY-4.0 |

### Abstract

NCR Corporation engineering diagram from 1992 documenting the NCR 3000 server cabinet design: processor boards each carrying two 50MHz Intel486 microprocessors, memory boards, eight Primary Micro Channel slots (with eight Optional slots on the Optional Side), 6.75-inch hot-pluggable fans, hot-pluggable internal SCSI fixed disks (up to 14 full-height or 28 half-height), 4 full-height or 8 half-height removable devices on each side, standard 525MB QIC tape and 1.44MB flex disk, optional 600MB CD-ROM and 1.3GB Digital Audio Tape, power back-up system batteries, security lock, and a local peripheral board for VGA monitor / mouse / keyboard / diagnostic monitor / parallel printer. The artifact provides concrete platform context for the Aberdeen Open OLTP white-paper claims about low-cost commercial multiprocessor platforms, X/Open compliance, and downsizing-from-mainframe value propositions of 1991-1992. Companion to the Norway 1992 OLTP seminar deck which references the NCR Model 3550 (UNIX V.4 multiprocessor up to eight i486-50MHz, ~320 MIPS, supporting 1,000+ workstations).

### Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | moderate | Concrete engineering documentation of the NCR 3000 family that underlies Aberdeen's 1991-1992 Open OLTP analyses; specifies the Intel486 50MHz / Micro Channel / hot-pluggable storage / X/Open platform that Kastner's white papers describe in the abstract. |
| **Relevance** | moderate | Documents the NCR commercial multiprocessor platform that Aberdeen OLTP/MP studies and the WSJ ad refer to; provides hardware context for the contemporaneous Kastner Korean and Norway translations. |
| **Prescience** | low | Specific cabinet design did not predict any unique trend; however, the architectural choices (commodity x86 multiprocessing, hot-pluggable storage, modular SCSI, redundant power, X/Open Unix) anticipated the rack-mount commodity-x86 server pattern that dominated the 2000s data center. |

### Prescience Detail

This study did not make forward-looking claims.

### Entities Referenced (3)

| Entity | Type | Status | Successor |
|--------|------|--------|-----------|
| NCR Corporation | company | active | Spun out of AT&T 1996; later split NCR/NCR Voyix 2023 |
| AT&T Corporation | company | split | Multiple divestitures; AT&T Inc. is now SBC-based |
| Intel Corporation | company | active |  |

### Technologies Referenced (7)

| Technology | Category | Vendor | Lifecycle (at study) | Lifecycle (current) |
|------------|----------|--------|---------------------|---------------------|
| NCR 3000 Server Family | computer-system | NCR | current | obsolete |
| Intel i486 at 50MHz | microprocessor | Intel | current | obsolete |
| IBM Micro Channel Architecture (MCA) | system-bus | IBM-licensed | mature | obsolete |
| Hot-Pluggable Disk and Fan Subsystems | storage-architecture | industry | emerging-commercial | ubiquitous |
| Small Computer System Interface (SCSI) | storage-bus | industry | mature | legacy-with-SAS-and-NVMe-successors |
| 1.3GB Digital Audio Tape (DAT) | storage-media | industry | current | obsolete |
| 525MB Quarter-Inch Cartridge (QIC) Tape | storage-media | industry | current | obsolete |

### Observation Summary

- Total observations: 6
- By type: hardware-spec: 5, affiliation: 1
