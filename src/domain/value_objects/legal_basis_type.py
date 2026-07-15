"""Legal basis types under 152-FZ and common privacy law frameworks."""

from enum import StrEnum, auto


class LegalBasisType(StrEnum):
    CONSENT = auto()
    CONTRACT = auto()
    LEGAL_OBLIGATION = auto()
    VITAL_INTEREST = auto()
    PUBLIC_INTEREST = auto()
    LEGITIMATE_INTEREST = auto()
    STATUTORY = auto()  # Specific to 152-FZ Article 6
