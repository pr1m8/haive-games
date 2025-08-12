
:py:mod:`games.multi_player.state`
==================================

.. py:module:: games.multi_player.state

Base state management for multi-player games.

This module provides the foundational state model for multi-player games,
supporting features like:
    - Player tracking and turn management
    - Game phase transitions
    - Move history recording
    - Public and private state management
    - Error handling

.. rubric:: Example

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


.. autolink-examples:: games.multi_player.state
   :collapse:

Classes
-------

.. autoapisummary::

   games.multi_player.state.MultiPlayerGameState


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MultiPlayerGameState:

   .. graphviz::
      :align: center

      digraph inheritance_MultiPlayerGameState {
        node [shape=record];
        "MultiPlayerGameState" [label="MultiPlayerGameState"];
        "pydantic.BaseModel" -> "MultiPlayerGameState";
      }

.. autopydantic_model:: games.multi_player.state.MultiPlayerGameState
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

.. autolink-examples:: games.multi_player.state
   :collapse:
   
.. autolink-skip:: next
