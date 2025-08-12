
:py:mod:`games.single_player.base`
==================================

.. py:module:: games.single_player.base

Single-player game framework for LLM-powered games.

This module provides a core framework for building single-player games where
an LLM can act as the player, the assistant, or the game engine. The framework
is designed to be flexible, extensible, and independent of any multiplayer
game concepts.

.. rubric:: Example

>>> from haive.agents.single_player import SinglePlayerGameAgent
>>> class WordleAgent(SinglePlayerGameAgent):
...     def __init__(self, config):
...         super().__init__(config)
...         self.state_manager = WordleStateManager

Typical usage:
    - Inherit from SinglePlayerGameState for game-specific state
    - Inherit from SinglePlayerStateManager for game logic
    - Inherit from SinglePlayerGameConfig for configuration
    - Inherit from SinglePlayerGameAgent for the agent implementation


.. autolink-examples:: games.single_player.base
   :collapse:

Classes
-------

.. autoapisummary::

   games.single_player.base.GameDifficulty
   games.single_player.base.GameMode
   games.single_player.base.GameSourceType
   games.single_player.base.PlayerType
   games.single_player.base.SinglePlayerGameAgent
   games.single_player.base.SinglePlayerGameConfig
   games.single_player.base.SinglePlayerGameState
   games.single_player.base.SinglePlayerStateManager


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for GameDifficulty:

   .. graphviz::
      :align: center

      digraph inheritance_GameDifficulty {
        node [shape=record];
        "GameDifficulty" [label="GameDifficulty"];
        "str" -> "GameDifficulty";
        "enum.Enum" -> "GameDifficulty";
      }

.. autoclass:: games.single_player.base.GameDifficulty
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **GameDifficulty** is an Enum defined in ``games.single_player.base``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for GameMode:

   .. graphviz::
      :align: center

      digraph inheritance_GameMode {
        node [shape=record];
        "GameMode" [label="GameMode"];
        "str" -> "GameMode";
        "enum.Enum" -> "GameMode";
      }

.. autoclass:: games.single_player.base.GameMode
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **GameMode** is an Enum defined in ``games.single_player.base``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for GameSourceType:

   .. graphviz::
      :align: center

      digraph inheritance_GameSourceType {
        node [shape=record];
        "GameSourceType" [label="GameSourceType"];
        "str" -> "GameSourceType";
        "enum.Enum" -> "GameSourceType";
      }

.. autoclass:: games.single_player.base.GameSourceType
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **GameSourceType** is an Enum defined in ``games.single_player.base``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for PlayerType:

   .. graphviz::
      :align: center

      digraph inheritance_PlayerType {
        node [shape=record];
        "PlayerType" [label="PlayerType"];
        "str" -> "PlayerType";
        "enum.Enum" -> "PlayerType";
      }

.. autoclass:: games.single_player.base.PlayerType
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **PlayerType** is an Enum defined in ``games.single_player.base``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for SinglePlayerGameAgent:

   .. graphviz::
      :align: center

      digraph inheritance_SinglePlayerGameAgent {
        node [shape=record];
        "SinglePlayerGameAgent" [label="SinglePlayerGameAgent"];
      }

.. autoclass:: games.single_player.base.SinglePlayerGameAgent
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for SinglePlayerGameConfig:

   .. graphviz::
      :align: center

      digraph inheritance_SinglePlayerGameConfig {
        node [shape=record];
        "SinglePlayerGameConfig" [label="SinglePlayerGameConfig"];
        "pydantic.BaseModel" -> "SinglePlayerGameConfig";
      }

.. autopydantic_model:: games.single_player.base.SinglePlayerGameConfig
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

   Inheritance diagram for SinglePlayerGameState:

   .. graphviz::
      :align: center

      digraph inheritance_SinglePlayerGameState {
        node [shape=record];
        "SinglePlayerGameState" [label="SinglePlayerGameState"];
        "pydantic.BaseModel" -> "SinglePlayerGameState";
      }

.. autopydantic_model:: games.single_player.base.SinglePlayerGameState
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

   Inheritance diagram for SinglePlayerStateManager:

   .. graphviz::
      :align: center

      digraph inheritance_SinglePlayerStateManager {
        node [shape=record];
        "SinglePlayerStateManager" [label="SinglePlayerStateManager"];
        "Generic[T]" -> "SinglePlayerStateManager";
      }

.. autoclass:: games.single_player.base.SinglePlayerStateManager
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: games.single_player.base
   :collapse:
   
.. autolink-skip:: next
