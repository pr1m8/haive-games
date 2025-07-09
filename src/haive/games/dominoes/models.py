"""Comprehensive data models for the Dominoes tile game.

This module defines the complete set of data structures for traditional Dominoes
gameplay, providing models for tile representation, game moves, strategic
analysis, and game state management. The implementation supports standard
double-six dominoes with traditional matching rules.

Dominoes is a classic tile-matching game involving:
- 28 tiles in a double-six set (0-0 through 6-6)
- Line-building with matching endpoints
- Strategic tile placement and blocking
- Point-based scoring systems

Key Models:
    DominoTile: Individual domino tile with two values
    DominoMove: Player's tile placement action
    DominoLinePosition: Position tracking on the domino line
    DominoAnalysis: Strategic evaluation for AI decision-making

Examples:
    Working with tiles::

        from haive.games.dominoes.models import DominoTile

        # Create standard tiles
        double_six = DominoTile(left=6, right=6)
        mixed_tile = DominoTile(left=3, right=5)

        # Check tile properties
        assert double_six.is_double() == True
        assert mixed_tile.sum() == 8
        print(double_six)  # "[6|6]"

    Making moves::

        from haive.games.dominoes.models import DominoMove

        move = DominoMove(
            tile=DominoTile(left=4, right=2),
            position="left",
            player="player1"
        )

    Strategic analysis::

        analysis = DominoAnalysis(
            available_moves=5,
            blocking_potential=3,
            point_value=12,
            strategy="Control high-value tiles"
        )

The models provide comprehensive tile management and strategic gameplay
support for AI-driven dominoes implementation.
"""

from typing import Literal

from pydantic import BaseModel, Field


class DominoTile(BaseModel):
    """A domino tile with two values."""

    left: int = Field(..., ge=0, le=6, description="Left value (0-6)")
    right: int = Field(..., ge=0, le=6, description="Right value (0-6)")

    def is_double(self) -> bool:
        """Check if this is a double (same value on both sides)."""
        return self.left == self.right

    def sum(self) -> int:
        """Get the sum of both values."""
        return self.left + self.right

    def reversed(self) -> "DominoTile":
        """Get a new tile with left and right values swapped."""
        return DominoTile(left=self.right, right=self.left)

    def __str__(self) -> str:
        """String representation of the tile."""
        return f"[{self.left}|{self.right}]"

    def __eq__(self, other) -> bool:
        """Check if two tiles are equal (ignoring order)."""
        if not isinstance(other, DominoTile):
            return False
        return (self.left == other.left and self.right == other.right) or (
            self.left == other.right and self.right == other.left
        )


class DominoMove(BaseModel):
    """A move in dominoes."""

    tile: DominoTile = Field(..., description="The tile to play")
    location: Literal["left", "right"] = Field(
        ..., description="Where to play the tile"
    )

    def __str__(self) -> str:
        """String representation of the move."""
        return f"Play {self.tile} on the {self.location} end"


class DominoesPlayerDecision(BaseModel):
    """A player's decision in dominoes."""

    move: DominoMove | None = Field(
        default=None, description="The move to make, if any"
    )
    pass_turn: bool = Field(default=False, description="Whether to pass the turn")
    reasoning: str = Field(..., description="Reasoning for the decision")

    def __str__(self) -> str:
        """String representation of the decision."""
        if self.pass_turn:
            return f"Pass the turn. Reasoning: {self.reasoning}"
        return f"Make move: {self.move}. Reasoning: {self.reasoning}"


class DominoesAnalysis(BaseModel):
    """Analysis of a dominoes position."""

    hand_strength: int = Field(
        ..., ge=1, le=10, description="Overall hand strength (1-10)"
    )
    pip_count_assessment: str = Field(..., description="Assessment of the pip count")
    open_ends: list[str] = Field(..., description="Analysis of open end values")
    missing_values: list[int] = Field(
        ..., description="Values not in the player's hand"
    )
    suggested_strategy: str = Field(..., description="Strategic recommendations")
    blocking_potential: str = Field(..., description="Potential for blocking opponent")
    reasoning: str = Field(..., description="Detailed reasoning for the analysis")
