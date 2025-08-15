games.framework.core.container
==============================

.. py:module:: games.framework.core.container


Attributes
----------

.. autoapisummary::

   games.framework.core.container.T


Classes
-------

.. autoapisummary::

   games.framework.core.container.GamePieceContainer


Module Contents
---------------

.. py:class:: GamePieceContainer(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`, :py:obj:`Generic`\ [\ :py:obj:`T`\ ]


   Base container for game pieces.

   This represents a collection of game pieces like a deck of cards, a bag of tiles, or
   a player's hand.


   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: GamePieceContainer
      :collapse:

   .. py:class:: Config

      .. py:attribute:: arbitrary_types_allowed
         :value: True




   .. py:method:: add(piece: T, position: str = 'top') -> None

      Add a piece to this container.

      :param piece: The piece to add
      :param position: Where to add the piece ("top", "bottom", or "random")


      .. autolink-examples:: add
         :collapse:


   .. py:method:: count() -> int

      Count pieces in the container.


      .. autolink-examples:: count
         :collapse:


   .. py:method:: is_empty() -> bool

      Check if container is empty.


      .. autolink-examples:: is_empty
         :collapse:


   .. py:method:: remove(piece_id: str) -> T | None

      Remove a piece by ID.

      :param piece_id: ID of the piece to remove

      :returns: The removed piece, or None if not found


      .. autolink-examples:: remove
         :collapse:


   .. py:method:: shuffle() -> None

      Shuffle the pieces in the container.


      .. autolink-examples:: shuffle
         :collapse:


   .. py:attribute:: id
      :type:  str
      :value: None



   .. py:attribute:: name
      :type:  str


   .. py:attribute:: pieces
      :type:  list[T]
      :value: None



   .. py:attribute:: properties
      :type:  dict[str, Any]
      :value: None



.. py:data:: T

