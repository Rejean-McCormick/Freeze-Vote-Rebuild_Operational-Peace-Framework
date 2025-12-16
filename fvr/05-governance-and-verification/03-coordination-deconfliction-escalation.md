# Coordination, deconfliction & escalation

Freeze–Vote–Rebuild assumes distrust and recurring incidents. This chapter defines the coordination machinery that prevents incidents from becoming escalation spirals and ensures disputes are processed through predictable channels.

## Objectives

- Prevent accidental clashes through reliable communication.
- Create fast, time-bounded incident handling.
- Reduce “retaliation-by-default” by providing a credible alternative.
- Make responses predictable through a pre-committed escalation ladder.

## Core components

### 1) Deconfliction channels (hotlines)
Minimum requirements:
- 24/7 hotline coverage
- named liaison officers on both sides (with alternates)
- authenticated communications (prevent spoofing)
- written protocols for what information can be shared
- logging of calls and outcomes (for audit)

### 2) Joint incident room (coordination cell)
Functions:
- intake and triage of incidents
- dispatch and access coordination for monitors
- tracking of unresolved disputes and deadlines
- coordination of humanitarian corridors and repair windows

### 3) Escalation ladder (pre-committed responses)
The escalation ladder defines what happens when incidents occur, based on:
- severity classification (S1–S4)
- confidence level (C1–C3)
- recurrence/pattern detection

The key is pre-commitment: responses are not improvised in the heat of events.

## Incident handling workflow (template)

1. **Report received**
   - from hotline, monitors, sensors, or observers

2. **Immediate safety step**
   - deconfliction call if active risk exists

3. **Triage and classification**
   - preliminary severity and confidence assigned

4. **Verification**
   - site access requested, evidence collected, corroboration obtained

5. **Adjudication**
   - contested cases go to dispute mechanism with deadlines

6. **Response**
   - apply ladder consequences (warnings → penalties → pauses/rollbacks)

7. **Publication**
   - report per the data governance policy

## Escalation ladder example (illustrative)

### Level 0: Routine management
Applies to S1/C2+ or minor incidents:
- log incident
- notify relevant liaison
- corrective action request
- no change in phase status

### Level 1: Formal warning + corrective measures
Applies to S2/C2+ or repeated S1:
- written warning
- mandated corrective measures within deadline
- increased monitoring in affected sector

### Level 2: Targeted consequences / benefit pause
Applies to S3/C2+ or repeated S2:
- temporary pause of specific benefit tier
- additional inspections or access requirements
- mandated remediation plan

### Level 3: Phase pause / rollback trigger
Applies to S4/C2+ or sustained S3 pattern:
- pause progression to next phase
- rollback of conditional incentives per pre-committed rules
- emergency governance council session within fixed timeframe

### Level 4: Termination / major enforcement posture
Applies to systematic high-severity violations or monitor expulsion:
- suspend framework implementation pending renegotiation
- initiate predefined external enforcement pathways (if any exist)

The precise ladder must be agreed and published in advance (except sensitive operational details).

## Dispute handling integration

Disputes must be time-bounded:
- rapid preliminary decisions to prevent escalation
- final decisions with published reasoning (privacy-aware)

See:
- Vote disputes: [`03-vote/06-dispute-resolution.md`](../03-vote/06-dispute-resolution.md)
- Governance model: [`05-governance-and-verification/01-status-neutral-governance-model.md`](01-status-neutral-governance-model.md)

## Coordination for corridors and repairs

The same coordination system should manage:
- corridor openings/closures
- repair windows and worksite access
- engineer convoy notifications and protections

See:
- [`02-freeze/04-humanitarian-corridors-protected-infrastructure.md`](../02-freeze/04-humanitarian-corridors-protected-infrastructure.md)

## Drafting note

When implementing, include:
- a one-page “incident SOP” with contact trees and deadlines,
- a RACI for who can declare an incident, who verifies, who adjudicates,
- a public-facing summary of escalation levels and consequences (without sensitive details).
