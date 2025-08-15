games
=====

.. py:module:: games

.. autoapi-nested-parse::

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


Submodules
----------

.. toctree::
   :maxdepth: 1

   /autoapi/games/among_us/index
   /autoapi/games/api/index
   /autoapi/games/base/index
   /autoapi/games/base_v2/index
   /autoapi/games/battleship/index
   /autoapi/games/benchmark/index
   /autoapi/games/board/index
   /autoapi/games/cards/index
   /autoapi/games/checkers/index
   /autoapi/games/chess/index
   /autoapi/games/clue/index
   /autoapi/games/common/index
   /autoapi/games/connect4/index
   /autoapi/games/core/index
   /autoapi/games/debate/index
   /autoapi/games/debate_v2/index
   /autoapi/games/dominoes/index
   /autoapi/games/example/index
   /autoapi/games/fox_and_geese/index
   /autoapi/games/framework/index
   /autoapi/games/go/index
   /autoapi/games/hold_em/index
   /autoapi/games/llm_config_factory/index
   /autoapi/games/mafia/index
   /autoapi/games/mancala/index
   /autoapi/games/mastermind/index
   /autoapi/games/monopoly/index
   /autoapi/games/multi_player/index
   /autoapi/games/nim/index
   /autoapi/games/poker/index
   /autoapi/games/reversi/index
   /autoapi/games/risk/index
   /autoapi/games/single_player/index
   /autoapi/games/tic_tac_toe/index
   /autoapi/games/utils/index


