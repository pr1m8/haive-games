
:py:mod:`games.core.components.cards.actions`
=============================================

.. py:module:: games.core.components.cards.actions


Classes
-------

.. autoapisummary::

   games.core.components.cards.actions.ActionResult
   games.core.components.cards.actions.CardAction
   games.core.components.cards.actions.DrawCardAction
   games.core.components.cards.actions.PlayCardAction


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ActionResult:

   .. graphviz::
      :align: center

      digraph inheritance_ActionResult {
        node [shape=record];
        "ActionResult" [label="ActionResult"];
        "pydantic.BaseModel" -> "ActionResult";
      }

.. autopydantic_model:: games.core.components.cards.actions.ActionResult
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

   Inheritance diagram for CardAction:

   .. graphviz::
      :align: center

      digraph inheritance_CardAction {
        node [shape=record];
        "CardAction" [label="CardAction"];
        "pydantic.BaseModel" -> "CardAction";
        "Generic[haive.games.core.components.cards.base.TCard, haive.games.core.components.cards.base.TState]" -> "CardAction";
      }

.. autopydantic_model:: games.core.components.cards.actions.CardAction
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

   Inheritance diagram for DrawCardAction:

   .. graphviz::
      :align: center

      digraph inheritance_DrawCardAction {
        node [shape=record];
        "DrawCardAction" [label="DrawCardAction"];
        "CardAction[haive.games.core.components.cards.base.TCard, haive.games.core.components.cards.base.TState]" -> "DrawCardAction";
      }

.. autoclass:: games.core.components.cards.actions.DrawCardAction
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for PlayCardAction:

   .. graphviz::
      :align: center

      digraph inheritance_PlayCardAction {
        node [shape=record];
        "PlayCardAction" [label="PlayCardAction"];
        "CardAction[haive.games.core.components.cards.base.TCard, haive.games.core.components.cards.base.TState]" -> "PlayCardAction";
      }

.. autoclass:: games.core.components.cards.actions.PlayCardAction
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: games.core.components.cards.actions
   :collapse:
   
.. autolink-skip:: next
