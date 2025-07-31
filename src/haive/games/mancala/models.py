"""Comprehensive data models for the Mancala (Kalah) board game.

This module defines the complete set of data structures for the traditional
Mancala game, providing models for move validation, strategic analysis, and
game state representation. The implementation follows standard Kalah rules
with 6 pits per player and seed redistribution mechanics.

Mancala is a classic strategy game involving:
- Two players with 6 pits each plus one store (mancala)
- Seed sowing mechanics with capture rules
- Strategic pit selection for optimal play
- Turn continuation and capture bonus rules

Key Models:
    MancalaMove: Represents a player's pit selection
    MancalaAnalysis: Strategic evaluation for AI decision-making

Examples:
    Making moves::

        from haive.games.mancala.models import MancalaMove

        # Select pit 2 for player 1
        move = MancalaMove(pit_index=2, player="player1")

        # Strategic center play
        center_move = MancalaMove(pit_index=3, player="player2")

    Strategic analysis::

        from haive.games.mancala.models import MancalaAnalysis

        analysis = MancalaAnalysis(
            captures_possible=[2, 4],
            free_turns_available=[1, 3],
            pit_values=[4, 3, 2, 5, 1, 6],
            strategy="Focus on pit 3 for free turn opportunity"
        )

The models support AI strategy development with comprehensive validation
and integration with the Mancala game engine.

"""

from typing import Literal

from pydantic import BaseModel, Field, ValidationInfo, field_validator


class MancalaMove(BaseModel):
    """Represents a move in Mancala.

    This class defines the structure of a move in Mancala, which includes the pit index
    to sow from and the player making the move.

    """

    pit_index: int = Field(
        ..., ge=0, lt=6, description="Index of the pit to sow from (0-5)"
    )
    player: Literal["player1", "player2"] = Field(
        ..., description="Player making the move"
    )

    @field_validator("pit_index")
    @classmethod
    def validate_pit_index(cls, v: int, info: ValidationInfo) -> int:
        """Validate that the pit index is valid for the player.

        Args:
            v: The pit index to validate.
            info: Validation info containing other field values.

        Returns:
            The validated pit index.

        Raises:
            ValueError: If pit index is out of valid range.

        """
        if "player" in info.data:
            # Adjust validation based on player
            if info.data["player"] == "player1" and not (0 <= v < 6):
                raise ValueError(f"Player 1 pit index must be 0-5, got {v}")
            if info.data["player"] == "player2" and not (0 <= v < 6):
                raise ValueError(f"Player 2 pit index must be 0-5, got {v}")
        return v

    def __str__(self) -> str:
        """Return string representation of the move."""
        return f"{self.player} sows from pit {self.pit_index}"


class MancalaAnalysis(BaseModel):
    """Analysis of a Mancala position.

    This class defines the structure of an analysis for a Mancala position, which
    includes the overall position evaluation, advantage level, stone distribution, pit
    recommendations, strategic focus, key tactics, and reasoning.

    """

    position_evaluation: Literal["winning", "losing", "equal", "unclear"] = Field(
        ..., description="Overall position evaluation"
    )
    advantage_level: int = Field(
        ..., ge=0, le=10, description="Level of advantage (0-10, where 10 is winning)"
    )
    stone_distribution: str = Field(..., description="Analysis of stone distribution")
    pit_recommendations: list[int] = Field(
        ..., description="Recommended pits to play from"
    )
    strategy_focus: Literal["offensive", "defensive", "balanced"] = Field(
        ..., description="Current strategic focus"
    )
    key_tactics: list[str] = Field(..., description="Key tactical considerations")
    reasoning: str = Field(..., description="Detailed reasoning for the analysis")
