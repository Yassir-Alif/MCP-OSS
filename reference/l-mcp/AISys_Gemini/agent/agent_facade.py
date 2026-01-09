from models import Envelope
from .result import AgentResult
from .executor import ToolExecutor
import logging

logger = logging.getLogger("Agent")

class AgentFacade:
    """
    The Execution Plane Entry Point.
    Accepts ONLY Envelopes. No Intents.
    """
    def __init__(self):
        self.executor = ToolExecutor()
        
    def execute_envelope(self, envelope: Envelope) -> AgentResult:
        logger.info(f"Agent received envelope {envelope.id} for {envelope.capability_name}")
        
        # 1. Integrity Check (Mock)
        if envelope.integrity_hash != "VALID":
            return AgentResult(success=False, error="Integrity Check Failed")

        # 2. Execution
        try:
            data = self.executor.execute(envelope.capability_name, envelope.parameters)
            return AgentResult(success=True, data=data)
        except Exception as e:
            return AgentResult(success=False, error=str(e))
