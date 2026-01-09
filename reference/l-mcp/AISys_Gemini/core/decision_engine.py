from .policy_enforcer import PolicyEnforcer
from models import Intent
from typing import Tuple, Dict, Any

class DecisionEngine:
    """
    Makes the GO/NO-GO decision.
    """
    def __init__(self):
        self.enforcer = PolicyEnforcer()

    def evaluate_intent(self, intent: Intent, proposed_tool: str, parameters: Dict[str, Any]) -> Tuple[bool, str]:
        """
        Returns (Approved: bool, Reason: str)
        """
        # 1. Check if capability exists and params are valid
        if not self.enforcer.check_capability(proposed_tool, parameters):
            return False, f"Capability '{proposed_tool}' violation or invalid parameters."

        # 2. Context checks (Placeholder for more complex logic)
        # For this reference implementation, we approve if capability matches.
        
        return True, "Policy Check Passed"
