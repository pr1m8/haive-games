
:py:mod:`games.mafia.state_manager`
===================================

.. py:module:: games.mafia.state_manager

State management for the Mafia game.

This module provides the core state management functionality for the Mafia game,
handling game state transitions, move validation, and game progression logic.

The state manager is responsible for:
    - Game initialization and setup
    - Phase transitions (day/night cycles)
    - Move validation and application
    - Game state filtering for information hiding
    - Win condition checking


.. autolink-examples:: games.mafia.state_manager
   :collapse:

Classes
-------

.. autoapisummary::

   games.mafia.state_manager.MafiaStateManager


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MafiaStateManager:

   .. graphviz::
      :align: center

      digraph inheritance_MafiaStateManager {
        node [shape=record];
        "MafiaStateManager" [label="MafiaStateManager"];
        "haive.games.framework.multi_player.state_manager.MultiPlayerGameStateManager[haive.games.mafia.state.MafiaGameState]" -> "MafiaStateManager";
      }

.. autoclass:: games.mafia.state_manager.MafiaStateManager
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: games.mafia.state_manager
   :collapse:
   
.. autolink-skip:: next
