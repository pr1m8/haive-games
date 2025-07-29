"""Connect4 game module.

A complete implementation of Connect Four using AI-powered players that can
analyze board positions, plan strategic moves, and play competitive games
using large language models for intelligent decision making.

Key Components:
    Connect4Agent: Main agent orchestrating LLM-powered Connect4 gameplay
    Connect4AgentConfig: Configuration for Connect4 game parameters and engines
    Connect4State: Game state management with board position tracking
    Connect4Move: Structured move representation with column selection
    Connect4PlayerDecision: Player decision model with move and reasoning
    Connect4Analysis: Position analysis and strategic evaluation

Example:
    >>> from haive.games.connect4 import Connect4Agent, Connect4AgentConfig
    >>> config = Connect4AgentConfig()
    >>> agent = Connect4Agent(config)
    >>> result = agent.run_game()
"""

from haive.games.connect4.agent import Connect4Agent
from haive.games.connect4.config import Connect4AgentConfig
from haive.games.connect4.models import (
    Connect4Analysis,
    Connect4Move,
    Connect4PlayerDecision,
)
from haive.games.connect4.state import Connect4State

__all__ = [
    "Connect4Agent",
    "Connect4AgentConfig",
    "Connect4Analysis",
    "Connect4Move",
    "Connect4PlayerDecision",
    "Connect4State",
]
