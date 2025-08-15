games.framework.core.piece
==========================

.. py:module:: games.framework.core.piece


Attributes
----------

.. autoapisummary::

   games.framework.core.piece.P


Classes
-------

.. autoapisummary::

   games.framework.core.piece.GamePiece


Module Contents
---------------

.. py:class:: GamePiece(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`, :py:obj:`Generic`\ [\ :py:obj:`P`\ ]


   Base class for any game piece that can be placed on a board.

   GamePiece serves as the foundation for all movable objects in games, such as chess
   pieces, playing cards, tiles, etc.


   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: GamePiece
      :collapse:

   .. py:class:: Config

      .. py:attribute:: arbitrary_types_allowed
         :value: True




   .. py:method:: assign_to_player(player_id: str) -> None

      Assign this piece to a player.

      :param player_id: ID of the player to assign this piece to


      .. autolink-examples:: assign_to_player
         :collapse:


   .. py:method:: can_move_to(position: P, board: Any) -> bool

      Check if this piece can move to the specified position.

      :param position: Target position to check
      :param board: The game board

      :returns: True if the piece can be moved to the position, False otherwise


      .. autolink-examples:: can_move_to
         :collapse:


   .. py:method:: get_property(key: str, default: Any = None) -> Any

      Get a property value with default if not found.


      .. autolink-examples:: get_property
         :collapse:


   .. py:method:: place_at(position: P) -> None

      Place this piece at the specified position.

      :param position: Position to place the piece at


      .. autolink-examples:: place_at
         :collapse:


   .. py:method:: set_property(key: str, value: Any) -> None

      Set a property value.


      .. autolink-examples:: set_property
         :collapse:


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



.. py:data:: P

