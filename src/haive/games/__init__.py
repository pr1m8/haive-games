"""Haive Games - Comprehensive game environment collection.

This package provides a rich ecosystem of game implementations designed
for AI agent training, research, and entertainment. Games range from
classic board games to card games to strategy games.

Game Categories:
    - Board Games: Chess, Checkers, Go, Reversi, Connect4, Tic-Tac-Toe
    - Card Games: Poker, Hold'em, Blackjack, UNO
    - Strategy Games: Risk, Monopoly, Debate, Mafia
    - Puzzle Games: Mancala, Mastermind, Nim, Sudoku, Wordle
    - Social Games: Among Us, Debate, Clue

Each game includes:
    - AI agent implementations with configurable difficulty
    - State management and game rules enforcement
    - Rich UI components for visualization
    - Tournament and benchmarking capabilities
    - Extensible configuration systems

Examples:
    Quick tic-tac-toe game::

        from haive.games.tic_tac_toe import TicTacToeAgent, TicTacToeState

        agent = TicTacToeAgent()
        game_state = TicTacToeState()
        result = agent.play(game_state)

    Chess with custom agents::

        from haive.games.chess import ChessAgent, ChessState

        white_agent = ChessAgent(name="white", difficulty="expert")
        black_agent = ChessAgent(name="black", difficulty="intermediate")

    Multi-player poker::

        from haive.games.poker import PokerAgent, PokerState

        agents = [PokerAgent(f"player_{i}") for i in range(4)]
        game = PokerState(players=agents)

All games support both human and AI players, with extensive configuration
options for gameplay variants, AI behavior, and visualization preferences.
"""

import lazy_loader as lazy

# Define submodules to lazy load
submodules = [
    "among_us",
    "api",
    "base",
    "base_v2",
    "battleship",
    "benchmark",
    "board",
    "cards",
    "checkers",
    "chess",
    "clue",
    "connect4",
    "core",
    "debate",
    "debate_v2",
    "dominoes",
    "example",
    "fox_and_geese",
    "framework",
    "go",
    "hold_em",
    "llm_config_factory",
    "mafia",
    "mancala",
    "mastermind",
    "monopoly",
    "multi_player",
    "nim",
    "poker",
    "reversi",
    "risk",
    "single_player",
    "tic_tac_toe",
    "utils",
]

# Define specific attributes from submodules to expose
# TODO: Customize this based on actual exports from each submodule
submod_attrs = {
    "among_us": [],  # TODO: Add specific exports from among_us
    "api": [],  # TODO: Add specific exports from api
    "base": [],  # TODO: Add specific exports from base
    "base_v2": [],  # TODO: Add specific exports from base_v2
    "battleship": [],  # TODO: Add specific exports from battleship
    "benchmark": [],  # TODO: Add specific exports from benchmark
    "board": [],  # TODO: Add specific exports from board
    "cards": [],  # TODO: Add specific exports from cards
    "checkers": [],  # TODO: Add specific exports from checkers
    "chess": [],  # TODO: Add specific exports from chess
    "clue": [],  # TODO: Add specific exports from clue
    "connect4": [],  # TODO: Add specific exports from connect4
    "core": [],  # TODO: Add specific exports from core
    "debate": [],  # TODO: Add specific exports from debate
    "debate_v2": [],  # TODO: Add specific exports from debate_v2
    "dominoes": [],  # TODO: Add specific exports from dominoes
    "example": [],  # TODO: Add specific exports from example
    "fox_and_geese": [],  # TODO: Add specific exports from fox_and_geese
    "framework": [],  # TODO: Add specific exports from framework
    "go": [],  # TODO: Add specific exports from go
    "hold_em": [],  # TODO: Add specific exports from hold_em
    "llm_config_factory": [],  # TODO: Add specific exports from llm_config_factory
    "mafia": [],  # TODO: Add specific exports from mafia
    "mancala": [],  # TODO: Add specific exports from mancala
    "mastermind": [],  # TODO: Add specific exports from mastermind
    "monopoly": [],  # TODO: Add specific exports from monopoly
    "multi_player": [],  # TODO: Add specific exports from multi_player
    "nim": [],  # TODO: Add specific exports from nim
    "poker": [],  # TODO: Add specific exports from poker
    "reversi": [],  # TODO: Add specific exports from reversi
    "risk": [],  # TODO: Add specific exports from risk
    "single_player": [],  # TODO: Add specific exports from single_player
    "tic_tac_toe": [],  # TODO: Add specific exports from tic_tac_toe
    "utils": [],  # TODO: Add specific exports from utils
}

# Attach lazy loading - this creates __getattr__, __dir__, and __all__
__getattr__, __dir__, __all__ = lazy.attach(
    __name__, submodules=submodules, submod_attrs=submod_attrs
)

# Add any eager imports here (lightweight utilities, etc.)
# Example: from .metadata import SomeUtility
# __all__ += ['SomeUtility']
