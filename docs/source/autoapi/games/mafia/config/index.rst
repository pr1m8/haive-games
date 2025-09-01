games.mafia.config
==================

.. py:module:: games.mafia.config

.. autoapi-nested-parse::

   Configuration for the Mafia game agent.

   This module provides configuration classes and utilities for the Mafia game
   agent, including:
       - Game settings (max days, discussion rounds)
       - LLM engine configurations
       - Role mappings and assignments
       - Debug settings

   .. rubric:: Example

   >>> from mafia.config import MafiaAgentConfig
   >>>
   >>> # Create a default configuration for 7 players
   >>> config = MafiaAgentConfig.default_config(
   ...     player_count=7,
   ...     max_days=3
   ... )
   >>> print(config.max_days)  # Shows 3



Classes
-------

.. toctree::
   :hidden:

   /autoapi/games/mafia/config/MafiaAgentConfig

.. autoapisummary::

   games.mafia.config.MafiaAgentConfig


