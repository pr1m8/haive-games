
:py:mod:`games.poker.state`
===========================

.. py:module:: games.poker.state

Texas Hold'em Poker game state management.

This module implements the core state management for a Texas Hold'em poker game,
including:
    - Game initialization and progression
    - Player action handling
    - Betting rounds and pot management
    - Hand evaluation and showdown logic
    - Side pot creation for all-in situations

The state management is built on top of LangGraph for AI agent integration,
using Pydantic models for type safety and validation.

.. rubric:: Example

>>> from poker.state import PokerState
>>>
>>> # Initialize a new game
>>> state = PokerState()
>>> state.initialize_game(["Alice", "Bob", "Charlie"], starting_chips=1000)
>>> state.start_new_hand()


.. autolink-examples:: games.poker.state
   :collapse:

Classes
-------

.. autoapisummary::

   games.poker.state.PokerState


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for PokerState:

   .. graphviz::
      :align: center

      digraph inheritance_PokerState {
        node [shape=record];
        "PokerState" [label="PokerState"];
        "pydantic.BaseModel" -> "PokerState";
      }

.. autopydantic_model:: games.poker.state.PokerState
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

.. autolink-examples:: games.poker.state
   :collapse:
   
.. autolink-skip:: next
