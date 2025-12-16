# Failure modes

This chapter lists the most important ways Freeze–Vote–Rebuild can fail, grouped by phase and by cross-cutting system. Each failure mode should eventually be linked to mitigations, owners, and gates in the risk register.

## Phase-specific failure modes

## Freeze failure modes

### FM-F1: “Freeze as cover for regrouping”
- Ceasefire reduces fighting but enables repositioning or rearmament.
**Mitigations:**
- explicit movement and posture rules in ceasefire architecture
- monitoring focused on redeployments and prohibited activity
- gate thresholds that include recurrence and pattern detection

### FM-F2: Monitor obstruction and intimidation
- Access denied or monitors threatened; reporting becomes toothless.
**Mitigations:**
- obstruction treated as high-severity incident
- automatic consequences tied to obstruction
- redundant technical verification where feasible

### FM-F3: Ambiguity-driven escalation
- Vague terms lead to repeated incidents and retaliatory cycles.
**Mitigations:**
- enumerated prohibited/permitted actions
- standardized incident classification rubric with confidence levels
- time-bounded adjudication and escalation ladder

### FM-F4: Humanitarian corridors become political hostages
- Corridors are closed or used coercively.
**Mitigations:**
- corridor uptime metrics and automatic review triggers
- observation and rapid dispute resolution for closures
- explicit prohibition of coercive use

## Vote failure modes

### FM-V1: Coercion and intimidation distort participation
- Voters and officials face threats; outcome becomes illegitimate.
**Mitigations:**
- anti-coercion package (hotlines, protections, observer access)
- defined triggers for reruns/invalidations
- integration with Freeze monitoring for safety incidents

### FM-V2: Displaced people excluded (de facto electorate manipulation)
- Eligibility rules or logistics prevent displaced participation.
**Mitigations:**
- explicit displaced categories with accessible registration pathways
- proof ladders and appeals
- participation metrics by category published in aggregate

### FM-V3: Digital/cyber compromise (if digital components exist)
- Registration or tabulation systems are attacked or mistrusted.
**Mitigations:**
- audit-first design with independent verifiable records
- offline fallbacks and redundancy
- independent security testing and incident response

### FM-V4: Post-result contestation without closure
- Disputes drag on, undermining legitimacy and triggering escalation.
**Mitigations:**
- strict timelines for complaints and appeals
- enforceable remedies
- fixed certification deadline with defined exceptions

### FM-V5: Vote-to-border gaming (if used)
- Rule design creates incentives to manipulate turnout, units, or eligibility.
**Mitigations:**
- pre-published, version-locked algorithm
- public simulation sandbox
- stable mapping units and anti-gerrymandering constraints

## Rebuild failure modes

### FM-R1: Corruption/capture collapses legitimacy
- Funds diverted; procurement politicized; donor confidence collapses.
**Mitigations:**
- independent audits, debarment authority, transparency stack
- tranche releases tied to integrity KPIs
- anomaly detection and spot checks

### FM-R2: Slow delivery undermines the “peace dividend”
- Reconstruction is too slow to stabilize politics and lives.
**Mitigations:**
- standardized project templates and procurement
- performance incentives (Reconstruction Olympics)
- bottleneck management and KPIs

### FM-R3: Unequal distribution fuels grievance
- Perceived favoritism or neglect triggers political backlash.
**Mitigations:**
- published prioritization criteria
- equity monitoring in dashboards
- grievance mechanisms for communities

## Cross-cutting failure modes

### FM-X1: Incentives not credible (domestic legal limits)
- Promised sanctions relief or funding cannot be delivered.
**Mitigations:**
- domestic approvals gate and activation clauses
- staged incentives with clear legal prerequisites
- publish what is legally feasible, not aspirational

### FM-X2: Governance capture or paralysis
- Decision bodies are captured or deadlocked.
**Mitigations:**
- balanced governance structure, rotating terms
- defined quorum and deadlock-breaking rules
- independent audit and publication rights

### FM-X3: Data governance failures
- Privacy breaches or security leaks endanger people and discredit the process.
**Mitigations:**
- role-based access and minimization
- secure audit rooms for raw data access
- clear publication/redaction policy

### FM-X4: Spoilers escalate violence to collapse the process
- Actors (internal or external) sabotage gates intentionally.
**Mitigations:**
- resilience through redundancy and rapid incident response
- predictable escalation ladder and rollback logic
- public reporting that reduces narrative manipulation

## Next

Translate these failure modes into a structured table with owners and triggers:
- [`08-risks-critiques-mitigations/02-risk-register.md`](02-risk-register.md)
