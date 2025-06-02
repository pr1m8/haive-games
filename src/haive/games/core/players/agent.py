from abc import ABC

from haive.agents.simple.config import SimpleAgentConfig
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field

from haive.games.core.agent.game_config import GameConfig


class BasePlayerAgent(SimpleAgentConfig, ABC):
    """Base class for player agents."""

    # input_schema: GameState
    # output_schema: GameState
    # state_schema: GameState
    analysis_prompt: ChatPromptTemplate
    move_prompt: ChatPromptTemplate
    move_model: BaseModel

    def __init__(self, game_config: GameConfig, player_config: PlayerConfig):
        super().__init__(game_config, player_config)
