games.core.components.cards.base
================================

.. py:module:: games.core.components.cards.base


Attributes
----------

.. autoapisummary::

   games.core.components.cards.base.TAction
   games.core.components.cards.base.TCard
   games.core.components.cards.base.TState


Classes
-------

.. autoapisummary::

   games.core.components.cards.base.Card
   games.core.components.cards.base.CardComparator
   games.core.components.cards.base.CardContainer
   games.core.components.cards.base.Deck
   games.core.components.cards.base.Hand


Module Contents
---------------

.. py:class:: Card(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Base model for all cards.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: Card
      :collapse:

   .. py:class:: Config

      .. py:attribute:: arbitrary_types_allowed
         :value: True




   .. py:method:: __eq__(other) -> bool


   .. py:method:: __str__() -> str


   .. py:method:: flip() -> None

      Flip the card's visibility.


      .. autolink-examples:: flip
         :collapse:


   .. py:attribute:: face_up
      :type:  bool
      :value: False



   .. py:attribute:: id
      :type:  str
      :value: None



   .. py:attribute:: name
      :type:  str


   .. py:attribute:: owner_id
      :type:  str | None
      :value: None



.. py:class:: CardComparator

   Bases: :py:obj:`Protocol`, :py:obj:`Generic`\ [\ :py:obj:`TCard`\ ]


   Protocol for card comparison strategies.


   .. autolink-examples:: CardComparator
      :collapse:

   .. py:method:: compare(card1: TCard, card2: TCard, context: dict = None) -> int
      :classmethod:


      Compare two cards.


      .. autolink-examples:: compare
         :collapse:


   .. py:method:: sort_cards(cards: collections.abc.Sequence[TCard], context: dict = None) -> list[TCard]
      :classmethod:


      Sort a list of cards.


      .. autolink-examples:: sort_cards
         :collapse:


.. py:class:: CardContainer(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`, :py:obj:`Generic`\ [\ :py:obj:`TCard`\ ]


   Base model for any collection of cards.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: CardContainer
      :collapse:

   .. py:class:: Config

      .. py:attribute:: arbitrary_types_allowed
         :value: True




   .. py:method:: add(card: TCard, position: str = 'top') -> None

      Add a card to this container.


      .. autolink-examples:: add
         :collapse:


   .. py:method:: count() -> int

      Count cards in the container.


      .. autolink-examples:: count
         :collapse:


   .. py:method:: is_empty() -> bool

      Check if container is empty.


      .. autolink-examples:: is_empty
         :collapse:


   .. py:method:: of_type(card_type: type[TCard]) -> type[CardContainer[TCard]]
      :classmethod:


      Create a type-specific card container.


      .. autolink-examples:: of_type
         :collapse:


   .. py:method:: remove(card_id: str) -> TCard | None

      Remove a card by ID.


      .. autolink-examples:: remove
         :collapse:


   .. py:method:: shuffle() -> None

      Shuffle the cards.


      .. autolink-examples:: shuffle
         :collapse:


   .. py:attribute:: cards
      :type:  list[TCard]
      :value: None



   .. py:attribute:: id
      :type:  str
      :value: None



   .. py:attribute:: name
      :type:  str


.. py:class:: Deck

   Bases: :py:obj:`CardContainer`\ [\ :py:obj:`TCard`\ ]


   A deck of cards that can be drawn from.


   .. autolink-examples:: Deck
      :collapse:

   .. py:method:: draw() -> TCard | None

      Draw the top card.


      .. autolink-examples:: draw
         :collapse:


   .. py:method:: draw_many(count: int) -> list[TCard]

      Draw multiple cards.


      .. autolink-examples:: draw_many
         :collapse:


   .. py:method:: peek_top(count: int = 1) -> list[TCard]

      Look at top cards without drawing.


      .. autolink-examples:: peek_top
         :collapse:


   .. py:attribute:: face_down
      :type:  bool
      :value: True



.. py:class:: Hand

   Bases: :py:obj:`CardContainer`\ [\ :py:obj:`TCard`\ ]


   A player's hand of cards.


   .. autolink-examples:: Hand
      :collapse:

   .. py:method:: add_card(card: TCard) -> None

      Add a card to the hand.


      .. autolink-examples:: add_card
         :collapse:


   .. py:method:: play_card(card_id: str) -> TCard | None

      Play a card (remove and mark as face up).


      .. autolink-examples:: play_card
         :collapse:


   .. py:attribute:: player_id
      :type:  str


.. py:data:: TAction

.. py:data:: TCard

.. py:data:: TState

