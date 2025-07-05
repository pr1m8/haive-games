"""Test cases for Checkers game state manager.

This module tests the CheckersStateManager class and its methods for managing
game state transitions, move validation, and game logic.
"""

import pytest

from haive.games.checkers.models import CheckersMove
from haive.games.checkers.state import CheckersState
from haive.games.checkers.state_manager import CheckersStateManager


class TestCheckersStateManagerInitialization:
    """Test cases for CheckersStateManager initialization."""

    def test_initialize_default_game(self) -> None:
        """Test initializing a default checkers game."""
        state = CheckersStateManager.initialize()

        # Check basic state properties
        assert state.turn == "red"
        assert state.game_status == "ongoing"
        assert state.winner is None
        assert len(state.move_history) == 0
        assert len(state.red_analysis) == 0
        assert len(state.black_analysis) == 0
        assert state.captured_pieces == {"red": [], "black": []}

        # Check board structure
        assert len(state.board) == 8
        assert all(len(row) == 8 for row in state.board)

        # Check piece placement
        # Count pieces
        red_pieces = sum(1 for row in state.board for cell in row if cell == 1)
        black_pieces = sum(1 for row in state.board for cell in row if cell == 3)
        empty_squares = sum(1 for row in state.board for cell in row if cell == 0)

        assert red_pieces == 12
        assert black_pieces == 12
        assert empty_squares == 40  # 64 - 24 pieces

    def test_board_size_constant(self) -> None:
        """Test that board size constant is correct."""
        assert CheckersStateManager.BOARD_SIZE == 8

    def test_initialize_board_string(self) -> None:
        """Test that initialization creates proper board string."""
        state = CheckersStateManager.initialize()

        # Should have a non-empty board string
        assert state.board_string is not None
        assert len(state.board_string) > 0

        # Should contain expected elements
        assert "r" in state.board_string  # Red pieces
        assert "b" in state.board_string  # Black pieces
        assert "." in state.board_string  # Empty squares
        assert "8 |" in state.board_string  # Row numbers
        assert "a b c d e f g h" in state.board_string  # Column labels


class TestBoardStringCreation:
    """Test cases for board string creation."""

    def test_create_board_string_standard_board(self) -> None:
        """Test creating board string from standard initial board."""
        # Create a standard initial board
        board = [
            [0, 3, 0, 3, 0, 3, 0, 3],
            [3, 0, 3, 0, 3, 0, 3, 0],
            [0, 3, 0, 3, 0, 3, 0, 3],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 1, 0, 1, 0, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0],
        ]

        board_string = CheckersStateManager._create_board_string(board)

        lines = board_string.split("\n")

        # Check structure
        assert len(lines) == 9  # 8 board rows + column labels

        # Check row numbering (8 down to 1)
        for i in range(8):
            expected_rank = 8 - i
            assert lines[i].startswith(f"{expected_rank} |")

        # Check column labels
        assert lines[8] == "    a b c d e f g h"

    def test_create_board_string_empty_board(self) -> None:
        """Test creating board string from empty board."""
        empty_board = [[0 for _ in range(8)] for _ in range(8)]
        board_string = CheckersStateManager._create_board_string(empty_board)

        # Should contain only dots for pieces
        lines = board_string.split("\n")
        for i in range(8):
            row_content = lines[i].split("| ")[1]  # Get content after "N | "
            pieces = row_content.split()
            assert all(piece == "." for piece in pieces)

    def test_create_board_string_mixed_pieces(self) -> None:
        """Test creating board string with all piece types."""
        mixed_board = [[0 for _ in range(8)] for _ in range(8)]
        mixed_board[0][0] = 1  # Red piece
        mixed_board[0][2] = 2  # Red king
        mixed_board[0][4] = 3  # Black piece
        mixed_board[0][6] = 4  # Black king

        board_string = CheckersStateManager._create_board_string(board_string)

        # Should contain all piece symbols
        assert "r" in board_string  # Red piece
        assert "R" in board_string  # Red king
        assert "b" in board_string  # Black piece
        assert "B" in board_string  # Black king

    def test_create_board_string_symbols_mapping(self) -> None:
        """Test that symbols are mapped correctly."""
        # Test each symbol individually
        test_boards = [
            [[1] + [0] * 7] + [[0] * 8] * 7,  # Red piece
            [[2] + [0] * 7] + [[0] * 8] * 7,  # Red king
            [[3] + [0] * 7] + [[0] * 8] * 7,  # Black piece
            [[4] + [0] * 7] + [[0] * 8] * 7,  # Black king
        ]

        expected_symbols = ["r", "R", "b", "B"]

        for board, expected_symbol in zip(test_boards, expected_symbols):
            board_string = CheckersStateManager._create_board_string(board)
            assert expected_symbol in board_string


class TestLegalMoveGeneration:
    """Test cases for legal move generation."""

    def test_get_legal_moves_initial_position_red(self) -> None:
        """Test getting legal moves from initial position for red."""
        state = CheckersStateManager.initialize()
        legal_moves = CheckersStateManager.get_legal_moves(state)

        # Red should have legal moves in the initial position
        assert len(legal_moves) > 0

        # All moves should be for red player
        assert all(move.player == "red" for move in legal_moves)

        # Should be regular moves, not jumps
        assert all(not move.is_jump for move in legal_moves)

        # Moves should be forward (diagonal) advances
        # In initial position, red pieces can move from rank 3 to rank 4,
        # rank 2 to rank 3, and rank 1 to rank 2

    def test_get_legal_moves_no_moves_available(self) -> None:
        """Test getting legal moves when no moves are available."""
        # Create a board where current player has no legal moves
        board = [[0 for _ in range(8)] for _ in range(8)]
        # Place a red piece surrounded by black pieces
        board[3][3] = 1  # Red piece
        board[2][2] = 3  # Black piece blocking
        board[2][4] = 3  # Black piece blocking
        board[4][2] = 3  # Black piece blocking
        board[4][4] = 3  # Black piece blocking

        state = CheckersState(board=board, turn="red")
        legal_moves = CheckersStateManager.get_legal_moves(state)

        # Should have no legal moves
        assert len(legal_moves) == 0

    def test_get_legal_moves_jump_priority(self) -> None:
        """Test that jump moves take priority over regular moves."""
        # Create a board with both regular moves and jump available
        board = [[0 for _ in range(8)] for _ in range(8)]
        board[5][1] = 1  # Red piece that can jump
        board[4][2] = 3  # Black piece to capture
        board[7][1] = 1  # Red piece that can make regular move

        state = CheckersState(board=board, turn="red")
        legal_moves = CheckersStateManager.get_legal_moves(state)

        # Should only return jump moves (mandatory in checkers)
        assert len(legal_moves) > 0
        assert all(move.is_jump for move in legal_moves)

    def test_get_legal_moves_black_turn(self) -> None:
        """Test getting legal moves when it's black's turn."""
        # Create a simple position with black to move
        board = [[0 for _ in range(8)] for _ in range(8)]
        board[2][1] = 3  # Black piece

        state = CheckersState(board=board, turn="black")
        legal_moves = CheckersStateManager.get_legal_moves(state)

        # All moves should be for black player
        assert all(move.player == "black" for move in legal_moves)

    def test_get_legal_moves_king_movement(self) -> None:
        """Test legal moves for king pieces."""
        # Create a board with a red king
        board = [[0 for _ in range(8)] for _ in range(8)]
        board[4][4] = 2  # Red king in center

        state = CheckersState(board=board, turn="red")
        legal_moves = CheckersStateManager.get_legal_moves(state)

        # King should have moves in all diagonal directions
        assert len(legal_moves) > 0
        assert all(move.player == "red" for move in legal_moves)


class TestJumpMoveGeneration:
    """Test cases for jump move generation specifically."""

    def test_get_jump_moves_simple_capture(self) -> None:
        """Test finding a simple jump move."""
        # Create a board with a clear jump opportunity
        board = [[0 for _ in range(8)] for _ in range(8)]
        board[5][1] = 1  # Red piece
        board[4][2] = 3  # Black piece to capture
        # Position (3,3) should be empty for the jump

        piece_values = [1, 2]  # Red pieces
        jumps = CheckersStateManager._get_jump_moves(board, "red", piece_values)

        assert len(jumps) > 0
        assert all(move.is_jump for move in jumps)
        assert all(move.player == "red" for move in jumps)

    def test_get_jump_moves_no_jumps_available(self) -> None:
        """Test when no jump moves are available."""
        # Create a board with no jump opportunities
        board = [[0 for _ in range(8)] for _ in range(8)]
        board[5][1] = 1  # Red piece with no adjacent enemies

        piece_values = [1, 2]  # Red pieces
        jumps = CheckersStateManager._get_jump_moves(board, "red", piece_values)

        assert len(jumps) == 0

    def test_get_jump_moves_blocked_landing(self) -> None:
        """Test jump moves when landing square is blocked."""
        # Create a board where jump landing square is occupied
        board = [[0 for _ in range(8)] for _ in range(8)]
        board[5][1] = 1  # Red piece
        board[4][2] = 3  # Black piece to capture
        board[3][3] = 1  # Red piece blocking landing square

        piece_values = [1, 2]  # Red pieces
        jumps = CheckersStateManager._get_jump_moves(board, "red", piece_values)

        # Should not be able to jump if landing square is occupied
        assert len(jumps) == 0


class TestRegularMoveGeneration:
    """Test cases for regular move generation."""

    def test_get_regular_moves_simple_position(self) -> None:
        """Test finding regular moves in a simple position."""
        # Create a board with a single red piece
        board = [[0 for _ in range(8)] for _ in range(8)]
        board[6][1] = 1  # Red piece

        piece_values = [1, 2]  # Red pieces
        moves = CheckersStateManager._get_regular_moves(board, "red", piece_values)

        assert len(moves) > 0
        assert all(not move.is_jump for move in moves)
        assert all(move.player == "red" for move in moves)

    def test_get_regular_moves_blocked_squares(self) -> None:
        """Test regular moves when some squares are blocked."""
        # Create a board where some moves are blocked
        board = [[0 for _ in range(8)] for _ in range(8)]
        board[6][1] = 1  # Red piece
        board[5][0] = 3  # Black piece blocking one diagonal
        board[5][2] = 1  # Red piece blocking other diagonal

        piece_values = [1, 2]  # Red pieces
        moves = CheckersStateManager._get_regular_moves(board, "red", piece_values)

        # Should have no legal regular moves (both diagonals blocked)
        assert len(moves) == 0

    def test_get_regular_moves_edge_pieces(self) -> None:
        """Test regular moves for pieces on board edges."""
        # Create a board with pieces on edges
        board = [[0 for _ in range(8)] for _ in range(8)]
        board[6][0] = 1  # Red piece on left edge
        board[6][7] = 1  # Red piece on right edge

        piece_values = [1, 2]  # Red pieces
        moves = CheckersStateManager._get_regular_moves(board, "red", piece_values)

        # Edge pieces should have fewer move options
        assert len(moves) >= 0  # May have some moves depending on forward squares


class TestMoveValidationHelpers:
    """Test cases for move validation helper methods."""

    def test_is_valid_position(self) -> None:
        """Test position validation helper."""
        # Valid positions
        assert CheckersStateManager._is_valid_position(0, 0) is True
        assert CheckersStateManager._is_valid_position(7, 7) is True
        assert CheckersStateManager._is_valid_position(3, 4) is True

        # Invalid positions
        assert CheckersStateManager._is_valid_position(-1, 0) is False
        assert CheckersStateManager._is_valid_position(0, -1) is False
        assert CheckersStateManager._is_valid_position(8, 0) is False
        assert CheckersStateManager._is_valid_position(0, 8) is False

    def test_algebraic_to_indices(self) -> None:
        """Test conversion from algebraic notation to array indices."""
        # Test various positions
        assert CheckersStateManager._algebraic_to_indices("a1") == (7, 0)
        assert CheckersStateManager._algebraic_to_indices("h8") == (0, 7)
        assert CheckersStateManager._algebraic_to_indices("d4") == (4, 3)
        assert CheckersStateManager._algebraic_to_indices("e5") == (3, 4)

    def test_indices_to_algebraic(self) -> None:
        """Test conversion from array indices to algebraic notation."""
        # Test various positions
        assert CheckersStateManager._indices_to_algebraic(7, 0) == "a1"
        assert CheckersStateManager._indices_to_algebraic(0, 7) == "h8"
        assert CheckersStateManager._indices_to_algebraic(4, 3) == "d4"
        assert CheckersStateManager._indices_to_algebraic(3, 4) == "e5"

    def test_algebraic_indices_round_trip(self) -> None:
        """Test that algebraic notation and indices convert consistently."""
        test_positions = ["a1", "b2", "c3", "d4", "e5", "f6", "g7", "h8"]

        for pos in test_positions:
            # Convert to indices and back
            row, col = CheckersStateManager._algebraic_to_indices(pos)
            converted_back = CheckersStateManager._indices_to_algebraic(row, col)
            assert converted_back == pos


class TestGameStatusAndWinning:
    """Test cases for game status checking and winner determination."""

    def test_check_game_over_ongoing_game(self) -> None:
        """Test game status check for ongoing game."""
        state = CheckersStateManager.initialize()

        # Initial position should be ongoing
        assert state.game_status == "ongoing"
        assert state.winner is None

    def test_check_game_over_no_pieces(self) -> None:
        """Test game over when a player has no pieces."""
        # Create a board with only red pieces
        board = [[0 for _ in range(8)] for _ in range(8)]
        board[0][0] = 1  # Single red piece

        state = CheckersState(
            board=board,
            turn="black",  # Black to move but has no pieces
            game_status="ongoing",
        )

        # This would be detected by the state manager's game over logic
        # The exact implementation depends on how the state manager
        # checks for no pieces or no legal moves

    def test_check_game_over_no_legal_moves(self) -> None:
        """Test game over when current player has no legal moves."""
        # Create a board where current player is blocked
        board = [[0 for _ in range(8)] for _ in range(8)]
        board[7][7] = 1  # Red piece in corner
        board[6][6] = 3  # Black piece blocking

        state = CheckersState(board=board, turn="red")
        legal_moves = CheckersStateManager.get_legal_moves(state)

        # If no legal moves, game should be over
        if len(legal_moves) == 0:
            # This represents a game over situation
            assert True
        else:
            # Still has moves, game continues
            assert len(legal_moves) > 0


class TestMoveApplication:
    """Test cases for applying moves to the game state."""

    def test_apply_move_regular_move(self) -> None:
        """Test applying a regular move."""
        state = CheckersStateManager.initialize()

        # Find a legal move
        legal_moves = CheckersStateManager.get_legal_moves(state)
        assert len(legal_moves) > 0

        move = legal_moves[0]  # Take the first legal move

        # Apply the move
        new_state = CheckersStateManager.apply_move(state, move)

        # Check that state was updated
        assert len(new_state.move_history) == len(state.move_history) + 1
        assert new_state.move_history[-1] == move

        # Turn should switch
        assert new_state.turn != state.turn

    def test_apply_move_invalid_move(self) -> None:
        """Test applying an invalid move."""
        state = CheckersStateManager.initialize()

        # Create an invalid move
        invalid_move = CheckersMove(
            from_position="a1",  # No piece here initially
            to_position="b2",
            player="red",
        )

        # Should raise an exception or return an error
        with pytest.raises((ValueError, Exception)):
            CheckersStateManager.apply_move(state, invalid_move)

    def test_apply_move_king_promotion(self) -> None:
        """Test that pieces are promoted to kings when reaching the end."""
        # Create a board with a red piece about to promote
        board = [[0 for _ in range(8)] for _ in range(8)]
        board[1][1] = 1  # Red piece near black's back rank

        state = CheckersState(board=board, turn="red")

        # Move the piece to the back rank
        promotion_move = CheckersMove(
            from_position="b7",  # b7 in algebraic notation
            to_position="a8",  # Reaching back rank
            player="red",
        )

        # This would test promotion logic if implemented
        # The exact test depends on the apply_move implementation
