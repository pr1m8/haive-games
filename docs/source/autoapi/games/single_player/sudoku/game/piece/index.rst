games.single_player.sudoku.game.piece
=====================================

.. py:module:: games.single_player.sudoku.game.piece


Classes
-------

.. autoapisummary::

   games.single_player.sudoku.game.piece.SudokuDigit


Module Contents
---------------

.. py:class:: SudokuDigit

   Bases: :py:obj:`haive.games.core.piece.base.GamePiece`\ [\ :py:obj:`haive.games.core.position.base.GridPosition`\ ]


   A digit in a Sudoku puzzle.


   .. autolink-examples:: SudokuDigit
      :collapse:

   .. py:method:: __str__() -> str

      String representation of the digit.


      .. autolink-examples:: __str__
         :collapse:


   .. py:method:: can_move_to(position: haive.games.core.position.base.GridPosition, board: Board) -> bool

      Check if this digit can be placed at the specified position.


      .. autolink-examples:: can_move_to
         :collapse:


   .. py:method:: validate_value(v: int) -> int
      :classmethod:


      Ensure value is between 1 and 9.


      .. autolink-examples:: validate_value
         :collapse:


   .. py:attribute:: fixed
      :type:  bool
      :value: False



   .. py:attribute:: value
      :type:  int
      :value: None



