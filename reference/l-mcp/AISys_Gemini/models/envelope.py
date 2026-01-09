from pydantic import BaseModel, Field
from datetime import datetime
from typing import Any, Dict
import uuid

class Envelope(BaseModel):
    """
    Structured envelope for passing instructions from Core (Enforcement) to Agent (Execution).
    Enforces strict separation: Agent receives this, not the Intent.
    """
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    intent_id: str
    capability_name: str
    parameters: Dict[str, Any]
    timestamp: datetime = Field(default_factory=datetime.now)
    # Simulator signature/integrity check
    integrity_hash: str = ""
