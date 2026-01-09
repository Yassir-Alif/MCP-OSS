from pydantic import BaseModel
from typing import List, Optional

class Capability(BaseModel):
    """
    Represents a static capability (whitelist-based).
    """
    name: str
    description: str
    allowed_parameters: Optional[List[str]] = None
    
class Permission(BaseModel):
    """
    Represents a permission binding.
    """
    capability_name: str
    constraints: dict = {}
