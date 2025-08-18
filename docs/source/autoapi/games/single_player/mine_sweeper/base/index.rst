games.single_player.mine_sweeper.base
=====================================

.. py:module:: games.single_player.mine_sweeper.base

Module documentation for games.single_player.mine_sweeper.base


.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">6 classes</span>   </div>


      
            
            

.. admonition:: Classes (6)
   :class: note

   .. autoapisummary::

      games.single_player.mine_sweeper.base.CellState
      games.single_player.mine_sweeper.base.Difficulty
      games.single_player.mine_sweeper.base.MinePiece
      games.single_player.mine_sweeper.base.MinesweeperBoard
      games.single_player.mine_sweeper.base.MinesweeperCell
      games.single_player.mine_sweeper.base.MinesweeperGame

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: CellState

            Bases: :py:obj:`str`, :py:obj:`enum.Enum`


            Possible states of a Minesweeper cell.

            Initialize self.  See help(type(self)) for accurate signature.


            .. py:attribute:: FLAGGED
               :value: 'flagged'



            .. py:attribute:: HIDDEN
               :value: 'hidden'



            .. py:attribute:: QUESTIONED
               :value: 'questioned'



            .. py:attribute:: REVEALED
               :value: 'revealed'




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: Difficulty

            Bases: :py:obj:`str`, :py:obj:`enum.Enum`


            Difficulty levels for Minesweeper.

            Initialize self.  See help(type(self)) for accurate signature.


            .. py:attribute:: BEGINNER
               :value: 'beginner'



            .. py:attribute:: CUSTOM
               :value: 'custom'



            .. py:attribute:: EXPERT
               :value: 'expert'



            .. py:attribute:: INTERMEDIATE
               :value: 'intermediate'




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: MinePiece

            Bases: :py:obj:`game_framework_base.GamePiece`\ [\ :py:obj:`game_framework_base.GridPosition`\ ]


            Represents a mine in Minesweeper.


            .. py:method:: __str__() -> str

               String representation of a mine.



            .. py:method:: can_move_to(position: game_framework_base.GridPosition, board: Board) -> bool

               Mines can't move in Minesweeper.




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: MinesweeperBoard

            Bases: :py:obj:`game_framework_base.GridBoard`\ [\ :py:obj:`MinesweeperCell`\ , :py:obj:`game_framework_base.GridPosition`\ , :py:obj:`MinePiece`\ ]


            The Minesweeper game board.


            .. py:method:: _calculate_adjacent_mines() -> None

               Calculate the number of adjacent mines for each cell.



            .. py:method:: chord(row: int, col: int) -> tuple[bool, int]

               Perform a chord (middle-click) to reveal all unflagged neighbors. Only works.
               if the number of flagged neighbors equals the cell's value.

               :param row: Row to chord
               :param col: Column to chord

               :returns: Tuple of (hit_mine, cells_revealed)



            .. py:method:: get_board_state() -> list[list[str]]

               Get the current visible board state as a 2D array.



            .. py:method:: get_mine_locations() -> list[tuple[int, int]]

               Get the locations of all mines.



            .. py:method:: get_remaining_mines() -> int

               Get the number of unflagged mines (for display).



            .. py:method:: initialize_board(difficulty: Difficulty = Difficulty.BEGINNER, custom_rows: int | None = None, custom_cols: int | None = None, custom_mines: int | None = None) -> None

               Initialize the Minesweeper board based on difficulty.



            .. py:method:: is_game_won() -> bool

               Check if the game has been won (all non-mine cells revealed).



            .. py:method:: place_mines(first_click_row: int, first_click_col: int) -> None

               Place mines randomly, ensuring the first click is safe.

               :param first_click_row: Row of first click
               :param first_click_col: Column of first click



            .. py:method:: reveal_all_mines() -> None

               Reveal all mines (for game over).



            .. py:method:: reveal_cell(row: int, col: int) -> tuple[bool, int]

               Reveal a cell at the specified position.

               :param row: Row to reveal
               :param col: Column to reveal

               :returns: Tuple of (hit_mine, cells_revealed)



            .. py:method:: toggle_flag(row: int, col: int) -> bool

               Toggle the flag state of a cell.

               :param row: Row to toggle
               :param col: Column to toggle

               :returns: True if flag was placed, False if removed or state is questioned



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




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: MinesweeperCell

            Bases: :py:obj:`game_framework_base.GridSpace`\ [\ :py:obj:`MinePiece`\ ]


            A cell in the Minesweeper grid.


            .. py:method:: get_display_value() -> str

               Get the display value for this cell based on its state.



            .. py:method:: is_flagged() -> bool

               Check if this cell has been flagged.



            .. py:method:: is_mine() -> bool

               Check if this cell contains a mine.



            .. py:method:: is_questioned() -> bool

               Check if this cell has been marked with a question.



            .. py:method:: is_revealed() -> bool

               Check if this cell has been revealed.



            .. py:method:: place_mine() -> None

               Place a mine in this cell.



            .. py:method:: reveal() -> bool

               Reveal this cell.

               :returns: True if it's a mine (game over), False otherwise



            .. py:method:: set_adjacent_mines(count: int) -> None

               Set the number of adjacent mines.



            .. py:method:: toggle_flag() -> CellState

               Toggle flag state: hidden -> flagged -> questioned -> hidden.

               :returns: The new state



            .. py:attribute:: adjacent_mines
               :type:  int
               :value: 0



            .. py:attribute:: has_mine
               :type:  bool
               :value: False



            .. py:attribute:: state
               :type:  CellState



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: MinesweeperGame(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            Model for managing a Minesweeper game.

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:method:: __str__() -> str

               String representation of the game.



            .. py:method:: chord(row: int, col: int) -> tuple[bool, bool, int]

               Perform a chord action.

               :param row: Row to chord
               :param col: Column to chord

               :returns: Tuple of (success, hit_mine, cells_revealed)



            .. py:method:: get_elapsed_time() -> int

               Get the elapsed time in seconds.



            .. py:method:: get_status() -> dict[str, Any]

               Get the current game status.



            .. py:method:: make_move(row: int, col: int) -> tuple[bool, bool, int]

               Make a move by revealing a cell.

               :param row: Row to reveal
               :param col: Column to reveal

               :returns: Tuple of (success, hit_mine, cells_revealed)



            .. py:method:: new_game(difficulty: Difficulty = Difficulty.BEGINNER, custom_rows: int | None = None, custom_cols: int | None = None, custom_mines: int | None = None) -> MinesweeperGame
               :classmethod:


               Create a new Minesweeper game with the specified difficulty.



            .. py:method:: restart() -> None

               Restart the game with the same settings.



            .. py:method:: toggle_flag(row: int, col: int) -> bool

               Toggle flag on a cell.

               :param row: Row to toggle
               :param col: Column to toggle

               :returns: True if successful, False otherwise



            .. py:method:: validate_game() -> MinesweeperGame

               Ensure game has valid components.



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






----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.single_player.mine_sweeper.base import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

