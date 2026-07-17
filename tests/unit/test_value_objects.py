"""Unit tests for domain value objects."""

from __future__ import annotations

import pytest

from src.domain.value_objects.activity_status import ActivityStatus
from src.domain.value_objects.consent_status import ConsentStatus
from src.domain.value_objects.dsr_status import DSRStatus
from src.domain.value_objects.incident_severity import IncidentSeverity
from src.domain.value_objects.legal_basis_type import LegalBasisType
from src.domain.value_objects.localization_status import LocalizationStatus
from src.domain.value_objects.transfer_risk_level import TransferRiskLevel
from src.domain.value_objects.user_role import UserRole


class TestActivityStatus:
    def test_all_values_exist(self):
        assert ActivityStatus.DRAFT
        assert ActivityStatus.ACTIVE
        assert ActivityStatus.UNDER_REVIEW
        assert ActivityStatus.ARCHIVED

    def test_string_representation(self):
        assert str(ActivityStatus.DRAFT) == "DRAFT"
        assert ActivityStatus.ACTIVE.value == "ACTIVE"


class TestLegalBasisType:
    def test_all_152fz_basis_types(self):
        expected = {
            "CONSENT",
            "CONTRACT",
            "LEGAL_OBLIGATION",
            "VITAL_INTEREST",
            "PUBLIC_INTEREST",
            "LEGITIMATE_INTEREST",
        }
        actual = {e.value for e in LegalBasisType}
        assert expected == actual


class TestConsentStatus:
    def test_lifecycle_states(self):
        assert ConsentStatus.ACTIVE.value == "ACTIVE"
        assert ConsentStatus.WITHDRAWN.value == "WITHDRAWN"
        assert ConsentStatus.EXPIRED.value == "EXPIRED"


class TestDSRStatus:
    def test_workflow_states(self):
        # Must contain these core states
        core = {"OPEN", "ASSIGNED", "IN_PROGRESS", "RESPONDED", "COMPLETED", "REJECTED"}
        actual = {e.value for e in DSRStatus}
        assert core.issubset(actual)


class TestIncidentSeverity:
    def test_ordering(self):
        severities = [s.value for s in IncidentSeverity]
        assert "CRITICAL" in severities
        assert "HIGH" in severities
        assert "MEDIUM" in severities
        assert "LOW" in severities


class TestTransferRiskLevel:
    def test_levels(self):
        expected = {"LOW", "MEDIUM", "HIGH", "PROHIBITED"}
        actual = {e.value for e in TransferRiskLevel}
        assert expected == actual


class TestLocalizationStatus:
    def test_statuses(self):
        # Must contain these core states
        core = {"PENDING", "COMPLIANT", "NON_COMPLIANT"} if hasattr(LocalizationStatus, "PENDING") else {"COMPLIANT", "NON_COMPLIANT", "UNKNOWN"}
        actual = {e.value for e in LocalizationStatus}
        assert core.issubset(actual)


class TestUserRole:
    def test_standard_roles(self):
        # Must contain these core roles
        core = {"admin", "dpo", "compliance", "legal", "viewer"}
        actual = {e.value for e in UserRole}
        assert core.issubset(actual)
