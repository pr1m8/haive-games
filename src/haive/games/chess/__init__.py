"""Chess game module.

A complete implementation of chess using AI-powered players that can
analyze positions, plan moves, and play strategic games using large
language models for decision making.

Key Components:
    ChessAgent: Main agent orchestrating LLM-powered chess gameplay
    ChessConfig: Configuration for chess game parameters and LLM engines
    ChessState: Game state management with board position tracking
    ChessMoveModel: Structured move representation with UCI notation
    ChessPlayerDecision: Player decision model with move and reasoning
    ChessAnalysis: Position analysis and evaluation

Example:
    >>> from haive.games.chess import ChessAgent, ChessConfig
    >>> config = ChessConfig()
    >>> agent = ChessAgent(config)
    >>> result = agent.run_game()
"""

from haive.games.chess.agent import ChessAgent
from haive.games.chess.config import ChessConfig
from haive.games.chess.models import (
    ChessAnalysis,
    ChessMoveModel,
    ChessMoveValidation,
    ChessPlayerDecision,
)
from haive.games.chess.state import ChessState

__all__ = [
    "ChessAgent",
    "ChessAnalysis",
    "ChessConfig",
    "ChessMoveModel",
    "ChessMoveValidation",
    "ChessPlayerDecision",
    "ChessState",
]
