import logging
from typing import Optional, Dict, Any
from models import Intent, IntentState, Envelope
from .decision_engine import DecisionEngine
from agent.agent_facade import AgentFacade

# Basic logging setup
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger("SystemAudit")

class IntentLifecycleManager:
    """
    Manages the strict state transitions of an Intent.
    """
    def __init__(self, agent: AgentFacade):
        self.decision_engine = DecisionEngine()
        self.agent = agent

    def process_intent(self, intent: Intent, proposed_tool: str, parameters: Dict[str, Any]) -> Intent:
        # 1. CREATED -> DECISION_PENDING
        if intent.current_state != IntentState.CREATED:
             # Just invalid state handling
             logger.error(f"Intent {intent.id} in invalid state {intent.current_state} for processing.")
             return intent

        intent.transition_to(IntentState.DECISION_PENDING, "Submission to Core", "Core")
        logger.info(f"Intent {intent.id} moved to DECISION_PENDING")

        # 2. Decision
        approved, reason = self.decision_engine.evaluate_intent(intent, proposed_tool, parameters)
        
        if approved:
            intent.transition_to(IntentState.APPROVED, "Policy Check Passed", "DecisionEngine", {"reason": reason})
            logger.info(f"Intent {intent.id} APPROVED")
            
            # 3. APPROVED -> EXECUTION_PENDING (Envelope Gen)
            envelope = Envelope(
                intent_id=intent.id,
                capability_name=proposed_tool,
                parameters=parameters,
                integrity_hash="VALID"
            )
            intent.transition_to(IntentState.EXECUTION_PENDING, "Envelope Created", "Enforcement")
            logger.info(f"Intent {intent.id} EXECUTION_PENDING")

            # 4. Handover to Agent
            try:
                result = self.agent.execute_envelope(envelope)
                if result.success:
                     intent.transition_to(IntentState.EXECUTED, "Agent Execution Success", "Agent", {"result": result.data})
                     logger.info(f"Intent {intent.id} EXECUTED")
                else:
                     intent.transition_to(IntentState.FAILED, "Agent Execution Failed", "Agent", {"error": result.error})
                     logger.error(f"Intent {intent.id} FAILED: {result.error}")
            except Exception as e:
                intent.transition_to(IntentState.FAILED, "System Error during execution", "Core", {"exception": str(e)})
                logger.error(f"Intent {intent.id} FAILED (Exception): {e}")

        else:
            intent.transition_to(IntentState.DENIED, "Policy Check Failed", "DecisionEngine", {"reason": reason})
            logger.warning(f"Intent {intent.id} DENIED: {reason}")
            # Terminal state. No execution.
            
        return intent
