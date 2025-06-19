"""Checkers game data models module.

This module provides data models for the checkers game, including:
    - Move representation with algebraic notation
    - Player decisions with reasoning and alternatives
    - Position analysis with strategic evaluations

These models enable structured data handling throughout the checkers game
implementation and provide strong typing for the LLM-based components.
"""

from typing import Literal

from pydantic import BaseModel, Field


class CheckersMove(BaseModel):
    """Represents a move in checkers.

    A structured representation of a checkers move with support for both
    regular moves and jumps (captures). Uses algebraic notation for
    position representation.

    Attributes:
        from_position (str): Starting position in algebraic notation (e.g., "a3")
        to_position (str): Ending position in algebraic notation (e.g., "b4")
        player (Literal["red", "black"]): The player making the move
        is_jump (bool): Whether this is a jump move (capturing an opponent's piece)
        captured_position (str | None): Position of the captured piece (if any)

    Examples:
        >>> # Regular move
        >>> move = CheckersMove(
        ...     from_position="a3",
        ...     to_position="b4",
        ...     player="red",
        ...     is_jump=False
        ... )
        >>> str(move)
        'a3-b4'

        >>> # Jump move
        >>> jump = CheckersMove(
        ...     from_position="c3",
        ...     to_position="e5",
        ...     player="black",
        ...     is_jump=True,
        ...     captured_position="d4"
        ... )
        >>> str(jump)
        'c3xe5'
    """

    from_position: str = Field(
        ..., description="Starting position in algebraic notation"
    )
    to_position: str = Field(..., description="Ending position in algebraic notation")
    player: Literal["red", "black"] = Field(..., description="Player making the move")
    is_jump: bool = Field(default=False, description="Whether this is a jump move")
    captured_position: str | None = Field(
        default=None, description="Position of captured piece if any"
    )

    def __str__(self) -> str:
        """String representation of the move in checkers notation.

        Returns:
            str: The move in checkers notation (e.g., "a3-b4" for regular moves,
                "a3xc5" for jumps)
        """
        if self.is_jump:
            return f"{self.from_position}x{self.to_position}"
        return f"{self.from_position}-{self.to_position}"


class CheckersPlayerDecision(BaseModel):
    """Player's decision for a move in checkers.

    A structured representation of a player's decision-making process,
    including the chosen move, reasoning, position evaluation, and
    alternative moves considered.

    This model is used as the structured output format for LLM-based
    player engines.

    Attributes:
        move (CheckersMove): The chosen move
        reasoning (str): Reasoning for the move choice
        evaluation (str): Position evaluation
        alternatives (list[str]): Alternative moves considered

    Examples:
        >>> # Create a player decision
        >>> decision = CheckersPlayerDecision(
        ...     move=CheckersMove(from_position="a3", to_position="b4", player="red"),
        ...     reasoning="Developing a piece toward the center",
        ...     evaluation="Slightly better position with center control",
        ...     alternatives=["c3-d4", "e3-f4"]
        ... )
    """

    move: CheckersMove = Field(..., description="The chosen move")
    reasoning: str = Field(..., description="Reasoning for the move choice")
    evaluation: str = Field(..., description="Position evaluation")
    alternatives: list[str] = Field(
        default_factory=list, description="Alternative moves considered"
    )


class CheckersAnalysis(BaseModel):
    """Analysis of a checkers position.

    A structured representation of a position analysis, including material
    advantage, center control, suggested moves, and an overall evaluation.

    This model is used as the structured output format for LLM-based
    analyzer engines.

    Attributes:
        material_advantage (str): Assessment of material advantage
        control_of_center (str): Assessment of center control
        suggested_moves (list[str]): List of suggested moves
        positional_evaluation (str): Overall position evaluation

    Examples:
        >>> # Create a position analysis
        >>> analysis = CheckersAnalysis(
        ...     material_advantage="Red has 12 pieces vs. Black's 10",
        ...     control_of_center="Red controls 3 of 4 center squares",
        ...     suggested_moves=["e3-f4", "c3-d4", "g3-h4"],
        ...     positional_evaluation="Red has a strong position with material advantage"
        ... )
    """

    material_advantage: str = Field(..., description="Assessment of material advantage")
    control_of_center: str = Field(..., description="Assessment of center control")
    suggested_moves: list[str] = Field(
        default_factory=list, description="List of suggested moves"
    )
    positional_evaluation: str = Field(..., description="Overall position evaluation")
