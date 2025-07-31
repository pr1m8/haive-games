# game_framework/core/turn.py

from __future__ import annotations

from enum import Enum
from typing import Any, Generic, TypeVar

from pydantic import BaseModel, Field

# Type variable for move types
M = TypeVar("M", bound=BaseModel)


class TurnPhase(str, Enum):
    """Common phases within a turn."""

    SETUP = "setup"
    MAIN = "main"
    CLEANUP = "cleanup"


class Turn(BaseModel, Generic[M]):
    """Represents a player's turn in a game.

    A turn tracks who is active, what phase the turn is in, and what moves have been
    made.

    """

    player_id: str
    turn_number: int
    phase: TurnPhase = TurnPhase.MAIN
    moves: list[M] = Field(default_factory=list)
    properties: dict[str, Any] = Field(default_factory=dict)

    def add_move(self, move: M) -> None:
        """Record a move made during this turn.

        Args:
            move: The move that was made

        """
        self.moves.append(move)

    def get_move_count(self) -> int:
        """Get the number of moves made this turn."""
        return len(self.moves)

    def set_phase(self, phase: TurnPhase) -> None:
        """Set the current phase of the turn.

        Args:
            phase: The phase to set

        """
        self.phase = phase

    def next_phase(self) -> TurnPhase:
        """Advance to the next phase.

        Returns:
            The new phase

        """
        phases = list(TurnPhase)
        current_index = phases.index(self.phase)
        next_index = (current_index + 1) % len(phases)
        self.phase = phases[next_index]
        return self.phase
