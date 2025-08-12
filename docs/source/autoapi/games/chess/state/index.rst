
:py:mod:`games.chess.state`
===========================

.. py:module:: games.chess.state

Chess game state models.

This module defines the state schema for chess games, including:
    - Board state representation using FEN notation
    - Move history tracking
    - Game status management
    - Position analysis storage
    - Player turn tracking

The state schema provides a complete representation of a chess game state
that can be used by the agent and state manager.


.. autolink-examples:: games.chess.state
   :collapse:

Classes
-------

.. autoapisummary::

   games.chess.state.ChessState


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for ChessState:

   .. graphviz::
      :align: center

      digraph inheritance_ChessState {
        node [shape=record];
        "ChessState" [label="ChessState"];
        "haive.core.schema.state_schema.StateSchema" -> "ChessState";
      }

.. autoclass:: games.chess.state.ChessState
   :members:
   :undoc-members:
   :show-inheritance:




.. rubric:: Related Links

.. autolink-examples:: games.chess.state
   :collapse:
   
.. autolink-skip:: next
