"""Mancala game module.

This package provides logic, configuration, state management, engine interfaces,
and an LLM-based agent for playing and analyzing Mancala games.
"""

from .agent import MancalaAgent
from .config import MancalaConfig
from .engines import mancala_engines
from .models import MancalaAnalysis, MancalaMove
from .state import MancalaState
from .state_manager import MancalaStateManager

__all__ = [
    "MancalaAgent",
    "MancalaAnalysis",
    "MancalaConfig",
    "MancalaMove",
    "MancalaState",
    "MancalaStateManager",
    "mancala_engines",
]
