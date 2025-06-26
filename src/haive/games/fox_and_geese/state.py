"""State for the Fox and Geese game.

This module defines the state for the Fox and Geese game,
which includes the fox's position, the geese's positions,
the current player's turn, the game status, the move history,
the winner, and the number of geese remaining.
"""

from typing import Any, Dict, List, Literal, Optional, Set

from pydantic import ConfigDict, Field, field_serializer, field_validator

from haive.games.fox_and_geese.models import FoxAndGeeseMove, FoxAndGeesePosition
from haive.games.framework.base.state import GameState


class FoxAndGeeseState(GameState):
    """State for a Fox and Geese game.

    This class defines the structure of the Fox and Geese game state,
    which includes the fox's position, the geese's positions,
    the current player's turn, the game status, the move history,
    the winner, and the number of geese remaining.
    """

    model_config = ConfigDict(arbitrary_types_allowed=True, validate_assignment=True)
    players: List[str] = Field(["fox", "geese"], description="Players in the game")
    fox_position: FoxAndGeesePosition = Field(..., description="Position of the fox")
    geese_positions: Set[FoxAndGeesePosition] = Field(
        ..., description="Positions of geese"
    )
    turn: Literal["fox", "geese"] = Field(..., description="Current player's turn")
    game_status: Literal["ongoing", "fox_win", "geese_win"] = Field(
        default="ongoing", description="Status of the game"
    )
    move_history: List[FoxAndGeeseMove] = Field(
        default_factory=list, description="History of moves"
    )
    winner: Optional[str] = Field(
        default=None, description="Winner of the game, if any"
    )
    num_geese: int = Field(default=0, description="Number of geese remaining")
    fox_analysis: List[str] = Field(
        default_factory=list, description="List of fox position analyses"
    )
    geese_analysis: List[str] = Field(
        default_factory=list, description="List of geese position analyses"
    )

    @field_validator("geese_positions", mode="before")
    @classmethod
    def validate_geese_positions(cls, v: Any) -> Set[FoxAndGeesePosition]:
        """Validate and convert geese positions to a set."""
        if v is None:
            return set()

        if isinstance(v, set):
            # Already a set, but ensure all items are FoxAndGeesePosition
            return {
                (
                    FoxAndGeesePosition.model_validate(pos)
                    if isinstance(pos, dict)
                    else pos
                )
                for pos in v
            }

        if isinstance(v, list):
            # Convert from list of dicts to set of FoxAndGeesePosition objects
            return {
                (
                    FoxAndGeesePosition.model_validate(pos)
                    if isinstance(pos, dict)
                    else pos
                )
                for pos in v
            }

        # Handle single position
        if isinstance(v, dict):
            return {FoxAndGeesePosition.model_validate(v)}

        if isinstance(v, FoxAndGeesePosition):
            return {v}

        # Default to empty set if we can't parse
        return set()

    @field_validator("fox_position", mode="before")
    @classmethod
    def validate_fox_position(cls, v: Any) -> FoxAndGeesePosition:
        """Validate and convert fox position."""
        if v is None:
            # Default fox position at center
            return FoxAndGeesePosition(row=3, col=3)

        if isinstance(v, dict):
            return FoxAndGeesePosition.model_validate(v)

        if isinstance(v, FoxAndGeesePosition):
            return v

        # Default to center if we can't parse
        return FoxAndGeesePosition(row=3, col=3)

    @field_validator("move_history", mode="before")
    @classmethod
    def validate_move_history(cls, v: Any) -> List[FoxAndGeeseMove]:
        """Validate and convert move history."""
        if v is None:
            return []

        if isinstance(v, list):
            return [
                FoxAndGeeseMove.model_validate(move) if isinstance(move, dict) else move
                for move in v
            ]

        return []

    @field_serializer("geese_positions")
    def serialize_geese_positions(
        self, geese_positions: Set[FoxAndGeesePosition]
    ) -> List[Dict[str, Any]]:
        """Serialize geese positions as a list of dictionaries."""
        return [pos.model_dump() for pos in geese_positions]

    @field_serializer("fox_position")
    def serialize_fox_position(
        self, fox_position: FoxAndGeesePosition
    ) -> Dict[str, Any]:
        """Serialize fox position as a dictionary."""
        return fox_position.model_dump()

    @field_serializer("move_history")
    def serialize_move_history(
        self, move_history: List[FoxAndGeeseMove]
    ) -> List[Dict[str, Any]]:
        """Serialize move history as a list of dictionaries."""
        return [move.model_dump() for move in move_history]

    @classmethod
    def initialize(cls) -> "FoxAndGeeseState":
        """Initialize a new Fox and Geese game."""
        # Fox starts at the center
        fox_position = FoxAndGeesePosition(row=3, col=3)

        # Geese start at the top
        geese_positions = set()
        for col in range(7):
            if col % 2 == 0:  # Only on white squares
                geese_positions.add(FoxAndGeesePosition(row=0, col=col))
                geese_positions.add(FoxAndGeesePosition(row=1, col=col))

        return cls(
            fox_position=fox_position,
            geese_positions=geese_positions,
            turn="fox",  # Fox goes first
            game_status="ongoing",
            move_history=[],
            num_geese=len(geese_positions),
            fox_analysis=[],
            geese_analysis=[],
        )

    @property
    def board_string(self) -> str:
        """Get a string representation of the board."""
        # Create an empty 7x7 board
        board = [[" " for _ in range(7)] for _ in range(7)]

        # Place the fox
        if self.fox_position:
            board[self.fox_position.row][self.fox_position.col] = "F"

        # Place the geese
        for goose in self.geese_positions:
            board[goose.row][goose.col] = "G"

        # Convert to string
        result = "  0 1 2 3 4 5 6\n"
        for i, row in enumerate(board):
            result += f"{i} {' '.join(row)}\n"

        return result

    def model_dump(self, **kwargs) -> Dict[str, Any]:
        """Override model_dump to ensure proper serialization."""
        # Get the base dump
        data = super().model_dump(**kwargs)

        # Ensure geese_positions is properly serialized
        if "geese_positions" in data and isinstance(data["geese_positions"], set):
            data["geese_positions"] = [
                pos.model_dump() if hasattr(pos, "model_dump") else pos
                for pos in data["geese_positions"]
            ]

        # Ensure fox_position is properly serialized
        if "fox_position" in data and hasattr(data["fox_position"], "model_dump"):
            data["fox_position"] = data["fox_position"].model_dump()

        # Ensure move_history is properly serialized
        if "move_history" in data and isinstance(data["move_history"], list):
            data["move_history"] = [
                move.model_dump() if hasattr(move, "model_dump") else move
                for move in data["move_history"]
            ]

        return data

    @classmethod
    def model_validate(cls, obj: Any, **kwargs) -> "FoxAndGeeseState":
        """Override model_validate to handle various input formats."""
        if isinstance(obj, cls):
            return obj

        if isinstance(obj, dict):
            # Handle nested state structures (common in LangGraph)
            if "game_state" in obj and isinstance(obj["game_state"], dict):
                return cls.model_validate(obj["game_state"], **kwargs)

            # Validate the dict directly
            return super().model_validate(obj, **kwargs)

        # Fall back to default validation
        return super().model_validate(obj, **kwargs)

    def __str__(self) -> str:
        """String representation of the game state."""
        return f"FoxAndGeeseState(turn={self.turn}, status={self.game_status}, geese={self.num_geese})"

    def __repr__(self) -> str:
        """Detailed string representation of the game state."""
        return (
            f"FoxAndGeeseState(fox_pos={self.fox_position}, geese_count={self.num_geese}, "
            f"turn={self.turn}, status={self.game_status}, moves={len(self.move_history)})"
        )
