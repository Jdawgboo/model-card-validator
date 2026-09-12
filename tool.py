"""Validate accountable model-card metadata."""
from __future__ import annotations

from typing import Any

REQUIRED = ("model_name", "intended_use", "limitations", "evaluation", "contact")


def validate(card: dict[str, Any]) -> list[str]:
    """Return missing or empty accountability fields in stable order."""
    errors = [f"missing:{field}" for field in REQUIRED if not card.get(field)]
    evaluation = card.get("evaluation")
    if evaluation and not isinstance(evaluation, dict):
        errors.append("type:evaluation:object")
    return errors
