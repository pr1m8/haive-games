"""Mancala game module for the Haive framework.

This package implements the classic Mancala (Kalah) board game, providing:
- Data models for game state, moves, and analysis
- Game logic and rules implementation
- State management for applying moves and tracking game progress
- LLM-based agents for move generation and position analysis
- Configuration options for customizing gameplay
- Example scripts for running and testing the game

The implementation follows the standard Kalah rules:
- Players take turns sowing stones from their pits
- Stones are distributed counterclockwise, one per pit
- Players' own stores are included; opponent's stores are skipped
- If the last stone lands in the player's store, they get another turn
- If the last stone lands in an empty pit on the player's side, they capture
  that stone and all stones in the opposite pit
- Game ends when all pits on one side are empty

For a quick demonstration without dependencies, run the minimal_test.py script.
For a full game with LLM agents, run the example.py script.
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
