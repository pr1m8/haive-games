
:py:mod:`games.core.game.core_game`
===================================

.. py:module:: games.core.game.core_game

Game engine for the game framework.

This module defines the base Game class that serves as the central point for game logic,
integrating all framework components.


.. autolink-examples:: games.core.game.core_game
   :collapse:

Classes
-------

.. autoapisummary::

   games.core.game.core_game.Game
   games.core.game.core_game.GameConfiguration
   games.core.game.core_game.GameFactory
   games.core.game.core_game.GameResult
   games.core.game.core_game.GameStatus
   games.core.game.core_game.RealTimeGame
   games.core.game.core_game.TurnBasedGame


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for Game:

   .. graphviz::
      :align: center

      digraph inheritance_Game {
        node [shape=record];
        "Game" [label="Game"];
        "pydantic.BaseModel" -> "Game";
        "Generic[P, T, S, C, M, PL]" -> "Game";
      }

.. autopydantic_model:: games.core.game.core_game.Game
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

   Inheritance diagram for GameConfiguration:

   .. graphviz::
      :align: center

      digraph inheritance_GameConfiguration {
        node [shape=record];
        "GameConfiguration" [label="GameConfiguration"];
        "pydantic.BaseModel" -> "GameConfiguration";
      }

.. autopydantic_model:: games.core.game.core_game.GameConfiguration
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

   Inheritance diagram for GameFactory:

   .. graphviz::
      :align: center

      digraph inheritance_GameFactory {
        node [shape=record];
        "GameFactory" [label="GameFactory"];
      }

.. autoclass:: games.core.game.core_game.GameFactory
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for GameResult:

   .. graphviz::
      :align: center

      digraph inheritance_GameResult {
        node [shape=record];
        "GameResult" [label="GameResult"];
        "str" -> "GameResult";
        "enum.Enum" -> "GameResult";
      }

.. autoclass:: games.core.game.core_game.GameResult
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **GameResult** is an Enum defined in ``games.core.game.core_game``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for GameStatus:

   .. graphviz::
      :align: center

      digraph inheritance_GameStatus {
        node [shape=record];
        "GameStatus" [label="GameStatus"];
        "str" -> "GameStatus";
        "enum.Enum" -> "GameStatus";
      }

.. autoclass:: games.core.game.core_game.GameStatus
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **GameStatus** is an Enum defined in ``games.core.game.core_game``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for RealTimeGame:

   .. graphviz::
      :align: center

      digraph inheritance_RealTimeGame {
        node [shape=record];
        "RealTimeGame" [label="RealTimeGame"];
        "Game[P, T, S, C, M, PL]" -> "RealTimeGame";
      }

.. autoclass:: games.core.game.core_game.RealTimeGame
   :members:
   :undoc-members:
   :show-inheritance:




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for TurnBasedGame:

   .. graphviz::
      :align: center

      digraph inheritance_TurnBasedGame {
        node [shape=record];
        "TurnBasedGame" [label="TurnBasedGame"];
        "Game[P, T, S, C, M, PL]" -> "TurnBasedGame";
      }

.. autoclass:: games.core.game.core_game.TurnBasedGame
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: games.core.game.core_game
   :collapse:
   
.. autolink-skip:: next
