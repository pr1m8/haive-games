
:py:mod:`games.mafia.state`
===========================

.. py:module:: games.mafia.state

Game state models for the Mafia game.

This module defines the core state model for the Mafia game, extending the
base MultiPlayerGameState with Mafia-specific functionality.

The state model tracks:
    - Player roles and statuses
    - Game phase and progression
    - Voting and action history
    - Public announcements
    - Night action outcomes

.. rubric:: Example

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


.. autolink-examples:: games.mafia.state
   :collapse:

Classes
-------

.. autoapisummary::

   games.mafia.state.MafiaGameState


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MafiaGameState:

   .. graphviz::
      :align: center

      digraph inheritance_MafiaGameState {
        node [shape=record];
        "MafiaGameState" [label="MafiaGameState"];
        "haive.games.framework.multi_player.state.MultiPlayerGameState" -> "MafiaGameState";
      }

.. autoclass:: games.mafia.state.MafiaGameState
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: games.mafia.state
   :collapse:
   
.. autolink-skip:: next
