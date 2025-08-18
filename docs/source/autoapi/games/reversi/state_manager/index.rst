games.reversi.state_manager
===========================

.. py:module:: games.reversi.state_manager

Reversi (Othello) game state management module.

This module provides comprehensive state management functionality for Reversi/Othello,
including move validation, disc flipping mechanics, and game progression tracking.

Reversi (also known as Othello) is a strategy board game played on an 8×8 board with
64 discs that are black on one side and white on the other. Players take turns placing
discs with their color facing up, attempting to trap opponent discs between their own
to flip them. The game starts with four discs in the center in a cross pattern.

Classes:
    ReversiStateManager: Main state management class for Reversi/Othello operations.

.. rubric:: Example

Basic Reversi game setup and play:

    >>> from haive.games.reversi.state_manager import ReversiStateManager
    >>> from haive.games.reversi.models import ReversiMove
    >>>
    >>> # Initialize standard Reversi game
    >>> state = ReversiStateManager.initialize()
    >>> print(f"Current player: {state.turn}")  # "B" (Black)
    >>> print(f"Board size: 8x8")
    >>> print(f"Black discs: {state.black_count}, White discs: {state.white_count}")
    >>>
    >>> # Get legal moves (must flip at least one opponent disc)
    >>> legal_moves = ReversiStateManager.get_legal_moves(state)
    >>> print(f"Legal moves for Black: {len(legal_moves)}")
    >>>
    >>> # Make a move
    >>> if legal_moves:
    ...     move = legal_moves[0]
    ...     new_state = ReversiStateManager.apply_move(state, move)
    ...     print(f"Move at ({move.row}, {move.col}) flipped {move.flipped_count} discs")

.. note::

   - Standard 8×8 board with initial cross pattern in center
   - Players are "B" (Black) and "W" (White) with Black moving first
   - Legal moves must flip at least one opponent disc
   - Game ends when no legal moves exist for both players
   - Winner is determined by who has more discs when game ends
   - Pass moves are automatic when no legal moves exist



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span>   </div>

.. autoapi-nested-parse::

   Reversi (Othello) game state management module.

   This module provides comprehensive state management functionality for Reversi/Othello,
   including move validation, disc flipping mechanics, and game progression tracking.

   Reversi (also known as Othello) is a strategy board game played on an 8×8 board with
   64 discs that are black on one side and white on the other. Players take turns placing
   discs with their color facing up, attempting to trap opponent discs between their own
   to flip them. The game starts with four discs in the center in a cross pattern.

   Classes:
       ReversiStateManager: Main state management class for Reversi/Othello operations.

   .. rubric:: Example

   Basic Reversi game setup and play:

       >>> from haive.games.reversi.state_manager import ReversiStateManager
       >>> from haive.games.reversi.models import ReversiMove
       >>>
       >>> # Initialize standard Reversi game
       >>> state = ReversiStateManager.initialize()
       >>> print(f"Current player: {state.turn}")  # "B" (Black)
       >>> print(f"Board size: 8x8")
       >>> print(f"Black discs: {state.black_count}, White discs: {state.white_count}")
       >>>
       >>> # Get legal moves (must flip at least one opponent disc)
       >>> legal_moves = ReversiStateManager.get_legal_moves(state)
       >>> print(f"Legal moves for Black: {len(legal_moves)}")
       >>>
       >>> # Make a move
       >>> if legal_moves:
       ...     move = legal_moves[0]
       ...     new_state = ReversiStateManager.apply_move(state, move)
       ...     print(f"Move at ({move.row}, {move.col}) flipped {move.flipped_count} discs")

   .. note::

      - Standard 8×8 board with initial cross pattern in center
      - Players are "B" (Black) and "W" (White) with Black moving first
      - Legal moves must flip at least one opponent disc
      - Game ends when no legal moves exist for both players
      - Winner is determined by who has more discs when game ends
      - Pass moves are automatic when no legal moves exist



      
            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      games.reversi.state_manager.ReversiStateManager

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: ReversiStateManager

            Bases: :py:obj:`haive.games.framework.base.state_manager.GameStateManager`\ [\ :py:obj:`haive.games.reversi.state.ReversiState`\ ]


            Manager for Reversi/Othello game state.


            .. py:method:: _get_flips(board: list[list[str | None]], row: int, col: int, player: str) -> set[tuple[int, int]]
               :classmethod:


               Get the positions of opponent's discs that would be flipped by placing.
               player's disc at (row, col).

               :param board: The current board.
               :param row: Row index of the move.
               :param col: Column index of the move.
               :param player: Player making the move ('B' or 'W').

               :returns: Positions of discs that would be flipped.
               :rtype: Set[Tuple[int, int]]



            .. py:method:: add_analysis(state: haive.games.reversi.state.ReversiState, player: str, analysis: haive.games.reversi.models.ReversiAnalysis) -> haive.games.reversi.state.ReversiState
               :classmethod:


               Add an analysis to the state.

               :param state: The current game state.
               :param player: The player who performed the analysis.
               :param analysis: The analysis to add.

               :returns: Updated state with the analysis added.
               :rtype: ReversiState



            .. py:method:: apply_move(state: haive.games.reversi.state.ReversiState, move: haive.games.reversi.models.ReversiMove) -> haive.games.reversi.state.ReversiState
               :classmethod:


               Apply a move to the current state and return the new state.

               :param state: The current game state.
               :param move: The move to apply.

               :returns: A new game state after applying the move.
               :rtype: ReversiState

               :raises ValueError: If the move is invalid.



            .. py:method:: check_game_status(state: haive.games.reversi.state.ReversiState) -> haive.games.reversi.state.ReversiState
               :classmethod:


               Check and update the game status.

               :param state: The current game state.

               :returns: The game state with updated status.
               :rtype: ReversiState



            .. py:method:: get_legal_moves(state: haive.games.reversi.state.ReversiState) -> list[haive.games.reversi.models.ReversiMove]
               :classmethod:


               Get all legal moves for the current state.

               :param state: The current game state.

               :returns: A list of all legal moves.
               :rtype: List[ReversiMove]



            .. py:method:: get_skip_move(state: haive.games.reversi.state.ReversiState) -> haive.games.reversi.state.ReversiState
               :classmethod:


               Apply a skip move when player has no legal moves.

               :param state: The current game state.

               :returns: A new game state after skipping the turn.
               :rtype: ReversiState



            .. py:method:: get_winner(state: haive.games.reversi.state.ReversiState) -> str | None
               :classmethod:


               Get the winner of the game, if any.

               :param state: The current game state.

               :returns: The winner ('B' or 'W'), or None if the game is ongoing or a draw.
               :rtype: Optional[str]



            .. py:method:: initialize(**kwargs) -> haive.games.reversi.state.ReversiState
               :classmethod:


               Initialize a new Reversi/Othello game.

               :param \*\*kwargs: Keyword arguments for game initialization.
                                  first_player: Which player goes first ('B' or 'W'). Default is 'B'.
                                  player_B: Which player is Black ('player1' or 'player2'). Default is 'player1'.
                                  player_W: Which player is White ('player1' or 'player2'). Default is 'player2'.

               :returns: A new Reversi game state.
               :rtype: ReversiState



            .. py:method:: is_legal_move(state: haive.games.reversi.state.ReversiState, row: int, col: int, player: str) -> bool
               :classmethod:


               Check if a move is legal.

               :param state: The current game state.
               :param row: Row index of the move.
               :param col: Column index of the move.
               :param player: Player making the move ('B' or 'W').

               :returns: True if the move is legal, False otherwise.
               :rtype: bool



            .. py:attribute:: DIRECTIONS





----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.reversi.state_manager import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

