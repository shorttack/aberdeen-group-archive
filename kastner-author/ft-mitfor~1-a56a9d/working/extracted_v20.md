## Who Cares If The Computer Breaks? 

MIT Forum — October 1995 Peter S. Kastner Vice President Aberdeen Group, Inc. Boston, Mass.  02108 (617) 723-7890 

## Agenda 

⬛Who cares if the computer breaks? 

# ⬛Where computer systems fail 

# ⬛Planning for the inevitable ⬛Approaches to minimizing downtime 

# Who Cares If the Computer Breaks? 

## Computer Industry Ancient History 

- ⬛One-tier computing 

**==> picture [170 x 111] intentionally omitted <==**

   - Jobs were batch-processed based on keypunched data entered on forms by people 

   - Reports printed on paper 

   - Virtually no one was on-line 

- ⬛Commercial computers kept the books 

- ⬛If the computer failed, jobs were restarted and run again 

## Fast Forward to the 1990s 

- ⬛Complex computing environments 

   - Multiple tiers of networks 

   - Computer-to-computer transactions 

– On-line, real-time changes 

   - Less paper, ad hoc queries 

- ⬛Commercial computers _make_ the money 

- ⬛But computer systems still fail! 

## Who Cares If The Computer Breaks? ⬛Public safety 

**==> picture [178 x 50] intentionally omitted <==**

⬛National security 

⬛Banking and financial system 

⬛Telecommunications industry 

- ⬛Retailers 

- ⬛45% of U.S. workers now using PCs 

⬛And virtually every aspect of our society 

# Where Computer Systems Fail 

## Hardware, Networks, & Software 

## Hardware Always Breaks 

## Reliability Trends 

⬛Unit reliability improvesUnit reliability improvesimproves over time due to fewer, more robust components 

**==> picture [602 x 231] intentionally omitted <==**

**----- Start of picture text -----**<br>
⬛Unit reliability improvesUnit reliability improvesimproves<br>over time due to fewer,<br>System<br>more robust components<br>⬛System reliability declines Mean Tim e Between Failure<br>over time due to more<br>components Components<br>1995<br>**----- End of picture text -----**<br>


**==> picture [41 x 14] intentionally omitted <==**

**----- Start of picture text -----**<br>
Time<br>**----- End of picture text -----**<br>


**==> picture [203 x 79] intentionally omitted <==**

**----- Start of picture text -----**<br>
1,000 x<br>**----- End of picture text -----**<br>


## Software Usually Breaks 

- ⬛Correct software will outlive its hardware and 

never fail 

- ⬛But most software fails 

   - Too many lines of code ... complexity exceeds human capacity 

   - Poor or unsystematic design, review, testing 

   - Poor choice of software development tools 

   - Repeated re-work due to business logic changes 

   - Trade-offs on quality vs. time-to-market 

## Networks Will Always Break 

⬛Networks suffer all the inherent problems of computer hardware and software, plus the reliability problems of electrical/light cables ⬛Network availability is a key inhibitor to the growth of distributed computing 

**No Digging** 

# Planning for the Inevitable 

_“A stitch in time saves nine”_ 

## Planning for Downtime 

⬛Backup files early and often 

- ⬛Keep backup copies off site 

⬛Design computer-free business procedures 

⬛Choose high-availability computing options 

⬛Hot backup of applications 

- ⬛Off-site disaster backup of applications 

## Application Availability 

**==> picture [165 x 16] intentionally omitted <==**

**----- Start of picture text -----**<br>
Downtime Per Year<br>**----- End of picture text -----**<br>


⬛There are lots of ways to measure availability 

- MTBSI 

– Hardware availability 

– System availability 

⬛Application availability to users is the most useful measure 

**==> picture [344 x 162] intentionally omitted <==**

**----- Start of picture text -----**<br>
10000.00 5259.6<br>1000.00 526.0<br>100.00 52.6<br>Minutes/Year<br>(log scale) 10.00 5.3<br>0.5<br>1.00<br>99.0000% 99.9000% 99.9900% 99.9990%<br>99.9999%<br>0.10<br>**----- End of picture text -----**<br>


## **Uptime Percent** 

⬛In today’s business world, 99.9% is a floor, not the ceiling 

## Planning for Downtime 

⬛Off-site disaster backup of applications ⬛Hot backup of applications 

⬛   High-availability Paranoia Curve computing options 

⬛Design computer-free business procedures 

# ⬛Keep backup copies off site 

# ⬛File backup early and often 

Approaches to Minimizing Downtime ⬛ _How paranoid are you?_ ⬛ _How much have you got to spend?_ 

– Hardware 

- Software 

- Networks 

- Other 

Approaches to Minimizing Downtime 

## Hardware 

- ⬛Standard industry practices to catch errors 

- ⬛Self-testing (including systems management software) 

- ⬛Overcapacity by design 

- ⬛Hot replacement of power, fan, disk components 

- ⬛RAID disk storage options 

- ⬛Redundant hardware with failover (N+1 or other) 

Approaches to Minimizing Downtime Classic Failover Architecture 

- ⬛Primary Machine 

⬛Secondary Machine 

- Runs critical application 

- Saves key data periodically 

   - Listens for periodic heartbeat message 

- Sends periodic “heartbeat” message to secondary 

– Eventually fails ... 

– Determines when Primary has stopped executing – Uses saved key data to restart/recover application 

Primary 

**==> picture [64 x 84] intentionally omitted <==**

Heartbeat Messages Critical Data Structures 

Secondary 

**==> picture [73 x 84] intentionally omitted <==**

## Approaches to Minimizing Downtime Hardware Failover Variations 

## _Hardware Self-Checking_ 

**==> picture [426 x 326] intentionally omitted <==**

**----- Start of picture text -----**<br>
N + 1<br>?<br>Shared Disk Tandem<br>Heartbeat<br>Messages<br>Digital Equipment<br>**----- End of picture text -----**<br>


**==> picture [204 x 108] intentionally omitted <==**

**----- Start of picture text -----**<br>
=<br>?<br>Stratus<br>**----- End of picture text -----**<br>


## Approaches to Minimizing Downtime 

## Networks 

- ⬛Redundant network interface hardware 

- ⬛Bridge/routers follow computer hardware path 

⬛Robust protocols 

⬛Adaptive routing eliminates point-point failure ⬛More options in high-end servers; few options in workgroup servers 

**==> picture [322 x 341] intentionally omitted <==**

**----- Start of picture text -----**<br>
WAN<br>LAN<br>**----- End of picture text -----**<br>


Approaches to Minimizing Downtime 

## Software Availability 

- ⬛Failover always involves software 

- ⬛Failure prediction technology aims to catch hardware failures before they happen 

- ⬛Operating system availability is directly related to age 

- ⬛RDBMS & OLTP software ensures data recoverability 

- ⬛Applications are poorly instrumented for failures, but will improve 

- ⬛Desktop software is still prone to failure 

## Opportunities 

- ⬛Hardware and Networks 

   - Note:  buyers are contradictory.  They want the highest availability levels but are unwilling to pay (much) more than commodity prices 

   - – Low/no-cost improvements in client-server application availability 

   - Added value by improved failure prediction due to better error-recovery reporting 

   - Self-repairing networks 

## Software and Services 

- ⬛Software 

   - Systems management tools down to the applicationobject level 

   - Adaptive routing to movable objects 

   - Client-server application testing tools 

   - Self-distributing databases 

- ⬛Services 

   - Disaster backup for client-server applications 

   - Availability audits and testing 

## Aberdeen Group Conclusions 

- ⬛Computer failures are becoming more catastrophic because we depend so much on computers 

- ⬛Reducing the cost and aggravation of downtime involves a spectrum of increasingly costly remedies 

- ⬛Hardware and network availability improvements are offset by more computers/networks that will fail 

- ⬛Most future improvements in availability will depend on system software that assists application failover without dramatically increasing development costs or complexity 

- ⬛There are interesting opportunities for new businesses 

**==> picture [576 x 397] intentionally omitted <==**

