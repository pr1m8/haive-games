from abc import ABC

from haive.core.engine.agent.config import AgentConfig

from haive.games.core.base.state import GameState


class GameAgentConfig(AgentConfig, ABC):
    """Base configuration for game agents."""

    state_schema: type[GameState] = Field(
        default_factory=GameState, description="State schema for the game"
    )
    game: type[Game] = Field(
        default_factory=Game, description="Game class for the game"
    )

    # players: List[Union]
