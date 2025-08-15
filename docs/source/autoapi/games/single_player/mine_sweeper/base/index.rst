games.single_player.mine_sweeper.base
=====================================

.. py:module:: games.single_player.mine_sweeper.base


Classes
-------

.. autoapisummary::

   games.single_player.mine_sweeper.base.CellState
   games.single_player.mine_sweeper.base.Difficulty
   games.single_player.mine_sweeper.base.MinePiece
   games.single_player.mine_sweeper.base.MinesweeperBoard
   games.single_player.mine_sweeper.base.MinesweeperCell
   games.single_player.mine_sweeper.base.MinesweeperGame


Module Contents
---------------

.. py:class:: CellState

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Possible states of a Minesweeper cell.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: CellState
      :collapse:

   .. py:attribute:: FLAGGED
      :value: 'flagged'



   .. py:attribute:: HIDDEN
      :value: 'hidden'



   .. py:attribute:: QUESTIONED
      :value: 'questioned'



   .. py:attribute:: REVEALED
      :value: 'revealed'



.. py:class:: Difficulty

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Difficulty levels for Minesweeper.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: Difficulty
      :collapse:

   .. py:attribute:: BEGINNER
      :value: 'beginner'



   .. py:attribute:: CUSTOM
      :value: 'custom'



   .. py:attribute:: EXPERT
      :value: 'expert'



   .. py:attribute:: INTERMEDIATE
      :value: 'intermediate'



.. py:class:: MinePiece

   Bases: :py:obj:`game_framework_base.GamePiece`\ [\ :py:obj:`game_framework_base.GridPosition`\ ]


   Represents a mine in Minesweeper.


   .. autolink-examples:: MinePiece
      :collapse:

   .. py:method:: __str__() -> str

      String representation of a mine.


      .. autolink-examples:: __str__
         :collapse:


   .. py:method:: can_move_to(position: game_framework_base.GridPosition, board: Board) -> bool

      Mines can't move in Minesweeper.


      .. autolink-examples:: can_move_to
         :collapse:


.. py:class:: MinesweeperBoard

   Bases: :py:obj:`game_framework_base.GridBoard`\ [\ :py:obj:`MinesweeperCell`\ , :py:obj:`game_framework_base.GridPosition`\ , :py:obj:`MinePiece`\ ]


   The Minesweeper game board.


   .. autolink-examples:: MinesweeperBoard
      :collapse:

   .. py:method:: _calculate_adjacent_mines() -> None

      Calculate the number of adjacent mines for each cell.


      .. autolink-examples:: _calculate_adjacent_mines
         :collapse:


   .. py:method:: chord(row: int, col: int) -> tuple[bool, int]

      Perform a chord (middle-click) to reveal all unflagged neighbors. Only works.
      if the number of flagged neighbors equals the cell's value.

      :param row: Row to chord
      :param col: Column to chord

      :returns: Tuple of (hit_mine, cells_revealed)


      .. autolink-examples:: chord
         :collapse:


   .. py:method:: get_board_state() -> list[list[str]]

      Get the current visible board state as a 2D array.


      .. autolink-examples:: get_board_state
         :collapse:


   .. py:method:: get_mine_locations() -> list[tuple[int, int]]

      Get the locations of all mines.


      .. autolink-examples:: get_mine_locations
         :collapse:


   .. py:method:: get_remaining_mines() -> int

      Get the number of unflagged mines (for display).


      .. autolink-examples:: get_remaining_mines
         :collapse:


   .. py:method:: initialize_board(difficulty: Difficulty = Difficulty.BEGINNER, custom_rows: int | None = None, custom_cols: int | None = None, custom_mines: int | None = None) -> None

      Initialize the Minesweeper board based on difficulty.


      .. autolink-examples:: initialize_board
         :collapse:


   .. py:method:: is_game_won() -> bool

      Check if the game has been won (all non-mine cells revealed).


      .. autolink-examples:: is_game_won
         :collapse:


   .. py:method:: place_mines(first_click_row: int, first_click_col: int) -> None

      Place mines randomly, ensuring the first click is safe.

      :param first_click_row: Row of first click
      :param first_click_col: Column of first click


      .. autolink-examples:: place_mines
         :collapse:


   .. py:method:: reveal_all_mines() -> None

      Reveal all mines (for game over).


      .. autolink-examples:: reveal_all_mines
         :collapse:


   .. py:method:: reveal_cell(row: int, col: int) -> tuple[bool, int]

      Reveal a cell at the specified position.

      :param row: Row to reveal
      :param col: Column to reveal

      :returns: Tuple of (hit_mine, cells_revealed)


      .. autolink-examples:: reveal_cell
         :collapse:


   .. py:method:: toggle_flag(row: int, col: int) -> bool

      Toggle the flag state of a cell.

      :param row: Row to toggle
      :param col: Column to toggle

      :returns: True if flag was placed, False if removed or state is questioned


      .. autolink-examples:: toggle_flag
         :collapse:


   .. py:attribute:: DIFFICULTY_SETTINGS


   .. py:attribute:: first_move_made
      :type:  bool
      :value: False



   .. py:attribute:: flagged_count
      :type:  int
      :value: 0



   .. py:attribute:: revealed_count
      :type:  int
      :value: 0



   .. py:attribute:: total_mines
      :type:  int
      :value: 0



.. py:class:: MinesweeperCell

   Bases: :py:obj:`game_framework_base.GridSpace`\ [\ :py:obj:`MinePiece`\ ]


   A cell in the Minesweeper grid.


   .. autolink-examples:: MinesweeperCell
      :collapse:

   .. py:method:: get_display_value() -> str

      Get the display value for this cell based on its state.


      .. autolink-examples:: get_display_value
         :collapse:


   .. py:method:: is_flagged() -> bool

      Check if this cell has been flagged.


      .. autolink-examples:: is_flagged
         :collapse:


   .. py:method:: is_mine() -> bool

      Check if this cell contains a mine.


      .. autolink-examples:: is_mine
         :collapse:


   .. py:method:: is_questioned() -> bool

      Check if this cell has been marked with a question.


      .. autolink-examples:: is_questioned
         :collapse:


   .. py:method:: is_revealed() -> bool

      Check if this cell has been revealed.


      .. autolink-examples:: is_revealed
         :collapse:


   .. py:method:: place_mine() -> None

      Place a mine in this cell.


      .. autolink-examples:: place_mine
         :collapse:


   .. py:method:: reveal() -> bool

      Reveal this cell.

      :returns: True if it's a mine (game over), False otherwise


      .. autolink-examples:: reveal
         :collapse:


   .. py:method:: set_adjacent_mines(count: int) -> None

      Set the number of adjacent mines.


      .. autolink-examples:: set_adjacent_mines
         :collapse:


   .. py:method:: toggle_flag() -> CellState

      Toggle flag state: hidden -> flagged -> questioned -> hidden.

      :returns: The new state


      .. autolink-examples:: toggle_flag
         :collapse:


   .. py:attribute:: adjacent_mines
      :type:  int
      :value: 0



   .. py:attribute:: has_mine
      :type:  bool
      :value: False



   .. py:attribute:: state
      :type:  CellState


.. py:class:: MinesweeperGame(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Model for managing a Minesweeper game.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: MinesweeperGame
      :collapse:

   .. py:method:: __str__() -> str

      String representation of the game.


      .. autolink-examples:: __str__
         :collapse:


   .. py:method:: chord(row: int, col: int) -> tuple[bool, bool, int]

      Perform a chord action.

      :param row: Row to chord
      :param col: Column to chord

      :returns: Tuple of (success, hit_mine, cells_revealed)


      .. autolink-examples:: chord
         :collapse:


   .. py:method:: get_elapsed_time() -> int

      Get the elapsed time in seconds.


      .. autolink-examples:: get_elapsed_time
         :collapse:


   .. py:method:: get_status() -> dict[str, Any]

      Get the current game status.


      .. autolink-examples:: get_status
         :collapse:


   .. py:method:: make_move(row: int, col: int) -> tuple[bool, bool, int]

      Make a move by revealing a cell.

      :param row: Row to reveal
      :param col: Column to reveal

      :returns: Tuple of (success, hit_mine, cells_revealed)


      .. autolink-examples:: make_move
         :collapse:


   .. py:method:: new_game(difficulty: Difficulty = Difficulty.BEGINNER, custom_rows: int | None = None, custom_cols: int | None = None, custom_mines: int | None = None) -> MinesweeperGame
      :classmethod:


      Create a new Minesweeper game with the specified difficulty.


      .. autolink-examples:: new_game
         :collapse:


   .. py:method:: restart() -> None

      Restart the game with the same settings.


      .. autolink-examples:: restart
         :collapse:


   .. py:method:: toggle_flag(row: int, col: int) -> bool

      Toggle flag on a cell.

      :param row: Row to toggle
      :param col: Column to toggle

      :returns: True if successful, False otherwise


      .. autolink-examples:: toggle_flag
         :collapse:


   .. py:method:: validate_game() -> MinesweeperGame

      Ensure game has valid components.


      .. autolink-examples:: validate_game
         :collapse:


   .. py:attribute:: board
      :type:  MinesweeperBoard


   .. py:attribute:: difficulty
      :type:  Difficulty


   .. py:attribute:: end_time
      :type:  float | None
      :value: None



   .. py:attribute:: game_over
      :type:  bool
      :value: False



   .. py:attribute:: id
      :type:  str
      :value: None



   .. py:attribute:: start_time
      :type:  float | None
      :value: None



   .. py:attribute:: win
      :type:  bool
      :value: False



