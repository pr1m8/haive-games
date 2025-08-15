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


   .. autolink-examples:: games.mancala.models
      :collapse:


Classes
-------

.. autoapisummary::

   games.mancala.models.MancalaAnalysis
   games.mancala.models.MancalaMove


Module Contents
---------------

.. py:class:: MancalaAnalysis(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Analysis of a Mancala position.

   This class defines the structure of an analysis for a Mancala position, which
   includes the overall position evaluation, advantage level, stone distribution, pit
   recommendations, strategic focus, key tactics, and reasoning.


   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: MancalaAnalysis
      :collapse:

   .. py:attribute:: advantage_level
      :type:  int
      :value: None



   .. py:attribute:: key_tactics
      :type:  list[str]
      :value: None



   .. py:attribute:: pit_recommendations
      :type:  list[int]
      :value: None



   .. py:attribute:: position_evaluation
      :type:  Literal['winning', 'losing', 'equal', 'unclear']
      :value: None



   .. py:attribute:: reasoning
      :type:  str
      :value: None



   .. py:attribute:: stone_distribution
      :type:  str
      :value: None



   .. py:attribute:: strategy_focus
      :type:  Literal['offensive', 'defensive', 'balanced']
      :value: None



.. py:class:: MancalaMove(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Represents a move in Mancala.

   This class defines the structure of a move in Mancala, which includes the pit index
   to sow from and the player making the move.


   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: MancalaMove
      :collapse:

   .. py:method:: __str__() -> str

      Return string representation of the move.


      .. autolink-examples:: __str__
         :collapse:


   .. py:method:: validate_pit_index(v: int, info: pydantic.ValidationInfo) -> int
      :classmethod:


      Validate that the pit index is valid for the player.

      :param v: The pit index to validate.
      :param info: Validation info containing other field values.

      :returns: The validated pit index.

      :raises ValueError: If pit index is out of valid range.


      .. autolink-examples:: validate_pit_index
         :collapse:


   .. py:attribute:: pit_index
      :type:  int
      :value: None



   .. py:attribute:: player
      :type:  Literal['player1', 'player2']
      :value: None



