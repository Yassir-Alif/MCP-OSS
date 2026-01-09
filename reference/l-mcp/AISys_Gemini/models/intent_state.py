from enum import Enum

class IntentState(str, Enum):
    """
    Normative Intent State Machine States.
    Strictly defined in MCP-OSS_Architektur-Modell_v1.0.txt.
    """
    CREATED = "CREATED"
    DECISION_PENDING = "DECISION_PENDING"
    APPROVED = "APPROVED"
    DENIED = "DENIED"
    EXECUTION_PENDING = "EXECUTION_PENDING"
    EXECUTED = "EXECUTED"
    FAILED = "FAILED"
