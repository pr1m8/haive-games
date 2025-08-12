
:py:mod:`games.go.state`
========================

.. py:module:: games.go.state

Go game state management.

This module provides state tracking and management for Go games, including:
    - Game state representation
    - Move validation and application
    - Board state tracking in SGF format
    - Capture counting
    - Game status management

.. rubric:: Example

>>> from haive.games.go.state import GoGameState, GoGameStateManager
>>>
>>> # Initialize a new game
>>> state = GoGameStateManager.initialize(board_size=19)
>>>
>>> # Apply moves
>>> state = GoGameStateManager.apply_move(state, (3, 4))  # Black's move
>>> state = GoGameStateManager.apply_move(state, (15, 15))  # White's move
>>>
>>> # Check game status
>>> print(state.game_status)  # 'ongoing'
>>> print(state.captured_stones)  # {'black': 0, 'white': 0}


.. autolink-examples:: games.go.state
   :collapse:

Classes
-------

.. autoapisummary::

   games.go.state.GoGameState


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for GoGameState:

   .. graphviz::
      :align: center

      digraph inheritance_GoGameState {
        node [shape=record];
        "GoGameState" [label="GoGameState"];
        "pydantic.BaseModel" -> "GoGameState";
      }

.. autopydantic_model:: games.go.state.GoGameState
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

.. autolink-examples:: games.go.state
   :collapse:
   
.. autolink-skip:: next
