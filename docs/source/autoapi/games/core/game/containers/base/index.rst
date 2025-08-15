games.core.game.containers.base
===============================

.. py:module:: games.core.game.containers.base

.. autoapi-nested-parse::

   Container models for game pieces in the game framework.

   This module defines containers for game pieces like decks of cards, bags of tiles, and
   player hands.


   .. autolink-examples:: games.core.game.containers.base
      :collapse:


Attributes
----------

.. autoapisummary::

   games.core.game.containers.base.C
   games.core.game.containers.base.T


Classes
-------

.. autoapisummary::

   games.core.game.containers.base.Deck
   games.core.game.containers.base.GamePieceContainer
   games.core.game.containers.base.PlayerHand


Module Contents
---------------

.. py:class:: Deck

   Bases: :py:obj:`GamePieceContainer`\ [\ :py:obj:`C`\ ]


   A deck of cards.

   This represents a collection of cards that can be drawn, shuffled, and dealt.



   .. autolink-examples:: Deck
      :collapse:

   .. py:method:: deal(num_players: int, cards_per_player: int) -> list[list[C]]

      Deal cards to multiple players.

      :param num_players: Number of players to deal to
      :param cards_per_player: Number of cards per player

      :returns: List of lists, where each inner list contains a player's cards


      .. autolink-examples:: deal
         :collapse:


   .. py:method:: discard(card: C) -> None

      Add a card to the discard pile.

      :param card: Card to discard


      .. autolink-examples:: discard
         :collapse:


   .. py:method:: draw() -> C | None

      Draw the top card and set its face up/down based on deck configuration.

      :returns: The drawn card, or None if deck is empty


      .. autolink-examples:: draw
         :collapse:


   .. py:method:: draw_bottom() -> C | None

      Draw the bottom card.

      :returns: The bottom card, or None if deck is empty


      .. autolink-examples:: draw_bottom
         :collapse:


   .. py:method:: peek_bottom(count: int = 1) -> list[C]

      Look at bottom cards without drawing.

      :param count: Number of cards to peek at

      :returns: List of cards from the bottom


      .. autolink-examples:: peek_bottom
         :collapse:


   .. py:method:: peek_top(count: int = 1) -> list[C]

      Look at top cards without drawing.

      :param count: Number of cards to peek at

      :returns: List of cards from the top


      .. autolink-examples:: peek_top
         :collapse:


   .. py:method:: recycle_discards(shuffle: bool = True) -> None

      Move all cards from discard pile back into the deck.

      :param shuffle: Whether to shuffle the deck after recycling


      .. autolink-examples:: recycle_discards
         :collapse:


   .. py:attribute:: discard_pile
      :type:  list[C]
      :value: None



   .. py:attribute:: face_down
      :type:  bool
      :value: True



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

      :raises ValueError: If position is not valid


      .. autolink-examples:: add
         :collapse:


   .. py:method:: clear() -> None

      Remove all pieces from the container.


      .. autolink-examples:: clear
         :collapse:


   .. py:method:: count() -> int

      Count pieces in the container.

      :returns: Number of pieces in the container


      .. autolink-examples:: count
         :collapse:


   .. py:method:: draw() -> T | None

      Draw the top piece.

      :returns: The top piece, or None if container is empty


      .. autolink-examples:: draw
         :collapse:


   .. py:method:: draw_many(count: int) -> list[T]

      Draw multiple pieces from the top.

      :param count: Number of pieces to draw

      :returns: List of drawn pieces


      .. autolink-examples:: draw_many
         :collapse:


   .. py:method:: filter(predicate: collections.abc.Callable[[T], bool]) -> list[T]

      Filter pieces by predicate.

      :param predicate: Function that returns True for pieces to include

      :returns: List of pieces matching the predicate


      .. autolink-examples:: filter
         :collapse:


   .. py:method:: find(predicate: collections.abc.Callable[[T], bool]) -> T | None

      Find a piece matching the predicate.

      :param predicate: Function that returns True for the desired piece

      :returns: The first matching piece, or None if not found


      .. autolink-examples:: find
         :collapse:


   .. py:method:: get_property(key: str, default: Any = None) -> Any

      Get a container property.

      :param key: Property name
      :param default: Default value if property doesn't exist

      :returns: Property value or default


      .. autolink-examples:: get_property
         :collapse:


   .. py:method:: is_empty() -> bool

      Check if container is empty.

      :returns: True if the container is empty, False otherwise


      .. autolink-examples:: is_empty
         :collapse:


   .. py:method:: peek(count: int = 1) -> list[T]

      Look at the top pieces without removing them.

      :param count: Number of pieces to peek at

      :returns: List of pieces from the top


      .. autolink-examples:: peek
         :collapse:


   .. py:method:: remove(piece_id: str) -> T | None

      Remove a piece by ID.

      :param piece_id: ID of the piece to remove

      :returns: The removed piece, or None if not found


      .. autolink-examples:: remove
         :collapse:


   .. py:method:: set_property(key: str, value: Any) -> None

      Set a container property.

      :param key: Property name
      :param value: Property value


      .. autolink-examples:: set_property
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



.. py:class:: PlayerHand

   Bases: :py:obj:`GamePieceContainer`\ [\ :py:obj:`T`\ ]


   A player's hand of pieces.

   This represents the collection of pieces a player holds, such as cards in a card
   game or tiles in Scrabble.



   .. autolink-examples:: PlayerHand
      :collapse:

   .. py:method:: add_piece(piece: T) -> None

      Add a piece to the hand and assign ownership to the player.

      :param piece: The piece to add


      .. autolink-examples:: add_piece
         :collapse:


   .. py:method:: play_piece(piece_id: str) -> T | None

      Play a piece (remove from hand).

      :param piece_id: ID of the piece to play

      :returns: The played piece, or None if not found


      .. autolink-examples:: play_piece
         :collapse:


   .. py:method:: play_pieces(piece_ids: list[str]) -> list[T]

      Play multiple pieces.

      :param piece_ids: List of piece IDs to play

      :returns: List of played pieces


      .. autolink-examples:: play_pieces
         :collapse:


   .. py:attribute:: player_id
      :type:  str


.. py:data:: C

.. py:data:: T

