"""Clue game module.

This module provides a Clue (Cluedo) game implementation for the Haive platform.
Players must deduce who committed a murder, with what weapon, and in which room.

The module includes:
    - Game state management and logic
    - Rich terminal UI visualization
    - AI-powered players and analysis
    - Game agent infrastructure

Example:
    >>> from haive.games.clue import ClueAgent, ClueConfig, ClueUI
    >>>
    >>> # Create and configure a Clue agent
    >>> config = ClueConfig()
    >>> agent = ClueAgent(config)
    >>> ui = ClueUI()
    >>>
    >>> # Initialize and display game state
    >>> state = ClueStateManager.initialize()
    >>> ui.display_state(state)
"""

from .agent import ClueAgent
from .config import ClueConfig
from .models import ClueGuess, ClueHypothesis, ClueResponse, ClueSolution
from .state import ClueState
from .state_manager import ClueStateManager
from .ui import ClueUI

__all__ = [
    "ClueAgent",
    "ClueConfig",
    "ClueGuess",
    "ClueHypothesis",
    "ClueResponse",
    "ClueSolution",
    "ClueState",
    "ClueStateManager",
    "ClueUI",
]
