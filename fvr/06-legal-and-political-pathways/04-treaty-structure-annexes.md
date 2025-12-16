# Treaty structure & annexes

Freeze–Vote–Rebuild is easier to implement when agreements are drafted as **modular instruments**: a core text for high-level commitments, with annexes for technical detail that can be updated without reopening the entire agreement (subject to agreed procedures).

This chapter describes a recommended drafting architecture.

## Objectives

- Reduce veto points by keeping the core instrument lean.
- Make operational details precise through annexes and SOPs.
- Enable updates and learning without renegotiating everything.
- Improve auditability by clearly separating commitments from implementation procedures.

## Recommended structure

### 1) Core instrument (the “political-legal spine”)
Should contain:
- statement of objectives and principles (verification-first, sequencing)
- definitions (key terms)
- governance structure and decision rules
- verification-first gates concept and certification authority
- high-level obligations by phase (Freeze, Vote, Rebuild)
- conditional incentives and rollback logic (at principle level)
- dispute resolution authority and timelines (high level)
- entry into force / domestic approvals activation clauses
- amendment and annex-update procedures

Keep it short enough to be ratifiable and readable.

### 2) Technical annexes (detailed and operational)
Attach annexes such as:
- maps and geographic definitions
- prohibited/permitted actions list
- incident classification rubric and reporting templates
- deconfliction SOP (hotlines, liaison trees)
- corridor and protected infrastructure registers
- vote rulebook (eligibility, modalities, audits, observation)
- dispute resolution procedures (filing rules, evidence standards, remedies)
- reconstruction procurement standards and audit terms
- data governance and publication policy
- KPI definitions and dashboard specs

### 3) SOPs and playbooks (operational manuals)
These can be annexed or referenced:
- monitor deployment and security SOPs
- election worker SOPs
- reconstruction project lifecycle SOPs
- fraud response and debarment procedures

## Annex update rules (critical)

Define:
- who can propose annex updates
- what approval threshold is required
- how changes are published and versioned
- “no surprise” rules (minimum notice periods)
- emergency change procedures (rare, time-bounded, logged)
- how disputes about annex changes are adjudicated

**Design rule:** core obligations should not be alterable via annex updates; annex updates refine implementation details.

## Version-locking as a legal concept

For Vote-related procedures (and any vote-to-border algorithm if used):
- publish the version-locked rules before execution
- define a strict change-control process
- record hashes or equivalent identifiers (if appropriate) to prove integrity of versions

## Linking treaty structure to gates

Each annex should map to gates:
- Freeze annexes → Freeze stability gate indicators
- Vote annexes → Vote readiness and certification gates
- Rebuild annexes → Reconstruction tranche and integrity gates

See:
- [`05-governance-and-verification/02-verification-first-gates.md`](../05-governance-and-verification/02-verification-first-gates.md)

## Domestic approvals integration

The core instrument should include activation clauses:
- obligations activate only after certified domestic approvals
- incentives activate only when legal authority exists

See:
- [`06-legal-and-political-pathways/01-domestic-approvals-gate.md`](01-domestic-approvals-gate.md)

## Drafting note

When populating this chapter with full content, include:
- a sample table of contents for the core instrument
- a sample annex list with “owned by” and “update rule” columns
- a mapping table from annexes → verification gates → consequences
