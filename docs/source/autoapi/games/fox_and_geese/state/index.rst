games.fox_and_geese.state
=========================

.. py:module:: games.fox_and_geese.state

.. autoapi-nested-parse::

   Comprehensive state management system for Fox and Geese gameplay and strategic.
   analysis.

   This module provides sophisticated state models for the classic Fox and Geese game
   with complete support for position tracking, strategic analysis, and game flow
   management. The state system maintains both traditional game mechanics and
   advanced strategic context for AI decision-making.

   The Fox and Geese game is an asymmetric strategy game where:
   - One player controls the fox (trying to escape to the other side)
   - The other player controls multiple geese (trying to trap the fox)
   - The fox can capture geese by jumping over them
   - The geese win by blocking all fox movement
   - The fox wins by reaching the opposite side or reducing geese numbers

   The state system supports:
   - Complete position tracking for fox and geese
   - Strategic analysis history for both players
   - Move validation and game completion detection
   - Performance metrics and statistical analysis
   - Board visualization and position evaluation

   .. rubric:: Examples

   Creating a new game state::

       state = FoxAndGeeseState.initialize()
       assert state.turn == "fox"
       assert state.game_status == "ongoing"
       assert len(state.geese_positions) > 0

   Accessing position information::

       # Check current positions
       fox_pos = state.fox_position
       geese_count = state.num_geese
       board_display = state.board_string

       # Strategic analysis
       fox_mobility = state.fox_mobility_score
       geese_formation = state.geese_formation_strength

   Tracking game progression::

       # Check game completion
       if state.is_game_over():
           winner = state.winner
           final_analysis = state.position_evaluation

       # Move history analysis
       recent_moves = state.get_recent_moves(3)
       capture_count = state.total_captures

   .. note::

      All state models use Pydantic v2 for validation and support both JSON
      serialization and integration with LangGraph for distributed gameplay.



Classes
-------

.. toctree::
   :hidden:

   /autoapi/games/fox_and_geese/state/FoxAndGeeseState

.. autoapisummary::

   games.fox_and_geese.state.FoxAndGeeseState


