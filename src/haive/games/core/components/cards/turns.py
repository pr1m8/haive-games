# haive/games/core/components/cards/turns.py

from enum import Enum
from typing import Generic, List, Optional

from pydantic import BaseModel, Field

from haive.games.core.components.actions import ActionResult, TAction
from haive.games.core.components.models import TCard, TState


class TurnPhase(str, Enum):
    """Common phases in a card game turn."""

    DRAW = "draw"
    PLAY = "play"
    DISCARD = "discard"
    SPECIAL = "special"


class CardGameTurn(BaseModel, Generic[TCard, TAction, TState]):
    """Model representing a turn in a card game."""

    player_id: str
    turn_number: int
    phase: TurnPhase = TurnPhase.DRAW
    actions: List[TAction] = Field(default_factory=list)
    available_actions: List[str] = Field(default_factory=list)

    class Config:
        arbitrary_types_allowed = True

    def add_action(self, action: TAction) -> None:
        """Record an action taken during this turn."""
        self.actions.append(action)

    def is_complete(self, state: TState) -> bool:
        """Check if the turn is complete."""
        # Basic implementation - subclasses should override
        return False

    def get_next_phase(self) -> Optional[TurnPhase]:
        """Get the next phase of the turn."""
        phases = list(TurnPhase)
        try:
            current_idx = phases.index(self.phase)
            if current_idx < len(phases) - 1:
                return phases[current_idx + 1]
        except ValueError:
            pass
        return None


class TurnManager(BaseModel, Generic[TCard, TAction, TState]):
    """Manages turn progression in a card game."""

    current_turn: Optional[CardGameTurn[TCard, TAction, TState]] = None
    turn_number: int = 0
    player_order: List[str] = Field(default_factory=list)
    current_player_idx: int = 0
    turn_direction: int = 1  # 1 for clockwise, -1 for counterclockwise

    class Config:
        arbitrary_types_allowed = True

    def start_game(self, players: List[str]) -> None:
        """Initialize the turn manager with players."""
        self.player_order = players.copy()
        self.current_player_idx = 0
        self.turn_number = 0

    def start_turn(self, state: TState) -> TState:
        """Start a new turn."""
        player_id = self.get_current_player()
        self.turn_number += 1

        # Create new turn object
        self.current_turn = CardGameTurn[TCard, TAction, TState](
            player_id=player_id, turn_number=self.turn_number, phase=TurnPhase.DRAW
        )

        # Update state
        state.current_player_id = player_id
        state.current_turn = self.current_turn

        return state

    def end_turn(self, state: TState) -> TState:
        """End the current turn and advance to the next player."""
        # Advance to the next player
        self.current_player_idx = (self.current_player_idx + self.turn_direction) % len(
            self.player_order
        )

        return state

    def process_action(
        self, action: TAction, state: TState
    ) -> Tuple[ActionResult, TState]:
        """Process an action within the current turn."""
        # Validate the action is allowed
        if state.rules.validate_action(action, state):
            # Execute the action
            result = action.execute(state)

            if result.success:
                # Record the action in the current turn
                self.current_turn.add_action(action)

                # Apply rule effects
                state.rules.apply_all_effects(action, state)

                # Check if the turn is complete
                if self.current_turn.is_complete(state):
                    state = self.end_turn(state)

            return result, state

        return ActionResult(success=False, message="Action not allowed by rules"), state

    def get_current_player(self) -> str:
        """Get the current player's ID."""
        if not self.player_order:
            return ""
        return self.player_order[self.current_player_idx]

    def reverse_direction(self) -> None:
        """Reverse the turn order direction."""
        self.turn_direction *= -1
