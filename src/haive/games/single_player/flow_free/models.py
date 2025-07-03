"""Models for Flow Free gameplay and analysis.

This module defines the core data models for the Flow Free puzzle game,
including move representation and strategic analysis.
"""

from enum import Enum

from pydantic import BaseModel, Field, computed_field


class FlowColor(str, Enum):
    """Color options for Flow Free pipes."""

    RED = "red"
    GREEN = "green"
    BLUE = "blue"
    YELLOW = "yellow"
    ORANGE = "orange"
    PURPLE = "purple"
    CYAN = "cyan"
    PINK = "pink"
    BROWN = "brown"
    GRAY = "gray"


class PipeDirection(str, Enum):
    """Direction of a pipe segment."""

    UP = "up"
    DOWN = "down"
    LEFT = "left"
    RIGHT = "right"
    NONE = "none"  # For endpoints


class Position(BaseModel):
    """A position on the Flow Free board.

    Attributes:
        row: Row index (0-based).
        col: Column index (0-based).
    """

    row: int = Field(..., ge=0, description="Row index (0-based)")
    col: int = Field(..., ge=0, description="Column index (0-based)")

    def __str__(self) -> str:
        """String representation of the position."""
        return f"({self.row}, {self.col})"


class FlowFreeMove(BaseModel):
    """Represents a single move in Flow Free.

    Attributes:
        flow_id: Identifier for the flow being extended.
        position: Position to place the next pipe segment.
    """

    flow_id: str = Field(..., description="ID of the flow to extend")
    position: Position = Field(..., description="Position to place pipe segment")

    def __str__(self) -> str:
        """String representation of the move."""
        return f"Flow {self.flow_id} to {self.position}"


class FlowFreeAnalysis(BaseModel):
    """Strategic analysis of a Flow Free board position.

    Attributes:
        completed_flows: List of flow IDs that have been completed.
        incomplete_flows: List of flow IDs that need completion.
        critical_flows: Flows that are most constrained and should be prioritized.
        blocked_flows: Flows that might be blocked or have limited space.
        recommended_move: The suggested next move based on analysis.
        reasoning: Detailed explanation of the analysis.
    """

    completed_flows: list[str] = Field(
        default_factory=list, description="Flow IDs that have been completed"
    )
    incomplete_flows: list[str] = Field(
        default_factory=list, description="Flow IDs that need completion"
    )
    critical_flows: list[str] = Field(
        default_factory=list,
        description="Flows that are most constrained and should be prioritized",
    )
    blocked_flows: list[str] = Field(
        default_factory=list,
        description="Flows that might be blocked or have limited space",
    )
    recommended_move: FlowFreeMove | None = Field(
        default=None, description="Suggested next move based on analysis"
    )
    reasoning: str = Field(..., description="Detailed explanation of the analysis")
    hint: str | None = Field(
        default=None, description="Hint text that can be shown to the player"
    )

    @computed_field
    @property
    def completion_percentage(self) -> float:
        """Calculate the percentage of flows completed."""
        total_flows = len(self.completed_flows) + len(self.incomplete_flows)
        if total_flows == 0:
            return 0.0
        return len(self.completed_flows) / total_flows * 100.0
