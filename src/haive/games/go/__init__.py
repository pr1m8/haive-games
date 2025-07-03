"""Go game implementation module.

This package provides a complete implementation of the Go game, including:
    - Game agent with LLM-powered players
    - State management with SGF support
    - Position analysis and territory evaluation
    - Move validation and scoring
    - Game visualization

Example:
    >>> from haive.games.go import GoAgent, GoAgentConfig
    >>>
    >>> # Create and configure a Go agent
    >>> config = GoAgentConfig(board_size=19, enable_analysis=True)
    >>> agent = GoAgent(config)
"""

from haive.games.go.agent import GoAgent
from haive.games.go.config import GoAgentConfig
from haive.games.go.models import (
    GoAnalysis,
    GoMoveModel,
    GoPlayerDecision,
)
from haive.games.go.state import GoGameState
from haive.games.go.state_manager import GoGameStateManager

__all__ = [
    "GoAgent",
    "GoAgentConfig",
    "GoAnalysis",
    "GoGameState",
    "GoGameStateManager",
    "GoMoveModel",
    "GoPlayerDecision",
]
