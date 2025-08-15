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


   .. autolink-examples:: games.fox_and_geese.state
      :collapse:


Classes
-------

.. autoapisummary::

   games.fox_and_geese.state.FoxAndGeeseState


Module Contents
---------------

.. py:class:: FoxAndGeeseState

   Bases: :py:obj:`haive.games.framework.base.state.GameState`


   Comprehensive state management for Fox and Geese gameplay with strategic.
   analysis.

   This class provides complete state management for the classic Fox and Geese game,
   supporting both traditional game mechanics and strategic analysis. The state system
   maintains position tracking, strategic context, and performance metrics for
   advanced AI decision-making and game analysis.

   The Fox and Geese game features asymmetric gameplay:
   - Fox: Single piece trying to escape to the opposite side or eliminate geese
   - Geese: Multiple pieces trying to trap the fox and prevent escape
   - Fox can capture geese by jumping over them (similar to checkers)
   - Geese cannot capture but can block fox movement
   - Victory conditions differ for each player

   The state system supports:
   - Complete position tracking with validation for both fox and geese
   - Strategic analysis history for both players with pattern recognition
   - Move validation and legal move generation
   - Game completion detection with multiple victory conditions
   - Performance metrics and statistical analysis for gameplay optimization
   - Board visualization and position evaluation for strategic assessment

   .. attribute:: players

      Fixed list of players ["fox", "geese"].
      Maintains consistent player identification.

      :type: List[str]

   .. attribute:: fox_position

      Current position of the fox piece.
      Tracked with full coordinate validation.

      :type: FoxAndGeesePosition

   .. attribute:: geese_positions

      Current positions of all geese.
      Maintained as a set for efficient position queries.

      :type: Set[FoxAndGeesePosition]

   .. attribute:: turn

      Current player's turn.
      Alternates between fox and geese players.

      :type: Literal["fox", "geese"]

   .. attribute:: game_status

      Current game state with completion detection.
      Tracks ongoing play and victory conditions.

      :type: Literal

   .. attribute:: move_history

      Complete chronological move history.
      Includes all moves made during the game.

      :type: List[FoxAndGeeseMove]

   .. attribute:: winner

      Winner identifier if game completed.
      Set when victory conditions are met.

      :type: Optional[str]

   .. attribute:: num_geese

      Current number of geese remaining on the board.
      Updated when geese are captured by the fox.

      :type: int

   .. attribute:: fox_analysis

      Strategic analysis history for fox player.
      Tracks reasoning and decision-making patterns.

      :type: List[str]

   .. attribute:: geese_analysis

      Strategic analysis history for geese player.
      Tracks reasoning and decision-making patterns.

      :type: List[str]

   .. rubric:: Examples

   Creating a new game state::

       state = FoxAndGeeseState.initialize()
       assert state.turn == "fox"
       assert state.game_status == "ongoing"
       assert state.fox_position.row == 3  # Center position
       assert len(state.geese_positions) > 0

   Accessing position information::

       # Check current positions
       fox_pos = state.fox_position
       geese_count = state.num_geese
       board_display = state.board_string

       # Strategic metrics
       fox_mobility = state.fox_mobility_score
       geese_formation = state.geese_formation_strength
       escape_distance = state.fox_escape_distance

   Managing strategic analysis::

       # Add analysis for fox player
       state.fox_analysis.append("Fox should move toward weak geese formation")

       # Add analysis for geese player
       state.geese_analysis.append("Geese should form blocking line")

       # Access latest strategic insights
       latest_fox_analysis = state.get_latest_fox_analysis()
       latest_geese_analysis = state.get_latest_geese_analysis()

   Game state queries::

       # Check game completion
       if state.is_game_over():
           winner = state.winner
           final_analysis = state.position_evaluation

       # Strategic position analysis
       mobility_analysis = state.mobility_analysis
       capture_threats = state.capture_threat_analysis
       formation_strength = state.formation_analysis

   Advanced game analysis::

       # Performance metrics
       stats = state.game_statistics
       print(f"Total moves: {stats['total_moves']}")
       print(f"Capture rate: {stats['capture_rate']:.1f}%")

       # Strategic evaluation
       position_eval = state.position_evaluation
       print(f"Fox advantage: {position_eval['fox_advantage']:.2f}")
       print(f"Geese control: {position_eval['geese_control']:.2f}")

   .. note::

      The state uses Pydantic v2 for validation and supports both JSON serialization
      and integration with LangGraph for distributed game systems. All position
      operations maintain game rule consistency and strategic context.


   .. autolink-examples:: FoxAndGeeseState
      :collapse:

   .. py:method:: __repr__() -> str

      Detailed string representation of the game state.


      .. autolink-examples:: __repr__
         :collapse:


   .. py:method:: __str__() -> str

      String representation of the game state.


      .. autolink-examples:: __str__
         :collapse:


   .. py:method:: get_latest_fox_analysis() -> str | None

      Get the latest strategic analysis for fox player.

      :returns: Latest fox analysis or None if no analysis exists.
      :rtype: Optional[str]


      .. autolink-examples:: get_latest_fox_analysis
         :collapse:


   .. py:method:: get_latest_geese_analysis() -> str | None

      Get the latest strategic analysis for geese player.

      :returns: Latest geese analysis or None if no analysis exists.
      :rtype: Optional[str]


      .. autolink-examples:: get_latest_geese_analysis
         :collapse:


   .. py:method:: get_recent_moves(count: int) -> list[haive.games.fox_and_geese.models.FoxAndGeeseMove]

      Get the most recent moves from the game history.

      :param count: Number of recent moves to return.
      :type count: int

      :returns: List of recent moves (up to count).
      :rtype: List[FoxAndGeeseMove]


      .. autolink-examples:: get_recent_moves
         :collapse:


   .. py:method:: initialize() -> FoxAndGeeseState
      :classmethod:


      Initialize a new Fox and Geese game.


      .. autolink-examples:: initialize
         :collapse:


   .. py:method:: is_game_over() -> bool

      Check if the game is over.

      :returns: True if game is over, False otherwise.
      :rtype: bool


      .. autolink-examples:: is_game_over
         :collapse:


   .. py:method:: model_dump(**kwargs) -> dict[str, Any]

      Override model_dump to ensure proper serialization.


      .. autolink-examples:: model_dump
         :collapse:


   .. py:method:: model_validate(obj: Any, **kwargs) -> FoxAndGeeseState
      :classmethod:


      Override model_validate to handle various input formats.


      .. autolink-examples:: model_validate
         :collapse:


   .. py:method:: serialize_fox_position(fox_position: haive.games.fox_and_geese.models.FoxAndGeesePosition) -> dict[str, Any]

      Serialize fox position as a dictionary.


      .. autolink-examples:: serialize_fox_position
         :collapse:


   .. py:method:: serialize_geese_positions(geese_positions: set[haive.games.fox_and_geese.models.FoxAndGeesePosition]) -> list[dict[str, Any]]

      Serialize geese positions as a list of dictionaries.


      .. autolink-examples:: serialize_geese_positions
         :collapse:


   .. py:method:: serialize_move_history(move_history: list[haive.games.fox_and_geese.models.FoxAndGeeseMove]) -> list[dict[str, Any]]

      Serialize move history as a list of dictionaries.


      .. autolink-examples:: serialize_move_history
         :collapse:


   .. py:method:: validate_fox_position(v: Any) -> haive.games.fox_and_geese.models.FoxAndGeesePosition
      :classmethod:


      Validate and convert fox position.


      .. autolink-examples:: validate_fox_position
         :collapse:


   .. py:method:: validate_geese_positions(v: Any) -> set[haive.games.fox_and_geese.models.FoxAndGeesePosition]
      :classmethod:


      Validate and convert geese positions to a set.


      .. autolink-examples:: validate_geese_positions
         :collapse:


   .. py:method:: validate_move_history(v: Any) -> list[haive.games.fox_and_geese.models.FoxAndGeeseMove]
      :classmethod:


      Validate and convert move history.


      .. autolink-examples:: validate_move_history
         :collapse:


   .. py:property:: board_string
      :type: str


      Get a string representation of the board.

      .. autolink-examples:: board_string
         :collapse:


   .. py:attribute:: fox_analysis
      :type:  list[str]
      :value: None



   .. py:property:: fox_escape_distance
      :type: int


      Calculate minimum distance for fox to reach escape edge.

      :returns: Minimum number of moves to reach the opposite edge.
      :rtype: int

      .. autolink-examples:: fox_escape_distance
         :collapse:


   .. py:property:: fox_mobility_score
      :type: float


      Calculate fox mobility score based on available moves.

      :returns: Mobility score from 0.0 (trapped) to 1.0 (maximum mobility).
      :rtype: float

      .. autolink-examples:: fox_mobility_score
         :collapse:


   .. py:attribute:: fox_position
      :type:  haive.games.fox_and_geese.models.FoxAndGeesePosition
      :value: None



   .. py:property:: game_statistics
      :type: dict[str, int | float | str]


      Generate comprehensive game statistics.

      :returns: Game statistics and metrics.
      :rtype: Dict[str, Union[int, float, str]]

      .. autolink-examples:: game_statistics
         :collapse:


   .. py:attribute:: game_status
      :type:  Literal['ongoing', 'fox_win', 'geese_win']
      :value: None



   .. py:attribute:: geese_analysis
      :type:  list[str]
      :value: None



   .. py:property:: geese_formation_strength
      :type: float


      Calculate geese formation strength for blocking fox.

      :returns: Formation strength from 0.0 (weak) to 1.0 (strong).
      :rtype: float

      .. autolink-examples:: geese_formation_strength
         :collapse:


   .. py:attribute:: geese_positions
      :type:  set[haive.games.fox_and_geese.models.FoxAndGeesePosition]
      :value: None



   .. py:attribute:: model_config


   .. py:attribute:: move_history
      :type:  list[haive.games.fox_and_geese.models.FoxAndGeeseMove]
      :value: None



   .. py:attribute:: num_geese
      :type:  int
      :value: None



   .. py:attribute:: players
      :type:  list[str]
      :value: None



   .. py:property:: position_evaluation
      :type: dict[str, str | float]


      Generate strategic position evaluation.

      :returns: Position evaluation metrics.
      :rtype: Dict[str, Union[str, float]]

      .. autolink-examples:: position_evaluation
         :collapse:


   .. py:property:: total_captures
      :type: int


      Count total number of geese captured by fox.

      :returns: Number of geese captured during the game.
      :rtype: int

      .. autolink-examples:: total_captures
         :collapse:


   .. py:attribute:: turn
      :type:  Literal['fox', 'geese']
      :value: None



   .. py:attribute:: winner
      :type:  str | None
      :value: None



