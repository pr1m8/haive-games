games.single_player.twenty_fourty_eight.game.board
==================================================

.. py:module:: games.single_player.twenty_fourty_eight.game.board


Classes
-------

.. autoapisummary::

   games.single_player.twenty_fourty_eight.game.board.TwentyFortyEightBoard


Module Contents
---------------

.. py:class:: TwentyFortyEightBoard

   Bases: :py:obj:`GridBoard`\ [\ :py:obj:`TwentyFortyEightSquare`\ , :py:obj:`GridPosition`\ , :py:obj:`NumberTile`\ ]


   The 2048 game board with sliding and merging mechanics.


   .. autolink-examples:: TwentyFortyEightBoard
      :collapse:

   .. py:method:: _move_tile(row: int, col: int, dr: int, dc: int) -> bool

      Try to move a tile from (row, col) in direction (dr, dc).

      :returns: True if the tile moved, False otherwise


      .. autolink-examples:: _move_tile
         :collapse:


   .. py:method:: clear() -> None

      Clear all tiles from the board.


      .. autolink-examples:: clear
         :collapse:


   .. py:method:: get_board_state() -> list[list[int]]

      Get the current board state as a 2D array of values.


      .. autolink-examples:: get_board_state
         :collapse:


   .. py:method:: get_max_tile() -> int

      Get the highest tile value on the board.


      .. autolink-examples:: get_max_tile
         :collapse:


   .. py:method:: has_valid_moves() -> bool

      Check if there are any valid moves remaining.


      .. autolink-examples:: has_valid_moves
         :collapse:


   .. py:method:: has_winning_tile(target: int = 2048) -> bool

      Check if the target tile value has been reached.


      .. autolink-examples:: has_winning_tile
         :collapse:


   .. py:method:: initialize_board() -> None

      Initialize an empty 4x4 grid.


      .. autolink-examples:: initialize_board
         :collapse:


   .. py:method:: move_tiles(direction: Direction) -> bool

      Move all tiles in the specified direction, merging where possible.

      :returns: True if any tiles moved, False otherwise


      .. autolink-examples:: move_tiles
         :collapse:


   .. py:method:: spawn_random_tile() -> NumberTile | None

      Spawn a new tile (2 or 4) in a random empty space.


      .. autolink-examples:: spawn_random_tile
         :collapse:


   .. py:attribute:: cols
      :type:  int
      :value: 4



   .. py:attribute:: rows
      :type:  int
      :value: 4



   .. py:attribute:: score
      :type:  int
      :value: 0



