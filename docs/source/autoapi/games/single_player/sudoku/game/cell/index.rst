games.single_player.sudoku.game.cell
====================================

.. py:module:: games.single_player.sudoku.game.cell


Classes
-------

.. autoapisummary::

   games.single_player.sudoku.game.cell.SudokuCell


Module Contents
---------------

.. py:class:: SudokuCell

   Bases: :py:obj:`haive.games.core.position.base.GridSpace`\ [\ :py:obj:`haive.games.single_player.sudoku.game.piece.SudokuDigit`\ ]


   A cell in the Sudoku grid.


   .. autolink-examples:: SudokuCell
      :collapse:

   .. py:method:: clear() -> bool

      Clear this cell.


      .. autolink-examples:: clear
         :collapse:


   .. py:method:: place_digit(digit: haive.games.single_player.sudoku.game.piece.SudokuDigit) -> bool

      Place a digit in this cell.


      .. autolink-examples:: place_digit
         :collapse:


   .. py:method:: set_value(value: int, fixed: bool = False) -> bool

      Set a value in this cell.


      .. autolink-examples:: set_value
         :collapse:


   .. py:method:: update_candidates(invalid_values: set[int]) -> None

      Update candidate values by removing invalid options.


      .. autolink-examples:: update_candidates
         :collapse:


   .. py:attribute:: candidates
      :type:  set[int]
      :value: None



   .. py:property:: is_fixed
      :type: bool


      Check if this cell has a fixed value.

      .. autolink-examples:: is_fixed
         :collapse:


   .. py:property:: value
      :type: int | None


      Get the current value of this cell.

      .. autolink-examples:: value
         :collapse:


