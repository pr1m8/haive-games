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



Classes
-------

.. toctree::
   :hidden:

   /autoapi/games/cards/models/card/Card
   /autoapi/games/cards/models/card/Rank
   /autoapi/games/cards/models/card/Suit

.. autoapisummary::

   games.cards.models.card.Card
   games.cards.models.card.Rank
   games.cards.models.card.Suit


