games.among_us.models
=====================

.. py:module:: games.among_us.models

.. autoapi-nested-parse::

   Comprehensive data models for Among Us social deduction gameplay.

   This module provides sophisticated data models for the Among Us game implementation,
   supporting both cooperative crew tasks and deceptive impostor gameplay. The models
   enable structured data handling for complex social deduction mechanics, spatial
   navigation, task management, and strategic decision-making.

   The models support:
   - Role-based gameplay (Crewmate vs Impostor)
   - Spatial navigation with rooms and vents
   - Task management with multiple task types
   - Sabotage systems with critical and non-critical events
   - Memory and observation tracking for deduction
   - Strategic analysis and decision-making
   - Meeting and voting mechanics

   .. rubric:: Examples

   Creating a player with tasks::

       player = PlayerState(
           id="player1",
           role=PlayerRole.CREWMATE,
           location="cafeteria",
           tasks=[
               Task(
                   id="task1",
                   type=TaskType.SHORT,
                   location="electrical",
                   description="Fix wiring"
               )
           ]
       )

   Impostor actions::

       impostor = PlayerState(
           id="impostor1",
           role=PlayerRole.IMPOSTOR,
           location="medbay"
       )

       # Check kill ability
       if impostor.can_kill(kill_cooldown=0):
           decision = AmongUsPlayerDecision(
               action_type=AmongUsActionType.KILL,
               target_player="player2",
               reasoning="Isolated target in medbay"
           )

   Sabotage management::

       sabotage = SabotageEvent(
           type="reactor",
           location="reactor",
           timer=30,
           resolution_points=[
               SabotageResolutionPoint(
                   id="reactor_left",
                   location="reactor",
                   description="Left panel"
               ),
               SabotageResolutionPoint(
                   id="reactor_right",
                   location="reactor",
                   description="Right panel"
               )
           ]
       )

       # Check if critical
       if sabotage.is_critical():
           print("Emergency! Reactor meltdown imminent!")

   .. note::

      All models use Pydantic for validation and support both JSON serialization
      and integration with LLM-based strategic decision systems.



Classes
-------

.. toctree::
   :hidden:

   /autoapi/games/among_us/models/AmongUsActionType
   /autoapi/games/among_us/models/AmongUsAnalysis
   /autoapi/games/among_us/models/AmongUsGamePhase
   /autoapi/games/among_us/models/AmongUsPlayerDecision
   /autoapi/games/among_us/models/PlayerMemory
   /autoapi/games/among_us/models/PlayerRole
   /autoapi/games/among_us/models/PlayerState
   /autoapi/games/among_us/models/Room
   /autoapi/games/among_us/models/RoomConnection
   /autoapi/games/among_us/models/SabotageEvent
   /autoapi/games/among_us/models/SabotageResolutionPoint
   /autoapi/games/among_us/models/SabotageStatus
   /autoapi/games/among_us/models/SabotageType
   /autoapi/games/among_us/models/Task
   /autoapi/games/among_us/models/TaskStatus
   /autoapi/games/among_us/models/TaskType
   /autoapi/games/among_us/models/Vent
   /autoapi/games/among_us/models/VentConnection

.. autoapisummary::

   games.among_us.models.AmongUsActionType
   games.among_us.models.AmongUsAnalysis
   games.among_us.models.AmongUsGamePhase
   games.among_us.models.AmongUsPlayerDecision
   games.among_us.models.PlayerMemory
   games.among_us.models.PlayerRole
   games.among_us.models.PlayerState
   games.among_us.models.Room
   games.among_us.models.RoomConnection
   games.among_us.models.SabotageEvent
   games.among_us.models.SabotageResolutionPoint
   games.among_us.models.SabotageStatus
   games.among_us.models.SabotageType
   games.among_us.models.Task
   games.among_us.models.TaskStatus
   games.among_us.models.TaskType
   games.among_us.models.Vent
   games.among_us.models.VentConnection


