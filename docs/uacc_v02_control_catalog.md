# UACC v0.2 Control Catalog — Hardened Core

**Version:** 0.2 Public Draft  
**Status:** Public draft / working reference  
**Scope:** Predictive/decisioning AI hardened core controls  
**Audience:** GRC, security, privacy, legal, model risk, AI engineering, MLOps, and audit teams  
**License:** CC BY 4.0  
**Last updated:** 2026-06-06

> UACC is an open working reference catalog. It does not provide legal advice, certify compliance, replace conformity assessment, or create a regulatory safe harbor. Crosswalks identify areas of overlap and potential evidence reuse; they do not establish equivalence between frameworks.

> As of June 2026, EU AI Act timelines remain subject to transition rules, guidance, and potential amendment. UACC maps selected control concepts within high-risk AI obligations, including aspects of Articles 9-15, but implementers should verify current applicability dates against official EU sources and jurisdiction-specific legal advice.

---

## 1. Scope and applicability

This public draft hardens 11 controls from the broader 35-control UACC base catalog for predictive/decisioning AI systems. The remaining base controls stay in less detailed working-reference form and are planned for later hardening. This document does not create a certification scheme.

Related-control references may point to controls in the broader 35-control UACC base catalog, not only the 11 controls hardened in this public draft.

The 11 hardened controls were selected because they form a minimum evidence-producing core for consequential predictive/decisioning AI systems: governance authority, system discovery, risk classification, pre-deployment risk analysis, rights impact assessment, data provenance, bias testing, operational monitoring, decision traceability, human oversight, and serious incident response. Other UACC base controls remain available in less detailed working-reference form and may be hardened in later releases after public feedback.

Organizations may adopt the default parameter assignments as a starting baseline, replace them with documented organization-defined values, or use them as assessment criteria for a defined system scope. Tailoring should be documented, approved, and retained as assessment evidence.

## 2. Document conventions

Each control is structured for assessment use: the Control Statement defines the requirement; Parameter Assignments provide default tailoring values; Applicability identifies where the control applies; Assessment Procedures and Pass/Fail Criteria support review; and Crosswalks identify alignment with external frameworks without claiming equivalence.

Terms used in this catalog are defined in `uacc_v02_glossary.md`; tier determination and assessment methodology are described in `uacc_v02_methodology.md`.

- **NORMATIVE** text defines requirements used for assessment.
- **INFORMATIVE** text provides explanation, context, crosswalks, or implementation guidance.
- `shall` indicates a mandatory requirement.
- `should` indicates a recommended practice.
- `[Assignment: organization-defined ...]` indicates tailoring.
- Conditional sections are included only when triggered. If a conditional section is not triggered, the control includes a compact `Conditional sections omitted [INFORMATIVE]` note instead of full `N/A` sections.

### 2.1 Key terms used in this draft

This table is a quick reference for reading the catalog. See `uacc_v02_glossary.md` and `uacc_v02_methodology.md` for fuller definitions and tier-determination guidance.

| Term | Meaning in this catalog |
|---|---|
| Hardened core | The 11 controls expanded to assessor-grade detail in this public draft. |
| Tier 0 | Prohibited or disallowed use; stop or do not deploy unless legal status changes. |
| Tier 1 | High-risk or consequential AI use requiring the strongest evidence baseline. |
| Tier 2 | Limited/moderate-risk AI use requiring documented governance and scaled evidence. |
| Tier 3 | Minimal/lower-risk AI use subject mainly to inventory, ownership, and baseline governance. |
| Actor roles | Provider, deployer, importer, distributor, and authorized representative roles are determined by the organization's actual role for a given AI system and jurisdiction; do not assume every role applies to every organization. |
| Evidence IDs | `EVD-*` references point to evidence artifact examples in `uacc_v02_evidence_templates.md`; equivalent documented evidence is acceptable when it preserves the same assessment facts. |
| Sector parameter pack | An organization-defined or sector-defined bundle of metrics, thresholds, sample-size rules, and approval parameters for a class of AI use cases. |
| Significant or material change | A change to intended purpose, population, model/data version, decision workflow, geography, legal role, risk tier, performance, or control design that could affect risk, obligations, or evidence validity. |

### 2.2 Crosswalk confidence labels

| Label | Meaning |
|---|---|
| Direct | Narrow requirement match; UACC evidence directly supports the mapped requirement. |
| Partial | UACC evidence supports part of a broader obligation or outcome. |
| Analogical | Similar control concept, but the source framework was not written for this exact AI-specific requirement. |
| Informative | Useful context or alignment only; not a requirement mapping. |

### 2.3 Approval authority and independence

- **Approval authority** is the role authorized to approve, maintain, or accept accountability for a governance artifact, policy, release, risk decision, or exception.
- **Independence criteria** are additional separation requirements used when review credibility depends on reviewer independence, such as model validation, bias testing, audit, risk acceptance, or release gating.

### 2.4 Common exception and risk-acceptance model

The common exception process is defined once here and referenced by controls. When a control states that per-control exception parameters are not triggered, the common exception process still applies to any approved deviation from a normative requirement.

1. Document the unmet requirement, affected system(s), rationale, residual risk, and compensating controls.
2. Obtain approval from the required authority before relying on the exception.
3. Record the exception in the risk register or exception register.
4. Set an expiration or review date.
5. Track remediation or renewal decisions.
6. Preserve evidence for assessment.

---

## 3. Hardened core controls

| Section | Control ID | Control title |
|---|---|---|
| 3.1 | `UACC-GOV-01` | AI Governance Policy |
| 3.2 | `UACC-INV-01` | AI System Inventory |
| 3.3 | `UACC-INV-02` | Risk Classification with Documented Rationale |
| 3.4 | `UACC-RSK-01` | Pre-Deployment AI Risk Assessment |
| 3.5 | `UACC-RSK-02` | Fundamental Rights Impact Assessment (FRIA) |
| 3.6 | `UACC-DAT-01` | Training Data Lineage and Provenance |
| 3.7 | `UACC-MDL-02` | Bias and Disparate Impact Testing |
| 3.8 | `UACC-MON-01` | Model Performance Monitoring |
| 3.9 | `UACC-MON-04` | Audit Logging for Decision Traceability |
| 3.10 | `UACC-HUM-01` | Human Oversight Mechanism Design |
| 3.11 | `UACC-INC-02` | Serious Incident Reporting Workflow |

### 3.1 UACC-GOV-01: AI Governance Policy

**Control Statement [NORMATIVE]:**  
The organization shall establish, document, approve, maintain, communicate, and periodically review an AI governance policy that defines [Assignment: organization-defined scope of AI systems covered], governance principles, decision authority, AI-specific risk management responsibilities, and applicable regulatory or contractual obligations.

**Parameter Assignments [NORMATIVE]:**

| Parameter ID | Parameter | Default | Rationale |
|---|---|---|---|
| `uacc-gov-01_prm_1` | Scope of AI systems covered | All AI systems as defined by the organization's adopted AI-system definition, including internally developed, third-party, predictive/decisioning, generative, and agentic systems. | Policy scope should not exclude material AI categories before inventory and risk classification occur. |
| `uacc-gov-01_prm_2` | Review frequency | At least annually and upon significant regulatory, organizational, risk, or AI-use change. | Keeps policy current as obligations and use cases change. |
| `uacc-gov-01_prm_3` | Approval authority | Board, board committee, C-suite executive, named executive owner, or formally delegated AI governance authority. | AI governance policy requires accountable senior approval without assuming a large-company committee structure. |
| `uacc-gov-01_prm_4` | Required policy topics | AI scope and definitions; governance principles; roles and decision authority; inventory and classification requirements; risk-management lifecycle; human oversight expectations; incident escalation; third-party AI expectations; exception/risk-acceptance process reference. | Ensures the policy addresses AI-specific governance rather than restating generic IT/security policy. |

**Applicability [NORMATIVE]:**
- Category: Administrative.
- Risk Tier Applicability: Tier 1, Tier 2, and Tier 3 at the organizational policy level.
- Actor Applicability: Provider, Deployer, Importer, Distributor, and Authorized Representative where the organization performs those roles.
- Organizational Scope: enterprise-wide; business-unit supplements may tighten requirements but shall not weaken the enterprise baseline without approved exception.
- AI Lifecycle Phase: Strategy & Design; informs all lifecycle phases.
- Required / Conditional / Informative: Required baseline governance control.

**Discussion [INFORMATIVE]:**  
An AI governance policy is the top-level management statement for AI risk governance. It should connect enterprise risk, compliance, privacy, cybersecurity, procurement, model risk, and incident-management processes to AI-specific obligations. It should not be limited to high-risk systems because inventory, classification, and shadow-AI discovery depend on enterprise scope before risk tiering.

**Conditional sections omitted [INFORMATIVE]:** Threat Anchor, Sampling Methodology, Reproducibility Metadata, Independence Criteria, and Exception / Risk-Acceptance Parameters are not triggered. GOV-01 requires approval authority for the policy, but it does not require model-validation-style independence criteria.

**Assessment Procedures [NORMATIVE]:**
- Examine AI governance policy, approval record, version/review history, scope definition, AI-specific governance topics, communication record, and exception/risk-acceptance process reference.
- Interview the policy owner, AI governance committee chair or delegated governance lead, and selected business or technology owner.
- Test policy accessibility, review currency, and — where an AI inventory exists — scope reconciliation to inventory.

**Pass/Fail Criteria [NORMATIVE]:**
- SATISFIED when a documented policy exists, is approved, current against the review frequency, defines AI scope, addresses AI-specific risks and governance responsibilities, assigns authority, is communicated, and where an inventory exists reconciles to inventory scope.
- OTHER THAN SATISFIED when no policy exists, approval is missing, the policy is stale, AI-specific risks or authority are omitted, scope is materially narrower than actual AI use without rationale, personnel cannot access it, or inventory/policy scope materially conflicts without rationale.

**Related Controls [INFORMATIVE]:** `UACC-GOV-02`, `UACC-GOV-03`, `UACC-INV-01`, `UACC-INV-03`, `UACC-RSK-01`, `UACC-INC-01`, `UACC-VEN-01`.

**Crosswalk [INFORMATIVE]:**

| Framework | Mapping | Confidence | Notes |
|---|---|---|---|
| `[AI-RMF]` | GOVERN 1.1, GOVERN 1.2 | Partial | Supports governance policy integration but does not satisfy all GOVERN outcomes by itself. |
| `[SP800-53]` | PM-1, PL-1 | Analogical | Maps to program/policy planning concepts; AI-specific tailoring may be refined when public/final COSAIS materials are available. |
| `[EU-AI-ACT]` | Article 17(1)(a) | Partial | Supports a regulatory-compliance strategy for provider QMS; does not establish a full QMS. |
| `[ISO42001]` | Clause 5.2, Annex A.2.2 | Partial | Supports AI policy requirements in an AIMS; does not imply certification. |
| `[COSAIS]` | Base governance/policy alignment | Informative | Mapping will be updated when public/final COSAIS materials are available. |

---

### 3.2 UACC-INV-01: AI System Inventory

**Control Statement [NORMATIVE]:**  
The organization shall establish, maintain, and periodically reconcile a structured inventory of all in-scope AI systems, including [Assignment: organization-defined metadata fields] for each system; shall update the inventory [Assignment: organization-defined update frequency]; and shall perform [Assignment: organization-defined discovery and reconciliation methods] to identify AI systems not yet registered in the inventory.

**Parameter Assignments [NORMATIVE]:**

| Parameter ID | Parameter | Default | Rationale |
|---|---|---|---|
| `uacc-inv-01_prm_1` | Metadata fields | Core mandatory: System ID, name, version, intended purpose, AI system type, owner, business owner, technical contact, deployment status/geography, last review, next review. Conditional: model type, data inputs/outputs, affected populations, vendor fields, risk tier/classification, provider/deployer role, human overseer. | Supports ownership and traceability without forcing non-applicable high-risk/vendor fields. |
| `uacc-inv-01_prm_2` | Update frequency | Event-driven updates upon known lifecycle events or validated discovery, with at least quarterly completeness review. | Makes “continuous maintenance” testable without requiring real-time inventory automation. |
| `uacc-inv-01_prm_3` | Reconciliation methods | Procurement/vendor records, SaaS/application inventory, cloud billing or service inventory, model registry, expense records, and business-owner attestations where available. Active endpoint/network/DLP/API-egress detection belongs in `UACC-INV-03`. | Proves inventory completeness while preserving the INV-03 boundary. |
| `uacc-inv-01_prm_4` | Registration timeframe | Initial triage within 10 business days; full registration/classification within 30 calendar days of validated discovery unless approved extension exists. | UACC-defined practical assessment default. |

**Applicability [NORMATIVE]:**
- Category: Administrative / Operational.
- Risk Tier Applicability: Tier 1, Tier 2, Tier 3.
- Actor Applicability: Provider, Deployer, Importer, Distributor, Authorized Representative where the organization performs those roles.
- Organizational Scope: enterprise-wide inventory baseline; local sub-registers shall reconcile to the enterprise inventory.
- AI Lifecycle Phase: Strategy & Design; Procurement; Development; Deployment; Operations; Retirement.
- Required / Conditional / Informative: Required baseline control.

**Discussion [INFORMATIVE]:**  
Inventory is not credible unless it includes reconciliation. `UACC-INV-01` reconciles against records the organization already holds. `UACC-INV-03` remains the active shadow-AI detection control for endpoint, network, DLP, browser-extension, API-egress, continuous tooling, investigation workflow, and follow-up metrics. Low-risk embedded AI features may use lightweight entries when they do not support consequential decisions, process sensitive data at material scale, or create regulated obligations; escalation to full metadata should occur when use becomes consequential.

**Sampling Methodology [NORMATIVE, where applicable]:** Review all Tier 1 inventory entries; sample Tier 2/Tier 3 entries; and test a risk-based sample of procurement, SaaS/application, cloud service-inventory or billing, model-registry, and business-attestation records likely to indicate AI use.

**Reproducibility Metadata [NORMATIVE, where applicable]:** Preserve source system, report/export name, extraction date/time, query/filter/detection rule, assessment period, reviewer or job ID, report/ticket/hash/evidence-event ID, and finding disposition.

**Conditional sections omitted [INFORMATIVE]:** Threat Anchor, Independence Criteria, and per-control Exception / Risk-Acceptance Parameters are not triggered.

**Assessment Procedures [NORMATIVE]:**
- Examine inventory register, metadata definitions, completeness reviews, reconciliation reports, registration records, classification links, retirement status, and exception records.
- Interview AI governance/ITAM, procurement, cloud/platform/security, and business owners.
- Test sampled inventory entries for metadata completeness and reconcile sampled source records to inventory entries or documented out-of-scope rationale.

**Pass/Fail Criteria [NORMATIVE]:**
- SATISFIED when a structured inventory exists, required metadata is populated for sampled entries, ownership/cadence are documented, reconciliation occurs, discovered systems are registered on time, and sampled source records reconcile or have documented rationale.
- OTHER THAN SATISFIED when no structured inventory exists, metadata is materially incomplete, no reconciliation exists, findings are not followed up, material unregistered AI use is found, or inventory cannot support classification/regulatory mapping.

**Crosswalk [INFORMATIVE]:**

| Framework | Mapping | Confidence | Notes |
|---|---|---|---|
| `[AI-RMF]` | GOVERN 1.6 | Direct | Directly implements inventory mechanisms. |
| `[AI-RMF]` | MAP 1.1 | Partial | Inventory supports context mapping. |
| `[SP800-53]` | CM-8, PM-5 | Analogical | AI-specific tailoring may be refined when public/final COSAIS materials are available. |
| `[EU-AI-ACT]` | Article 49; Articles 16, 26 | Partial | Supports registration/role management for applicable high-risk systems and Article 6(3) determinations; does not create a general legal inventory duty for all AI systems or complete legal obligations. |
| `[ISO42001]` | Annex A.4.2, A.4.5 | Partial | Supports AIMS resource/system documentation. |
| `[COSAIS]` | Inventory alignment | Informative | Mapping will be updated when public/final COSAIS materials are available. |

---

### 3.3 UACC-INV-02: Risk Classification with Documented Rationale

**Control Statement [NORMATIVE]:**  
The organization shall classify each AI system by risk tier using [Assignment: organization-defined classification methodology], document the classification rationale including [Assignment: organization-defined rationale elements], and obtain approval from [Assignment: organization-defined approval role] before deployment or material use.

**Parameter Assignments [NORMATIVE]:**

| Parameter ID | Parameter | Default | Rationale |
|---|---|---|---|
| `uacc-inv-02_prm_1` | Classification methodology | Sequential screen: prohibited practices, product-safety high risk, Annex III high risk, Article 6(3) derogation where legally available and claimed, including confirmation that the system does not perform profiling of natural persons, transparency obligations, residual lower-risk classification. | Follows EU AI Act classification logic while allowing local methodology and preventing unsupported derogation downgrades. |
| `uacc-inv-02_prm_2` | Rationale elements | Intended purpose, affected population, applicable articles/annexes or organizational risk criteria, prohibited-practice screen, high-risk screen, classification basis, Article 6(3) derogation justification where claimed including statutory-condition analysis and profiling-exclusion confirmation, transparency obligations, and non-EU risk basis where applicable. | Makes classification reviewable across EU and non-EU contexts. |
| `uacc-inv-02_prm_3` | Approval role | Compliance Lead or Legal Counsel. | Classification can have legal/regulatory consequences. |
| `uacc-inv-02_prm_4` | Review trigger | At registration, before deployment, annually, and upon significant change. | Classification can change as use changes. |

**Applicability [NORMATIVE]:**
- Category: Administrative.
- Risk Tier Applicability: all tiers.
- Actor Applicability: Provider and Deployer; other actors where role obligations require classification.
- Organizational Scope: all inventoried AI systems.
- AI Lifecycle Phase: Strategy & Design; Deployment; Operations.
- Required / Conditional / Informative: Required.

**Discussion [INFORMATIVE]:**  
Classification drives which controls, evidence, and obligations apply. For consequential predictive/decisioning systems, Article 6(3) derogation claims should be treated as exceptional classification outcomes, not default downgrades. Where claimed, the record should affirmatively address each statutory condition, confirm that the system does not perform profiling of natural persons, identify any required registration or documentation consequence, and include compliance/legal approval. Unsupported, undocumented, unapproved, or profiling-involving derogation claims should not be used to avoid Tier 1 treatment. See the tier determination methodology in `uacc_v02_methodology.md` for the readable EU and non-EU decision flow.

**Sampling Methodology [NORMATIVE, where applicable]:** Review all Tier 1 classifications and a risk-based sample of Tier 2/Tier 3 classifications; include new registrations, systems claiming Article 6(3) derogation, and systems with significant changes where present.

**Independence Criteria [NORMATIVE, where applicable]:** Classification approval shall be performed by a compliance/legal role that is not solely accountable for shipping the system.

**Conditional sections omitted [INFORMATIVE]:** Threat Anchor, Reproducibility Metadata, and per-control Exception / Risk-Acceptance Parameters are not triggered.

**Assessment Procedures [NORMATIVE]:**
- Examine classification worksheet, prohibited-practice screen, high-risk screen, article/annex or organizational risk citations, Article 6(3) derogation justifications, statutory-condition analysis, profiling-exclusion evidence, required registration/documentation evidence where applicable, transparency-obligation determinations, approvals, and revalidation records.
- Interview compliance/legal and system owner.
- Test sampled systems for complete sequential-screen rationale, approval, and revalidation where due.

**Pass/Fail Criteria [NORMATIVE]:**
- SATISFIED when each sampled system has current classification, traceable sequential-screen rationale, approval, and revalidation where due.
- OTHER THAN SATISFIED when classification is missing, superficial, unapproved, stale, omits a required screen, derogation claims lack documented legal/compliance rationale, or a system matching a prohibited-practice screen is deployed or continues operation without documented legal/compliance escalation, suspension/withdrawal decision, and preserved classification record.

**Crosswalk [INFORMATIVE]:**

| Framework | Mapping | Confidence | Notes |
|---|---|---|---|
| `[AI-RMF]` | MAP 1.1, MAP 1.5 | Partial | Supports context/risk categorization. |
| `[SP800-53]` | RA-2 | Analogical | Maps to security categorization concepts; AI-specific tailoring may be refined when public/final COSAIS materials are available. |
| `[EU-AI-ACT]` | Article 6, Annex III | Direct | Direct for classification workflow where EU AI Act classification applies. |
| `[EU-AI-ACT]` | Article 5 | Partial | Supports prohibited-practice screening only; does not itself satisfy substantive prohibition obligations. |
| `[ISO42001]` | 6.1.2, A.5.2 | Partial | Supports AI risk classification and impact assessment. |
| `[COSAIS]` | Classification alignment | Informative | Mapping will be updated when public/final COSAIS materials are available. |

---

### 3.4 UACC-RSK-01: Pre-Deployment AI Risk Assessment

**Control Statement [NORMATIVE]:**  
The organization shall conduct a structured risk assessment for each [Assignment: organization-defined risk tier] AI system before deployment, identifying risks under intended use and reasonably foreseeable misuse, documenting severity, likelihood, residual risk, and treatment decisions in [Assignment: organization-defined risk documentation].

**Parameter Assignments [NORMATIVE]:**

| Parameter ID | Parameter | Default | Rationale |
|---|---|---|---|
| `uacc-rsk-01_prm_1` | Risk tier trigger | Tier 1 mandatory; Tier 2 recommended or required where organizational policy defines material risk. | Prioritizes high-risk systems while supporting scaled adoption. |
| `uacc-rsk-01_prm_2` | Risk categories | Health, safety, fundamental rights, bias, performance, data quality, adversarial manipulation, privacy, security, downstream decision impact, and foreseeable misuse. | Covers AI-specific harms and operational failure modes. |
| `uacc-rsk-01_prm_3` | Minimum assessment content | Intended use, reasonably foreseeable misuse, affected population, severity, likelihood, inherent risk, controls/mitigations, residual risk, treatment decision, owner, approval, and next review trigger. | Makes risk assessments comparable and reviewable. |
| `uacc-rsk-01_prm_4` | Documentation | `EVD-03` or equivalent risk assessment plus risk register entry. | Preserves traceability without requiring a specific template. |
| `uacc-rsk-01_prm_5` | Approval role | Accountable business/risk owner with compliance/legal input where rights, safety, or regulatory obligations are material. | Residual-risk acceptance should sit with an accountable owner, not only the build team. |
| `uacc-rsk-01_prm_6` | Review triggers | Pre-deployment, significant change, material incident, annual reassessment for Tier 1. | Keeps risk evidence current. |

**Applicability [NORMATIVE]:**
- Category: Administrative.
- Risk Tier Applicability: Tier 1 required; Tier 2 conditional/recommended.
- Actor Applicability: Provider and Deployer.
- Organizational Scope: all in-scope high-risk systems.
- AI Lifecycle Phase: Development; Deployment; Operations reassessment.
- Required / Conditional / Informative: Required for Tier 1.

**Threat Anchor [CONDITIONAL — included]:** Known and reasonably foreseeable risks, foreseeable misuse, model drift, performance degradation, bias/discrimination, and adversarial manipulation that can lead to harmful decision outcomes.

**Sampling Methodology [NORMATIVE, where applicable]:** Review all Tier 1 deployments in the assessment period and a risk-based sample of change-triggered reassessments.

**Independence Criteria [NORMATIVE, where applicable]:** Residual-risk acceptance for Tier 1 systems shall include an accountable approver who is not solely accountable for shipping the system.

**Exception / Risk-Acceptance Parameters [CONDITIONAL — included]:** Exceptions to required pre-deployment assessment, untreated high residual risk, or deployment before mitigation closure require documented residual risk, compensating controls, accountable risk-owner approval, expiration/review date, and exception-register linkage.

**Conditional sections omitted [INFORMATIVE]:** Reproducibility Metadata is not triggered unless the organization uses automated risk scoring or generated risk outputs.

**Assessment Procedures [NORMATIVE]:**
- Examine `EVD-03` or equivalent reports, risk register entries, treatment decisions, residual-risk approvals, approval-to-deploy records, and reassessment evidence.
- Interview risk manager, model/system owner, and accountable risk owner.
- Test that sampled Tier 1 deployments completed risk assessment before production and that residual risk was approved.

**Pass/Fail Criteria [NORMATIVE]:**
- SATISFIED when required systems have pre-deployment assessment, intended-use and misuse analysis, severity/likelihood and residual-risk documentation, registered risks, treatment decisions, accountable approval, and current reassessment.
- OTHER THAN SATISFIED when any Tier 1 system is deployed without assessment, severity/likelihood or residual-risk documentation is missing, treatment decisions are missing, residual risk is unapproved, or assessment occurs only after production use.

**Crosswalk [INFORMATIVE]:**

| Framework | Mapping | Confidence | Notes |
|---|---|---|---|
| `[AI-RMF]` | MAP 2.1, MAP 2.3, MAP 5.1 | Partial | Supports risk identification, context, and impact analysis. |
| `[SP800-53]` | RA-3 | Partial | Supports risk assessment function; the gap is AI-specific risk categories and evidence expectations. |
| `[EU-AI-ACT]` | Article 9(2)(a)-(b) | Direct | Direct for risk identification/evaluation concepts where high-risk AI Act obligations apply. |
| `[ISO42001]` | 6.1.2, 8.2 | Partial | Supports AI risk assessment and treatment. |
| `[COSAIS]` | Risk assessment alignment | Informative | Mapping will be updated when public/final COSAIS materials are available. |

---

### 3.5 UACC-RSK-02: Fundamental Rights Impact Assessment (FRIA)

**Control Statement [NORMATIVE]:**  
The organization shall conduct a Fundamental Rights Impact Assessment, or equivalent rights-impact assessment where applicable, before use for each deployment where such assessment is legally required, required by organizational policy, or triggered for consequential use; shall assess impact on [Assignment: organization-defined fundamental rights] for [Assignment: organization-defined affected groups]; shall document mitigations; and shall obtain [Assignment: organization-defined approval].

**Parameter Assignments [NORMATIVE]:**

| Parameter ID | Parameter | Default | Rationale |
|---|---|---|---|
| `uacc-rsk-02_prm_1` | Applicability trigger | Legally required FRIA, organization-required FRIA, or non-EU rights-impact assessment for consequential use involving material effects on rights, access to services, employment, credit, education, benefits, due process, privacy, safety, or protected/vulnerable groups. | Prevents unreviewed “not applicable” decisions and defines the non-EU equivalent trigger. |
| `uacc-rsk-02_prm_2` | Rights considered | Non-discrimination, privacy/data protection, effective remedy, access to essential services, dignity, and other rights applicable under the EU Charter, sector law, or organizational policy. | Avoids an exhaustive fixed rights taxonomy. |
| `uacc-rsk-02_prm_3` | Affected groups | Protected classes, vulnerable populations, and user/subject groups relevant to the use case. | Centers foreseeable affected populations. |
| `uacc-rsk-02_prm_4` | Minimum content | Process/use description, affected groups, rights impacts, severity/likelihood, mitigations, residual risk, owner, approval, and notification/authority submission where legally required. | Aligns assessment, mitigation, and legal notification evidence. |
| `uacc-rsk-02_prm_5` | Timing | Before first deployment and upon significant change. | Supports Article 27-style pre-use assessment and policy equivalents. |
| `uacc-rsk-02_prm_6` | Approval | Compliance/legal/DPO where applicable. | Rights-impact decisions require accountable review. |

**Applicability [NORMATIVE]:**
- Category: Administrative.
- Risk Tier Applicability: Tier 1 where FRIA, legal-equivalent, or organizational rights-impact trigger applies; document non-applicability rationale for other Tier 1 deployments.
- Actor Applicability: Deployer primary; Provider supporting where needed.
- Organizational Scope: deployments and materially changed uses that trigger FRIA, legal-equivalent, or organization-required rights-impact assessment.
- AI Lifecycle Phase: Development; Deployment.
- Required / Conditional / Informative: Required where a legal FRIA obligation, non-EU rights-impact trigger for consequential use, or organizational rights-impact policy applies. Document non-applicability rationale for Tier 1 deployments that do not require FRIA or equivalent assessment.

**Threat Anchor [CONDITIONAL — included]:** Fundamental-rights harms from consequential automated or AI-assisted decisions, including discrimination, denial of services/opportunities, privacy intrusion, lack of remedy, and compounding impacts on vulnerable groups.

**Sampling Methodology [NORMATIVE, where applicable]:** Review all Tier 1 deployments requiring FRIA during the assessment period.

**Independence Criteria [NORMATIVE, where applicable]:** FRIA approval shall include compliance/legal/DPO review not solely accountable for shipping the affected system.

**Conditional sections omitted [INFORMATIVE]:** Reproducibility Metadata and per-control Exception / Risk-Acceptance Parameters are not triggered by default.

**Assessment Procedures [NORMATIVE]:**
- Examine FRIA reports or documented non-applicability rationales, affected-group analysis, rights-impact assessment, mitigation plan, residual-risk approval, DPO/legal approval, notification/authority submission where required, and cross-reference to bias evaluation and human oversight controls.
- Interview legal/DPO, compliance, and system owner.
- Test FRIA completion before production deployment for sampled applicable systems.

**Pass/Fail Criteria [NORMATIVE]:**
- SATISFIED when applicability is documented, required FRIAs exist before deployment, identify affected groups, assess rights impacts, document mitigations and residual risk, identify owners, include approval, and include required notification/submission evidence where applicable.
- OTHER THAN SATISFIED when applicability is undocumented, FRIA is missing, late, generic, omits affected-group or rights analysis, lacks mitigation ownership, lacks approval, or omits required authority notification/submission evidence.

**Crosswalk [INFORMATIVE]:**

| Framework | Mapping | Confidence | Notes |
|---|---|---|---|
| `[AI-RMF]` | MAP 5.1, MAP 5.2 | Partial | Supports impact analysis and affected-community considerations. |
| `[SP800-53]` | RA-8, PT-5 | Analogical | Maps to privacy/risk assessment concepts. |
| `[EU-AI-ACT]` | Article 27 | Direct | Direct where Article 27 applies, including required authority notification/submission evidence; not all high-risk deployments trigger Article 27. |
| `[ISO42001]` | 6.1.4, A.5.4, A.5.5 | Partial | Supports AI impact assessment and stakeholder considerations. |
| `[COSAIS]` | Rights-impact alignment | Informative | Mapping will be updated when public/final COSAIS materials are available. |

---

### 3.6 UACC-DAT-01: Training Data Lineage and Provenance

**Control Statement [NORMATIVE]:**  
The organization shall maintain lineage and provenance records for datasets used to train, validate, test, or materially update in-scope AI systems, including [Assignment: organization-defined source, rights, transformation, version, and quality metadata].

**Parameter Assignments [NORMATIVE]:**

| Parameter ID | Parameter | Default | Rationale |
|---|---|---|---|
| `uacc-dat-01_prm_1` | Metadata | Data source, collection period, rights basis, transformation steps, dataset version/hash, quality checks, restrictions, retention, and known lineage limitations. | Supports traceability and responsible use decisions. |
| `uacc-dat-01_prm_2` | Rights/provenance evidence | Contract, license, consent/authorization record, data-sharing agreement, vendor attestation, internal policy authorization, or documented legal/privacy basis as applicable. | Makes “rights basis” assessable without prescribing one legal model. |
| `uacc-dat-01_prm_3` | Cadence | Per dataset version and material update. | Lineage must follow the evidence actually used for model development or adaptation. |
| `uacc-dat-01_prm_4` | Owner | Data Steward or Data Engineering Lead. | Assigns accountability for lineage evidence. |
| `uacc-dat-01_prm_5` | Third-party/foundation-model limitation evidence | Vendor provenance statement, model/system card, contractual warranty, data-use restriction, or documented limitation where full training-data lineage is unavailable. | Gives deployers/provider-customers a realistic evidence path. |

**Applicability [NORMATIVE]:**
- Category: Technical / Administrative.
- Risk Tier Applicability: Tier 1 required; Tier 2 recommended.
- Actor Applicability: Provider; Deployer where retraining, fine-tuning, evaluation dataset construction, or material adaptation occurs.
- Organizational Scope: datasets supporting in-scope models.
- AI Lifecycle Phase: Data Preparation; Development; Change Management.
- Required / Conditional / Informative: Required for Tier 1 model development or adaptation.

**Threat Anchor [CONDITIONAL — included]:** Untraceable, unauthorized, stale, poisoned, or mis-specified data can undermine model validity, fairness, privacy, and security.

**Reproducibility Metadata [NORMATIVE, where applicable]:** Dataset identifier/hash, source extract timestamp, transformation code version, quality report ID, lineage graph/version, and responsible role.

**Sampling Methodology [NORMATIVE, where applicable]:** Review all Tier 1 model-development dataset versions where the population is small; otherwise use a risk-based sample that includes material training, validation, testing, fine-tuning, and high-impact transformation datasets.

**Conditional sections omitted [INFORMATIVE]:** Independence Criteria and per-control Exception / Risk-Acceptance Parameters are not triggered by default.

**Assessment Procedures [NORMATIVE]:**
- Examine data lineage records, dataset manifests, rights/provenance evidence, transformation logs, quality reports, lineage limitations, and links to model validation/model cards.
- Interview data steward, model owner, and privacy/legal where rights basis is material.
- Test sampled model versions against referenced dataset lineage.

**Pass/Fail Criteria [NORMATIVE]:**
- SATISFIED when sampled datasets have source, rights/provenance evidence or documented limitation, transformations, versions, quality checks, restrictions, and traceability to model versions.
- OTHER THAN SATISFIED when lineage is missing, transformation/version evidence is not reproducible at a reasonable level, rights/provenance cannot be established or bounded, or material third-party limitations are undisclosed.

**Crosswalk [INFORMATIVE]:**

| Framework | Mapping | Confidence | Notes |
|---|---|---|---|
| `[AI-RMF]` | MAP 2.3 | Partial | Supports data/context understanding. |
| `[SP800-53]` | SR-4, SA-4 | Analogical | Maps to provenance and acquisition/source due-diligence concepts for datasets and third-party data. |
| `[EU-AI-ACT]` | Article 10(2) | Partial | Supports data governance and provenance concepts but does not fully satisfy Article 10. |
| `[ISO42001]` | A.7.4 | Partial | Supports data management evidence in an AIMS. |
| `[COSAIS]` | Data provenance alignment | Informative | Mapping will be updated when public/final COSAIS materials are available. |

---

### 3.7 UACC-MDL-02: Bias and Disparate Impact Testing

**Control Statement [NORMATIVE]:**  
The organization shall evaluate each predictive/decisioning AI model for bias and disparate impact across [Assignment: organization-defined protected attributes] before deployment and upon each retrained or materially changed version; shall use [Assignment: organization-defined fairness metrics, thresholds, and sector parameter pack]; shall document results, limitations, threshold breaches, and remediation actions in a bias evaluation report; and shall obtain approval from [Assignment: organization-defined independent approval role] before production promotion.

**Parameter Assignments [NORMATIVE]:**

| Parameter ID | Parameter | Default | Rationale |
|---|---|---|---|
| `uacc-mdl-02_prm_1` | Protected attributes | Attributes protected by applicable law/policy and attributes relevant to foreseeable disparate impact; when direct attributes are unavailable, document lawful basis, proxy/alternative strategy, limitations, and residual uncertainty. | Prevents performative “not measured” outcomes while respecting legal/data constraints. |
| `uacc-mdl-02_prm_2` | Metric selection rule | Select metrics based on decision context, harm type, target population, available labels, and sector parameter pack; document tradeoffs where fairness metrics conflict. | Fairness metrics are not interchangeable. |
| `uacc-mdl-02_prm_3` | Candidate metric set | Adverse-impact ratio or selection-rate disparity; false positive/false negative parity; equalized odds/equal opportunity; calibration or predictive parity where appropriate; segment performance and error analysis. | Provides a practical menu without requiring every metric. |
| `uacc-mdl-02_prm_4` | Sector parameter pack | Organization-defined pack identifying required attributes, metrics, thresholds, subgroup sample rules, approval roles, and conditional-pass limits for the use case. Example: a credit/lending pack may identify legally permitted protected-attribute handling, adverse-impact ratio, false-positive/false-negative parity, calibration checks, subgroup sample floors, approval role, and conditional-pass duration. | Aligns testing to sector risk and avoids arbitrary thresholds. |
| `uacc-mdl-02_prm_5` | Subgroup sample floor | Soft floor of 100 records per subgroup where feasible; fewer than 30 records requires insufficient-data flag; 30-99 records may be used with caution, confidence/uncertainty notation, and reviewer rationale. | Makes small-population handling explicit. |
| `uacc-mdl-02_prm_6` | Evaluation frequency | Before deployment, before each production promotion of retrained/materially changed versions, and at least annually for Tier 1 systems. | Keeps evidence current across model changes. |
| `uacc-mdl-02_prm_7` | Independent approval role | Model Risk, Independent Validation, Compliance Analytics, or equivalent role separated from model development/product ownership. | Supports credible gatekeeping. |
| `uacc-mdl-02_prm_8` | Conditional-pass duration | Maximum 90 calendar days unless stricter sector pack or legal/risk authority requires shorter duration. | Prevents open-ended production use with unresolved fairness risk. |

**Applicability [NORMATIVE]:**
- Category: Technical.
- Risk Tier Applicability: Tier 1 required.
- Actor Applicability: Provider; Deployer when modifying/adapting or when provider evidence is insufficient.
- Organizational Scope: fairness metric rules, threshold catalogs, sector packs, and approval-role definitions.
- AI Lifecycle Phase: Development; Deployment gate; Operations through monitoring.
- Required / Conditional / Informative: Required for Tier 1 predictive/decisioning models.

**Threat Anchor [CONDITIONAL — included]:** Bias/disparate impact, manipulated or poisoned data/model behavior, and Annex III high-risk decision harms.

**Sampling Methodology [NORMATIVE, where applicable]:** Define evaluation population, assessment period, subgroup sample floor, stratification, random/stratified sampling, and insufficient-data rules. Where protected attributes or labels are unavailable, document the lawful basis analysis, proxy/alternative method if used, limitations, and residual risk.

**Reproducibility Metadata [NORMATIVE, where applicable]:** Minimum evidence includes model version/hash where available, dataset version, evaluation date, evaluation code/notebook version, evaluator, and result file/report ID. Mature evidence may also include dataset hash, evaluation code SHA, seeds, environment/container digest, result hash, and evidence-event ID.

**Independence Criteria [NORMATIVE, where applicable]:** Reviewer shall be separated from model development/product ownership, shall not author the evaluated pipeline/report, shall have relevant competence, and shall have authority to block promotion.

**Exception / Risk-Acceptance Parameters [CONDITIONAL — included]:** Conditional pass requires compensating controls, independent approval plus risk/legal authority where applicable, maximum duration, re-evaluation cadence, and exception-register linkage.

**Assessment Procedures [NORMATIVE]:**
- Examine `EVD-05` or equivalent reports, metric rules, sector packs, protected-attribute rationale, model registry/promotions, approvals, remediation and monitoring.
- Interview model owner, validator, MLOps, compliance/legal.
- Test promotion gate, threshold-breach handling, insufficient-data handling, and reproducibility evidence.

**Pass/Fail Criteria [NORMATIVE]:**
- SATISFIED when all sampled in-scope model versions have completed bias evaluation, documented metrics/thresholds/attributes or lawful alternative rationale, sector pack, reproducibility evidence, independent approval, handled breaches/insufficient-data findings, and enforced promotion gates.
- OTHER THAN SATISFIED when any model is promoted without required testing/approval, metric/threshold choices are arbitrary or undocumented, protected-attribute limitations are ignored, breaches lack treatment, or conditional pass exceeds approved limits.

**Crosswalk [INFORMATIVE]:**

| Framework | Mapping | Confidence | Notes |
|---|---|---|---|
| `[AI-RMF]` | MEASURE 2.11 | Direct | Directly supports bias/disparate-impact evaluation. |
| `[AI-RMF]` | MEASURE 2.6, MEASURE 2.7 | Partial | Supports performance/fairness measurement. |
| `[SP800-53]` | RA-3, SI-4 | Analogical | Maps to risk and monitoring concepts; AI-specific tailoring may be refined when public/final COSAIS materials are available. |
| `[EU-AI-ACT]` | Articles 9, 10, 15, 27 | Partial | Supports risk, data, accuracy/robustness, and FRIA evidence; does not complete legal obligations. |
| `[ISO42001]` | A.6.2.4, 9.1 | Partial | Supports assessment and monitoring within an AIMS. |
| `[COSAIS]` | Bias-testing alignment | Informative | Mapping will be updated when public/final COSAIS materials are available. |

---

### 3.8 UACC-MON-01: Model Performance Monitoring

**Control Statement [NORMATIVE]:**  
The organization shall monitor deployed in-scope AI systems against [Assignment: organization-defined performance metrics, operational thresholds, and alert criteria], investigate threshold breaches, and document corrective actions.

**Parameter Assignments [NORMATIVE]:**

| Parameter ID | Parameter | Default | Rationale |
|---|---|---|---|
| `uacc-mon-01_prm_1` | Monitoring metric classes | Operational telemetry; data-quality/drift indicators; score/output distribution; override/appeal/complaint rates; outcome/performance metrics where labels or valid outcomes are available; delayed-label backtesting where outcomes arrive later. | Avoids assuming real-time ground truth while preserving monitoring expectations. |
| `uacc-mon-01_prm_2` | Threshold rationale | Metric and threshold selection documented against intended use, validation results, risk assessment, and sector parameter pack where applicable. | Prevents arbitrary alert criteria. |
| `uacc-mon-01_prm_3` | Review cadence | Continuous or event-driven telemetry with at least monthly formal review for Tier 1, including documented no-alert review where no breaches occur. | Ensures periodic evidence even during quiet periods. |
| `uacc-mon-01_prm_4` | Escalation path | Model owner, MLOps/model operations, governance/risk, and provider/vendor contact where telemetry is vendor-operated. | Supports follow-up across operational models. |

**Applicability [NORMATIVE]:**
- Category: Operational / Technical.
- Risk Tier Applicability: Tier 1 required.
- Actor Applicability: Provider where operating post-market monitoring; Deployer where operating system in production or relying on vendor monitoring evidence.
- Organizational Scope: production systems.
- AI Lifecycle Phase: Operations.
- Required / Conditional / Informative: Required for Tier 1 production systems.

**Threat Anchor [CONDITIONAL — included]:** Silent performance degradation, model drift, data-quality degradation, and operational failures causing unreliable decisions.

**Sampling Methodology [NORMATIVE, where applicable]:** Review monitoring coverage for all Tier 1 production systems and sample alerts/breaches from the assessment period. Where no alerts occurred, sample monthly review records, dashboard exports, or no-breach attestations to verify monitoring was active.

**Reproducibility Metadata [NORMATIVE, where applicable]:** Monitoring configuration version, metric definitions, data window, dashboard/export timestamp, alert ID, incident/ticket ID, and model version.

**Exception / Risk-Acceptance Parameters [CONDITIONAL — included]:** Disabled telemetry, missing required metrics, accepted threshold breaches, or prolonged monitoring outages require documented compensating controls, accountable approval, expiration/review date, and exception-register linkage.

**Conditional sections omitted [INFORMATIVE]:** Independence Criteria are not triggered by default.

**Assessment Procedures [NORMATIVE]:**
- Examine dashboards, metric definitions, threshold rationale, alert configs, alert logs, no-alert review records, breach investigations, corrective actions, and vendor monitoring evidence where applicable.
- Interview MLOps/model operations and system owner.
- Test sampled alerts for routing and closure.

**Pass/Fail Criteria [NORMATIVE]:**
- SATISFIED when monitoring is active for sampled systems, metrics and thresholds are defined with rationale, alerts route to owners, breaches are investigated, no-alert periods still show review evidence, and corrective actions are tracked.
- OTHER THAN SATISFIED when monitoring is disabled/incomplete without approved exception, threshold rationale is absent, no-alert periods cannot be evidenced, or breaches are ignored.

**Crosswalk [INFORMATIVE]:**

| Framework | Mapping | Confidence | Notes |
|---|---|---|---|
| `[AI-RMF]` | MEASURE 3.1, MEASURE 3.2, MANAGE 4.1 | Partial | Supports operational monitoring and response. |
| `[SP800-53]` | SI-4, CA-7 | Analogical | Maps to system monitoring/continuous assessment concepts. |
| `[EU-AI-ACT]` | Articles 17, 26(5), 72 | Partial | Supports QMS, deployer monitoring, and post-market monitoring evidence where role-specific obligations apply. |
| `[ISO42001]` | 9.1, A.6.2.6 | Partial | Supports performance evaluation and operational monitoring in an AIMS. |
| `[COSAIS]` | Monitoring alignment | Informative | Mapping will be updated when public/final COSAIS materials are available. |

---

### 3.9 UACC-MON-04: Audit Logging for Decision Traceability

**Control Statement [NORMATIVE]:**  
The organization shall log AI-assisted decisions with sufficient metadata to reconstruct the decision, including [Assignment: organization-defined log fields], protect logs from unauthorized alteration, and retain logs for [Assignment: organization-defined retention period].

**Parameter Assignments [NORMATIVE]:**

| Parameter ID | Parameter | Default | Rationale |
|---|---|---|---|
| `uacc-mon-04_prm_1` | Log fields | Request ID, timestamp, system/model version, input references or hashes, output/decision reference, confidence/score where applicable, human override/intervention, operator identity where applicable, and downstream decision reference. | Supports reconstruction without requiring raw sensitive payloads in every case. |
| `uacc-mon-04_prm_2` | Retention period | Organization-defined with documented rationale tied to legal/regulatory obligations, appeal/remedy windows, incident investigation, audit needs, privacy/data-minimization requirements, and vendor/customer contracts. For Tier 1 production decisioning workflows, the default minimum is the longer of six months or the applicable appeal/remedy window plus a reasonable investigation period, unless a shorter period is required by law or approved through documented privacy/security risk acceptance with compensating evidence preservation. Longer retention applies where required by law, contract, incident-response needs, or sector policy. | Makes retention assessable, prevents treating a six-month floor as universally sufficient, and remains bounded by privacy/data-minimization obligations. |
| `uacc-mon-04_prm_3` | Integrity protection | Tamper-evident storage or equivalent, such as append-only logging, restricted admin access, signed/hash batches, object lock/WORM, SIEM immutability, or separately stored hash manifests. | Provides realistic maturity paths for integrity evidence. |
| `uacc-mon-04_prm_4` | Confidentiality/minimization controls | Access restriction, purpose limitation, sensitive-field redaction/tokenization where feasible, and data-classification alignment. | Prevents over-logging from creating privacy or security risk. |

**Applicability [NORMATIVE]:**
- Category: Technical.
- Risk Tier Applicability: Tier 1 required.
- Actor Applicability: Provider and Deployer according to operational role.
- Organizational Scope: production decisioning workflows.
- AI Lifecycle Phase: Operations; Incident Response; Audit.
- Required / Conditional / Informative: Required for Tier 1 production decisioning workflows and other systems where appeal, accountability, incident, or legal traceability is required. Document non-applicability rationale for excluded Tier 1 workflows.

**Threat Anchor [CONDITIONAL — included]:** Missing traceability prevents accountability, appeal, incident investigation, and root-cause analysis.

**Sampling Methodology [NORMATIVE, where applicable]:** Sample production decisions and reconstruct from logs; include decisions with overrides, adverse outcomes, and incidents where available.

**Reproducibility Metadata [NORMATIVE, where applicable]:** Log schema version, extraction query, extraction timestamp, hash/integrity proof, model version, and reconstruction test ID.

**Conditional sections omitted [INFORMATIVE]:** Independence Criteria and per-control Exception / Risk-Acceptance Parameters are not triggered by default.

**Assessment Procedures [NORMATIVE]:**
- Examine log schema, retention rationale, access controls, minimization controls, integrity controls, sample logs, and reconstruction tests.
- Interview security/MLOps.
- Test reconstruction of sampled decisions.

**Pass/Fail Criteria [NORMATIVE]:**
- SATISFIED when sampled decisions are reconstructable for the applicable retention period, required fields or references are present, logs are protected for integrity and confidentiality, the retention rationale meets the Tier 1 default minimum or has an approved documented exception, retention is technically enforced, and sensitive data is minimized or protected.
- OTHER THAN SATISFIED when critical fields are missing, integrity/confidentiality cannot be shown, retention is unsupported, materially shorter than the applicable default without approved rationale, not technically enforced, or reconstruction fails.

**Crosswalk [INFORMATIVE]:**

| Framework | Mapping | Confidence | Notes |
|---|---|---|---|
| `[AI-RMF]` | GOVERN 1.4, MEASURE 2.3 | Partial | Supports transparent risk-management controls and documented assurance/measurement evidence. |
| `[SP800-53]` | AU-2, AU-3, AU-9, AU-11, AU-12 | Partial | Supports event logging, log content, log protection, and retention; the gap is AI-specific decision metadata. |
| `[EU-AI-ACT]` | Articles 12, 19, 26(5) | Partial | Supports logging, retention, and deployer monitoring evidence; does not by itself implement Article 12 design requirements. |
| `[ISO42001]` | A.6.2.8 | Partial | Supports recording and reporting concepts relevant to operational decision traceability. |
| `[COSAIS]` | Logging alignment | Informative | Mapping will be updated when public/final COSAIS materials are available. |

---

### 3.10 UACC-HUM-01: Human Oversight Mechanism Design

**Control Statement [NORMATIVE]:**  
The organization shall design, implement, test, and maintain human oversight mechanisms that enable qualified human overseers to understand AI system outputs, decide not to use or override outputs, and interrupt or escalate system operation where appropriate.

**Parameter Assignments [NORMATIVE]:**

| Parameter ID | Parameter | Default | Rationale |
|---|---|---|---|
| `uacc-hum-01_prm_1` | Oversight capabilities | Understand, monitor, decide not to use or override outputs, escalate, document rationale, and interrupt, pause, or stop system operation where the workflow or system design supports such intervention. Where interruption/pause/stop is not technically feasible, document the feasibility basis, residual risk, and compensating controls such as pre-deployment gating, rollback, kill-switch at an upstream/downstream control point, post-decision review, or incident escalation. | Aligns oversight with practical intervention authority without allowing unsupported infeasibility claims. |
| `uacc-hum-01_prm_2` | Effectiveness criteria | Overseer has workflow-specific training, sufficient context or explanation/reason codes where appropriate, authority to override or escalate, usable interface controls, documented escalation path, and workload/alert burden that allows meaningful review. | Prevents nominal human-in-the-loop controls. |
| `uacc-hum-01_prm_3` | Test cadence | Pre-deployment, at least annually for Tier 1, and after significant workflow/interface change. | Keeps oversight mechanisms current. |
| `uacc-hum-01_prm_4` | Authorized roles | Organization-defined roles with documented qualifications/training. | Ensures the oversight role is assigned and competent. |

**Applicability [NORMATIVE]:**
- Category: Technical / Operational.
- Risk Tier Applicability: Tier 1 required.
- Actor Applicability: Deployer primary for operational use; Provider supports design where Article 14-style design obligations or customer commitments apply.
- Organizational Scope: workflows using in-scope AI outputs.
- AI Lifecycle Phase: Development; Deployment; Operations.
- Required / Conditional / Informative: Required for Tier 1 systems requiring human oversight. For Tier 1 systems where a specific oversight capability is not used or not technically feasible, document the capability-specific rationale, approval, residual risk, compensating controls, and review date. Infeasibility of interruption/pause/stop does not remove the requirement for meaningful human review, override/non-use authority where applicable, escalation, and oversight records.

**Threat Anchor [CONDITIONAL — included]:** Nominal or ineffective oversight can fail to prevent harmful automated or AI-assisted decisions.

**Sampling Methodology [NORMATIVE, where applicable]:** Sample oversight workflows, override records, adverse/appealed decisions, and test cases for escalation/interruption functions. Include high-volume or high-consequence workflows where available.

**Reproducibility Metadata [NORMATIVE, where applicable]:** Test case ID, system version, role/access profile, test timestamp, output/override evidence, and tester identity.

**Exception / Risk-Acceptance Parameters [CONDITIONAL — included]:** Unavailable, disabled, untested, or materially ineffective oversight requires documented compensating controls, accountable approval, expiration/review date, and exception-register linkage.

**Conditional sections omitted [INFORMATIVE]:** Independence Criteria are not triggered by default.

**Assessment Procedures [NORMATIVE]:**
- Examine oversight design, interface evidence, RBAC, override/interruption tests, logs, training/qualification records, workload or queue evidence where relevant, and escalation records.
- Interview overseers and product/engineering.
- Test override/interruption/escalation functions.

**Pass/Fail Criteria [NORMATIVE]:**
- SATISFIED when oversight mechanisms exist, are tested, usable by authorized and trained roles, provide sufficient context and time for meaningful review, allow override/non-use and escalation where applicable, support interruption/pause/stop where technically feasible, document justified non-feasibility and compensating controls where not feasible, and produce records with rationale.
- OTHER THAN SATISFIED when oversight is unavailable, merely nominal, impractical, untested, lacks authority/training/context/time, lacks records, or claims technical infeasibility without documented basis, approval, residual-risk treatment, and compensating controls.

**Crosswalk [INFORMATIVE]:**

| Framework | Mapping | Confidence | Notes |
|---|---|---|---|
| `[AI-RMF]` | GOVERN 3.2 | Partial | Supports human roles and accountability. |
| `[SP800-53]` | AC-3, AC-6 | Analogical | Maps to access/privilege concepts for authorized oversight roles. |
| `[EU-AI-ACT]` | Articles 14, 26 | Partial | Supports provider-side oversight design and deployer-side competent use; does not by itself satisfy all role-specific obligations. |
| `[ISO42001]` | A.9.3, A.6.2.6 | Partial | Supports human oversight and operational control in an AIMS. |
| `[COSAIS]` | Human oversight alignment | Informative | Mapping will be updated when public/final COSAIS materials are available. |

---

### 3.11 UACC-INC-02: Serious Incident Reporting Workflow

**Control Statement [NORMATIVE]:**  
The organization shall define, test, and operate a serious AI incident reporting workflow that classifies incidents, determines reporting obligations and timelines, notifies responsible parties, preserves evidence, and tracks corrective actions.

**Parameter Assignments [NORMATIVE]:**

| Parameter ID | Parameter | Default | Rationale |
|---|---|---|---|
| `uacc-inc-02_prm_1` | Severity criteria | Death or serious health harm; serious and irreversible critical-infrastructure disruption; serious infringement of fundamental-rights obligations; serious harm to property or environment; regulator-defined serious incident; or organizationally defined serious AI incident. | Anchors classification to consequence-based thresholds. |
| `uacc-inc-02_prm_2` | Reporting matrix | Jurisdiction/regulator, actor role, reportable event type, clock-start definition, internal escalation SLA, external notification deadline, accountable owner, and evidence-preservation steps. | Makes “organization-defined based on applicable law” assessable. |
| `uacc-inc-02_prm_3` | EU AI Act timing reference | Where Article 73 applies, report after causal link or reasonable likelihood is established and within applicable statutory outer limits, including shorter windows for specified severe events. | Avoids replacing statutory timing with an internal SLA. |
| `uacc-inc-02_prm_4` | Responsible roles | Incident response, compliance/legal, model/system owner, provider/vendor contact, communications where needed, and authority liaison where applicable. | Coordinates operational and legal response. |

**Applicability [NORMATIVE]:**
- Category: Operational.
- Risk Tier Applicability: Tier 1 required.
- Actor Applicability: Provider, Deployer, Importer, Distributor, Authorized Representative where reporting obligations apply. Provider-facing reporting may be primary under some regimes; deployers may have immediate provider/authority notification or suspension duties where applicable.
- Organizational Scope: production AI systems and reportable pre-production events where policy requires.
- AI Lifecycle Phase: Operations; Incident Response.
- Required / Conditional / Informative: Required where serious incident obligations or policy apply.

**Threat Anchor [CONDITIONAL — included]:** Delayed or incomplete serious incident reporting increases harm, regulatory exposure, and loss of evidence.

**Sampling Methodology [NORMATIVE, where applicable]:** Review all serious incidents in the assessment period and a sample of near-miss or lower-severity AI incidents to test classification.

**Reproducibility Metadata [NORMATIVE, where applicable]:** Incident ID, detection timestamp, classification timestamp, reporting clock start, evidence hashes/links, notification records, and corrective-action IDs.

**Independence Criteria [NORMATIVE, where applicable]:** Serious incident classification shall include compliance/legal review independent from the team solely accountable for the affected system.

**Exception / Risk-Acceptance Parameters [CONDITIONAL — included]:** Reporting deadlines shall not be waived where legal obligations apply. Internal deadline extensions require documented legal/compliance approval and rationale.

**Assessment Procedures [NORMATIVE]:**
- Examine incident playbook, severity matrix, reporting matrix, legal timeline mapping, prohibited-practice/T0 escalation handling, case records, notification evidence, timestamps including reporting-clock start, corrective-action tracker, and exercises.
- Interview incident response and compliance/legal.
- Test tabletop or sampled cases for classification and timeline conformance.

**Pass/Fail Criteria [NORMATIVE]:**
- SATISFIED when workflow exists, responsibilities are assigned, incidents are classified using defined criteria, prohibited-practice/T0 findings are escalated for legal/compliance review and suspension/withdrawal decision where applicable, reporting-clock start and legal determination are documented, required notifications occur on time, evidence is preserved, and corrective actions are tracked.
- OTHER THAN SATISFIED when reporting criteria are undefined, prohibited-practice/T0 escalation handling is absent where such findings occur, legal timeline mapping or clock start is missing, notifications are late/missing, evidence preservation fails, or corrective actions are unmanaged.

**Crosswalk [INFORMATIVE]:**

| Framework | Mapping | Confidence | Notes |
|---|---|---|---|
| `[AI-RMF]` | MANAGE 4.1 | Partial | Supports monitoring risks/incidents and taking response actions. |
| `[SP800-53]` | IR-6, IR-8 | Partial | Supports incident reporting and incident response planning; the gap is AI-specific incident classification and legal timing. |
| `[EU-AI-ACT]` | Article 73 | Direct | Direct where Article 73 applies and statutory timing/role obligations are mapped; does not cover all incident obligations outside that scope. |
| `[ISO42001]` | A.8.4, A.8.3 | Partial | Supports communication of incidents and external reporting concepts. |
| `[COSAIS]` | Incident reporting alignment | Informative | Mapping will be updated when public/final COSAIS materials are available. |

---

## 4. References

- `[AI-RMF]` NIST AI Risk Management Framework 1.0.
- `[SP800-53]` NIST SP 800-53 Rev. 5.
- `[EU-AI-ACT]` Regulation (EU) 2024/1689.
- `[ISO42001]` ISO/IEC 42001:2023.
- `[COSAIS]` COSAIS public materials.

## 5. Change history

| Date | Change |
|---|---|
| 2026-06-06 | Expanded all 11 hardened controls for public-draft assessability, conservative crosswalk labels, evidence expectations, and implementation caveats. |
| 2026-06-04 | Defined the public v0.2 hardened core as 11 controls, including `UACC-GOV-01`. |
