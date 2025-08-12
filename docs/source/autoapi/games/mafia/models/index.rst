
:py:mod:`games.mafia.models`
============================

.. py:module:: games.mafia.models

Models for the Mafia game implementation.

This module defines the core data models and enums used in the Mafia game, including:
    - Game phases (setup, night, day discussion, voting)
    - Player roles (villager, mafia, detective, doctor, narrator)
    - Action types (speak, vote, kill, investigate, save)
    - State tracking for players and game
    - Decision models for LLM output

.. rubric:: Example

>>> from mafia.models import PlayerRole, GamePhase, MafiaAction
>>>
>>> # Create a player action
>>> action = MafiaAction(
...     player_id="Player_1",
...     action_type="vote",
...     phase=GamePhase.DAY_VOTING,
...     round_number=1,
...     target_id="Player_2"
... )


.. autolink-examples:: games.mafia.models
   :collapse:

Classes
-------

.. autoapisummary::

   games.mafia.models.ActionType
   games.mafia.models.GamePhase
   games.mafia.models.MafiaAction
   games.mafia.models.MafiaPlayerDecision
   games.mafia.models.MafiaPlayerDecisionSchema
   games.mafia.models.NarratorAction
   games.mafia.models.NarratorDecision
   games.mafia.models.NarratorDecisionSchema
   games.mafia.models.PlayerRole
   games.mafia.models.PlayerState


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ActionType:

   .. graphviz::
      :align: center

      digraph inheritance_ActionType {
        node [shape=record];
        "ActionType" [label="ActionType"];
        "str" -> "ActionType";
        "enum.Enum" -> "ActionType";
      }

.. autoclass:: games.mafia.models.ActionType
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **ActionType** is an Enum defined in ``games.mafia.models``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for GamePhase:

   .. graphviz::
      :align: center

      digraph inheritance_GamePhase {
        node [shape=record];
        "GamePhase" [label="GamePhase"];
        "str" -> "GamePhase";
        "enum.Enum" -> "GamePhase";
      }

.. autoclass:: games.mafia.models.GamePhase
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **GamePhase** is an Enum defined in ``games.mafia.models``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MafiaAction:

   .. graphviz::
      :align: center

      digraph inheritance_MafiaAction {
        node [shape=record];
        "MafiaAction" [label="MafiaAction"];
        "pydantic.BaseModel" -> "MafiaAction";
      }

.. autopydantic_model:: games.mafia.models.MafiaAction
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

   Inheritance diagram for MafiaPlayerDecision:

   .. graphviz::
      :align: center

      digraph inheritance_MafiaPlayerDecision {
        node [shape=record];
        "MafiaPlayerDecision" [label="MafiaPlayerDecision"];
        "pydantic.BaseModel" -> "MafiaPlayerDecision";
      }

.. autopydantic_model:: games.mafia.models.MafiaPlayerDecision
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

   Inheritance diagram for MafiaPlayerDecisionSchema:

   .. graphviz::
      :align: center

      digraph inheritance_MafiaPlayerDecisionSchema {
        node [shape=record];
        "MafiaPlayerDecisionSchema" [label="MafiaPlayerDecisionSchema"];
        "pydantic.BaseModel" -> "MafiaPlayerDecisionSchema";
      }

.. autopydantic_model:: games.mafia.models.MafiaPlayerDecisionSchema
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

   Inheritance diagram for NarratorAction:

   .. graphviz::
      :align: center

      digraph inheritance_NarratorAction {
        node [shape=record];
        "NarratorAction" [label="NarratorAction"];
        "pydantic.BaseModel" -> "NarratorAction";
      }

.. autopydantic_model:: games.mafia.models.NarratorAction
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

   Inheritance diagram for NarratorDecision:

   .. graphviz::
      :align: center

      digraph inheritance_NarratorDecision {
        node [shape=record];
        "NarratorDecision" [label="NarratorDecision"];
        "pydantic.BaseModel" -> "NarratorDecision";
      }

.. autopydantic_model:: games.mafia.models.NarratorDecision
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

   Inheritance diagram for NarratorDecisionSchema:

   .. graphviz::
      :align: center

      digraph inheritance_NarratorDecisionSchema {
        node [shape=record];
        "NarratorDecisionSchema" [label="NarratorDecisionSchema"];
        "pydantic.BaseModel" -> "NarratorDecisionSchema";
      }

.. autopydantic_model:: games.mafia.models.NarratorDecisionSchema
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

   Inheritance diagram for PlayerRole:

   .. graphviz::
      :align: center

      digraph inheritance_PlayerRole {
        node [shape=record];
        "PlayerRole" [label="PlayerRole"];
        "str" -> "PlayerRole";
        "enum.Enum" -> "PlayerRole";
      }

.. autoclass:: games.mafia.models.PlayerRole
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **PlayerRole** is an Enum defined in ``games.mafia.models``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for PlayerState:

   .. graphviz::
      :align: center

      digraph inheritance_PlayerState {
        node [shape=record];
        "PlayerState" [label="PlayerState"];
        "pydantic.BaseModel" -> "PlayerState";
      }

.. autopydantic_model:: games.mafia.models.PlayerState
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

.. autolink-examples:: games.mafia.models
   :collapse:
   
.. autolink-skip:: next
