#!/usr/bin/env python3
"""Validate UACC governance.yaml examples against the public v0.2 schema."""

from __future__ import annotations

import copy
import json
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schemas" / "governance_yaml_schema.json"
EXAMPLE_PATHS = [
    ROOT / "examples" / "governance.yaml",
    ROOT / "examples" / "governance_tier1_high_risk.yaml",
]


def load_schema() -> dict:
    schema = json.loads(SCHEMA_PATH.read_text())
    Draft202012Validator.check_schema(schema)
    return schema


def load_yaml(path: Path) -> dict:
    with path.open() as f:
        return yaml.safe_load(f)


def assert_valid(validator: Draft202012Validator, instance: dict, label: str) -> None:
    errors = sorted(validator.iter_errors(instance), key=lambda e: list(e.path))
    if errors:
        details = "\n".join(
            f"- {'/'.join(map(str, error.path)) or '<root>'}: {error.message}"
            for error in errors
        )
        raise AssertionError(f"{label} should be valid but failed:\n{details}")


def assert_invalid(validator: Draft202012Validator, instance: dict, label: str) -> None:
    if not list(validator.iter_errors(instance)):
        raise AssertionError(f"{label} should be invalid but passed")


def main() -> None:
    schema = load_schema()
    validator = Draft202012Validator(schema)

    examples = {path.name: load_yaml(path) for path in EXAMPLE_PATHS}
    for name, example in examples.items():
        assert_valid(validator, example, name)

    tier2 = examples["governance.yaml"]

    missing_overlays = copy.deepcopy(tier2)
    missing_overlays.pop("overlays", None)
    assert_invalid(validator, missing_overlays, "missing overlays negative case")

    genai_valid = copy.deepcopy(tier2)
    genai_valid["overlays"] = ["genai_llm"]
    genai_valid["genai"] = {
        "prompt_injection": {},
        "output_safety": {},
        "hallucination_monitoring": {},
        "audit_logging": {},
    }
    assert_valid(validator, genai_valid, "genai_llm positive case")

    genai_empty = copy.deepcopy(tier2)
    genai_empty["overlays"] = ["genai_llm"]
    genai_empty["genai"] = {}
    assert_invalid(validator, genai_empty, "genai_llm empty genai negative case")

    tier1_missing_required_blocks = copy.deepcopy(tier2)
    tier1_missing_required_blocks["system"]["risk_tier"] = 1
    assert_invalid(
        validator,
        tier1_missing_required_blocks,
        "Tier 1 missing required blocks negative case",
    )

    print("UACC governance.yaml validation passed")
    print("- schema is valid Draft 2020-12 JSON Schema")
    for path in EXAMPLE_PATHS:
        print(f"- {path.relative_to(ROOT)} validates")
    print("- negative cases fail as expected")


if __name__ == "__main__":
    main()
