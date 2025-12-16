# Templates

This page contains reusable templates that support implementation. Copy these into working documents and adapt as needed.

## Template A: Verification gate definition

**Gate name:**  
**Purpose:**  
**Phase:** (Freeze / Vote / Rebuild / Cross-cutting)

**Indicators:**  
- Indicator 1:
- Indicator 2:
- Indicator 3:

**Thresholds:**  
- Indicator 1 threshold:
- Indicator 2 threshold:
- Indicator 3 threshold:

**Measurement window:** (e.g., rolling 14 days)  
**Data sources:** (monitors, sensors, audits, observers)  
**Decision authority:** (who certifies)  
**Dispute process:** (how contested determinations are handled)  
**Consequences if PASS:** (what unlocks)  
**Consequences if FAIL:** (pause/rollback; what changes immediately)  
**Publication policy:** (what is published, what is restricted)  
**Notes / assumptions:**  

---

## Template B: Incident report (Freeze)

**Incident ID:**  
**Date/time (UTC/local):**  
**Location:** (coordinates + locality)  
**Reporting channel:** (hotline / monitor / sensor / other)

**Description:**  
**Immediate safety actions taken:**  
**Parties involved (if known):**  

**Classification (preliminary):**  
- Severity: (S1–S4)  
- Confidence: (C1–C3)  
- Recurrence flag: (Yes/No)

**Evidence:**  
- Photos/video:
- Witness statements:
- Sensor data:
- Site visit notes:
- Other:

**Access status:** (full / partial / denied)  
**Obstruction/intimidation noted:** (Yes/No; details)

**Verification actions:**  
**Adjudication status:** (open / resolved / disputed)  
**Outcome and decision:**  
**Consequences applied (if any):**  
**Publication status:** (public aggregate / restricted / redacted)

---

## Template C: Vote complaint filing

**Complaint ID:**  
**Filed by:** (voter / observer / official / other; anonymize if needed)  
**Date/time filed:**  
**Location / modality:** (polling place / registration center / remote center)

**Type:** (registration / coercion / procedure / counting / other)  
**Description:**  
**Evidence attached:**  
**Immediate risk/safety concerns:** (Yes/No; details)

**Requested remedy:** (recount / rerun / corrective action / other)  
**Initial triage classification:** (minor/serious/critical)  
**Timeline commitments:**  
- acknowledge by:
- preliminary decision by:
- final decision by:

**Disposition:** (open / resolved / escalated / appealed)  
**Decision summary (publishable):**  

---

## Template D: Vote audit summary

**Audit method:** (risk-limiting / recount triggers / other)  
**Scope:** (sites covered, sample size, modalities)  
**Key reconciliation checks:**  
- issued vs returned:
- pollbook vs counted:
- chain-of-custody exceptions:

**Findings:**  
- discrepancies:
- anomalies flagged:
- procedural violations:

**Remedies applied:**  
**Observer notes (if applicable):**  
**Conclusion:** (within tolerance / requires action / fails integrity threshold)  
**Publication plan:** (what is published vs restricted)

---

## Template E: Reconstruction project registry entry

**Project ID:**  
**Category:** (housing / energy / transport / health / education / other)  
**Location:** (general + precise in restricted record)  
**Scope:**  
**Beneficiaries:** (estimated households/users)  
**Budget:**  
**Funding source:**  
**Contractor(s):**  
**Procurement method:** (competitive / emergency / other; justification)

**Milestones:**  
- M1:
- M2:
- M3:

**Verification evidence required:** (photos, inspections, certificates)  
**Audit requirements:** (thresholds, cadence)  
**Risk flags:** (security / corruption / complexity)  
**Status:** (planned / in progress / completed)  
**Completion evidence:**  

---

## Template F: Debarment decision record (Rebuild)

**Vendor/entity:**  
**Reason for action:** (fraud / nonperformance / conflict-of-interest / other)  
**Evidence summary:**  
**Due process steps taken:** (notice, response window, hearing)  
**Decision:** (debarred / suspended / warning)  
**Duration:**  
**Appeal rights and timeline:**  
**Publication status:** (public summary + restricted evidence file)

---

## Template G: KPI dashboard spec (minimum fields)

**Dashboard name:**  
**Audience:** (public / restricted / audit-only)  
**Update frequency:**  
**Indicators included:**  
- indicator definition
- data source
- calculation method
- caveats/limitations

**Redaction rules:**  
**Access controls:**  
**Owner:**  
**Audit trail/logging:**  

---

## Drafting note

As the book is populated with real content, keep these templates:
- stable (avoid frequent breaking changes),
- versioned (changes recorded in [`00-start-here/04-changelog-versioning.md`](../00-start-here/04-changelog-versioning.md)),
- referenced from the chapters that use them.
