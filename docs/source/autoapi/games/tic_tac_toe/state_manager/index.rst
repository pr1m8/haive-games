games.tic_tac_toe.state_manager
===============================

.. py:module:: games.tic_tac_toe.state_manager

.. autoapi-nested-parse::

   Tic Tac Toe game state management module.

   This module provides comprehensive state management functionality for the classic
   Tic Tac Toe game, including board initialization, move validation, win detection,
   and game status tracking.

   Tic Tac Toe is a classic strategy game played on a 3×3 grid where players take
   turns placing their marks (X or O) in empty squares. The first player to get
   three marks in a row (horizontally, vertically, or diagonally) wins.

   Classes:
       TicTacToeStateManager: Main state management class for Tic Tac Toe operations.

   .. rubric:: Example

   Basic Tic Tac Toe game setup and play:

       >>> from haive.games.tic_tac_toe.state_manager import TicTacToeStateManager
       >>> from haive.games.tic_tac_toe.models import TicTacToeMove
       >>>
       >>> # Initialize game
       >>> state = TicTacToeStateManager.initialize()
       >>> print(f"Current player: {state.turn}")
       >>>
       >>> # Make a move in the center
       >>> move = TicTacToeMove(row=1, col=1, player="X")
       >>> new_state = TicTacToeStateManager.apply_move(state, move)
       >>>
       >>> # Check for winners
       >>> winner = TicTacToeStateManager.get_winner(new_state)
       >>> print(f"Winner: {winner}")

   .. note::

      The board uses 0-based indexing where (0,0) is top-left and (2,2) is bottom-right.
      Players are represented as "X" and "O" strings in the game state.


   .. autolink-examples:: games.tic_tac_toe.state_manager
      :collapse:


Classes
-------

.. autoapisummary::

   games.tic_tac_toe.state_manager.TicTacToeStateManager


Module Contents
---------------

.. py:class:: TicTacToeStateManager

   Bases: :py:obj:`haive.games.framework.base.state_manager.GameStateManager`\ [\ :py:obj:`haive.games.tic_tac_toe.state.TicTacToeState`\ ]


   Manager for Tic Tac Toe game state.


   .. autolink-examples:: TicTacToeStateManager
      :collapse:

   .. py:method:: _is_winning_board(board: list[list[str | None]], player: str) -> bool
      :classmethod:


      Check if the board is a win for the specified player.

      :param board: The board to check.
      :param player: The player to check for ('X' or 'O').

      :returns: True if the player has won, False otherwise.
      :rtype: bool


      .. autolink-examples:: _is_winning_board
         :collapse:


   .. py:method:: add_analysis(state: haive.games.tic_tac_toe.state.TicTacToeState, player: str, analysis: haive.games.tic_tac_toe.models.TicTacToeAnalysis) -> haive.games.tic_tac_toe.state.TicTacToeState
      :classmethod:


      Add an analysis to the state.

      :param state: The current game state.
      :param player: The player who performed the analysis.
      :param analysis: The analysis to add.

      :returns: Updated state with the analysis added.
      :rtype: TicTacToeState


      .. autolink-examples:: add_analysis
         :collapse:


   .. py:method:: apply_move(state: haive.games.tic_tac_toe.state.TicTacToeState, move: haive.games.tic_tac_toe.models.TicTacToeMove) -> haive.games.tic_tac_toe.state.TicTacToeState
      :classmethod:


      Apply a move to the current state and return the new state.

      :param state: The current game state.
      :param move: The move to apply.

      :returns: A new game state after applying the move.
      :rtype: TicTacToeState

      :raises ValueError: If the move is invalid.


      .. autolink-examples:: apply_move
         :collapse:


   .. py:method:: check_game_status(state: haive.games.tic_tac_toe.state.TicTacToeState) -> haive.games.tic_tac_toe.state.TicTacToeState
      :classmethod:


      Check and update the game status.

      :param state: The current game state.

      :returns: The game state with updated status.
      :rtype: TicTacToeState


      .. autolink-examples:: check_game_status
         :collapse:


   .. py:method:: find_winning_move(state: haive.games.tic_tac_toe.state.TicTacToeState, player: str) -> list[tuple[int, int]]
      :classmethod:


      Find a winning move for the specified player, if any.

      :param state: The current game state.
      :param player: The player to find a winning move for ('X' or 'O').

      :returns: List of winning move coordinates (row, col), or empty list if none.
      :rtype: List[Tuple[int, int]]


      .. autolink-examples:: find_winning_move
         :collapse:


   .. py:method:: get_legal_moves(state: haive.games.tic_tac_toe.state.TicTacToeState) -> list[haive.games.tic_tac_toe.models.TicTacToeMove]
      :classmethod:


      Get all legal moves for the current state.

      :param state: The current game state.

      :returns: A list of all legal moves.
      :rtype: List[TicTacToeMove]


      .. autolink-examples:: get_legal_moves
         :collapse:


   .. py:method:: get_winner(state: haive.games.tic_tac_toe.state.TicTacToeState) -> str | None
      :classmethod:


      Get the winner of the game, if any.

      :param state: The current game state.

      :returns: The winner ('X' or 'O'), or None if the game is ongoing or a draw.
      :rtype: Optional[str]


      .. autolink-examples:: get_winner
         :collapse:


   .. py:method:: initialize(**kwargs) -> haive.games.tic_tac_toe.state.TicTacToeState
      :classmethod:


      Initialize a new Tic Tac Toe game.

      :param \*\*kwargs: Keyword arguments for game initialization.
                         first_player: Which player goes first ('X' or 'O'). Default is 'X'.
                         player_X: Which player is X ('player1' or 'player2'). Default is 'player1'.
                         player_O: Which player is O ('player1' or 'player2'). Default is 'player2'.

      :returns: A new Tic Tac Toe game state.
      :rtype: TicTacToeState


      .. autolink-examples:: initialize
         :collapse:


