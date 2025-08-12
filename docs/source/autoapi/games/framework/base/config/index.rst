
:py:mod:`games.framework.base.config`
=====================================

.. py:module:: games.framework.base.config

Base configuration module for game agents.

This module provides the foundational configuration class for game agents,
defining common settings and parameters that all game agents need.

.. rubric:: Example

>>> config = GameConfig(
...     state_schema=ChessState,
...     engines={"player1": player1_engine},
...     enable_analysis=True
... )

Typical usage:
    - Inherit from GameConfig to create game-specific configurations
    - Override default values to customize game behavior
    - Use as configuration for game agents


.. autolink-examples:: games.framework.base.config
   :collapse:

Classes
-------

.. autoapisummary::

   games.framework.base.config.GameConfig


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for GameConfig:

   .. graphviz::
      :align: center

      digraph inheritance_GameConfig {
        node [shape=record];
        "GameConfig" [label="GameConfig"];
        "haive.core.engine.agent.agent.AgentConfig" -> "GameConfig";
      }

.. autoclass:: games.framework.base.config.GameConfig
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: games.framework.base.config
   :collapse:
   
.. autolink-skip:: next
