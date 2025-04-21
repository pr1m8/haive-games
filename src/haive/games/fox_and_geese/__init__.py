"""Fox and Geese game module.

This module provides logic, configuration, state management, engine interfaces,
and an LLM-based agent for playing and analyzing Fox and Geese games.
"""

from .agent import FoxAndGeeseAgent
from .config import FoxAndGeeseConfig
from .models import FoxAndGeeseAnalysis, FoxAndGeeseMove, FoxAndGeesePosition
from .state import FoxAndGeeseState
from .state_manager import FoxAndGeeseStateManager

__all__ = [
    "FoxAndGeeseAgent",
    "FoxAndGeeseAnalysis",
    "FoxAndGeeseConfig",
    "FoxAndGeeseMove",
    "FoxAndGeesePosition",
    "FoxAndGeeseState",
    "FoxAndGeeseStateManager"
]
