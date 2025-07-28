"""Comprehensive data models for strategic Tic Tac Toe gameplay and positional
analysis.

This module provides sophisticated data models for the classic game of Tic Tac Toe,
supporting both traditional gameplay and advanced strategic analysis. The models
enable structured data handling throughout the game implementation and provide
strong typing for LLM-based components and strategic decision-making systems.

The models support:
- Complete move representation with coordinate validation
- Strategic analysis with winning/blocking move detection
- Fork opportunity identification for advanced play
- Position evaluation from game theory perspective
- Multi-level strategic recommendations
- Perfect play analysis and minimax integration

Examples:
    Basic move representation::

        move = TicTacToeMove(
            row=0,
            col=1,
            player="X"
        )
        print(str(move))  # Output: "X places at (0, 1)"

    Strategic position analysis::

        analysis = TicTacToeAnalysis(
            winning_moves=[{"row": 0, "col": 2}],
            blocking_moves=[{"row": 1, "col": 1}],
            fork_opportunities=[],
            center_available=False,
            corner_available=True,
            position_evaluation="winning",
            recommended_move={"row": 0, "col": 2},
            strategy="Win immediately by completing top row"
        )

    Fork creation analysis::

        analysis = TicTacToeAnalysis(
            winning_moves=[],
            blocking_moves=[],
            fork_opportunities=[{"row": 0, "col": 0}, {"row": 2, "col": 2}],
            center_available=False,
            corner_available=True,
            position_evaluation="uncleaf",
            recommended_move={"row": 0, "col": 0},
            strategy="Create fork with two winning threats"
        )

Note:
    All models use Pydantic for validation and support both JSON serialization
    and integration with LLM-based strategic analysis systems for perfect play.
"""

from typing import Dict, List, Literal, Optional

from pydantic import BaseModel, Field, computed_field, field_validator


class TicTacToeMove(BaseModel):
    """Comprehensive representation of a Tic Tac Toe move with validation and
    game context.

    This model provides complete representation of moves in Tic Tac Toe, supporting
    both basic gameplay and advanced strategic analysis. It includes coordinate
    validation, player identification, and integration with game state management
    for perfect play algorithms and educational systems.

    The model supports:
    - Coordinate validation for 3x3 grid constraints
    - Player symbol enforcement (X or O)
    - Move notation generation for game records
    - Integration with minimax and alpha-beta pruning
    - Educational move explanations
    - Tournament play recording standards

    Attributes:
        row (int): Row index (0-2) where the player places their symbol.
            Uses 0-based indexing with 0=top, 1=middle, 2=bottom.
        col (int): Column index (0-2) where the player places their symbol.
            Uses 0-based indexing with 0=left, 1=center, 2=right.
        player (Literal['X', 'O']): The symbol representing the player.
            'X' traditionally plays first, 'O' plays second.

    Examples:
        Basic move creation::

            move = TicTacToeMove(row=1, col=1, player="X")
            print(str(move))  # Output: "X places at (1, 1)"
            # This represents X playing in the center square

        Corner move for strategic play::

            corner_move = TicTacToeMove(row=0, col=0, player="X")
            # Opening corner move - classic strategic opening

        Blocking move example::

            block = TicTacToeMove(row=2, col=2, player="O")
            # O blocks X's potential diagonal win

        Educational notation::

            move = TicTacToeMove(row=0, col=2, player="X")
            # Top-right corner: strategic for controlling diagonals

    Note:
        Moves are validated to ensure coordinates are within the 3x3 grid.
        The string representation provides human-readable move descriptions.
    """

    row: int = Field(
        ...,
        ge=0,
        lt=3,
        description="Row index (0-2) with 0=top, 1=middle, 2=bottom",
        examples=[0, 1, 2],
    )

    col: int = Field(
        ...,
        ge=0,
        lt=3,
        description="Column index (0-2) with 0=left, 1=center, 2=right",
        examples=[0, 1, 2],
    )

    player: Literal["X", "O"] = Field(
        ...,
        description="Player symbol making the move (X plays first traditionally)",
        examples=["X", "O"],
    )

    @computed_field
    @property
    def board_position(self) -> str:
        """Get human-readable board position name.

        Returns:
            str: Position name like 'center', 'top-left corner', etc.
        """
        positions = [
            ["top-left corner", "top-center", "top-right corner"],
            ["middle-left", "center", "middle-right"],
            ["bottom-left corner", "bottom-center", "bottom-right corner"],
        ]
        return positions[self.row][self.col]

    @computed_field
    @property
    def is_corner(self) -> bool:
        """Check if this move is a corner position.

        Returns:
            bool: True if the move is in a corner (strategic positions).
        """
        return (self.row, self.col) in [(0, 0), (0, 2), (2, 0), (2, 2)]

    @computed_field
    @property
    def is_center(self) -> bool:
        """Check if this move is the center position.

        Returns:
            bool: True if the move is in the center (most valuable position).
        """
        return self.row == 1 and self.col == 1

    @computed_field
    @property
    def is_edge(self) -> bool:
        """Check if this move is an edge (non-corner, non-center) position.

        Returns:
            bool: True if the move is on an edge (weakest positions).
        """
        return not self.is_corner and not self.is_center

    def __str__(self) -> str:
        """Generate human-readable string representation of the move.

        Returns:
            str: Formatted move description with position details.

        Examples:
            >>> move = TicTacToeMove(row=1, col=1, player="X")
            >>> print(str(move))
            X places at (1, 1) - center

            >>> move = TicTacToeMove(row=0, col=0, player="O")
            >>> print(str(move))
            O places at (0, 0) - top-left corner
        """
        return (
            f"{self.player} places at ({self.row}, {self.col}) - {self.board_position}"
        )


class TicTacToeAnalysis(BaseModel):
    """Advanced strategic analysis model for Tic Tac Toe positions with game
    theory insights.

    This model provides comprehensive analysis of Tic Tac Toe positions using
    game theory principles, perfect play algorithms, and strategic heuristics.
    It supports both educational gameplay and competitive AI decision-making
    with detailed explanations of optimal strategies.

    The analysis includes:
    - Immediate win detection and threat assessment
    - Defensive move identification to prevent losses
    - Fork creation and prevention strategies
    - Positional advantage evaluation (center, corners, edges)
    - Game-theoretic position classification
    - Perfect play recommendations with explanations
    - Educational insights for learning optimal strategy

    Attributes:
        winning_moves (List[Dict[str, int]]): Coordinates that win immediately.
            Each dict contains 'row' and 'col' keys for winning positions.
        blocking_moves (List[Dict[str, int]]): Moves that must be played to prevent loss.
            Critical defensive moves to block opponent's winning threats.
        fork_opportunities (List[Dict[str, int]]): Moves creating multiple threats.
            Advanced positions that force opponent into defensive play.
        center_available (bool): Whether the center square (1,1) is unoccupied.
            Center control is crucial for optimal Tic Tac Toe strategy.
        corner_available (bool): Whether any corner square is unoccupied.
            Corners are second-best positions after center.
        position_evaluation (Literal): Game-theoretic evaluation of position.
            Classifications: winning, losing, drawing, unclear.
        recommended_move (Optional[Dict[str, int]]): Best move by perfect play.
            Computed using minimax algorithm with full game tree search.
        strategy (str): Natural language explanation of optimal strategy.
            Educational description for understanding the position.
        move_priority (Optional[int]): Priority ranking of recommended move.
            1=win, 2=block loss, 3=create fork, 4=block fork, 5=positional.
        optimal_outcome (Optional[Literal]): Expected result with perfect play.
            Predicts game outcome assuming both players play optimally.

    Examples:
        Winning position analysis::

            analysis = TicTacToeAnalysis(
                winning_moves=[{"row": 0, "col": 2}],
                blocking_moves=[],
                fork_opportunities=[],
                center_available=False,
                corner_available=False,
                position_evaluation="winning",
                recommended_move={"row": 0, "col": 2},
                strategy="Win immediately by completing the top row",
                move_priority=1,
                optimal_outcome="win"
            )

        Defensive position requiring blocking::

            analysis = TicTacToeAnalysis(
                winning_moves=[],
                blocking_moves=[{"row": 1, "col": 1}],
                fork_opportunities=[],
                center_available=True,
                corner_available=True,
                position_evaluation="losing",
                recommended_move={"row": 1, "col": 1},
                strategy="Must block opponent's winning threat in center",
                move_priority=2,
                optimal_outcome="draw"
            )

        Fork creation opportunity::

            analysis = TicTacToeAnalysis(
                winning_moves=[],
                blocking_moves=[],
                fork_opportunities=[{"row": 0, "col": 0}, {"row": 2, "col": 2}],
                center_available=False,
                corner_available=True,
                position_evaluation="uncleaf",
                recommended_move={"row": 0, "col": 0},
                strategy="Create fork with two winning threats - opponent cannot block both",
                move_priority=3,
                optimal_outcome="win"
            )

        Opening position analysis::

            analysis = TicTacToeAnalysis(
                winning_moves=[],
                blocking_moves=[],
                fork_opportunities=[],
                center_available=True,
                corner_available=True,
                position_evaluation="uncleaf",
                recommended_move={"row": 1, "col": 1},
                strategy="Control center for maximum strategic flexibility",
                move_priority=5,
                optimal_outcome="draw"
            )

    Note:
        This model provides the foundation for perfect Tic Tac Toe play.
        With optimal strategy, the game always ends in a draw.
    """

    winning_moves: List[Dict[str, int]] = Field(
        default_factory=list,
        description="List of winning moves (row, col) for immediate victory",
        examples=[[{"row": 0, "col": 2}], [{"row": 1, "col": 0}, {"row": 2, "col": 1}]],
    )

    blocking_moves: List[Dict[str, int]] = Field(
        default_factory=list,
        description="Critical defensive moves to prevent opponent's immediate win",
        examples=[[{"row": 1, "col": 1}], [{"row": 0, "col": 0}]],
    )

    fork_opportunities: List[Dict[str, int]] = Field(
        default_factory=list,
        description="Moves creating multiple winning threats simultaneously",
        examples=[[{"row": 0, "col": 0}, {"row": 2, "col": 2}]],
    )

    center_available: bool = Field(
        ...,
        description="Whether the center square (1,1) is unoccupied - most valuable position",
        examples=[True, False],
    )

    corner_available: bool = Field(
        ...,
        description="Whether any corner square is unoccupied - second-best positions",
        examples=[True, False],
    )

    position_evaluation: Literal["winning", "losing", "drawing", "unclear"] = Field(
        ...,
        description="Game-theoretic evaluation from current player's perspective",
        examples=["winning", "losing", "drawing", "unclear"],
    )

    recommended_move: Optional[Dict[str, int]] = Field(
        default=None,
        description="Optimal move computed by perfect play algorithm",
        examples=[{"row": 1, "col": 1}, {"row": 0, "col": 0}],
    )

    strategy: str = Field(
        ...,
        min_length=10,
        max_length=500,
        description="Natural language explanation of optimal strategy and reasoning",
        examples=[
            "Win immediately by completing the diagonal",
            "Must block opponent's winning threat in center",
            "Create fork to guarantee victory next turn",
            "Control center for maximum strategic options",
        ],
    )

    move_priority: Optional[int] = Field(
        default=None,
        ge=1,
        le=5,
        description="Priority ranking: 1=win, 2=block, 3=fork, 4=block fork, 5=positional",
        examples=[1, 2, 3, 4, 5],
    )

    optimal_outcome: Optional[Literal["win", "draw", "loss"]] = Field(
        default=None,
        description="Expected game outcome with perfect play from this position",
        examples=["win", "draw", "loss"],
    )

    @field_validator("winning_moves", "blocking_moves", "fork_opportunities")
    @classmethod
    def validate_move_coordinates(cls, v: List[Dict[str, int]]) -> List[Dict[str, int]]:
        """Validate that all move coordinates are within bounds.

        Args:
            v (List[Dict[str, int]]): List of move coordinates to validate.

        Returns:
            List[Dict[str, int]]: Validated move coordinates.

        Raises:
            ValueError: If coordinates are out of bounds.
        """
        for move in v:
            if "row" not in move or "col" not in move:
                raise ValueError("Each move must have 'row' and 'col' keys")
            if not (0 <= move["row"] <= 2 and 0 <= move["col"] <= 2):
                raise ValueError(
                    f"Invalid coordinates: row={move['row']}, col={move['col']}"
                )
        return v

    @computed_field
    @property
    def has_immediate_threat(self) -> bool:
        """Check if there's an immediate win or loss threat.

        Returns:
            bool: True if winning or blocking moves exist.
        """
        return len(self.winning_moves) > 0 or len(self.blocking_moves) > 0

    @computed_field
    @property
    def threat_level(self) -> str:
        """Assess the urgency level of the position.

        Returns:
            str: Threat level classification.
        """
        if self.winning_moves:
            return "critical-win"
        elif self.blocking_moves:
            return "critical-defense"
        elif self.fork_opportunities:
            return "strategic-advantage"
        else:
            return "positional-play"

    @computed_field
    @property
    def move_count(self) -> Dict[str, int]:
        """Count available moves by category.

        Returns:
            Dict[str, int]: Counts of different move types.
        """
        return {
            "winning": len(self.winning_moves),
            "blocking": len(self.blocking_moves),
            "forks": len(self.fork_opportunities),
            "total_critical": len(self.winning_moves) + len(self.blocking_moves),
        }

    model_config = {"arbitrary_types_allowed": True}
