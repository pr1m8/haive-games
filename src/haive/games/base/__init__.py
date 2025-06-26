"""Base framework for game agents.

This package provides the foundational classes and utilities for building game agents,
including experimental features for game development.

Core Components:
    - GameAgent: Base class for implementing game-specific agents
    - GameConfig: Configuration class for game agents
    - GameState: Base state representation for games
    - GameStateManager: Interface for managing game state transitions
    - GameAgentFactory: Factory for creating game agents

Experimental Components:
    - GameTemplateGenerator: Template generator for creating new game implementations
      Warning: This component is experimental and its API may change.

Example:
    >>> from haive.agents.agent_games.framework.base import GameAgent, GameConfig
    >>> from haive.agents.agent_games.framework.base import GameTemplateGenerator  # Experimental
"""

from haive.games.base.agent import GameAgent, run_game
from haive.games.base.config import GameConfig
from haive.games.base.factory import GameAgentFactory
from haive.games.base.state import GameState
from haive.games.base.state_manager import GameStateManager
from haive.games.base.template_generator import GameTemplateGenerator

# from .utils import run_game
__all__ = [
    "GameAgent",
    "GameConfig",
    "GameState",
    "GameStateManager",
    "GameAgentFactory",
    "GameTemplateGenerator",  # Experimental
    #'run_game',
    "run_game",
]
