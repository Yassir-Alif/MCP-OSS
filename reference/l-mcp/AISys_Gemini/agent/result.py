from pydantic import BaseModel
from typing import Any, Optional

class AgentResult(BaseModel):
    success: bool
    data: Optional[Any] = None
    error: Optional[str] = None
