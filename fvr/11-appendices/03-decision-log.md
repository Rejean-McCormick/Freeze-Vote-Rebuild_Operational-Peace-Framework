# Decision log

This log records editorial and design decisions made while consolidating multiple drafts into a single GitBook. The goal is traceability: reviewers should be able to see what was chosen, what was deferred, and why.

## How to use this log

For each decision, record:
- **ID**
- **Date**
- **Decision**
- **Rationale**
- **Alternatives considered**
- **Impact (what changed)**
- **Where reflected in the book**
- **Source inputs affected**

## Decisions (initial set)

### D-001 — Canonical structure: Freeze → Vote → Rebuild
- **Date:** (to fill)
- **Decision:** Adopt Freeze–Vote–Rebuild as the canonical three-phase structure.
- **Rationale:** Most drafts share this skeleton; it supports sequencing and verification-first gating.
- **Alternatives:** Freeze-only; Freeze + negotiations; Rebuild-first narratives.
- **Impact:** All core content organized into `02-freeze/`, `03-vote/`, `04-rebuild/`.
- **Where:** entire ToC; [`01-proposal-at-a-glance/00-the-proposal-at-a-glance.md`](../01-proposal-at-a-glance/00-the-proposal-at-a-glance.md).

### D-002 — Status-neutral framing in the core chapters
- **Date:** (to fill)
- **Decision:** Keep the core mechanism status-neutral; move advocacy language to essays.
- **Rationale:** Neutrality improves reviewability and reduces misinterpretation as a predetermined settlement.
- **Alternatives:** Embed political framing into core text.
- **Impact:** Created `10-background-and-essays/` and “What this is not.”
- **Where:** [`01-proposal-at-a-glance/04-what-this-is-not.md`](../01-proposal-at-a-glance/04-what-this-is-not.md), `10-background-and-essays/`.

### D-003 — Verification-first gates as the control mechanism
- **Date:** (to fill)
- **Decision:** Treat gates as the controlling logic for progression and incentives.
- **Rationale:** Reduces reliance on trust and makes conditionality auditable.
- **Alternatives:** Narrative sequencing without formal gates; ad hoc certification.
- **Impact:** Added dedicated gates chapter and references across phases.
- **Where:** [`05-governance-and-verification/02-verification-first-gates.md`](../05-governance-and-verification/02-verification-first-gates.md).

### D-004 — Vote-to-border is optional, not required
- **Date:** (to fill)
- **Decision:** Include vote-to-border as an optional module with strict safeguards.
- **Rationale:** Some drafts use it; others do not. Making it optional preserves flexibility and reduces misuse risk.
- **Alternatives:** Require vote-to-border; exclude it entirely.
- **Impact:** Created module with simulation/version-lock requirements.
- **Where:** [`03-vote/05-vote-to-border-mechanics.md`](../03-vote/05-vote-to-border-mechanics.md).

### D-005 — Displaced persons inclusion is a hard requirement
- **Date:** (to fill)
- **Decision:** Treat displaced/refugee inclusion as a core legitimacy requirement.
- **Rationale:** Exclusion creates incentives for displacement and undermines legitimacy.
- **Alternatives:** Current-residents-only electorate; symbolic inclusion without enforceable metrics.
- **Impact:** Built explicit electorate categories and metrics expectations.
- **Where:** [`03-vote/02-electorate-definition.md`](../03-vote/02-electorate-definition.md).

### D-006 — Reconstruction governance must be auditable by design
- **Date:** (to fill)
- **Decision:** Require transparency stack, audits, and tranche gating in Rebuild.
- **Rationale:** Capture/corruption is a dominant failure mode; auditable design is required for durability.
- **Alternatives:** High-trust reconstruction; minimal transparency.
- **Impact:** Added accountability chapter, templates, and KPI linkages.
- **Where:** [`04-rebuild/05-accountability-transparency.md`](../04-rebuild/05-accountability-transparency.md), `09-implementation-toolkit/`.

### D-007 — “Peace-build campus” treated as optional model
- **Date:** (to fill)
- **Decision:** Preserve symbolic/patronage governance concept as optional, not canonical.
- **Rationale:** High variance in feasibility and acceptance; useful for outreach but risky as a requirement.
- **Alternatives:** Make it central; remove entirely.
- **Impact:** Kept as optional governance model.
- **Where:** [`04-rebuild/03-peace-build-campus-governance.md`](../04-rebuild/03-peace-build-campus-governance.md).

### D-008 — Advocacy essays preserved separately
- **Date:** (to fill)
- **Decision:** Preserve American realism and Papal-origin framings as essays outside the core.
- **Rationale:** Valuable for stakeholder persuasion; should not contaminate neutral spec.
- **Alternatives:** Merge into core; discard.
- **Impact:** Created Background & essays section.
- **Where:** `10-background-and-essays/`.

### D-009 — Data governance treated as a first-class constraint
- **Date:** (to fill)
- **Decision:** Add explicit data governance, privacy, and security chapter.
- **Rationale:** Voting and monitoring data can endanger people and delegitimize the process if mishandled.
- **Alternatives:** Implicit data handling; ad hoc redactions.
- **Impact:** Added role-based access and publication policy structure.
- **Where:** [`05-governance-and-verification/04-data-governance-privacy-security.md`](../05-governance-and-verification/04-data-governance-privacy-security.md).

## Maintenance note

- Add new decisions whenever the canonical mechanism changes or a major option is added/removed.
- Keep IDs stable; do not renumber.
- If a decision reverses a previous one, reference the earlier ID explicitly.
