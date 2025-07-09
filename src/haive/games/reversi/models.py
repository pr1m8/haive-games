"""Comprehensive data models for Reversi (Othello) strategic board game.

This module defines the complete set of data structures for the classic Reversi
game, providing models for move validation, strategic analysis, and board
position evaluation. The implementation supports standard 8x8 Reversi with
traditional disc-flipping mechanics.

Reversi is a strategic board game involving:
- 8x8 board with alternating black and white disc placement
- Disc-flipping mechanics with line capture rules
- Strategic corner and edge control
- Endgame optimization for maximum disc count

Key Models:
    Position: Board coordinate representation (row, col)
    ReversiMove: Player's disc placement action
    ReversiAnalysis: Strategic evaluation for AI decision-making

Examples:
    Working with positions::

        from haive.games.reversi.models import Position

        # Corner positions (strategic)
        corner = Position(row=0, col=0)
        opposite_corner = Position(row=7, col=7)

        # Center positions (opening)
        center = Position(row=3, col=3)
        adjacent = Position(row=4, col=4)

    Making moves::

        from haive.games.reversi.models import ReversiMove

        # Black player opening move
        move = ReversiMove(row=3, col=2, player="B")

        # White player response
        counter_move = ReversiMove(row=2, col=2, player="W")

    Strategic analysis::

        from haive.games.reversi.models import ReversiAnalysis

        analysis = ReversiAnalysis(
            mobility=12,
            stability=8,
            corner_control=2,
            edge_control=5,
            evaluation_score=0.3,
            strategy="Focus on corner control and edge stability"
        )

The models provide comprehensive strategic analysis capabilities for
AI-driven Reversi gameplay with position evaluation and move optimization.
"""

from typing import Literal

from pydantic import BaseModel, Field


class Position(BaseModel):
    """A coordinate on the Reversi board.

    Attributes:
        row (int): Row index (0-7).
        col (int): Column index (0-7).
    """

    row: int = Field(..., ge=0, lt=8, description="Row index (0-7)")
    col: int = Field(..., ge=0, lt=8, description="Column index (0-7)")


class ReversiMove(BaseModel):
    """Represents a single Reversi move.

    Attributes:
        row (int): Row position of the move (0-7).
        col (int): Column position of the move (0-7).
        player (str): The player making the move ('B' or 'W').
    """

    row: int = Field(..., ge=0, lt=8, description="Row index (0-7)")
    col: int = Field(..., ge=0, lt=8, description="Column index (0-7)")
    player: Literal["B", "W"] = Field(
        ..., description="Player making the move (B=Black, W=White)"
    )

    def __str__(self) -> str:
        row_letter = chr(ord("A") + self.row)
        col_num = self.col + 1
        return f"{self.player} places at {row_letter}{col_num} ({self.row}, {self.col})"


class ReversiAnalysis(BaseModel):
    """Strategy and evaluation report for a Reversi position.

    Attributes:
        mobility (int): Number of legal moves available.
        frontier_discs (int): Count of discs adjacent to at least one empty space.
        corner_discs (int): Number of corners occupied by the player.
        stable_discs (int): Discs that cannot be flipped.
        positional_score (int): Positional heuristic score.
        position_evaluation (str): Assessment of advantage (e.g., 'winning', 'equal').
        recommended_moves (List[Position]): Preferred moves based on analysis.
        danger_zones (List[Position]): High-risk positions to avoid.
        strategy (str): Summary of strategic approach.
        reasoning (str): Detailed explanation of analysis.
    """

    mobility: int = Field(..., description="Number of legal moves available")
    frontier_discs: int = Field(
        ..., description="Number of discs adjacent to empty spaces"
    )
    corner_discs: int = Field(..., description="Number of corner positions captured")
    stable_discs: int = Field(..., description="Number of discs that cannot be flipped")
    positional_score: int = Field(
        ..., description="Score based on strategic position values"
    )
    position_evaluation: Literal["winning", "losing", "equal", "unclear"] = Field(
        ..., description="Overall position evaluation"
    )
    recommended_moves: list[Position] = Field(
        ..., description="List of recommended moves in order of preference"
    )
    danger_zones: list[Position] = Field(
        ..., description="Positions to avoid (may lead to opponent advantage)"
    )
    strategy: str = Field(..., description="Strategic assessment and recommendation")
    reasoning: str = Field(..., description="Detailed reasoning for the analysis")
