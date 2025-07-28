"""Comprehensive data models for the Fox and Geese asymmetric strategy game.

This module defines the complete set of data structures for the classic Fox and Geese
game, providing models for position tracking, move validation, strategic analysis,
and game state management. The implementation supports the traditional asymmetric
gameplay where one fox attempts to capture geese while geese try to trap the fox.

Fox and Geese is a classic asymmetric strategy game involving:
- One fox piece that can move and capture in any direction
- Multiple geese pieces that can only move forward and sideways
- 7x7 board with specific starting positions
- Victory conditions: fox captures enough geese OR geese trap the fox
- Strategic depth through positioning and tactical maneuvering

Key Models:
    FoxAndGeesePosition: Board coordinate representation with validation
    FoxAndGeeseMove: Complete move description with capture mechanics
    FoxAndGeeseAnalysis: Strategic evaluation for AI decision-making

Examples:
    Working with positions::

        from haive.games.fox_and_geese.models import FoxAndGeesePosition

        # Create board positions
        fox_start = FoxAndGeesePosition(row=0, col=3)  # Fox starting position
        geese_line = FoxAndGeesePosition(row=6, col=2)  # Geese back line

        # Positions are hashable for set operations
        positions = {fox_start, geese_line}
        print(fox_start)  # "(0, 3)"

    Making moves::

        from haive.games.fox_and_geese.models import FoxAndGeeseMove

        # Fox move with capture
        fox_capture = FoxAndGeeseMove(
            from_pos=FoxAndGeesePosition(row=2, col=2),
            to_pos=FoxAndGeesePosition(row=4, col=4),
            piece_type="fox",
            capture=FoxAndGeesePosition(row=3, col=3)
        )

        # Goose defensive move
        goose_move = FoxAndGeeseMove(
            from_pos=FoxAndGeesePosition(row=5, col=1),
            to_pos=FoxAndGeesePosition(row=4, col=1),
            piece_type="goose"
        )

    Strategic analysis::

        from haive.games.fox_and_geese.models import FoxAndGeeseAnalysis

        analysis = FoxAndGeeseAnalysis(
            advantage="fox",
            advantage_level=7,
            key_features=["fox has breakthrough", "geese scattered"],
            fox_strategy="Push through center, target isolated geese",
            geese_strategy="Regroup and form defensive line",
            critical_squares=["(3,3)", "(4,4)", "(5,5)"],
            explanation="Fox has tactical advantage with open center control"
        )

The models provide comprehensive support for asymmetric game analysis and
strategic AI development with proper validation and immutable data structures.
"""

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


class FoxAndGeesePosition(BaseModel):
    """Immutable position coordinate on the Fox and Geese board.

    Represents a specific square on the 7x7 Fox and Geese board using
    zero-indexed row and column coordinates. The position is immutable
    and hashable, making it suitable for use in sets and as dictionary keys.

    The board layout follows traditional Fox and Geese conventions:
    - Row 0: Top of the board (fox starting area)
    - Row 6: Bottom of the board (geese starting area)
    - Column 0-6: Left to right across the board

    Attributes:
        row: Row coordinate (0-6) from top to bottom of the board.
        col: Column coordinate (0-6) from left to right of the board.

    Examples:
        Creating positions::

            # Fox starting position (center top)
            fox_start = FoxAndGeesePosition(row=0, col=3)

            # Geese starting positions (bottom row)
            geese_positions = [
                FoxAndGeesePosition(row=6, col=i) for i in range(7)
            ]

            # Center board position
            center = FoxAndGeesePosition(row=3, col=3)

        Position validation::

            # Valid positions
            valid_pos = FoxAndGeesePosition(row=5, col=2)
            assert 0 <= valid_pos.row < 7
            assert 0 <= valid_pos.col < 7

            # Invalid positions raise validation errors
            try:
                invalid = FoxAndGeesePosition(row=7, col=3)  # Row too high
            except ValueError as e:
                print(f"Invalid position: {e}")

        Working with position sets::

            # Positions are hashable
            occupied_squares = {
                FoxAndGeesePosition(row=0, col=3),  # Fox
                FoxAndGeesePosition(row=6, col=0),  # Goose
                FoxAndGeesePosition(row=6, col=1),  # Goose
            }

            # Check if position is occupied
            test_pos = FoxAndGeesePosition(row=3, col=3)
            is_occupied = test_pos in occupied_squares

        Strategic context::

            # Corner positions (strategic for fox)
            corners = [
                FoxAndGeesePosition(row=0, col=0),
                FoxAndGeesePosition(row=0, col=6),
                FoxAndGeesePosition(row=6, col=0),
                FoxAndGeesePosition(row=6, col=6)
            ]

            # Center control positions
            center_squares = [
                FoxAndGeesePosition(row=3, col=3),
                FoxAndGeesePosition(row=3, col=4),
                FoxAndGeesePosition(row=4, col=3),
                FoxAndGeesePosition(row=4, col=4)
            ]

    Note:
        The position is frozen (immutable) to ensure data integrity and
        enable use as dictionary keys and in sets. String representation
        uses mathematical coordinate notation: "(row, col)".
    """

    # Enable frozen for proper hashing in sets
    model_config = ConfigDict(frozen=True)

    row: int = Field(ge=0, lt=7, description="Row (0-6)")
    col: int = Field(ge=0, lt=7, description="Column (0-6)")

    def __str__(self) -> str:
        """String representation of the position.

        Returns:
            str: Position in format "(row, col)".

        Examples:
            Position display::

                pos = FoxAndGeesePosition(row=3, col=4)
                print(pos)  # "(3, 4)"
        """
        return f"({self.row}, {self.col})"

    def __eq__(self, other) -> bool:
        """Check equality with another position.

        Args:
            other: Object to compare with.

        Returns:
            bool: True if positions have same row and column.
        """
        if not isinstance(other, FoxAndGeesePosition):
            return False
        return self.row == other.row and self.col == other.col

    def __hash__(self) -> int:
        """Generate hash for use in sets and dictionaries.

        Returns:
            int: Hash value based on row and column coordinates.
        """
        return hash((self.row, self.col))


class FoxAndGeeseMove(BaseModel):
    """Represents a move in Fox and Geese.

    This class defines the structure of a move in Fox and Geese, which
    includes a starting position, an ending position, a piece type, and
    an optional captured position.
    """

    # Enable frozen for consistency
    model_config = ConfigDict(frozen=True)

    from_pos: FoxAndGeesePosition = Field(description="Starting position")
    to_pos: FoxAndGeesePosition = Field(description="Ending position")
    piece_type: Literal["fox", "goose"] = Field(description="Type of piece moved")
    capture: FoxAndGeesePosition | None = Field(
        default=None, description="Position of captured goose, if any"
    )

    def __str__(self) -> str:
        if self.capture:
            return f"{self.piece_type.capitalize()} moves from {self.from_pos} to {self.to_pos}, capturing at {self.capture}"
        return f"{self.piece_type.capitalize()} moves from {self.from_pos} to {self.to_pos}"

    def __eq__(self, other) -> bool:
        if not isinstance(other, FoxAndGeeseMove):
            return False
        return (
            self.from_pos == other.from_pos
            and self.to_pos == other.to_pos
            and self.piece_type == other.piece_type
            and self.capture == other.capture
        )

    def __hash__(self) -> int:
        return hash((self.from_pos, self.to_pos, self.piece_type, self.capture))


class FoxAndGeeseAnalysis(BaseModel):
    """Analysis of a Fox and Geese position.

    This class defines the structure of an analysis of a Fox and Geese
    position, which includes an advantage, an advantage level, key
    features, fox strategy, geese strategy, and critical squares.
    """

    model_config = ConfigDict(frozen=True)

    advantage: Literal["fox", "geese", "equal"] = Field(
        description="Which side has the advantage"
    )
    advantage_level: int = Field(ge=0, le=10, description="Level of advantage (0-10)")
    key_features: list[str] = Field(
        default_factory=list, description="Key strategic features of the position"
    )
    fox_strategy: str = Field(description="Recommended strategy for the fox")
    geese_strategy: str = Field(description="Recommended strategy for the geese")
    critical_squares: list[str] = Field(
        default_factory=list,
        description="Critical squares or formations in the position",
    )
    explanation: str = Field(description="Detailed explanation of the analysis")

    def __eq__(self, other) -> bool:
        if not isinstance(other, FoxAndGeeseAnalysis):
            return False
        return (
            self.advantage == other.advantage
            and self.advantage_level == other.advantage_level
            and self.key_features == other.key_features
            and self.fox_strategy == other.fox_strategy
            and self.geese_strategy == other.geese_strategy
            and self.critical_squares == other.critical_squares
            and self.explanation == other.explanation
        )

    def __hash__(self) -> int:
        return hash(
            (
                self.advantage,
                self.advantage_level,
                tuple(self.key_features),
                self.fox_strategy,
                self.geese_strategy,
                tuple(self.critical_squares),
                self.explanation,
            )
        )
