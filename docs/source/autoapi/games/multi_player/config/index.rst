games.multi_player.config
=========================

.. py:module:: games.multi_player.config

.. autoapi-nested-parse::

   Configuration for multi-player game agents.

   This module provides the configuration class for multi-player game agents,
   supporting features like:
       - Role-based player configurations
       - LLM engine configurations per role
       - Game state schema definitions
       - Visualization settings
       - Game flow control

   .. rubric:: Example

   >>> from haive.agents.agent_games.framework.multi_player.config import MultiPlayerGameConfig
   >>> from haive.core.engine.aug_llm import AugLLMConfig
   >>>
   >>> # Create a game configuration
   >>> config = MultiPlayerGameConfig(
   ...     state_schema=MyGameState,
   ...     engines={
   ...         "player": {"move": player_llm_config},
   ...         "narrator": {"narrate": narrator_llm_config}
   ...     }
   ... )



Classes
-------

.. toctree::
   :hidden:

   /autoapi/games/multi_player/config/MultiPlayerGameConfig

.. autoapisummary::

   games.multi_player.config.MultiPlayerGameConfig


