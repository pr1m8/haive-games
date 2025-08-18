games.framework.core.piece
==========================

.. py:module:: games.framework.core.piece

Module documentation for games.framework.core.piece


.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span> • <span class="module-stat">1 attributes</span>   </div>


      

.. admonition:: Attributes (1)
   :class: tip

   .. autoapisummary::

      games.framework.core.piece.P

            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      games.framework.core.piece.GamePiece

            
            

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

            GamePiece serves as the foundation for all movable objects in games, such as chess
            pieces, playing cards, tiles, etc.


            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:class:: Config

               .. py:attribute:: arbitrary_types_allowed
                  :value: True




            .. py:method:: assign_to_player(player_id: str) -> None

               Assign this piece to a player.

               :param player_id: ID of the player to assign this piece to



            .. py:method:: can_move_to(position: P, board: Any) -> bool

               Check if this piece can move to the specified position.

               :param position: Target position to check
               :param board: The game board

               :returns: True if the piece can be moved to the position, False otherwise



            .. py:method:: get_property(key: str, default: Any = None) -> Any

               Get a property value with default if not found.



            .. py:method:: place_at(position: P) -> None

               Place this piece at the specified position.

               :param position: Position to place the piece at



            .. py:method:: set_property(key: str, value: Any) -> None

               Set a property value.



            .. py:attribute:: id
               :type:  str
               :value: None



            .. py:attribute:: name
               :type:  str | None
               :value: None



            .. py:attribute:: owner_id
               :type:  str | None
               :value: None



            .. py:attribute:: position
               :type:  P | None
               :value: None



            .. py:attribute:: properties
               :type:  dict[str, Any]
               :value: None




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: P




----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.framework.core.piece import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

