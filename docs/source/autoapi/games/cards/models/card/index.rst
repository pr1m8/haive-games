
:py:mod:`games.cards.models.card`
=================================

.. py:module:: games.cards.models.card

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




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for Card:

   .. graphviz::
      :align: center

      digraph inheritance_Card {
        node [shape=record];
        "Card" [label="Card"];
      }

.. autoclass:: games.cards.models.card.Card
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for Rank:

   .. graphviz::
      :align: center

      digraph inheritance_Rank {
        node [shape=record];
        "Rank" [label="Rank"];
        "enum.Enum" -> "Rank";
      }

.. autoclass:: games.cards.models.card.Rank
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **Rank** is an Enum defined in ``games.cards.models.card``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for Suit:

   .. graphviz::
      :align: center

      digraph inheritance_Suit {
        node [shape=record];
        "Suit" [label="Suit"];
        "enum.Enum" -> "Suit";
      }

.. autoclass:: games.cards.models.card.Suit
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **Suit** is an Enum defined in ``games.cards.models.card``.





.. rubric:: Related Links

.. autolink-examples:: games.cards.models.card
   :collapse:
   
.. autolink-skip:: next
