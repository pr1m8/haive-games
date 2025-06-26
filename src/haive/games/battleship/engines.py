"""Battleship game engine configurations.

This module provides engine configurations for the Battleship game, including:
    - Player decision engines
    - Ship placement engines
    - Analysis engines
"""

from haive.core.engine.aug_llm import AugLLMConfig
from haive.core.models.llm.base import AzureLLMConfig

from haive.games.battleship.models import Analysis, MoveCommand, ShipPlacementWrapper
from haive.games.battleship.prompts import (
    generate_analysis_prompt,
    generate_move_prompt,
    generate_ship_placement_prompt,
)


def build_battleship_engines() -> dict[str, AugLLMConfig]:
    """Build engine configurations for the Battleship game.

    This function creates AugLLMConfig objects for:
        - Player 1 ship placement
        - Player 2 ship placement
        - Player 1 move selection
        - Player 2 move selection
        - Player 1 analysis
        - Player 2 analysis

    Returns:
        Dict[str, AugLLMConfig]: Dictionary of engine configurations
    """
    # Default LLM configuration
    default_llm_config = AzureLLMConfig(model="gpt-4o", parameters={"temperature": 0.7})

    engines = {
        "player1_ship_placement": AugLLMConfig(
            name="player1_ship_placement",
            llm_config=default_llm_config,
            prompt_template=generate_ship_placement_prompt("Player 1"),
            structured_output_model=ShipPlacementWrapper,
            description="Player 1 ship placement",
            structured_output_version="v1",
        ),
        "player2_ship_placement": AugLLMConfig(
            name="player2_ship_placement",
            llm_config=default_llm_config,
            prompt_template=generate_ship_placement_prompt("Player 2"),
            structured_output_model=ShipPlacementWrapper,
            description="Player 2 ship placement",
            structured_output_version="v1",
        ),
        "player1_move": AugLLMConfig(
            name="player1_move",
            llm_config=default_llm_config,
            prompt_template=generate_move_prompt("Player 1"),
            structured_output_model=MoveCommand,
            description="Player 1 move selection",
            structured_output_version="v1",
        ),
        "player2_move": AugLLMConfig(
            name="player2_move",
            llm_config=default_llm_config,
            prompt_template=generate_move_prompt("Player 2"),
            structured_output_model=MoveCommand,
            description="Player 2 move selection",
            structured_output_version="v1",
        ),
        "player1_analyzer": AugLLMConfig(
            name="player1_analyzer",
            llm_config=default_llm_config,
            prompt_template=generate_analysis_prompt("Player 1"),
            structured_output_model=Analysis,
            description="Player 1 analysis",
            structured_output_version="v1",
        ),
        "player2_analyzer": AugLLMConfig(
            name="player2_analyzer",
            llm_config=default_llm_config,
            prompt_template=generate_analysis_prompt("Player 2"),
            structured_output_model=Analysis,
            description="Player 2 analysis",
            structured_output_version="v1",
        ),
    }

    return engines
