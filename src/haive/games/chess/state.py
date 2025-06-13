"""Chess game state models."""

from typing import Any, Dict, List, Literal, Optional

import chess
from haive.core.schema.state_schema import StateSchema
from pydantic import BaseModel, Field, computed_field


class ChessState(StateSchema):
    """State schema for the chess game using StateSchema base."""

    # Board state
    board_fens: List[str] = Field(
        default_factory=lambda: [chess.Board().fen()],
        description="List of FEN board states, latest at the end",
    )

    # Move tracking
    move_history: List[tuple[str, str]] = Field(
        default_factory=list, description="List of (player_color, UCI move) tuples"
    )

    # Game flow
    current_player: Literal["white", "black"] = Field(
        default="white", description="Current player making a move"
    )

    turn: Literal["white", "black"] = Field(default="white", description="Current turn")

    # Game status
    game_status: Literal["ongoing", "check", "checkmate", "stalemate", "draw"] = Field(
        default="ongoing", description="Status of the game"
    )

    game_result: Optional[str] = Field(
        default=None, description="Final game result (white_win, black_win, draw)"
    )

    # Analysis
    white_analysis: List[Dict[str, Any]] = Field(
        default_factory=list, description="White's position analysis"
    )

    black_analysis: List[Dict[str, Any]] = Field(
        default_factory=list, description="Black's position analysis"
    )

    # Captured pieces
    captured_pieces: Dict[str, List[str]] = Field(
        default_factory=lambda: {"white": [], "black": []},
        description="Captured pieces by each player",
    )

    # Error handling
    error_message: Optional[str] = Field(
        default=None, description="Error message if any"
    )

    # Additional fields for LLM context
    legal_moves: Optional[str] = Field(
        default=None, description="Legal moves in current position"
    )

    recent_moves: Optional[str] = Field(
        default=None, description="Recent moves formatted for LLM"
    )

    @computed_field
    @property
    def board_fen(self) -> str:
        """Get the current board state (latest FEN)."""
        return self.board_fens[-1] if self.board_fens else chess.Board().fen()

    @computed_field
    @property
    def current_board_fen(self) -> str:
        """Alias for board_fen for compatibility."""
        return self.board_fen

    def get_board(self) -> chess.Board:
        """Get a chess.Board object for the current position."""
        return chess.Board(self.board_fen)
