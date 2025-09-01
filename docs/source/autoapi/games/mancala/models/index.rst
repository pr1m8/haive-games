games.mancala.models
====================

.. py:module:: games.mancala.models

.. autoapi-nested-parse::

   Comprehensive data models for the Mancala (Kalah) board game.

   This module defines the complete set of data structures for the traditional
   Mancala game, providing models for move validation, strategic analysis, and
   game state representation. The implementation follows standard Kalah rules
   with 6 pits per player and seed redistribution mechanics.

   Mancala is a classic strategy game involving:
   - Two players with 6 pits each plus one store (mancala)
   - Seed sowing mechanics with capture rules
   - Strategic pit selection for optimal play
   - Turn continuation and capture bonus rules

   Key Models:
       MancalaMove: Represents a player's pit selection
       MancalaAnalysis: Strategic evaluation for AI decision-making

   .. rubric:: Examples

   Making moves::

       from haive.games.mancala.models import MancalaMove

       # Select pit 2 for player 1
       move = MancalaMove(pit_index=2, player="player1")

       # Strategic center play
       center_move = MancalaMove(pit_index=3, player="player2")

   Strategic analysis::

       from haive.games.mancala.models import MancalaAnalysis

       analysis = MancalaAnalysis(
           captures_possible=[2, 4],
           free_turns_available=[1, 3],
           pit_values=[4, 3, 2, 5, 1, 6],
           strategy="Focus on pit 3 for free turn opportunity"
       )

   The models support AI strategy development with comprehensive validation
   and integration with the Mancala game engine.



Classes
-------

.. toctree::
   :hidden:

   /autoapi/games/mancala/models/MancalaAnalysis
   /autoapi/games/mancala/models/MancalaMove

.. autoapisummary::

   games.mancala.models.MancalaAnalysis
   games.mancala.models.MancalaMove


