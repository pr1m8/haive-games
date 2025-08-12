
:py:mod:`games.cards.standard.poker.scoring`
============================================

.. py:module:: games.cards.standard.poker.scoring


Classes
-------

.. autoapisummary::

   games.cards.standard.poker.scoring.PokerHandEvaluator
   games.cards.standard.poker.scoring.PokerHandRank
   games.cards.standard.poker.scoring.PokerHandType


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for PokerHandEvaluator:

   .. graphviz::
      :align: center

      digraph inheritance_PokerHandEvaluator {
        node [shape=record];
        "PokerHandEvaluator" [label="PokerHandEvaluator"];
        "haive.games.cards.card.components.scoring.HandEvaluator[haive.games.cards.card.components.standard.StandardCard]" -> "PokerHandEvaluator";
      }

.. autoclass:: games.cards.standard.poker.scoring.PokerHandEvaluator
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for PokerHandRank:

   .. graphviz::
      :align: center

      digraph inheritance_PokerHandRank {
        node [shape=record];
        "PokerHandRank" [label="PokerHandRank"];
        "haive.games.cards.card.components.scoring.HandRank[haive.games.cards.card.components.standard.StandardCard]" -> "PokerHandRank";
      }

.. autoclass:: games.cards.standard.poker.scoring.PokerHandRank
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for PokerHandType:

   .. graphviz::
      :align: center

      digraph inheritance_PokerHandType {
        node [shape=record];
        "PokerHandType" [label="PokerHandType"];
        "enum.IntEnum" -> "PokerHandType";
      }

.. autoclass:: games.cards.standard.poker.scoring.PokerHandType
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **PokerHandType** is an Enum defined in ``games.cards.standard.poker.scoring``.





.. rubric:: Related Links

.. autolink-examples:: games.cards.standard.poker.scoring
   :collapse:
   
.. autolink-skip:: next
