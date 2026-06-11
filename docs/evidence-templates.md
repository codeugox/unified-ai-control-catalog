---
description: Evidence traceability index and artifact expectations for assessing UACC v0.2 AI governance controls.
---

# UACC v0.2 Evidence Traceability Index

**Version:** 0.2 Public Draft  
**Status:** Public draft / working reference  

This document shows how the v0.2 core maps controls to practical evidence artifacts. It provides the traceability index and the v0.2 evidence-template changes that matter for implementation and review; it is not a complete fill-in-the-blank evidence workbook.

## Evidence-to-control index

| Template | Evidence artifact | Primary controls |
|---|---|---|
| EVD-01 | AI System Inventory Register | INV-01, INV-03, GOV-01 scope verification |
| EVD-02 | Risk Classification Decision Record | INV-02 |
| EVD-03 | AI Risk Assessment Report | RSK-01, RSK-03 |
| EVD-04 | Fundamental Rights Impact Assessment | RSK-02 |
| EVD-05 | Bias Evaluation Report | MDL-02, DAT-03, MON-03 |
| EVD-06 | Model Card | MDL-03 |
| EVD-07 | Model Validation Report | MDL-01 |
| EVD-08 | Adversarial Robustness Test Report | MDL-04, GEN-01 |
| EVD-09 | Data Lineage Record | DAT-01, GEN-05 |
| EVD-10 | Data Quality Report | DAT-02 |
| EVD-11 | Instructions for Use | TRN-01, RSK-03, TRN-03 |
| EVD-12 | Human Oversight Design Specification | HUM-01, HUM-02, HUM-03 |
| EVD-13 | Decision Review Sampling Report | HUM-03 |
| EVD-14 | AI Incident Response Playbook | INC-01 |
| EVD-15 | Serious Incident Notification Form | INC-02 |
| EVD-16 | Post-Incident Review Report | INC-03 |
| EVD-17 | Vendor AI Risk Assessment | VEN-01, VEN-02, VEN-03 |
| EVD-18 | AI System Retirement Checklist | RET-01 |

## Direct operational evidence

Some v0.2 core controls intentionally rely on direct operational evidence rather than a numbered `EVD-*` form:

| Control | Direct operational evidence |
|---|---|
| MON-01 | Monitoring dashboard exports, alert configuration, alert history, breach investigations, corrective-action records. |
| MON-04 | Audit log samples, log schema, retention policy, integrity verification, reconstruction test evidence. |

## Example evidence artifact contents

The examples below are illustrative, not full templates. They show the type of information an assessor, implementer, or reviewer should expect to see in representative evidence artifacts for the v0.2 core. They are selected examples, not exhaustive coverage of every `EVD-*` item.

### EVD-01 — AI System Inventory Register

Typical contents:

- System ID, system name, owner, business purpose, lifecycle status, and deployment environment.
- Risk tier, classification status, actor role, affected population, and applicable geography.
- Core metadata for model/system version, data inputs, vendor or third-party dependency where applicable, and human overseer where required.
- Discovery or reconciliation source, such as procurement, SaaS/application inventory, cloud service inventory, model registry, expense record, or owner attestation.
- Date discovered or reconciled, triage date, registration due date, disposition, and exception or extension reference where applicable.
- Last reviewed date, review cadence, and owner attestation or recertification status.

### EVD-02 — Risk Classification Decision Record

Typical contents:

- System ID and inventory reference.
- Classification screen results for prohibited practices, high-risk triggers, transparency obligations, and residual lower-risk classification.
- Applicable legal, regulatory, contractual, or organizational classification basis.
- Article 6(3) derogation rationale where claimed, including who decided the derogation applies and why the system does or does not materially influence a decision.
- Approval role, approver name or committee, decision date, and next revalidation trigger.

### EVD-03 — AI Risk Assessment Report

Typical contents:

- Intended use, reasonably foreseeable misuse, deployment context, and affected groups.
- Risk register entries covering safety, rights, privacy, discrimination, performance, security, operational, and downstream decision impacts.
- Severity, likelihood, inherent risk, mitigations, residual risk, and treatment decision.
- Open risk owners, remediation due dates, and deployment gate decision.
- Release or change-ticket reference, blocking criteria, and risk-acceptance approver where residual risk remains.
- Residual-risk communication items that should feed deployer instructions or operational playbooks.

### EVD-04 — Fundamental Rights Impact Assessment

Typical contents:

- System ID, deployment context, deployer or provider role, and affected population.
- Rights and interests assessed, such as non-discrimination, privacy/data protection, access to essential services, dignity, remedy, and due process where applicable.
- Impact analysis for protected classes, vulnerable populations, or other affected groups.
- Mitigations, human oversight measures, appeal or review paths, and unresolved residual impacts.
- Legal, compliance, DPO, or equivalent review or consultation, accountable approval role, approval date, and significant-change trigger.

### EVD-05 — Bias Evaluation Report

Typical contents:

- System ID, model version, dataset versions, evaluation date, and sector parameter pack ID.
- Protected or affected groups evaluated, sample sizes, subgroup floors, and confidence or insufficient-data caveats.
- Fairness metrics selected, selection rationale, thresholds, and results by group.
- Mitigations, retest results, conditional pass or exception decision, and remediation owner.
- Reproducibility metadata, including model hash, dataset hash, code version, seed, environment/container digest, and result hash or evidence-event ID.
- Independent approver, independence basis, conflict-of-interest check, approval date, and authority-to-block confirmation.

### EVD-09 — Data Lineage Record

Typical contents:

- Dataset name, version, owner, source system, collection method, and collection date range.
- Source provenance, third-party data source or license reference where applicable, and known limitations.
- Transformation chain, feature engineering steps, joins, filters, exclusions, and quality gates.
- Train/validation/test split definitions, labeling method, synthetic data flag where applicable, sensitive/PII handling, and usage restrictions.
- Dataset hash, storage location, access-control owner, and retention or deletion requirements.
- Linkage to model version, model card, risk assessment, and bias evaluation evidence.

### EVD-12 — Human Oversight Design Specification

Typical contents:

- Oversight objective, human overseer role, authority, required competence, and escalation path.
- Interface or workflow description showing how the overseer interprets outputs and contextual information.
- Override, non-use, interruption, escalation, and rationale-capture mechanisms.
- Pre-deployment and periodic test results for override/interruption functionality.
- Training, qualification, and access-control evidence for designated overseers.
- Capability-specific feasibility assessment for interruption, pause, stop, override, non-use, and escalation, including any documented technical infeasibility rationale.
- Compensating controls and residual-risk approval where interruption, pause, or stop is not feasible.
- Post-deployment oversight effectiveness evidence, such as sampled overrides, escalation outcomes, usability issues, latency constraints, or evidence that overseers had enough context and time to act.

### EVD-15 — Serious Incident Notification Form

Typical contents:

- System ID, owner, actor role, risk tier, and applicable authority, recipient, or contractual/regulatory notification channel.
- Incident description, detection time, classification rationale, severity, affected users/groups, and known or suspected harm.
- Timeline of containment, mitigation, escalation, and reporting decisions.
- Internal escalation timestamp, external notification deadline calculation, responsible person, approval, and transmission timestamp where applicable.
- Links to incident record, audit logs, root-cause analysis, corrective actions, and post-incident review evidence.

### MON-01 — Direct operational evidence for Model Performance Monitoring

Typical contents:

- Monitoring dashboard or export showing production metrics, data window, system/model version, and timestamp.
- Alert configuration, threshold values, alert recipients, and escalation routing.
- Reference baseline, monitored metric definitions, drift or performance calculation method, label availability assumptions, and threshold review owner.
- Alert history, breach tickets, investigation notes, corrective actions, and closure evidence.
- Segment-level monitoring where applicable, especially for Tier 1 systems and affected-group analysis.
- Evidence that monitoring coverage includes all in-scope production systems, with assessor sampling used to verify that claim.

### MON-04 — Direct operational evidence for Audit Logging and Decision Traceability

Typical contents:

- Log schema with required fields such as request ID, timestamp, model version, input reference or redacted/minimized input snapshot where permitted, output reference, confidence/score, override flag, and operator/overseer where applicable.
- Sample decision logs and reconstruction test showing that a sampled decision can be traced end to end.
- Retention policy and rationale, applicable legal/contractual/appeal windows, default minimum or approved exception, technical enforcement mechanism, storage location, access control, minimization/redaction rules, and tamper-evidence or integrity mechanism.
- Log extraction query, extraction timestamp, hash or integrity proof, and reviewer identity.
- Evidence that logs remain reconstructable for the retained period, or that approved exceptions preserve sufficient alternative evidence such as signed decision summaries, case records, or immutable references.
- Incident, appeal, or audit sample linkage where logs were used to investigate or reconstruct a decision.

## v0.2 targeted updates already applied

### EVD-01 — AI System Inventory Register

EVD-01 now distinguishes core mandatory metadata from conditional metadata so low-risk or internal systems are not forced to populate irrelevant high-risk/vendor fields. It also adds discovery/reconciliation evidence fields:

- discovery/reconciliation source;
- source system/export name;
- query/filter/detection rule;
- validated discovery date;
- initial triage date;
- registration due date;
- finding disposition;
- disposition rationale;
- exception/extension reference.

### EVD-05 — Bias Evaluation Report

EVD-05 now includes fields needed by the MDL-02 vertical slice:

- sector parameter pack ID;
- reproducibility metadata;
- model/dataset hashes;
- evaluation code version/Git SHA;
- random seeds where applicable;
- evaluation environment/container digest;
- result hash or evidence-event ID;
- independent approver and independence basis;
- conflict-of-interest check;
- conditional-pass expiration and exception-register linkage.

## Public draft note

This document is a summary index intended to support implementation planning and review. Future releases may publish standalone fill-in-the-blank evidence forms derived from this traceability model.
