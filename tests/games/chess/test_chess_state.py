"""Unit tests for chess game state.

This module tests the ChessState class, including board representation,
move history tracking, game status management, and state transitions.
"""

import chess
import pytest

from haive.games.chess.state import ChessState


class TestChessState:
    """Test suite for ChessState."""

    @pytest.fixture
    def initial_state(self) -> ChessState:
        """Create an initial chess state for testing."""
        return ChessState()

    @pytest.fixture
    def midgame_state(self) -> ChessState:
        """Create a chess state in the middle of a game."""
        state = ChessState()
        state.board_fen = (
            "r1bqkb1r/pppp1ppp/2n2n2/4p3/2B1P3/5N2/PPPP1PPP/RNBQK2R w KQkq - 4 4"
        )
        state.move_history = [
            ("white", "e2e4"),
            ("black", "e7e5"),
            ("white", "Nf3"),
            ("black", "Nc6"),
            ("white", "Bc4"),
            ("black", "Nf6"),
        ]
        state.turn = "white"
        return state

    def test_initial_chess_state_has_correct_defaults(
        self, initial_state: ChessState
    ) -> None:
        """Test that initial chess state has correct default values."""
        # Assert
        assert initial_state.board_fen == chess.STARTING_FEN
        assert initial_state.move_history == []
        assert initial_state.current_player == "white"
        assert initial_state.turn == "white"
        assert initial_state.game_status == "ongoing"
        assert initial_state.game_result is None
        assert initial_state.captured_pieces == {"white": [], "black": []}

    def test_get_board_returns_valid_chess_board(
        self, initial_state: ChessState
    ) -> None:
        """Test that get_board returns a valid chess.Board object."""
        # Act
        board = initial_state.get_board()

        # Assert
        assert isinstance(board, chess.Board)
        assert board.fen() == chess.STARTING_FEN
        assert not board.is_game_over()

    def test_get_board_handles_invalid_fen_gracefully(self) -> None:
        """Test that get_board raises ValueError for invalid FEN."""
        # Arrange
        state = ChessState()
        state.board_fen = "invalid fen string"

        # Act & Assert
        with pytest.raises(ValueError) as exc_info:
            state.get_board()
        assert "Invalid FEN string" in str(exc_info.value)

    def test_current_board_computed_field(self, initial_state: ChessState) -> None:
        """Test that current_board computed field returns FEN."""
        # Act
        current_board = initial_state.current_board

        # Assert
        assert current_board == chess.STARTING_FEN
        assert current_board == initial_state.board_fen

    def test_state_tracks_move_history(self, midgame_state: ChessState) -> None:
        """Test that state properly tracks move history."""
        # Assert
        assert len(midgame_state.move_history) == 6
        assert midgame_state.move_history[0] == ("white", "e2e4")
        assert midgame_state.move_history[-1] == ("black", "Nf6")

        # Check alternating colors
        for i, (color, _) in enumerate(midgame_state.move_history):
            expected_color = "white" if i % 2 == 0 else "black"
            assert color == expected_color

    def test_state_tracks_captured_pieces(self) -> None:
        """Test that state tracks captured pieces correctly."""
        # Arrange
        state = ChessState()
        state.captured_pieces = {
            "white": ["pawn", "knight"],
            "black": ["pawn", "pawn", "bishop"],
        }

        # Assert
        assert len(state.captured_pieces["white"]) == 2
        assert len(state.captured_pieces["black"]) == 3
        assert "knight" in state.captured_pieces["white"]
        assert state.captured_pieces["black"].count("pawn") == 2

    def test_game_status_transitions(self) -> None:
        """Test various game status values."""
        # Arrange
        state = ChessState()

        # Test check status
        state.game_status = "check"
        assert state.game_status == "check"
        assert state.game_result is None

        # Test checkmate status
        state.game_status = "checkmate"
        state.game_result = "white_win"
        assert state.game_status == "checkmate"
        assert state.game_result == "white_win"

        # Test draw status
        state.game_status = "draw"
        state.game_result = "draw"
        assert state.game_status == "draw"
        assert state.game_result == "draw"

    def test_analysis_fields_store_position_data(self) -> None:
        """Test that analysis fields can store position analysis data."""
        # Arrange
        state = ChessState()
        white_analysis = {
            "evaluation": 0.3,
            "best_moves": ["Nf3", "e4", "d4"],
            "threats": [],
        }
        black_analysis = {
            "evaluation": -0.3,
            "best_moves": ["e5", "d5", "Nf6"],
            "opportunities": ["Control center"],
        }

        # Act
        state.white_analysis.append(white_analysis)
        state.black_analysis.append(black_analysis)

        # Assert
        assert len(state.white_analysis) == 1
        assert state.white_analysis[0]["evaluation"] == 0.3
        assert len(state.black_analysis) == 1
        assert "opportunities" in state.black_analysis[0]

    def test_state_serialization(self, midgame_state: ChessState) -> None:
        """Test that state can be serialized and deserialized."""
        # Act
        state_dict = midgame_state.model_dump()
        restored_state = ChessState(**state_dict)

        # Assert
        assert restored_state.board_fen == midgame_state.board_fen
        assert restored_state.move_history == midgame_state.move_history
        assert restored_state.turn == midgame_state.turn
        assert restored_state.get_board().fen() == midgame_state.get_board().fen()

    def test_state_with_endgame_position(self) -> None:
        """Test state with an endgame position."""
        # Arrange - Fool's mate position
        state = ChessState()
        state.board_fen = (
            "rnb1kbnr/pppp1ppp/8/4p3/6Pq/5P2/PPPPP2P/RNBQKBNR w KQkq - 1 3"
        )
        state.game_status = "checkmate"
        state.game_result = "black_win"
        state.move_history = [
            ("white", "f2f3"),
            ("black", "e7e5"),
            ("white", "g2g4"),
            ("black", "Qh4#"),
        ]

        # Act
        board = state.get_board()

        # Assert
        assert board.is_checkmate()
        assert state.game_status == "checkmate"
        assert state.game_result == "black_win"
        assert len(state.move_history) == 4
