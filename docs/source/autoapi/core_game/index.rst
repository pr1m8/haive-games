
:py:mod:`core_game`
===================

.. py:module:: core_game

Game engine for the game framework.

This module defines the base Game class that serves as the central point for game logic,
integrating all framework components.


.. autolink-examples:: core_game
   :collapse:

Classes
-------

.. autoapisummary::

   core_game.Game
   core_game.GameConfiguration
   core_game.GameFactory
   core_game.GameResult
   core_game.GameStatus
   core_game.RealTimeGame
   core_game.TurnBasedGame


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

.. autopydantic_model:: core_game.Game
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

.. autopydantic_model:: core_game.GameConfiguration
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

.. autoclass:: core_game.GameFactory
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

.. autoclass:: core_game.GameResult
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **GameResult** is an Enum defined in ``core_game``.





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

.. autoclass:: core_game.GameStatus
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **GameStatus** is an Enum defined in ``core_game``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for RealTimeGame:

   .. graphviz::
      :align: center

      digraph inheritance_RealTimeGame {
        node [shape=record];
        "RealTimeGame" [label="RealTimeGame"];
        "Game[P, T, S, C, M, PL]" -> "RealTimeGame";
      }

.. autoclass:: core_game.RealTimeGame
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

.. autoclass:: core_game.TurnBasedGame
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: core_game
   :collapse:
   
.. autolink-skip:: next
