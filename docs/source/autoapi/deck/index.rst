deck
====

.. py:module:: deck


Attributes
----------

.. autoapisummary::

   deck.C


Classes
-------

.. autoapisummary::

   deck.Deck


Module Contents
---------------

.. py:class:: Deck

   Bases: :py:obj:`haive.games.framework.core.container.GamePieceContainer`\ [\ :py:obj:`C`\ ]


   A deck of cards.

   This represents a collection of cards that can be drawn, shuffled, and dealt.



   .. autolink-examples:: Deck
      :collapse:

   .. py:method:: create_standard_deck() -> Deck[haive.games.framework.pieces.card.PlayingCard]
      :classmethod:


      Create a standard 52-card deck.

      :returns: A new deck with standard playing cards


      .. autolink-examples:: create_standard_deck
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


   .. py:method:: draw_many(count: int) -> list[C]

      Draw multiple cards from the top.

      :param count: Number of cards to draw

      :returns: List of drawn cards


      .. autolink-examples:: draw_many
         :collapse:


   .. py:attribute:: discard_pile
      :type:  list[C]
      :value: None



   .. py:attribute:: face_down
      :type:  bool
      :value: True



.. py:data:: C

