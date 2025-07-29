"""Comprehensive state management system for Fox and Geese gameplay and
strategic analysis.

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

Examples:
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

Note:
    All state models use Pydantic v2 for validation and support both JSON
    serialization and integration with LangGraph for distributed gameplay.
"""

from typing import Any, Literal

from pydantic import (
    ConfigDict,
    Field,
    computed_field,
    field_serializer,
    field_validator,
)

from haive.games.fox_and_geese.models import FoxAndGeeseMove, FoxAndGeesePosition
from haive.games.framework.base.state import GameState


class FoxAndGeeseState(GameState):
    """Comprehensive state management for Fox and Geese gameplay with strategic
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

    Attributes:
        players (List[str]): Fixed list of players ["fox", "geese"].
            Maintains consistent player identification.
        fox_position (FoxAndGeesePosition): Current position of the fox piece.
            Tracked with full coordinate validation.
        geese_positions (Set[FoxAndGeesePosition]): Current positions of all geese.
            Maintained as a set for efficient position queries.
        turn (Literal["fox", "geese"]): Current player's turn.
            Alternates between fox and geese players.
        game_status (Literal): Current game state with completion detection.
            Tracks ongoing play and victory conditions.
        move_history (List[FoxAndGeeseMove]): Complete chronological move history.
            Includes all moves made during the game.
        winner (Optional[str]): Winner identifier if game completed.
            Set when victory conditions are met.
        num_geese (int): Current number of geese remaining on the board.
            Updated when geese are captured by the fox.
        fox_analysis (List[str]): Strategic analysis history for fox player.
            Tracks reasoning and decision-making patterns.
        geese_analysis (List[str]): Strategic analysis history for geese player.
            Tracks reasoning and decision-making patterns.

    Examples:
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

    Note:
        The state uses Pydantic v2 for validation and supports both JSON serialization
        and integration with LangGraph for distributed game systems. All position
        operations maintain game rule consistency and strategic context.
    """

    model_config = ConfigDict(arbitrary_types_allowed=True, validate_assignment=True)

    players: list[str] = Field(
        default=["fox", "geese"],
        description="Fixed list of players in the asymmetric game",
    )
    fox_position: FoxAndGeesePosition = Field(
        ..., description="Current position of the fox piece with coordinate validation"
    )
    geese_positions: set[FoxAndGeesePosition] = Field(
        ...,
        description="Current positions of all geese pieces (set for efficient queries)",
    )
    turn: Literal["fox", "geese"] = Field(
        ..., description="Current player's turn (alternates between fox and geese)"
    )
    game_status: Literal["ongoing", "fox_win", "geese_win"] = Field(
        default="ongoing",
        description="Current game state with victory condition detection",
    )
    move_history: list[FoxAndGeeseMove] = Field(
        default_factory=list,
        description="Complete chronological history of all moves made",
    )
    winner: str | None = Field(
        default=None, description="Winner identifier if game completed, None if ongoing"
    )
    num_geese: int = Field(
        default=0, ge=0, description="Current number of geese remaining on the board"
    )
    fox_analysis: list[str] = Field(
        default_factory=list,
        description="Strategic analysis history for fox player with reasoning patterns",
    )
    geese_analysis: list[str] = Field(
        default_factory=list,
        description="Strategic analysis history for geese player with reasoning patterns",
    )

    @field_validator("geese_positions", mode="before")
    @classmethod
    def validate_geese_positions(cls, v: Any) -> set[FoxAndGeesePosition]:
        """Validate and convert geese positions to a set."""
        if v is None:
            return set()

        if isinstance(v, set):
            # Already a set, but ensure all items are FoxAndGeesePosition
            return {
                (
                    FoxAndGeesePosition.model_validate(pos)
                    if isinstance(pos, dict)
                    else pos
                )
                for pos in v
            }

        if isinstance(v, list):
            # Convert from list of dicts to set of FoxAndGeesePosition objects
            return {
                (
                    FoxAndGeesePosition.model_validate(pos)
                    if isinstance(pos, dict)
                    else pos
                )
                for pos in v
            }

        # Handle single position
        if isinstance(v, dict):
            return {FoxAndGeesePosition.model_validate(v)}

        if isinstance(v, FoxAndGeesePosition):
            return {v}

        # Default to empty set if we can't parse
        return set()

    @field_validator("fox_position", mode="before")
    @classmethod
    def validate_fox_position(cls, v: Any) -> FoxAndGeesePosition:
        """Validate and convert fox position."""
        if v is None:
            # Default fox position at center
            return FoxAndGeesePosition(row=3, col=3)

        if isinstance(v, dict):
            return FoxAndGeesePosition.model_validate(v)

        if isinstance(v, FoxAndGeesePosition):
            return v

        # Default to center if we can't parse
        return FoxAndGeesePosition(row=3, col=3)

    @field_validator("move_history", mode="before")
    @classmethod
    def validate_move_history(cls, v: Any) -> list[FoxAndGeeseMove]:
        """Validate and convert move history."""
        if v is None:
            return []

        if isinstance(v, list):
            return [
                FoxAndGeeseMove.model_validate(move) if isinstance(move, dict) else move
                for move in v
            ]

        return []

    @field_serializer("geese_positions")
    def serialize_geese_positions(
        self, geese_positions: set[FoxAndGeesePosition]
    ) -> list[dict[str, Any]]:
        """Serialize geese positions as a list of dictionaries."""
        return [pos.model_dump() for pos in geese_positions]

    @field_serializer("fox_position")
    def serialize_fox_position(
        self, fox_position: FoxAndGeesePosition
    ) -> dict[str, Any]:
        """Serialize fox position as a dictionary."""
        return fox_position.model_dump()

    @field_serializer("move_history")
    def serialize_move_history(
        self, move_history: list[FoxAndGeeseMove]
    ) -> list[dict[str, Any]]:
        """Serialize move history as a list of dictionaries."""
        return [move.model_dump() for move in move_history]

    @classmethod
    def initialize(cls) -> "FoxAndGeeseState":
        """Initialize a new Fox and Geese game."""
        # Fox starts at the center
        fox_position = FoxAndGeesePosition(row=3, col=3)

        # Geese start at the top
        geese_positions = set()
        for col in range(7):
            if col % 2 == 0:  # Only on white squares
                geese_positions.add(FoxAndGeesePosition(row=0, col=col))
                geese_positions.add(FoxAndGeesePosition(row=1, col=col))

        return cls(
            fox_position=fox_position,
            geese_positions=geese_positions,
            turn="fox",  # Fox goes first
            game_status="ongoing",
            move_history=[],
            num_geese=len(geese_positions),
            fox_analysis=[],
            geese_analysis=[],
        )

    @property
    def board_string(self) -> str:
        """Get a string representation of the board."""
        # Create an empty 7x7 board
        board = [[" " for _ in range(7)] for _ in range(7)]

        # Place the fox
        if self.fox_position:
            board[self.fox_position.row][self.fox_position.col] = "F"

        # Place the geese
        for goose in self.geese_positions:
            board[goose.row][goose.col] = "G"

        # Convert to string
        result = "  0 1 2 3 4 5 6\n"
        for i, row in enumerate(board):
            result += f"{i} {' '.join(row)}\n"

        return result

    @computed_field
    @property
    def fox_mobility_score(self) -> float:
        """Calculate fox mobility score based on available moves.

        Returns:
            float: Mobility score from 0.0 (trapped) to 1.0 (maximum mobility).
        """
        # Check adjacent positions for movement options
        adjacent_positions = [
            (self.fox_position.row - 1, self.fox_position.col),
            (self.fox_position.row + 1, self.fox_position.col),
            (self.fox_position.row, self.fox_position.col - 1),
            (self.fox_position.row, self.fox_position.col + 1),
        ]

        valid_moves = 0
        for row, col in adjacent_positions:
            if (
                0 <= row < 7
                and 0 <= col < 7
                and FoxAndGeesePosition(row=row, col=col) not in self.geese_positions
            ):
                valid_moves += 1

        return valid_moves / 4.0  # Normalize to 0-1 range

    @computed_field
    @property
    def fox_escape_distance(self) -> int:
        """Calculate minimum distance for fox to reach escape edge.

        Returns:
            int: Minimum number of moves to reach the opposite edge.
        """
        # Fox escapes by reaching row 0 (starting from center)
        return self.fox_position.row

    @computed_field
    @property
    def geese_formation_strength(self) -> float:
        """Calculate geese formation strength for blocking fox.

        Returns:
            float: Formation strength from 0.0 (weak) to 1.0 (strong).
        """
        if not self.geese_positions:
            return 0.0

        # Check how well geese form a blocking line
        geese_rows = [pos.row for pos in self.geese_positions]

        # Formation is stronger when geese are in a line ahead of fox
        avg_row = sum(geese_rows) / len(geese_rows)
        formation_score = 1.0 - (abs(avg_row - self.fox_position.row) / 7.0)

        return max(0.0, min(1.0, formation_score))

    @computed_field
    @property
    def total_captures(self) -> int:
        """Count total number of geese captured by fox.

        Returns:
            int: Number of geese captured during the game.
        """
        # Calculate from initial geese count minus current count
        initial_geese = 8  # Standard starting number
        return initial_geese - self.num_geese

    @computed_field
    @property
    def game_statistics(self) -> dict[str, int | float | str]:
        """Generate comprehensive game statistics.

        Returns:
            Dict[str, Union[int, float, str]]: Game statistics and metrics.
        """
        total_moves = len(self.move_history)
        fox_moves = sum(1 for move in self.move_history if move.piece_type == "fox")
        geese_moves = total_moves - fox_moves

        return {
            "total_moves": total_moves,
            "fox_moves": fox_moves,
            "geese_moves": geese_moves,
            "captures": self.total_captures,
            "capture_rate": (
                (self.total_captures / total_moves * 100) if total_moves > 0 else 0
            ),
            "fox_mobility": self.fox_mobility_score,
            "geese_formation": self.geese_formation_strength,
            "escape_distance": self.fox_escape_distance,
            "game_phase": (
                "endgame"
                if self.num_geese < 4
                else "midgame" if self.num_geese < 6 else "opening"
            ),
        }

    @computed_field
    @property
    def position_evaluation(self) -> dict[str, str | float]:
        """Generate strategic position evaluation.

        Returns:
            Dict[str, Union[str, float]]: Position evaluation metrics.
        """
        fox_advantage = (
            self.fox_mobility_score * 0.4 + (1.0 - self.fox_escape_distance / 7.0) * 0.6
        )
        geese_advantage = (
            self.geese_formation_strength * 0.6 + (self.num_geese / 8.0) * 0.4
        )

        if fox_advantage > geese_advantage + 0.2:
            evaluation = "Fox advantage"
        elif geese_advantage > fox_advantage + 0.2:
            evaluation = "Geese advantage"
        else:
            evaluation = "Balanced position"

        return {
            "fox_advantage": fox_advantage,
            "geese_advantage": geese_advantage,
            "evaluation": evaluation,
            "mobility_score": self.fox_mobility_score,
            "formation_score": self.geese_formation_strength,
            "capture_threat": self.total_captures / 8.0,
        }

    def get_latest_fox_analysis(self) -> str | None:
        """Get the latest strategic analysis for fox player.

        Returns:
            Optional[str]: Latest fox analysis or None if no analysis exists.
        """
        return self.fox_analysis[-1] if self.fox_analysis else None

    def get_latest_geese_analysis(self) -> str | None:
        """Get the latest strategic analysis for geese player.

        Returns:
            Optional[str]: Latest geese analysis or None if no analysis exists.
        """
        return self.geese_analysis[-1] if self.geese_analysis else None

    def get_recent_moves(self, count: int) -> list[FoxAndGeeseMove]:
        """Get the most recent moves from the game history.

        Args:
            count (int): Number of recent moves to return.

        Returns:
            List[FoxAndGeeseMove]: List of recent moves (up to count).
        """
        return self.move_history[-count:] if self.move_history else []

    def is_game_over(self) -> bool:
        """Check if the game is over.

        Returns:
            bool: True if game is over, False otherwise.
        """
        return self.game_status != "ongoing"

    def model_dump(self, **kwargs) -> dict[str, Any]:
        """Override model_dump to ensure proper serialization."""
        # Get the base dump
        data = super().model_dump(**kwargs)

        # Ensure geese_positions is properly serialized
        if "geese_positions" in data and isinstance(data["geese_positions"], set):
            data["geese_positions"] = [
                pos.model_dump() if hasattr(pos, "model_dump") else pos
                for pos in data["geese_positions"]
            ]

        # Ensure fox_position is properly serialized
        if "fox_position" in data and hasattr(data["fox_position"], "model_dump"):
            data["fox_position"] = data["fox_position"].model_dump()

        # Ensure move_history is properly serialized
        if "move_history" in data and isinstance(data["move_history"], list):
            data["move_history"] = [
                move.model_dump() if hasattr(move, "model_dump") else move
                for move in data["move_history"]
            ]

        return data

    @classmethod
    def model_validate(cls, obj: Any, **kwargs) -> "FoxAndGeeseState":
        """Override model_validate to handle various input formats."""
        if isinstance(obj, cls):
            return obj

        if isinstance(obj, dict):
            # Handle nested state structures (common in LangGraph)
            if "game_state" in obj and isinstance(obj["game_state"], dict):
                return cls.model_validate(obj["game_state"], **kwargs)

            # Validate the dict directly
            return super().model_validate(obj, **kwargs)

        # Fall back to default validation
        return super().model_validate(obj, **kwargs)

    def __str__(self) -> str:
        """String representation of the game state."""
        return f"FoxAndGeeseState(turn={self.turn}, status={self.game_status}, geese={self.num_geese})"

    def __repr__(self) -> str:
        """Detailed string representation of the game state."""
        return (
            f"FoxAndGeeseState(fox_pos={self.fox_position}, geese_count={self.num_geese}, "
            f"turn={self.turn}, status={self.game_status}, moves={len(self.move_history)})"
        )
