"""Tests for Reversi game state management."""

import pytest

from haive.games.reversi.state import ReversiState
from haive.games.reversi.state_manager import ReversiStateManager


def test_reversi_state_initialization():
    """Test initialization of Reversi game state."""
    # Default initialization (Black first, player1=Black, player2=White)
    state = ReversiStateManager.initialize()

    # Check board structure
    assert len(state.board) == 8
    assert all(len(row) == 8 for row in state.board)

    # Check initial disc placement (standard 2x2 center setup)
    assert state.board[3][3] == "W"
    assert state.board[3][4] == "B"
    assert state.board[4][3] == "B"
    assert state.board[4][4] == "W"

    # Check initial disc count
    counts = state.disc_count
    assert counts["B"] == 2
    assert counts["W"] == 2

    # Check turn
    assert state.turn == "B"

    # Check player assignments
    assert state.player_B == "player1"
    assert state.player_W == "player2"

    # Check game status
    assert state.game_status == "ongoing"
    assert state.winner is None

    # Empty move history
    assert len(state.move_history) == 0


def test_reversi_state_board_validation():
    """Test board validation in ReversiState."""
    # Create a valid board
    valid_board = [[None for _ in range(8)] for _ in range(8)]
    valid_board[3][3] = "W"
    valid_board[3][4] = "B"
    valid_board[4][3] = "B"
    valid_board[4][4] = "W"

    # This should not raise an exception
    ReversiState(board=valid_board, turn="B", player_B="player1", player_W="player2")

    # Invalid board (wrong size - too few rows)
    invalid_board_rows = [[None for _ in range(8)] for _ in range(7)]
    with pytest.raises(ValueError):
        ReversiState(
            board=invalid_board_rows, turn="B", player_B="player1", player_W="player2"
        )

    # Invalid board (wrong size - too few columns)
    invalid_board_cols = [[None for _ in range(7)] for _ in range(8)]
    with pytest.raises(ValueError):
        ReversiState(
            board=invalid_board_cols, turn="B", player_B="player1", player_W="player2"
        )

    # Invalid board (invalid cell values)
    invalid_board_values = [[None for _ in range(8)] for _ in range(8)]
    invalid_board_values[3][3] = "X"  # Invalid value, should be "B", "W", or None
    with pytest.raises(ValueError):
        ReversiState(
            board=invalid_board_values, turn="B", player_B="player1", player_W="player2"
        )


def test_board_string_representation():
    """Test the string representation of the board."""
    state = ReversiStateManager.initialize()

    # Get the board string
    board_string = state.board_string

    # Check that it contains the expected elements
    assert "1 2 3 4 5 6 7 8" in board_string  # Column numbers
    assert "A |" in board_string  # Row A
    assert "H |" in board_string  # Row H
    assert "B|" in board_string  # Black disc
    assert "W|" in board_string  # White disc
    assert "Black: 2 discs, White: 2 discs" in board_string  # Disc count


def test_current_player_name():
    """Test the current_player_name property."""
    # Initialize with Black first
    state = ReversiStateManager.initialize(first_player="B")
    assert state.turn == "B"
    assert state.current_player_name == state.player_B

    # Initialize with White first
    state = ReversiStateManager.initialize(first_player="W")
    assert state.turn == "W"
    assert state.current_player_name == state.player_W
