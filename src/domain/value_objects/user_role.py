"""Platform user roles with RBAC semantics."""

from enum import StrEnum, auto


class UserRole(StrEnum):
    ADMIN = auto()
    DPO = auto()           # Data Protection Officer
    COMPLIANCE = auto()
    LEGAL = auto()
    ANALYST = auto()
    VIEWER = auto()
