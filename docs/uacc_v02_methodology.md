# UACC v0.2 Methodology

**Version:** 0.2 Public Draft  
**Status:** Public draft / working reference  

## Purpose

This methodology explains how to apply the v0.2 hardened core without treating UACC as a certification scheme or legal safe harbor.

The hardened core is the subset of UACC controls expanded to assessor-grade detail in this public draft. Other base-catalog controls remain in less detailed working-reference form until later releases.

## Assessment approach

Each hardened control uses three assessment methods:

- **Examine:** inspect documents, records, logs, configuration, approvals, reports, or evidence events.
- **Interview:** confirm process understanding with accountable roles.
- **Test:** sample or exercise a workflow, gate, log, report, or control outcome.

## Tier determination methodology

`UACC-INV-02` is the authoritative control for risk classification. This section explains how to apply that control in a readable decision flow. Organizations should document the classification rationale, approval, and revalidation evidence in the risk classification decision record.

### Default sequential screen

Screen each AI system in order. The first confirmed match determines the tier unless the organization applies a stricter internal classification. If classification evidence is incomplete, conflicting, or not approved, default to the higher plausible tier until the classification decision record is updated.

Where a single AI system serves multiple use cases at different risk tiers, the system inherits the highest applicable tier unless the organization demonstrates technical and organizational separation sufficient to govern each use case independently. Separation is sufficient only where each use case can be independently governed, monitored, approved, changed, suspended, audited, and evidenced without relying on controls from a lower-tier use case. Separation should cover, as applicable, deployment configuration, data sources, retrieval indexes, prompts, access controls, logging, monitoring, human review, release gates, incident response, and change management.

```text
Prohibited practice or prohibited by policy?
        │
        ├── yes ──▶ T0 — stop / do not deploy or continue operation
        │
        ▼ no
High-risk AI use?
Product-safety high risk, Annex III high risk,
or organization-defined high-impact use?
        │
        ├── yes ──▶ T1 — high-risk / high-assurance governance
        │
        ▼ no
Transparency-only, limited-risk interaction,
or material-but-bounded AI use?
        │
        ├── yes ──▶ T2 — limited-risk / proportionate governance
        │
        ▼ no
Minimal impact on rights, safety, access to services,
employment, credit, insurance, education,
or other material decisions?
        │
        └────────▶ T3 — minimal-risk / lightweight governance baseline
```

T0 is a stop state, not a risk-acceptance tier. Where a prohibited practice or policy-prohibited use is identified, the organization should not deploy or continue operation unless legal status changes or the classification is corrected through documented legal/compliance review. The record should preserve the prohibited-practice screen, escalation, suspension/withdrawal decision, affected-system scope, and any remediation or decommissioning evidence.

### EU AI Act default path

For organizations or systems that determine they are in EU AI Act scope, the default `UACC-INV-02` classification methodology screens for:

1. prohibited practices;
2. product-safety high-risk classification;
3. Annex III high-risk classification;
4. Article 6(3) derogation, where claimed;
5. transparency or limited-risk obligations; and
6. residual lower-risk classification.

Where Article 6(3) derogation is legally available and claimed, the classification record should include affirmative justification against the statutory conditions, confirmation that the system does not perform profiling of natural persons, required registration/documentation analysis where applicable, and compliance/legal approval. For UACC tiering, an unsupported, undocumented, unapproved, or profiling-involving derogation claim defaults the system to T1 until the derogation is substantiated or withdrawn.

### Non-EU or framework-neutral path

Organizations outside EU AI Act scope should still tier AI systems using an organizational risk-based path. At minimum, classification should consider whether the AI use materially affects:

- rights, liberties, dignity, or non-discrimination;
- health, safety, physical security, or critical services;
- access to employment, credit, insurance, education, housing, public benefits, or essential services;
- legal, financial, disciplinary, eligibility, or similarly consequential decisions;
- vulnerable populations or protected classes;
- scale of deployment, automation level, reversibility of harm, and availability of meaningful human review;
- security-sensitive automation, privileged access, autonomous tool use, production-system control, or cyber-defense/security decisioning; and
- transparency expectations, user interaction, or disclosure obligations.

If these factors indicate high impact or high consequence, classify the system as T1 even when no EU AI Act classification applies. If the use creates material transparency or bounded operational risk without high-impact decisioning, classify as T2. If impact is minimal and no higher-risk trigger applies, classify as T3.

Human review should be treated as meaningful only when reviewers have authority, time, competence, context, and tooling to override, reject, or escalate AI outputs, and when override or escalation decisions are logged or sampled. Where interruption, pause, or stop is claimed to be technically infeasible, the claim should be capability-specific, documented, approved, and paired with compensating controls proportionate to the risk.

Organizations should reassess tier classification when intended purpose, affected population, deployment context, decision scope, automation level, geography, legal role, model/data version, performance, or control design changes materially from the conditions documented at initial classification. Reclassification should be event-driven, approved by the classification owner or designated compliance/legal authority, and recorded in the classification decision record. Routine model, prompt, or data updates may be handled through change control without reclassification only when documented thresholds show the approved tier and control assumptions remain valid.

### Relationship to NIST Low / Moderate / High

Do not convert NIST Low, Moderate, or High impact baselines directly into UACC tiers. NIST impact baselines address information-system confidentiality, integrity, and availability. UACC tiers address AI-specific governance, safety, rights, transparency, and compliance risk. Apply both dimensions and use the stricter applicable requirement.

## Conditional sections

Conditional fields are included only when triggered. If a conditional section is not triggered, the canonical control should include one compact omitted-section note rather than a full `N/A` section.

Example: `Conditional sections omitted [INFORMATIVE]: Sampling Methodology is not triggered because this control does not require statistical sampling.`

Use one compact omitted-section note per control unless a specific omitted field needs separate explanation.

## Exception and risk acceptance

The common process is defined once in the control catalog's common exception and risk-acceptance model: document the unmet requirement, affected systems, rationale, residual risk, compensating controls, approval, register entry, expiration/review date, and remediation/renewal status.

## Evidence reuse

UACC evidence artifacts are designed to support multiple overlapping obligations. Crosswalk confidence labels explain the strength of each mapping and prevent equivalence overclaims.

A Partial or Analogical mapping means the evidence may require supplementation to fully satisfy the mapped requirement under its source framework.

Reused evidence should identify the system, model or component version, data scope, environment, time period, control owner, assessment method, and mapped obligation. Evidence may be reused only where those conditions remain applicable. Partial or Analogical mappings require documented gap analysis, supplemental evidence where needed, and approval by the accountable control owner.

## v0.2 release scope

The public draft hardens 11 of the broader 35 base controls. The remaining controls stay at working-reference depth until later releases.
