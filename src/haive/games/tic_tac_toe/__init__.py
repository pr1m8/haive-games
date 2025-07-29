"""Tic-Tac-Toe game module.

A complete implementation of the classic Tic-Tac-Toe game using AI-powered
players that can analyze board positions, plan strategic moves, and play
competitive games using large language models for decision making.

Key Components:
    TicTacToeAgent: Main agent orchestrating LLM-powered Tic-Tac-Toe gameplay
    TicTacToeAgentConfig: Configuration for game parameters and LLM engines
    TicTacToeState: Game state management with 3x3 board tracking
    TicTacToeMove: Structured move representation with position validation
    TicTacToeAnalysis: Position analysis and strategic evaluation

Example:
    >>> from haive.games.tic_tac_toe import TicTacToeAgent, TicTacToeAgentConfig
    >>> config = TicTacToeAgentConfig()
    >>> agent = TicTacToeAgent(config)
    >>> result = agent.run_game()
"""

from haive.games.tic_tac_toe.agent import TicTacToeAgent
from haive.games.tic_tac_toe.config import TicTacToeConfig as TicTacToeAgentConfig
from haive.games.tic_tac_toe.models import (
    TicTacToeAnalysis,
    TicTacToeMove,
)
from haive.games.tic_tac_toe.state import TicTacToeState

__all__ = [
    "TicTacToeAgent",
    "TicTacToeAgentConfig",
    "TicTacToeAnalysis",
    "TicTacToeMove",
    "TicTacToeState",
]
