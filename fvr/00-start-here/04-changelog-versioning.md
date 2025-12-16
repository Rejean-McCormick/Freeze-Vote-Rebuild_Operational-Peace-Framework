# Changelog & versioning

This page tracks releases of the GitBook and explains how source drafts map into the unified structure.

## Versioning scheme (recommended)

Use semantic versioning for the GitBook:

- **MAJOR**: structural changes (navigation, chapter layout, scope changes)
- **MINOR**: significant content additions or policy/operational refinements
- **PATCH**: typo fixes, wording clarifications, formatting updates

Example: `v1.2.3`

## Source documents and how they map

This GitBook consolidates multiple inputs into a single maintained structure:

- **Comprehensive proposal (neutral, verification-first)**  
  Broad narrative and concept framing across Freeze / Vote / Rebuild.

- **“v4 — Operational Peace Framework”**  
  More implementation-oriented: sequencing, action items, legal/approval gating, and operational detail.

- **“McCormick-style off-ramp” essay**  
  Persuasive framing aimed at US realist audiences; narrative-style argumentation.

- **“Projet du Pape François…” (French variant)**  
  Alternate origin/variant framing and rhetorical positioning; useful as background and comparative material.

The unified book uses:
- Chapters `02`–`04` for the core mechanism (Freeze / Vote / Rebuild).
- Chapters `05`–`06` for cross-cutting verification + legal pathways.
- Chapter `10` for essays/variants (kept separate from the core mechanism).
- Chapter `11` to archive source texts and maintain traceability.

## Change control (recommended workflow)

When updating the GitBook:
1. Make substantive design changes via pull request (or tracked edit) and document the rationale in:
   - **Decision log** ([`11-appendices/03-decision-log.md`](../11-appendices/03-decision-log.md))
2. Record the release here under **GitBook releases**.
3. If a change alters how drafts are interpreted, update:
   - **Deltas between versions** ([`01-proposal-at-a-glance/05-deltas-between-versions.md`](../01-proposal-at-a-glance/05-deltas-between-versions.md))

## GitBook releases

### Unreleased
- Initial scaffold created (file tree, navigation, reader pathways).
- Content pages are placeholders pending extraction from source drafts.

### v1.0.0 (planned)
- First complete pass of core chapters:
  - Freeze / Vote / Rebuild
  - Governance & verification
  - Legal & political pathways
- Initial risk register and stakeholder playbooks.
- Source-text archive populated with reference-only originals.

## Conventions and flags

Use these markers in pages while drafting:

- **[TBD]** — requires content drafting
- **[ASSUMPTION]** — relies on a premise that should be made explicit and testable
- **[RISK]** — introduces or depends on a nontrivial failure mode
- **[OPEN QUESTION]** — requires stakeholder input or empirical validation
- **[SOURCE NOTE]** — indicates which source draft introduced the idea (for traceability)

## Attribution and licensing (placeholder)

Add here:
- Document owner / maintainer
- Licensing terms (if any)
- Citation guidance for reuse

If you want stricter governance, add a short “editorial policy” section here and enforce it via the decision log.
