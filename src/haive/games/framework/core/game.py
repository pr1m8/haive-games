# game_framework/core/game.py

from __future__ import annotations

import uuid
from enum import Enum
from typing import Any, Generic, TypeVar

from pydantic import BaseModel, Field, computed_field

from haive.games.framework.core.move import Move
from haive.games.framework.core.turn import Turn


class GameStatus(str, Enum):
    """Possible statuses of a game."""

    NOT_STARTED = "not_started"
    IN_PROGRESS = "in_progress"
    PAUSED = "paused"
    COMPLETED = "completed"


class Player(BaseModel):
    """A player in a game."""

    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    properties: dict[str, Any] = Field(default_factory=dict)


# Type variables for game state and moves
S = TypeVar("S", bound=BaseModel)
M = TypeVar("M", bound=Move)


class Game(BaseModel, Generic[S, M]):
    """Base class for all games.

    A Game represents a complete playable game with turns, moves, and
    state.
    """

    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    players: list[Player] = Field(default_factory=list)
    current_player_idx: int = 0
    status: GameStatus = GameStatus.NOT_STARTED
    state: S  # Game-specific state
    turns: list[Turn[M]] = Field(default_factory=list)
    winner_id: str | None = None

    class Config:
        arbitrary_types_allowed = True

    @computed_field
    @property
    def current_turn(self) -> Turn[M] | None:
        """Get the current turn, if any."""
        if not self.turns:
            return None
        return self.turns[-1]

    @computed_field
    @property
    def turn_number(self) -> int:
        """Get the current turn number."""
        return len(self.turns)

    def start_game(self) -> None:
        """Start the game."""
        if self.status == GameStatus.NOT_STARTED:
            self.status = GameStatus.IN_PROGRESS
            self.start_turn()

    def add_player(self, player: Player) -> None:
        """Add a player to the game.

        Args:
            player: The player to add
        """
        if self.status == GameStatus.NOT_STARTED:
            self.players.append(player)

    def get_current_player(self) -> Player | None:
        """Get the current player.

        Returns:
            The current player, or None if no players
        """
        if not self.players:
            return None
        return self.players[self.current_player_idx]

    def start_turn(self) -> Turn[M]:
        """Start a new turn for the current player.

        Returns:
            The new turn
        """
        current_player = self.get_current_player()
        if not current_player:
            raise ValueError("No players in game")

        turn = Turn[M](player_id=current_player.id, turn_number=len(self.turns) + 1)

        self.turns.append(turn)
        return turn

    def end_turn(self) -> None:
        """End the current turn and advance to the next player."""
        # Next player's turn
        self.current_player_idx = (self.current_player_idx + 1) % len(self.players)

        # Only automatically start a new turn if game is still in progress
        if self.status == GameStatus.IN_PROGRESS:
            self.start_turn()

    def make_move(self, move: M) -> bool:
        """Make a move in the game.

        Validates the move, applies it to the state, and updates the turn.

        Args:
            move: The move to make

        Returns:
            True if the move was valid and applied, False otherwise
        """
        # Ensure game is in progress
        if self.status != GameStatus.IN_PROGRESS:
            return False

        # Ensure move is from current player
        current_player = self.get_current_player()
        if not current_player or move.player_id != current_player.id:
            return False

        # Validate move
        if not move.is_valid(self.state):
            return False

        # Apply move to state
        self.state = move.apply(self.state)

        # Record move in current turn
        if self.current_turn:
            self.current_turn.add_move(move)

        # Check for game end
        if self.check_game_over():
            self.status = GameStatus.COMPLETED

        return True

    def check_game_over(self) -> bool:
        """Check if the game is over.

        Returns:
            True if the game is over, False otherwise
        """
        # Subclasses should implement game-specific end conditions
        return False
