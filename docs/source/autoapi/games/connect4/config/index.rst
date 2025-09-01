games.connect4.config
=====================

.. py:module:: games.connect4.config

.. autoapi-nested-parse::

   Connect4 agent configuration module.

   This module provides configuration classes for the Connect4 game agent, including:
       - Base configuration for Connect4 agents
       - LLM configuration for players and analyzers
       - Game settings and visualization options

   .. rubric:: Example

   >>> from haive.games.connect4 import Connect4AgentConfig
   >>>
   >>> # Create a config with analysis enabled
   >>> config = Connect4AgentConfig(
   ...     enable_analysis=True,
   ...     should_visualize_graph=True,
   ...     max_moves=42  # Maximum possible moves in Connect4
   ... )



Classes
-------

.. toctree::
   :hidden:

   /autoapi/games/connect4/config/Connect4AgentConfig

.. autoapisummary::

   games.connect4.config.Connect4AgentConfig


