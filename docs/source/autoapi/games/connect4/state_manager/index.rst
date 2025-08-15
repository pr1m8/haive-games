games.connect4.state_manager
============================

.. py:module:: games.connect4.state_manager

.. autoapi-nested-parse::

   Connect Four game state management module.

   This module provides comprehensive state management functionality for the Connect Four
   game, including board management, move validation, win detection, and game status tracking.

   Connect Four is a strategy game played on a 7×6 grid where players take turns dropping
   colored pieces into columns. The pieces fall to the lowest available position in the
   chosen column. The first player to get four pieces in a row (horizontally, vertically,
   or diagonally) wins the game.

   Classes:
       Connect4StateManager: Main state management class for Connect Four operations.

   .. rubric:: Example

   Basic Connect Four game setup and play:

       >>> from haive.games.connect4.state_manager import Connect4StateManager
       >>> from haive.games.connect4.models import Connect4Move
       >>>
       >>> # Initialize game (red player starts)
       >>> state = Connect4StateManager.initialize()
       >>> print(f"Current player: {state.current_player}")  # "red"
       >>> print(f"Board size: {len(state.board)}x{len(state.board[0])}")  # "6x7"
       >>>
       >>> # Drop piece in center column
       >>> move = Connect4Move(column=3, explanation="Center play")
       >>> new_state = Connect4StateManager.apply_move(state, move)
       >>>
       >>> # Check if column is full
       >>> legal_moves = Connect4StateManager.get_legal_moves(new_state)
       >>> print(f"Available columns: {[m.column for m in legal_moves]}")

   .. note::

      - Columns are 0-indexed (0-6 for a standard 7-column board)
      - Players alternate between "red" and "yellow"
      - Pieces are placed at the bottom-most available position in each column
      - The game ends when a player gets 4 in a row or the board is full (draw)


   .. autolink-examples:: games.connect4.state_manager
      :collapse:


Classes
-------

.. autoapisummary::

   games.connect4.state_manager.Connect4StateManager


Module Contents
---------------

.. py:class:: Connect4StateManager

   Bases: :py:obj:`haive.games.framework.base.state_manager.GameStateManager`\ [\ :py:obj:`haive.games.connect4.state.Connect4State`\ ]


   Manager for Connect4 game state.

   This class provides methods for managing Connect4 game state, including:
       - Game initialization
       - Move application and validation
       - Win condition checking
       - Game state conversion

   The state manager follows the immutable state pattern, creating
   new state instances rather than modifying existing ones.



   .. autolink-examples:: Connect4StateManager
      :collapse:

   .. py:method:: _check_win(state: haive.games.connect4.state.Connect4State, row: int, col: int) -> bool
      :classmethod:


      Check if there's a win at the specified position.

      Checks for four in a row horizontally, vertically, and diagonally
      after a piece is placed at the specified position.

      :param state: Current game state
      :param row: Row index where the piece was placed
      :param col: Column index where the piece was placed

      :returns: True if there's a win, False otherwise
      :rtype: bool


      .. autolink-examples:: _check_win
         :collapse:


   .. py:method:: apply_move(state: haive.games.connect4.state.Connect4State, move: haive.games.connect4.models.Connect4Move) -> haive.games.connect4.state.Connect4State
      :classmethod:


      Apply a move to the Connect4 state.

      Applies the given move to the game state, updating the board,
      checking win conditions, and switching turns as appropriate.

      :param state: Current game state
      :param move: Move to apply

      :returns: Updated game state after applying the move
      :rtype: Connect4State

      :raises ValueError: If the move is invalid (column full or out of range)

      .. rubric:: Example

      >>> state = Connect4StateManager.initialize()
      >>> move = Connect4Move(column=3)
      >>> new_state = Connect4StateManager.apply_move(state, move)
      >>> new_state.turn
      'yellow'


      .. autolink-examples:: apply_move
         :collapse:


   .. py:method:: check_game_over(state: haive.games.connect4.state.Connect4State) -> bool
      :classmethod:


      Check if the game is over (win or draw).

      :param state: Current game state

      :returns: True if the game is over, False otherwise
      :rtype: bool

      .. rubric:: Example

      >>> state = Connect4StateManager.initialize()
      >>> Connect4StateManager.check_game_over(state)
      False


      .. autolink-examples:: check_game_over
         :collapse:


   .. py:method:: ensure_state(state: dict[str, Any] | haive.games.connect4.state.Connect4State) -> haive.games.connect4.state.Connect4State
      :classmethod:


      Ensure the input is a proper Connect4State object.

      :param state: State object or dictionary

      :returns: Properly typed state object
      :rtype: Connect4State

      .. rubric:: Example

      >>> state_dict = {"board": [[None for _ in range(7)] for _ in range(6)],
      ...               "turn": "red", "game_status": "ongoing"}
      >>> state = Connect4StateManager.ensure_state(state_dict)
      >>> isinstance(state, Connect4State)
      True


      .. autolink-examples:: ensure_state
         :collapse:


   .. py:method:: get_legal_moves(state: haive.games.connect4.state.Connect4State) -> list[haive.games.connect4.models.Connect4Move]
      :classmethod:


      Get all legal moves for the current game state.

      Returns a list of all valid moves (non-full columns) for the current player.

      :param state: Current game state

      :returns: List of legal moves
      :rtype: list[Connect4Move]

      .. rubric:: Example

      >>> state = Connect4StateManager.initialize()
      >>> legal_moves = Connect4StateManager.get_legal_moves(state)
      >>> len(legal_moves)
      7  # All columns are empty in a new game


      .. autolink-examples:: get_legal_moves
         :collapse:


   .. py:method:: initialize() -> haive.games.connect4.state.Connect4State
      :classmethod:


      Initialize a new Connect4 game.

      Creates a fresh Connect4 game state with an empty board,
      red player starting, and game status set to ongoing.

      :returns: A new game state with default settings
      :rtype: Connect4State

      .. rubric:: Example

      >>> state = Connect4StateManager.initialize()
      >>> state.turn
      'red'
      >>> state.game_status
      'ongoing'


      .. autolink-examples:: initialize
         :collapse:


