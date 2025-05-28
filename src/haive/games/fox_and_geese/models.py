"""Models for the Fox and Geese game.

This module defines the models for the Fox and Geese game,
including the move and analysis models.
"""

from typing import List, Literal, Optional

from pydantic import BaseModel, ConfigDict, Field


class FoxAndGeesePosition(BaseModel):
    """Position on the Fox and Geese board.

    This class defines the structure of a position on the Fox and Geese board,
    which includes a row and column coordinate.
    """

    # Enable frozen for proper hashing in sets
    model_config = ConfigDict(frozen=True)

    row: int = Field(ge=0, lt=7, description="Row (0-6)")
    col: int = Field(ge=0, lt=7, description="Column (0-6)")

    def __str__(self) -> str:
        return f"({self.row}, {self.col})"

    def __eq__(self, other) -> bool:
        if not isinstance(other, FoxAndGeesePosition):
            return False
        return self.row == other.row and self.col == other.col

    def __hash__(self) -> int:
        return hash((self.row, self.col))


class FoxAndGeeseMove(BaseModel):
    """Represents a move in Fox and Geese.

    This class defines the structure of a move in Fox and Geese,
    which includes a starting position, an ending position,
    a piece type, and an optional captured position.
    """

    # Enable frozen for consistency
    model_config = ConfigDict(frozen=True)

    from_pos: FoxAndGeesePosition = Field(description="Starting position")
    to_pos: FoxAndGeesePosition = Field(description="Ending position")
    piece_type: Literal["fox", "goose"] = Field(description="Type of piece moved")
    capture: Optional[FoxAndGeesePosition] = Field(
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

    This class defines the structure of an analysis of a Fox and Geese position,
    which includes an advantage, an advantage level,
    key features, fox strategy, geese strategy,
    and critical squares.
    """

    model_config = ConfigDict(frozen=True)

    advantage: Literal["fox", "geese", "equal"] = Field(
        description="Which side has the advantage"
    )
    advantage_level: int = Field(ge=0, le=10, description="Level of advantage (0-10)")
    key_features: List[str] = Field(
        default_factory=list, description="Key strategic features of the position"
    )
    fox_strategy: str = Field(description="Recommended strategy for the fox")
    geese_strategy: str = Field(description="Recommended strategy for the geese")
    critical_squares: List[str] = Field(
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
