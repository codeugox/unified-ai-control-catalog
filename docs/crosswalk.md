---
description: Confidence-labeled mappings from UACC v0.2 controls to NIST AI RMF, SP 800-53, EU AI Act, ISO/IEC 42001, and COSAIS.
---

# UACC v0.2 Crosswalk

**Version:** 0.2 Public Draft  
**Status:** Public draft / working reference

Crosswalks identify areas of overlap and potential evidence reuse. They do not establish legal equivalence, certification, or conformity.

## Confidence labels

| Label | Meaning |
|---|---|
| Direct | Narrow requirement match; UACC evidence directly supports the mapped requirement. |
| Partial | UACC evidence supports part of a broader obligation or outcome. |
| Analogical | Similar control concept, but the source framework was not written for this exact AI-specific requirement. |
| Informative | Useful context or alignment only; not a requirement mapping. |

## v0.2 core crosswalk summary

| UACC control | AI RMF | SP 800-53 | EU AI Act | ISO/IEC 42001 | COSAIS |
|---|---|---|---|---|---|
| UACC-GOV-01 | GOVERN 1.1/1.2 [Partial] | PM-1/PL-1 [Analogical] | Art. 17(1)(a) [Partial] | 5.2/A.2.2 [Partial] | [Informative] |
| UACC-INV-01 | GOVERN 1.6 [Direct], MAP 1.1 [Partial] | CM-8/PM-5 [Analogical] | Art. 49, 16, 26 [Partial] | A.4.2/A.4.5 [Partial] | [Informative] |
| UACC-INV-02 | MAP 1.1/1.5 [Partial] | RA-2 [Analogical] | Art. 5/6/Annex III [Direct for classification logic] | 6.1.2/A.5.2 [Partial] | [Informative] |
| UACC-RSK-01 | MAP 2.1/2.3/5.1 [Partial] | RA-3 [Partial] | Art. 9(2)(a)-(b) [Direct for risk identification/evaluation] | 6.1.2/8.2 [Partial] | [Informative] |
| UACC-RSK-02 | MAP 5.1/5.2 [Partial] | RA-8/PT-5 [Analogical] | Art. 27 [Direct where applicable] | 6.1.4/A.5.4/A.5.5 [Partial] | [Informative] |
| UACC-DAT-01 | MAP 2.3 [Partial] | SR-4/SA-4 [Analogical] | Art. 10(2) [Partial] | A.7.4 [Partial] | [Informative] |
| UACC-MDL-02 | MEASURE 2.11 [Direct] | RA-3/SI-4 [Analogical] | Art. 9/10/15/27 [Partial] | A.6.2.4/9.1 [Partial] | [Informative] |
| UACC-MON-01 | MEASURE 3.1/3.2/MANAGE 4.1 [Partial] | SI-4/CA-7 [Analogical] | Art. 17/72 [Partial] | 9.1/A.6.2.6 [Partial] | [Informative] |
| UACC-MON-04 | GOVERN 1.4/MEASURE 2.3 [Partial] | AU-2/AU-3/AU-9/AU-11/AU-12 [Partial] | Arts. 12/19/26(5) [Partial] | A.6.2.8 [Partial] | [Informative] |
| UACC-HUM-01 | GOVERN 3.2 [Partial] | AC-3/AC-6 [Analogical] | Arts. 14/26 [Partial] | A.9.3/A.6.2.6 [Partial] | [Informative] |
| UACC-INC-02 | MANAGE 4.1 [Partial] | IR-6/IR-8 [Partial] | Art. 73 [Direct where applicable] | A.8.4/A.8.3 [Partial] | [Informative] |

## GenAI overlay crosswalk status

GenAI overlay controls (`UACC-GEN-*`) are not yet included in the v0.2 crosswalk table. They remain working-draft overlay controls, and framework mappings for prompt injection, output safety, RAG governance, excessive agency, and related GenAI risks are planned for a later release.

## COSAIS note

COSAIS mappings remain Informative until public/final COSAIS materials provide stable identifiers. UACC should adopt COSAIS IDs as the authoritative SP 800-53 AI-tailoring reference when available.
