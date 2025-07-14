"""Unit tests for chess state manager.

This module tests the ChessStateManager class, including move application,
game state updates, and turn management.
"""

from unittest.mock import patch

import chess
import pytest

from haive.games.chess.state import ChessState
from haive.games.chess.state_manager import ChessGameStateManager


class TestChessStateManager:
    """Test suite for ChessGameStateManager."""

    @pytest.fixture
    def state_manager(self) -> type[ChessGameStateManager]:
        """Return the ChessGameStateManager class for testing."""
        return ChessGameStateManager

    @pytest.fixture
    def initial_state(self) -> ChessState:
        """Create an initial chess state."""
        return ChessState()

    def test_state_manager_initialization(
        self, state_manager: ChessStateManager
    ) -> None:
        """Test that state manager initializes correctly."""
        # Assert
        assert isinstance(state_manager, ChessStateManager)
        assert hasattr(state_manager, "apply_move")
        assert hasattr(state_manager, "update_game_status")

    def test_apply_move_updates_board_state(
        self, state_manager: ChessStateManager, initial_state: ChessState
    ) -> None:
        """Test that apply_move correctly updates the board state."""
        # Arrange
        move = "e2e4"

        # Act
        updated_state = state_manager.apply_move(initial_state, move)

        # Assert
        assert updated_state.board_fen != initial_state.board_fen
        assert ("white", move) in updated_state.move_history
        assert updated_state.turn == "black"

        # Verify the move was actually applied
        board = updated_state.get_board()
        assert board.piece_at(chess.E4) is not None
        assert board.piece_at(chess.E2) is None

    def test_apply_move_alternates_turns(
        self, state_manager: ChessStateManager, initial_state: ChessState
    ) -> None:
        """Test that turns alternate correctly after moves."""
        # Arrange
        moves = ["e2e4", "e7e5", "Nf3", "Nc6"]
        state = initial_state

        # Act & Assert
        for i, move in enumerate(moves):
            state = state_manager.apply_move(state, move)
            expected_turn = "black" if i % 2 == 0 else "white"
            assert state.turn == expected_turn
            assert len(state.move_history) == i + 1

    def test_apply_move_detects_check(self, state_manager: ChessStateManager) -> None:
        """Test that apply_move detects check situations."""
        # Arrange - Scholar's mate attempt position
        state = ChessState()
        state.board_fen = (
            "r1bqkbnr/pppp1ppp/2n5/4p3/2B1P3/5Q2/PPPP1PPP/RNB1K1NR b KQkq - 0 3"
        )

        # Act - Black plays a move that doesn't block check
        with patch.object(state_manager, "update_game_status") as mock_update:
            state_manager.apply_move(state, "Nf6")

        # Assert
        mock_update.assert_called_once()

    def test_apply_move_handles_castling(
        self, state_manager: ChessStateManager
    ) -> None:
        """Test that castling moves are handled correctly."""
        # Arrange - Position where castling is possible
        state = ChessState()
        state.board_fen = "r3k2r/pppppppp/8/8/8/8/PPPPPPPP/R3K2R w KQkq - 0 1"

        # Act - White castles kingside
        updated_state = state_manager.apply_move(state, "O-O")

        # Assert
        board = updated_state.get_board()
        assert board.piece_at(chess.G1) is not None  # King on g1
        assert board.piece_at(chess.F1) is not None  # Rook on f1
        assert board.piece_at(chess.E1) is None  # No piece on e1
        assert board.piece_at(chess.H1) is None  # No piece on h1

    def test_apply_move_handles_en_passant(
        self, state_manager: ChessStateManager
    ) -> None:
        """Test that en passant captures are handled correctly."""
        # Arrange - Position with en passant possible
        state = ChessState()
        state.board_fen = "rnbqkbnr/ppp1pppp/8/3pP3/8/8/PPPP1PPP/RNBQKBNR w KQkq d6 0 3"

        # Act - White captures en passant
        updated_state = state_manager.apply_move(state, "exd6")

        # Assert
        board = updated_state.get_board()
        assert board.piece_at(chess.D6) is not None  # White pawn on d6
        assert board.piece_at(chess.D5) is None  # Black pawn removed

    def test_apply_move_tracks_captured_pieces(
        self, state_manager: ChessStateManager
    ) -> None:
        """Test that captured pieces are tracked correctly."""
        # Arrange - Position with a capture possible
        state = ChessState()
        state.board_fen = "rnbqkbnr/ppp1pppp/8/3p4/3P4/8/PPP1PPPP/RNBQKBNR w KQkq - 0 2"

        # Act - White captures black's pawn
        updated_state = state_manager.apply_move(state, "dxe5")

        # Assert
        assert "pawn" in updated_state.captured_pieces["black"]
        assert len(updated_state.captured_pieces["black"]) == 1
        assert len(updated_state.captured_pieces["white"]) == 0

    def test_update_game_status_detects_checkmate(
        self, state_manager: ChessStateManager
    ) -> None:
        """Test that checkmate is detected correctly."""
        # Arrange - Fool's mate position
        state = ChessState()
        state.board_fen = (
            "rnb1kbnr/pppp1ppp/8/4p3/6Pq/5P2/PPPPP2P/RNBQKBNR w KQkq - 1 3"
        )

        # Act
        updated_state = state_manager.update_game_status(state)

        # Assert
        assert updated_state.game_status == "checkmate"
        assert updated_state.game_result == "black_win"

    def test_update_game_status_detects_stalemate(
        self, state_manager: ChessStateManager
    ) -> None:
        """Test that stalemate is detected correctly."""
        # Arrange - Stalemate position
        state = ChessState()
        state.board_fen = "7k/5Q2/6K1/8/8/8/8/8 b - - 0 1"

        # Act
        updated_state = state_manager.update_game_status(state)

        # Assert
        assert updated_state.game_status == "stalemate"
        assert updated_state.game_result == "draw"

    def test_update_game_status_detects_check(
        self, state_manager: ChessStateManager
    ) -> None:
        """Test that check (but not checkmate) is detected."""
        # Arrange - Check but not checkmate
        state = ChessState()
        state.board_fen = "rnbqkbnr/pppp1ppp/8/4p3/4P3/8/PPPPQPPP/RNB1KBNR b KQkq - 1 2"

        # Act
        updated_state = state_manager.update_game_status(state)

        # Assert
        assert updated_state.game_status == "check"
        assert updated_state.game_result is None

    def test_apply_invalid_move_raises_error(
        self, state_manager: ChessStateManager, initial_state: ChessState
    ) -> None:
        """Test that invalid moves raise appropriate errors."""
        # Arrange
        invalid_moves = ["e2e5", "Nf6", "xyz", "e9e10"]

        # Act & Assert
        for move in invalid_moves:
            with pytest.raises(ValueError):
                state_manager.apply_move(initial_state, move)

    def test_promotion_move_handling(self, state_manager: ChessStateManager) -> None:
        """Test that pawn promotion is handled correctly."""
        # Arrange - White pawn ready to promote
        state = ChessState()
        state.board_fen = "rnbqkbn1/pppppppP/8/8/8/8/PPPPPP1P/RNBQKBNR w KQq - 0 1"

        # Act - Promote to queen
        updated_state = state_manager.apply_move(state, "h7h8=Q")

        # Assert
        board = updated_state.get_board()
        piece = board.piece_at(chess.H8)
        assert piece is not None
        assert piece.piece_type == chess.QUEEN
        assert piece.color == chess.WHITE
