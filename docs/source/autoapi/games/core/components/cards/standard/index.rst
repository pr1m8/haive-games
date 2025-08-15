games.core.components.cards.standard
====================================

.. py:module:: games.core.components.cards.standard


Classes
-------

.. autoapisummary::

   games.core.components.cards.standard.StandardCard
   games.core.components.cards.standard.StandardCardComparator
   games.core.components.cards.standard.StandardDeckFactory
   games.core.components.cards.standard.StandardRank
   games.core.components.cards.standard.StandardSuit


Module Contents
---------------

.. py:class:: StandardCard

   Bases: :py:obj:`haive.games.core.components.models.Card`


   Standard playing card.


   .. autolink-examples:: StandardCard
      :collapse:

   .. py:method:: __str__() -> str

      String representation of card.


      .. autolink-examples:: __str__
         :collapse:


   .. py:method:: format() -> str

      Format the card for display.


      .. autolink-examples:: format
         :collapse:


   .. py:method:: set_color(v, values)
      :classmethod:


      Set card color based on suit.


      .. autolink-examples:: set_color
         :collapse:


   .. py:method:: set_face_card(v, values)
      :classmethod:


      Determine if this is a face card.


      .. autolink-examples:: set_face_card
         :collapse:


   .. py:method:: set_name(v, values)
      :classmethod:


      Set default name based on rank and suit.


      .. autolink-examples:: set_name
         :collapse:


   .. py:method:: set_value(v, values)
      :classmethod:


      Auto-set value based on rank.


      .. autolink-examples:: set_value
         :collapse:


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



.. py:class:: StandardCardComparator

   Comparator for standard playing cards.


   .. autolink-examples:: StandardCardComparator
      :collapse:

   .. py:method:: compare(card1: StandardCard, card2: StandardCard, context: dict = None) -> int
      :classmethod:


      Compare two standard cards.


      .. autolink-examples:: compare
         :collapse:


   .. py:method:: sort_cards(cards: list[StandardCard], context: dict = None) -> list[StandardCard]
      :classmethod:


      Sort standard cards by rank and optionally suit.


      .. autolink-examples:: sort_cards
         :collapse:


.. py:class:: StandardDeckFactory

   Factory for creating standard card decks.


   .. autolink-examples:: StandardDeckFactory
      :collapse:

   .. py:method:: create_pinochle_deck() -> haive.games.core.components.models.Deck[StandardCard]
      :staticmethod:


      Create a pinochle deck (2 copies of 9-A).


      .. autolink-examples:: create_pinochle_deck
         :collapse:


   .. py:method:: create_standard_deck(include_jokers: bool = False) -> haive.games.core.components.models.Deck[StandardCard]
      :staticmethod:


      Create a standard 52-card deck.


      .. autolink-examples:: create_standard_deck
         :collapse:


.. py:class:: StandardRank

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Standard card ranks.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: StandardRank
      :collapse:

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



.. py:class:: StandardSuit

   Bases: :py:obj:`str`, :py:obj:`enum.Enum`


   Standard card suits.

   Initialize self.  See help(type(self)) for accurate signature.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: StandardSuit
      :collapse:

   .. py:attribute:: CLUBS
      :value: 'clubs'



   .. py:attribute:: DIAMONDS
      :value: 'diamonds'



   .. py:attribute:: HEARTS
      :value: 'hearts'



   .. py:attribute:: SPADES
      :value: 'spades'



