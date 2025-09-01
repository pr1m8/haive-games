games.multi_player.factory
==========================

.. py:module:: games.multi_player.factory

.. autoapi-nested-parse::

   Factory for creating multi-player game agents.

   This module provides a factory class for creating multi-player game agents,
   automating the creation of game-specific agent classes with proper configuration
   and state management.

   .. rubric:: Example

   >>> from haive.agents.agent_games.framework.multi_player.factory import MultiPlayerGameFactory
   >>>
   >>> # Create a new chess agent class
   >>> ChessAgent = MultiPlayerGameFactory.create_game_agent(
   ...     name="ChessAgent",
   ...     state_schema=ChessState,hv
   ...     state_manager=ChessStateManager,
   ...     player_roles=["white", "black"],
   ...     aug_llm_configs={
   ...         "white": {"move": white_llm_config},
   ...         "black": {"move": black_llm_config}
   ...     }
   ... )



Classes
-------

.. toctree::
   :hidden:

   /autoapi/games/multi_player/factory/MultiPlayerGameFactory

.. autoapisummary::

   games.multi_player.factory.MultiPlayerGameFactory


