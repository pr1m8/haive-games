games.dominoes.state
====================

.. py:module:: games.dominoes.state

.. autoapi-nested-parse::

   Comprehensive state management system for Dominoes gameplay and strategic analysis.

   This module provides sophisticated state models for Dominoes games with complete
   support for tile tracking, board management, strategic analysis, and game flow
   control. The state system maintains both traditional dominoes mechanics and
   advanced strategic context for AI decision-making.

   The state system supports:
   - Complete tile tracking with hand and boneyard management
   - Strategic analysis history for multiplayer gameplay
   - Board state validation and move legality checking
   - Game progression tracking with pass and block detection
   - Performance metrics and statistical analysis
   - Multiple game variants and scoring systems

   .. rubric:: Examples

   Creating a new game state::

       state = DominoesState.initialize(
           player_names=["player1", "player2"],
           tiles_per_hand=7
       )
       assert state.turn in ["player1", "player2"]
       assert state.game_status == "ongoing"

   Accessing game information::

       # Check board state
       left_open = state.left_value
       right_open = state.right_value
       board_display = state.board_string

       # Check hand sizes
       hand_sizes = state.hand_sizes
       tiles_remaining = state.boneyard_size

   Tracking strategic analysis::

       analysis = DominoesAnalysis(
           hand_strength="Strong high-value tiles",
           blocking_opportunities=["Block 5-5 connection"],
           optimal_plays=["Play 6-4 on right end"],
           endgame_strategy="Hold doubles for scoring"
       )
       state.add_analysis(analysis, "player1")

   Game state queries::

       # Check game completion
       if state.is_game_over():
           winner = state.winner
           final_scores = state.scores

       # Strategic position analysis
       playable_tiles = state.get_playable_tiles("player1")
       board_control = state.board_control_analysis

   .. note::

      All state models use Pydantic for validation and support both JSON
      serialization and integration with LangGraph for distributed gameplay.



Classes
-------

.. toctree::
   :hidden:

   /autoapi/games/dominoes/state/DominoesState

.. autoapisummary::

   games.dominoes.state.DominoesState


