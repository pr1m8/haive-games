"""Reversi (Othello) game module.

This package provides components for simulating and interacting with Reversi,
including game agents, state logic, model schemas, engine prompts, and configuration.
"""

from haive.games.reversi.agent import ReversiAgent
from haive.games.reversi.config import ReversiConfig
from haive.games.reversi.engines import reversi_engines
from haive.games.reversi.models import ReversiAnalysis, ReversiMove
from haive.games.reversi.state import ReversiState
from haive.games.reversi.state_manager import ReversiStateManager

__all__ = [
    "ReversiAgent",
    "ReversiAnalysis",
    "ReversiConfig",
    "ReversiMove",
    "ReversiState",
    "ReversiStateManager",
    "reversi_engines",
]
