"""Monopoly Agent module - Main agent interface.

This module provides the main agent interface for Monopoly games,
wrapping the game agent and providing a simplified interface.
"""

from .monopoly.game_agent import MonopolyGameAgent, MonopolyGameAgentConfig
from .monopoly.player_agent import (
    MonopolyPlayerAgent,
    MonopolyPlayerAgentConfig,
)
from .monopoly.state import MonopolyState

# Export the main classes for easy importing
__all__ = [
    "MonopolyGameAgent",
    "MonopolyGameAgentConfig",
    "MonopolyPlayerAgent",
    "MonopolyPlayerAgentConfig",
    "MonopolyState",
]

# For compatibility, provide aliases
MonopolyAgent = MonopolyGameAgent
MonopolyAgentConfig = MonopolyGameAgentConfig
