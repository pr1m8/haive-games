
:py:mod:`games.core.components.cards.turns`
===========================================

.. py:module:: games.core.components.cards.turns


Classes
-------

.. autoapisummary::

   games.core.components.cards.turns.CardGameTurn
   games.core.components.cards.turns.TurnManager
   games.core.components.cards.turns.TurnPhase


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for CardGameTurn:

   .. graphviz::
      :align: center

      digraph inheritance_CardGameTurn {
        node [shape=record];
        "CardGameTurn" [label="CardGameTurn"];
        "pydantic.BaseModel" -> "CardGameTurn";
        "Generic[haive.games.core.components.models.TCard, haive.games.core.components.actions.TAction, haive.games.core.components.models.TState]" -> "CardGameTurn";
      }

.. autopydantic_model:: games.core.components.cards.turns.CardGameTurn
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

   Inheritance diagram for TurnManager:

   .. graphviz::
      :align: center

      digraph inheritance_TurnManager {
        node [shape=record];
        "TurnManager" [label="TurnManager"];
        "pydantic.BaseModel" -> "TurnManager";
        "Generic[haive.games.core.components.models.TCard, haive.games.core.components.actions.TAction, haive.games.core.components.models.TState]" -> "TurnManager";
      }

.. autopydantic_model:: games.core.components.cards.turns.TurnManager
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

   Inheritance diagram for TurnPhase:

   .. graphviz::
      :align: center

      digraph inheritance_TurnPhase {
        node [shape=record];
        "TurnPhase" [label="TurnPhase"];
        "str" -> "TurnPhase";
        "enum.Enum" -> "TurnPhase";
      }

.. autoclass:: games.core.components.cards.turns.TurnPhase
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **TurnPhase** is an Enum defined in ``games.core.components.cards.turns``.





.. rubric:: Related Links

.. autolink-examples:: games.core.components.cards.turns
   :collapse:
   
.. autolink-skip:: next
