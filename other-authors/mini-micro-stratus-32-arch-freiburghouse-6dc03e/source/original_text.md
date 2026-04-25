# Mini-Micro Systems: Robert Freiburghouse on the Stratus/32 Architecture — VOS, StrataLINK, and 'Continuous Processing' (1982)

> Archived from: Stratus-Arch-Freiburghouse-1982-Mini-Micro-Systems-5.pdf
> Original publication date: 1982
> Author: Robert Freiburghouse (Stratus Computer)

---

## Original Document Text


===== Stratus-Arch-Freiburghouse-1982-Mini-Micro-Systems-5.txt =====
                                                       NEW SYSTEMS




                                            feSD-scaO^
                                  ROBERT FREIBURGHOUSE, Stratus Computer, Inc.



              Any number of modules, each configurable to be fully redundant,
                    achieves ' continuous processing ’ for the Stratus/32


   Buyers who must have a computer system that                    interactive program development. It uses a combina­
continues to function despite failures have not had               tion of hardware and software that provides continuous
much of a selection, but their choice has been                    processing of user programs during computer failure
broadened by the introduction of the Stratus/32 system            without checkpoint/restart programming at the user or
from Stratus Computer, Inc., Natick, Mass. With 4M                system level. Central to the system’s fail-safe operation
bytes of memory, dual i43M-byte disks, a 600-lpm                  are processing modules, each of which has redundant
printer and magnetic tape, a typical Stratus/32 sells for         logic and communication paths, logic and CPU boards
$172,000, including COBOL and vos software licenses.              and main and disk memory. Twin components operate
Based on COBOL benchmarks, the system’s performance               in parallel with each other; when one fails, its partner
equals or surpasses that of several popular superminis.           carries on.
   The Stratus/32 multiprocessor, fault-tolerant system
for commercial applications supports on-line transac­             Architectural overview
tion processing, batch processing, word processing and               The Stratus/32 processing modules are connected via




Fig. 1. A Stratus/32 system consists of as many as 32 processing modules connected by a high-speed coaxial link. The modules can be
located anywhere within an office building or can be adjacent to each other.
                                                        of the module they are using. Likewise, batch jobs can
Each processing module can be                           run anywhere in the system.
configured as fully redundant, partially                  All VOS service requests have a uniform interface
                                                        that is independent of the processing module on which
redundant or non-redundant.
                                                        the work will be performed. For example, a request to
                                                        open a file has the same form and arguments regardless
the StrataLlNK high-speed coaxial link. Each process­ of where the file resides. VOS examines the file name,
ing module consists of memory, two Motorola Corp. looks in a device table to determine the module that
68000 CPUs, at least one disk and various peripheral owns the device and performs the requested operation
controllers and devices (Fig. 1). Both 68000 CPUs are or makes a network request over the StrataLlNK to the
visible to the operating system, and each executes its VOS running the owning module. The requesting
own instruction stream using a shared memory.           program does not see the network request. Conse­
   Each processing module can be configured as fully quently, user programs are unaware of the location of
redundant, partially redundant or non-redundant. The files or devices and see the multiple-module network as
degree of a module’s redundancy determines the a single virtual-computer system (Fig. 2).
module’s resistance to hardware failure. A fully redun­
dant module can withstand failure of essentially any Examining the hardware
component in the module without performance or data       A processing module includes one or more cabinets
loss and without user program interruption. Multiple that contain a complete computer with a logic-board
modules are used only to achieve greater system chassis, dual power supplies, peripheral devices and
capacity; they never serve as backup for other modules. and terminal port. A single cabinet holds a fully
   Stratus’s distributed virtual operating system (VOS) redundant module consisting of two i43M-byte disk
runs in each of the processing modules. All modules are drives, a magnetic tape, 16M bytes of memory,
equal and can operate independently, but through the redundant CPU boards and a set of redundant peripher­
use of transparent local networking software, VOS al controllers (Fig. 3).
makes the entire set of processing modules appear as a    A high-speed bus with a 125-nsec. cycle time is
single computer system to programs, programmers central to processing-module organization The bus—
and application users.                                  virtually two buses operating in parallel—has two sets
  Although each peripheral device is attached to a of data and control-logic paths. The data path on each
processing module, VOS makes all devices available to bus is 32 bits wide, and data can be put on the bus every
programs running in any module. Similarly, a program bus cycle. This results in a potential bus rate of 32M
running in a module creates processes to run in the bytes per sec., although processor/memory boards now
same module or in others. An interactive terminal user run at 16M bytes per sec. By comparison a VAX/11-780
can create processes to execute commands or to run bus runs at 13M bytes per sec.
programs in any module. The users need not be aware        Each logic board that can be attached to the bus can




rig. z. i ne oiraius/oz virtual operating system (vuoj maKes an processing modules appear as part of a
devices, files and system resources are accessible as if it were a single computer.                    single virtual system in which all
                                                                 hard. In either case, the failure is noted in a
The CPU board contains two complete                              hardware-failure log file, and selected terminals are
sets of logic and is self-checking.                              notified of the failure. If the board passes the
                                                                 maintenance-software check, it is resynchronized with
                                                                 its redundant partner and put back on-line, and its red
However, the operating system has sufficient software            light is turned off. If the board fails the software check,
error detection to run dual StrataLiNKs as separate              it remains off-line, and a red light on the system control
parallel links until one fails. Failure of a link is detected,   panel is lit.
and data are retransmitted over the other link without              A failed board can be replaced in a running system by
affecting users of the link. A link failure could cause          a nontechnical person without special tools and without
some performance loss because a dual link has a                  affecting any user’s program. VOS dynamically reconfi­
2.8M-byte-per-sec. transmission rate, while a single             gures itself when a board is added or removed from the
link has a 1.4M-byte-per-sec. rate. But because most             system.
links do not operate even close to their maximum rates,
it is unlikely that an application would notice the              Operating-system software
performance difference.                                            Each processing module contains two software-
                                                                visible 68000 processors and a software-visible Z80 p.p
A failure scenario                                              on each peripheral controller. The VOS off-loads de­
  When a logic board or an attached peripheral device tailed I/O processing to the Z80s and uses one of the
fails, it puts itself off-line, lights a red light on the board 68000s to respond to interrupts and to execute the word
and transmits an interrupt to the operating system. processor. The other 68000 executes user code and
Maintenance software in the system then tests the non-interrupt-driven system code. For example, a user
failed board to determine if the failure was transient or program that calls VOS to perform disk I/O has the user
                                                                68000 enter VOS and set up the disk-l/o command chain.
                                                                The user 68000 is then rescheduled to execute another
                                                                user’s program. The disk-l/o operations are executed
                                                                by the Z80 on the disk controller, and when the disk
                                                                operation completes, the “executive” 68000 responds to
                                                                the interrupt and posts a notification to the scheduler
                                                                that this I/O event is complete. Depending on the
                                                                setting of the scheduler’s parameters, the user 68000
                                                                can be rescheduled to execute the user’s program then
                                                                or at the next scheduling interval.
                                                                    A “process” is a virtual CPU and a 16M-byte address
                                                                space in which a sequence of user programs can be
                                                                executed. A process is created when a user logs onto
                                                                the system, and is terminated when a user logs off. A
                                                                process can create additional processes that operate
                                                                independently of the creating process. VOS uses system
                                                                processes to monitor terminals for log-in requests, to
                                                                run the spooler and to perform requests made by other
                                                                processing modules.
                                                                    Each process has an address space consisting of 4M
                                                                bytes for VOS and 12M bytes for a user program (Fig.
                                                                6). A program consists of any number of separately
                                                                compiled subroutines, which can be written in different
                                                                source languages.
                                                                    The i6M-byte virtual address space is divided into
                                                                4096-byte pages that are mapped into physical memory
                                                                pages by an address-translation map on the CPU board.
                                                                The translation occurs within the 125-nsec. clock cycle
                                                                and does not slow the CPU. The user’s program and
                                                                 most of the programs in vos see only the virtual
                                                                 address space and are unaware of the translation.
                                                                    The hardware address-translation map informs the
                                                                 scheduling and paging algorithms of which physical
                                                                 pages were recently used and which virtual pages of
                                                                 each process were recently used by that process. Thus,
                                                                 it is possible to determine quickly the real working set
When data are written to a given
memory location, both memory
controllers respond and write the data
into their memory.
of each process and which physical page of memory to
replace when a new page is required.
Sharing and protection.
   Each page of a process’s address space has an
associated access code that allows execution, read/write
or read-only. The processor has supervisor and user
execution states, and, for each state, it has potentially
separate access codes for each page of the address
space. These access codes are stored in the address­
translation map used to translate virtual to physical        Fig. 5. A single Stratus/32 CPU board contains four Motorola
addresses, and are enforced for every memory refer­          68000 processors that provide two software-visible processors. The
ence in both user and supervisor states.                     board is fully self-checking and contains redundant virtuallphysical
                                                             address-translation maps.
   All users share the physical pages of VOS and appear
in the address space of each process. Likewise, user
programs are shared if executed by more than one • CRT menu-oriented commands. The VOS com­
process. Sharing user programs and system commands
                                               mand interpreter accepts all commands in two forms: a
and utilities requires no action on the part of a user and
                                               conventional line-oriented form suitable for use on
                                               hard-copy terminals or from within command language
occurs with no visible effect to the user. All code
                                               programs called command macros, and a CRT menu
produced by Stratus compilers is pure and reentrant.
                                               form that displays all command options and their
   A user’s program is protected from destruction
                                               default values. The CRT menu form is invoked by typing
because each page of program instructions is given an
                                               the name of the command followed by a function key. A
execute-only access code. A user’s data are protected
                                               command reference manual is unnecessary.
from other users because they exist only in the address
                                                  • Five industry-standard languages. These include
space of the user. The data are also protected from
execution to aid debugging of users’ programs. COBOL 74, FORTRAN 78, PL/l-G, Pascal and BASIC. All
                                               languages are supported by optimizing compilers that
   Inter-process communication facilities of VOS allow a
                                               share an optimizer and a code generator that produces
multi-process application to be developed on a single­
                                               highly optimized relocatable binary code. Subroutines
module configuration and run later without modifica­
                                               written in all languages can be combined into a
tion on a distributed configuration consisting of multi­
                                               program, and all languages can call all VOS service
ple processing modules, or even on multiple Stratus
                                               subroutines. All compiled code is pure and reentrant.
systems connected by StrataNET. Consequently, the
mechanisms used to start, stop or synchronize pro­• Program debugging. Program development in
                                               any high-level language can be done entirely within
cesses do not use shared memory; they use the file
system as a high-level shared memory.          that language without the programmer’s knowing the
                                               instruction set, data formats or register arrangement
   Every file in the file system has an associated lock
                                               of the 68000 processor. For all languages, the debugger
and an associated event. In addition, each record in a
                                               can set breakpoints on statements, display variables,
file has an associated lock. Locks synchronize file access
                                               make assignments to variables, execute calls and
between two or more processes and can be set or reset
                                               functions, execute gotos, step through the program and
to indicate reading or updating of the file or records.
                                               execute conditional breakpoints. The debugger can be
   Simple notification and waiting for events between
                                               entered to start execution of a program, when a
processes are performed using event counts. An event
                                               program fails or to examine a snapshot of a program
count is a large integer that is incremented each time
that it is notified by a process.              that has failed.
                                                  • Data security. Each file has an access-control list
   Most inter-process communication is related to files
                                               consisting of pairs of user ids and associated access
and consists of notifying processes that data are
                                               rights (execute, read or read/write). Access rights can
available to be processed or of waiting for data to arrive
                                               be specified by a user or groups of users and are
for processing. The use of events and locks associated
                                               enforced by the vos I/O system. Access-control lists
with files is consequently natural and efficient.
                                               provide file security without embedding passwords into
User-visible software                          programs. The lists operate on the basis of people or
  The Stratus/32 was introduced with a host of groups who access the file; consequently, they are easy
native-mode software, including:               to administer and use. Security is provided regardless
The bus virtually two buses operating                              and is self-checking. Four Motorola 88000 processors
                                                                   provide each board with two processors visible to the
in parallel—has two sets of data and
                                                                   operating system (Fig. 5). A redundant partner CPU
control-logic paths.                                               board ensures continuous processing in the event of a
                                                                   failure of a CPU board. At a component price of
detect its own failure and shut itself down. It can also approximately $100 for each 68000, this is a cost-
run with a redundant board that continues to operate in effective solution to continuous processing that was not
the event of its partner’s failure. Neither logic board is practical until the availability of VLSI technology.
primary, and neither is aware of the other. The pair of                Redundancy is achieved by using a pair of logic
boards appears collectively to other system components boards for each logical entity in the system. Each board
as a fail-safe entity.                                             is attached to both halves of the bus, and both boards
   The self-checking technique used by each type of operate in parallel, performing identical operations.
board differs slightly, but generally involves the use of The output of both boards is placed on the bus at the
two sets of logic on a board. Each set performs every same instant and is guaranteed to be identical.
operation in parallel with the other. When data are to                 Memory is duplicated in a redundant system so that
be sent to the bus or to a device, the results produced N megabytes of program-visible memory is implement­
 by the two sets of logic are compared. If identical, the ed using 2NM bytes of physical memory with N
 result is sent onto the bus or to the device. Dissimilar megabytes attached to each of two memory controllers.
 results indicate a board failure, and no data are sent. In When data are written to a given memory location,
 this case, a red LED on the board is lit, and an interrupt both memory controllers respond and write the data
 signal is sent on the bus. Until the board is tested and into their memory. When data are read from memory,
 logically reconnected by maintenance software, it both controllers respond and read from their memory.
 remains off-line. The board’s redundant partner contin­               The controllers and the memory are synchronized
 ues to operate, and no other component of the system is and appear to the rest of the system as a single logical
 aware of the failure (Fig. 4).                                     entity. Memory subsystems are not paired with CPUs,
    The CPU board contains two complete sets of logic bus halves or other system components. Memory is
                                                                    implemented from 64K rams and is packaged on im- or
                                                                    2M-byte boards. It has a 375-nsec. read-cycle time and
                                                                    is four-way interleaved. A typical processing module
                                                                    has 4M or 8M bytes of memory. In packaged configura­
                                                                    tions, Stratus sells memory for $5000 per megabyte. A
                                                                    2M-byte array board lists for $20,000.
                                                                       The memory system can be dynamically reconfigured
                                                                    to be redundant or non-redundant. This allows a module
                                                                    to use all available memory when full redundancy is not
                                                                    needed. Reconfiguration can occur on-line without
                                                                    affecting running programs.
                                                                        Disks cannot run completely synchronized with each
                                                                     other; they require help from the operating system to
                                                                     provide continuous processing. Each disk can be
                                                                     configured to have a duplicate. The mirror disk is
                                                                     attached to a separate controller to protect from
                                                                     controller failure. When a program writes a record to a
                                                                     redundant disk, the operating system writes records to
                                                                     the disk and to its mirror. When a program reads from
                                                                     the disk, the operating system reads from the disk that
                                                                     is not busy or whose heads are best positioned to read
                                                                     the record. If a read error occurs, the record is read
                                                                     from the other disk.
                                                                        An error-correction code stored with each disk
                                                                     record detects media failures during a read. A read
                                                                     error from a redundant disk results in reading the same
                                                                     record from its partner. Non-redundant disks are
                                                                     vulnerable to total disk failure, but are protected from
                                                                     media failures by vos, which verifies each write. A
                                                                     record that cannot be verified is rewritten to another
                                                                      disk block, and the bad block is removed from the
  F,9-3^S,L"
        drive and two software-visible CPUs. (Additional disks and
                                                                      available disk space.
   tapes are held in adjacent cabinets.)
                                                                        StrataLlNKs, like disks, cannot run synchronized.
All languages are supported by                                                 • Transaction processing. VOS supports the devel­
optimizing compilers that share an                                          opment of transaction-oriented applications by provid­
                                                                            ing CRT forms-design utility and forms I/O statements in
optimizer and a code generator that                                         all high-level programming languages, multi-terminal
produces highly optimized relocatable                                       transaction control in all high-level programming
binary code.                                                                languages, individual record and file locking, multi-key
                                                                            indexed file access, queued file access and file-system
                                                                            operations to ensure the integrity of transactions.
                                                                               Data representing a transaction can be processed
of what programs or system commands are used to                             directly by a user-written transaction-control program,
access files.                                                               or data can be written into a queued file to be processed
   • Networking. StrataNET permits two or more                              by other programs, called transaction servers, which
Stratus systems to run as if they were one system. Just                     operate asynchronously with respect to the transaction­
as users of individual processing modules of a system                       control program. Transaction servers can run in any
have access to their entire system, users of a networked                    processing module, not just modules running the
system have access to the entire network without any                        transaction-control program. Likewise, transaction­
network-oriented requests or commands. Normal file                          control programs can run in several modules. The
operations and inter-process communication operate                          number and distribution of transaction servers can be
transparently to the user’s program.                                        dynamically altered in response to changes in the
                                                                            transaction rate.                                       ■

                                                            Process
     VOS       Programs      Data    Heap         Stack
                                                             data
                                    ------ ►-    -4------
                                                                            Robert Freiburghouse is co-founder and vice president of
  4M bytes                                                                  software engineering, at Stratus Computer, Inc., Natick, Mass.
  reserved                           12M bytes


Fig. 6. Stratus/32 virtual address space provides as much as 12M
bytes of program and data space per user program. The stack is
the interrupt directory; the heap is handy for temporary data that must
be stored randomly. Both expand and contract as needed. User
programs and system code are shared without user involvement, and
no segment limits are imposed on programs or data.




                                          Reprinted from MINI-MICRO SYSTEMS May, 1982
                                            © 1982 CAHNERS PUBLISHING COMPANY




                                                                          STRATUS COMPUTER, INC
                                                                          17-19 STRATHMORE ROAD
                                                                          NATICK, MA 01760
                                                                          (617) 653-1466


---

## Frictionless Data Package Metadata

> Auto-generated by Archival Ingest Skill v16

### Study Record

| Field | Value |
|-------|-------|
| study_id | mini-micro-stratus-32-arch-freiburghouse-6dc03e |
| title | Mini-Micro Systems: Robert Freiburghouse on the Stratus/32 Architecture — VOS, StrataLINK, and 'Continuous Processing' (1982) |
| author | Robert Freiburghouse (Stratus Computer) |
| date | 1982 |
| type | trade-press-architectural-feature |
| subject_domain | fault-tolerant-computing/computer-architecture |
| methodology | vendor-architect-byline-trade-press |
| source_file | Stratus-Arch-Freiburghouse-1982-Mini-Micro-Systems-5.pdf |
| license | CC-BY-4.0 |

### Abstract

1982 Mini-Micro Systems bylined feature article by Robert Freiburghouse (Stratus Computer's principal software architect, formerly of Multics PL/I compiler design) detailing the Stratus/32 architecture and 'continuous processing' design philosophy. Key architecture facts documented: up to 32 processing modules connected via StrataLINK high-speed coaxial link (32 Mbits/sec; 2.8 MB/sec dual / 1.4 MB/sec single); each processing module configurable as fully redundant, partially redundant, or non-redundant; each module contains two Motorola 68000 CPUs sharing memory plus one Z80 per peripheral controller; high-speed bus 125-nsec cycle, two parallel data/control paths 32-bit wide, 32 MB/sec potential (16 MB/sec actual at processor/memory boards) — vs VAX 11/780 at 13 MB/sec; CPU board self-checking with paired logic, full-redundant module survives any component failure without performance/data loss; failed boards replaceable by non-technical personnel without tools while system running; VOS distributed virtual OS makes all modules appear as single virtual computer; per-process address space 16 MB (4 MB VOS + 12 MB user). Typical Stratus/32 priced at $172,000 (4 MB memory, dual i43MB disks, 600 lpm printer, mag tape, COBOL + VOS licenses). This is the canonical first-party architectural reference for the Stratus/32 platform throughout the 1982 Stratus quote corpus (studies 1-3 of Batch 25).

### Document Assessment

| Dimension | Rating | Rationale |
|-----------|--------|-----------|
| **Importance** | high | Authoritative bylined Stratus architecture reference from Freiburghouse himself — the technical primary source backing Kastner's marketing claims in the parallel 1982 quote corpus. |
| **Relevance** | high | Companion architectural reference for the Stratus/32 system that anchors Kastner's pre-Aberdeen marketing voice; technical baseline for fault-tolerant architecture discussions across the archive. |
| **Prescience** | high | Stratus/32's pair-and-spare hardware redundancy + transparent single-system-image distributed OS (VOS) prefigured: (1) modern RAS-class server hardware (e.g., IBM Z mainframes' lockstep processors); (2) software-defined HA clusters as the dominant successor pattern; (3) hot-pluggable component replacement ubiquitous in modern data-center hardware. |

### Prescience Detail

This study did not make forward-looking claims.

### Entities Referenced (5)

| Entity | Type | Status | Successor |
|--------|------|--------|-----------|
| Robert A. Freiburghouse | person | active |  |
| Stratus Computer | company | acquired | Stratus Technologies (now Penguin Solutions) |
| Motorola, Inc. | company | split | Freescale Semiconductor (2004) -> NXP (2015); Motorola Solutions / Mobility |
| Digital Equipment Corporation (DEC) | company | acquired | Compaq (1998), then HP (2002) |
| Mini-Micro Systems | publication | defunct | Cahners Publishing; absorbed/discontinued early 1990s |

### Technologies Referenced (8)

| Technology | Category | Vendor | Lifecycle (at study) | Lifecycle (current) |
|------------|----------|--------|---------------------|---------------------|
| Stratus/32 Continuous Processing System | computer-system | Stratus | newly-launched-1982 | obsolete |
| Stratus VOS (Virtual Operating System) | operating-system | Stratus | newly-launched-1982 | active-as-stratus-vos |
| StrataLINK Inter-Module High-Speed Coaxial Link | interconnect | Stratus | current-1982 | obsolete |
| Stratus Dual-Path 32-bit Parallel Bus (125-nsec cycle) | system-bus | Stratus | current-1982 | obsolete |
| Stratus Self-Checking Hardware Pair Architecture | computer-architecture | Stratus | current-1982 | active-in-stratus-ftServer |
| Paired Motorola 68000 CPUs (Stratus Module) | microprocessor-architecture | Motorola/Stratus | current-1982 | obsolete |
| Zilog Z80 Peripheral Controller Coprocessor | microcontroller | Zilog/Stratus | current-1982 | obsolete |
| Hot-Pluggable Board Replacement (no tools, non-tech personnel) | system-feature | Stratus | newly-launched-1982 | ubiquitous |

### Observation Summary

- Total observations: 8
- By type: product-spec: 7, affiliation: 1
