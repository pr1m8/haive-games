games.hold_em.state
===================

.. py:module:: games.hold_em.state

.. autoapi-nested-parse::

   Fixed Texas Hold'em game state models.

   Key fixes:
   1. Added Annotated type for current_player_index to handle concurrent updates
   2. Fixed reducer setup for fields that might be updated concurrently
   3. Added proper field annotations for LangGraph compatibility



Classes
-------

.. toctree::
   :hidden:

   /autoapi/games/hold_em/state/GamePhase
   /autoapi/games/hold_em/state/HoldemState
   /autoapi/games/hold_em/state/PlayerAction
   /autoapi/games/hold_em/state/PlayerDecision
   /autoapi/games/hold_em/state/PlayerState
   /autoapi/games/hold_em/state/PlayerStatus
   /autoapi/games/hold_em/state/PokerAction

.. autoapisummary::

   games.hold_em.state.GamePhase
   games.hold_em.state.HoldemState
   games.hold_em.state.PlayerAction
   games.hold_em.state.PlayerDecision
   games.hold_em.state.PlayerState
   games.hold_em.state.PlayerStatus
   games.hold_em.state.PokerAction


Functions
---------

.. autoapisummary::

   games.hold_em.state.last_value_reducer


Module Contents
---------------

.. py:function:: last_value_reducer(a: Any, b: Any) -> Any

   Reducer that takes the last value - for fields that should be overwritten.


