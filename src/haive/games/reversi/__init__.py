"""Reversi (Othello) game module.

This package provides components for simulating and interacting with Reversi,
including game agents, state logic, model schemas, engine prompts, and configuration.
"""

from .agent import ReversiAgent
from .config import ReversiConfig
from .engines import reversi_engines
from .models import ReversiAnalysis, ReversiMove
from .state import ReversiState
from .state_manager import ReversiStateManager

__all__ = [
    "ReversiAgent",
    "ReversiAnalysis",
    "ReversiConfig",
    "ReversiMove",
    "ReversiState",
    "ReversiStateManager",
    "reversi_engines",
]
