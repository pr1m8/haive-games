# game_framework/core/player.py

from __future__ import annotations

import random
import uuid
from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar

from pydantic import BaseModel, Field

# Type variable for moves
M = TypeVar("M", bound=BaseModel)
# Type variable for game state
S = TypeVar("S", bound=BaseModel)


class Player(BaseModel, ABC):
    """Base class for all player types in games.

    This is an abstract base class that defines the common interface for all player
    types (human, AI, etc.).

    """

    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    is_active: bool = True
    properties: dict[str, Any] = Field(default_factory=dict)

    class Config:
        arbitrary_types_allowed = True

    @abstractmethod
    def get_move(self, game_state: S, valid_moves: list[M]) -> M | None:
        """Get a move from this player.

        Args:
            game_state: Current game state
            valid_moves: List of valid moves

        Returns:
            The chosen move, or None if no move chosen

        """


class HumanPlayer(Player):
    """A human player that requires external input for moves.

    Human players don't automatically generate moves; they receive them through UI
    interactions.

    """

    def get_move(self, game_state: S, valid_moves: list[M]) -> M | None:
        """Get a move from this player.

        For human players, this should be called after receiving
        input from the user interface.

        Args:
            game_state: Current game state
            valid_moves: List of valid moves

        Returns:
            None (human players don't auto-generate moves)

        """
        # Human players don't auto-generate moves
        return None

    def select_move(self, move: M) -> M:
        """Select a move for this player.

        Args:
            move: The selected move

        Returns:
            The selected move

        """
        return move


class AIPlayer(Player, Generic[S, M]):
    """Base class for AI/computer-controlled players.

    AI players automatically generate moves based on the game state.

    """

    difficulty: str = "medium"  # easy, medium, hard

    @abstractmethod
    def get_move(self, game_state: S, valid_moves: list[M]) -> M | None:
        """Get a move from this AI player.

        Args:
            game_state: Current game state
            valid_moves: List of valid moves

        Returns:
            The chosen move, or None if no move chosen

        """


class RandomAIPlayer(AIPlayer[S, M]):
    """An AI player that selects random valid moves.

    This is the simplest form of AI player, useful for testing or for games where random
    play is appropriate.

    """

    def get_move(self, game_state: S, valid_moves: list[M]) -> M | None:
        """Get a random valid move.

        Args:
            game_state: Current game state
            valid_moves: List of valid moves

        Returns:
            A randomly selected valid move, or None if no valid moves

        """

        if not valid_moves:
            return None
        return random.choice(valid_moves)


class RuleBasedAIPlayer(AIPlayer[S, M]):
    """An AI player that follows predefined rules to select moves.

    Rule-based AIs use heuristics and decision trees to choose moves.

    """

    rules: list[dict[str, Any]] = Field(default_factory=list)

    def get_move(self, game_state: S, valid_moves: list[M]) -> M | None:
        """Get a move using predefined rules.

        Args:
            game_state: Current game state
            valid_moves: List of valid moves

        Returns:
            The chosen move, or None if no move chosen

        """
        # Subclasses should implement rule-based logic
        # Default implementation falls back to random

        if not valid_moves:
            return None
        return random.choice(valid_moves)

    def add_rule(self, condition: str, action: str, priority: int = 1) -> None:
        """Add a rule for the AI to follow.

        Args:
            condition: When to apply this rule
            action: What to do when the condition is met
            priority: Rule priority (higher numbers take precedence)

        """
        self.rules.append(
            {"condition": condition, "action": action, "priority": priority}
        )
