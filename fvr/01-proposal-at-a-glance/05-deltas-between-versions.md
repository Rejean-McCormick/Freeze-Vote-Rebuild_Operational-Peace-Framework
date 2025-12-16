# Deltas between versions

This GitBook consolidates several drafts/variants of the **Freeze–Vote–Rebuild (FVR)** concept into one maintainable, reviewable structure. This page explains how they differ, what is considered “mainline” in the book, and where variant material is preserved.

## Why this page exists

The source materials differ in:
- **audience** (operators vs policymakers vs persuasion),
- **level of detail** (high-level concept vs implementable steps),
- **tone and framing** (neutral mechanism design vs advocacy narrative),
- **governance/legal specifics** (some drafts propose particular institutions; others stay option-based).

To keep the GitBook coherent, this book:
- maintains a **single core narrative** (Freeze → Vote → Rebuild),
- treats certain elements as **options** rather than commitments,
- preserves variant text in **Background and essays** and **Appendices**.

## The inputs (high-level characterization)

### A) “Comprehensive proposal” (neutral, verification-first)
**What it is:** the broadest statement of the concept.  
**Strengths:** readable end-to-end narrative; big-picture architecture; clear three-phase framing.  
**Typical gaps:** fewer implementation checklists; less explicit on institutional/legal gating; details sometimes presented conceptually rather than operationally.

### B) “v4 — Operational Peace Framework”
**What it is:** an implementation-leaning variant intended to be actionable.  
**Strengths:** sequencing discipline; “immediate actions”; clearer governance/approval logic; more concrete operational components.  
**Typical gaps:** may over-specify institutions; may read like a memo rather than a public explainer.

### C) “McCormick-style off-ramp” essay (US realist framing)
**What it is:** persuasion-first narrative aimed at an American realism audience.  
**Strengths:** strong argumentation and political framing; useful for stakeholder buy-in.  
**Typical gaps:** not a spec; fewer auditable details; may simplify operational constraints.

### D) “Projet du Pape François…” (French variant / origin framing)
**What it is:** an alternate framing that emphasizes a particular moral/diplomatic posture.  
**Strengths:** distinctive narrative and “why” framing; helpful for historical/ideological provenance.  
**Typical gaps:** contains rhetorical or institutional proposals that may not be feasible or universally acceptable; not written as a neutral operational design.

## What is “canonical” in this GitBook

**Canonical** means: “the maintained, reconciled version used for review and iteration.”

Canonical content lives in:
- `02-freeze/`
- `03-vote/`
- `04-rebuild/`
- cross-cutting enablers: `05-governance-and-verification/` and `06-legal-and-political-pathways/`

Non-canonical (preserved as context) lives in:
- `10-background-and-essays/` (advocacy narratives, variants)
- [`11-appendices/04-source-text-archive.md`](../11-appendices/04-source-text-archive.md) (reference-only originals)

## Delta summary by theme

### 1) Sequencing and “gates”
- **Comprehensive**: presents sequencing clearly, but tends to describe gates at a conceptual level.
- **v4 Operational**: emphasizes gating, domestic approvals, and step-by-step execution.
- **Essays/variants**: emphasize the “why” more than operational gating.

**GitBook approach:** keep gating as a core concept, with measurable criteria in `05-governance-and-verification/`.

### 2) Monitoring / stabilization design (Freeze)
- **Comprehensive**: stresses monitoring, incident grading, dashboards, humanitarian protections.
- **v4 Operational**: more specific on mechanisms and immediate setup actions.
- **McCormick-style**: often uses concrete imagery (buffering, sensors/OSCE-style monitoring) as persuasion.
- **French variant**: may propose distinctive institutional concepts and rhetoric.

**GitBook approach:** define a neutral monitoring “menu of options,” then standardize what must be true regardless of option (reporting, access, independence).

### 3) Voting integrity and inclusion (Vote)
- **Comprehensive**: strong emphasis on including displaced people; legitimacy framing.
- **v4 Operational**: tends to specify publish-and-lock mechanics (rules, algorithm versioning, pre-release simulation).
- **McCormick-style**: highlights auditable digital mechanisms in a simplified way.
- **French variant**: framing differs; details may not align with neutral spec language.

**GitBook approach:** treat “vote-to-border” and simulations as optional modules, with strict integrity requirements.

### 4) Reconstruction governance (Rebuild)
- **Comprehensive**: introduces reconstruction acceleration ideas and transparency imperatives.
- **v4 Operational**: tends to formalize governance proposals (institutions, patronage structures, named models).
- **Essays/variants**: use reconstruction as legitimacy and “peace dividend” argument.

**GitBook approach:** keep “Reconstruction Olympics” as a delivery model, but present governance structures as configurable (with pros/cons).

### 5) Legal/justice framing
- **v4 Operational**: more explicit on domestic approvals and legal pathway structuring.
- **Comprehensive**: generally keeps the justice topic framed as constraints and tradeoffs.
- **Essays/variants**: may adopt stronger rhetorical lines that are not implementation-ready.

**GitBook approach:** place legal pathways in `06-legal-and-political-pathways/` with clearly labeled options and constraints; avoid implying guaranteed legal outcomes.

## How conflicts are resolved (editorial rules)

When drafts disagree or a detail is overspecified:
1. Prefer **mechanism requirements** over **named institutions**.
2. If multiple plausible designs exist, present them as **Options A/B/C** with tradeoffs.
3. Keep persuasion language out of the core chapters; place it in `10-background-and-essays/`.
4. Anything that changes the mechanism’s commitments must be recorded in the **Decision log**.

## Traceability: where to find the originals

- Reference-only originals are listed in: [`11-appendices/04-source-text-archive.md`](../11-appendices/04-source-text-archive.md)
- Major reconciliation choices are recorded in: [`11-appendices/03-decision-log.md`](../11-appendices/03-decision-log.md)
- The current maintained logic is in:
  - Freeze: `02-freeze/`
  - Vote: `03-vote/`
  - Rebuild: `04-rebuild/`
  - Gates: [`05-governance-and-verification/02-verification-first-gates.md`](../05-governance-and-verification/02-verification-first-gates.md)

## Suggested “source note” convention (optional)

While drafting, add a short footer block on pages that heavily draw from one input:

> **Source note:** Derived primarily from [Operational v4] with supporting concepts from [Comprehensive] and narrative framing from [McCormick-style].

(Keep these notes short; the source archive is the canonical record.)
