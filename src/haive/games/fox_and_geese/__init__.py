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

from haive.games.fox_and_geese.agent import FoxAndGeeseAgent
from haive.games.fox_and_geese.config import FoxAndGeeseConfig
from haive.games.fox_and_geese.models import (
    FoxAndGeeseAnalysis,
    FoxAndGeeseMove,
    FoxAndGeesePosition,
)
from haive.games.fox_and_geese.rich_ui import FoxAndGeeseRichUI
from haive.games.fox_and_geese.state import FoxAndGeeseState
from haive.games.fox_and_geese.state_manager import FoxAndGeeseStateManager
from haive.games.fox_and_geese.ui import FoxAndGeeseUI

__all__ = [
    "FoxAndGeeseAgent",
    "FoxAndGeeseAnalysis",
    "FoxAndGeeseConfig",
    "FoxAndGeeseMove",
    "FoxAndGeesePosition",
    "FoxAndGeeseRichUI",
    "FoxAndGeeseState",
    "FoxAndGeeseStateManager",
    "FoxAndGeeseUI",
]
