# Electorate definition

Electorate design is one of the most politically sensitive parts of the Vote phase. In Freeze–Vote–Rebuild, the key principle is:

> Eligibility must not collapse into “whoever is currently on the ground.”  
> The process must explicitly include displaced persons and refugees.

This chapter defines how to specify electorate rules in an operational, auditable way.

## Objectives

- Define who can vote in a way that is clear, fair, and resistant to manipulation.
- Include displaced persons/refugees through explicit eligibility pathways.
- Minimize incentives to displace populations to reshape outcomes.
- Provide an identity/verification method that can be audited.

## Eligibility categories (template)

A robust electorate definition typically covers:

### Category A: Current residents
- individuals residing in the relevant territory as of a defined cutoff date
- documentation options for residency (civil registry, utility records, etc.)

### Category B: Internally displaced persons (IDPs)
- individuals displaced within the country who can demonstrate prior residence
- mechanisms for registration and verification without excessive burden

### Category C: Refugees / external displaced persons
- individuals displaced across borders who can demonstrate prior residence and identity
- modalities for participation (consulates, supervised centers, secure remote options)

### Category D: Special cases
- military personnel (where stationed vs where registered)
- incarcerated persons
- individuals without documentation (proof alternatives, sworn statements with checks)
- minors reaching voting age between cutoff and voting date

## Key design choices that must be specified

### 1) Cutoff dates
You must define:
- the reference date for residency eligibility
- the reference date for displacement eligibility
- how to handle people who moved legitimately before the cutoff

### 2) Proof standards (identity + eligibility)
Define a ranked “proof ladder”:
- primary proofs (national ID, civil registry)
- secondary proofs (records, attestations, verified documents)
- exception pathway (for those lacking documents) with safeguards against fraud

### 3) Registration workflow
- where and how registration occurs (in-person, online, hybrid)
- identity verification steps
- appeals process for rejected registrations
- timeline for publishing provisional and final rolls

### 4) Voter roll transparency vs privacy
- what can be published (aggregated statistics)
- what must remain private (individual identities)
- independent audit access rules

### 5) Anti-duplication and anti-fraud controls
- unique voter identifiers
- cross-checking across modalities/locations
- reconciliation procedures after voting

## Inclusion of displaced persons: operational requirements

To make inclusion real, not rhetorical, specify:
- access points (registration centers, consulates, supervised hubs)
- language and accessibility support
- secure participation measures (especially for vulnerable groups)
- protections against retaliation and coercion
- transportation/logistics support where necessary

Track inclusion with metrics:
- registration rates by category (resident / IDP / refugee)
- rejection rates and appeal outcomes
- participation rates by category
- reported coercion incidents by category/location

## Common failure modes and mitigations

- **Exclusion by paperwork:** mitigate with proof ladders and accessible registration.
- **Fraud via weak proofs:** mitigate with layered verification, audits, and reconciliation.
- **Displacement incentives:** mitigate by anchoring eligibility to a cutoff date and including displaced categories.
- **Privacy abuse:** mitigate with strict data governance and independent auditing.

## Links to related chapters

- Voting modalities and identity systems: [`03-vote/03-voting-system-design.md`](03-voting-system-design.md)
- Integrity and observation: [`03-vote/04-integrity-observation.md`](04-integrity-observation.md)
- Data governance: [`05-governance-and-verification/04-data-governance-privacy-security.md`](../05-governance-and-verification/04-data-governance-privacy-security.md)
- Dispute handling: [`03-vote/06-dispute-resolution.md`](06-dispute-resolution.md)
