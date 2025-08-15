games.single_player.sudoku.game.board
=====================================

.. py:module:: games.single_player.sudoku.game.board


Classes
-------

.. autoapisummary::

   games.single_player.sudoku.game.board.SudokuBoard


Module Contents
---------------

.. py:class:: SudokuBoard

   Bases: :py:obj:`haive.games.core.board.base.GridBoard`\ [\ :py:obj:`haive.games.single_player.sudoku.game.cell.SudokuCell`\ , :py:obj:`haive.games.core.position.base.GridPosition`\ , :py:obj:`haive.games.single_player.sudoku.game.piece.SudokuDigit`\ ]


   The Sudoku game board with validation logic.


   .. autolink-examples:: SudokuBoard
      :collapse:

   .. py:method:: autosolve_step() -> bool

      Perform one step of automatic solving using basic strategies.

      :returns: True if a cell was filled, False otherwise


      .. autolink-examples:: autosolve_step
         :collapse:


   .. py:method:: clear_cell(row: int, col: int) -> bool

      Clear a cell at the specified position.


      .. autolink-examples:: clear_cell
         :collapse:


   .. py:method:: get_box_values(box_row: int, box_col: int) -> list[int]

      Get all values in a 3x3 box.


      .. autolink-examples:: get_box_values
         :collapse:


   .. py:method:: get_candidates_state() -> dict[tuple[int, int], set[int]]

      Get the current candidates state.


      .. autolink-examples:: get_candidates_state
         :collapse:


   .. py:method:: get_column_values(col: int) -> list[int]

      Get all values in a column.


      .. autolink-examples:: get_column_values
         :collapse:


   .. py:method:: get_puzzle_state() -> list[list[int]]

      Get the current puzzle state as a 2D array.


      .. autolink-examples:: get_puzzle_state
         :collapse:


   .. py:method:: get_row_values(row: int) -> list[int]

      Get all values in a row.


      .. autolink-examples:: get_row_values
         :collapse:


   .. py:method:: initialize_board() -> None

      Initialize an empty 9x9 Sudoku grid.


      .. autolink-examples:: initialize_board
         :collapse:


   .. py:method:: is_complete() -> bool

      Check if the puzzle is complete (all cells filled).


      .. autolink-examples:: is_complete
         :collapse:


   .. py:method:: is_solved() -> bool

      Check if the puzzle is correctly solved.


      .. autolink-examples:: is_solved
         :collapse:


   .. py:method:: is_valid() -> bool

      Check if the current board state is valid.


      .. autolink-examples:: is_valid
         :collapse:


   .. py:method:: is_valid_placement(row: int, col: int, value: int) -> bool

      Check if placing a value at a position would be valid.


      .. autolink-examples:: is_valid_placement
         :collapse:


   .. py:method:: load_puzzle(puzzle: list[list[int]]) -> None

      Load a puzzle into the board.

      :param puzzle: 9x9 grid with digits (0 for empty cells)


      .. autolink-examples:: load_puzzle
         :collapse:


   .. py:method:: set_value(row: int, col: int, value: int) -> bool

      Set a value at the specified position.


      .. autolink-examples:: set_value
         :collapse:


   .. py:method:: update_all_candidates() -> None

      Update candidates for all cells.


      .. autolink-examples:: update_all_candidates
         :collapse:


   .. py:method:: update_candidates(row: int, col: int) -> None

      Update candidates for a specific cell.


      .. autolink-examples:: update_candidates
         :collapse:


   .. py:method:: update_candidates_for_related_cells(row: int, col: int) -> None

      Update candidates for all cells related to the specified position.


      .. autolink-examples:: update_candidates_for_related_cells
         :collapse:


   .. py:attribute:: box_size
      :type:  int
      :value: 3



   .. py:attribute:: cols
      :type:  int
      :value: 9



   .. py:attribute:: rows
      :type:  int
      :value: 9



