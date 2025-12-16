# Vote-to-border mechanics (optional)

Some variants of Freeze–Vote–Rebuild include a “vote-to-border” component: a published method that maps vote outcomes to territorial or administrative lines. In this GitBook, vote-to-border is treated as an **optional module**.

If used, it must be designed to be:
- **transparent** (published rules),
- **version-locked** (no midstream changes),
- **simulatable** (public sandbox before the vote),
- **auditable** (inputs/outputs and edge cases are inspectable),
- **resistant to manipulation** (especially via strategic displacement or gerrymandering).

## Why include vote-to-border at all?

Potential benefits:
- reduces arbitrariness by committing to rules in advance,
- narrows post-vote bargaining space (fewer “interpretation wars”),
- makes tradeoffs visible before voting, not after.

Potential risks:
- creates strong incentives to manipulate turnout or eligibility,
- hard edge cases (mixed areas, security constraints, minority protections),
- may be viewed as legitimizing outcomes that should be negotiated separately.

## Core design requirements

### 1) Define the mapping unit
Specify the unit that maps votes to outcomes, e.g.:
- municipality / district / precinct
- contiguous geographic cells (grid-based)
- administrative units with defined boundaries

Avoid ad hoc redrawing during or after the vote.

### 2) Define the decision rule
Examples (illustrative only):
- simple majority by unit
- supermajority thresholds for boundary changes
- turnout-adjusted rules (high risk; can be gamed)
- multi-option outcomes with runoff rules

### 3) Define contiguity and coherence constraints
If borders are produced, specify constraints such as:
- contiguity (no isolated enclaves unless explicitly allowed)
- corridor rules for access
- treatment of mixed units (subdivision rules or shared administration options)

### 4) Define minority protections and human rights constraints
Vote-to-border must not be a “license” for rights violations. Specify:
- protections for minorities in any resultant zones
- policing/security constraints under Freeze conditions
- mechanisms for monitoring rights compliance post-result

### 5) Lock inputs and publish the algorithm
Before the vote:
- publish the full mapping algorithm and parameters
- publish the data inputs that will be used (boundaries, units, registries)
- establish a version-lock and governance process for any emergency changes
- define how disputes about inputs are handled

## The simulation/sandbox requirement

A public simulation platform should allow stakeholders to:
- test hypothetical vote distributions,
- explore edge cases (mixed units, low turnout, displaced participation),
- verify that the published rules behave as advertised,
- detect incentives for gaming.

Publish:
- code (or at minimum a deterministic spec),
- sample datasets,
- documented examples and edge-case handling,
- a change log and cryptographic hashes (if applicable) to support version-locking.

## Fraud and manipulation risks (and mitigations)

### Risk: strategic exclusion or displacement
Mitigate via:
- electorate inclusion rules with cutoffs ([`03-vote/02-electorate-definition.md`](02-electorate-definition.md))
- independent audits of registration and participation
- transparency on participation by category (resident/IDP/refugee)

### Risk: gerrymandering via unit choice
Mitigate via:
- choosing stable, pre-existing administrative units where possible
- publishing boundaries and forbidding midstream changes
- independent review of unit design

### Risk: low-turnout gaming
Mitigate via:
- cautious use of turnout thresholds (can be exploited)
- robust anti-coercion measures and access support
- explicit rules for inconclusive units (e.g., rerun, runoff, negotiated fallback)

## When not to use vote-to-border

Consider excluding this module if:
- security conditions make free participation implausible in key areas,
- displaced inclusion cannot be operationalized credibly,
- boundary consequences would create unacceptable rights risks,
- parties cannot pre-commit to rules and accept the outputs.

## Links to related chapters

- Legitimacy criteria: [`03-vote/01-objective-legitimacy-criteria.md`](01-objective-legitimacy-criteria.md)
- Electorate definition: [`03-vote/02-electorate-definition.md`](02-electorate-definition.md)
- Voting system design: [`03-vote/03-voting-system-design.md`](03-voting-system-design.md)
- Dispute resolution: [`03-vote/06-dispute-resolution.md`](06-dispute-resolution.md)
- Data governance: [`05-governance-and-verification/04-data-governance-privacy-security.md`](../05-governance-and-verification/04-data-governance-privacy-security.md)
