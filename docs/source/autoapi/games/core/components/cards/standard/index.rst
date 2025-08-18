games.core.components.cards.standard
====================================

.. py:module:: games.core.components.cards.standard

Module documentation for games.core.components.cards.standard


.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">5 classes</span>   </div>


      
            
            

.. admonition:: Classes (5)
   :class: note

   .. autoapisummary::

      games.core.components.cards.standard.StandardCard
      games.core.components.cards.standard.StandardCardComparator
      games.core.components.cards.standard.StandardDeckFactory
      games.core.components.cards.standard.StandardRank
      games.core.components.cards.standard.StandardSuit

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: StandardCard

            Bases: :py:obj:`haive.games.core.components.models.Card`


            Standard playing card.


            .. py:method:: __str__() -> str

               String representation of card.



            .. py:method:: format() -> str

               Format the card for display.



            .. py:method:: set_color(v, values)
               :classmethod:


               Set card color based on suit.



            .. py:method:: set_face_card(v, values)
               :classmethod:


               Determine if this is a face card.



            .. py:method:: set_name(v, values)
               :classmethod:


               Set default name based on rank and suit.



            .. py:method:: set_value(v, values)
               :classmethod:


               Auto-set value based on rank.



            .. py:attribute:: _rank_values
               :type:  ClassVar[dict[StandardRank, int]]


            .. py:attribute:: color
               :type:  str
               :value: 'black'



            .. py:attribute:: is_face_card
               :type:  bool
               :value: False



            .. py:attribute:: rank
               :type:  StandardRank


            .. py:attribute:: suit
               :type:  StandardSuit


            .. py:attribute:: value
               :type:  int
               :value: 0




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: StandardCardComparator

            Comparator for standard playing cards.


            .. py:method:: compare(card1: StandardCard, card2: StandardCard, context: dict = None) -> int
               :classmethod:


               Compare two standard cards.



            .. py:method:: sort_cards(cards: list[StandardCard], context: dict = None) -> list[StandardCard]
               :classmethod:


               Sort standard cards by rank and optionally suit.




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: StandardDeckFactory

            Factory for creating standard card decks.


            .. py:method:: create_pinochle_deck() -> haive.games.core.components.models.Deck[StandardCard]
               :staticmethod:


               Create a pinochle deck (2 copies of 9-A).



            .. py:method:: create_standard_deck(include_jokers: bool = False) -> haive.games.core.components.models.Deck[StandardCard]
               :staticmethod:


               Create a standard 52-card deck.




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: StandardRank

            Bases: :py:obj:`str`, :py:obj:`enum.Enum`


            Standard card ranks.

            Initialize self.  See help(type(self)) for accurate signature.


            .. py:attribute:: ACE
               :value: 'ace'



            .. py:attribute:: EIGHT
               :value: '8'



            .. py:attribute:: FIVE
               :value: '5'



            .. py:attribute:: FOUR
               :value: '4'



            .. py:attribute:: JACK
               :value: 'jack'



            .. py:attribute:: KING
               :value: 'king'



            .. py:attribute:: NINE
               :value: '9'



            .. py:attribute:: QUEEN
               :value: 'queen'



            .. py:attribute:: SEVEN
               :value: '7'



            .. py:attribute:: SIX
               :value: '6'



            .. py:attribute:: TEN
               :value: '10'



            .. py:attribute:: THREE
               :value: '3'



            .. py:attribute:: TWO
               :value: '2'




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: StandardSuit

            Bases: :py:obj:`str`, :py:obj:`enum.Enum`


            Standard card suits.

            Initialize self.  See help(type(self)) for accurate signature.


            .. py:attribute:: CLUBS
               :value: 'clubs'



            .. py:attribute:: DIAMONDS
               :value: 'diamonds'



            .. py:attribute:: HEARTS
               :value: 'hearts'



            .. py:attribute:: SPADES
               :value: 'spades'






----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.core.components.cards.standard import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

