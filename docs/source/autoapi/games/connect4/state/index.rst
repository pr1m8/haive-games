games.connect4.state
====================

.. py:module:: games.connect4.state

.. autoapi-nested-parse::

   Connect4 game state module.

   This module defines the core state representation for Connect4 games,
   including board representation, move tracking, and game status.

   .. rubric:: Example

   >>> from haive.games.connect4.state import Connect4State
   >>> from haive.games.connect4.models import Connect4Move
   >>>
   >>> # Initialize a new game
   >>> state = Connect4State.initialize()
   >>> state.board_string  # Get string representation
   >>>
   >>> # Check game properties
   >>> state.is_column_full(3)  # Check if column is full
   >>> state.get_next_row(3)    # Get next available row in column


   .. autolink-examples:: games.connect4.state
      :collapse:


Classes
-------

.. autoapisummary::

   games.connect4.state.Connect4State


Module Contents
---------------

.. py:class:: Connect4State

   Bases: :py:obj:`haive.games.framework.base.state.GameState`


   State representation for a Connect4 game.

   This class represents the complete state of a Connect4 game, including:
       - Board representation (6x7 grid)
       - Current player's turn
       - Game status and winner
       - Move history
       - Position analysis for both players

   The board is represented as a 6x7 grid of cells, where each cell can be:
       - None: Empty cell
       - "red": Red player's piece
       - "yellow": Yellow player's piece

   .. attribute:: board

      6x7 board representation (rows x columns)

      :type: list[list[str | None]]

   .. attribute:: turn

      Current player's turn

      :type: Literal["red", "yellow"]

   .. attribute:: game_status

      Game status

      :type: Literal["ongoing", "red_win", "yellow_win", "draw"]

   .. attribute:: move_history

      History of moves made in the game

      :type: list[Connect4Move]

   .. attribute:: red_analysis

      Analysis history for the red player

      :type: list[dict]

   .. attribute:: yellow_analysis

      Analysis history for the yellow player

      :type: list[dict]

   .. attribute:: winner

      Winner of the game, if any

      :type: Optional[str]

   .. attribute:: error_message

      Error message from the last operation

      :type: Optional[str]

   .. rubric:: Examples

   >>> state = Connect4State.initialize()
   >>> state.turn
   'red'
   >>> state.is_column_full(3)
   False


   .. autolink-examples:: Connect4State
      :collapse:

   .. py:method:: get_next_row(column: int) -> int | None

      Get the next available row in a column.

      Returns the row index where a piece would land if dropped in the
      specified column, or None if the column is full.

      :param column: Column index (0-6)

      :returns: Row index for the next piece, or None if column is full
      :rtype: Optional[int]

      .. rubric:: Example

      >>> state = Connect4State.initialize()
      >>> state.get_next_row(3)
      5  # Bottom row (gravity effect)


      .. autolink-examples:: get_next_row
         :collapse:


   .. py:method:: initialize()
      :classmethod:


      Initialize a new Connect4 game.

      Creates a new Connect4 game state with an empty board,
      red player starting, and game status set to ongoing.

      :returns: A new game state
      :rtype: Connect4State

      .. rubric:: Example

      >>> state = Connect4State.initialize()
      >>> state.turn
      'red'
      >>> state.game_status
      'ongoing'


      .. autolink-examples:: initialize
         :collapse:


   .. py:method:: is_column_full(column: int) -> bool

      Check if a column is full.

      :param column: Column index to check (0-6)

      :returns: True if the column is full, False otherwise
      :rtype: bool

      .. rubric:: Example

      >>> state = Connect4State.initialize()
      >>> state.is_column_full(3)
      False


      .. autolink-examples:: is_column_full
         :collapse:


   .. py:method:: validate_board_dimensions(board)
      :classmethod:


      Validate board dimensions are 6x7.

      :param board: Board to validate

      :returns: Validated board
      :rtype: list[list[str | None]]

      :raises ValueError: If board dimensions are invalid


      .. autolink-examples:: validate_board_dimensions
         :collapse:


   .. py:attribute:: board
      :type:  list[list[str | None]]
      :value: None



   .. py:property:: board_string
      :type: str


      Get a string representation of the board.

      Returns a formatted string representation of the current board state,
      with column and row indices, cell contents, and borders.

      :returns: String representation of the board
      :rtype: str

      .. rubric:: Example

      >>> state = Connect4State.initialize()
      >>> # state.board_string displays:
        0 1 2 3 4 5 6
        -------------
      0| | | | | | | |
      1| | | | | | | |
      2| | | | | | | |
      3| | | | | | | |
      4| | | | | | | |
      5| | | | | | | |
        -------------
        0 1 2 3 4 5 6

      .. autolink-examples:: board_string
         :collapse:


   .. py:attribute:: error_message
      :type:  str | None
      :value: None



   .. py:attribute:: game_status
      :type:  Literal['ongoing', 'red_win', 'yellow_win', 'draw']
      :value: None



   .. py:attribute:: move_history
      :type:  list[haive.games.connect4.models.Connect4Move]
      :value: None



   .. py:attribute:: red_analysis
      :type:  list[dict]
      :value: None



   .. py:attribute:: turn
      :type:  Literal['red', 'yellow']
      :value: None



   .. py:attribute:: winner
      :type:  str | None
      :value: None



   .. py:attribute:: yellow_analysis
      :type:  list[dict]
      :value: None



