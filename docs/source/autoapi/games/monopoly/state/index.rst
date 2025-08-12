
:py:mod:`games.monopoly.state`
==============================

.. py:module:: games.monopoly.state


Classes
-------

.. autoapisummary::

   games.monopoly.state.GameStatus
   games.monopoly.state.MonopolyState


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for GameStatus:

   .. graphviz::
      :align: center

      digraph inheritance_GameStatus {
        node [shape=record];
        "GameStatus" [label="GameStatus"];
        "str" -> "GameStatus";
        "enum.Enum" -> "GameStatus";
      }

.. autoclass:: games.monopoly.state.GameStatus
   :members:
   :undoc-members:
   :show-inheritance:

   .. note::

      **GameStatus** is an Enum defined in ``games.monopoly.state``.





.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MonopolyState:

   .. graphviz::
      :align: center

      digraph inheritance_MonopolyState {
        node [shape=record];
        "MonopolyState" [label="MonopolyState"];
        "pydantic.BaseModel" -> "MonopolyState";
      }

.. autopydantic_model:: games.monopoly.state.MonopolyState
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



Functions
---------

.. autoapisummary::

   games.monopoly.state.add_events
   games.monopoly.state.add_strings

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


   .. autolink-examples:: add_events
      :collapse:

.. py:function:: add_strings(left: list[str], right: list[str]) -> list[str]

   Custom reducer for string lists.

   Generic reducer for accumulating string lists in LangGraph state updates.

   :param left: Existing strings in the state.
   :type left: List[str]
   :param right: New strings to add.
   :type right: List[str]

   :returns: Combined list of strings.
   :rtype: List[str]


   .. autolink-examples:: add_strings
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: games.monopoly.state
   :collapse:
   
.. autolink-skip:: next
