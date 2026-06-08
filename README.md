# Unified AI Control Catalog (UACC) v0.2 Public Draft

Assessor-oriented AI governance controls, reusable evidence expectations, crosswalk confidence labels, and governance-as-code artifacts for predictive/decisioning AI systems.

**Version:** 0.2 Public Draft  
**Status:** Public draft / working reference  
**Scope:** Predictive/decisioning AI hardened core, with a working GenAI overlay documented separately  
**License:** Documentation/text under CC BY 4.0; schema/scripts under MIT  
**Last updated:** 2026-06-06

UACC is a public working reference for AI governance, security, risk, and compliance teams that need controls they can actually assess. It translates AI governance expectations into control language, evidence expectations, crosswalk confidence labels, and governance-as-code artifacts that can support internal reviews, audit preparation, vendor assessments, and emerging AI regulatory readiness work.

> UACC is an open working reference catalog. It does not provide legal advice, certify compliance, replace conformity assessment, or create a regulatory safe harbor. Crosswalks identify areas of overlap and potential evidence reuse; they do not establish equivalence between frameworks.

## Why UACC exists

AI governance teams are often asked to turn overlapping expectations from internal risk programs, security frameworks, ISO/IEC 42001, NIST guidance, sector requirements, and emerging AI regulation into controls that can actually be assigned, implemented, evidenced, and reviewed.

Common practitioner problems include:

- auditors or customers asking for evidence of AI governance before evidence expectations are clear;
- legal, security, privacy, model risk, and engineering teams using different control language for the same system;
- framework mappings that imply coverage without explaining whether the mapping is Direct, Partial, Analogical, or only Informative;
- AI systems moving through engineering pipelines faster than quarterly governance reviews can track; and
- uncertainty about how to operationalize high-risk AI obligations without overclaiming legal compliance.

UACC's practical differentiator is the combination of assessor-oriented control language, reusable evidence expectations, confidence-labeled framework crosswalks, and governance-as-code artifacts in one public working reference.

UACC is also informed by related academic work on translating AI risk-management guidance into assessable control structures, including research on aligning NIST AI RMF functions with NIST SP 800-53 control families in cybersecurity GRC programs. See `ATTRIBUTION.md` for citation details; citation does not imply endorsement or validation of UACC.

## Positioning with COSAIS, NIST, ISO/IEC 42001, and the EU AI Act

UACC does not replace NIST COSAIS. COSAIS is expected to provide NIST-led SP 800-53 control-overlay guidance for securing AI systems once finalized. UACC is designed to complement COSAIS by adding practitioner-facing implementation detail, including actor-specific applicability, EU AI Act Article 9-15 crosswalks, ISO/IEC 42001 mappings, evidence templates, sector parameter packs, assessment procedures, and governance-as-code artifacts. COSAIS mappings remain Informative until public/final COSAIS materials provide stable identifiers.

As of June 2026, EU AI Act timelines remain subject to transition rules, guidance, and potential amendment. UACC maps selected control concepts within high-risk AI obligations, including aspects of Articles 9-15, but implementers should verify current applicability dates against official EU sources and jurisdiction-specific legal advice.

UACC is intended to help organizations structure controls and evidence that may support readiness activities. It does not determine whether a system is in scope, classify a system as legally high-risk, complete provider/deployer obligations, or substitute for legal analysis, assurance advice, or conformity assessment.

## Who this is for

- AI governance, risk, compliance, and legal teams designing AI control programs.
- Security, privacy, model risk, and internal audit teams reviewing AI systems.
- AI engineering, MLOps, and platform teams implementing evidence-producing controls.
- Organizations preparing for AI assurance, vendor review, ISO/IEC 42001 alignment, NIST-aligned governance, or EU AI Act readiness activities.

## Why use UACC?

UACC helps practitioners move from framework intent to reviewable implementation by:

- making AI governance controls easier to assign, test, and evidence;
- showing what evidence may be reusable across frameworks without claiming equivalence;
- separating strong mappings from Partial, Analogical, or Informative mappings;
- connecting controls to risk tiers, actor roles, assessment procedures, and evidence artifacts; and
- supporting governance-as-code so AI system metadata, overlays, and approval gates can be validated consistently.

## Current status

The v0.2 public draft includes a hardened subset of 11 controls from the broader 35-control UACC base catalog before expanding the rest. These 11 controls have expanded control language, parameter defaults, applicability guidance, evidence expectations, assessment procedures, and crosswalk notes to support review and implementation. “Hardened” does **not** mean independently certified, regulator-approved, legally sufficient, or production-tested in every environment.

GenAI overlay controls (`UACC-GEN-*`) are documented separately in the GenAI overlay. This release focuses on the predictive/decisioning AI base catalog.

## Start here

| Goal | Start with |
|---|---|
| See the full 35-control base catalog and 11 hardened controls | `docs/uacc_v02_control_index.md` |
| Read the full hardened control text | `docs/uacc_v02_control_catalog.md` |
| Understand tiering and assessment methodology | `docs/uacc_v02_methodology.md` |
| Plan audit/evidence artifacts | `docs/uacc_v02_evidence_templates.md` |
| Review framework mappings and confidence labels | `docs/uacc_v02_crosswalk.md` |
| Understand governance-as-code | `docs/uacc_v02_governance_as_code.md` |
| Try the YAML examples and schema validator | `examples/`, `schemas/`, `scripts/` |
| Review GenAI-specific overlay controls | `docs/uacc_v02_genai_overlay.md` |
| Look up terminology | `docs/uacc_v02_glossary.md` |

## Quick start: validate governance YAML

From the repository root:

```bash
python3 -m pip install pyyaml jsonschema
python3 scripts/validate_governance_yaml.py
```

Expected result: the JSON Schema is valid, the Tier 2 and Tier 1 example YAML files validate, and built-in negative cases fail as expected.

## Repository contents

```text
docs/
  uacc_v02_control_index.md        # fast view of all 35 controls and hardened status
  uacc_v02_control_catalog.md      # full assessor-grade text for the 11 hardened controls
  uacc_v02_evidence_templates.md   # evidence traceability and example artifact contents
  uacc_v02_governance_as_code.md   # YAML/schema governance-as-code model
  uacc_v02_genai_overlay.md        # GenAI overlay controls and schema mapping
  uacc_v02_methodology.md          # tiering, evidence reuse, exception, and assessment method
  uacc_v02_crosswalk.md            # framework mappings and confidence labels
  uacc_v02_glossary.md             # working definitions
examples/
  governance.yaml
  governance_tier1_high_risk.yaml
schemas/
  governance_yaml_schema.json
scripts/
  validate_governance_yaml.py
archive/
```

## What UACC is not

UACC is not:

- legal advice;
- a certification scheme;
- a conformity assessment procedure;
- a regulatory safe harbor;
- a complete compliance program;
- an assertion that mapped controls are equivalent to legal, regulatory, or standards requirements.

Organizations remain responsible for determining applicability, implementing controls, validating evidence, and obtaining legal or assurance advice where needed.

## Feedback and contribution

This is a public draft intended for review and implementation feedback. Feedback from practitioners, assessors, auditors, counsel, engineers, security teams, and AI governance teams is welcome.

High-value feedback areas include control wording, crosswalk confidence labels, evidence expectations, governance-as-code validation, schema fields that are hard to operationalize, sector parameter packs, and proposed overlays. See `CONTRIBUTING.md` for contribution guidance. Avoid submitting third-party copyrighted standards text unless reuse rights are clear.

## License

UACC documentation and original text are licensed under CC BY 4.0 unless otherwise noted. Software-oriented artifacts, including `schemas/governance_yaml_schema.json` and scripts under `scripts/`, are licensed under the MIT License. Referenced third-party standards, laws, frameworks, taxonomies, trademarks, articles, PDFs, and other materials remain under their own terms.
