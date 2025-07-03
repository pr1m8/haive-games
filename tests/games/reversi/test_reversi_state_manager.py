"""Tests for Reversi state manager functionality."""

import pytest

from haive.games.reversi.models import ReversiMove
from haive.games.reversi.state import ReversiState
from haive.games.reversi.state_manager import ReversiStateManager


def test_get_legal_moves():
    """Test the identification of legal moves."""
    # Initialize a new game
    state = ReversiStateManager.initialize()

    # Get legal moves for Black (first player)
    legal_moves = ReversiStateManager.get_legal_moves(state)

    # In a standard Reversi starting position, Black has 4 legal moves
    assert len(legal_moves) == 4

    # Check that the legal moves are the expected ones
    expected_positions = [(2, 3), (3, 2), (4, 5), (5, 4)]
    move_positions = [(move.row, move.col) for move in legal_moves]

    for pos in expected_positions:
        assert pos in move_positions


def test_applying_move():
    """Test applying a move to the game state."""
    # Initialize a new game
    state = ReversiStateManager.initialize()

    # Create a valid move for Black
    move = ReversiMove(row=2, col=3, player="B")

    # Apply the move
    new_state = ReversiStateManager.apply_move(state, move)

    # Check that the move was applied correctly
    assert new_state.board[2][3] == "B"  # New disc placed

    # Check that appropriate discs were flipped
    assert new_state.board[3][3] == "B"  # Should be flipped from W to B

    # Check turn has switched to White
    assert new_state.turn == "W"

    # Check move history
    assert len(new_state.move_history) == 1
    assert new_state.move_history[0].row == 2
    assert new_state.move_history[0].col == 3
    assert new_state.move_history[0].player == "B"

    # Check disc count updated
    counts = new_state.disc_count
    assert counts["B"] == 4  # Was 2, added 1 new disc and flipped 1
    assert counts["W"] == 1  # Was 2, lost 1 to flipping


def test_illegal_move():
    """Test handling of illegal moves."""
    # Initialize a new game
    state = ReversiStateManager.initialize()

    # Create an illegal move (no discs flipped)
    illegal_move = ReversiMove(row=0, col=0, player="B")

    # Applying the illegal move should raise an error
    with pytest.raises(ValueError):
        ReversiStateManager.apply_move(state, illegal_move)

    # Create a move for the wrong player
    wrong_player_move = ReversiMove(row=2, col=3, player="W")  # Should be Black's turn

    # Applying the wrong player's move should raise an error
    with pytest.raises(ValueError):
        ReversiStateManager.apply_move(state, wrong_player_move)


def test_get_flips():
    """Test the calculation of which discs would be flipped by a move."""
    # Initialize a new game
    state = ReversiStateManager.initialize()

    # For the starting position, playing Black at (2,3) should flip (3,3)
    flips = ReversiStateManager._get_flips(state.board, 2, 3, "B")
    assert (3, 3) in flips
    assert len(flips) == 1

    # For the starting position, playing White at (2,3) should not flip any discs
    flips = ReversiStateManager._get_flips(state.board, 2, 3, "W")
    assert len(flips) == 0


def test_skip_move():
    """Test skipping a turn when no legal moves are available."""
    # Create a custom board where Black has no legal moves
    board = [[None for _ in range(8)] for _ in range(8)]
    # Set up a position where Black has no legal moves but White does
    board[3][3] = "W"
    board[3][4] = "W"
    board[3][5] = "W"
    board[4][3] = "B"
    board[4][4] = "B"
    board[4][5] = "B"

    state = ReversiState(board=board, turn="B", player_B="player1", player_W="player2")

    # Verify Black has no legal moves
    black_moves = ReversiStateManager.get_legal_moves(state)
    assert len(black_moves) == 0

    # Apply skip move
    new_state = ReversiStateManager.get_skip_move(state)

    # Check turn has switched to White
    assert new_state.turn == "W"

    # Check skip count increased
    assert new_state.skip_count == 1

    # Check game is still ongoing
    assert new_state.game_status == "ongoing"


def test_game_over_detection():
    """Test detection of game end conditions."""
    # Create a custom board where the game is over (full board)
    board = [["B" for _ in range(8)] for _ in range(8)]
    # Make White win by having more discs
    for i in range(4):
        for j in range(8):
            board[i][j] = "W"

    state = ReversiState(board=board, turn="B", player_B="player1", player_W="player2")

    # Check game status
    updated_state = ReversiStateManager.check_game_status(state)

    # Game should be over with White winning
    assert updated_state.game_status == "W_win"
    assert updated_state.winner == "W"

    # Test draw condition
    board = [["B" for _ in range(8)] for _ in range(8)]
    # Make equal number of discs for both players
    for i in range(4):
        for j in range(8):
            board[i][j] = "W"

    state = ReversiState(board=board, turn="B", player_B="player1", player_W="player2")

    # Check game status
    updated_state = ReversiStateManager.check_game_status(state)

    # Game should be a draw
    assert updated_state.game_status == "draw"
    assert updated_state.winner is None


def test_is_legal_move():
    """Test the is_legal_move method."""
    # Initialize a new game
    state = ReversiStateManager.initialize()

    # Check some known legal moves for Black
    assert ReversiStateManager.is_legal_move(state, 2, 3, "B") is True
    assert ReversiStateManager.is_legal_move(state, 3, 2, "B") is True

    # Check some known illegal moves for Black
    assert (
        ReversiStateManager.is_legal_move(state, 0, 0, "B") is False
    )  # No discs flipped
    assert (
        ReversiStateManager.is_legal_move(state, 3, 3, "B") is False
    )  # Cell already occupied
