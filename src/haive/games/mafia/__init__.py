"""Mafia game implementation module.

This package provides a complete implementation of the Mafia party game, including:
    - Multi-player game agent with role-based gameplay
    - Day/Night phase management
    - Role-specific actions and abilities
    - Hidden information and voting mechanics
    - Game state tracking and validation
    - Specialized LLM configurations for different roles
    - Advanced analysis capabilities

The Mafia game is a social deduction game where players are assigned secret roles
and must work together or against each other to achieve their faction's goals.
The game alternates between day and night phases, with different actions available
to players based on their roles.

Example:
    >>> from haive.games.mafia import MafiaAgent, MafiaAgentConfig
    >>>
    >>> # Create and configure a Mafia game agent
    >>> config = MafiaAgentConfig.default_config(
    ...     player_count=7,
    ...     max_days=3
    ... )
    >>> agent = MafiaAgent(config)
    >>>
    >>> # Initialize the game with players
    >>> from haive.games.mafia.state_manager import MafiaStateManager
    >>> player_names = ["Player_1", "Player_2", "Player_3", "Player_4", "Player_5", "Player_6", "Narrator"]
    >>> initial_state = MafiaStateManager.initialize(player_names)
    >>>
    >>> # Run the game
    >>> for state in agent.app.stream(initial_state.model_dump()):
    ...     agent.visualize_state(state)
"""

from haive.games.mafia.agent import MafiaAgent
from haive.games.mafia.config import MafiaAgentConfig
from haive.games.mafia.engines import (
    aug_llm_configs,
    generate_detective_prompt,
    generate_doctor_prompt,
    generate_mafia_prompt,
    generate_narrator_prompt,
    generate_villager_prompt,
)
from haive.games.mafia.models import (
    ActionType,
    GamePhase,
    MafiaAction,
    PlayerRole,
    PlayerState,
)
from haive.games.mafia.state import MafiaGameState
from haive.games.mafia.state_manager import MafiaStateManager

# Temporarily disabled due to import issues
# from haive.games.mafia.aug_llms import (
#     get_mafia_analyzer,
#     suspicion_analyzer,
#     psychology_analyzer,
#     strategy_analyzer,
#     voting_analyzer,
# )

__all__ = [
    # Agent and configuration
    "MafiaAgent",
    "MafiaAgentConfig",
    # Core models
    "MafiaGameState",
    "PlayerState",
    "MafiaAction",
    "PlayerRole",
    "GamePhase",
    "ActionType",
    # State management
    "MafiaStateManager",
    # Engine prompts
    "generate_villager_prompt",
    "generate_mafia_prompt",
    "generate_detective_prompt",
    "generate_doctor_prompt",
    "generate_narrator_prompt",
    "aug_llm_configs",
    # Advanced analyzers (temporarily disabled)
    # "get_mafia_analyzer",
    # "suspicion_analyzer",
    # "psychology_analyzer",
    # "strategy_analyzer",
    # "voting_analyzer",
]
