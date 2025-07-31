from enum import Enum
from typing import Literal

from pydantic import BaseModel, Field, computed_field, field_validator

r"""Comprehensive data models for strategic Nim gameplay and mathematical
analysis.

This module provides sophisticated data models for the mathematical game of Nim,
supporting both traditional gameplay and advanced strategic analysis. The models
enable structured data handling throughout the Nim game implementation and provide
strong typing for LLM-based components and mathematical analysis systems.

The models support:
- Complete move representation with pile management and validation
- Mathematical analysis using nimber theory and optimal play strategies
- Strategic decision-making with reasoning and game theory principles
- Multi-variant Nim support (standard, misère, fibonacci, etc.)
- Comprehensive game state evaluation and winning position detection
- Advanced AI decision-making for optimal strategic gameplay

Examples:
    Basic move representation::\n

        move = NimMove(
            pile_index=0,
            stones_taken=3,
            player="Player1"
        )
        print(str(move))  # Output: "Player1 takes 3 stones from pile 0"

    Strategic analysis with nimber theory::\n

        analysis = NimAnalysis(
            nim_sum=5,
            position_evaluation="winning",
            recommended_move=optimal_move,
            explanation="Position has nim-sum 5, making it a winning position",
            winning_strategy="Force nim-sum to 0 for opponent",
            mathematical_proof="By Sprague-Grundy theorem, non-zero nim-sum indicates winning position"
        )

    Game variant configuration::\n

        variant = NimVariant(
            name="Misère Nim",
            rule_modification="Last player to move loses",
            strategy_differences="Endgame strategy reverses in single-stone piles"
        )

    Multi-pile position analysis::\n

        position = NimPosition(
            piles=[7, 5, 3, 1],
            current_player="Player1",
            moves_remaining=16,
            position_type="complex"
        )

Note:
    All models use Pydantic for validation and support both JSON serialization
    and integration with LLM-based strategic analysis systems for advanced gameplay.
"""


class NimVariant(str, Enum):
    """Enumeration of Nim game variants and rule modifications.

    Defines different variants of Nim with their specific rules and strategic
    considerations, affecting optimal play strategies and analysis approaches.

    Values:
        STANDARD: Classic Nim rules (last player to move wins)
        MISERE: Misère Nim (last player to move loses)
        FIBONACCI: Fibonacci Nim (can only take 1 or 2 stones)
        KAYLES: Kayles variant (splitting piles allowed)
        SUBTRACTION: Subtraction game (limited move set)

    """

    STANDARD = "standard"
    MISERE = "misere"
    FIBONACCI = "fibonacci"
    KAYLES = "kayles"
    SUBTRACTION = "subtraction"


class PositionType(str, Enum):
    """Enumeration of Nim position types for strategic analysis.

    Categorizes positions based on their strategic characteristics and
    complexity, helping guide appropriate analysis approaches.

    Values:
        SIMPLE: Simple endgame position (1-2 piles)
        COMPLEX: Complex midgame position (3+ piles)
        CRITICAL: Critical position requiring precise calculation
        TRIVIAL: Trivial position with obvious moves

    """

    SIMPLE = "simple"
    COMPLEX = "complex"
    CRITICAL = "critical"
    TRIVIAL = "trivial"


class NimMove(BaseModel):
    r"""Comprehensive representation of a Nim move with strategic context and validation.

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

    Attributes:
        pile_index (int): Index of the pile to take stones from (0-based indexing).
            Must be a valid pile index within the current game state.
        stones_taken (int): Number of stones to take from the specified pile.
            Must be positive and not exceed the pile size.
        player (str): Name or identifier of the player making the move.
            Used for game history and strategic analysis tracking.
        reasoning (Optional[str]): Strategic reasoning behind the move choice.
            Provides context for decision-making and learning analysis.
        move_quality (Optional[str]): Assessment of move quality for analysis.
            Categorizes moves as optimal, good, poor, or blunder.
        alternative_moves (List[Dict[str, int]]): Other moves considered.
            Shows depth of strategic analysis and decision-making process.
        time_taken (Optional[float]): Time taken to make the move in seconds.
            Useful for performance analysis and time management.

    Examples:
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

    Note:
        Move validation should be performed by the game state manager to ensure
        moves comply with Nim rules and current pile configurations.

    """

    pile_index: int = Field(
        ...,
        ge=0,
        description="Index of the pile to take stones from (0-based indexing)",
        examples=[0, 1, 2, 3, 4],
    )

    stones_taken: int = Field(
        ...,
        ge=1,
        description="Number of stones to take from the specified pile (must be positive)",
        examples=[1, 2, 3, 5, 10],
    )

    player: str = Field(
        ...,
        min_length=1,
        max_length=50,
        description="Name or identifier of the player making the move",
        examples=["Player1", "AliceAI", "BobBot", "Human"],
    )

    reasoning: str | None = Field(
        default=None,
        max_length=500,
        description="Strategic reasoning behind the move choice for analysis and learning",
        examples=[
            "Forcing nim-sum to 0 to put opponent in losing position",
            "Taking all stones from largest pile to simplify position",
            "Creating symmetric position to maintain winning advantage",
        ],
    )

    move_quality: Literal["optimal", "good", "poor", "blunder"] | None = Field(
        default=None,
        description="Assessment of move quality for strategic analysis",
        examples=["optimal", "good", "poor", "blunder"],
    )

    alternative_moves: list[dict[str, int]] = Field(
        default_factory=list,
        description="Other moves considered during decision-making process",
        examples=[
            [
                {"pile_index": 0, "stones_taken": 1},
                {"pile_index": 1, "stones_taken": 3},
            ],
            [{"pile_index": 2, "stones_taken": 2}],
        ],
    )

    time_taken: float | None = Field(
        default=None,
        ge=0.0,
        description="Time taken to make the move in seconds",
        examples=[1.5, 2.3, 10.7, 0.1],
    )

    @field_validator("alternative_moves")
    @classmethod
    def validate_alternative_moves(
        cls, v: list[dict[str, int]]
    ) -> list[dict[str, int]]:
        """Validate alternative moves have required fields.

        Args:
            v (List[Dict[str, int]]): List of alternative moves to validate.

        Returns:
            List[Dict[str, int]]: Validated alternative moves.

        Raises:
            ValueError: If alternative moves are malformed.

        """
        for move in v:
            if not isinstance(move, dict):
                raise ValueError("Alternative moves must be dictionaries")
            if "pile_index" not in move or "stones_taken" not in move:
                raise ValueError(
                    "Alternative moves must have 'pile_index' and 'stones_taken' fields"
                )
            if not isinstance(move["pile_index"], int) or move["pile_index"] < 0:
                raise ValueError("pile_index must be a non-negative integer")
            if not isinstance(move["stones_taken"], int) or move["stones_taken"] < 1:
                raise ValueError("stones_taken must be a positive integer")
        return v

    @computed_field
    @property
    def move_notation(self) -> str:
        """Generate algebraic notation for the move.

        Returns:
            str: Move in algebraic notation format (e.g., "P0-3" for pile 0, take 3).

        """
        return f"P{self.pile_index}-{self.stones_taken}"

    @computed_field
    @property
    def has_strategic_context(self) -> bool:
        """Check if move includes strategic analysis context.

        Returns:
            bool: True if move includes reasoning or quality assessment.

        """
        return self.reasoning is not None or self.move_quality is not None

    def __str__(self) -> str:
        r"""Generate human-readable string representation of the move.

        Returns:
            str: Formatted move description including player and action.

        Examples:
            Basic move format::\n

                move = NimMove(pile_index=0, stones_taken=3, player="Player1")
                print(str(move))  # Output: "Player1 takes 3 stones from pile 0"

            Move with quality assessment::\n

                move = NimMove(
                    pile_index=1, stones_taken=2, player="AI",
                    move_quality="optimal"
                )
                print(str(move))  # Output: "AI takes 2 stones from pile 1 (optimal)"

        """
        base_str = f"{self.player} takes {self.stones_taken} stones from pile {
            self.pile_index
        }"
        if self.move_quality:
            base_str += f" ({self.move_quality})"
        return base_str


class NimAnalysis(BaseModel):
    r"""Advanced strategic analysis model for Nim positions with mathematical rigor.

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

    Attributes:
        nim_sum (int): Binary XOR sum of all pile sizes (nimber value).
            Fundamental value for determining position type and optimal play.
        position_evaluation (Literal): Classification of position strength.
            Determines whether position is winning, losing, or drawn.
        recommended_move (NimMove): Optimal move based on mathematical analysis.
            Move that maintains or achieves winning position when possible.
        explanation (str): Detailed explanation of the strategic analysis.
            Educational content explaining the reasoning and mathematics.
        winning_strategy (str): High-level strategy for winning from this position.
            Strategic guidance for maintaining advantage or fighting for draws.
        mathematical_proof (Optional[str]): Mathematical justification for analysis.
            Formal proof or theorem application supporting the conclusion.
        alternative_moves (List[NimMove]): Other strong moves considered.
            Shows depth of analysis and strategic alternatives.
        position_complexity (PositionType): Categorization of position difficulty.
            Helps guide analysis depth and computational requirements.
        variant_considerations (Optional[str]): Special considerations for game variants.
            Adaptations needed for misère, fibonacci, or other Nim variants.

    Examples:
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

    Note:
        This model provides structured analysis output for strategic decision-making
        and supports both human-readable explanations and automated analysis systems.

    """

    nim_sum: int = Field(
        ...,
        ge=0,
        description="Binary XOR sum of all pile sizes (nimber value) - fundamental for optimal play",
        examples=[0, 1, 3, 5, 7, 15],
    )

    position_evaluation: Literal["winning", "losing", "drawn", "complex"] = Field(
        ...,
        description="Strategic classification of position strength from current player's perspective",
        examples=["winning", "losing", "drawn", "complex"],
    )

    recommended_move: NimMove = Field(
        ...,
        description="Optimal move based on mathematical analysis and strategic principles",
    )

    explanation: str = Field(
        ...,
        min_length=20,
        max_length=1000,
        description="Detailed explanation of the strategic analysis with mathematical reasoning",
        examples=[
            "Position has nim-sum 5, making it a winning position. To maintain advantage, reduce pile 2 by 4 stones.",
            "Nim-sum is 0, indicating a losing position. Best try is to take all stones from largest pile.",
            "Complex endgame position requiring precise calculation of parity and remaining moves.",
        ],
    )

    winning_strategy: str = Field(
        ...,
        min_length=10,
        max_length=500,
        description="High-level strategy for winning or achieving best result from this position",
        examples=[
            "Force nim-sum to 0 for opponent to maintain winning advantage",
            "Look for opponent mistakes and maintain symmetry when possible",
            "Count total stones and analyze parity in misère endgame",
        ],
    )

    mathematical_proof: str | None = Field(
        default=None,
        max_length=800,
        description="Mathematical justification or theorem application supporting the analysis",
        examples=[
            "By Sprague-Grundy theorem, nim-sum 0 is a P-position (losing for current player)",
            "Theorem: All positions with nim-sum ≠ 0 are N-positions (winning for current player)",
            "Misère theorem: Strategy changes when all piles have size ≤ 1",
        ],
    )

    alternative_moves: list[NimMove] = Field(
        default_factory=list,
        description="Other strong moves considered during analysis showing strategic depth",
    )

    position_complexity: PositionType = Field(
        default=PositionType.SIMPLE,
        description="Categorization of position difficulty for analysis depth guidance",
    )

    variant_considerations: str | None = Field(
        default=None,
        max_length=300,
        description="Special considerations for game variants (misère, fibonacci, etc.)",
        examples=[
            "Misère rule reverses strategy when all piles have size ≤ 1",
            "Fibonacci Nim limits moves to 1 or 2 stones per turn",
            "Kayles variant allows pile splitting which changes optimal strategy",
        ],
    )

    @computed_field
    @property
    def is_winning_position(self) -> bool:
        """Determine if current position is winning for the active player.

        Returns:
            bool: True if position is winning, False otherwise.

        """
        return self.position_evaluation == "winning"

    @computed_field
    @property
    def analysis_confidence(self) -> Literal["high", "medium", "low"]:
        """Assess confidence level of the analysis.

        Returns:
            Literal: Confidence level based on position complexity and proof strength.

        """
        if self.mathematical_proof and self.position_complexity in [
            PositionType.SIMPLE,
            PositionType.TRIVIAL,
        ]:
            return "high"
        elif self.position_complexity == PositionType.COMPLEX:
            return "medium"
        else:
            return "low"

    @computed_field
    @property
    def strategic_summary(self) -> dict[str, str | int | bool]:
        """Generate concise strategic summary.

        Returns:
            Dict[str, Union[str, int, bool]]: Key strategic insights and metrics.

        """
        return {
            "nim_sum": self.nim_sum,
            "position_type": self.position_evaluation,
            "is_winning": self.is_winning_position,
            "complexity": self.position_complexity.value,
            "confidence": self.analysis_confidence,
            "has_proof": self.mathematical_proof is not None,
            "alternative_count": len(self.alternative_moves),
        }

    def __str__(self) -> str:
        r"""Generate human-readable string representation of the analysis.

        Returns:
            str: Formatted analysis summary with key insights.

        Examples:
            Basic analysis format::\n

                analysis = NimAnalysis(...)
                print(str(analysis))
                # Output: "Analysis: winning position (nim-sum: 5) - Force nim-sum to 0 for opponent"

            Complex analysis with proof::\n

                analysis = NimAnalysis(mathematical_proof="By Sprague-Grundy theorem...")
                print(str(analysis))
                # Output: "Analysis: losing position (nim-sum: 0) - Mathematical proof available"

        """
        proof_indicator = (
            " - Mathematical proof available" if self.mathematical_proof else ""
        )
        return f"Analysis: {self.position_evaluation} position (nim-sum: {
            self.nim_sum
        }) - {self.winning_strategy}{proof_indicator}"

    model_config = {"arbitrary_types_allowed": True}
