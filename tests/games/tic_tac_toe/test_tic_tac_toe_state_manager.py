"""Tests for Tic Tac Toe state manager functionality."""

import pytest

from haive.games.tic_tac_toe.models import TicTacToeAnalysis, TicTacToeMove
from haive.games.tic_tac_toe.state import TicTacToeState
from haive.games.tic_tac_toe.state_manager import TicTacToeStateManager


def test_get_legal_moves():
    """Test the identification of legal moves."""
    # Initialize a new game
    state = TicTacToeStateManager.initialize()

    # Get legal moves
    legal_moves = TicTacToeStateManager.get_legal_moves(state)

    # In an empty board, all 9 positions are legal
    assert len(legal_moves) == 9

    # Check that each move has the correct player
    assert all(move.player == "X" for move in legal_moves)

    # Make a move and check legal moves again
    move = TicTacToeMove(row=1, col=1, player="X")
    new_state = TicTacToeStateManager.apply_move(state, move)

    legal_moves = TicTacToeStateManager.get_legal_moves(new_state)

    # Now there should be 8 legal moves
    assert len(legal_moves) == 8

    # Check that each move has the correct player (now O's turn)
    assert all(move.player == "O" for move in legal_moves)

    # The center position should no longer be a legal move
    assert not any(move.row == 1 and move.col == 1 for move in legal_moves)


def test_apply_move():
    """Test applying a move to the game state."""
    # Initialize a new game
    state = TicTacToeStateManager.initialize()

    # Create a valid move for X
    move = TicTacToeMove(row=0, col=0, player="X")

    # Apply the move
    new_state = TicTacToeStateManager.apply_move(state, move)

    # Check that the move was applied correctly
    assert new_state.board[0][0] == "X"

    # Check turn has switched to O
    assert new_state.turn == "O"

    # Check move history
    assert len(new_state.move_history) == 1
    assert new_state.move_history[0].row == 0
    assert new_state.move_history[0].col == 0
    assert new_state.move_history[0].player == "X"

    # Apply another move (O's turn)
    move_o = TicTacToeMove(row=1, col=1, player="O")
    newer_state = TicTacToeStateManager.apply_move(new_state, move_o)

    # Check that the move was applied correctly
    assert newer_state.board[1][1] == "O"

    # Check turn has switched back to X
    assert newer_state.turn == "X"

    # Check move history
    assert len(newer_state.move_history) == 2
    assert newer_state.move_history[1].player == "O"


def test_illegal_move():
    """Test handling of illegal moves."""
    # Initialize a new game
    state = TicTacToeStateManager.initialize()

    # Make a move
    move = TicTacToeMove(row=0, col=0, player="X")
    new_state = TicTacToeStateManager.apply_move(state, move)

    # Try to move to an occupied cell
    illegal_move = TicTacToeMove(row=0, col=0, player="O")

    # Applying the illegal move should raise an error
    with pytest.raises(ValueError):
        TicTacToeStateManager.apply_move(new_state, illegal_move)

    # Try to move out of turn
    wrong_turn_move = TicTacToeMove(row=1, col=1, player="X")  # Should be O's turn

    # Applying the wrong turn move should raise an error
    with pytest.raises(ValueError):
        TicTacToeStateManager.apply_move(new_state, wrong_turn_move)


def test_check_game_status_win():
    """Test win detection in various patterns."""
    # Helper function to create a board with specific moves
    def make_board_with_moves(moves):
        state = TicTacToeStateManager.initialize()
        for move in moves:
            state = TicTacToeStateManager.apply_move(state, move)
        return state

    # Test horizontal win
    horizontal_win_moves = [
        TicTacToeMove(row=0, col=0, player="X"),
        TicTacToeMove(row=1, col=0, player="O"),
        TicTacToeMove(row=0, col=1, player="X"),
        TicTacToeMove(row=1, col=1, player="O"),
        TicTacToeMove(row=0, col=2, player="X"),
    ]
    state = make_board_with_moves(horizontal_win_moves)

    # Check game status
    state = TicTacToeStateManager.check_game_status(state)
    assert state.game_status == "X_win"
    assert state.winner == "X"

    # Test vertical win
    vertical_win_moves = [
        TicTacToeMove(row=0, col=0, player="X"),
        TicTacToeMove(row=0, col=1, player="O"),
        TicTacToeMove(row=1, col=0, player="X"),
        TicTacToeMove(row=1, col=1, player="O"),
        TicTacToeMove(row=2, col=0, player="X"),
    ]
    state = make_board_with_moves(vertical_win_moves)

    # Check game status
    state = TicTacToeStateManager.check_game_status(state)
    assert state.game_status == "X_win"
    assert state.winner == "X"

    # Test diagonal win (top-left to bottom-right)
    diagonal1_win_moves = [
        TicTacToeMove(row=0, col=0, player="X"),
        TicTacToeMove(row=0, col=1, player="O"),
        TicTacToeMove(row=1, col=1, player="X"),
        TicTacToeMove(row=0, col=2, player="O"),
        TicTacToeMove(row=2, col=2, player="X"),
    ]
    state = make_board_with_moves(diagonal1_win_moves)

    # Check game status
    state = TicTacToeStateManager.check_game_status(state)
    assert state.game_status == "X_win"
    assert state.winner == "X"

    # Test diagonal win (top-right to bottom-left)
    diagonal2_win_moves = [
        TicTacToeMove(row=0, col=2, player="X"),
        TicTacToeMove(row=0, col=0, player="O"),
        TicTacToeMove(row=1, col=1, player="X"),
        TicTacToeMove(row=1, col=0, player="O"),
        TicTacToeMove(row=2, col=0, player="X"),
    ]
    state = make_board_with_moves(diagonal2_win_moves)

    # Check game status
    state = TicTacToeStateManager.check_game_status(state)
    assert state.game_status == "X_win"
    assert state.winner == "X"


def test_check_game_status_draw():
    """Test draw detection when board is full with no winner."""
    # Create a board with a draw
    draw_board = [["X", "O", "X"], ["X", "O", "O"], ["O", "X", "X"]]
    state = TicTacToeState(
        board=draw_board,
        turn="X",
        game_status="ongoing",
        player_X="player1",
        player_O="player2",
    )

    # Check game status
    state = TicTacToeStateManager.check_game_status(state)
    assert state.game_status == "draw"
    assert state.winner is None


def test_find_winning_move():
    """Test the ability to find winning moves."""
    # Create a board where X has a winning move
    board = [["X", "X", None], ["O", "O", None], [None, None, None]]
    state = TicTacToeState(
        board=board,
        turn="X",
        game_status="ongoing",
        player_X="player1",
        player_O="player2",
    )

    # Find winning move for X
    winning_moves = TicTacToeStateManager.find_winning_move(state, "X")
    assert len(winning_moves) == 1
    assert winning_moves[0] == (0, 2)  # Completes top row

    # Create a board where O has a winning move
    board = [["X", None, "X"], ["O", "O", None], ["X", None, None]]
    state = TicTacToeState(
        board=board,
        turn="O",
        game_status="ongoing",
        player_X="player1",
        player_O="player2",
    )

    # Find winning move for O
    winning_moves = TicTacToeStateManager.find_winning_move(state, "O")
    assert len(winning_moves) == 1
    assert winning_moves[0] == (1, 2)  # Completes middle row

    # Create a board with multiple winning moves
    board = [["X", "X", None], [None, "X", None], [None, None, "X"]]
    state = TicTacToeState(
        board=board,
        turn="X",
        game_status="ongoing",
        player_X="player1",
        player_O="player2",
    )

    # Find winning moves for X
    winning_moves = TicTacToeStateManager.find_winning_move(state, "X")
    assert len(winning_moves) == 2
    assert (0, 2) in winning_moves  # Completes top row
    assert (1, 0) in winning_moves  # Completes diagonal


def test_add_analysis():
    """Test adding analysis to the game state."""
    # Create a state
    state = TicTacToeStateManager.initialize()

    # Create an analysis
    analysis = TicTacToeAnalysis(
        winning_moves=[],
        blocking_moves=[],
        fork_opportunities=[{"row": 1, "col": 1}],
        center_available=True,
        corner_available=True,
        position_evaluation="unclear",
        recommended_move={"row": 1, "col": 1},
        strategy="Take the center for best strategic position",
    )

    # Add analysis for player1
    new_state = TicTacToeStateManager.add_analysis(state, "player1", analysis)
    assert len(new_state.player1_analysis) == 1
    assert new_state.player1_analysis[0] == analysis

    # Add analysis for player2
    new_state = TicTacToeStateManager.add_analysis(state, "player2", analysis)
    assert len(new_state.player2_analysis) == 1
    assert new_state.player2_analysis[0] == analysis
