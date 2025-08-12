
:py:mod:`games.core.components.cards.base`
==========================================

.. py:module:: games.core.components.cards.base


Classes
-------

.. autoapisummary::

   games.core.components.cards.base.Card
   games.core.components.cards.base.CardComparator
   games.core.components.cards.base.CardContainer
   games.core.components.cards.base.Deck
   games.core.components.cards.base.Hand


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for Card:

   .. graphviz::
      :align: center

      digraph inheritance_Card {
        node [shape=record];
        "Card" [label="Card"];
        "pydantic.BaseModel" -> "Card";
      }

.. autopydantic_model:: games.core.components.cards.base.Card
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for CardComparator:

   .. graphviz::
      :align: center

      digraph inheritance_CardComparator {
        node [shape=record];
        "CardComparator" [label="CardComparator"];
        "Protocol" -> "CardComparator";
        "Generic[TCard]" -> "CardComparator";
      }

.. autoclass:: games.core.components.cards.base.CardComparator
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for CardContainer:

   .. graphviz::
      :align: center

      digraph inheritance_CardContainer {
        node [shape=record];
        "CardContainer" [label="CardContainer"];
        "pydantic.BaseModel" -> "CardContainer";
        "Generic[TCard]" -> "CardContainer";
      }

.. autopydantic_model:: games.core.components.cards.base.CardContainer
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for Deck:

   .. graphviz::
      :align: center

      digraph inheritance_Deck {
        node [shape=record];
        "Deck" [label="Deck"];
        "CardContainer[TCard]" -> "Deck";
      }

.. autoclass:: games.core.components.cards.base.Deck
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for Hand:

   .. graphviz::
      :align: center

      digraph inheritance_Hand {
        node [shape=record];
        "Hand" [label="Hand"];
        "CardContainer[TCard]" -> "Hand";
      }

.. autoclass:: games.core.components.cards.base.Hand
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: games.core.components.cards.base
   :collapse:
   
.. autolink-skip:: next
