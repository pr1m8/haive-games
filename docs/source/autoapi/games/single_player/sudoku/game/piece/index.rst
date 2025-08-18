games.single_player.sudoku.game.piece
=====================================

.. py:module:: games.single_player.sudoku.game.piece

Module documentation for games.single_player.sudoku.game.piece


.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span>   </div>


      
            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      games.single_player.sudoku.game.piece.SudokuDigit

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: SudokuDigit

            Bases: :py:obj:`haive.games.core.piece.base.GamePiece`\ [\ :py:obj:`haive.games.core.position.base.GridPosition`\ ]


            A digit in a Sudoku puzzle.


            .. py:method:: __str__() -> str

               String representation of the digit.



            .. py:method:: can_move_to(position: haive.games.core.position.base.GridPosition, board: Board) -> bool

               Check if this digit can be placed at the specified position.



            .. py:method:: validate_value(v: int) -> int
               :classmethod:


               Ensure value is between 1 and 9.



            .. py:attribute:: fixed
               :type:  bool
               :value: False



            .. py:attribute:: value
               :type:  int
               :value: None






----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.single_player.sudoku.game.piece import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

