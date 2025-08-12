
:py:mod:`games.among_us.models`
===============================

.. py:module:: games.among_us.models

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


.. autolink-examples:: games.among_us.models
   :collapse:

Classes
-------

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


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for AmongUsActionType:

   .. graphviz::
      :align: center

      digraph inheritance_AmongUsActionType {
        node [shape=record];
        "AmongUsActionType" [label="AmongUsActionType"];
        "str" -> "AmongUsActionType";
        "enum.Enum" -> "AmongUsActionType";
      }

.. autoclass:: games.among_us.models.AmongUsActionType
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **AmongUsActionType** is an Enum defined in ``games.among_us.models``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for AmongUsAnalysis:

   .. graphviz::
      :align: center

      digraph inheritance_AmongUsAnalysis {
        node [shape=record];
        "AmongUsAnalysis" [label="AmongUsAnalysis"];
        "pydantic.BaseModel" -> "AmongUsAnalysis";
      }

.. autopydantic_model:: games.among_us.models.AmongUsAnalysis
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for AmongUsGamePhase:

   .. graphviz::
      :align: center

      digraph inheritance_AmongUsGamePhase {
        node [shape=record];
        "AmongUsGamePhase" [label="AmongUsGamePhase"];
        "str" -> "AmongUsGamePhase";
        "enum.Enum" -> "AmongUsGamePhase";
      }

.. autoclass:: games.among_us.models.AmongUsGamePhase
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **AmongUsGamePhase** is an Enum defined in ``games.among_us.models``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for AmongUsPlayerDecision:

   .. graphviz::
      :align: center

      digraph inheritance_AmongUsPlayerDecision {
        node [shape=record];
        "AmongUsPlayerDecision" [label="AmongUsPlayerDecision"];
        "pydantic.BaseModel" -> "AmongUsPlayerDecision";
      }

.. autopydantic_model:: games.among_us.models.AmongUsPlayerDecision
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for PlayerMemory:

   .. graphviz::
      :align: center

      digraph inheritance_PlayerMemory {
        node [shape=record];
        "PlayerMemory" [label="PlayerMemory"];
        "pydantic.BaseModel" -> "PlayerMemory";
      }

.. autopydantic_model:: games.among_us.models.PlayerMemory
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for PlayerRole:

   .. graphviz::
      :align: center

      digraph inheritance_PlayerRole {
        node [shape=record];
        "PlayerRole" [label="PlayerRole"];
        "str" -> "PlayerRole";
        "enum.Enum" -> "PlayerRole";
      }

.. autoclass:: games.among_us.models.PlayerRole
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **PlayerRole** is an Enum defined in ``games.among_us.models``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for PlayerState:

   .. graphviz::
      :align: center

      digraph inheritance_PlayerState {
        node [shape=record];
        "PlayerState" [label="PlayerState"];
        "pydantic.BaseModel" -> "PlayerState";
      }

.. autopydantic_model:: games.among_us.models.PlayerState
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for Room:

   .. graphviz::
      :align: center

      digraph inheritance_Room {
        node [shape=record];
        "Room" [label="Room"];
        "pydantic.BaseModel" -> "Room";
      }

.. autopydantic_model:: games.among_us.models.Room
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for RoomConnection:

   .. graphviz::
      :align: center

      digraph inheritance_RoomConnection {
        node [shape=record];
        "RoomConnection" [label="RoomConnection"];
        "pydantic.BaseModel" -> "RoomConnection";
      }

.. autopydantic_model:: games.among_us.models.RoomConnection
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for SabotageEvent:

   .. graphviz::
      :align: center

      digraph inheritance_SabotageEvent {
        node [shape=record];
        "SabotageEvent" [label="SabotageEvent"];
        "pydantic.BaseModel" -> "SabotageEvent";
      }

.. autopydantic_model:: games.among_us.models.SabotageEvent
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for SabotageResolutionPoint:

   .. graphviz::
      :align: center

      digraph inheritance_SabotageResolutionPoint {
        node [shape=record];
        "SabotageResolutionPoint" [label="SabotageResolutionPoint"];
        "pydantic.BaseModel" -> "SabotageResolutionPoint";
      }

.. autopydantic_model:: games.among_us.models.SabotageResolutionPoint
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for SabotageStatus:

   .. graphviz::
      :align: center

      digraph inheritance_SabotageStatus {
        node [shape=record];
        "SabotageStatus" [label="SabotageStatus"];
        "str" -> "SabotageStatus";
        "enum.Enum" -> "SabotageStatus";
      }

.. autoclass:: games.among_us.models.SabotageStatus
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **SabotageStatus** is an Enum defined in ``games.among_us.models``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for SabotageType:

   .. graphviz::
      :align: center

      digraph inheritance_SabotageType {
        node [shape=record];
        "SabotageType" [label="SabotageType"];
        "str" -> "SabotageType";
        "enum.Enum" -> "SabotageType";
      }

.. autoclass:: games.among_us.models.SabotageType
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **SabotageType** is an Enum defined in ``games.among_us.models``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for Task:

   .. graphviz::
      :align: center

      digraph inheritance_Task {
        node [shape=record];
        "Task" [label="Task"];
        "pydantic.BaseModel" -> "Task";
      }

.. autopydantic_model:: games.among_us.models.Task
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for TaskStatus:

   .. graphviz::
      :align: center

      digraph inheritance_TaskStatus {
        node [shape=record];
        "TaskStatus" [label="TaskStatus"];
        "str" -> "TaskStatus";
        "enum.Enum" -> "TaskStatus";
      }

.. autoclass:: games.among_us.models.TaskStatus
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **TaskStatus** is an Enum defined in ``games.among_us.models``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for TaskType:

   .. graphviz::
      :align: center

      digraph inheritance_TaskType {
        node [shape=record];
        "TaskType" [label="TaskType"];
        "str" -> "TaskType";
        "enum.Enum" -> "TaskType";
      }

.. autoclass:: games.among_us.models.TaskType
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **TaskType** is an Enum defined in ``games.among_us.models``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for Vent:

   .. graphviz::
      :align: center

      digraph inheritance_Vent {
        node [shape=record];
        "Vent" [label="Vent"];
        "pydantic.BaseModel" -> "Vent";
      }

.. autopydantic_model:: games.among_us.models.Vent
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for VentConnection:

   .. graphviz::
      :align: center

      digraph inheritance_VentConnection {
        node [shape=record];
        "VentConnection" [label="VentConnection"];
        "pydantic.BaseModel" -> "VentConnection";
      }

.. autopydantic_model:: games.among_us.models.VentConnection
   :members:
   :undoc-members:
   :show-inheritance:
   :model-show-field-summary:
   :model-show-config-summary:
   :model-show-validator-members:
   :model-show-validator-summary:
   :model-show-json:
   :field-list-validators:
   :field-show-constraints:





.. rubric:: Related Links

.. autolink-examples:: games.among_us.models
   :collapse:
   
.. autolink-skip:: next
