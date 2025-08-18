games.single_player.twenty_fourty_eight.game.board
==================================================

.. py:module:: games.single_player.twenty_fourty_eight.game.board

Module documentation for games.single_player.twenty_fourty_eight.game.board


.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span>   </div>


      
            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      games.single_player.twenty_fourty_eight.game.board.TwentyFortyEightBoard

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: TwentyFortyEightBoard

            Bases: :py:obj:`GridBoard`\ [\ :py:obj:`TwentyFortyEightSquare`\ , :py:obj:`GridPosition`\ , :py:obj:`NumberTile`\ ]


            The 2048 game board with sliding and merging mechanics.


            .. py:method:: _move_tile(row: int, col: int, dr: int, dc: int) -> bool

               Try to move a tile from (row, col) in direction (dr, dc).

               :returns: True if the tile moved, False otherwise



            .. py:method:: clear() -> None

               Clear all tiles from the board.



            .. py:method:: get_board_state() -> list[list[int]]

               Get the current board state as a 2D array of values.



            .. py:method:: get_max_tile() -> int

               Get the highest tile value on the board.



            .. py:method:: has_valid_moves() -> bool

               Check if there are any valid moves remaining.



            .. py:method:: has_winning_tile(target: int = 2048) -> bool

               Check if the target tile value has been reached.



            .. py:method:: initialize_board() -> None

               Initialize an empty 4x4 grid.



            .. py:method:: move_tiles(direction: Direction) -> bool

               Move all tiles in the specified direction, merging where possible.

               :returns: True if any tiles moved, False otherwise



            .. py:method:: spawn_random_tile() -> NumberTile | None

               Spawn a new tile (2 or 4) in a random empty space.



            .. py:attribute:: cols
               :type:  int
               :value: 4



            .. py:attribute:: rows
               :type:  int
               :value: 4



            .. py:attribute:: score
               :type:  int
               :value: 0






----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.single_player.twenty_fourty_eight.game.board import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

