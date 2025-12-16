# Verification-first gates

Verification-first gates are the control mechanism of Freeze–Vote–Rebuild. They define measurable criteria that must be met to:
- advance from one phase to the next,
- unlock conditional incentives (aid, sanctions adjustments, funding tranches),
- trigger pauses or rollbacks when compliance fails.

This chapter provides a template for gate design.

## Design principles for gates

A good gate is:
- **measurable** (or independently attestable),
- **time-bounded** (measured over a defined window),
- **multi-indicator** (harder to game),
- **linked to consequences** (advance/pause/rollback),
- **auditable** (evidence can be reviewed independently).

Avoid gates based on intent, rhetoric, or vague “good faith.”

## Gate taxonomy

### Phase gates (macro)
Determine progression:
- Pre-Freeze → Freeze
- Freeze → Vote
- Vote → Rebuild (scale)

### Benefit gates (micro)
Determine incremental unlocks within phases:
- corridor expansion
- licensing/waivers
- reconstruction tranche releases
- expanded access arrangements

## Template: define each gate in a standard format

For each gate, specify:

1. **Name and purpose**
2. **Indicators** (what is measured)
3. **Thresholds** (numeric or categorical)
4. **Measurement window** (e.g., rolling 14 days)
5. **Data sources** (monitors, sensors, audits, observers)
6. **Decision authority** (who certifies)
7. **Consequences** (advance/pause/rollback; what exactly changes)
8. **Appeal/dispute process** (how contested determinations are handled)
9. **Publication policy** (what is reported publicly)

## Example gates (illustrative)

### Gate A: Freeze Stability Gate
**Purpose:** verify the ceasefire is holding well enough to begin Vote preparation.

Indicators (examples):
- count of high-severity incidents (S3/S4) per week
- civilian harm incidents and protected infrastructure strikes
- monitor access denials / obstruction events
- corridor uptime

Thresholds (examples):
- S3/S4 incidents below agreed threshold for 14 days
- zero (or near-zero) protected infrastructure strikes at S4/C3
- no unresolved monitor obstruction events
- corridor uptime above agreed minimum

Consequences:
- authorize Vote operational rollout (registration, observer deployment)
- unlock defined incentive tier (if ladder is used)

---

### Gate B: Vote Readiness Gate
**Purpose:** confirm the Vote can occur safely and credibly.

Indicators (examples):
- observer mission deployed to target coverage
- voter roll publication complete + appeal window processed
- anti-coercion hotline functioning and staffed
- cybersecurity readiness checks complete (if digital components exist)

Consequences:
- authorize opening of voting window

---

### Gate C: Vote Integrity Gate (Certification Gate)
**Purpose:** determine whether results can be certified.

Indicators (examples):
- observer integrity assessment meets agreed standard
- audit results within tolerance thresholds
- dispute caseload resolved within timelines
- no unresolved systemic coercion findings

Consequences:
- certify results and unlock Rebuild scaling tier
- if failed: reruns/recounts in defined areas or fallback mechanism

---

### Gate D: Reconstruction Integrity Gate (Tranche Gate)
**Purpose:** release reconstruction funds only when governance and delivery remain clean.

Indicators (examples):
- audit findings below threshold
- % payments tied to verified milestones
- procurement compliance rate
- debarment enforcement functioning
- KPI performance within expected bands

Consequences:
- release tranche / expand project pipeline
- if failed: suspend disbursement, initiate remediation, replace operators if necessary

## Gaming resistance: multi-indicator design

To reduce gaming:
- use multiple indicators across security, access, and integrity
- track recurrence and patterns, not just counts
- include “obstruction” as a high-severity indicator
- require independent corroboration for major events
- audit the monitors (meta-verification)

## Governance integration

Gates rely on governance bodies to:
- certify compliance based on evidence,
- adjudicate contested findings,
- enforce consequences.

See:
- governance model: [`05-governance-and-verification/01-status-neutral-governance-model.md`](01-status-neutral-governance-model.md)
- escalation ladder: [`05-governance-and-verification/03-coordination-deconfliction-escalation.md`](03-coordination-deconfliction-escalation.md)

## Drafting note

When the book is populated with full content, this page should include:
- a single table listing all gates, indicators, thresholds, windows, and consequences,
- clear mapping to the incentives ladder in [`02-freeze/05-sanctions-aid-linkage-during-freeze.md`](../02-freeze/05-sanctions-aid-linkage-during-freeze.md),
- links to KPI definitions in [`09-implementation-toolkit/03-metrics-kpis.md`](../09-implementation-toolkit/03-metrics-kpis.md).
