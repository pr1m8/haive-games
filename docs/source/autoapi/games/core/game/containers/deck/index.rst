
:py:mod:`games.core.game.containers.deck`
=========================================

.. py:module:: games.core.game.containers.deck

Deck classes for card games in the game framework.

This module defines the Deck container type and related classes for card games.


.. autolink-examples:: games.core.game.containers.deck
   :collapse:

Classes
-------

.. autoapisummary::

   games.core.game.containers.deck.Card
   games.core.game.containers.deck.Deck
   games.core.game.containers.deck.StandardPlayingCardDeck


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for Card:

   .. graphviz::
      :align: center

      digraph inheritance_Card {
        node [shape=record];
        "Card" [label="Card"];
        "game_framework.pieces.base.GamePiece" -> "Card";
      }

.. autoclass:: games.core.game.containers.deck.Card
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for Deck:

   .. graphviz::
      :align: center

      digraph inheritance_Deck {
        node [shape=record];
        "Deck" [label="Deck"];
        "game_framework.containers.base.GamePieceContainer[C]" -> "Deck";
      }

.. autoclass:: games.core.game.containers.deck.Deck
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for StandardPlayingCardDeck:

   .. graphviz::
      :align: center

      digraph inheritance_StandardPlayingCardDeck {
        node [shape=record];
        "StandardPlayingCardDeck" [label="StandardPlayingCardDeck"];
        "Deck" -> "StandardPlayingCardDeck";
      }

.. autoclass:: games.core.game.containers.deck.StandardPlayingCardDeck
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: games.core.game.containers.deck
   :collapse:
   
.. autolink-skip:: next
