
:py:mod:`games`
===============

.. py:module:: games

Haive Games - Comprehensive game environment collection.

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

.. rubric:: Examples

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


.. autolink-examples:: games
   :collapse:




