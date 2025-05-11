"""State for the Fox and Geese game.

This module defines the state for the Fox and Geese game,
which includes the fox's position, the geese's positions,
the current player's turn, the game status, the move history,
the winner, and the number of geese remaining.
"""

from typing import Literal

from pydantic import Field

from haive.games.fox_and_geese.models import FoxAndGeeseMove, FoxAndGeesePosition
from haive.games.framework.base.state import GameState


class FoxAndGeeseState(GameState):
    """State for a Fox and Geese game.

    This class defines the structure of the Fox and Geese game state,
    which includes the fox's position, the geese's positions,
    the current player's turn, the game status, the move history,
    the winner, and the number of geese remaining.
    """

    fox_position: FoxAndGeesePosition = Field(..., description="Position of the fox")
    geese_positions: set[FoxAndGeesePosition] = Field(
        ..., description="Positions of geese"
    )
    turn: Literal["fox", "geese"] = Field(..., description="Current player's turn")
    game_status: Literal["ongoing", "fox_win", "geese_win"] = Field(
        default="ongoing", description="Status of the game"
    )
    move_history: list[FoxAndGeeseMove] = Field(
        default_factory=list, description="History of moves"
    )
    winner: str | None = Field(default=None, description="Winner of the game, if any")
    num_geese: int = Field(default=0, description="Number of geese remaining")

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
        )

    @property
    def board_string(self) -> str:
        """Get a string representation of the board."""
        # Create an empty 7x7 board
        board = [[" " for _ in range(7)] for _ in range(7)]

        # Place the fox
        board[self.fox_position.row][self.fox_position.col] = "F"

        # Place the geese
        for goose in self.geese_positions:
            board[goose.row][goose.col] = "G"

        # Convert to string
        result = "  0 1 2 3 4 5 6\n"
        for i, row in enumerate(board):
            result += f"{i} {' '.join(row)}\n"

        return result
