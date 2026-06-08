# UACC v0.2 Control Index

**Version:** 0.2 Public Draft  
**Status:** Public draft / working reference  
**Scope:** Full 35-control base catalog index; 11 controls hardened in v0.2  
**Audience:** Evaluators, implementers, assessors, contributors, and reviewers  
**License:** CC BY 4.0  
**Last updated:** 2026-06-06

> UACC is an open working reference catalog. It does not provide legal advice, certify compliance, replace conformity assessment, or create a regulatory safe harbor. Crosswalks identify areas of overlap and potential evidence reuse; they do not establish equivalence between frameworks.

This index gives a fast view of the full UACC base catalog. The v0.2 public draft hardens 11 controls to assessor-grade depth and keeps the remaining 24 controls visible as the public roadmap for future hardening.

GenAI overlay controls (`UACC-GEN-*`) are documented separately in the GenAI overlay. This index covers the predictive/decisioning base catalog.

The crosswalk-at-a-glance column is a simplified orientation aid. The full control catalog and crosswalk document remain authoritative for exact mapping language, confidence labels, and citations.

## Status legend

| Status | Meaning |
|---|---|
| Hardened v0.2 | Included in the v0.2 public control catalog with full assessor-grade detail. |
| Working reference | Valid base-catalog control retained at reference depth; planned for future hardening. |

## Risk tier quick reference

UACC risk tiers describe AI-system governance and assurance depth. They are not the same as NIST Low, Moderate, and High impact baselines.

| UACC tier | Working meaning | Typical control implication |
|---|---|---|
| Tier 0 / T0 | Prohibited AI use under applicable law, policy, or organizational risk appetite. | Do not deploy or continue operation; escalate for legal/compliance review, disable or withdraw the use, and preserve decision records. |
| Tier 1 / T1 | High-risk or high-impact AI use, including systems treated as high-risk under applicable law, policy, or organizational classification. | Full assessor-grade evidence, stronger approval, monitoring, oversight, and incident expectations. |
| Tier 2 / T2 | Limited-risk AI use with material transparency, operational, or governance obligations but not full high-risk treatment. | Baseline governance, inventory, classification, transparency, and proportionate monitoring/evidence. |
| Tier 3 / T3 | Minimal-risk AI use with low expected impact on rights, safety, access to services, or material decisions. | Lightweight inventory, policy coverage, and risk classification; additional controls only when triggered. |

### Relationship to NIST Low / Moderate / High

NIST Low / Moderate / High impact baselines classify information systems by potential impact to confidentiality, integrity, and availability. UACC Tier 1 / Tier 2 / Tier 3 classify AI use by governance, safety, rights, transparency, and compliance risk. They can be used together, but they do not convert one-for-one.

| NIST impact baseline | UACC relationship |
|---|---|
| Low | A NIST Low system can still contain a Tier 1 AI use if the AI materially affects rights, access, safety, employment, credit, insurance, education, law enforcement, or other high-impact decisions. |
| Moderate | A common pairing for production enterprise AI. The NIST baseline addresses system security impact; UACC adds AI-specific evidence, oversight, monitoring, and crosswalk obligations. |
| High | A NIST High system still needs UACC tiering for AI-specific risk. A Tier 3 AI feature inside a NIST High system inherits strong security controls, but does not automatically become Tier 1 for AI governance unless the AI use itself is high-risk. |

In practice, apply the stricter requirement from either dimension: use NIST/FedRAMP-style baselines for information-system security impact and UACC tiers for AI-specific governance and assurance depth.

How tiers are determined: see `UACC-INV-02` in the control catalog and the tier determination methodology in `uacc_v02_methodology.md`.

## Hardened-core quick view

| Control ID | Title | Domain | One-line pass/fail focus | Primary evidence | Crosswalk-at-a-glance |
|---|---|---|---|---|---|
| `UACC-GOV-01` | AI Governance Policy | Governance | Policy is approved, communicated, current, AI-specific, and mapped to authority and scope. | AI governance policy; EVD-01 for scope verification | NIST AI RMF GOVERN; SP 800-53 PM/PL; EU AI Act Art. 17; ISO/IEC 42001 Clause 5 / Annex A.2 |
| `UACC-INV-01` | AI System Inventory | Inventory | Inventory is current and reconciled against available business/system records. | EVD-01 | NIST AI RMF GOVERN/MAP; SP 800-53 CM/PM; EU AI Act Art. 49; ISO/IEC 42001 Annex A.4 |
| `UACC-INV-02` | Risk Classification with Documented Rationale | Inventory | Each system has a documented risk classification with rationale and approval. | EVD-02 | NIST AI RMF MAP; SP 800-53 RA; EU AI Act Art. 6 / Annex III; ISO/IEC 42001 risk assessment |
| `UACC-RSK-01` | Pre-Deployment AI Risk Assessment | Risk | Material risks and foreseeable misuse are assessed before deployment or significant change. | EVD-03 | NIST AI RMF MAP; SP 800-53 RA; EU AI Act Art. 9; ISO/IEC 42001 risk assessment/execution |
| `UACC-RSK-02` | Fundamental Rights Impact Assessment (FRIA) | Risk | Deployments with FRIA, equivalent rights-impact, or organizational rights-impact triggers complete the assessment before use and update it on material change. | EVD-04 | NIST AI RMF MAP; SP 800-53 privacy/risk; EU AI Act Art. 27; ISO/IEC 42001 impact assessment |
| `UACC-DAT-01` | Training Data Lineage and Provenance | Data | Training/validation/test data lineage is documented, versioned, and traceable. | EVD-09 | NIST AI RMF MAP; SP 800-53 SA/SR; EU AI Act Art. 10; ISO/IEC 42001 Annex A.7 |
| `UACC-MDL-02` | Bias and Disparate Impact Testing | Model | Bias/disparate-impact tests meet thresholds or trigger remediation before promotion. | EVD-05 | NIST AI RMF MEASURE; SP 800-53 RA/SI; EU AI Act Arts. 9/10; ISO/IEC 42001 validation/responsible use |
| `UACC-MON-01` | Model Performance Monitoring | Monitoring | Deployed performance is monitored with thresholds, alerts, investigation, and response. | Monitoring exports; alert logs | NIST AI RMF MEASURE/MANAGE; SP 800-53 SI/CA; EU AI Act Arts. 17/72; ISO/IEC 42001 monitoring |
| `UACC-MON-04` | Audit Logging for Decision Traceability | Monitoring | Decision logs preserve required metadata and integrity for reconstruction and audit. | Audit log sample; retention/integrity evidence | NIST AI RMF MEASURE/GOVERN; SP 800-53 AU; EU AI Act Arts. 12/19/26; ISO/IEC 42001 recording/reporting |
| `UACC-HUM-01` | Human Oversight Mechanism Design | Human Oversight | Qualified humans can interpret outputs, override decisions, and interrupt operation where required. | EVD-12 | NIST AI RMF GOVERN; SP 800-53 AC; EU AI Act Arts. 14/26; ISO/IEC 42001 responsible operation |
| `UACC-INC-02` | Serious Incident Reporting Workflow | Incident Response | Serious AI incidents can be classified, escalated, and reported within required timelines. | EVD-15 | NIST AI RMF MANAGE; SP 800-53 IR; EU AI Act Art. 73; ISO/IEC 42001 incident communication |

## Full 35-control base catalog index

| Control ID | Title | Domain | Status | Risk tier | Primary evidence | Implementation focus | Crosswalk-at-a-glance |
|---|---|---|---|---|---|---|---|
| `UACC-GOV-01` | AI Governance Policy | Governance | Hardened v0.2 | T1, T2, T3 | AI governance policy; EVD-01 for scope verification | Establish AI-specific policy, scope, principles, decision authority, and review cadence. | AI RMF GOVERN; SP 800-53 PM/PL; EU AI Act Art. 17; ISO/IEC 42001 Clause 5 / Annex A.2 |
| `UACC-GOV-02` | AI Decision Rights and Accountability Matrix | Governance | Working reference | T1, T2 | AI RACI matrix; governance committee charter; escalation procedures | Define lifecycle roles, decision rights, named accountable owners, and escalation paths. | AI RMF GOVERN; SP 800-53 PM; EU AI Act Art. 17; ISO/IEC 42001 Clause 5 / Annex A.3 |
| `UACC-GOV-03` | AI Literacy and Competence Program | Governance | Working reference | T1, T2, T3 | Training syllabus; completion records; competence assessments | Ensure AI-involved personnel complete role-appropriate AI literacy and competence training. | AI RMF GOVERN; SP 800-53 AT; EU AI Act Art. 4 / Art. 14; ISO/IEC 42001 Clauses 7.2/7.3 |
| `UACC-GOV-04` | AI Audit and Governance Review Cadence | Governance | Working reference | T1 | Governance review plan; audit reports; finding tracker | Review AI governance, compliance, fairness, performance, and remediation on a recurring cadence. | AI RMF GOVERN; SP 800-53 CA/PM; EU AI Act Art. 17; ISO/IEC 42001 Clauses 9.2/9.3 |
| `UACC-INV-01` | AI System Inventory | Inventory | Hardened v0.2 | T1, T2, T3 | EVD-01 | Maintain a current inventory and reconcile it against available business/system records. | AI RMF GOVERN/MAP; SP 800-53 CM/PM; EU AI Act Art. 49; ISO/IEC 42001 Annex A.4 |
| `UACC-INV-02` | Risk Classification with Documented Rationale | Inventory | Hardened v0.2 | T1, T2, T3 | EVD-02 | Classify systems by risk tier and document rationale, derogations, and approval. | AI RMF MAP; SP 800-53 RA; EU AI Act Art. 6 / Annex III; ISO/IEC 42001 risk assessment |
| `UACC-INV-03` | Shadow AI Detection | Inventory | Working reference | T1, T2 | EVD-01 plus discovery scan report | Actively discover unregistered AI use and route findings to inventory/classification. | AI RMF GOVERN/MAP; SP 800-53 CM/SA; EU AI Act Art. 26; ISO/IEC 42001 scope/resource documentation |
| `UACC-RSK-01` | Pre-Deployment AI Risk Assessment | Risk | Hardened v0.2 | T1 | EVD-03 | Assess known and foreseeable risks, misuse, severity, likelihood, mitigations, and residual risk before deployment. | AI RMF MAP; SP 800-53 RA; EU AI Act Art. 9; ISO/IEC 42001 risk assessment/execution |
| `UACC-RSK-02` | Fundamental Rights Impact Assessment (FRIA) | Risk | Hardened v0.2 | T1 | EVD-04 | Assess impacts on affected people and groups before deployment where FRIA, equivalent rights-impact, or organizational rights-impact triggers apply. | AI RMF MAP; SP 800-53 RA/PT; EU AI Act Art. 27; ISO/IEC 42001 impact assessment |
| `UACC-RSK-03` | Residual Risk Communication to Deployers | Risk | Working reference | T1 | EVD-03; EVD-11 | Communicate residual risks, limitations, required mitigations, and foreseeable misuse to deployers. | AI RMF GOVERN/MANAGE; SP 800-53 SA/PL; EU AI Act Arts. 9/13; ISO/IEC 42001 documentation |
| `UACC-DAT-01` | Training Data Lineage and Provenance | Data | Hardened v0.2 | T1 | EVD-09 | Document dataset provenance, transformations, versions, hashes, and limitations. | AI RMF MAP; SP 800-53 SA/SR; EU AI Act Art. 10; ISO/IEC 42001 Annex A.7 |
| `UACC-DAT-02` | Training Data Quality Assessment | Data | Working reference | T1 | EVD-10 | Assess completeness, accuracy, representativeness, schema validity, and fitness for purpose. | AI RMF MAP/MEASURE; SP 800-53 SI/SA; EU AI Act Art. 10; ISO/IEC 42001 Annex A.7 |
| `UACC-DAT-03` | Pre-Training Bias Examination | Data | Working reference | T1 | EVD-05 section 2 | Examine datasets for bias across relevant protected or affected-group attributes before training. | AI RMF MAP/MEASURE; SP 800-53 RA/SI; EU AI Act Art. 10; ISO/IEC 42001 responsible-use/data controls |
| `UACC-DAT-04` | Special Category Personal Data Safeguards | Data | Working reference | T1 | DPIA; safeguard implementation record; DPO sign-off | Govern special-category data processing for bias detection/correction with safeguards. | AI RMF GOVERN; SP 800-53 PT; EU AI Act Art. 10; ISO/IEC 42001 data/impact controls |
| `UACC-MDL-01` | Pre-Production Model Validation | Model | Working reference | T1 | EVD-07 | Validate declared model performance and block release on unacceptable regression. | AI RMF MEASURE; SP 800-53 CA/SA; EU AI Act Arts. 9/15; ISO/IEC 42001 validation/monitoring |
| `UACC-MDL-02` | Bias and Disparate Impact Testing | Model | Hardened v0.2 | T1 | EVD-05 | Test fairness metrics, adverse-impact ratios, thresholds, remediation, approval, and reproducibility. | AI RMF MEASURE; SP 800-53 RA/SI; EU AI Act Arts. 9/10; ISO/IEC 42001 validation/responsible use |
| `UACC-MDL-03` | Model Card Generation | Model | Working reference | T1, T2 | EVD-06 | Produce model cards covering purpose, data, evaluation, limitations, fairness, ownership, and escalation. | AI RMF MAP; SP 800-53 SA; EU AI Act Art. 11 / Annex IV; ISO/IEC 42001 technical documentation |
| `UACC-MDL-04` | Adversarial Robustness Testing | Model | Working reference | T1 | EVD-08 | Test relevant adversarial inputs, manipulation, evasion, and distribution-shift scenarios. | AI RMF MEASURE; SP 800-53 SA/SI; EU AI Act Art. 15; ISO/IEC 42001 validation |
| `UACC-TRN-01` | Instructions for Use | Transparency | Working reference | T1 | EVD-11 | Provide deployer-facing instructions, limitations, performance characteristics, and oversight measures. | AI RMF MAP/GOVERN; SP 800-53 SA/PL; EU AI Act Art. 13; ISO/IEC 42001 documentation/user information |
| `UACC-TRN-02` | Decision Explainability Artifacts | Transparency | Working reference | T1 | Explainability artifacts; model documentation | Generate artifacts that help deployers and affected individuals understand decision factors. | AI RMF MAP/MEASURE; SP 800-53 PL/PT; EU AI Act Art. 13; ISO/IEC 42001 documentation |
| `UACC-TRN-03` | Affected Individual Notification | Transparency | Working reference | T1 | EVD-11; notification template and delivery audit | Notify affected individuals of high-risk AI use and provide meaningful decision information. | AI RMF GOVERN; SP 800-53 PT; EU AI Act Arts. 50/26; ISO/IEC 42001 interested-party information |
| `UACC-HUM-01` | Human Oversight Mechanism Design | Human Oversight | Hardened v0.2 | T1 | EVD-12 | Design oversight interfaces and mechanisms for interpretation, override, and interruption. | AI RMF GOVERN; SP 800-53 AC; EU AI Act Arts. 14/26; ISO/IEC 42001 responsible operation |
| `UACC-HUM-02` | Human Overseer Qualification | Human Oversight | Working reference | T1 | EVD-12 | Designate overseers with documented authority, competence, and system-specific training. | AI RMF GOVERN; SP 800-53 PS/AT; EU AI Act Art. 14; ISO/IEC 42001 competence/human resources |
| `UACC-HUM-03` | Automated Decision Review Sampling | Human Oversight | Working reference | T1 | EVD-13 | Review sampled AI-driven decisions, track agreement, and escalate systematic disagreements. | AI RMF MEASURE/MANAGE; SP 800-53 CA/AU; EU AI Act Art. 14; ISO/IEC 42001 operation/monitoring |
| `UACC-MON-01` | Model Performance Monitoring | Monitoring | Hardened v0.2 | T1 | Monitoring exports; alert logs | Monitor deployed performance against thresholds with alerting and investigation workflow. | AI RMF MEASURE/MANAGE; SP 800-53 SI/CA; EU AI Act Arts. 17/72; ISO/IEC 42001 monitoring |
| `UACC-MON-02` | Data and Model Drift Detection | Monitoring | Working reference | T1 | Drift configuration; drift logs; investigation records | Detect production input/output drift against baselines and investigate threshold breaches. | AI RMF MEASURE; SP 800-53 SI; EU AI Act Arts. 9/72; ISO/IEC 42001 operation/monitoring |
| `UACC-MON-03` | Post-Deployment Fairness Monitoring | Monitoring | Working reference | T1 | EVD-05; fairness trend reports | Monitor fairness degradation in production and trigger remediation or retraining when needed. | AI RMF MEASURE; SP 800-53 SI/CA; EU AI Act Arts. 9/72; ISO/IEC 42001 monitoring/responsible use |
| `UACC-MON-04` | Audit Logging for Decision Traceability | Monitoring | Hardened v0.2 | T1 | Audit log sample; retention/integrity records | Log decision metadata sufficient to reconstruct decisions and support audit. | AI RMF MEASURE/GOVERN; SP 800-53 AU; EU AI Act Arts. 12/19/26; ISO/IEC 42001 recording/reporting |
| `UACC-INC-01` | AI-Specific Incident Response Playbook | Incident Response | Working reference | T1 | EVD-14 | Maintain and test AI-specific incident scenarios, roles, escalation, and tabletop exercises. | AI RMF MANAGE; SP 800-53 IR; EU AI Act Art. 17; ISO/IEC 42001 incident communication/corrective action |
| `UACC-INC-02` | Serious Incident Reporting Workflow | Incident Response | Hardened v0.2 | T1 | EVD-15 | Classify, escalate, and report serious AI incidents to authorities within required timeframes. | AI RMF MANAGE; SP 800-53 IR; EU AI Act Art. 73; ISO/IEC 42001 incident communication |
| `UACC-INC-03` | Post-Incident Root Cause Analysis | Incident Response | Working reference | T1 | EVD-16 | Complete root cause analysis, corrective actions, risk-register updates, and lessons learned. | AI RMF MANAGE; SP 800-53 IR; EU AI Act Art. 17; ISO/IEC 42001 corrective action/improvement |
| `UACC-VEN-01` | Vendor AI Risk Assessment | Third-Party | Working reference | T1 | EVD-17 | Assess third-party AI components, vendor governance, data provenance, security, and conformity evidence. | AI RMF GOVERN; SP 800-53 SR; EU AI Act Arts. 25/47; ISO/IEC 42001 supplier responsibilities |
| `UACC-VEN-02` | Contractual AI Governance Requirements | Third-Party | Working reference | T1 | EVD-17; AI contract clause template | Include AI-specific documentation, change, incident, audit, data, and conformity clauses in contracts. | AI RMF GOVERN; SP 800-53 SR/SA; EU AI Act Arts. 25/16; ISO/IEC 42001 suppliers |
| `UACC-VEN-03` | Ongoing Vendor AI Performance Monitoring | Third-Party | Working reference | T1 | EVD-17; vendor monitoring reports | Monitor vendor AI performance, model updates, incidents, and governance posture during operation. | AI RMF MANAGE; SP 800-53 SR; EU AI Act Art. 26; ISO/IEC 42001 supplier monitoring |
| `UACC-RET-01` | AI System Retirement and Decommissioning | Retirement | Working reference | T1 | EVD-18 | Govern retirement, access revocation, secure disposal/archival, data deletion, and audit preservation. | AI RMF GOVERN; SP 800-53 SA/CM/MP/AU; EU AI Act Arts. 21/18; ISO/IEC 42001 operation/monitoring |

## Why v0.2 hardens 11 instead of all 35

The v0.2 public draft hardens 11 controls first to validate the assessor-grade pattern across governance, inventory, risk, data, model validation, monitoring, human oversight, and incident reporting. Publishing the full 35-control index keeps the intended scope visible while focusing detailed assessment language where the framework is most ready for review and pilot use.

Future releases are expected to harden additional controls and supporting artifacts after public feedback confirms the control template, crosswalk confidence labels, evidence expectations, and governance-as-code model are stable. Specific future-version scope may change based on review and implementation feedback.
