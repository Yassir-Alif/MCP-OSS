from typing import Dict, Any, List
from models import Capability

class PolicyEnforcer:
    """
    Enforces policies and capabilities.
    White-list based.
    """
    def __init__(self):
        # Hardcoded capabilities for reference implementation
        self.capabilities: Dict[str, Capability] = {
            "fs.list": Capability(name="fs.list", description="List files in directory", allowed_parameters=["path"]),
            "fs.read": Capability(name="fs.read", description="Read file content", allowed_parameters=["path"]),
        }

    def check_capability(self, capability_name: str, parameters: Dict[str, Any]) -> bool:
        if capability_name not in self.capabilities:
            return False
            
        cap = self.capabilities[capability_name]
        # Basic parameter check
        if cap.allowed_parameters:
            for param in parameters:
                if param not in cap.allowed_parameters:
                    return False
        return True
