# Verification & monitoring

The Freeze phase depends on credible verification. This chapter defines what must be monitored, how incidents are classified, and how information becomes actionable.

## Goals

Verification and monitoring should:
- make major violations **hard to deny**,
- reduce escalation driven by ambiguity and misinformation,
- support conditional incentives (“gates”),
- protect civilians and humanitarian operations.

## What to monitor (minimum set)

### 1) Kinetic activity
- shelling/strike incidents (time, location, type)
- drone/UAV activity (where restricted)
- troop or heavy equipment movements (where restricted)
- air activity (where restricted)

### 2) Civilian harm and protected infrastructure
- civilian casualties and mass-casualty events
- strikes on protected sites (power, water, hospitals, schools)
- damage to corridors and repair sites

### 3) Access and obstruction
- monitor access denials
- interference or intimidation incidents
- corridor closures and aid delays

### 4) Disinformation indicators (operational, not rhetorical)
- fabricated incident reports
- manipulated imagery claims
- systematic denial of verifiable events

## Data sources (menu)

A robust monitoring design uses multiple sources:
- field observer reports (with secure comms)
- hotline and liaison reports
- sensor networks where feasible (acoustic, radar, UAV monitoring)
- satellite imagery and open-source verification (as appropriate)
- humanitarian/medical reporting channels (protected, privacy-aware)

The architecture should assume adversarial conditions and require corroboration for major claims.

## Incident reporting workflow

A minimal workflow:
1. **Intake** (hotline, observer report, sensor trigger)
2. **Triage** (severity/urgency; immediate deconfliction if needed)
3. **Verification** (site visit, sensor confirmation, cross-source checks)
4. **Classification** (apply rubric; record confidence level)
5. **Adjudication** (contested cases go through dispute mechanism)
6. **Publication/notification** (per reporting policy and security constraints)
7. **Consequence** (trigger escalation ladder or gate rollback if thresholds crossed)

## Incident classification (example rubric)

Classification should be standardized, predictable, and time-bounded.

### Severity (S)
- **S1 Minor:** isolated small-arms or low-impact incident; no civilian harm
- **S2 Serious:** clear violation with material effect; limited civilian risk
- **S3 Major:** significant attack, repeated pattern, or high-risk action
- **S4 Critical:** mass-casualty event, strike on protected infrastructure, or deliberate escalation

### Confidence (C)
- **C1 Low:** single-source or unverified claim
- **C2 Medium:** partial corroboration
- **C3 High:** multi-source corroboration / verified observation

### Recurrence (R)
- tracking repeated violations over time to detect patterns and intent

This rubric allows “S3/C3” style reporting that is legible to stakeholders and supports gate thresholds.

## Dashboards and reporting

### Public-facing transparency (where feasible)
- aggregate incident counts by category and severity
- protected infrastructure incidents
- access denials and corridor disruptions
- rolling trend lines (7/14/30 days)

### Restricted reporting (where necessary)
- precise unit locations, sensitive sensor placements
- protected personal data (witnesses, victims)
- tactical details that could enable targeting

The book’s default preference is: publish as much as possible without creating new security risks.

## Verification gates linkage

Monitoring outputs feed verification gates:
- “Freeze stability gate” might require sustained low S3/S4 incidents and full monitor access.
- “Humanitarian gate” might require corridor uptime and repair window compliance.

Gate definitions live in:
- [`05-governance-and-verification/02-verification-first-gates.md`](../05-governance-and-verification/02-verification-first-gates.md)

## Common failure modes and mitigations

- **Gaming the metrics:** mitigate by tracking multiple indicators and recurrence patterns.
- **Access denial:** mitigate with automatic consequences tied to obstruction.
- **Data poisoning:** mitigate with multi-source corroboration and chain-of-custody.
- **Over-classification secrecy:** mitigate with a clear publication policy and independent audit.

## Next
- Protected infrastructure and repair windows: [`02-freeze/04-humanitarian-corridors-protected-infrastructure.md`](04-humanitarian-corridors-protected-infrastructure.md)
- Escalation ladder and dispute handling: [`05-governance-and-verification/03-coordination-deconfliction-escalation.md`](../05-governance-and-verification/03-coordination-deconfliction-escalation.md)
