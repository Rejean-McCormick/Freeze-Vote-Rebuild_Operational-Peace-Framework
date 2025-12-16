# Ceasefire architecture

This chapter outlines a ceasefire design that supports **verification-first** implementation. It is written as a structure (what must be specified) rather than a final legal text.

## Design goals

A ceasefire architecture should:
- be **unambiguous** (who, where, what actions stop),
- be **verifiable** (observable indicators, reporting rules),
- reduce **accidental escalation** (deconfliction),
- include **enforcement logic** (what happens after violations),
- be **modular** (core text + annexes/SOPs).

## Minimum clauses to specify

### 1) Scope and geography
- defined area of application (front line, buffer zones, airspace)
- mapping reference (agreed map annex and coordinates)
- rules for disputed or unclear sectors (temporary administration rules)

### 2) Prohibited and permitted actions
Prohibited actions should be enumerated, not implied. Typical categories:
- offensive ground advances
- artillery/rocket strikes (define calibers/ranges where relevant)
- drone strikes and UAV operations (define types and permitted uses)
- air operations (define no-fly zones or flight corridors)
- mining, sabotage, or strikes on critical infrastructure

Permitted actions should also be explicit:
- defensive posture maintenance
- medical evacuation and casualty retrieval
- humanitarian operations
- monitored repair work on protected infrastructure

### 3) Force posture and movement rules
- limits on redeployments near the line
- heavy weapons pullback zones (if used)
- rules for rotations and resupply
- notification requirements for permitted movements

### 4) Reporting and notification
- required reporting intervals (daily/weekly)
- incident reporting format and deadlines
- advance notification requirements for specified activities (repairs, convoys)

### 5) Compliance measurement and baselines
- establish baseline indicators (e.g., average daily incidents, civilian harm metrics)
- define measurement windows (rolling 7-day, 14-day)
- specify what constitutes a “major violation” vs “minor incident”

### 6) Incident response and escalation ladder
- immediate deconfliction steps (hotline)
- time-bounded investigation steps (monitor access, evidence preservation)
- consequences tied to severity and recurrence
- dispute resolution mechanism for contested findings

### 7) Access and protections
- monitor freedom of movement (including inspections where agreed)
- humanitarian access and corridor protections
- protected infrastructure definitions and repair window rules

## Annexes that should be pre-written

To avoid vague commitments, attach operational annexes:
- **Annex A:** maps/coordinates, lines and zones
- **Annex B:** prohibited/permitted actions list (with definitions)
- **Annex C:** incident reporting template + classification rubric
- **Annex D:** deconfliction SOP (hotlines, liaison structure)
- **Annex E:** humanitarian corridor map + rules
- **Annex F:** protected infrastructure list + repair protocols
- **Annex G:** verification data handling and publication policy

## Common failure modes (and design mitigations)

- **Ambiguity loopholes:** mitigate by enumerating permitted/prohibited actions.
- **“Weapon type” disputes:** mitigate by defining categories with measurable criteria.
- **Propaganda-driven escalation:** mitigate with standardized incident grading and transparent reporting.
- **Monitor obstruction:** mitigate with explicit access clauses and automatic consequences.

## Links to related chapters

- Monitoring and incident grading details: [`02-freeze/03-verification-monitoring.md`](03-verification-monitoring.md)
- Deconfliction system design: [`05-governance-and-verification/03-coordination-deconfliction-escalation.md`](../05-governance-and-verification/03-coordination-deconfliction-escalation.md)
- Conditional incentives: [`02-freeze/05-sanctions-aid-linkage-during-freeze.md`](05-sanctions-aid-linkage-during-freeze.md)
