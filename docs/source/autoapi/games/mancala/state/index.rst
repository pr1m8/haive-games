
:py:mod:`games.mancala.state`
=============================

.. py:module:: games.mancala.state

State for the Mancala game.

This module defines the state for the Mancala game, which includes the board, turn, game
status, move history, free turn, winner, and player analyses.


.. autolink-examples:: games.mancala.state
   :collapse:

Classes
-------

.. autoapisummary::

   games.mancala.state.MancalaState


Module Contents
---------------




.. toggle:: Show Inheritance Diagram

   Inheritance diagram for MancalaState:

   .. graphviz::
      :align: center

      digraph inheritance_MancalaState {
        node [shape=record];
        "MancalaState" [label="MancalaState"];
        "haive.games.framework.base.state.GameState" -> "MancalaState";
      }

.. autoclass:: games.mancala.state.MancalaState
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autoapisummary::

   games.mancala.state.extract_analysis_from_message

.. py:function:: extract_analysis_from_message(analysis: Any) -> dict[str, Any] | None

   Extract analysis data from an AIMessage object.

   :param analysis: The analysis object to extract from.

   :returns: Extracted analysis data or None if extraction fails.


   .. autolink-examples:: extract_analysis_from_message
      :collapse:



.. rubric:: Related Links

.. autolink-examples:: games.mancala.state
   :collapse:
   
.. autolink-skip:: next
