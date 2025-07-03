"""Monopoly game implementation module.

This package provides a complete implementation of the Monopoly board game, including:
    - Game agent with property management
    - Player agents with trading and decision-making
    - Property buying, selling, and rent collection
    - Chance and Community Chest cards
    - Jail mechanics and special spaces

Example:
    >>> from haive.games.monopoly import MonopolyAgent, MonopolyAgentConfig
    >>> config = MonopolyAgentConfig()
    >>> agent = MonopolyAgent(config)
"""

from haive.games.monopoly.agent import (
    MonopolyAgent,
    MonopolyAgentConfig,
    MonopolyGameAgent,
    MonopolyGameAgentConfig,
    MonopolyPlayerAgent,
    MonopolyPlayerAgentConfig,
)
from haive.games.monopoly.state import MonopolyState

__all__ = [
    "MonopolyAgent",
    "MonopolyAgentConfig",
    "MonopolyGameAgent",
    "MonopolyGameAgentConfig",
    "MonopolyPlayerAgent",
    "MonopolyPlayerAgentConfig",
    "MonopolyState",
]
