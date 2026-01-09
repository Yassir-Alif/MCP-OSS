import pytest
from models import Intent, IntentState
from core.intent_manager import IntentLifecycleManager
from agent.agent_facade import AgentFacade

class TestArchitecture:

    def test_state_machine_happy_path(self):
        """
        Verify the strict path:
        CREATED -> DECISION_PENDING -> APPROVED -> EXECUTION_PENDING -> EXECUTED
        """
        agent = AgentFacade()
        manager = IntentLifecycleManager(agent)
        
        intent = Intent(source="test", content="list files")
        # Assert initial state
        assert intent.current_state == IntentState.CREATED
        
        # Process
        final_intent = manager.process_intent(intent, "fs.list", {"path": "."})
        
        # Assert Final State
        assert final_intent.current_state == IntentState.EXECUTED
        
        # Verify History Order
        states = [step.to_state for step in final_intent.history]
        expected = [
            IntentState.DECISION_PENDING,
            IntentState.APPROVED,
            IntentState.EXECUTION_PENDING,
            IntentState.EXECUTED
        ]
        assert states == expected

    def test_denied_path(self):
        """
        Verify denial based on Policy.
        CREATED -> DECISION_PENDING -> DENIED
        """
        agent = AgentFacade()
        manager = IntentLifecycleManager(agent)
        
        intent = Intent(source="test", content="delete system")
        
        # Use Forbidden Tool
        final_intent = manager.process_intent(intent, "system.delete", {})
        
        assert final_intent.current_state == IntentState.DENIED
        
        states = [step.to_state for step in final_intent.history]
        assert IntentState.DECISION_PENDING in states
        assert IntentState.DENIED in states
        assert IntentState.EXECUTED not in states 

    def test_manual_state_jumping(self):
        """
        Simulate manual tampering. 
        Note: The Intent object technically allows it (it's a data object), 
        but the Manager tracks it via history.
        """
        intent = Intent(source="test", content="hack")
        intent.transition_to(IntentState.APPROVED, "Hack", "Hacker")
        
        # In a real enforcement system, we would cryptographically verifying transitions.
        # Here we verify that the Model records it correctly.
        assert intent.current_state == IntentState.APPROVED
        assert len(intent.history) == 1

    def test_agent_isolation(self):
        """
        Verify Agent cannot process an Intent, only Envelope.
        This is a type check / logic check.
        """
        agent = AgentFacade()
        intent = Intent(source="test", content="exploit")
        
        # Python is dynamic, but we expect strict typing/error if we pass wrong object
        # agent.execute_envelope expects Envelope. 
        # Passing Intent should fail (AttributeError or similar).
        with pytest.raises(Exception):
            agent.execute_envelope(intent)

if __name__ == "__main__":
    pytest.main()
