games.single_player.sudoku.game.cell
====================================

.. py:module:: games.single_player.sudoku.game.cell

Module documentation for games.single_player.sudoku.game.cell


.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span>   </div>


      
            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      games.single_player.sudoku.game.cell.SudokuCell

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: SudokuCell

            Bases: :py:obj:`haive.games.core.position.base.GridSpace`\ [\ :py:obj:`haive.games.single_player.sudoku.game.piece.SudokuDigit`\ ]


            A cell in the Sudoku grid.


            .. py:method:: clear() -> bool

               Clear this cell.



            .. py:method:: place_digit(digit: haive.games.single_player.sudoku.game.piece.SudokuDigit) -> bool

               Place a digit in this cell.



            .. py:method:: set_value(value: int, fixed: bool = False) -> bool

               Set a value in this cell.



            .. py:method:: update_candidates(invalid_values: set[int]) -> None

               Update candidate values by removing invalid options.



            .. py:attribute:: candidates
               :type:  set[int]
               :value: None



            .. py:property:: is_fixed
               :type: bool


               Check if this cell has a fixed value.


            .. py:property:: value
               :type: int | None


               Get the current value of this cell.





----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.single_player.sudoku.game.cell import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

