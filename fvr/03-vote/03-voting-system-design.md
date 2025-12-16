# Integrity & observation

The Vote phase must be credible under adversarial conditions. This chapter defines the integrity safeguards and observation architecture required to make outcomes defensible.

## Objectives

- Prevent or deter coercion, fraud, and manipulation.
- Provide independent evidence about process integrity.
- Detect anomalies early enough to correct them.
- Create a record that can withstand post-result contestation.

## Integrity threats (baseline assumptions)

Design should assume:
- intimidation and retaliation threats against voters and officials,
- administrative manipulation (selective exclusion, “missing” registrants),
- disinformation and fabricated incident claims,
- cyber attacks on registration, reporting, or tabulation systems,
- physical disruption of polling and transport.

## Observation mission: requirements

An observation mission must have:

### 1) Independence
- governance that prevents capture
- funding and logistics that avoid single-party dependence

### 2) Access
- freedom to visit polling sites, counting sites, and registration centers
- ability to interview stakeholders without intimidation
- access to key documents and procedures (within privacy limits)

### 3) Coverage and sampling plan
- deployment coverage targets (e.g., % of sites covered)
- statistically meaningful sampling where full coverage is impossible
- explicit monitoring of high-risk areas and displaced voting sites

### 4) Reporting authority
- right to publish findings on a defined schedule
- ability to flag urgent integrity concerns in real time
- transparent methodology disclosures (what was observed, how, and limitations)

### 5) Coordination with security and monitoring systems
- channels to report threats and intimidation incidents
- integration with Freeze monitoring when violence affects voting safety

## Anti-coercion package (minimum)

A credible anti-coercion design includes:
- secret ballot protections (procedural and physical)
- safeguards against “supervised voting” by coercers
- protections for election workers and observers
- rapid response for intimidation claims (hotline + investigation)
- safe reporting mechanisms for vulnerable groups
- rules for invalidating or re-running compromised precincts

Track coercion with:
- complaint volume and category breakdown
- geographic clustering of threats
- incident severity and recurrence
- correlation with turnout anomalies (as a flag)

## Audit and integrity checks (minimum)

Even with observers, you need auditability:

- chain-of-custody documentation for ballots/records
- reconciliation checks (issued vs returned vs counted)
- risk-limiting audit or defined recount triggers
- independent review of tabulation software (if used)
- logs that are tamper-evident and time-stamped (where feasible)

## Transparency: what should be published

Publish, at minimum:
- rulebook and procedures (version-locked)
- observer mission methodology and reports
- aggregate participation and turnout statistics
- incident and complaint summaries (privacy-protected)
- audit results and reconciliation summaries
- final results with clear aggregation logic

Keep restricted:
- personally identifiable voter data
- information that increases physical security risk
- sensitive cyber defense details

(See [`05-governance-and-verification/04-data-governance-privacy-security.md`](../05-governance-and-verification/04-data-governance-privacy-security.md).)

## Integration with dispute resolution

Integrity findings must have procedural consequences:
- observer flags can trigger investigations
- defined thresholds trigger recounts or reruns
- timelines are enforced to prevent indefinite contestation

See: [`03-vote/06-dispute-resolution.md`](06-dispute-resolution.md).

## Links to related chapters

- Voting system design: [`03-vote/03-voting-system-design.md`](03-voting-system-design.md)
- Dispute resolution: [`03-vote/06-dispute-resolution.md`](06-dispute-resolution.md)
- Freeze monitoring linkages (safety and access): [`02-freeze/03-verification-monitoring.md`](../02-freeze/03-verification-monitoring.md)
- Governance and escalation: [`05-governance-and-verification/03-coordination-deconfliction-escalation.md`](../05-governance-and-verification/03-coordination-deconfliction-escalation.md)
