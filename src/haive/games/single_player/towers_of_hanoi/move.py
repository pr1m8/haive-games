"""Tower of Hanoi move model"""

from typing import Any

from pydantic import BaseModel, Field, field_validator


class HanoiMoveModel(BaseModel):
    """Model for structured output of Tower of Hanoi moves."""

    from_peg: int = Field(..., description="Source peg number (1, 2, or 3)")
    to_peg: int = Field(..., description="Destination peg number (1, 2, or 3)")
    reasoning: str = Field(..., description="Explanation for this move")

    @field_validator("from_peg")
    @classmethod
    def validate_from_peg(cls, v: int) -> int:
        if v not in [1, 2, 3]:
            raise ValueError("Source peg must be 1, 2, or 3")
        return v

    @field_validator("to_peg")
    @classmethod
    def validate_to_peg(cls, v: int, info: Any) -> int:
        if v not in [1, 2, 3]:
            raise ValueError("Destination peg must be 1, 2, or 3")
        if "from_peg" in info.data and v == info.data["from_peg"]:
            raise ValueError("Source and destination pegs must be different")
        return v
