# UACC v0.2 Governance as Code

**Version:** 0.2 Public Draft  
**Status:** Public draft / working reference  

Governance-as-code expresses selected UACC requirements in version-controlled configuration and CI/CD or workflow gates. It is not a turnkey product and does not replace management-system processes, human approvals, or legal review.

## Public draft artifacts

- Schema: `../schemas/governance_yaml_schema.json`
- Tier 2 example: `../examples/governance.yaml`
- Tier 1 high-risk example: `../examples/governance_tier1_high_risk.yaml`
- Validation script: `../scripts/validate_governance_yaml.py`
- Canonical catalog: `uacc_v02_control_catalog.md`
- GenAI overlay reference: `uacc_v02_genai_overlay.md`

### Tier 2 example

```yaml title="examples/governance.yaml"
--8<-- "examples/governance.yaml"
```

### Tier 1 high-risk example

```yaml title="examples/governance_tier1_high_risk.yaml"
--8<-- "examples/governance_tier1_high_risk.yaml"
```

### Governance YAML schema

```json title="schemas/governance_yaml_schema.json"
--8<-- "schemas/governance_yaml_schema.json"
```

## Schema status

The public schema includes base predictive/decisioning blocks plus a GenAI overlay block. The sample governance files were validated locally against the public schema on 2026-06-06 using JSON Schema Draft 2020-12 validation. Run `python3 scripts/validate_governance_yaml.py` from the public repository root to repeat the validation.

JSON Schema validation checks structure, types, required fields, enumerations, patterns, and conditional requirements. JSON Schema `default` values are annotations; validation does not automatically materialize defaults or prove that governance teams prevent project teams from loosening controls. Organizations that use defaults operationally should apply them through a controlled configuration-generation or policy-enforcement process.

The schema is normative for governance-configuration syntax in this public draft. It does not make every referenced overlay control assessor-grade in v0.2 and does not replace the control catalog, evidence review, or approval workflow.

## Evidence event envelope

The `evidence_emission` block in `governance.yaml` identifies how evidence events are emitted, signed, and addressed. In v0.2, the schema requires the following envelope contract identifier and version when evidence emission is configured:

- `envelope_contract`: `uacc.evidence_event_envelope.v0_2`
- `envelope_version`: `0.2.0`

An evidence event envelope is the minimum metadata wrapper that makes a generated evidence record traceable to a system, control, source, signer, and time period. It is not a complete evidence payload and does not prove control operating effectiveness by itself.

Minimum envelope fields for the v0.2 contract are:

| Field | Purpose |
|---|---|
| `event_id` | Unique evidence event identifier. |
| `event_type` | Evidence event type, such as `assessment_result`, `approval`, `monitoring_export`, `log_reconstruction`, `exception_record`, or `incident_notification`. |
| `event_timestamp` | Timestamp when the event was generated or finalized. |
| `system_id` | AI system identifier that links to the inventory record. |
| `control_id` | UACC control or overlay control associated with the evidence. |
| `evidence_artifact_id` | Evidence template or artifact identifier where applicable, such as `EVD-05` or `MON-04`. |
| `source_system` | System, workflow, repository, dashboard, ticketing tool, or service that produced the event. |
| `assessment_period_start` / `assessment_period_end` | Time period covered by the event where applicable. |
| `subject_version` | Model, prompt, dataset, policy, workflow, schema, or configuration version covered by the evidence where applicable. |
| `result_status` | Outcome such as `passed`, `failed`, `conditional_pass`, `not_applicable`, or `informational`. |
| `artifact_uri` | URI, object path, ticket link, report link, or evidence-store reference for the underlying artifact. |
| `artifact_hash` | Hash or integrity reference for the artifact where available. |
| `signer_identity` | Identity that signs or attests to the event, aligned to the configured `signer_identity`. |
| `signature` | Signature, attestation reference, or `none` only where the configured signing method allows it. |

Organizations may add local fields, but should preserve these envelope fields or a documented equivalent mapping if they want automated evidence records to remain portable across UACC tooling. JSON Schema validation of `governance.yaml` confirms the emission configuration; it does not validate individual evidence event payloads in v0.2.

## GenAI ID synchronization

`uacc_v02_genai_overlay.md` is the public reference for GenAI overlay control IDs in v0.2:

| Schema sub-block | Canonical mapping | Notes |
|---|---|---|
| `prompt_injection` | `UACC-GEN-01` | Prompt injection defenses and tests. |
| `output_safety` | `UACC-GEN-02` | Output filtering, PII/secret redaction, policy override logging. |
| `hallucination_monitoring` | `UACC-GEN-03` | Grounding, citation, and review sampling. |
| `output_safety` leakage controls and audit/logging fields | Partial `UACC-GEN-04` support | Data leakage prevention is represented through PII/secret redaction and auditability in this public draft schema. Audit logging supports investigation but must itself be governed by minimization, redaction, retention, and access controls. |
| `rag_governance` | `UACC-GEN-05` | RAG source inventory requirement, corpus provenance, access control, and corpus change review. |
| `audit_logging` | `UACC-MON-04` | GenAI-specific audit fields. |
| `system_prompt_change_control` | Supporting schema capability | Not a `GEN-05` control. It supports `GEN-01`, `GEN-08`, release governance, and auditability. |

## Public draft scope note

The public draft schema does not create a dedicated `data_leakage_prevention` block. It documents `UACC-GEN-04` support through `output_safety` redaction controls and audit/logging fields. A later schema version may split data leakage prevention into a dedicated block if public feedback shows that implementers need separate configuration.

Overlay names are use-case labels plus conditional validation hooks. For v0.2, `genai_llm` has the most developed overlay schema. Other overlay values are retained for forward-compatible classification and may require additional organization-defined controls outside the schema until future releases add deeper schema profiles.
