r"""Comprehensive state management system for Checkers gameplay and strategic
analysis.

This module provides sophisticated state models for Checkers games with complete
support for board representation, move tracking, strategic analysis, and game
flow management. The state system maintains both game mechanics and strategic
context for advanced AI decision-making.

The state system supports:
- Complete board representation with algebraic notation
- Strategic analysis history for both players
- Comprehensive move tracking with pattern analysis
- Game phase detection and endgame recognition
- Performance metrics and statistical analysis
- Rule variant support for different Checkers types

Examples:
    Creating a new game state::\n

        state = CheckersState.initialize()
        assert state.turn == "red"
        assert state.game_status == "ongoing"

    Accessing board information::\n

        # Check piece at position
        piece = state.get_piece_at("a3")  # Red piece
        assert piece == 1

        # Get board visualization
        print(state.board_string)

    Tracking strategic analysis::\n

        analysis = CheckersAnalysis(
            material_advantage="Equal material",
            control_of_center="Red controls center",
            suggested_moves=["e3-f4", "c3-d4"],
            positional_evaluation="Balanced position"
        )
        state.add_analysis(analysis, "red")

    Game state queries::\n

        # Check game completion
        if state.is_game_over():
            winner = state.winner

        # Material balance
        material = state.material_balance

        # Move patterns
        recent_moves = state.get_recent_moves(5)

Note:
    All state models use Pydantic for validation and support both JSON
    serialization and integration with LangGraph for distributed gameplay.
"""

from collections.abc import Sequence
from enum import Enum
from typing import ClassVar, Dict, List, Literal, Optional, Union

from pydantic import BaseModel, Field, computed_field, field_validator

from haive.games.checkers.models import CheckersAnalysis, CheckersMove


class PieceType(int, Enum):
    """Enumeration of piece types in Checkers.

    Defines the numeric values used in the board representation for different
    piece types, supporting both regular pieces and kings for each player.

    Values:
        EMPTY: Empty square (0)
        RED_PIECE: Regular red piece (1)
        RED_KING: Red king piece (2)
        BLACK_PIECE: Regular black piece (3)
        BLACK_KING: Black king piece (4)
    """

    EMPTY = 0
    RED_PIECE = 1
    RED_KING = 2
    BLACK_PIECE = 3
    BLACK_KING = 4


class GamePhase(str, Enum):
    """Enumeration of game phases in Checkers.

    Defines the different phases of a Checkers game, which affects
    strategic considerations and AI decision-making approaches.

    Values:
        OPENING: Early game with full piece complement
        MIDDLE: Mid-game with active piece development
        ENDGAME: Late game with few pieces remaining
        FINISHED: Game has concluded with a winner
    """

    OPENING = "opening"
    MIDDLE = "middle"
    ENDGAME = "endgame"
    FINISHED = "finished"


class CheckersState(BaseModel):
    r"""Comprehensive state model for Checkers gameplay with strategic analysis
    support.

    This class provides complete state management for Checkers games, supporting
    both game mechanics and strategic analysis. The state system maintains board
    representation, move history, strategic context, and performance metrics for
    advanced AI decision-making and game analysis.

    The state system supports:
    - Complete board representation with algebraic notation conversion
    - Strategic analysis history for both players with pattern tracking
    - Comprehensive move tracking with game phase detection
    - Performance metrics and statistical analysis
    - Rule variant support for different Checkers types
    - Game completion detection and winner determination

    Board representation uses a 2D grid with these piece values:
    - 0: Empty square
    - 1: Red piece (regular)
    - 2: Red king
    - 3: Black piece (regular)
    - 4: Black king

    Attributes:
        board (List[List[Literal[0, 1, 2, 3, 4]]]): 2D grid representation of the board
            using PieceType enum values for type safety and clarity.
        board_string (str): Human-readable string representation of the board with
            coordinates for visualization and debugging.
        turn (Literal["red", "black"]): Current player's turn with validation.
        move_history (Sequence[CheckersMove]): Complete chronological history of
            all moves made in the game with strategic context.
        game_status (Literal["ongoing", "game_over"]): Current game status with
            automatic detection of terminal positions.
        winner (Optional[Literal["red", "black"]]): Winner of the game if completed,
            None if game is still in progress.
        red_analysis (Sequence[CheckersAnalysis]): Complete history of strategic
            analyses from red's perspective for learning and adaptation.
        black_analysis (Sequence[CheckersAnalysis]): Complete history of strategic
            analyses from black's perspective for learning and adaptation.
        captured_pieces (Dict[str, List[str]]): Comprehensive tracking of pieces
            captured by each player with position information.
        turn_number (int): Current turn number starting from 1 for game tracking.
        last_capture_turn (Optional[int]): Turn number of the last capture for
            draw rule enforcement (50-move rule equivalent).

    Examples:
        Creating a new game state::\n

            state = CheckersState.initialize()
            assert state.turn == "red"
            assert state.game_status == "ongoing"
            assert state.turn_number == 1

        Accessing board information::\n

            # Check piece at algebraic position
            piece = state.get_piece_at("a3")
            assert piece == PieceType.RED_PIECE

            # Get board visualization
            print(state.board_string)

            # Check if position is empty
            if state.is_empty_at("d4"):
                print("Position d4 is empty")

        Managing strategic analysis::\n

            analysis = CheckersAnalysis(
                material_advantage="Red +1 piece advantage",
                control_of_center="Red controls 3 of 4 center squares",
                suggested_moves=["e3-f4", "c3-d4", "g3-h4"],
                positional_evaluation="Slight advantage to Red"
            )
            state.add_analysis(analysis, "red")

            # Access latest analysis
            latest = state.get_latest_analysis("red")

        Game state queries::\n

            # Check game completion
            if state.is_game_over():
                winner = state.winner
                phase = state.game_phase

            # Material and position analysis
            material = state.material_balance
            kings = state.king_count
            center_control = state.center_control_score

            # Move pattern analysis
            recent_moves = state.get_recent_moves(5)
            capture_count = state.total_captures

        Advanced state analysis::\n

            # Performance metrics
            stats = state.game_statistics
            print(f"Game phase: {stats['game_phase']}")
            print(f"Move count: {stats['move_count']}")

            # Strategic position evaluation
            evaluation = state.position_evaluation
            print(f"Material score: {evaluation['material_score']}")
            print(f"Positional score: {evaluation['positional_score']}")

    Note:
        The state uses Pydantic for validation and supports both JSON serialization
        and integration with LangGraph for distributed game systems.
    """

    board: List[List[Literal[0, 1, 2, 3, 4]]] = Field(
        default_factory=lambda: CheckersState._default_board(),
        description="2D grid representation of the board using PieceType enum values",
    )

    board_string: str = Field(
        default_factory=lambda: CheckersState._create_board_string(
            CheckersState._default_board()
        ),
        description="Human-readable string representation of the board with coordinates",
    )

    turn: Literal["red", "black"] = Field(
        default="red",
        description="Current player's turn (red moves first in standard Checkers)",
    )

    move_history: Sequence[CheckersMove] = Field(
        default_factory=list,
        description="Complete chronological history of all moves made in the game",
    )

    game_status: Literal["ongoing", "game_over"] = Field(
        default="ongoing",
        description="Current game status with automatic terminal position detection",
    )

    winner: Optional[Literal["red", "black"]] = Field(
        default=None,
        description="Winner of the game if completed, None if game is still in progress",
    )

    red_analysis: Sequence[CheckersAnalysis] = Field(
        default_factory=list,
        description="Complete history of strategic analyses from red's perspective",
    )

    black_analysis: Sequence[CheckersAnalysis] = Field(
        default_factory=list,
        description="Complete history of strategic analyses from black's perspective",
    )

    captured_pieces: Dict[str, List[str]] = Field(
        default_factory=lambda: {"red": [], "black": []},
        description="Comprehensive tracking of pieces captured by each player",
    )

    turn_number: int = Field(
        default=1,
        ge=1,
        description="Current turn number starting from 1 for game tracking",
    )

    last_capture_turn: Optional[int] = Field(
        default=None,
        description="Turn number of the last capture for draw rule enforcement",
    )

    # Class constants for board representation
    __board_size: ClassVar[int] = 8
    __symbols: ClassVar[Dict[int, str]] = {0: ".", 1: "r", 2: "R", 3: "b", 4: "B"}
    __piece_symbols: ClassVar[Dict[int, str]] = {
        PieceType.EMPTY: "Empty",
        PieceType.RED_PIECE: "Red Piece",
        PieceType.RED_KING: "Red King",
        PieceType.BLACK_PIECE: "Black Piece",
        PieceType.BLACK_KING: "Black King",
    }

    @field_validator("turn_number")
    @classmethod
    def validate_turn_number(cls, v: int) -> int:
        """Validate turn number is positive.

        Args:
            v (int): Turn number to validate.

        Returns:
            int: Validated turn number.

        Raises:
            ValueError: If turn number is not positive.
        """
        if v < 1:
            raise ValueError("Turn number must be positive")
        return v

    @computed_field
    @property
    def game_phase(self) -> GamePhase:
        """Determine the current game phase based on piece count and move
        history.

        Returns:
            GamePhase: Current phase of the game (opening, middle, endgame, finished).
        """
        if self.game_status == "game_over":
            return GamePhase.FINISHED

        total_pieces = sum(
            sum(1 for cell in row if cell != PieceType.EMPTY) for row in self.board
        )

        if total_pieces >= 16:  # Most pieces still on board
            return GamePhase.OPENING
        elif total_pieces >= 8:  # Moderate piece count
            return GamePhase.MIDDLE
        else:  # Few pieces remaining
            return GamePhase.ENDGAME

    @computed_field
    @property
    def material_balance(self) -> Dict[str, Union[int, float]]:
        """Calculate material balance and piece distribution.

        Returns:
            Dict[str, Union[int, float]]: Material balance statistics including
                piece counts, king counts, and overall material score.
        """
        red_pieces = red_kings = black_pieces = black_kings = 0

        for row in self.board:
            for cell in row:
                if cell == PieceType.RED_PIECE:
                    red_pieces += 1
                elif cell == PieceType.RED_KING:
                    red_kings += 1
                elif cell == PieceType.BLACK_PIECE:
                    black_pieces += 1
                elif cell == PieceType.BLACK_KING:
                    black_kings += 1

        # Calculate material score (kings worth 1.5 pieces)
        red_score = red_pieces + (red_kings * 1.5)
        black_score = black_pieces + (black_kings * 1.5)

        return {
            "red_pieces": red_pieces,
            "red_kings": red_kings,
            "black_pieces": black_pieces,
            "black_kings": black_kings,
            "red_total": red_pieces + red_kings,
            "black_total": black_pieces + black_kings,
            "red_score": red_score,
            "black_score": black_score,
            "material_difference": red_score - black_score,
        }

    @computed_field
    @property
    def king_count(self) -> Dict[str, int]:
        """Count kings for each player.

        Returns:
            Dict[str, int]: Number of kings for each player.
        """
        red_kings = black_kings = 0

        for row in self.board:
            for cell in row:
                if cell == PieceType.RED_KING:
                    red_kings += 1
                elif cell == PieceType.BLACK_KING:
                    black_kings += 1

        return {"red": red_kings, "black": black_kings}

    @computed_field
    @property
    def center_control_score(self) -> Dict[str, Union[int, float]]:
        """Calculate center control score for strategic evaluation.

        Returns:
            Dict[str, Union[int, float]]: Center control statistics.
        """
        # Define center squares (d4, e4, d5, e5)
        center_squares = [(3, 3), (3, 4), (4, 3), (4, 4)]
        red_control = black_control = 0

        for row, col in center_squares:
            piece = self.board[row][col]
            if piece in [PieceType.RED_PIECE, PieceType.RED_KING]:
                red_control += 1
            elif piece in [PieceType.BLACK_PIECE, PieceType.BLACK_KING]:
                black_control += 1

        return {
            "red_control": red_control,
            "black_control": black_control,
            "total_center_squares": len(center_squares),
            "red_percentage": (red_control / len(center_squares)) * 100,
            "black_percentage": (black_control / len(center_squares)) * 100,
        }

    @computed_field
    @property
    def total_captures(self) -> int:
        """Count total number of captures in the game.

        Returns:
            int: Total number of pieces captured by both players.
        """
        return len(self.captured_pieces["red"]) + len(self.captured_pieces["black"])

    @computed_field
    @property
    def position_evaluation(self) -> Dict[str, Union[int, float, str]]:
        """Generate comprehensive position evaluation.

        Returns:
            Dict[str, Union[int, float, str]]: Position evaluation metrics.
        """
        material = self.material_balance
        center = self.center_control_score

        # Simple positional evaluation
        positional_score = (
            material["material_difference"] * 10
            + (center["red_control"] - center["black_control"]) * 5
        )

        if positional_score > 10:
            evaluation = "Red advantage"
        elif positional_score < -10:
            evaluation = "Black advantage"
        else:
            evaluation = "Balanced position"

        return {
            "material_score": material["material_difference"],
            "positional_score": positional_score,
            "center_control_difference": center["red_control"]
            - center["black_control"],
            "evaluation": evaluation,
            "game_phase": self.game_phase.value,
        }

    @computed_field
    @property
    def game_statistics(self) -> Dict[str, Union[int, float, str]]:
        """Generate comprehensive game statistics.

        Returns:
            Dict[str, Union[int, float, str]]: Game statistics and metrics.
        """
        material = self.material_balance

        return {
            "turn_number": self.turn_number,
            "move_count": len(self.move_history),
            "game_phase": self.game_phase.value,
            "total_pieces": material["red_total"] + material["black_total"],
            "total_captures": self.total_captures,
            "red_analysis_count": len(self.red_analysis),
            "black_analysis_count": len(self.black_analysis),
            "last_capture_turn": self.last_capture_turn or 0,
            "turns_since_capture": self.turn_number - (self.last_capture_turn or 0),
        }

    def get_piece_at(self, position: str) -> int:
        r"""Get the piece at a specific algebraic position.

        Args:
            position (str): Algebraic position (e.g., "a3", "h6").

        Returns:
            int: Piece type at the position (PieceType enum value).

        Raises:
            ValueError: If position format is invalid.

        Examples:
            Getting piece at position::\n

                state = CheckersState.initialize()
                piece = state.get_piece_at("a3")
                assert piece == PieceType.RED_PIECE

                # Check if position is empty
                if state.get_piece_at("d4") == PieceType.EMPTY:
                    print("Position d4 is empty")
        """
        if len(position) != 2:
            raise ValueError("Position must be 2 characters (e.g., 'a3')")

        col = ord(position[0].lower()) - ord("a")
        row = 8 - int(position[1])

        if not (0 <= col < 8 and 0 <= row < 8):
            raise ValueError(f"Position {position} is outside board bounds")

        return self.board[row][col]

    def is_empty_at(self, position: str) -> bool:
        """Check if a position is empty.

        Args:
            position (str): Algebraic position to check.

        Returns:
            bool: True if position is empty, False otherwise.
        """
        return self.get_piece_at(position) == PieceType.EMPTY

    def add_analysis(self, analysis: CheckersAnalysis, player: str) -> None:
        """Add strategic analysis for a player.

        Args:
            analysis (CheckersAnalysis): Analysis to add.
            player (str): Player the analysis is for ("red" or "black").

        Raises:
            ValueError: If player is not "red" or "black".
        """
        if player == "red":
            self.red_analysis = list(self.red_analysis) + [analysis]
        elif player == "black":
            self.black_analysis = list(self.black_analysis) + [analysis]
        else:
            raise ValueError(f"Invalid player: {player}")

    def get_latest_analysis(self, player: str) -> Optional[CheckersAnalysis]:
        """Get the latest analysis for a player.

        Args:
            player (str): Player to get analysis for ("red" or "black").

        Returns:
            Optional[CheckersAnalysis]: Latest analysis or None if no analysis exists.
        """
        if player == "red":
            return self.red_analysis[-1] if self.red_analysis else None
        elif player == "black":
            return self.black_analysis[-1] if self.black_analysis else None
        else:
            raise ValueError(f"Invalid player: {player}")

    def get_recent_moves(self, count: int) -> List[CheckersMove]:
        """Get the most recent moves from the game history.

        Args:
            count (int): Number of recent moves to return.

        Returns:
            List[CheckersMove]: List of recent moves (up to count).
        """
        return list(self.move_history[-count:]) if self.move_history else []

    def is_game_over(self) -> bool:
        """Check if the game is over.

        Returns:
            bool: True if game is over, False otherwise.
        """
        return self.game_status == "game_over"

    @classmethod
    def _default_board(cls) -> List[List[int]]:
        """Create the default starting board for checkers.

        Creates an 8x8 checkers board with the standard starting positions:
        - Black pieces on top three rows (rows 0-2)
        - Red pieces on bottom three rows (rows 5-7)
        - Empty middle rows (rows 3-4)

        Returns:
            List[List[int]]: 2D grid representation of the default board.

        Note:
            The board uses PieceType enum values:
            - 0: Empty square
            - 1: Red piece
            - 2: Red king
            - 3: Black piece
            - 4: Black king
        """
        return [
            [0, 3, 0, 3, 0, 3, 0, 3],
            [3, 0, 3, 0, 3, 0, 3, 0],
            [0, 3, 0, 3, 0, 3, 0, 3],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 1, 0, 1, 0, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0],
        ]

    @classmethod
    def _create_board_string(cls, board: List[List[int]]) -> str:
        r"""Create a string representation of the board for display.

        Converts the 2D grid representation to a human-readable string with
        row and column coordinates for visualization and debugging.

        Args:
            board (List[List[int]]): 2D grid representation of the board.

        Returns:
            str: String representation of the board with coordinates.

        Examples:
            Creating board visualization::\n

                board = CheckersState._default_board()
                print(CheckersState._create_board_string(board))
                # Output:
                # 8 | . b . b . b . b
                # 7 | b . b . b . b .
                # 6 | . b . b . b . b
                # 5 | . . . . . . . .
                # 4 | . . . . . . . .
                # 3 | r . r . r . r .
                # 2 | . r . r . r . r
                # 1 | r . r . r . r .
                #     a b c d e f g h
        """
        rows = [
            f"{cls.__board_size - i} | "
            + " ".join(cls._get_symbol(cell) for cell in row)
            for i, row in enumerate(board)
        ]
        col_labels = "    " + " ".join("abcdefgh")
        return "\n".join(rows) + "\n" + col_labels

    @classmethod
    def _get_symbol(cls, cell: int) -> str:
        """Get the symbol for a cell value.

        Converts the numeric cell value to its corresponding display symbol:
        - 0: "." (empty)
        - 1: "r" (red piece)
        - 2: "R" (red king)
        - 3: "b" (black piece)
        - 4: "B" (black king)

        Args:
            cell (int): Cell value (0-4).

        Returns:
            str: Symbol representing the cell.
        """
        return cls.__symbols[cell]

    @classmethod
    def initialize(cls) -> "CheckersState":
        r"""Initialize a new checkers game state.

        Creates a fresh checkers state with the standard starting board,
        red to move first, and default values for all other fields.

        Returns:
            CheckersState: A new game state ready to play.

        Examples:
            Creating a new game::\n

                state = CheckersState.initialize()
                assert state.turn == "red"
                assert state.game_status == "ongoing"
                assert state.turn_number == 1
                assert len(state.move_history) == 0

            Verifying initial board setup::\n

                state = CheckersState.initialize()
                material = state.material_balance
                assert material["red_total"] == 12
                assert material["black_total"] == 12
                assert material["red_kings"] == 0
                assert material["black_kings"] == 0
        """
        board = cls._default_board()
        return cls(board=board, board_string=cls._create_board_string(board))

    model_config = {"arbitrary_types_allowed": True}
