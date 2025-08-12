
:py:mod:`games.hold_em.state_manager`
=====================================

.. py:module:: games.hold_em.state_manager

Texas Hold'em game state management module.

This module provides a dedicated state manager for Texas Hold'em poker games,
offering static methods for state manipulation, including:
    - Creating and initializing game states
    - Advancing game phases
    - Applying player actions
    - Handling betting rounds
    - Managing pot and chip distribution
    - Tracking hand history

The state manager serves as a central interface for manipulating the game state
in a consistent manner, separating state manipulation logic from the game agent.

.. rubric:: Example

>>> from haive.games.hold_em.state_manager import HoldemGameStateManager
>>> from haive.games.hold_em.state import HoldemState, PlayerState
>>>
>>> # Create player states
>>> players = [
>>>     PlayerState(player_id="p1", name="Alice", chips=1000, position=0),
>>>     PlayerState(player_id="p2", name="Bob", chips=1000, position=1),
>>> ]
>>>
>>> # Initialize a new game state
>>> state = HoldemGameStateManager.create_initial_state(
>>>     players=players,
>>>     small_blind=10,
>>>     big_blind=20
>>> )
>>>
>>> # Advance the game to the next phase
>>> updated_state = HoldemGameStateManager.advance_phase(state)


.. autolink-examples:: games.hold_em.state_manager
   :collapse:

Classes
-------

.. autoapisummary::

   games.hold_em.state_manager.HoldemGameStateManager


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for HoldemGameStateManager:

   .. graphviz::
      :align: center

      digraph inheritance_HoldemGameStateManager {
        node [shape=record];
        "HoldemGameStateManager" [label="HoldemGameStateManager"];
      }

.. autoclass:: games.hold_em.state_manager.HoldemGameStateManager
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: games.hold_em.state_manager
   :collapse:
   
.. autolink-skip:: next
