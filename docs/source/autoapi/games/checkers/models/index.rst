games.checkers.models
=====================

.. py:module:: games.checkers.models


Classes
-------

.. autoapisummary::

   games.checkers.models.CheckersAnalysis
   games.checkers.models.CheckersMove
   games.checkers.models.CheckersPlayerDecision


Module Contents
---------------

.. py:class:: CheckersAnalysis(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Advanced strategic analysis model for Checkers position evaluation.

   This model provides comprehensive analysis of Checkers positions, including
   material evaluation, positional assessment, tactical opportunities, and
   strategic recommendations. It supports advanced AI decision-making and
   provides structured output for LLM-based analyzer engines.

   The analysis includes:
   - Material advantage assessment with piece counting
   - Center control evaluation and positional factors
   - Tactical opportunities and threats identification
   - Strategic move recommendations with prioritization
   - Overall position evaluation with confidence scoring

   .. attribute:: material_advantage

      Detailed assessment of material balance including
      piece counts, king advantages, and positional piece values.

      :type: str

   .. attribute:: control_of_center

      Analysis of center control including square
      occupation, piece mobility, and territorial advantage.

      :type: str

   .. attribute:: suggested_moves

      Prioritized list of recommended moves in
      algebraic notation with strategic reasoning.

      :type: List[str]

   .. attribute:: positional_evaluation

      Overall position assessment including
      strategic outlook, winning chances, and key factors.

      :type: str

   .. rubric:: Examples

   Balanced position analysis::\n

       analysis = CheckersAnalysis(
           material_advantage="Equal material: Red 10 pieces, Black 10 pieces, Red has 1 king advantage",
           control_of_center="Red controls 3 of 4 center squares with advanced piece formation",
           suggested_moves=["e3-f4", "c3-d4", "g3-h4"],
           positional_evaluation="Slightly favorable for Red due to superior piece placement and king advantage"
       )

   Tactical advantage analysis::\n

       analysis = CheckersAnalysis(
           material_advantage="Red ahead by 2 pieces (11 vs 9), material advantage increasing",
           control_of_center="Red dominates center with 4 pieces vs Black's 1",
           suggested_moves=["d4xf6", "b4xd6", "f4-g5"],
           positional_evaluation="Winning position for Red with multiple tactical threats"
       )

   Endgame analysis::\n

       analysis = CheckersAnalysis(
           material_advantage="Red: 2 kings, Black: 1 king + 1 piece, Red has endgame advantage",
           control_of_center="Center control less relevant in endgame, focus on king activity",
           suggested_moves=["Ka8-b7", "Kc6-d5", "Kc6-b5"],
           positional_evaluation="Technical win for Red with proper king technique"
       )

   .. note::

      This model provides structured analysis output for strategic decision-making
      and supports both human-readable explanations and automated analysis.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: CheckersAnalysis
      :collapse:

   .. py:property:: analysis_summary
      :type: dict[str, str | int]


      Generate a concise summary of the analysis.

      :returns: Summary containing key analysis points.
      :rtype: Dict[str, Union[str, int]]

      .. autolink-examples:: analysis_summary
         :collapse:


   .. py:attribute:: control_of_center
      :type:  str
      :value: None



   .. py:attribute:: material_advantage
      :type:  str
      :value: None



   .. py:attribute:: positional_evaluation
      :type:  str
      :value: None



   .. py:attribute:: suggested_moves
      :type:  list[str]
      :value: None



.. py:class:: CheckersMove(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Comprehensive representation of a Checkers move with strategic context.

   This model provides complete representation of Checkers moves, supporting
   both regular moves and jump sequences (captures). It uses standard algebraic
   notation for position representation and includes strategic metadata for
   analysis and decision-making.

   The model supports:
   - Regular diagonal moves for standard gameplay
   - Jump moves with capture mechanics
   - Multi-jump sequences for complex captures
   - King promotion and special moves
   - Strategic evaluation and move validation

   .. attribute:: from_position

      Starting position in algebraic notation (e.g., "a3").
      Uses standard checkers notation with columns a-h and rows 1-8.

      :type: str

   .. attribute:: to_position

      Ending position in algebraic notation (e.g., "b4").
      Must be a valid diagonal move according to Checkers rules.

      :type: str

   .. attribute:: player

      The player making the move.
      Red typically starts first in standard Checkers gameplay.

      :type: Literal["red", "black"]

   .. attribute:: is_jump

      Whether this is a jump move capturing an opponent's piece.
      Jump moves are mandatory when available according to Checkers rules.

      :type: bool

   .. attribute:: captured_position

      Position of the captured piece if any.
      Required when is_jump=True, indicates the captured piece's location.

      :type: Optional[str]

   .. rubric:: Examples

   Regular piece advancement::\n

       move = CheckersMove(
           from_position="a3",
           to_position="b4",
           player="red",
           is_jump=False
       )
       print(str(move))  # Output: "a3-b4"

   Capture move with jump::\n

       jump = CheckersMove(
           from_position="c3",
           to_position="e5",
           player="black",
           is_jump=True,
           captured_position="d4"
       )
       print(str(jump))  # Output: "c3xe5"

   King piece movement::\n

       king_move = CheckersMove(
           from_position="h8",
           to_position="f6",
           player="red",
           is_jump=False
       )
       # King can move backwards unlike regular pieces

   Multi-jump sequence component::\n

       first_jump = CheckersMove(
           from_position="a3",
           to_position="c5",
           player="red",
           is_jump=True,
           captured_position="b4"
       )
       # Additional jumps would be separate moves in sequence

   .. note::

      Move validation should be performed by the game state manager to ensure
      moves comply with Checkers rules and current board configuration.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: CheckersMove
      :collapse:

   .. py:method:: __str__() -> str

      Generate standard Checkers notation for the move.

      Produces move notation following standard Checkers conventions:
      - Regular moves: "a3-b4"
      - Jump moves: "a3xc5"
      - Multi-jump sequences: "a3xc5xe7"

      :returns: The move in standard Checkers notation format.
      :rtype: str

      .. rubric:: Examples

      Regular move notation::\n

          move = CheckersMove(from_position="a3", to_position="b4", player="red")
          print(str(move))  # Output: "a3-b4"

      Jump move notation::\n

          jump = CheckersMove(
              from_position="c3", to_position="e5", player="black",
              is_jump=True, captured_position="d4"
          )
          print(str(jump))  # Output: "c3xe5"


      .. autolink-examples:: __str__
         :collapse:


   .. py:method:: validate_captured_position(v: str | None, values) -> str | None
      :classmethod:


      Validate captured position is provided when move is a jump.

      :param v: Captured position to validate.
      :type v: Optional[str]
      :param values: Other field values for validation context.

      :returns: Validated captured position.
      :rtype: Optional[str]

      :raises ValueError: If captured position is invalid for jump moves.


      .. autolink-examples:: validate_captured_position
         :collapse:


   .. py:method:: validate_position_format(v: str) -> str
      :classmethod:


      Validate that position follows algebraic notation format.

      :param v: Position string to validate.
      :type v: str

      :returns: Validated position string.
      :rtype: str

      :raises ValueError: If position format is invalid.


      .. autolink-examples:: validate_position_format
         :collapse:


   .. py:attribute:: captured_position
      :type:  str | None
      :value: None



   .. py:attribute:: from_position
      :type:  str
      :value: None



   .. py:attribute:: is_jump
      :type:  bool
      :value: None



   .. py:property:: move_distance
      :type: int


      Calculate the distance of the move in squares.

      :returns: Distance moved in board squares (1 for regular moves, 2+ for jumps).
      :rtype: int

      .. autolink-examples:: move_distance
         :collapse:


   .. py:attribute:: player
      :type:  Literal['red', 'black']
      :value: None



   .. py:attribute:: to_position
      :type:  str
      :value: None



.. py:class:: CheckersPlayerDecision(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Comprehensive decision model for strategic Checkers gameplay.

   This model captures the complete decision-making process of a Checkers player,
   including the chosen move, strategic reasoning, position evaluation, and
   alternative moves considered. It provides structured output for LLM-based
   player engines and supports advanced strategic analysis.

   The decision model includes:
   - Primary move selection with full validation
   - Detailed strategic reasoning and analysis
   - Position evaluation with tactical considerations
   - Alternative moves analysis for strategic depth
   - Confidence scoring and risk assessment

   .. attribute:: move

      The chosen move with complete position information.
      Must be a valid move according to current board state.

      :type: CheckersMove

   .. attribute:: reasoning

      Detailed reasoning for the move choice including strategic
      considerations, tactical analysis, and long-term planning.

      :type: str

   .. attribute:: evaluation

      Comprehensive position evaluation including material
      balance, positional advantages, and strategic outlook.

      :type: str

   .. attribute:: alternatives

      List of alternative moves considered in algebraic
      notation, showing depth of strategic analysis.

      :type: List[str]

   .. rubric:: Examples

   Basic strategic decision::\n

       move = CheckersMove(from_position="a3", to_position="b4", player="red")
       decision = CheckersPlayerDecision(
           move=move,
           reasoning="Advancing toward center to establish control while maintaining defensive formation",
           evaluation="Slightly favorable position with improved piece mobility",
           alternatives=["c3-d4", "e3-f4", "g3-h4"]
       )

   Tactical capture decision::\n

       jump_move = CheckersMove(
           from_position="c3", to_position="e5", player="black",
           is_jump=True, captured_position="d4"
       )
       decision = CheckersPlayerDecision(
           move=jump_move,
           reasoning="Mandatory capture removes opponent's advanced piece and opens king row path",
           evaluation="Significant material advantage with tactical initiative",
           alternatives=[]  # No alternatives for mandatory jumps
       )

   King promotion decision::\n

       king_move = CheckersMove(from_position="f7", to_position="g8", player="red")
       decision = CheckersPlayerDecision(
           move=king_move,
           reasoning="Promoting to king provides backward movement capability and strategic flexibility",
           evaluation="Decisive advantage with king piece on opponent's back rank",
           alternatives=["d7-e8", "h7-g8"]
       )

   .. note::

      This model is designed for structured output from LLM-based player engines
      and provides comprehensive strategic context for move analysis.

   Create a new model by parsing and validating input data from keyword arguments.

   Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
   validated to form a valid model.

   `self` is explicitly positional-only to allow `self` as a field name.


   .. autolink-examples:: __init__
      :collapse:


   .. autolink-examples:: CheckersPlayerDecision
      :collapse:

   .. py:method:: validate_alternatives(v: list[str]) -> list[str]
      :classmethod:


      Validate alternative moves use proper algebraic notation.

      :param v: List of alternative moves to validate.
      :type v: List[str]

      :returns: Validated list of alternative moves.
      :rtype: List[str]


      .. autolink-examples:: validate_alternatives
         :collapse:


   .. py:attribute:: alternatives
      :type:  list[str]
      :value: None



   .. py:attribute:: evaluation
      :type:  str
      :value: None



   .. py:attribute:: move
      :type:  CheckersMove
      :value: None



   .. py:attribute:: reasoning
      :type:  str
      :value: None



