games.core.piece.tile
=====================

.. py:module:: games.core.piece.tile


Classes
-------

.. autoapisummary::

   games.core.piece.tile.Tile


Module Contents
---------------

.. py:class:: Tile

   Bases: :py:obj:`GamePiece`\ [\ :py:obj:`P`\ ]


   A tile used in tile-based games (Scrabble, Mahjong, etc.).


   .. autolink-examples:: Tile
      :collapse:

   .. py:method:: can_move_to(position: P, board: Board) -> bool

      Check if this tile can be placed at the specified position.


      .. autolink-examples:: can_move_to
         :collapse:


   .. py:method:: flip() -> None

      Flip the tile's face.


      .. autolink-examples:: flip
         :collapse:


   .. py:attribute:: face_up
      :type:  bool
      :value: True



   .. py:attribute:: value
      :type:  int
      :value: 0



