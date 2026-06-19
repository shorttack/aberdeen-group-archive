# v1.8.0 quotations corpus — prescience scoring report

Generated: 2026-06-19T19:41:41.314181+00:00

## Run metadata

- Model: `sonar-reasoning-pro`
- Strategy: P2 default, P1 tiebreaker on (bucket=medium AND confidence≤2)
- Rows scored: **334**
- Tiebreakers invoked: **42**
- Tiebreaker rate: 12.6% of rows
- P2-medium NOT tiebroken (confidence=3): 46
- Parse-fails total: 0

## Final-bucket distribution

| Bucket | Count |
|---|---:|
| high | 184 |
| medium | 84 |
| low | 66 |
| parse_fail | 0 |
| human_review | 0 |

## Final-pipeline mix

| Pipeline | Count |
|---|---:|
| P2 | 322 |
| P1_tiebreak | 12 |
| P2_p1_fail | 0 |
| human_review | 0 |

## P2 bucket distribution (pre-tiebreak)

| Bucket | Count |
|---|---:|
| high | 181 |
| medium | 88 |
| low | 65 |
| parse_fail | 0 |

## Tiebreaker effectiveness

- Of 42 tiebreakers invoked, P1 won (changed final verdict) on **12** rows = 28.6%

## Top 20 high-confidence prescient rows (final_bucket=high, conf=3)

| row_id | score | horizon | headline | publication | date |
|---|---:|---|---|---|---|
| 104 | 5 | LH | Stratus still rock solid as it moves CISC users to RISC | Computerworld | 1992-11-02 |
| 1095 | 5 | SH-3y | "The APIs will allow application programmers to write softwa | AP |  |
| 1108 | 5 | SH-3y | "I don't see any loss of momentum for Apple," Kastner said.  | AP |  |
| 1147 | 5 | SH-3y | This build-to-order model has worked not only with PCs, but  | AP |  |
| 1148 | 5 | SH-3y | Now more than ever, said Kastner, basic business principles  |  |  |
| 1149 | 5 | SH-3y | Now more than ever, said Kastner, basic business principles  |  |  |
| 115 | 5 | SH-3y | PowerBuilder may add Intersolv tools | Computerworld | 1993-04-12 |
| 1153 | 5 | SH-3y | The much-talked-about 64-bit microprocessors coming down the | E-Commerce Times |  |
| 1154 | 5 | SH-3y | But although AMD and Intel seem to be preparing for battle,  | AP |  |
| 1186 | 5 | SH-3y | -- Peter S. Kastner | AP |  |
| 1187 | 5 | SH-3y | What is controversial about this site is shooting live game  |  |  |
| 1193 | 5 | SH-3y | That makes the introduction of dual core processors for pers |  |  |
| 1208 | 5 | SH-3y | All the major microprocessor manufacturers are drooling over | AP |  |
| 14 | 5 | SH-5y | Mini vendors adapt in order to survive | Computerworld | 1989-03-13 |
| 140 | 5 | SH-5y | Software vendors converge on database market | Computerworld | 1993-11-29 |
| 145 | 5 | SH-5y | TECHNOLOGY ON TRIAL | Computerworld | 1993-11-29 |
| 155 | 5 | SH-5y | Compaq, TI to team on fast Ethernet | Computerworld | 1994-08-15 |
| 173 | 5 | SH-5y | Technology Forecast Forecast '96 | Computerworld | 1996-01-02 |
| 28 | 5 | SH-3y | Support for open systems builds piece by piece | Computerworld | 1989-12-25 |
| 41 | 5 | SH-3y | How low can mail-order firms go? Watch'em | Computerworld | 1991-08-05 |

## Top 20 high-confidence non-prescient rows (final_bucket=low, conf=3)

| row_id | score | horizon | headline | publication | date |
|---|---:|---|---|---|---|
| 1109 | 0 | SH-3y | With PC sales making up the overwhelming majority of Apple r | AP |  |
| 1132 | 0 | SH-3y | Peter Kastner, a personal computer analyst with the Aberdeen |  |  |
| 1161 | 0 | SH-3y | In addition to supporting current versions of Microsoft Wind |  |  |
| 1163 | 0 | SH-3y | So far, Gateway has put out 45 new digital devices this year |  |  |
| 1166 | 0 | SH-3y | SanDisk (SNDK 14.89, +0.08, +0.54%) shares climbed 19 cents  | AP |  |
| 1167 | 0 | SH-3y | SanDisk (SNDK 14.89, +0.08, +0.54%) shares climbed 19 cents  | AP |  |
| 1180 | 0 | SH-3y | Peter S Kastner Blogging at oncomputerstips.blogspot.com | AP |  |
| 1200 | 0 | SH-3y | Caveat: Be sure to have your user manual so that you can get |  |  |
| 26 | 0 | SH-5y | SQL Server update boasts openness | Computerworld | 1989-10-09 |
| 50 | 0 | SH-3y | Sun will soon detail multimedia strategy | Computerworld | 1992-01-06 |
| 56 | 0 | SH-3y | AIX database stuck in lab; users express little concern | Computerworld | 1992-03-30 |
| 579 | 0 | SH-3y | Look for Mac OS X 10.4 "Tiger" | Kastner Blog |  |
| 616 | 0 | SH-3y | Software Patents Create Havoc in Eurpoe | Kastner Blog |  |
| 759 | 0 | SH-3y | IBM, Lotus iron out agreement | Computerworld | 1995-06-19 |
| 864 | 0 | SH-3y | RDBMS show they can pull OLTP weight | Computerworld | 1989-02-27 |
| 879 | 0 | SH-3y | SQL Server update boasts openness | Computerworld | 1989-10-09 |
| 880 | 0 | SH-3y | SQL Server update boasts openness | Computerworld | 1989-10-09 |
| 883 | 0 | SH-3y | Unix draws a crowd | Computerworld | 1990-03-19 |
| 884 | 0 | SH-3y | Unix draws a crowd | Computerworld | 1990-03-19 |
| 891 | 0 | SH-3y | Integration vs. specialization | Computerworld | 1990-05-07 |

## Tiebreaker flips (P1 changed verdict, 12 rows)

| row_id | P2 (b/conf) | P1 (b/conf) | final | headline |
|---|---|---|---|---|
| 1093 | medium/2 | medium/3 | medium | Even partners that don't have to rely on Informix  |
| 147 | medium/2 | medium/3 | medium | Price wars pressure low end Forecast |
| 810 | medium/2 | medium/3 | medium | Apple to answer rumors with facts |
| 1137 | medium/2 | medium/3 | medium | As the Microsoft appeal goes forward, it will be i |
| 953 | medium/2 | medium/3 | medium | NCR taps Pentium for mainframe-class servers |
| 731 | medium/2 | high/3 | high | DEC moves to VAX, Alpha mixed clusters |
| 766 | medium/2 | medium/3 | medium | DBMS tool meets demand |
| 958 | medium/2 | medium/3 | medium | USL makes microkernel move |
| 933 | medium/1 | low/2 | low | Page exits Software AG News |
| 23 | medium/2 | medium/3 | medium | DEC challenges IBM CASE strategy |
| 872 | medium/2 | high/3 | high | Tesseract, Walker to be financial software allies |
| 873 | medium/2 | high/3 | high | Tesseract, Walker to be financial software allies |