games.single_player.sudoku.game.board
=====================================

.. py:module:: games.single_player.sudoku.game.board

Module documentation for games.single_player.sudoku.game.board


.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span>   </div>


      
            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      games.single_player.sudoku.game.board.SudokuBoard

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: SudokuBoard

            Bases: :py:obj:`haive.games.core.board.base.GridBoard`\ [\ :py:obj:`haive.games.single_player.sudoku.game.cell.SudokuCell`\ , :py:obj:`haive.games.core.position.base.GridPosition`\ , :py:obj:`haive.games.single_player.sudoku.game.piece.SudokuDigit`\ ]


            The Sudoku game board with validation logic.


            .. py:method:: autosolve_step() -> bool

               Perform one step of automatic solving using basic strategies.

               :returns: True if a cell was filled, False otherwise



            .. py:method:: clear_cell(row: int, col: int) -> bool

               Clear a cell at the specified position.



            .. py:method:: get_box_values(box_row: int, box_col: int) -> list[int]

               Get all values in a 3x3 box.



            .. py:method:: get_candidates_state() -> dict[tuple[int, int], set[int]]

               Get the current candidates state.



            .. py:method:: get_column_values(col: int) -> list[int]

               Get all values in a column.



            .. py:method:: get_puzzle_state() -> list[list[int]]

               Get the current puzzle state as a 2D array.



            .. py:method:: get_row_values(row: int) -> list[int]

               Get all values in a row.



            .. py:method:: initialize_board() -> None

               Initialize an empty 9x9 Sudoku grid.



            .. py:method:: is_complete() -> bool

               Check if the puzzle is complete (all cells filled).



            .. py:method:: is_solved() -> bool

               Check if the puzzle is correctly solved.



            .. py:method:: is_valid() -> bool

               Check if the current board state is valid.



            .. py:method:: is_valid_placement(row: int, col: int, value: int) -> bool

               Check if placing a value at a position would be valid.



            .. py:method:: load_puzzle(puzzle: list[list[int]]) -> None

               Load a puzzle into the board.

               :param puzzle: 9x9 grid with digits (0 for empty cells)



            .. py:method:: set_value(row: int, col: int, value: int) -> bool

               Set a value at the specified position.



            .. py:method:: update_all_candidates() -> None

               Update candidates for all cells.



            .. py:method:: update_candidates(row: int, col: int) -> None

               Update candidates for a specific cell.



            .. py:method:: update_candidates_for_related_cells(row: int, col: int) -> None

               Update candidates for all cells related to the specified position.



            .. py:attribute:: box_size
               :type:  int
               :value: 3



            .. py:attribute:: cols
               :type:  int
               :value: 9



            .. py:attribute:: rows
               :type:  int
               :value: 9






----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.single_player.sudoku.game.board import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

