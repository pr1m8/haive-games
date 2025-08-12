
:py:mod:`games.monopoly.models`
===============================

.. py:module:: games.monopoly.models


Classes
-------

.. autoapisummary::

   games.monopoly.models.BuildingDecision
   games.monopoly.models.CardType
   games.monopoly.models.DiceRoll
   games.monopoly.models.GameEvent
   games.monopoly.models.JailDecision
   games.monopoly.models.Player
   games.monopoly.models.PlayerActionType
   games.monopoly.models.PlayerAnalysis
   games.monopoly.models.Property
   games.monopoly.models.PropertyColor
   games.monopoly.models.PropertyDecision
   games.monopoly.models.PropertyType
   games.monopoly.models.TradeOffer
   games.monopoly.models.TradeResponse


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for BuildingDecision:

   .. graphviz::
      :align: center

      digraph inheritance_BuildingDecision {
        node [shape=record];
        "BuildingDecision" [label="BuildingDecision"];
        "pydantic.BaseModel" -> "BuildingDecision";
      }

.. autopydantic_model:: games.monopoly.models.BuildingDecision
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

   Inheritance diagram for CardType:

   .. graphviz::
      :align: center

      digraph inheritance_CardType {
        node [shape=record];
        "CardType" [label="CardType"];
        "str" -> "CardType";
        "enum.Enum" -> "CardType";
      }

.. autoclass:: games.monopoly.models.CardType
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **CardType** is an Enum defined in ``games.monopoly.models``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for DiceRoll:

   .. graphviz::
      :align: center

      digraph inheritance_DiceRoll {
        node [shape=record];
        "DiceRoll" [label="DiceRoll"];
        "pydantic.BaseModel" -> "DiceRoll";
      }

.. autopydantic_model:: games.monopoly.models.DiceRoll
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

   Inheritance diagram for GameEvent:

   .. graphviz::
      :align: center

      digraph inheritance_GameEvent {
        node [shape=record];
        "GameEvent" [label="GameEvent"];
        "pydantic.BaseModel" -> "GameEvent";
      }

.. autopydantic_model:: games.monopoly.models.GameEvent
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

   Inheritance diagram for JailDecision:

   .. graphviz::
      :align: center

      digraph inheritance_JailDecision {
        node [shape=record];
        "JailDecision" [label="JailDecision"];
        "pydantic.BaseModel" -> "JailDecision";
      }

.. autopydantic_model:: games.monopoly.models.JailDecision
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

   Inheritance diagram for Player:

   .. graphviz::
      :align: center

      digraph inheritance_Player {
        node [shape=record];
        "Player" [label="Player"];
        "pydantic.BaseModel" -> "Player";
      }

.. autopydantic_model:: games.monopoly.models.Player
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

   Inheritance diagram for PlayerActionType:

   .. graphviz::
      :align: center

      digraph inheritance_PlayerActionType {
        node [shape=record];
        "PlayerActionType" [label="PlayerActionType"];
        "str" -> "PlayerActionType";
        "enum.Enum" -> "PlayerActionType";
      }

.. autoclass:: games.monopoly.models.PlayerActionType
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **PlayerActionType** is an Enum defined in ``games.monopoly.models``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for PlayerAnalysis:

   .. graphviz::
      :align: center

      digraph inheritance_PlayerAnalysis {
        node [shape=record];
        "PlayerAnalysis" [label="PlayerAnalysis"];
        "pydantic.BaseModel" -> "PlayerAnalysis";
      }

.. autopydantic_model:: games.monopoly.models.PlayerAnalysis
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

   Inheritance diagram for Property:

   .. graphviz::
      :align: center

      digraph inheritance_Property {
        node [shape=record];
        "Property" [label="Property"];
        "pydantic.BaseModel" -> "Property";
      }

.. autopydantic_model:: games.monopoly.models.Property
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

   Inheritance diagram for PropertyColor:

   .. graphviz::
      :align: center

      digraph inheritance_PropertyColor {
        node [shape=record];
        "PropertyColor" [label="PropertyColor"];
        "str" -> "PropertyColor";
        "enum.Enum" -> "PropertyColor";
      }

.. autoclass:: games.monopoly.models.PropertyColor
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **PropertyColor** is an Enum defined in ``games.monopoly.models``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for PropertyDecision:

   .. graphviz::
      :align: center

      digraph inheritance_PropertyDecision {
        node [shape=record];
        "PropertyDecision" [label="PropertyDecision"];
        "pydantic.BaseModel" -> "PropertyDecision";
      }

.. autopydantic_model:: games.monopoly.models.PropertyDecision
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

   Inheritance diagram for PropertyType:

   .. graphviz::
      :align: center

      digraph inheritance_PropertyType {
        node [shape=record];
        "PropertyType" [label="PropertyType"];
        "str" -> "PropertyType";
        "enum.Enum" -> "PropertyType";
      }

.. autoclass:: games.monopoly.models.PropertyType
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **PropertyType** is an Enum defined in ``games.monopoly.models``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for TradeOffer:

   .. graphviz::
      :align: center

      digraph inheritance_TradeOffer {
        node [shape=record];
        "TradeOffer" [label="TradeOffer"];
        "pydantic.BaseModel" -> "TradeOffer";
      }

.. autopydantic_model:: games.monopoly.models.TradeOffer
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

   Inheritance diagram for TradeResponse:

   .. graphviz::
      :align: center

      digraph inheritance_TradeResponse {
        node [shape=record];
        "TradeResponse" [label="TradeResponse"];
        "pydantic.BaseModel" -> "TradeResponse";
      }

.. autopydantic_model:: games.monopoly.models.TradeResponse
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

.. autolink-examples:: games.monopoly.models
   :collapse:
   
.. autolink-skip:: next
