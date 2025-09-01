games.single_player.base
========================

.. py:module:: games.single_player.base

.. autoapi-nested-parse::

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



Attributes
----------

.. autoapisummary::

   games.single_player.base.T


Classes
-------

.. toctree::
   :hidden:

   /autoapi/games/single_player/base/GameDifficulty
   /autoapi/games/single_player/base/GameMode
   /autoapi/games/single_player/base/GameSourceType
   /autoapi/games/single_player/base/PlayerType
   /autoapi/games/single_player/base/SinglePlayerGameAgent
   /autoapi/games/single_player/base/SinglePlayerGameConfig
   /autoapi/games/single_player/base/SinglePlayerGameState
   /autoapi/games/single_player/base/SinglePlayerStateManager

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

.. py:data:: T

