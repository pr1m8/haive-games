games.core.game.piece
=====================

.. py:module:: games.core.game.piece

Module documentation for games.core.game.piece


.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">2 classes</span>   </div>


      
            
            

.. admonition:: Classes (2)
   :class: note

   .. autoapisummary::

      games.core.game.piece.GamePiece
      games.core.game.piece.GamePieceProtocol

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: GamePiece(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`, :py:obj:`Generic`\ [\ :py:obj:`P`\ ]


            Base class for any game piece that can be placed on a board.

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:method:: assign_to_player(player_id: str) -> None

               Assign this piece to a player.



            .. py:method:: can_move_to(position: P, board: Board) -> bool
               :abstractmethod:


               Check if this piece can move to the specified position.



            .. py:method:: place_at(position: P) -> None

               Place this piece at the specified position.



            .. py:attribute:: id
               :type:  str
               :value: None



            .. py:attribute:: owner_id
               :type:  str | None
               :value: None



            .. py:attribute:: position
               :type:  P | None
               :value: None




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: GamePieceProtocol

            Bases: :py:obj:`Protocol`


            Protocol defining the required interface for game pieces.


            .. py:method:: assign_to_player(player_id: str) -> None


            .. py:method:: can_move_to(position: Position, board: Board) -> bool


            .. py:method:: place_at(position: Position) -> None


            .. py:attribute:: id
               :type:  str


            .. py:attribute:: owner_id
               :type:  str | None


            .. py:attribute:: position
               :type:  Position | None





----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.core.game.piece import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

