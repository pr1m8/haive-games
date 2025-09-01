games.base.config
=================

.. py:module:: games.base.config

.. autoapi-nested-parse::

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



Classes
-------

.. toctree::
   :hidden:

   /autoapi/games/base/config/GameConfig

.. autoapisummary::

   games.base.config.GameConfig


