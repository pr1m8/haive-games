games.poker.state
=================

.. py:module:: games.poker.state

.. autoapi-nested-parse::

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



Attributes
----------

.. autoapisummary::

   games.poker.state.logger


Classes
-------

.. toctree::
   :hidden:

   /autoapi/games/poker/state/PokerState

.. autoapisummary::

   games.poker.state.PokerState


Module Contents
---------------

.. py:data:: logger

