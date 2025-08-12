
:py:mod:`games.among_us.state`
==============================

.. py:module:: games.among_us.state

Comprehensive state management for Among Us social deduction gameplay.

This module provides the core state model for managing Among Us game sessions,
tracking player positions, tasks, sabotages, and game progression. The state
system supports complex spatial navigation, role-based mechanics, and real-time
event handling for authentic social deduction experiences.

The state management includes:
- Dynamic map initialization with rooms and vents
- Player position and status tracking
- Task completion monitoring
- Sabotage event management
- Meeting and voting mechanics
- Win condition evaluation
- Observation and memory systems

.. rubric:: Examples

Initializing a game state::

    state = AmongUsState()
    state.initialize_map()  # Creates Skeld map by default

    # Add players
    state.player_states["player1"] = PlayerState(
        id="player1",
        role=PlayerRole.CREWMATE,
        location="cafeteria"
    )

Checking win conditions::

    winner = state.check_win_condition()
    if winner == "crewmates":
        print("All tasks completed!")
    elif winner == "impostors":
        print("Impostors have taken control!")

Managing sabotages::

    # Create reactor meltdown
    sabotage = SabotageEvent(
        type="reactor",
        location="reactor",
        timer=30
    )
    state.sabotages.append(sabotage)

    # Check if critical
    active = state.get_active_sabotage()
    if active and active.is_critical():
        print(f"Emergency! {active.timer}s remaining!")

.. note::

   The state model extends MultiPlayerGameState and integrates with
   LangGraph for distributed game session management.


.. autolink-examples:: games.among_us.state
   :collapse:

Classes
-------

.. autoapisummary::

   games.among_us.state.AmongUsState


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for AmongUsState:

   .. graphviz::
      :align: center

      digraph inheritance_AmongUsState {
        node [shape=record];
        "AmongUsState" [label="AmongUsState"];
        "haive.games.framework.multi_player.state.MultiPlayerGameState" -> "AmongUsState";
      }

.. autoclass:: games.among_us.state.AmongUsState
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: games.among_us.state
   :collapse:
   
.. autolink-skip:: next
