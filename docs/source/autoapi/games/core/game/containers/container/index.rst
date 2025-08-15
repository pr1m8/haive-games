games.core.game.containers.container
====================================

.. py:module:: games.core.game.containers.container


Attributes
----------

.. autoapisummary::

   games.core.game.containers.container.T


Classes
-------

.. autoapisummary::

   games.core.game.containers.container.Deck
   games.core.game.containers.container.GamePieceContainer
   games.core.game.containers.container.PlayerHand
   games.core.game.containers.container.TileBag


Module Contents
---------------

.. py:class:: Deck

   Bases: :py:obj:`GamePieceContainer`\ [\ :py:obj:`Card`\ ]


   A deck of cards.


   .. autolink-examples:: Deck
      :collapse:

   .. py:method:: create_standard_deck() -> Deck
      :classmethod:


      Create a standard 52-card deck.


      .. autolink-examples:: create_standard_deck
         :collapse:


   .. py:method:: deal(num_players: int, cards_per_player: int) -> list[list[Card]]

      Deal cards to multiple players.


      .. autolink-examples:: deal
         :collapse:


   .. py:method:: draw() -> Card | None

      Draw the top card.


      .. autolink-examples:: draw
         :collapse:


   .. py:attribute:: face_down
      :type:  bool
      :value: True



.. py:class:: GamePieceContainer(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`, :py:obj:`Generic`\ [\ :py:obj:`T`\ ]


   Base container for game pieces.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: GamePieceContainer
      :collapse:

   .. py:method:: add(piece: T, position: str = 'top') -> None

      Add a piece to this container.


      .. autolink-examples:: add
         :collapse:


   .. py:method:: count() -> int

      Count pieces in the container.


      .. autolink-examples:: count
         :collapse:


   .. py:method:: draw() -> T | None

      Draw the top piece.


      .. autolink-examples:: draw
         :collapse:


   .. py:method:: draw_many(count: int) -> list[T]

      Draw multiple pieces.


      .. autolink-examples:: draw_many
         :collapse:


   .. py:method:: filter(predicate: collections.abc.Callable[[T], bool]) -> list[T]

      Filter pieces by predicate.


      .. autolink-examples:: filter
         :collapse:


   .. py:method:: find(predicate: collections.abc.Callable[[T], bool]) -> T | None

      Find a piece matching the predicate.


      .. autolink-examples:: find
         :collapse:


   .. py:method:: is_empty() -> bool

      Check if container is empty.


      .. autolink-examples:: is_empty
         :collapse:


   .. py:method:: peek(count: int = 1) -> list[T]

      Look at the top pieces without removing them.


      .. autolink-examples:: peek
         :collapse:


   .. py:method:: remove(piece_id: str) -> T | None

      Remove a piece by ID.


      .. autolink-examples:: remove
         :collapse:


   .. py:method:: shuffle() -> None

      Shuffle the pieces.


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



.. py:class:: PlayerHand

   Bases: :py:obj:`GamePieceContainer`\ [\ :py:obj:`T`\ ]


   A player's hand of pieces.


   .. autolink-examples:: PlayerHand
      :collapse:

   .. py:method:: add_piece(piece: T) -> None

      Add a piece to the hand and assign ownership.


      .. autolink-examples:: add_piece
         :collapse:


   .. py:method:: can_play(piece_id: str, position: Position, board: Board) -> bool

      Check if a piece can be played at the given position.


      .. autolink-examples:: can_play
         :collapse:


   .. py:method:: play_piece(piece_id: str) -> T | None

      Play a piece (remove from hand).


      .. autolink-examples:: play_piece
         :collapse:


   .. py:attribute:: player_id
      :type:  str


.. py:class:: TileBag

   Bases: :py:obj:`GamePieceContainer`\ [\ :py:obj:`Tile`\ ]


   A bag of tiles (Scrabble, Mahjong).


   .. autolink-examples:: TileBag
      :collapse:

   .. py:method:: draw_many_random(count: int) -> list[Tile]

      Draw multiple random tiles.


      .. autolink-examples:: draw_many_random
         :collapse:


   .. py:method:: draw_random() -> Tile | None

      Draw a random tile from the bag.


      .. autolink-examples:: draw_random
         :collapse:


.. py:data:: T

