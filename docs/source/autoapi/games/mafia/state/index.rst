games.mafia.state
=================

.. py:module:: games.mafia.state

.. autoapi-nested-parse::

   Game state models for the Mafia game.

   This module defines the core state model for the Mafia game, extending the
   base MultiPlayerGameState with Mafia-specific functionality.

   The state model tracks:
       - Player roles and statuses
       - Game phase and progression
       - Voting and action history
       - Public announcements
       - Night action outcomes

   .. rubric:: Examples

   >>> from mafia.state import MafiaGameState
   >>> from mafia.models import PlayerRole, GamePhase
   >>>
   >>> # Create a new game state
   >>> state = MafiaGameState(
   ...     players=["Player_1", "Player_2", "Narrator"],
   ...     roles={"Player_1": PlayerRole.VILLAGER,
   ...            "Player_2": PlayerRole.MAFIA,
   ...            "Narrator": PlayerRole.NARRATOR},
   ...     game_phase=GamePhase.SETUP
   ... )



Classes
-------

.. toctree::
   :hidden:

   /autoapi/games/mafia/state/MafiaGameState

.. autoapisummary::

   games.mafia.state.MafiaGameState


