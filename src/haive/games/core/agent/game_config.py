from abc import ABC
from enum import Enum
from typing import Any, TypeVar

from haive.core.engine.agent.agent import AgentConfig
from pydantic import Field, computed_field, field_validator


class GamePlayerType(Enum):
    SinglePlayer = "single_player"
    MultiPlayer = "multi_player"
    Team = "team"


class PlayerType(str, Enum):
    pass


Player = TypeVar("Player")


class GameAgentConfig(AgentConfig, ABC):
    """Base class for game agent configurations."""

    players: list[Player] = Field(default_factory=list)
    state_schema: type[GameState] = Field(default_factory=GameState)

    @computed_field
    @property
    def num_players(self) -> int:
        """Get the number of players in the game."""
        return len(self.players)

    @field_validator("players")
    @classmethod
    def validate_players(cls, v) -> Any:
        """Validate the players in the game."""
        if len(v) == 0:
            raise ValueError("At least one player is required")
        return v
