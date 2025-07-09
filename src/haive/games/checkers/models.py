"""Comprehensive data models for strategic Checkers gameplay and analysis.

This module provides sophisticated data models for the classic game of Checkers
(also known as Draughts), supporting both traditional gameplay and advanced
strategic analysis. The models enable structured data handling throughout the
Checkers game implementation and provide strong typing for LLM-based components.

The models support:
- Complete move representation with algebraic notation
- Strategic decision-making with reasoning and alternatives
- Advanced position analysis with material and positional evaluation
- Multi-jump sequences and king promotion mechanics
- Comprehensive game state tracking and validation

Examples:
    Basic move representation::\n

        move = CheckersMove(
            from_position="a3",
            to_position="b4",
            player="red",
            is_jump=False
        )
        print(str(move))  # Output: "a3-b4"

    Jump move with capture::\n

        jump = CheckersMove(
            from_position="c3",
            to_position="e5",
            player="black",
            is_jump=True,
            captured_position="d4"
        )
        print(str(jump))  # Output: "c3xe5"

    Strategic decision-making::\n

        decision = CheckersPlayerDecision(
            move=move,
            reasoning="Advancing toward king row while maintaining material advantage",
            evaluation="Favorable position with strong center control",
            alternatives=["a3-b4", "c3-d4", "e3-f4"]
        )

    Position analysis::\n

        analysis = CheckersAnalysis(
            material_advantage="Red: 10 pieces, Black: 8 pieces (+2 material)",
            control_of_center="Red controls 3/4 center squares",
            suggested_moves=["e3-f4", "c3-d4", "g3-h4"],
            positional_evaluation="Red has winning advantage"
        )

Note:
    All models use Pydantic for validation and support both JSON serialization
    and integration with LLM-based strategic analysis systems.
"""

from typing import Dict, List, Literal, Optional, Union

from pydantic import BaseModel, Field, computed_field, field_validator


class CheckersMove(BaseModel):
    """Comprehensive representation of a Checkers move with strategic context.

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

    Attributes:
        from_position (str): Starting position in algebraic notation (e.g., "a3").
            Uses standard checkers notation with columns a-h and rows 1-8.
        to_position (str): Ending position in algebraic notation (e.g., "b4").
            Must be a valid diagonal move according to Checkers rules.
        player (Literal["red", "black"]): The player making the move.
            Red typically starts first in standard Checkers gameplay.
        is_jump (bool): Whether this is a jump move capturing an opponent's piece.
            Jump moves are mandatory when available according to Checkers rules.
        captured_position (Optional[str]): Position of the captured piece if any.
            Required when is_jump=True, indicates the captured piece's location.

    Examples:
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

    Note:
        Move validation should be performed by the game state manager to ensure
        moves comply with Checkers rules and current board configuration.
    """

    from_position: str = Field(
        ...,
        min_length=2,
        max_length=2,
        description="Starting position in algebraic notation (e.g., 'a3')",
        examples=["a3", "b4", "c5", "d6", "e7", "f8", "g1", "h2"],
    )

    to_position: str = Field(
        ...,
        min_length=2,
        max_length=2,
        description="Ending position in algebraic notation (e.g., 'b4')",
        examples=["a3", "b4", "c5", "d6", "e7", "f8", "g1", "h2"],
    )

    player: Literal["red", "black"] = Field(
        ...,
        description="Player making the move (red typically starts first)",
        examples=["red", "black"],
    )

    is_jump: bool = Field(
        default=False,
        description="Whether this is a jump move capturing an opponent's piece",
        examples=[True, False],
    )

    captured_position: Optional[str] = Field(
        default=None,
        min_length=2,
        max_length=2,
        description="Position of captured piece if this is a jump move",
        examples=["b4", "d4", "f4", "h4", "a5", "c5", "e5", "g5"],
    )

    @field_validator("from_position", "to_position")
    @classmethod
    def validate_position_format(cls, v: str) -> str:
        """Validate that position follows algebraic notation format.

        Args:
            v (str): Position string to validate.

        Returns:
            str: Validated position string.

        Raises:
            ValueError: If position format is invalid.
        """
        if len(v) != 2:
            raise ValueError("Position must be exactly 2 characters (e.g., 'a3')")

        column, row = v[0], v[1]
        if column not in "abcdefgh":
            raise ValueError("Column must be a letter from 'a' to 'h'")
        if row not in "12345678":
            raise ValueError("Row must be a number from '1' to '8'")

        return v.lower()

    @field_validator("captured_position")
    @classmethod
    def validate_captured_position(cls, v: Optional[str], values) -> Optional[str]:
        """Validate captured position is provided when move is a jump.

        Args:
            v (Optional[str]): Captured position to validate.
            values: Other field values for validation context.

        Returns:
            Optional[str]: Validated captured position.

        Raises:
            ValueError: If captured position is invalid for jump moves.
        """
        if v is not None:
            if len(v) != 2:
                raise ValueError("Captured position must be exactly 2 characters")
            column, row = v[0], v[1]
            if column not in "abcdefgh" or row not in "12345678":
                raise ValueError("Captured position must use valid algebraic notation")
            return v.lower()
        return v

    def __str__(self) -> str:
        """Generate standard Checkers notation for the move.

        Produces move notation following standard Checkers conventions:
        - Regular moves: "a3-b4"
        - Jump moves: "a3xc5"
        - Multi-jump sequences: "a3xc5xe7"

        Returns:
            str: The move in standard Checkers notation format.

        Examples:
            Regular move notation::\n

                move = CheckersMove(from_position="a3", to_position="b4", player="red")
                print(str(move))  # Output: "a3-b4"

            Jump move notation::\n

                jump = CheckersMove(
                    from_position="c3", to_position="e5", player="black",
                    is_jump=True, captured_position="d4"
                )
                print(str(jump))  # Output: "c3xe5"
        """
        if self.is_jump:
            return f"{self.from_position}x{self.to_position}"
        return f"{self.from_position}-{self.to_position}"

    @computed_field
    @property
    def move_distance(self) -> int:
        """Calculate the distance of the move in squares.

        Returns:
            int: Distance moved in board squares (1 for regular moves, 2+ for jumps).
        """
        from_col = ord(self.from_position[0]) - ord("a")
        from_row = int(self.from_position[1]) - 1
        to_col = ord(self.to_position[0]) - ord("a")
        to_row = int(self.to_position[1]) - 1

        return max(abs(to_col - from_col), abs(to_row - from_row))


class CheckersPlayerDecision(BaseModel):
    """Comprehensive decision model for strategic Checkers gameplay.

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

    Attributes:
        move (CheckersMove): The chosen move with complete position information.
            Must be a valid move according to current board state.
        reasoning (str): Detailed reasoning for the move choice including strategic
            considerations, tactical analysis, and long-term planning.
        evaluation (str): Comprehensive position evaluation including material
            balance, positional advantages, and strategic outlook.
        alternatives (List[str]): List of alternative moves considered in algebraic
            notation, showing depth of strategic analysis.

    Examples:
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

    Note:
        This model is designed for structured output from LLM-based player engines
        and provides comprehensive strategic context for move analysis.
    """

    move: CheckersMove = Field(
        ..., description="The chosen move with complete position and player information"
    )

    reasoning: str = Field(
        ...,
        min_length=10,
        max_length=500,
        description="Detailed strategic reasoning for the move choice including tactical analysis",
        examples=[
            "Advancing toward center to establish control while maintaining defensive formation",
            "Mandatory capture removes opponent's advanced piece and opens king row path",
            "Promoting to king provides backward movement capability and strategic flexibility",
        ],
    )

    evaluation: str = Field(
        ...,
        min_length=10,
        max_length=300,
        description="Comprehensive position evaluation including material balance and strategic outlook",
        examples=[
            "Slightly favorable position with improved piece mobility",
            "Significant material advantage with tactical initiative",
            "Decisive advantage with king piece on opponent's back rank",
        ],
    )

    alternatives: List[str] = Field(
        default_factory=list,
        description="List of alternative moves considered in algebraic notation",
        examples=[
            ["c3-d4", "e3-f4", "g3-h4"],
            ["a3-b4", "c3-d4"],
            [],  # No alternatives for mandatory moves
        ],
    )

    @field_validator("alternatives")
    @classmethod
    def validate_alternatives(cls, v: List[str]) -> List[str]:
        """Validate alternative moves use proper algebraic notation.

        Args:
            v (List[str]): List of alternative moves to validate.

        Returns:
            List[str]: Validated list of alternative moves.
        """
        for move in v:
            if "-" in move:
                # Regular move format: "a3-b4"
                parts = move.split("-")
                if len(parts) != 2:
                    raise ValueError(f"Invalid move format: {move}")
            elif "x" in move:
                # Jump move format: "a3xc5"
                parts = move.split("x")
                if len(parts) != 2:
                    raise ValueError(f"Invalid jump format: {move}")
            else:
                raise ValueError(f"Move must contain '-' or 'x': {move}")
        return v


class CheckersAnalysis(BaseModel):
    """Advanced strategic analysis model for Checkers position evaluation.

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

    Attributes:
        material_advantage (str): Detailed assessment of material balance including
            piece counts, king advantages, and positional piece values.
        control_of_center (str): Analysis of center control including square
            occupation, piece mobility, and territorial advantage.
        suggested_moves (List[str]): Prioritized list of recommended moves in
            algebraic notation with strategic reasoning.
        positional_evaluation (str): Overall position assessment including
            strategic outlook, winning chances, and key factors.

    Examples:
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

    Note:
        This model provides structured analysis output for strategic decision-making
        and supports both human-readable explanations and automated analysis.
    """

    material_advantage: str = Field(
        ...,
        min_length=10,
        max_length=200,
        description="Detailed assessment of material balance including piece counts and king advantages",
        examples=[
            "Equal material: Red 10 pieces, Black 10 pieces, Red has 1 king advantage",
            "Red ahead by 2 pieces (11 vs 9), material advantage increasing",
            "Red: 2 kings, Black: 1 king + 1 piece, Red has endgame advantage",
        ],
    )

    control_of_center: str = Field(
        ...,
        min_length=10,
        max_length=200,
        description="Analysis of center control including square occupation and territorial advantage",
        examples=[
            "Red controls 3 of 4 center squares with advanced piece formation",
            "Red dominates center with 4 pieces vs Black's 1",
            "Center control less relevant in endgame, focus on king activity",
        ],
    )

    suggested_moves: List[str] = Field(
        default_factory=list,
        description="Prioritized list of recommended moves in algebraic notation",
        examples=[
            ["e3-f4", "c3-d4", "g3-h4"],
            ["d4xf6", "b4xd6", "f4-g5"],
            ["Ka8-b7", "Kc6-d5", "Kc6-b5"],
        ],
    )

    positional_evaluation: str = Field(
        ...,
        min_length=10,
        max_length=300,
        description="Overall position assessment including strategic outlook and winning chances",
        examples=[
            "Slightly favorable for Red due to superior piece placement and king advantage",
            "Winning position for Red with multiple tactical threats",
            "Technical win for Red with proper king technique",
        ],
    )

    @computed_field
    @property
    def analysis_summary(self) -> Dict[str, Union[str, int]]:
        """Generate a concise summary of the analysis.

        Returns:
            Dict[str, Union[str, int]]: Summary containing key analysis points.
        """
        return {
            "material_status": self.material_advantage.split(",")[0],
            "center_control": self.control_of_center.split(",")[0],
            "move_count": len(self.suggested_moves),
            "position_assessment": self.positional_evaluation.split(",")[0],
        }
