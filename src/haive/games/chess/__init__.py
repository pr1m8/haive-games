"""Chess game implementation module.

This package provides a complete implementation of the Chess game, including:
    - Game agent with LLM-powered players
    - State management with FEN support
    - Position analysis and evaluation
    - Move validation and piece movement
    - Game visualization

Example:
    >>> from haive.games.chess import ChessAgent, ChessConfig
    >>>
    >>> # Create and configure a Chess agent
    >>> config = ChessConfig(enable_analysis=True)
    >>> agent = ChessAgent(config)
"""

from haive.games.chess.agent import ChessAgent
from haive.games.chess.config import ChessConfig
from haive.games.chess.models import (
    ChessAnalysis,
    ChessMoveModel,
    ChessPlayerDecision,
)
from haive.games.chess.state import ChessState
from haive.games.chess.state_manager import ChessGameStateManager

__all__ = [
    "ChessAgent",
    "ChessConfig",
    "ChessAnalysis",
    "ChessGameStateManager",
    "ChessMoveModel",
    "ChessPlayerDecision",
    "ChessState",
]
