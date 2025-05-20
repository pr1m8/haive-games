from abc import ABC, abstractmethod
from enum import Enum
from typing import List, Optional, Type, TypeVar

from haive.core.engine.agent.agent import AgentConfig
from pydantic import BaseModel, Field, computed_field, field_validator


class GamePlayerType(Enum):
    SinglePlayer = "single_player"
    MultiPlayer = "multi_player"
    Team = "team"   
class PlayerType()
    

Player = TypeVar("Player")
class GameAgentConfig(AgentConfig, ABC):
    """Base class for game agent configurations."""

    players: List[Player] = Field(default_factory=list)
    state_schema: Type[GameState] = Field(default_factory=GameState)
    
    
    @computed_field
    @property
    def num_players(self) -> int:
        """Get the number of players in the game."""
        return len(self.players)
    
    @field_validator("players")
    def validate_players(cls, v):
        """Validate the players in the game."""
        if len(v) == 0:
            raise ValueError("At least one player is required")
        return v
    
    