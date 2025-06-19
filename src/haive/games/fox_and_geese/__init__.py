"""Fox and Geese game module.

This module provides logic, configuration, state management, engine interfaces,
and an LLM-based agent for playing and analyzing Fox and Geese games.

Components:
    - FoxAndGeeseState: Data model for the game state
    - FoxAndGeeseAgent: Agent that manages the game flow
    - FoxAndGeeseUI: Basic UI for game visualization
    - FoxAndGeeseRichUI: Enhanced UI with improved styling and animations
    - FoxAndGeesePosition: Model for a position on the board
    - FoxAndGeeseMove: Model for a move in the game
"""

from .agent import FoxAndGeeseAgent
from .config import FoxAndGeeseConfig
from .models import FoxAndGeeseAnalysis, FoxAndGeeseMove, FoxAndGeesePosition
from .rich_ui import FoxAndGeeseRichUI
from .state import FoxAndGeeseState
from .state_manager import FoxAndGeeseStateManager
from .ui import FoxAndGeeseUI

__all__ = [
    "FoxAndGeeseAgent",
    "FoxAndGeeseAnalysis",
    "FoxAndGeeseConfig",
    "FoxAndGeeseMove",
    "FoxAndGeesePosition",
    "FoxAndGeeseState",
    "FoxAndGeeseStateManager",
    "FoxAndGeeseUI",
    "FoxAndGeeseRichUI",
]
