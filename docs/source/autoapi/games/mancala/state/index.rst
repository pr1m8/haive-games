games.mancala.state
===================

.. py:module:: games.mancala.state

.. autoapi-nested-parse::

   State for the Mancala game.

   This module defines the state for the Mancala game, which includes the board, turn, game
   status, move history, free turn, winner, and player analyses.



Attributes
----------

.. autoapisummary::

   games.mancala.state.logger


Classes
-------

.. toctree::
   :hidden:

   /autoapi/games/mancala/state/MancalaState

.. autoapisummary::

   games.mancala.state.MancalaState


Functions
---------

.. autoapisummary::

   games.mancala.state.extract_analysis_from_message


Module Contents
---------------

.. py:function:: extract_analysis_from_message(analysis: Any) -> dict[str, Any] | None

   Extract analysis data from an AIMessage object.

   :param analysis: The analysis object to extract from.

   :returns: Extracted analysis data or None if extraction fails.


.. py:data:: logger

