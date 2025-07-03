"""Dominoes Game Package.

This package provides a dominoes game implementation with rich terminal UI.

Components:
    - DominoesState: Data model for the game state
    - DominoesAgent: Agent that manages the game flow
    - DominoesUI: Basic UI for game visualization
    - DominoesRichUI: Enhanced UI with improved styling and animations
    - DominoTile: Model for a domino tile
    - DominoMove: Model for a move in the game
"""

from haive.games.dominoes.agent import DominoesAgent
from haive.games.dominoes.config import DominoesAgentConfig
from haive.games.dominoes.models import (
    DominoesAnalysis,
    DominoesPlayerDecision,
    DominoMove,
    DominoTile,
)
from haive.games.dominoes.rich_ui import DominoesRichUI
from haive.games.dominoes.state import DominoesState
from haive.games.dominoes.state_manager import DominoesStateManager
from haive.games.dominoes.ui import DominoesUI

__all__ = [
    "DominoMove",
    "DominoTile",
    "DominoesAgent",
    "DominoesAgentConfig",
    "DominoesAnalysis",
    "DominoesPlayerDecision",
    "DominoesRichUI",
    "DominoesState",
    "DominoesStateManager",
    "DominoesUI",
]
