games.cards.models.card
=======================

.. py:module:: games.cards.models.card

.. autoapi-nested-parse::

   Card representation and operations for card games.

   This module provides classes for representing playing cards, including ranks,
   suits, and card values. It's designed to be used in various card game implementations
   with consistent handling of card comparisons and representations.

   .. rubric:: Example

   >>> from haive.games.cards.models.card import Card, Rank, Suit
   >>> card = Card(Rank.ACE, Suit.SPADES)
   >>> print(card)
   A`
   >>> card.value
   14


   .. autolink-examples:: games.cards.models.card
      :collapse:


Classes
-------

.. autoapisummary::

   games.cards.models.card.Card
   games.cards.models.card.Rank
   games.cards.models.card.Suit


Module Contents
---------------

.. py:class:: Card(rank: Rank, suit: Suit)

   A playing card with rank and suit.

   Represents a standard playing card with rank and suit, providing methods
   for comparison, display, and game-specific value calculations.

   .. attribute:: rank

      The rank of the card (2-10, J, Q, K, A, Joker).

   .. attribute:: suit

      The suit of the card (clubs, diamonds, hearts, spades, joker).

   .. attribute:: value

      The numeric value of the card for comparisons.

   .. rubric:: Examples

   >>> card = Card(Rank.ACE, Suit.SPADES)
   >>> print(card)
   A`
   >>> card.value
   14
   >>> card.long_name
   'Ace of Spades'

   Initialize a card with rank and suit.

   :param rank: The rank of the card.
   :param suit: The suit of the card.

   :raises ValueError: If a standard card is created with Joker suit but not Joker rank.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: Card
      :collapse:

   .. py:method:: __eq__(other: object) -> bool

      Check if two cards are equal.

      :param other: Another card to compare with.

      :returns: True if the cards have the same rank and suit, False otherwise.


      .. autolink-examples:: __eq__
         :collapse:


   .. py:method:: __gt__(other: Card) -> bool

      Check if this card has a higher value than another.

      :param other: Another card to compare with.

      :returns: True if this card's value is greater than the other card's value.


      .. autolink-examples:: __gt__
         :collapse:


   .. py:method:: __lt__(other: Card) -> bool

      Check if this card has a lower value than another.

      :param other: Another card to compare with.

      :returns: True if this card's value is less than the other card's value.


      .. autolink-examples:: __lt__
         :collapse:


   .. py:method:: __repr__() -> str

      Return a detailed representation of the card.

      :returns: A string representation for debugging.


      .. autolink-examples:: __repr__
         :collapse:


   .. py:method:: __str__() -> str

      Return a string representation of the card.

      :returns: A string with rank and suit symbols.


      .. autolink-examples:: __str__
         :collapse:


   .. py:method:: blackjack_value() -> int

      Calculate the value of the card in Blackjack.

      Aces are worth 11 by default (caller should handle alternate values).
      Face cards (J, Q, K) are worth 10.

      :returns: The card's value in Blackjack.


      .. autolink-examples:: blackjack_value
         :collapse:


   .. py:method:: from_string(card_str: str) -> Card
      :classmethod:


      Create a card from a string representation.

      :param card_str: A string like "AH" (Ace of Hearts) or "10S" (Ten of Spades).

      :returns: A new Card instance.

      :raises ValueError: If the string format is invalid.


      .. autolink-examples:: from_string
         :collapse:


   .. py:method:: is_face_card() -> bool

      Check if the card is a face card (Jack, Queen, or King).

      :returns: True if the card is a face card, False otherwise.


      .. autolink-examples:: is_face_card
         :collapse:


   .. py:property:: long_name
      :type: str


      Get the full name of the card.

      :returns: A string with the full name (e.g., "Ace of Spades").

      .. autolink-examples:: long_name
         :collapse:


   .. py:attribute:: rank


   .. py:attribute:: suit


   .. py:attribute:: value


.. py:class:: Rank(*args, **kwds)

   Bases: :py:obj:`enum.Enum`


   Playing card ranks.

   Standard card ranks for a 52-card deck, with values that facilitate numeric
   comparisons between cards.



   .. autolink-examples:: Rank
      :collapse:

   .. py:method:: __str__() -> str

      Return a string representation of the rank.

      :returns: A string representation suitable for display.


      .. autolink-examples:: __str__
         :collapse:


   .. py:attribute:: ACE
      :value: 14



   .. py:attribute:: EIGHT
      :value: 8



   .. py:attribute:: FIVE
      :value: 5



   .. py:attribute:: FOUR
      :value: 4



   .. py:attribute:: JACK
      :value: 11



   .. py:attribute:: JOKER
      :value: 15



   .. py:attribute:: KING
      :value: 13



   .. py:attribute:: NINE
      :value: 9



   .. py:attribute:: QUEEN
      :value: 12



   .. py:attribute:: SEVEN
      :value: 7



   .. py:attribute:: SIX
      :value: 6



   .. py:attribute:: TEN
      :value: 10



   .. py:attribute:: THREE
      :value: 3



   .. py:attribute:: TWO
      :value: 2



.. py:class:: Suit(*args, **kwds)

   Bases: :py:obj:`enum.Enum`


   Playing card suits.

   Standard card suits for a 52-card deck, with optional support for additional special
   suits in non-standard decks.



   .. autolink-examples:: Suit
      :collapse:

   .. py:method:: __str__() -> str

      Return the Unicode symbol for the suit.

      :returns: The Unicode character representing the suit.


      .. autolink-examples:: __str__
         :collapse:


   .. py:attribute:: CLUBS


   .. py:attribute:: DIAMONDS


   .. py:attribute:: HEARTS


   .. py:attribute:: JOKER


   .. py:attribute:: SPADES


   .. py:property:: color
      :type: str


      Get the color of the suit (red or black).

      :returns: "red" or "black".
      :rtype: The color as a string

      .. autolink-examples:: color
         :collapse:


