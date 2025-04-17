# src/haive/agents/agent_games/dominoes/config.py

from typing import Dict, Type
from pydantic import Field
from haive_games.framework.base.config import GameConfig
from haive_games.dominoes.state import DominoesState
from haive_core.engine.aug_llm import AugLLMConfig
from haive_games.dominoes.engines import aug_llm_configs


class DominoesAgentConfig(GameConfig):
    """Configuration for the dominoes agent."""
    
    state_schema: Type[DominoesState] = Field(default=DominoesState)
    
    engines: Dict[str, AugLLMConfig] = Field(
        default=aug_llm_configs, description="LLM engine configs for dominoes"
    )
    
    enable_analysis: bool = Field(
        default=True, description="Whether to enable in-game analysis"
    )
    
    visualize: bool = Field(
        default=True, description="Whether to visualize the game"
    )
    
    hand_size: int = Field(
        default=7, description="Tiles per player at start"
    )

    @classmethod
    def default_config(cls):
        return cls(
            state_schema=DominoesState,
            engines=aug_llm_configs,
            enable_analysis=True,
            visualize=True,
            hand_size=7,
        )
