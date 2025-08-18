games.dominoes.state
====================

.. py:module:: games.dominoes.state

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



.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">1 classes</span>   </div>

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



      
            
            

.. admonition:: Classes (1)
   :class: note

   .. autoapisummary::

      games.dominoes.state.DominoesState

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: DominoesState(/, **data: Any)

            Bases: :py:obj:`haive.games.framework.base.state.GameState`


            Comprehensive state management for Dominoes gameplay with strategic analysis.
            support.

            This class provides complete state management for Dominoes games, supporting
            both traditional dominoes mechanics and strategic analysis. The state system
            maintains tile tracking, board management, strategic context, and performance
            metrics for advanced AI decision-making and game analysis.

            The state system supports:
            - Complete tile tracking with hand and boneyard management
            - Strategic analysis history for multiplayer gameplay with learning capability
            - Board state validation and move legality checking
            - Game progression tracking with pass and block detection
            - Performance metrics and statistical analysis for gameplay optimization
            - Multiple game variants and scoring systems

            The game follows traditional dominoes rules:
            - Each player starts with 7 tiles (configurable)
            - Players take turns placing tiles that match board ends
            - Game ends when a player plays all tiles or board is blocked
            - Scoring typically based on remaining tiles in opponents' hands

            .. attribute:: players

               List of player names in turn order.
               Maintains consistent ordering for gameplay flow.

               :type: List[str]

            .. attribute:: hands

               Current tiles in each player's hand.
               Private information tracked for game management.

               :type: Dict[str, List[DominoTile]]

            .. attribute:: board

               Tiles currently placed on the board.
               Represents the train/line of connected dominoes.

               :type: List[DominoTile]

            .. attribute:: boneyard

               Undealt tiles available for drawing.
               Used when players cannot play and must draw.

               :type: List[DominoTile]

            .. attribute:: turn

               Current player's turn identifier.
               Cycles through players list for turn management.

               :type: str

            .. attribute:: game_status

               Current game state with completion detection.
               Tracks ongoing play, wins, and draw conditions.

               :type: Literal

            .. attribute:: move_history

               Complete move history.
               Includes both tile placements and pass actions.

               :type: List[Union[DominoMove, Literal["pass"]]]

            .. attribute:: last_passes

               Count of consecutive passes for block detection.
               Used to determine when board is blocked.

               :type: int

            .. attribute:: scores

               Current scores for each player.
               Updated based on game variant scoring rules.

               :type: Dict[str, int]

            .. attribute:: winner

               Winner identifier if game completed.
               Set when victory conditions are met.

               :type: Optional[str]

            .. attribute:: player1_analysis

               Strategic analysis history for player1.
               Tracks reasoning and decision-making patterns.

               :type: List[DominoesAnalysis]

            .. attribute:: player2_analysis

               Strategic analysis history for player2.
               Tracks reasoning and decision-making patterns.

               :type: List[DominoesAnalysis]

            .. rubric:: Examples

            Creating a new game state::

                state = DominoesState.initialize(
                    player_names=["Alice", "Bob"],
                    tiles_per_hand=7
                )
                assert state.turn in ["Alice", "Bob"]
                assert len(state.players) == 2
                assert all(len(hand) == 7 for hand in state.hands.values())

            Accessing game information::

                # Check board state
                left_open = state.left_value  # Value that can be matched on left
                right_open = state.right_value  # Value that can be matched on right
                board_display = state.board_string  # Human-readable board

                # Check hand and boneyard sizes
                hand_sizes = state.hand_sizes
                tiles_remaining = state.boneyard_size
                total_tiles = state.total_tiles_in_play

            Managing strategic analysis::

                analysis = DominoesAnalysis(
                    hand_strength="Strong concentration of 5s and 6s",
                    blocking_opportunities=["Block opponent's 3-3 double"],
                    optimal_plays=["Play 5-2 on left end for control"],
                    endgame_strategy="Hold 6-6 double for final scoring"
                )
                state.add_analysis(analysis, "Alice")

                # Access latest strategic insights
                latest_analysis = state.get_latest_analysis("Alice")

            Game state queries::

                # Check game completion
                if state.is_game_over():
                    winner = state.winner
                    final_scores = state.scores
                    game_summary = state.game_summary

                # Strategic position analysis
                playable_tiles = state.get_playable_tiles("Alice")
                board_control = state.board_control_analysis
                tile_distribution = state.tile_distribution_analysis

            Advanced game analysis::

                # Performance metrics
                stats = state.game_statistics
                print(f"Moves played: {stats['total_moves']}")
                print(f"Pass rate: {stats['pass_percentage']:.1f}%")

                # Strategic evaluation
                position_eval = state.position_evaluation
                print(f"Board control: {position_eval['board_control']}")
                print(f"Hand strength: {position_eval['hand_strength_analysis']}")

            .. note::

               The state uses Pydantic for validation and supports both JSON serialization
               and integration with LangGraph for distributed game systems. All tile
               operations maintain game rule consistency and strategic context.

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:method:: add_analysis(analysis: haive.games.dominoes.models.DominoesAnalysis, player: str) -> None

               Add strategic analysis for a player.



            .. py:method:: get_latest_analysis(player: str) -> haive.games.dominoes.models.DominoesAnalysis | None

               Get the latest analysis for a player.



            .. py:method:: get_playable_tiles(player: str) -> list[haive.games.dominoes.models.DominoTile]

               Get tiles that a player can currently play.



            .. py:method:: initialize(player_names: list[str] | None = None, tiles_per_hand: int = 7) -> DominoesState
               :classmethod:


               Initialize a new dominoes game with proper tile distribution.

               :param player_names: List of player names. Defaults to ["player1", "player2"].
               :param tiles_per_hand: Number of tiles to deal to each player. Default is 7.

               :returns: A new game state ready to play.
               :rtype: DominoesState



            .. py:method:: is_game_over() -> bool

               Check if the game is over.



            .. py:attribute:: board
               :type:  list[haive.games.dominoes.models.DominoTile]
               :value: None



            .. py:property:: board_string
               :type: str


               Get a human-readable string representation of the board.

               :returns: Visual representation of the domino train with connecting lines.
               :rtype: str


            .. py:attribute:: boneyard
               :type:  list[haive.games.dominoes.models.DominoTile]
               :value: None



            .. py:property:: boneyard_size
               :type: int


               Get the number of tiles remaining in the boneyard.


            .. py:property:: game_statistics
               :type: dict[str, int | float | str]


               Generate comprehensive game statistics.


            .. py:attribute:: game_status
               :type:  Literal['ongoing', 'player1_win', 'player2_win', 'draw']
               :value: None



            .. py:property:: hand_sizes
               :type: dict[str, int]


               Get the current hand sizes for all players.


            .. py:attribute:: hands
               :type:  dict[str, list[haive.games.dominoes.models.DominoTile]]
               :value: None



            .. py:property:: is_blocked
               :type: bool


               Check if the board is blocked (all players have passed).


            .. py:attribute:: last_passes
               :type:  int
               :value: None



            .. py:property:: left_value
               :type: int | None


               Get the value on the left end of the board that can be matched.

               :returns: Value that can be matched on left end, None if board empty.
               :rtype: Optional[int]


            .. py:attribute:: model_config

               Configuration for the model, should be a dictionary conforming to [`ConfigDict`][pydantic.config.ConfigDict].


            .. py:attribute:: move_history
               :type:  list[haive.games.dominoes.models.DominoMove | Literal['pass']]
               :value: None



            .. py:attribute:: player1_analysis
               :type:  list[haive.games.dominoes.models.DominoesAnalysis]
               :value: None



            .. py:attribute:: player2_analysis
               :type:  list[haive.games.dominoes.models.DominoesAnalysis]
               :value: None



            .. py:attribute:: players
               :type:  list[str]
               :value: None



            .. py:property:: position_evaluation
               :type: dict[str, str | int | float]


               Generate strategic position evaluation.


            .. py:property:: right_value
               :type: int | None


               Get the value on the right end of the board that can be matched.

               :returns: Value that can be matched on right end, None if board empty.
               :rtype: Optional[int]


            .. py:attribute:: scores
               :type:  dict[str, int]
               :value: None



            .. py:property:: total_tiles_in_play
               :type: int


               Get the total number of tiles currently in players' hands and on board.


            .. py:attribute:: turn
               :type:  str
               :value: None



            .. py:attribute:: winner
               :type:  str | None
               :value: None






----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.dominoes.state import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

