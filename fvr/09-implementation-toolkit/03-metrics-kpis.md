# Metrics & KPIs

Freeze–Vote–Rebuild is verification-first: progress depends on measurable indicators. This chapter lists suggested metrics and KPIs to support gates, dashboards, and accountability.

These are not all mandatory. The intent is to provide a menu with a recommended “minimum viable set.”

## Principles for KPI design

- Prefer **multi-indicator** sets (harder to game).
- Track **trends** over windows (7/14/30 days), not single-day spikes.
- Separate **leading indicators** (early warnings) from **lagging indicators** (outcomes).
- Publish aggregates where feasible; restrict sensitive details.

## Freeze KPIs

### Security and incidents
- **High-severity incident rate (S3/S4)** per week
- **Total incident rate** by category (shelling, UAV, movement violations)
- **Civilian casualty events** (count; severity)
- **Protected infrastructure strikes** (count; severity/confidence)
- **Recurrence index** (repeat violations by sector/unit over time)

### Access and obstruction
- **Monitor access denial count** (and duration)
- **Mean time to incident site access**
- **Humanitarian corridor uptime** (% hours open)
- **Aid convoy disruption events** (count; severity)

### Stabilization outcomes (proxy)
- **Power/water service uptime** in key regions (%)
- **Mean time to repair** for critical outages (hours/days)
- **Displacement flow rate** (new displacement events; where measurable)

## Vote KPIs

### Inclusion and participation
- **Registration completion rate** by category (resident / IDP / refugee)
- **Rejection rate** and **appeal success rate**
- **Turnout** overall and by category (aggregate)
- **Polling/center uptime** (% open as scheduled)

### Integrity and safety
- **Coercion/intimidation complaint rate** (per 10,000 registrants)
- **Observer coverage rate** (% sites observed; sampling coverage)
- **Chain-of-custody exceptions** (count and severity)
- **Reconciliation error rate** (issued vs returned vs counted discrepancies)

### Audit outcomes
- **Audit discrepancy rate** (within tolerance vs action-required)
- **Recount/rerun triggers activated** (count; reason)
- **Dispute resolution timeliness** (% resolved within deadlines)

## Rebuild KPIs

### Delivery throughput
- **Projects started/completed** per month (by category/region)
- **Time-to-mobilize** (award → mobilization)
- **On-time milestone rate** (% milestones hit)
- **Service restored** (MW restored, households rehoused, beds/clinic capacity, school seats)

### Cost and efficiency
- **Cost variance vs benchmark** (%)
- **Change order rate** (% of contract value; count)
- **Unit cost** benchmarks (e.g., cost per km road repaired; per classroom rebuilt)

### Integrity and transparency
- **% payments tied to verified milestones**
- **Competitive procurement rate** (% competitive vs emergency)
- **Audit finding rate** (major/minor) and **remediation completion rate**
- **Debarments issued and enforced** (count; time to enforce)
- **Vendor concentration index** (risk indicator for capture)

### Equity and legitimacy proxies
- **Geographic distribution** of projects vs stated criteria
- **Community grievance rate** and resolution timeliness
- **User satisfaction proxy** (where measurable)

## Cross-cutting KPIs

### Governance performance
- **Time to adjudicate incidents/disputes** (median; % within deadlines)
- **Publication timeliness** (reports released on schedule)
- **Deadlock rate** (governance decisions delayed beyond thresholds)

### Data governance
- **Security incidents** (attempts and confirmed breaches)
- **Unauthorized access events** (count)
- **Redaction exceptions** (count; justification)

## Minimum viable KPI set (recommended)

If you must start small, track:
- Freeze: S3/S4 incident rate, monitor obstruction count, corridor uptime
- Vote: registration rates by category, coercion complaint rate, observer coverage, audit discrepancy rate
- Rebuild: % milestone-verified payments, audit finding rate, projects completed/month, cost variance vs benchmark

## Link to gates

KPIs feed gate thresholds:
- [`05-governance-and-verification/02-verification-first-gates.md`](../05-governance-and-verification/02-verification-first-gates.md)

## Drafting note

When implementing, define for each KPI:
- exact definition,
- data source and collection method,
- update cadence,
- publication policy,
- owner and audit access rules.
