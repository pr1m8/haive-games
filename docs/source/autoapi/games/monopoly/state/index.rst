games.monopoly.state
====================

.. py:module:: games.monopoly.state


Classes
-------

.. toctree::
   :hidden:

   /autoapi/games/monopoly/state/GameStatus
   /autoapi/games/monopoly/state/MonopolyState

.. autoapisummary::

   games.monopoly.state.GameStatus
   games.monopoly.state.MonopolyState


Functions
---------

.. autoapisummary::

   games.monopoly.state.add_events
   games.monopoly.state.add_strings


Module Contents
---------------

.. py:function:: add_events(left: list[haive.games.monopoly.models.GameEvent], right: list[haive.games.monopoly.models.GameEvent]) -> list[haive.games.monopoly.models.GameEvent]

   Custom reducer for game events - always append new events.

   This reducer ensures that when state updates occur through LangGraph Commands,
   game events are properly accumulated rather than replaced.

   :param left: Existing events in the state.
   :type left: List[GameEvent]
   :param right: New events to add.
   :type right: List[GameEvent]

   :returns: Combined list of events.
   :rtype: List[GameEvent]


.. py:function:: add_strings(left: list[str], right: list[str]) -> list[str]

   Custom reducer for string lists.

   Generic reducer for accumulating string lists in LangGraph state updates.

   :param left: Existing strings in the state.
   :type left: List[str]
   :param right: New strings to add.
   :type right: List[str]

   :returns: Combined list of strings.
   :rtype: List[str]


