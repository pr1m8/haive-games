games.core.game.containers.deck
===============================

.. py:module:: games.core.game.containers.deck

.. autoapi-nested-parse::

   Deck classes for card games in the game framework.

   This module defines the Deck container type and related classes for card games.


   .. autolink-examples:: games.core.game.containers.deck
      :collapse:


Attributes
----------

.. autoapisummary::

   games.core.game.containers.deck.C


Classes
-------

.. autoapisummary::

   games.core.game.containers.deck.Card
   games.core.game.containers.deck.Deck
   games.core.game.containers.deck.StandardPlayingCardDeck


Module Contents
---------------

.. py:class:: Card

   Bases: :py:obj:`game_framework.pieces.base.GamePiece`


   Simple Card class for illustration.


   .. autolink-examples:: Card
      :collapse:

   .. py:method:: flip() -> None

      Flip the card face up/down.


      .. autolink-examples:: flip
         :collapse:


   .. py:attribute:: face_up
      :type:  bool
      :value: False



.. py:class:: Deck

   Bases: :py:obj:`game_framework.containers.base.GamePieceContainer`\ [\ :py:obj:`C`\ ]


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


   .. py:method:: insert(card: C, position: int) -> None

      Insert a card at a specific position.

      :param card: Card to insert
      :param position: Position to insert at (0 for top, len(self.pieces) for bottom)

      :raises ValueError: If position is out of bounds


      .. autolink-examples:: insert
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


   .. py:method:: place_on_bottom(card: C) -> None

      Place a card on the bottom of the deck.

      :param card: Card to place


      .. autolink-examples:: place_on_bottom
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



.. py:class:: StandardPlayingCardDeck

   Bases: :py:obj:`Deck`


   A standard 52-card playing card deck.


   .. autolink-examples:: StandardPlayingCardDeck
      :collapse:

   .. py:class:: Rank

      Bases: :py:obj:`str`, :py:obj:`enum.Enum`


      Standard card ranks.

      Initialize self.  See help(type(self)) for accurate signature.


      .. autolink-examples:: __init__
         :collapse:


      .. autolink-examples:: Rank
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




   .. py:class:: Suit

      Bases: :py:obj:`str`, :py:obj:`enum.Enum`


      Standard card suits.

      Initialize self.  See help(type(self)) for accurate signature.


      .. autolink-examples:: __init__
         :collapse:


      .. autolink-examples:: Suit
         :collapse:

      .. py:attribute:: CLUBS
         :value: 'clubs'



      .. py:attribute:: DIAMONDS
         :value: 'diamonds'



      .. py:attribute:: HEARTS
         :value: 'hearts'



      .. py:attribute:: SPADES
         :value: 'spades'




   .. py:method:: create_standard_deck(include_jokers: bool = False) -> StandardPlayingCardDeck
      :classmethod:


      Create a standard 52-card deck.

      :param include_jokers: Whether to include jokers in the deck

      :returns: A new StandardPlayingCardDeck instance


      .. autolink-examples:: create_standard_deck
         :collapse:


.. py:data:: C

