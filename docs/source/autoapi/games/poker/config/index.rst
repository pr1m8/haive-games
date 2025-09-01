games.poker.config
==================

.. py:module:: games.poker.config

.. autoapi-nested-parse::

   Configuration module for the Poker agent.

   This module provides configuration classes and utilities for setting up
   poker game agents, including:
       - Game settings (blinds, starting chips, max hands)
       - Player configurations and names
       - LLM engine configurations
       - State management settings
       - Game history and analysis options

   The module supports multiple LLM providers and allows customization of
   game parameters through a Pydantic-based configuration system.

   .. rubric:: Example

   >>> from poker.config import PokerAgentConfig
   >>>
   >>> # Create default config for 6 players
   >>> config = PokerAgentConfig.default_config(
   ...     player_names=["P1", "P2", "P3", "P4", "P5", "P6"],
   ...     starting_chips=2000,
   ...     small_blind=10,
   ...     big_blind=20
   ... )



Classes
-------

.. toctree::
   :hidden:

   /autoapi/games/poker/config/PokerAgentConfig

.. autoapisummary::

   games.poker.config.PokerAgentConfig


