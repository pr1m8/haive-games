
:py:mod:`games.among_us.state_manager`
======================================

.. py:module:: games.among_us.state_manager

Comprehensive state management mixin for Among Us social deduction gameplay.

This module provides the core state management functionality for Among Us games,
handling complex game mechanics including role assignments, task management,
sabotage systems, meeting coordination, and win condition evaluation. The state
manager coordinates all gameplay elements for authentic Among Us experiences.

The state manager handles:
- Game initialization with role assignments and task generation
- Move validation and application for all player actions
- Complex sabotage mechanics with resolution systems
- Meeting and voting coordination
- Win condition evaluation and game progression
- Player state filtering for information hiding
- Legal move generation for AI decision-making

.. rubric:: Examples

Initializing a game::

    state = AmongUsStateManagerMixin.initialize(
        player_names=["Alice", "Bob", "Charlie", "David", "Eve"],
        map_name="skeld",
        num_impostors=1
    )

Applying player moves::

    move = {"action": "move", "location": "electrical"}
    new_state = AmongUsStateManagerMixin.apply_move(state, "Alice", move)

Checking game status::

    updated_state = AmongUsStateManagerMixin.check_game_status(state)
    if updated_state.game_status == "ended":
        print(f"Game over! Winner: {updated_state.winner}")

.. note::

   This is a mixin class designed to be inherited by game agents,
   providing state management capabilities without agent-specific behavior.


.. autolink-examples:: games.among_us.state_manager
   :collapse:

Classes
-------

.. autoapisummary::

   games.among_us.state_manager.AmongUsStateManagerMixin


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for AmongUsStateManagerMixin:

   .. graphviz::
      :align: center

      digraph inheritance_AmongUsStateManagerMixin {
        node [shape=record];
        "AmongUsStateManagerMixin" [label="AmongUsStateManagerMixin"];
        "haive.games.framework.multi_player.state_manager.MultiPlayerGameStateManager[haive.games.among_us.state.AmongUsState]" -> "AmongUsStateManagerMixin";
      }

.. autoclass:: games.among_us.state_manager.AmongUsStateManagerMixin
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: games.among_us.state_manager
   :collapse:
   
.. autolink-skip:: next
