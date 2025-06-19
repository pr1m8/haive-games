"""Checkers game implementation module.

This package provides a complete implementation of the Checkers game, including:
    - Game agent with LLM-powered players
    - State management with board representation
    - Position analysis and evaluation
    - Move validation and piece movement
    - Rich UI visualization
    - Jump detection and king promotion

The module supports standard checkers rules including mandatory jumps and
king promotions, with configurable options for board size and rule variations.

Example:
    >>> from haive.games.checkers import CheckersAgent, CheckersAgentConfig
    >>>
    >>> # Create and configure a Checkers agent
    >>> config = CheckersAgentConfig()
    >>> agent = CheckersAgent(config)
    >>>
    >>> # Run a game with visualization
    >>> agent.run_game(visualize=True)
"""

from haive.games.checkers.agent import CheckersAgent
from haive.games.checkers.config import CheckersAgentConfig
from haive.games.checkers.models import (
    CheckersAnalysis,
    CheckersMove,
    CheckersPlayerDecision,
)
from haive.games.checkers.state import CheckersState
from haive.games.checkers.state_manager import CheckersStateManager

__all__ = [
    "CheckersAgent",
    "CheckersAgentConfig",
    "CheckersAnalysis",
    "CheckersMove",
    "CheckersPlayerDecision",
    "CheckersState",
    "CheckersStateManager",
]
