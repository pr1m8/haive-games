"""Tests for Tic Tac Toe game state."""

import pytest

from haive.games.tic_tac_toe.state import TicTacToeState


def test_tic_tac_toe_state_initialization():
    """Test initialization of Tic Tac Toe game state."""
    # Default initialization
    state = TicTacToeState.initialize()

    # Check board structure
    assert len(state.board) == 3
    assert all(len(row) == 3 for row in state.board)
    assert all(cell is None for row in state.board for cell in row)

    # Check initial game status
    assert state.turn == "X"
    assert state.game_status == "ongoing"
    assert state.winner is None
    assert state.error_message is None

    # Check player assignments
    assert state.player_X == "player1"
    assert state.player_O == "player2"

    # Check empty move history and analysis
    assert len(state.move_history) == 0
    assert len(state.player1_analysis) == 0
    assert len(state.player2_analysis) == 0


def test_tic_tac_toe_state_board_validation():
    """Test board validation in TicTacToeState."""
    # Valid board
    valid_board = [[None, None, None], [None, "X", None], [None, None, "O"]]
    state = TicTacToeState(
        board=valid_board,
        turn="X",
        game_status="ongoing",
        player_X="player1",
        player_O="player2",
    )
    assert state.board == valid_board

    # Invalid board size (too few rows)
    invalid_board_rows = [[None, None, None], [None, "X", None]]
    with pytest.raises(ValueError):
        TicTacToeState(
            board=invalid_board_rows,
            turn="X",
            game_status="ongoing",
            player_X="player1",
            player_O="player2",
        )

    # Invalid board size (too few columns)
    invalid_board_cols = [[None, None], [None, "X"], [None, None]]
    with pytest.raises(ValueError):
        TicTacToeState(
            board=invalid_board_cols,
            turn="X",
            game_status="ongoing",
            player_X="player1",
            player_O="player2",
        )

    # Invalid cell value
    invalid_board_value = [[None, None, None], [None, "Z", None], [None, None, "O"]]
    with pytest.raises(ValueError):
        TicTacToeState(
            board=invalid_board_value,
            turn="X",
            game_status="ongoing",
            player_X="player1",
            player_O="player2",
        )


def test_empty_cells_property():
    """Test the empty_cells property."""
    # Empty board
    state = TicTacToeState.initialize()
    assert len(state.empty_cells) == 9
    assert (0, 0) in state.empty_cells
    assert (2, 2) in state.empty_cells

    # Partially filled board
    state.board[0][0] = "X"
    state.board[1][1] = "O"
    assert len(state.empty_cells) == 7
    assert (0, 0) not in state.empty_cells
    assert (1, 1) not in state.empty_cells
    assert (0, 1) in state.empty_cells


def test_is_board_full_property():
    """Test the is_board_full property."""
    # Empty board
    state = TicTacToeState.initialize()
    assert state.is_board_full is False

    # Partially filled board
    state.board[0][0] = "X"
    state.board[1][1] = "O"
    assert state.is_board_full is False

    # Full board
    full_board = [["X", "O", "X"], ["X", "O", "O"], ["O", "X", "X"]]
    state = TicTacToeState(
        board=full_board,
        turn="X",
        game_status="ongoing",
        player_X="player1",
        player_O="player2",
    )
    assert state.is_board_full is True


def test_current_player_name_property():
    """Test the current_player_name property."""
    # X's turn
    state = TicTacToeState.initialize(first_player="X")
    assert state.turn == "X"
    assert state.current_player_name == state.player_X

    # O's turn
    state.turn = "O"
    assert state.current_player_name == state.player_O

    # Custom player assignments
    state = TicTacToeState.initialize(
        first_player="X", player_X="player2", player_O="player1"
    )
    assert state.turn == "X"
    assert state.current_player_name == "player2"


def test_board_string_property():
    """Test the board_string property."""
    # Create a state with a non-empty board
    board = [["X", None, "O"], [None, "X", None], ["O", None, None]]
    state = TicTacToeState(
        board=board,
        turn="O",
        game_status="ongoing",
        player_X="player1",
        player_O="player2",
    )

    # Get board string
    board_string = state.board_string

    # Check formatting
    assert "0 1 2" in board_string  # Column headers
    assert "0 |" in board_string  # Row label
    assert "1 |" in board_string
    assert "2 |" in board_string
    assert "X|" in board_string  # X symbol
    assert "O|" in board_string  # O symbol
    assert " |" in board_string  # Empty cell
