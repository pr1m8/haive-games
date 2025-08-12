
:py:mod:`games.cards.standard.bs.models`
========================================

.. py:module:: games.cards.standard.bs.models


Classes
-------

.. autoapisummary::

   games.cards.standard.bs.models.Card
   games.cards.standard.bs.models.CardSuit
   games.cards.standard.bs.models.ChallengeAction
   games.cards.standard.bs.models.PlayerClaimAction
   games.cards.standard.bs.models.PlayerState


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

.. autopydantic_model:: games.cards.standard.bs.models.Card
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

   Inheritance diagram for CardSuit:

   .. graphviz::
      :align: center

      digraph inheritance_CardSuit {
        node [shape=record];
        "CardSuit" [label="CardSuit"];
        "str" -> "CardSuit";
        "enum.Enum" -> "CardSuit";
      }

.. autoclass:: games.cards.standard.bs.models.CardSuit
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **CardSuit** is an Enum defined in ``games.cards.standard.bs.models``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ChallengeAction:

   .. graphviz::
      :align: center

      digraph inheritance_ChallengeAction {
        node [shape=record];
        "ChallengeAction" [label="ChallengeAction"];
        "pydantic.BaseModel" -> "ChallengeAction";
      }

.. autopydantic_model:: games.cards.standard.bs.models.ChallengeAction
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

   Inheritance diagram for PlayerClaimAction:

   .. graphviz::
      :align: center

      digraph inheritance_PlayerClaimAction {
        node [shape=record];
        "PlayerClaimAction" [label="PlayerClaimAction"];
        "pydantic.BaseModel" -> "PlayerClaimAction";
      }

.. autopydantic_model:: games.cards.standard.bs.models.PlayerClaimAction
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

   Inheritance diagram for PlayerState:

   .. graphviz::
      :align: center

      digraph inheritance_PlayerState {
        node [shape=record];
        "PlayerState" [label="PlayerState"];
        "pydantic.BaseModel" -> "PlayerState";
      }

.. autopydantic_model:: games.cards.standard.bs.models.PlayerState
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





.. rubric:: Related Links

.. autolink-examples:: games.cards.standard.bs.models
   :collapse:
   
.. autolink-skip:: next
