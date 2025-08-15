games.framework.core.space
==========================

.. py:module:: games.framework.core.space


Attributes
----------

.. autoapisummary::

   games.framework.core.space.P
   games.framework.core.space.T


Classes
-------

.. autoapisummary::

   games.framework.core.space.Space


Module Contents
---------------

.. py:class:: Space(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`, :py:obj:`Generic`\ [\ :py:obj:`P`\ , :py:obj:`T`\ ]


   A single space on a game board that can hold a piece.

   Spaces are the fundamental units that make up a board. Each space has a position and
   can optionally contain a game piece.


   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: Space
      :collapse:

   .. py:class:: Config

      .. py:attribute:: arbitrary_types_allowed
         :value: True




   .. py:method:: is_occupied() -> bool

      Check if this space contains a piece.


      .. autolink-examples:: is_occupied
         :collapse:


   .. py:method:: place_piece(piece: T) -> bool

      Place a piece on this space.

      :param piece: The piece to place

      :returns: True if the piece was placed successfully, False otherwise


      .. autolink-examples:: place_piece
         :collapse:


   .. py:method:: remove_piece() -> T | None

      Remove the piece from this space.

      :returns: The removed piece, or None if there was no piece


      .. autolink-examples:: remove_piece
         :collapse:


   .. py:attribute:: connections
      :type:  set[str]
      :value: None



   .. py:attribute:: id
      :type:  str
      :value: None



   .. py:attribute:: name
      :type:  str | None
      :value: None



   .. py:attribute:: piece
      :type:  T | None
      :value: None



   .. py:attribute:: position
      :type:  P


   .. py:attribute:: properties
      :type:  dict[str, Any]
      :value: None



.. py:data:: P

.. py:data:: T

