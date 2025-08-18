games.core.piece.tile
=====================

.. py:module:: games.core.piece.tile

Module documentation for games.core.piece.tile


.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span>   </div>


      
            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      games.core.piece.tile.Tile

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: Tile

            Bases: :py:obj:`GamePiece`\ [\ :py:obj:`P`\ ]


            A tile used in tile-based games (Scrabble, Mahjong, etc.).


            .. py:method:: can_move_to(position: P, board: Board) -> bool

               Check if this tile can be placed at the specified position.



            .. py:method:: flip() -> None

               Flip the tile's face.



            .. py:attribute:: face_up
               :type:  bool
               :value: True



            .. py:attribute:: value
               :type:  int
               :value: 0






----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.core.piece.tile import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

