---
description: Working UACC GenAI overlay for prompt injection, output safety, RAG governance, hallucination monitoring, leakage prevention, and agentic risk.
---

# UACC v0.2 GenAI Overlay

**Version:** 0.2 Public Draft  
**Status:** Public draft / working reference  
**Scope:** Working GenAI overlay controls; not part of the v0.2 core 11-control predictive/decisioning set  
**Audience:** GRC, security, privacy, AI engineering, application security, MLOps, and audit teams  
**License:** This document and control descriptions are CC BY 4.0; schema/scripts are MIT  
**Last updated:** 2026-06-06

> UACC is an open working reference catalog. It does not provide legal advice, certify compliance, replace conformity assessment, or create a regulatory safe harbor. Crosswalks identify areas of overlap and potential evidence reuse; they do not establish equivalence between frameworks.

The GenAI overlay adds controls for LLM assistants, RAG systems, and API-integrated GenAI systems. In v0.2, these controls are a working overlay rather than part of the v0.2 core 11-control predictive/decisioning set. They are intended to guide implementation and evidence collection for GenAI-specific risks while the base UACC controls continue to apply where relevant.

The v0.2 core is the stable v0.2 baseline for predictive or decisioning AI systems. The GenAI overlay is separate because LLM, RAG, and agentic systems introduce different risks, such as prompt injection, retrieved-context compromise, hallucination, leakage through generated output, and excessive tool agency.

Schema mappings in this document describe configuration support. Schema presence is not evidence of control operating effectiveness; implementers still need test results, approvals, monitoring records, review evidence, and residual-risk decisions appropriate to the system and risk tier.

## Canonical GenAI control IDs

This document is the public reference for GenAI overlay control IDs in v0.2.

| Control | Canonical title | Implementation focus | v0.2 schema / draft status |
|---|---|---|---|
| `UACC-GEN-01` | Prompt Injection Defense | Detect, test, and block or contain direct and indirect prompt-injection attempts from user inputs, retrieved content, tool outputs, or other untrusted context that could override protected instructions or manipulate tool calls. | Working draft; schema sub-block `prompt_injection` maps here. |
| `UACC-GEN-02` | Output Safety and Content Filtering | Apply output filtering, policy checks, unsafe-content handling, and override logging appropriate to the system's use case and risk tier. | Working draft; schema sub-block `output_safety` maps here. |
| `UACC-GEN-03` | Hallucination Detection and Grounding | Monitor grounding, citation quality, unsupported claims, and review sampling for LLM outputs where factuality or source attribution matters. | Working draft; schema sub-block `hallucination_monitoring` maps here. |
| `UACC-GEN-04` | Data Leakage Prevention | Prevent or detect leakage of secrets, personal data, sensitive source material, confidential prompts, or unauthorized retrieved context through model outputs, retrieval flows, or operational handling. | Working draft; partially schema-supported through `output_safety` redaction controls and auditability. Logging supports investigation but must itself be governed by minimization, redaction, retention, and access controls. |
| `UACC-GEN-05` | RAG Data Source Governance | Govern retrieval corpus inventory, source provenance, retrieval-time authorization, access control, source trust, corpus/chunking/index changes, and indirect prompt-injection considerations for RAG systems. | Working draft; schema sub-block `rag_governance` maps here. |
| `UACC-GEN-06` | AI-Generated Content Provenance and Labeling | Label or preserve provenance for AI-generated content where users, downstream systems, or policy require disclosure or traceability. | Working draft; not schema-enforced in v0.2. |
| `UACC-GEN-07` | Excessive Agency Prevention | Constrain autonomous tool/action scope, approval gates, permissions, rate limits, and blast radius for agentic or tool-using systems. | Working draft; not schema-enforced in v0.2. |
| `UACC-GEN-08` | GenAI-Specific Production Monitoring | Monitor GenAI behavior, guardrail events, refusals, unsafe outputs, grounding failures, suspected leakage events, tool-call anomalies, and user-reported issues in production. | Working draft; partially supported through GenAI schema sub-blocks and base monitoring controls. |
| `UACC-GEN-09` | User Interaction Transparency | Inform users when they are interacting with GenAI and disclose material limitations, use constraints, or review/escalation paths where appropriate. | Working draft; not schema-enforced in v0.2. |

## Governance-as-code mapping

When `genai_llm` is selected in `governance.yaml`, the public v0.2 schema requires a `genai` block. The required and conditional sub-blocks map to the GenAI overlay as follows:

| Schema sub-block | Primary mapping | Notes |
|---|---|---|
| `prompt_injection` | `UACC-GEN-01` | Prompt injection defenses and tests. |
| `output_safety` | `UACC-GEN-02`; partially supports `UACC-GEN-04` | Output filtering, PII/secret redaction, and policy override logging. |
| `hallucination_monitoring` | `UACC-GEN-03` | Grounding, citation, and review sampling. |
| `audit_logging` | `UACC-MON-04`; supports investigation for `UACC-GEN-04` and monitoring for `UACC-GEN-08` | GenAI-specific logging fields that support traceability, leakage investigation, and production monitoring. Logging is not itself a leakage-prevention control unless minimization, redaction, retention, and access controls are enforced. |
| `rag_governance` | `UACC-GEN-05` | Required only when RAG is in scope; covers source inventory requirement, corpus provenance, access control, indirect-injection detection, and corpus change review. |
| `system_prompt_change_control` | Supporting schema capability | Supports prompt/release governance, regression testing, and auditability. It is not a standalone `UACC-GEN-*` control in v0.2. |

## Priority overlay assessor checks

The following GenAI controls include preliminary assessor-facing checks in v0.2 because they are common review focus areas. They remain working overlay controls and are not part of the v0.2 core 11-control predictive/decisioning set.

### UACC-GEN-01 — Prompt Injection Defense

**Assessment focus:** Determine whether direct and indirect prompt-injection risks are identified, tested, mitigated, monitored, and routed for response.

**Minimum evidence examples:** Prompt-injection threat model or test plan; direct and indirect injection test cases; RAG/retrieved-context test cases where applicable; tool-output injection test cases where applicable; system/developer instruction protection evidence; blocked/allowed decision logs; remediation tickets; monitoring or incident-routing records for suspected prompt injection.

**Preliminary pass/fail criteria:**

- SATISFIED when the system has documented prompt-injection test coverage for user input and other untrusted context; applicable RAG/tool-output injection paths are tested; controls block, contain, or safely route successful injection attempts; failures have remediation owners and due dates; and suspected prompt-injection events can be monitored, logged, or escalated.
- OTHER THAN SATISFIED when prompt-injection risk is undocumented, testing covers only benign direct prompts, retrieved/tool context is untested where applicable, protected instructions can be overridden without detection or containment, failed tests lack remediation, or no monitoring/escalation path exists for suspected prompt injection.

### UACC-GEN-07 — Excessive Agency Prevention

**Assessment focus:** Determine whether agentic or tool-using systems are constrained so autonomous actions cannot exceed approved scope, permissions, or blast radius.

**Minimum evidence examples:** Tool/action inventory; permission matrix; least-privilege configuration; approval-gate rules for high-impact actions; rate/scope limits; rollback, pause, disablement, or kill-switch test evidence; action logs; blast-radius review; material tool/workflow change review.

**Preliminary pass/fail criteria:**

- SATISFIED when tools/actions are inventoried; permissions are least-privilege and tied to approved use cases; high-impact actions require human approval or equivalent control; scope/rate limits reduce blast radius; actions are logged; rollback, pause, disablement, or kill-switch paths are tested where applicable; and material tool/workflow changes trigger review.
- OTHER THAN SATISFIED when autonomous tools/actions are undocumented, over-permissioned, lack approval gates for high-impact actions, lack effective scope/rate limits, cannot be reconstructed from logs, lack tested disablement or rollback paths where feasible, or continue operating after material tool/workflow changes without review.

## Minimum evidence examples

The GenAI overlay is a working draft, but implementers should still preserve evidence that shows how GenAI-specific risks are managed. Examples include:

| Control area | Example evidence | Typical owner / reviewer |
|---|---|---|
| Prompt injection | Prompt-injection test results, red-team prompts, indirect-injection test cases for retrieved content, blocked/allowed decision logs, and remediation tickets. | Application security, AI engineering, security review. |
| Output safety and leakage | Output filter configuration, redaction test results, policy override logs, sensitive-output incidents, log minimization settings, and access-control review for prompt/output traces. | AI engineering, privacy, security operations. |
| Hallucination and grounding | Grounding/citation sampling results, unsupported-claim review records, evaluation set results, and user-reported factuality issues. | AI engineering, product owner, model risk or quality review. |
| RAG governance | RAG corpus inventory, source approval records, access-control review, corpus/chunking/index change log, retrieval authorization checks, and corpus poisoning or indirect-injection tests. | AI engineering, data owner, application security, privacy. |
| Excessive agency | Tool permission matrix, approval gates, rate limits, action logs, rollback/kill-switch tests, and blast-radius review. | AI engineering, application security, product owner. |
| Production monitoring | Guardrail event dashboards, unsafe-output tickets, refusal/override trends, leakage investigations, tool-call anomaly reports, and incident escalations. | Security operations, MLOps, AI governance. |
| User transparency | User disclosure copy, UI screenshots, terms or instructions, limitation notices, and escalation/review path evidence. | Product owner, legal/compliance, UX. |

## Relationship to base controls

Base UACC controls still apply where relevant, especially governance, inventory, risk assessment, monitoring, incident response, vendor management, and retention controls. The GenAI overlay adds implementation detail for LLM-specific risks. In some cases, a GenAI control supplements a base control; in others, it provides a GenAI-specific alternative where predictive-model evidence would not fit the system architecture.

Base controls may need GenAI-specific evidence extensions, especially for monitoring, incident response, vendor management, privacy/data retention, and audit logging. Implementers should document the local interpretation, risk tier, evidence source, and residual risk for each GenAI control they apply.
