"""Localization rules — 152-FZ data localization requirements."""

from __future__ import annotations

from typing import Any

from src.infrastructure.rules import RuleFinding, RuleSet, RuleSeverity


class LocalizationRuleSet(RuleSet):
    def evaluate(self, context: dict[str, Any]) -> list[RuleFinding]:
        findings: list[RuleFinding] = []
        activity = context.get("activity")
        assessments = context.get("localization_assessments", [])

        if not activity:
            return findings

        # R-LOC-001: Activity with PD of Russian citizens must have localization assessment
        if activity.get("status") == "active" and not assessments:
            findings.append(
                RuleFinding(
                    rule_id="R-LOC-001",
                    severity=RuleSeverity.WARNING,
                    message="Active activity has no localization assessment",
                    details={"activity_id": activity.get("id")},
                )
            )

        # R-LOC-002: First-write-in-Russia must be true
        for assessment in assessments:
            if not assessment.get("first_write_in_russia"):
                findings.append(
                    RuleFinding(
                        rule_id="R-LOC-002",
                        severity=RuleSeverity.VIOLATION,
                        message="First write of personal data is NOT in Russia — 152-FZ violation",
                        details={"assessment_id": assessment.get("id")},
                    )
                )

        # R-LOC-003: Processor must support localization
        for assessment in assessments:
            if not assessment.get("processor_localization_supported"):
                findings.append(
                    RuleFinding(
                        rule_id="R-LOC-003",
                        severity=RuleSeverity.WARNING,
                        message="Processor does not confirm localization support",
                        details={"assessment_id": assessment.get("id")},
                    )
                )

        # R-LOC-004: Cross-border transfer with non-compliant localization
        if activity.get("cross_border_transfer") and activity.get(
            "localization_status"
        ) in ("unknown", "non_compliant"):
            findings.append(
                RuleFinding(
                    rule_id="R-LOC-004",
                    severity=RuleSeverity.CRITICAL,
                    message="Cross-border transfer enabled but localization status is non-compliant",
                    details={"activity_id": activity.get("id")},
                )
            )

        return findings
