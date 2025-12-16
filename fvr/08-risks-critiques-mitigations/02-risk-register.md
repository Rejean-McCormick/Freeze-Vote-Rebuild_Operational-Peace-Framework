# Risk register

This page is the working risk register for Freeze–Vote–Rebuild. It is designed to be updated as the framework is refined and as stakeholders stress-test assumptions.

## How to use this register

For each risk, record:
- **ID**
- **Risk statement**
- **Phase** (Freeze / Vote / Rebuild / Cross-cutting)
- **Likelihood** (Low/Med/High)
- **Impact** (Low/Med/High)
- **Early warning indicators**
- **Mitigations**
- **Owner(s)**
- **Linked gates / triggers**
- **Response plan** (pause/rollback/remediate)

## Risk register (initial set)

### R-F1: Freeze used for regrouping
- **Phase:** Freeze
- **Likelihood:** Med
- **Impact:** High
- **Early indicators:** unusual redeployments; spikes in restricted movements; pattern of “minor” violations
- **Mitigations:** explicit movement limits; monitoring of redeployments; recurrence tracking
- **Owner:** Monitoring mission + governance council
- **Linked gates:** Freeze stability gate thresholds (S3/S4 + movement indicators)
- **Response:** pause incentives; targeted inspections; escalation ladder level-up

### R-F2: Monitor obstruction
- **Phase:** Freeze
- **Likelihood:** Med
- **Impact:** High
- **Early indicators:** denied site visits; delayed access; intimidation reports
- **Mitigations:** obstruction treated as high-severity; automatic consequences; redundant technical verification
- **Owner:** Governance council + monitoring mission
- **Linked gates:** monitor access indicator in Freeze gates
- **Response:** immediate gate failure review; pause/rollback tier; publish obstruction findings

### R-F3: Corridor weaponization
- **Phase:** Freeze
- **Likelihood:** Med
- **Impact:** High
- **Early indicators:** frequent closures; selective access; coercion allegations
- **Mitigations:** corridor uptime KPI; rapid adjudication; explicit prohibition of coercive use
- **Owner:** Humanitarian coordination + monitors
- **Linked gates:** humanitarian access gate
- **Response:** investigation within deadline; consequences for recurrence

### R-V1: Coercion and intimidation distort Vote
- **Phase:** Vote
- **Likelihood:** Med
- **Impact:** High
- **Early indicators:** threats, turnout anomalies, clustered complaints, observer obstruction
- **Mitigations:** anti-coercion package; observer coverage; rerun triggers; protected reporting
- **Owner:** Vote administration + observers + dispute panel
- **Linked gates:** Vote integrity/certification gate
- **Response:** invalidate/rerun compromised areas; extend voting window if needed

### R-V2: Displaced people excluded
- **Phase:** Vote
- **Likelihood:** Med
- **Impact:** High
- **Early indicators:** low displaced registration; high rejection rates; access barriers
- **Mitigations:** explicit displaced categories; proof ladders; expanded registration centers; appeals
- **Owner:** Vote administration + civil society support
- **Linked gates:** Vote readiness gate (roll completeness + inclusion metrics)
- **Response:** extend registration; deploy extra centers; reopen appeals window

### R-V3: Cyber compromise (digital components)
- **Phase:** Vote
- **Likelihood:** Med
- **Impact:** High
- **Early indicators:** outages, integrity alerts, intrusion reports, unexplained anomalies
- **Mitigations:** audit-first design; offline fallback; independent testing; segmented systems
- **Owner:** Vote administration + independent security auditors
- **Linked gates:** Vote readiness gate; Vote integrity gate
- **Response:** switch to fallback mode; isolate systems; independent investigation

### R-V4: Disputes drag on and delegitimize outcome
- **Phase:** Vote
- **Likelihood:** Med
- **Impact:** High
- **Early indicators:** backlog growth; missed deadlines; refusal to comply with remedies
- **Mitigations:** strict timelines; limited appeal grounds; publish reasoned decisions
- **Owner:** Dispute resolution panel
- **Linked gates:** certification gate deadlines
- **Response:** enforce deadlines; apply remedies; escalate noncompliance via governance ladder

### R-R1: Reconstruction capture/corruption
- **Phase:** Rebuild
- **Likelihood:** Med
- **Impact:** High
- **Early indicators:** sole-source spikes; repeated change orders; vendor concentration; audit flags
- **Mitigations:** transparency stack; independent audits; debarment; milestone-based payments
- **Owner:** Reconstruction authority + auditors
- **Linked gates:** reconstruction tranche/integrity gate
- **Response:** suspend tranche; debar vendors; replace operators; remediation plan

### R-R2: Rebuild too slow to stabilize conditions
- **Phase:** Rebuild
- **Likelihood:** Med
- **Impact:** Med/High
- **Early indicators:** project pipeline stagnation; procurement delays; low throughput KPIs
- **Mitigations:** standardized templates; performance incentives; bottleneck tasking
- **Owner:** Reconstruction authority
- **Linked gates:** delivery KPIs in tranche gates
- **Response:** re-sequence pipeline; adjust incentives; increase capacity

### R-X1: Incentives not deliverable due to domestic legal limits
- **Phase:** Cross-cutting
- **Likelihood:** Med
- **Impact:** High
- **Early indicators:** legislative resistance; lack of authority for promised actions
- **Mitigations:** domestic approvals gate; activation clauses; publish feasible ladder only
- **Owner:** guarantor states + legal teams
- **Linked gates:** domestic approvals gate
- **Response:** revise incentive schedule; delay activation; renegotiate commitments

### R-X2: Governance paralysis or capture
- **Phase:** Cross-cutting
- **Likelihood:** Med
- **Impact:** High
- **Early indicators:** deadlock; unexplained decision delays; transparency suppression
- **Mitigations:** balanced composition; deadlock-breaking rules; independent publication rights
- **Owner:** governance council + oversight board
- **Linked gates:** governance performance indicators (timeliness, transparency)
- **Response:** invoke deadlock rules; external arbitration; restructure governance

### R-X3: Data breach / privacy failure
- **Phase:** Cross-cutting
- **Likelihood:** Med
- **Impact:** High
- **Early indicators:** unauthorized access logs; leaks; intimidation after disclosures
- **Mitigations:** minimization; role-based access; encryption; secure audit rooms
- **Owner:** data stewards + security teams
- **Linked gates:** data governance compliance checks
- **Response:** incident response; system pause; independent investigation; remediation

## Maintenance

- Add new risks as they emerge during stakeholder review.
- Update likelihood/impact as conditions change.
- Record major mitigation decisions in the **Decision log** ([`11-appendices/03-decision-log.md`](../11-appendices/03-decision-log.md)).
