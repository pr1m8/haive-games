games.nim.models
================

.. py:module:: games.nim.models

Module documentation for games.nim.models


.. raw:: html
   
   <div class="autoapi-module-summary">
<span class="module-stat">4 classes</span>   </div>


      
            
            

.. admonition:: Classes (4)
   :class: note

   .. autoapisummary::

      games.nim.models.NimAnalysis
      games.nim.models.NimMove
      games.nim.models.NimVariant
      games.nim.models.PositionType

            
            

.. dropdown:: :octicon:`book` Complete API Documentation
   :open:
   :class-title: sd-font-weight-bold sd-text-info
   :class-container: sd-border-info

   .. grid:: 1 2 2 3
      :gutter: 2

      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: NimAnalysis(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            Advanced strategic analysis model for Nim positions with mathematical rigor.

            This model provides comprehensive analysis of Nim positions using game theory,
            nimber theory, and optimal play strategies. It supports advanced AI decision-making
            and provides structured output for LLM-based analyzer engines with mathematical
            foundations and strategic insights.

            The analysis includes:
            - Mathematical nim-sum calculation using XOR operations
            - Winning/losing position classification using Sprague-Grundy theorem
            - Optimal move generation with strategic reasoning
            - Game theory analysis with minimax considerations
            - Variant-specific strategy adaptations
            - Educational explanations of mathematical concepts

            .. attribute:: nim_sum

               Binary XOR sum of all pile sizes (nimber value).
               Fundamental value for determining position type and optimal play.

               :type: int

            .. attribute:: position_evaluation

               Classification of position strength.
               Determines whether position is winning, losing, or drawn.

               :type: Literal

            .. attribute:: recommended_move

               Optimal move based on mathematical analysis.
               Move that maintains or achieves winning position when possible.

               :type: NimMove

            .. attribute:: explanation

               Detailed explanation of the strategic analysis.
               Educational content explaining the reasoning and mathematics.

               :type: str

            .. attribute:: winning_strategy

               High-level strategy for winning from this position.
               Strategic guidance for maintaining advantage or fighting for draws.

               :type: str

            .. attribute:: mathematical_proof

               Mathematical justification for analysis.
               Formal proof or theorem application supporting the conclusion.

               :type: Optional[str]

            .. attribute:: alternative_moves

               Other strong moves considered.
               Shows depth of analysis and strategic alternatives.

               :type: List[NimMove]

            .. attribute:: position_complexity

               Categorization of position difficulty.
               Helps guide analysis depth and computational requirements.

               :type: PositionType

            .. attribute:: variant_considerations

               Special considerations for game variants.
               Adaptations needed for misère, fibonacci, or other Nim variants.

               :type: Optional[str]

            .. rubric:: Examples

            Basic position analysis::\n

                analysis = NimAnalysis(
                    nim_sum=5,
                    position_evaluation="winning",
                    recommended_move=optimal_move,
                    explanation="Position has nim-sum 5, making it a winning position",
                    winning_strategy="Force nim-sum to 0 for opponent",
                    position_complexity=PositionType.SIMPLE
                )

            Complex position with mathematical proof::\n

                analysis = NimAnalysis(
                    nim_sum=0,
                    position_evaluation="losing",
                    recommended_move=best_try_move,
                    explanation="Nim-sum is 0, indicating a losing position for the current player",
                    winning_strategy="Look for opponent mistakes and maintain symmetry when possible",
                    mathematical_proof="By Sprague-Grundy theorem, nim-sum 0 is a P-position (losing)",
                    position_complexity=PositionType.COMPLEX
                )

            Misère Nim analysis::\n

                analysis = NimAnalysis(
                    nim_sum=1,
                    position_evaluation="complex",
                    recommended_move=endgame_move,
                    explanation="Misère endgame requires different strategy than standard Nim",
                    winning_strategy="Count total stones and analyze parity in endgame",
                    variant_considerations="Misère rule reverses strategy when all piles have size ≤ 1",
                    position_complexity=PositionType.CRITICAL
                )

            Educational analysis for learning::\n

                analysis = NimAnalysis(
                    nim_sum=3,
                    position_evaluation="winning",
                    recommended_move=teaching_move,
                    explanation="To find optimal move: calculate nim-sum, then reduce one pile to make nim-sum 0",
                    winning_strategy="Always leave opponent with nim-sum 0 (cold position)",
                    mathematical_proof="Theorem: All positions with nim-sum ≠ 0 are winning (hot positions)",
                    position_complexity=PositionType.SIMPLE
                )

            .. note::

               This model provides structured analysis output for strategic decision-making
               and supports both human-readable explanations and automated analysis systems.

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:method:: __str__() -> str

               Generate human-readable string representation of the analysis.

               :returns: Formatted analysis summary with key insights.
               :rtype: str

               .. rubric:: Examples

               Basic analysis format::\n

                   analysis = NimAnalysis(...)
                   print(str(analysis))
                   # Output: "Analysis: winning position (nim-sum: 5) - Force nim-sum to 0 for opponent"

               Complex analysis with proof::\n

                   analysis = NimAnalysis(mathematical_proof="By Sprague-Grundy theorem...")
                   print(str(analysis))
                   # Output: "Analysis: losing position (nim-sum: 0) - Mathematical proof available"



            .. py:attribute:: alternative_moves
               :type:  list[NimMove]
               :value: None



            .. py:property:: analysis_confidence
               :type: Literal['high', 'medium', 'low']


               Assess confidence level of the analysis.

               :returns: Confidence level based on position complexity and proof strength.
               :rtype: Literal


            .. py:attribute:: explanation
               :type:  str
               :value: None



            .. py:property:: is_winning_position
               :type: bool


               Determine if current position is winning for the active player.

               :returns: True if position is winning, False otherwise.
               :rtype: bool


            .. py:attribute:: mathematical_proof
               :type:  str | None
               :value: None



            .. py:attribute:: model_config

               Configuration for the model, should be a dictionary conforming to [`ConfigDict`][pydantic.config.ConfigDict].


            .. py:attribute:: nim_sum
               :type:  int
               :value: None



            .. py:attribute:: position_complexity
               :type:  PositionType
               :value: None



            .. py:attribute:: position_evaluation
               :type:  Literal['winning', 'losing', 'drawn', 'complex']
               :value: None



            .. py:attribute:: recommended_move
               :type:  NimMove
               :value: None



            .. py:property:: strategic_summary
               :type: dict[str, str | int | bool]


               Generate concise strategic summary.

               :returns: Key strategic insights and metrics.
               :rtype: Dict[str, Union[str, int, bool]]


            .. py:attribute:: variant_considerations
               :type:  str | None
               :value: None



            .. py:attribute:: winning_strategy
               :type:  str
               :value: None




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: NimMove(/, **data: Any)

            Bases: :py:obj:`pydantic.BaseModel`


            Comprehensive representation of a Nim move with strategic context and validation.

            This model provides complete representation of Nim moves, supporting both
            basic gameplay and advanced strategic analysis. It includes validation for
            legal moves, strategic context for decision-making, and comprehensive
            mathematical analysis integration.

            The model supports:
            - Complete move specification with pile and stone count
            - Strategic reasoning and alternative move analysis
            - Mathematical validation and constraint checking
            - Multi-variant Nim support with rule adaptations
            - Performance evaluation and move quality assessment

            .. attribute:: pile_index

               Index of the pile to take stones from (0-based indexing).
               Must be a valid pile index within the current game state.

               :type: int

            .. attribute:: stones_taken

               Number of stones to take from the specified pile.
               Must be positive and not exceed the pile size.

               :type: int

            .. attribute:: player

               Name or identifier of the player making the move.
               Used for game history and strategic analysis tracking.

               :type: str

            .. attribute:: reasoning

               Strategic reasoning behind the move choice.
               Provides context for decision-making and learning analysis.

               :type: Optional[str]

            .. attribute:: move_quality

               Assessment of move quality for analysis.
               Categorizes moves as optimal, good, poor, or blunder.

               :type: Optional[str]

            .. attribute:: alternative_moves

               Other moves considered.
               Shows depth of strategic analysis and decision-making process.

               :type: List[Dict[str, int]]

            .. attribute:: time_taken

               Time taken to make the move in seconds.
               Useful for performance analysis and time management.

               :type: Optional[float]

            .. rubric:: Examples

            Basic move in standard Nim::\n

                move = NimMove(
                    pile_index=0,
                    stones_taken=3,
                    player="Player1"
                )
                print(str(move))  # Output: "Player1 takes 3 stones from pile 0"

            Strategic move with reasoning::\n

                move = NimMove(
                    pile_index=1,
                    stones_taken=2,
                    player="AliceAI",
                    reasoning="Forcing nim-sum to 0 to put opponent in losing position",
                    move_quality="optimal",
                    alternative_moves=[{"pile_index": 0, "stones_taken": 1}]
                )

            Tournament move with timing::\n

                move = NimMove(
                    pile_index=2,
                    stones_taken=5,
                    player="BobBot",
                    reasoning="Maintaining winning position with precise calculation",
                    move_quality="optimal",
                    time_taken=2.3
                )

            Analysis of move alternatives::\n

                move = NimMove(
                    pile_index=0,
                    stones_taken=1,
                    player="CharlieAI",
                    move_quality="good",
                    alternative_moves=[
                        {"pile_index": 1, "stones_taken": 3},
                        {"pile_index": 2, "stones_taken": 2}
                    ]
                )
                # Shows consideration of multiple options

            .. note::

               Move validation should be performed by the game state manager to ensure
               moves comply with Nim rules and current pile configurations.

            Create a new model by parsing and validating input data from keyword arguments.

            Raises [`ValidationError`][pydantic_core.ValidationError] if the input data cannot be
            validated to form a valid model.

            `self` is explicitly positional-only to allow `self` as a field name.


            .. py:method:: __str__() -> str

               Generate human-readable string representation of the move.

               :returns: Formatted move description including player and action.
               :rtype: str

               .. rubric:: Examples

               Basic move format::\n

                   move = NimMove(pile_index=0, stones_taken=3, player="Player1")
                   print(str(move))  # Output: "Player1 takes 3 stones from pile 0"

               Move with quality assessment::\n

                   move = NimMove(
                       pile_index=1, stones_taken=2, player="AI",
                       move_quality="optimal"
                   )
                   print(str(move))  # Output: "AI takes 2 stones from pile 1 (optimal)"



            .. py:method:: validate_alternative_moves(v: list[dict[str, int]]) -> list[dict[str, int]]
               :classmethod:


               Validate alternative moves have required fields.

               :param v: List of alternative moves to validate.
               :type v: List[Dict[str, int]]

               :returns: Validated alternative moves.
               :rtype: List[Dict[str, int]]

               :raises ValueError: If alternative moves are malformed.



            .. py:attribute:: alternative_moves
               :type:  list[dict[str, int]]
               :value: None



            .. py:property:: has_strategic_context
               :type: bool


               Check if move includes strategic analysis context.

               :returns: True if move includes reasoning or quality assessment.
               :rtype: bool


            .. py:property:: move_notation
               :type: str


               Generate algebraic notation for the move.

               :returns: Move in algebraic notation format (e.g., "P0-3" for pile 0, take 3).
               :rtype: str


            .. py:attribute:: move_quality
               :type:  Literal['optimal', 'good', 'poor', 'blunder'] | None
               :value: None



            .. py:attribute:: pile_index
               :type:  int
               :value: None



            .. py:attribute:: player
               :type:  str
               :value: None



            .. py:attribute:: reasoning
               :type:  str | None
               :value: None



            .. py:attribute:: stones_taken
               :type:  int
               :value: None



            .. py:attribute:: time_taken
               :type:  float | None
               :value: None




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: NimVariant

            Bases: :py:obj:`str`, :py:obj:`enum.Enum`


            Enumeration of Nim game variants and rule modifications.

            Defines different variants of Nim with their specific rules and strategic
            considerations, affecting optimal play strategies and analysis approaches.

            Values:
                STANDARD: Classic Nim rules (last player to move wins)
                MISERE: Misère Nim (last player to move loses)
                FIBONACCI: Fibonacci Nim (can only take 1 or 2 stones)
                KAYLES: Kayles variant (splitting piles allowed)
                SUBTRACTION: Subtraction game (limited move set)


            Initialize self.  See help(type(self)) for accurate signature.


            .. py:attribute:: FIBONACCI
               :value: 'fibonacci'



            .. py:attribute:: KAYLES
               :value: 'kayles'



            .. py:attribute:: MISERE
               :value: 'misere'



            .. py:attribute:: STANDARD
               :value: 'standard'



            .. py:attribute:: SUBTRACTION
               :value: 'subtraction'




      .. grid-item-card:: 
         :class-card: sd-border-0 sd-shadow-sm
         :class-title: sd-text-center sd-font-weight-bold

.. py:class:: PositionType

            Bases: :py:obj:`str`, :py:obj:`enum.Enum`


            Enumeration of Nim position types for strategic analysis.

            Categorizes positions based on their strategic characteristics and
            complexity, helping guide appropriate analysis approaches.

            Values:
                SIMPLE: Simple endgame position (1-2 piles)
                COMPLEX: Complex midgame position (3+ piles)
                CRITICAL: Critical position requiring precise calculation
                TRIVIAL: Trivial position with obvious moves


            Initialize self.  See help(type(self)) for accurate signature.


            .. py:attribute:: COMPLEX
               :value: 'complex'



            .. py:attribute:: CRITICAL
               :value: 'critical'



            .. py:attribute:: SIMPLE
               :value: 'simple'



            .. py:attribute:: TRIVIAL
               :value: 'trivial'






----

.. admonition:: Quick Reference
   :class: tip

   .. code-block:: python

      from games.nim.models import *

      # Module provides type hints for mypy compatibility
      # View source: https://github.com/haive-ai/haive

