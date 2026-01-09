from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
import uuid
from .intent_state import IntentState

class IntentTransition(BaseModel):
    """
    Audit record for a single state transition.
    """
    from_state: Optional[IntentState]
    to_state: IntentState
    timestamp: datetime = Field(default_factory=datetime.now)
    trigger: str
    component: str
    metadata: dict = {}

class Intent(BaseModel):
    """
    Root entity representing a user/operator intent.
    Carries full state history.
    """
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    source: str
    content: str
    current_state: IntentState = IntentState.CREATED
    history: List[IntentTransition] = []
    
    def transition_to(self, new_state: IntentState, trigger: str, component: str, metadata: dict = {}) -> None:
        """
        Records a transition and updates current state.
        This does NOT contain the logic to validate if the transition is allowed (Core's job).
        """
        transition = IntentTransition(
            from_state=self.current_state,
            to_state=new_state,
            trigger=trigger,
            component=component,
            metadata=metadata
        )
        self.history.append(transition)
        self.current_state = new_state
