games.core.components.cards.base
================================

.. py:module:: games.core.components.cards.base

Module documentation for games.core.components.cards.base


.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">5 classes</span> • <span class="module-stat">3 attributes</span>   </div>


      

.. admonition:: Attributes (3)
   :class: tip

   .. autoapisummary::

      games.core.components.cards.base.TAction
      games.core.components.cards.base.TCard
      games.core.components.cards.base.TState

            
            

.. admonition:: Classes (5)
   :class: note

   .. autoapisummary::

      games.core.components.cards.base.Card
      games.core.components.cards.base.CardComparator
      games.core.components.cards.base.CardContainer
      games.core.components.cards.base.Deck
      games.core.components.cards.base.Hand

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: Card(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            Base model for all cards.

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:class:: Config

               .. py:attribute:: arbitrary_types_allowed
                  :value: True




            .. py:method:: __eq__(other) -> bool


            .. py:method:: __str__() -> str


            .. py:method:: flip() -> None

               Flip the card's visibility.



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




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: CardComparator

            Bases: :py:obj:`Protocol`, :py:obj:`Generic`\ [\ :py:obj:`TCard`\ ]


            Protocol for card comparison strategies.


            .. py:method:: compare(card1: TCard, card2: TCard, context: dict = None) -> int
               :classmethod:


               Compare two cards.



            .. py:method:: sort_cards(cards: collections.abc.Sequence[TCard], context: dict = None) -> list[TCard]
               :classmethod:


               Sort a list of cards.




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: CardContainer(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`, :py:obj:`Generic`\ [\ :py:obj:`TCard`\ ]


            Base model for any collection of cards.

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:class:: Config

               .. py:attribute:: arbitrary_types_allowed
                  :value: True




            .. py:method:: add(card: TCard, position: str = 'top') -> None

               Add a card to this container.



            .. py:method:: count() -> int

               Count cards in the container.



            .. py:method:: is_empty() -> bool

               Check if container is empty.



            .. py:method:: of_type(card_type: type[TCard]) -> type[CardContainer[TCard]]
               :classmethod:


               Create a type-specific card container.



            .. py:method:: remove(card_id: str) -> TCard | None

               Remove a card by ID.



            .. py:method:: shuffle() -> None

               Shuffle the cards.



            .. py:attribute:: cards
               :type:  list[TCard]
               :value: None



            .. py:attribute:: id
               :type:  str
               :value: None



            .. py:attribute:: name
               :type:  str



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: Deck

            Bases: :py:obj:`CardContainer`\ [\ :py:obj:`TCard`\ ]


            A deck of cards that can be drawn from.


            .. py:method:: draw() -> TCard | None

               Draw the top card.



            .. py:method:: draw_many(count: int) -> list[TCard]

               Draw multiple cards.



            .. py:method:: peek_top(count: int = 1) -> list[TCard]

               Look at top cards without drawing.



            .. py:attribute:: face_down
               :type:  bool
               :value: True




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: Hand

            Bases: :py:obj:`CardContainer`\ [\ :py:obj:`TCard`\ ]


            A player's hand of cards.


            .. py:method:: add_card(card: TCard) -> None

               Add a card to the hand.



            .. py:method:: play_card(card_id: str) -> TCard | None

               Play a card (remove and mark as face up).



            .. py:attribute:: player_id
               :type:  str



      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: TAction


      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: TCard


      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:data:: TState




----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.core.components.cards.base import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

