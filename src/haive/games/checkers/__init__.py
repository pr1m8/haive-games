"""Checkers game module.

A complete implementation of checkers (draughts) using AI-powered players
that can analyze board positions, plan moves, and execute strategic gameplay
using large language models for intelligent decision making.

Key Components:
    CheckersAgent: Main agent orchestrating LLM-powered checkers gameplay
    CheckersAgentConfig: Configuration for checkers game parameters and engines
    CheckersState: Game state management with board position and piece tracking
    CheckersMove: Structured move representation with validation
    CheckersPlayerDecision: Player decision model with move and reasoning
    CheckersAnalysis: Position analysis and strategic evaluation

Example:
    >>> from haive.games.checkers import CheckersAgent, CheckersAgentConfig
    >>> config = CheckersAgentConfig()
    >>> agent = CheckersAgent(config)
    >>> result = agent.run_game()
"""

from haive.games.checkers.agent import CheckersAgent
from haive.games.checkers.config import CheckersAgentConfig
from haive.games.checkers.models import (
    CheckersAnalysis,
    CheckersMove,
    CheckersPlayerDecision,
)
from haive.games.checkers.state import CheckersState

__all__ = [
    "CheckersAgent",
    "CheckersAgentConfig",
    "CheckersAnalysis",
    "CheckersMove",
    "CheckersPlayerDecision",
    "CheckersState",
]
