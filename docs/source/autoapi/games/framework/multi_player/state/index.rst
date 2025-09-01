games.framework.multi_player.state
==================================

.. py:module:: games.framework.multi_player.state

.. autoapi-nested-parse::

   Base state management for multi-player games.

   This module provides the foundational state model for multi-player games,
   supporting features like:
       - Player tracking and turn management
       - Game phase transitions
       - Move history recording
       - Public and private state management
       - Error handling

   .. rubric:: Examples

   >>> from haive.agents.agent_games.framework.multi_player.state import MultiPlayerGameState
   >>>
   >>> # Create a game state
   >>> state = MultiPlayerGameState(
   ...     players=["player1", "player2", "player3"],
   ...     game_phase=GamePhase.SETUP
   ... )
   >>>
   >>> # Advance to next player
   >>> next_player = state.advance_player()



Classes
-------

.. toctree::
   :hidden:

   /autoapi/games/framework/multi_player/state/MultiPlayerGameState

.. autoapisummary::

   games.framework.multi_player.state.MultiPlayerGameState


