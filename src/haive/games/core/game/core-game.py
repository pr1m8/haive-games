"""
Game engine for the game framework.

This module defines the base Game class that serves as the central point
for game logic, integrating all framework components.
"""

from __future__ import annotations

import random
import uuid
from abc import ABC, abstractmethod
from enum import Enum, auto
from typing import (
    Any,
    Callable,
    Dict,
    Generic,
    List,
    Optional,
    Protocol,
    Set,
    Tuple,
    Type,
    TypeVar,
)

from game.core.board import Board
from game.core.container import GamePieceContainer
from game.core.move import Move, MoveResult, MoveStatus, MoveType
from game.core.piece import GamePiece
from game.core.player import Player, PlayerType
from game.core.position import Position
from game.core.space import Space
from pydantic import BaseModel, Field, computed_field, field_validator

# Type variables for generics
P = TypeVar("P", bound=Position)
T = TypeVar("T", bound=GamePiece)
S = TypeVar("S", bound=Space)
C = TypeVar("C", bound=GamePieceContainer)
M = TypeVar("M", bound=Move)
PL = TypeVar("PL", bound=Player)


class GameStatus(str, Enum):
    """Status of a game."""

    NOT_STARTED = "not_started"
    IN_PROGRESS = "in_progress"
    PAUSED = "paused"
    FINISHED = "finished"
    ABORTED = "aborted"


class GameResult(str, Enum):
    """Result of a finished game."""

    WIN = "win"  # Single player won
    DRAW = "draw"  # Draw/tie
    UNDETERMINED = "undetermined"  # Result not yet determined


class GameConfiguration(BaseModel):
    """Configuration options for a game."""

    name: str
    min_players: int = 1
    max_players: int = 2
    allow_ai_players: bool = True
    allow_network_players: bool = True
    enable_observers: bool = True
    options: Dict[str, Any] = Field(default_factory=dict)

    @field_validator("min_players", "max_players")
    @classmethod
    def validate_player_count(cls, v: int) -> int:
        """Ensure player counts are valid."""
        if v < 1:
            raise ValueError("Player count must be positive")
        return v

    def is_valid_player_count(self, count: int) -> bool:
        """Check if a player count is valid for this game."""
        return self.min_players <= count <= self.max_players


class Game(BaseModel, Generic[P, T, S, C, M, PL]):
    """
    Base class for all games.

    The Game class ties together all game components and implements the core game loop.
    It manages the game state, players, turns, and rules.
    """

    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    config: GameConfiguration
    players: List[PL] = Field(default_factory=list)
    board: Optional[Board[S, P, T]] = None
    containers: Dict[str, C] = Field(default_factory=dict)
    pieces: Dict[str, T] = Field(default_factory=dict)

    # Game state tracking
    status: GameStatus = GameStatus.NOT_STARTED
    current_player_index: int = 0
    turn_number: int = 0
    round_number: int = 0
    move_history: List[MoveResult[M]] = Field(default_factory=list)

    # Result tracking
    result: GameResult = GameResult.UNDETERMINED
    winners: List[str] = Field(default_factory=list)  # Player IDs
    scores: Dict[str, int] = Field(default_factory=dict)  # Player ID -> Score

    # Event callbacks
    callbacks: Dict[str, List[Callable]] = Field(default_factory=dict)

    # Game-specific properties
    properties: Dict[str, Any] = Field(default_factory=dict)

    class Config:
        arbitrary_types_allowed = True

    def initialize(self) -> None:
        """
        Initialize the game.

        This should be called after adding players and before starting the game.
        """
        # Validate player count
        if not self.config.is_valid_player_count(len(self.players)):
            raise ValueError(
                f"Invalid player count. This game requires {self.config.min_players}-{self.config.max_players} players."
            )

        # Initialize scores
        self.scores = {player.id: 0 for player in self.players}

        # Reset game state
        self.status = GameStatus.NOT_STARTED
        self.current_player_index = 0
        self.turn_number = 0
        self.round_number = 0
        self.move_history = []
        self.result = GameResult.UNDETERMINED
        self.winners = []

        # Call game-specific initialization
        self.setup_game()

        # Trigger initialization event
        self._trigger_event("on_initialize")

    @abstractmethod
    def setup_game(self) -> None:
        """
        Set up the game-specific components.

        This should be implemented by subclasses to create the board,
        pieces, and other game elements.
        """
        pass

    def start(self) -> None:
        """Start the game."""
        if self.status != GameStatus.NOT_STARTED:
            raise ValueError(f"Cannot start game with status {self.status}")

        # Set status to in progress
        self.status = GameStatus.IN_PROGRESS

        # Start the first turn
        self.start_turn()

        # Trigger start event
        self._trigger_event("on_start")

    def start_turn(self) -> None:
        """Start a new turn."""
        # Increment turn number
        self.turn_number += 1

        # Check if we've completed a round
        if self.current_player_index == 0:
            self.round_number += 1

        # Get current player
        current_player = self.get_current_player()

        # Trigger turn start event
        self._trigger_event("on_turn_start", player=current_player)

    def end_turn(self) -> None:
        """End the current turn and move to the next player."""
        # Get current player
        current_player = self.get_current_player()

        # Trigger turn end event
        self._trigger_event("on_turn_end", player=current_player)

        # Move to next player
        self.current_player_index = (self.current_player_index + 1) % len(self.players)

        # Start the next turn
        self.start_turn()

    def get_current_player(self) -> Optional[PL]:
        """Get the current player."""
        if not self.players:
            return None
        return self.players[self.current_player_index]

    def is_finished(self) -> bool:
        """Check if the game is finished."""
        return self.status == GameStatus.FINISHED

    def finish(self, result: GameResult, winners: List[str] = None) -> None:
        """
        Finish the game with a result.

        Args:
            result: Result of the game
            winners: List of winning player IDs
        """
        self.status = GameStatus.FINISHED
        self.result = result
        self.winners = winners or []

        # Trigger finish event
        self._trigger_event("on_finish", result=result, winners=self.winners)

    def abort(self) -> None:
        """Abort the game."""
        self.status = GameStatus.ABORTED

        # Trigger abort event
        self._trigger_event("on_abort")

    def pause(self) -> None:
        """Pause the game."""
        if self.status == GameStatus.IN_PROGRESS:
            self.status = GameStatus.PAUSED

            # Trigger pause event
            self._trigger_event("on_pause")

    def resume(self) -> None:
        """Resume a paused game."""
        if self.status == GameStatus.PAUSED:
            self.status = GameStatus.IN_PROGRESS

            # Trigger resume event
            self._trigger_event("on_resume")

    def add_player(self, player: PL) -> None:
        """
        Add a player to the game.

        Args:
            player: Player to add
        """
        # Check if game has already started
        if self.status != GameStatus.NOT_STARTED:
            raise ValueError("Cannot add player after game has started")

        # Check if player count would exceed max
        if len(self.players) >= self.config.max_players:
            raise ValueError(
                f"Cannot add more players. Maximum is {self.config.max_players}"
            )

        # Validate player type
        if player.type == PlayerType.AI and not self.config.allow_ai_players:
            raise ValueError("AI players are not allowed in this game")

        if player.type == PlayerType.NETWORK and not self.config.allow_network_players:
            raise ValueError("Network players are not allowed in this game")

        # Add player
        self.players.append(player)

        # Initialize score
        self.scores[player.id] = 0

        # Trigger player added event
        self._trigger_event("on_player_added", player=player)

    @abstractmethod
    def get_valid_moves(self, player_id: str) -> List[M]:
        """
        Get all valid moves for a player.

        Args:
            player_id: ID of the player

        Returns:
            List of valid moves
        """
        pass

    def process_move(self, move: M) -> MoveResult[M]:
        """
        Process a move from a player.

        Args:
            move: Move to process

        Returns:
            Result of the move
        """
        # Check if game is in progress
        if self.status != GameStatus.IN_PROGRESS:
            return MoveResult(
                move=move,
                status=MoveStatus.ILLEGAL,
                message=f"Game is not in progress (status: {self.status})",
            )

        # Check if it's the player's turn
        current_player = self.get_current_player()
        if not current_player or move.player_id != current_player.id:
            return MoveResult(
                move=move, status=MoveStatus.ILLEGAL, message="Not your turn"
            )

        # Validate and execute the move
        if not move.validate(self):
            return MoveResult(
                move=move, status=MoveStatus.INVALID, message="Invalid move"
            )

        # Execute the move
        result = move.execute(self)

        # Record the move
        self.move_history.append(result)

        # Trigger move event
        self._trigger_event("on_move", result=result)

        # Check for game end condition
        if self.check_end_condition():
            # Game has ended
            self.determine_winner()
        else:
            # Continue to next turn if move was successful
            if result.status == MoveStatus.SUCCESS:
                self.end_turn()

        return result

    @abstractmethod
    def check_end_condition(self) -> bool:
        """
        Check if the game has reached an end condition.

        Returns:
            True if the game should end, False otherwise
        """
        return False

    @abstractmethod
    def determine_winner(self) -> None:
        """
        Determine the winner(s) of the game.

        This should set the result and winners properties.
        """
        pass

    def get_state_for_player(self, player_id: str) -> Dict[str, Any]:
        """
        Get a representation of the game state for a specific player.

        This should include only information visible to that player.

        Args:
            player_id: ID of the player

        Returns:
            Dictionary with game state information
        """
        # Base implementation - subclasses should override for game-specific visibility
        return {
            "game_id": self.id,
            "name": self.name,
            "status": self.status,
            "turn_number": self.turn_number,
            "round_number": self.round_number,
            "current_player": (
                self.get_current_player().id if self.get_current_player() else None
            ),
            "players": [
                {"id": p.id, "name": p.name, "score": self.scores[p.id]}
                for p in self.players
            ],
            "is_your_turn": self.get_current_player()
            and self.get_current_player().id == player_id,
            "result": self.result if self.is_finished() else GameResult.UNDETERMINED,
            "winners": self.winners,
        }

    def get_piece(self, piece_id: str) -> Optional[T]:
        """
        Get a piece by ID.

        Args:
            piece_id: ID of the piece

        Returns:
            The piece, or None if not found
        """
        return self.pieces.get(piece_id)

    def get_container(self, container_id: str) -> Optional[C]:
        """
        Get a container by ID.

        Args:
            container_id: ID of the container

        Returns:
            The container, or None if not found
        """
        return self.containers.get(container_id)

    def create_position(self, position_data: Dict[str, Any]) -> Optional[P]:
        """
        Create a Position object from a dictionary representation.

        Args:
            position_data: Dictionary with position data

        Returns:
            Position object, or None if invalid
        """
        # Base implementation - subclasses should override for specific position types
        raise NotImplementedError

    def register_callback(self, event: str, callback: Callable) -> None:
        """
        Register a callback for a game event.

        Args:
            event: Event name
            callback: Callback function
        """
        if event not in self.callbacks:
            self.callbacks[event] = []
        self.callbacks[event].append(callback)

    def unregister_callback(self, event: str, callback: Callable) -> None:
        """
        Unregister a callback for a game event.

        Args:
            event: Event name
            callback: Callback function
        """
        if event in self.callbacks and callback in self.callbacks[event]:
            self.callbacks[event].remove(callback)

    def _trigger_event(self, event: str, **kwargs) -> None:
        """
        Trigger an event, calling all registered callbacks.

        Args:
            event: Event name
            **kwargs: Event data
        """
        if event in self.callbacks:
            for callback in self.callbacks[event]:
                try:
                    callback(self, **kwargs)
                except Exception as e:
                    print(f"Error in {event} callback: {e}")

    def set_property(self, key: str, value: Any) -> None:
        """
        Set a game property.

        Args:
            key: Property name
            value: Property value
        """
        self.properties[key] = value

    def get_property(self, key: str, default: Any = None) -> Any:
        """
        Get a game property.

        Args:
            key: Property name
            default: Default value if property doesn't exist

        Returns:
            Property value or default
        """
        return self.properties.get(key, default)


class TurnBasedGame(Game[P, T, S, C, M, PL]):
    """
    Base class for turn-based games.

    This adds additional turn management functionality.
    """

    turn_timeout: Optional[int] = None  # Timeout in seconds, None for no timeout
    turn_actions: Dict[str, int] = Field(
        default_factory=dict
    )  # Player ID -> Actions taken this turn
    max_actions_per_turn: int = 1
    turn_direction: int = 1  # 1 for clockwise, -1 for counterclockwise

    def end_turn(self) -> None:
        """End the current turn and move to the next player."""
        # Get current player
        current_player = self.get_current_player()

        # Trigger turn end event
        self._trigger_event("on_turn_end", player=current_player)

        # Reset turn actions for this player
        if current_player:
            self.turn_actions[current_player.id] = 0

        # Move to next player based on turn direction
        self.current_player_index = (
            self.current_player_index + self.turn_direction
        ) % len(self.players)

        # Start the next turn
        self.start_turn()

    def reverse_turn_order(self) -> None:
        """Reverse the turn order direction."""
        self.turn_direction *= -1

        # Trigger turn direction change event
        self._trigger_event("on_turn_direction_change", direction=self.turn_direction)

    def skip_turn(self) -> None:
        """Skip the current player's turn."""
        # Get current player
        current_player = self.get_current_player()

        # Trigger turn skip event
        self._trigger_event("on_turn_skip", player=current_player)

        # Move to next player
        self.end_turn()

    def record_action(self, player_id: str) -> None:
        """
        Record an action taken by a player this turn.

        Args:
            player_id: ID of the player
        """
        if player_id not in self.turn_actions:
            self.turn_actions[player_id] = 0

        self.turn_actions[player_id] += 1

    def can_take_action(self, player_id: str) -> bool:
        """
        Check if a player can take another action this turn.

        Args:
            player_id: ID of the player

        Returns:
            True if the player can take an action, False otherwise
        """
        if player_id not in self.turn_actions:
            return True

        return self.turn_actions[player_id] < self.max_actions_per_turn

    def process_move(self, move: M) -> MoveResult[M]:
        """
        Process a move from a player, tracking actions per turn.

        Args:
            move: Move to process

        Returns:
            Result of the move
        """
        # Check if game is in progress
        if self.status != GameStatus.IN_PROGRESS:
            return MoveResult(
                move=move,
                status=MoveStatus.ILLEGAL,
                message=f"Game is not in progress (status: {self.status})",
            )

        # Check if it's the player's turn
        current_player = self.get_current_player()
        if not current_player or move.player_id != current_player.id:
            return MoveResult(
                move=move, status=MoveStatus.ILLEGAL, message="Not your turn"
            )

        # Check if player can take another action
        if not self.can_take_action(move.player_id):
            return MoveResult(
                move=move,
                status=MoveStatus.ILLEGAL,
                message=f"Maximum actions per turn ({self.max_actions_per_turn}) reached",
            )

        # Execute the parent's move processing
        result = super().process_move(move)

        # If successful, record the action
        if result.status == MoveStatus.SUCCESS:
            self.record_action(move.player_id)

            # Check if player has reached max actions
            if (
                self.turn_actions.get(move.player_id, 0) >= self.max_actions_per_turn
                and move_type != MoveType.PASS
            ):  # Don't end turn after a pass move
                self.end_turn()

        return result


class RealTimeGame(Game[P, T, S, C, M, PL]):
    """
    Base class for real-time games.

    This adds functionality for games that don't use strict turns.
    """

    tick_rate: float = 60.0  # Ticks per second
    current_tick: int = 0
    action_cooldowns: Dict[str, Dict[str, int]] = Field(
        default_factory=dict
    )  # Player ID -> Action Type -> Ticks until available

    def update(self, delta_time: float) -> None:
        """
        Update the game state for a time step.

        Args:
            delta_time: Time in seconds since last update
        """
        # Increment current tick
        self.current_tick += 1

        # Update cooldowns
        for player_id, cooldowns in self.action_cooldowns.items():
            for action_type in list(cooldowns.keys()):
                cooldowns[action_type] -= 1
                if cooldowns[action_type] <= 0:
                    del cooldowns[action_type]

        # Update game state
        self.update_game_state(delta_time)

        # Trigger tick event
        self._trigger_event("on_tick", tick=self.current_tick, delta_time=delta_time)

    @abstractmethod
    def update_game_state(self, delta_time: float) -> None:
        """
        Update the game state for a time step.

        Args:
            delta_time: Time in seconds since last update
        """
        pass

    def set_cooldown(self, player_id: str, action_type: str, ticks: int) -> None:
        """
        Set a cooldown for an action.

        Args:
            player_id: ID of the player
            action_type: Type of action
            ticks: Number of ticks until the action is available again
        """
        if player_id not in self.action_cooldowns:
            self.action_cooldowns[player_id] = {}

        self.action_cooldowns[player_id][action_type] = ticks

    def is_action_on_cooldown(self, player_id: str, action_type: str) -> bool:
        """
        Check if an action is on cooldown.

        Args:
            player_id: ID of the player
            action_type: Type of action

        Returns:
            True if the action is on cooldown, False otherwise
        """
        return (
            player_id in self.action_cooldowns
            and action_type in self.action_cooldowns[player_id]
            and self.action_cooldowns[player_id][action_type] > 0
        )

    def process_move(self, move: M) -> MoveResult[M]:
        """
        Process a move from a player, checking cooldowns.

        Args:
            move: Move to process

        Returns:
            Result of the move
        """
        # Check if game is in progress
        if self.status != GameStatus.IN_PROGRESS:
            return MoveResult(
                move=move,
                status=MoveStatus.ILLEGAL,
                message=f"Game is not in progress (status: {self.status})",
            )

        # Check if action is on cooldown
        if self.is_action_on_cooldown(move.player_id, move.move_type):
            return MoveResult(
                move=move,
                status=MoveStatus.ILLEGAL,
                message=f"Action {move.move_type} is on cooldown",
            )

        # Execute the move
        result = super().process_move(move)

        # Set cooldown if move was successful
        if result.status == MoveStatus.SUCCESS:
            # Default cooldown of 1 tick, can be overridden in specific move types
            cooldown = move.get_property("cooldown", 1)
            if cooldown > 0:
                self.set_cooldown(move.player_id, move.move_type, cooldown)

        return result


class GameFactory:
    """Factory for creating game instances."""

    @staticmethod
    def create_game(game_type: Type[Game], config: GameConfiguration, **kwargs) -> Game:
        """
        Create a game instance.

        Args:
            game_type: Type of game to create
            config: Game configuration
            **kwargs: Additional arguments for the game constructor

        Returns:
            Game instance
        """
        return game_type(name=config.name, config=config, **kwargs)
