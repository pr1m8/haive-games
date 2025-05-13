from typing import Any

from pydantic import BaseModel, Field

from .models import Card, PlayerState


class BullshitGameState(BaseModel):
    """Represents the overall state of a Bullshit game."""

    players: list[PlayerState] = Field(default_factory=list)
    current_pile: list[Card] = Field(default_factory=list)
    current_claimed_value: str | None = None
    current_player_index: int = Field(default=0)
    game_status: str = Field(default="ongoing")
    winner: str | None = None
    last_played_cards: list[Card] = Field(default_factory=list)
    challenge_history: list[dict[str, Any]] = Field(default_factory=list)
