"""Battleship game module.

A complete implementation of the classic naval strategy game Battleship,
featuring AI-powered players that strategically place ships and hunt
opponent vessels on a grid-based battlefield.

Key Components:
    BattleshipAgent: Main game agent with LLM-powered strategy
    BattleshipAgentConfig: Configuration for game parameters
    BattleshipState: Game state management
    GamePhase: Enum for different game phases
    Ship models and utilities

Example:
    >>> from haive.games.battleship import BattleshipAgent, BattleshipAgentConfig
    >>> config = BattleshipAgentConfig()
    >>> agent = BattleshipAgent(config)
    >>> result = agent.run_game()
"""

from haive.games.battleship.agent import BattleshipAgent
from haive.games.battleship.config import BattleshipAgentConfig
from haive.games.battleship.models import (
    Coordinates,
    GamePhase,
    MoveCommand,
    MoveResult,
    PlayerBoard,
    Ship,
    ShipPlacement,
    ShipType,
)
from haive.games.battleship.state import BattleshipState

__all__ = [
    "BattleshipAgent",
    "BattleshipAgentConfig",
    "BattleshipState",
    "Coordinates",
    "GamePhase",
    "MoveCommand",
    "MoveResult",
    "PlayerBoard",
    "Ship",
    "ShipPlacement",
    "ShipType",
]
