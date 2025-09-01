games.mafia.models
==================

.. py:module:: games.mafia.models

.. autoapi-nested-parse::

   Models for the Mafia game implementation.

   This module defines the core data models and enums used in the Mafia game, including:
       - Game phases (setup, night, day discussion, voting)
       - Player roles (villager, mafia, detective, doctor, narrator)
       - Action types (speak, vote, kill, investigate, save)
       - State tracking for players and game
       - Decision models for LLM output

   .. rubric:: Examples

   >>> from mafia.models import PlayerRole, GamePhase, MafiaAction
   >>>
   >>> # Create a player action
   >>> action = MafiaAction(
   ...     player_id="Player_1",
   ...     action_type="vote",
   ...     phase=GamePhase.DAY_VOTING,
   ...     round_number=1,
   ...     target_id="Player_2"
   ... )



Classes
-------

.. toctree::
   :hidden:

   /autoapi/games/mafia/models/ActionType
   /autoapi/games/mafia/models/GamePhase
   /autoapi/games/mafia/models/MafiaAction
   /autoapi/games/mafia/models/MafiaPlayerDecision
   /autoapi/games/mafia/models/MafiaPlayerDecisionSchema
   /autoapi/games/mafia/models/NarratorAction
   /autoapi/games/mafia/models/NarratorDecision
   /autoapi/games/mafia/models/NarratorDecisionSchema
   /autoapi/games/mafia/models/PlayerRole
   /autoapi/games/mafia/models/PlayerState

.. autoapisummary::

   games.mafia.models.ActionType
   games.mafia.models.GamePhase
   games.mafia.models.MafiaAction
   games.mafia.models.MafiaPlayerDecision
   games.mafia.models.MafiaPlayerDecisionSchema
   games.mafia.models.NarratorAction
   games.mafia.models.NarratorDecision
   games.mafia.models.NarratorDecisionSchema
   games.mafia.models.PlayerRole
   games.mafia.models.PlayerState


